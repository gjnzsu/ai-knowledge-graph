import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load core skills and consolidated data
with open('core-skills-top30.json', 'r', encoding='utf-8') as f:
    core_data = json.load(f)

with open('skills-knowledge-graph-consolidated.json', 'r', encoding='utf-8') as f:
    graph_data = json.load(f)

core_skills = {s['id']: s for s in core_data['core_skills']}
all_skills = {s['id']: s for s in graph_data['skills']}

print("=" * 80)
print("STEP 4: CREATING WORKFLOW PATHS")
print("=" * 80)

# Define common workflows using core and essential skills
workflows = [
    {
        'id': 'new-feature',
        'name': 'New Feature Development',
        'description': 'Complete workflow for building a new feature from idea to production',
        'steps': [
            {'skill': 'brainstorming', 'phase': 'Discovery', 'description': 'Generate and explore feature ideas'},
            {'skill': 'discovery-process', 'phase': 'Discovery', 'description': 'Validate problem and solution fit'},
            {'skill': 'problem-statement', 'phase': 'Planning', 'description': 'Define the problem clearly'},
            {'skill': 'user-story', 'phase': 'Planning', 'description': 'Write user stories with acceptance criteria'},
            {'skill': 'writing-plans', 'phase': 'Planning', 'description': 'Create implementation plan'},
            {'skill': 'language-agnostic-tdd', 'phase': 'Implementation', 'description': 'Write tests first'},
            {'skill': 'executing-plans', 'phase': 'Implementation', 'description': 'Implement the feature'},
            {'skill': 'code-reviewer', 'phase': 'Review', 'description': 'Review code quality'},
            {'skill': 'verification-before-completion', 'phase': 'Verification', 'description': 'Verify everything works'},
            {'skill': 'webapp-testing', 'phase': 'Testing', 'description': 'Test in browser'},
        ],
        'when_to_use': 'When building any new feature from scratch',
        'estimated_time': '1-5 days depending on complexity'
    },
    {
        'id': 'bug-fix',
        'name': 'Bug Fix Workflow',
        'description': 'Systematic approach to fixing bugs',
        'steps': [
            {'skill': 'systematic-debugging', 'phase': 'Investigation', 'description': 'Identify root cause'},
            {'skill': 'language-agnostic-tdd', 'phase': 'Testing', 'description': 'Write failing test first'},
            {'skill': 'executing-plans', 'phase': 'Implementation', 'description': 'Fix the bug'},
            {'skill': 'verification-before-completion', 'phase': 'Verification', 'description': 'Verify fix works'},
            {'skill': 'code-reviewer', 'phase': 'Review', 'description': 'Review the fix'},
        ],
        'when_to_use': 'When fixing any bug or unexpected behavior',
        'estimated_time': '1-4 hours'
    },
    {
        'id': 'refactoring',
        'name': 'Code Refactoring',
        'description': 'Safe refactoring with test coverage',
        'steps': [
            {'skill': 'code-reviewer', 'phase': 'Analysis', 'description': 'Identify code smells'},
            {'skill': 'language-agnostic-tdd', 'phase': 'Safety Net', 'description': 'Ensure test coverage'},
            {'skill': 'writing-plans', 'phase': 'Planning', 'description': 'Plan refactoring approach'},
            {'skill': 'executing-plans', 'phase': 'Implementation', 'description': 'Refactor incrementally'},
            {'skill': 'verification-before-completion', 'phase': 'Verification', 'description': 'Verify no regressions'},
        ],
        'when_to_use': 'When improving code quality without changing behavior',
        'estimated_time': '2-8 hours'
    },
    {
        'id': 'product-discovery',
        'name': 'Product Discovery',
        'description': 'Validate product ideas before building',
        'steps': [
            {'skill': 'market-research', 'phase': 'Research', 'description': 'Understand market and competition'},
            {'skill': 'discovery-process', 'phase': 'Discovery', 'description': 'Run discovery interviews'},
            {'skill': 'problem-statement', 'phase': 'Definition', 'description': 'Define the problem'},
            {'skill': 'brainstorming', 'phase': 'Ideation', 'description': 'Generate solution ideas'},
            {'skill': 'user-story', 'phase': 'Documentation', 'description': 'Document as user stories'},
        ],
        'when_to_use': 'Before building any new product or major feature',
        'estimated_time': '1-2 weeks'
    },
    {
        'id': 'documentation',
        'name': 'Documentation Creation',
        'description': 'Create comprehensive documentation',
        'steps': [
            {'skill': 'doc-coauthoring', 'phase': 'Writing', 'description': 'Write documentation'},
            {'skill': 'drawio', 'phase': 'Diagrams', 'description': 'Create diagrams'},
            {'skill': 'pptx', 'phase': 'Presentations', 'description': 'Create presentations'},
        ],
        'when_to_use': 'When documenting features, architecture, or processes',
        'estimated_time': '2-4 hours'
    },
    {
        'id': 'multi-agent-project',
        'name': 'Multi-Agent Project',
        'description': 'Coordinate multiple agents for complex projects',
        'steps': [
            {'skill': 'writing-plans', 'phase': 'Planning', 'description': 'Create detailed plan'},
            {'skill': 'team', 'phase': 'Setup', 'description': 'Create agent team'},
            {'skill': 'dispatching-parallel-agents', 'phase': 'Execution', 'description': 'Dispatch parallel work'},
            {'skill': 'verification-before-completion', 'phase': 'Verification', 'description': 'Verify all work'},
        ],
        'when_to_use': 'For large projects with independent parallel tasks',
        'estimated_time': '1-3 days'
    },
    {
        'id': 'code-review-cycle',
        'name': 'Code Review Cycle',
        'description': 'Complete code review workflow',
        'steps': [
            {'skill': 'requesting-code-review', 'phase': 'Request', 'description': 'Prepare and request review'},
            {'skill': 'code-reviewer', 'phase': 'Review', 'description': 'Perform code review'},
            {'skill': 'receiving-code-review', 'phase': 'Response', 'description': 'Address feedback'},
            {'skill': 'verification-before-completion', 'phase': 'Verification', 'description': 'Verify changes'},
        ],
        'when_to_use': 'Before merging any significant code changes',
        'estimated_time': '1-2 hours'
    },
    {
        'id': 'deployment',
        'name': 'Deployment Workflow',
        'description': 'Safe deployment to production',
        'steps': [
            {'skill': 'verification-before-completion', 'phase': 'Pre-Deploy', 'description': 'Verify everything passes'},
            {'skill': 'finishing-a-development-branch', 'phase': 'Merge', 'description': 'Merge to main'},
            {'skill': 'webapp-testing', 'phase': 'Post-Deploy', 'description': 'Test in production'},
        ],
        'when_to_use': 'When deploying code to production',
        'estimated_time': '30 minutes - 2 hours'
    },
    {
        'id': 'learning-new-codebase',
        'name': 'Learning New Codebase',
        'description': 'Efficiently understand unfamiliar code',
        'steps': [
            {'skill': 'codebase-onboarding', 'phase': 'Overview', 'description': 'Generate onboarding guide'},
            {'skill': 'graphify', 'phase': 'Visualization', 'description': 'Create knowledge graph'},
            {'skill': 'code-reviewer', 'phase': 'Analysis', 'description': 'Review code patterns'},
        ],
        'when_to_use': 'When joining a new project or exploring unfamiliar code',
        'estimated_time': '2-4 hours'
    },
    {
        'id': 'skill-management',
        'name': 'Skill Management',
        'description': 'Manage and organize your skills',
        'steps': [
            {'skill': 'skill-stocktake', 'phase': 'Audit', 'description': 'Audit existing skills'},
            {'skill': 'skill-creator', 'phase': 'Creation', 'description': 'Create new skills'},
            {'skill': 'graphify', 'phase': 'Visualization', 'description': 'Visualize relationships'},
        ],
        'when_to_use': 'When organizing or creating skills',
        'estimated_time': '1-2 hours'
    },
    {
        'id': 'presentation-creation',
        'name': 'Presentation Creation',
        'description': 'Create professional presentations',
        'steps': [
            {'skill': 'brainstorming', 'phase': 'Content', 'description': 'Brainstorm content'},
            {'skill': 'ppt-generator', 'phase': 'Generation', 'description': 'Generate slides'},
            {'skill': 'frontend-design', 'phase': 'Design', 'description': 'Apply design principles'},
        ],
        'when_to_use': 'When creating presentations or pitch decks',
        'estimated_time': '1-3 hours'
    },
    {
        'id': 'autonomous-development',
        'name': 'Autonomous Development',
        'description': 'Set up autonomous agent loops',
        'steps': [
            {'skill': 'autonomous-agent-harness', 'phase': 'Setup', 'description': 'Configure agent harness'},
            {'skill': 'autonomous-loops', 'phase': 'Execution', 'description': 'Run autonomous loops'},
            {'skill': 'eval-harness', 'phase': 'Evaluation', 'description': 'Evaluate results'},
        ],
        'when_to_use': 'For long-running autonomous development tasks',
        'estimated_time': 'Hours to days'
    },
    {
        'id': 'api-development',
        'name': 'API Development',
        'description': 'Build and test APIs',
        'steps': [
            {'skill': 'backend-patterns', 'phase': 'Design', 'description': 'Design API architecture'},
            {'skill': 'language-agnostic-tdd', 'phase': 'Testing', 'description': 'Write API tests'},
            {'skill': 'executing-plans', 'phase': 'Implementation', 'description': 'Implement endpoints'},
            {'skill': 'e2e-testing', 'phase': 'Testing', 'description': 'Test end-to-end'},
        ],
        'when_to_use': 'When building REST APIs or backend services',
        'estimated_time': '1-3 days'
    },
]

