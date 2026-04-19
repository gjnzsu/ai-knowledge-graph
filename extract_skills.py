#!/usr/bin/env python3
"""
Extract all skills from markdown files and create a comprehensive knowledge graph JSON.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set

def parse_skill_section(content: str, category: str, source_file: str) -> Dict:
    """Parse a skill section and extract metadata."""
    lines = content.strip().split('\n')

    skill = {
        "id": "",
        "name": "",
        "purpose": "",
        "when_to_use": "",
        "dependencies": [],
        "invokes": [],
        "related": [],
        "category": category,
        "source_file": source_file
    }

    # Extract skill ID from header (### skill-name)
    header_match = re.match(r'^###\s+(.+)$', lines[0])
    if header_match:
        skill["id"] = header_match.group(1).strip()
        skill["name"] = skill["id"].replace('-', ' ').title()

    # Parse fields
    for line in lines[1:]:
        if line.startswith('**Purpose**:'):
            skill["purpose"] = line.replace('**Purpose**:', '').strip()
        elif line.startswith('**When to use**:'):
            skill["when_to_use"] = line.replace('**When to use**:', '').strip()
        elif line.startswith('**Dependencies**:'):
            deps_text = line.replace('**Dependencies**:', '').strip()
            if deps_text and deps_text.lower() != 'none':
                skill["dependencies"] = [d.strip() for d in deps_text.split(',')]
        elif line.startswith('**Invokes**:'):
            invokes_text = line.replace('**Invokes**:', '').strip()
            if invokes_text and invokes_text.lower() != 'none':
                skill["invokes"] = [i.strip() for i in invokes_text.split(',')]
        elif line.startswith('**Related**:'):
            related_text = line.replace('**Related**:', '').strip()
            if related_text and related_text.lower() != 'none':
                skill["related"] = [r.strip() for r in related_text.split(',')]
        elif line.startswith('**Domain**:'):
            skill["domain"] = line.replace('**Domain**:', '').strip()

    return skill

def extract_skills_from_file(file_path: Path) -> List[Dict]:
    """Extract all skills from a markdown file."""
    content = file_path.read_text(encoding='utf-8')

    # Determine category from filename
    category_map = {
        'build-testing-skills.md': 'Build and Testing',
        'product-management-skills.md': 'Product Management',
        'documentation-content-design.md': 'Documentation and Content',
        'infrastructure-devops-database.md': 'Infrastructure and DevOps',
        'domain-specialized-skills.md': 'Domain Specialized',
        'core-superpowers.md': 'Core Superpowers',
        'agent-orchestration-skills.md': 'Agent Orchestration',
        'code-review-skills.md': 'Code Review',
        'framework-language-patterns.md': 'Framework and Language Patterns',
        'financial-business-skills.md': 'Financial and Business'
    }

    category = category_map.get(file_path.name, 'Other')

    # Split by ### headers (skill sections)
    sections = re.split(r'\n(?=###\s+[a-z])', content)

    skills = []
    for section in sections:
        if section.strip() and section.startswith('###'):
            try:
                skill = parse_skill_section(section, category, file_path.name)
                if skill["id"]:
                    skills.append(skill)
            except Exception as e:
                print(f"Error parsing section in {file_path.name}: {e}")

    return skills

def create_relationships(skills: List[Dict]) -> List[Dict]:
    """Create relationship edges from skill metadata."""
    relationships = []
    skill_ids = {s["id"] for s in skills}

    for skill in skills:
        source = skill["id"]

        # Dependencies relationships
        for dep in skill.get("dependencies", []):
            if dep in skill_ids:
                relationships.append({
                    "source": source,
                    "target": dep,
                    "type": "depends_on",
                    "confidence": 1.0
                })

        # Invokes relationships
        for inv in skill.get("invokes", []):
            # Clean up invokes (might be tool names)
            inv_clean = inv.lower().replace(' ', '-')
            if inv_clean in skill_ids:
                relationships.append({
                    "source": source,
                    "target": inv_clean,
                    "type": "invokes",
                    "confidence": 1.0
                })

        # Related relationships
        for rel in skill.get("related", []):
            if rel in skill_ids:
                relationships.append({
                    "source": source,
                    "target": rel,
                    "type": "related_to",
                    "confidence": 0.8
                })

    return relationships

def main():
    """Main extraction function."""
    skills_dir = Path(__file__).parent / 'skills-analysis'

    if not skills_dir.exists():
        print(f"Skills directory not found: {skills_dir}")
        return

    all_skills = []
    source_files = []

    # Process each markdown file
    for md_file in sorted(skills_dir.glob('*.md')):
        if md_file.name == 'GRAPH_REPORT.md':
            continue

        print(f"Processing {md_file.name}...")
        skills = extract_skills_from_file(md_file)
        all_skills.extend(skills)
        source_files.append(md_file.name)
        print(f"  Found {len(skills)} skills")

    # Create relationships
    print("\nCreating relationships...")
    relationships = create_relationships(all_skills)

    # Build final JSON structure
    output = {
        "metadata": {
            "generated_at": "2026-04-19",
            "total_skills": len(all_skills),
            "total_relationships": len(relationships),
            "source_files": source_files,
            "categories": list(set(s["category"] for s in all_skills))
        },
        "skills": all_skills,
        "relationships": relationships
    }

    # Write output
    output_file = Path(__file__).parent / 'skills-knowledge-graph.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Extracted {len(all_skills)} skills")
    print(f"[OK] Created {len(relationships)} relationships")
    print(f"[OK] Output written to {output_file}")

    # Print category breakdown
    print("\nSkills by category:")
    category_counts = {}
    for skill in all_skills:
        cat = skill["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat, count in sorted(category_counts.items()):
        print(f"  {cat}: {count}")

if __name__ == '__main__':
    main()