print(f"\nCreated {len(workflows)} workflow paths:")
print("-" * 80)

for i, workflow in enumerate(workflows, 1):
    print(f"\n{i}. {workflow['name']}")
    print(f"   {workflow['description']}")
    print(f"   Steps: {len(workflow['steps'])}")
    print(f"   When: {workflow['when_to_use']}")
    print(f"   Time: {workflow['estimated_time']}")

# Save workflows
workflows_data = {
    'generated_at': '2026-04-19',
    'total_workflows': len(workflows),
    'description': 'Common development workflows using core skills',
    'workflows': workflows
}

with open('skill-workflows.json', 'w', encoding='utf-8') as f:
    json.dump(workflows_data, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print("WORKFLOW STATISTICS")
print("=" * 80)

# Analyze workflow coverage
all_workflow_skills = set()
for workflow in workflows:
    for step in workflow['steps']:
        all_workflow_skills.add(step['skill'])

print(f"Total workflows: {len(workflows)}")
print(f"Unique skills used: {len(all_workflow_skills)}")
print(f"Average steps per workflow: {sum(len(w['steps']) for w in workflows) / len(workflows):.1f}")

# Most used skills in workflows
skill_usage = {}
for workflow in workflows:
    for step in workflow['steps']:
        skill_usage[step['skill']] = skill_usage.get(step['skill'], 0) + 1

print("\nMost used skills in workflows:")
for skill, count in sorted(skill_usage.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  {skill:<40} (used in {count} workflows)")

print(f"\n[SUCCESS] Saved to: skill-workflows.json")
