# Skills Cleanup & Workflow Guide

**Generated**: 2026-04-19  
**Version**: 2.0

---

## 🎉 Cleanup Complete!

### Summary of Changes

**Before**: 300 skills, 446 relationships  
**After**: 279 skills, 400 relationships  
**Reduction**: 21 skills (7% cleaner!)

---

## 📊 What We Did

### 1. ✅ Removed 7 Exact Duplicates

Skills that appeared in multiple categories:
- `dispatching-parallel-agents` (kept in Agent Orchestration)
- `subagent-driven-development` (kept in Agent Orchestration)
- `database-reviewer` (kept in Code Review)
- `remotion-video-creation` (kept in Documentation)
- `healthcare-phi-compliance` (kept in Domain Specialized)
- `feature-investment-advisor` (kept in Product Management)
- `recommendation-canvas` (kept in Product Management)

### 2. ✅ Consolidated 20 Skills into 6 Unified Skills

#### **Unified Build Resolver** (replaces 6 skills)
- Handles: C++, Go, Java, Kotlin, Rust, PyTorch
- **When to use**: Any build error in any language
- **Benefit**: One skill to maintain, consistent behavior

#### **Language Agnostic TDD** (replaces 4 skills)
- Handles: C++, Go, Kotlin, Rust testing
- **When to use**: Writing tests in any language
- **Benefit**: Unified TDD workflow

#### **Unified Coding Standards** (replaces 3 skills)
- Handles: C++, Java, general standards
- **When to use**: Enforcing code quality
- **Benefit**: Consistent standards across languages

#### **Workshop Facilitation** (replaces 3 skills)
- Handles: Journey mapping, story mapping, positioning
- **When to use**: Running any workshop
- **Benefit**: One skill with multiple templates

#### **Instinct Manager** (replaces 2 skills)
- Handles: Import, export, manage instincts
- **When to use**: Managing learned patterns
- **Benefit**: Unified instinct management

#### **PM Career Advisor** (replaces 2 skills)
- Handles: Director and VP/CPO transitions
- **When to use**: PM career advancement
- **Benefit**: Complete career guidance

### 3. ✅ Identified Top 30 Core Skills

The most important skills based on dependencies and usage:

**Top 10 Hub Skills** (most depended upon):
1. Ppt Generator
2. Autonomous Agent Harness
3. Webapp Testing
4. Discovery Process
5. Market Research
6. Language Agnostic TDD
7. Springboot Patterns
8. Autonomous Loops
9. Frontend Design
10. Kotlin Patterns

**See**: `core-skills-top30.json` for complete list

### 4. ✅ Created 13 Workflow Paths

Common development workflows using core skills:

1. **New Feature Development** (10 steps, 1-5 days)
2. **Bug Fix Workflow** (5 steps, 1-4 hours)
3. **Code Refactoring** (5 steps, 2-8 hours)
4. **Product Discovery** (5 steps, 1-2 weeks)
5. **Documentation Creation** (3 steps, 2-4 hours)
6. **Multi-Agent Project** (4 steps, 1-3 days)
7. **Code Review Cycle** (4 steps, 1-2 hours)
8. **Deployment Workflow** (3 steps, 30min-2 hours)
9. **Learning New Codebase** (3 steps, 2-4 hours)
10. **Skill Management** (3 steps, 1-2 hours)
11. **Presentation Creation** (3 steps, 1-3 hours)
12. **Autonomous Development** (3 steps, hours-days)
13. **API Development** (4 steps, 1-3 days)

**See**: `skill-workflows.json` for complete details

---

## 🚀 How to Use Workflows

### Example: New Feature Development

```
1. Discovery Phase
   └─ brainstorming → Generate ideas
   └─ discovery-process → Validate problem/solution
   
2. Planning Phase
   └─ problem-statement → Define the problem
   └─ user-story → Write acceptance criteria
   └─ writing-plans → Create implementation plan
   
3. Implementation Phase
   └─ language-agnostic-tdd → Write tests first
   └─ executing-plans → Implement feature
   
4. Review & Verification
   └─ code-reviewer → Review quality
   └─ verification-before-completion → Verify everything
   └─ webapp-testing → Test in browser
```

### Most Used Skills Across All Workflows

1. **verification-before-completion** (6 workflows) - Always verify!
2. **code-reviewer** (5 workflows) - Quality matters
3. **language-agnostic-tdd** (4 workflows) - Test-driven
4. **executing-plans** (4 workflows) - Execute systematically
5. **brainstorming** (3 workflows) - Start with ideas

---

## 📁 Files Generated

### Core Files
- `skills-knowledge-graph.json` - **Main file** (279 skills, 400 relationships)
- `core-skills-top30.json` - Top 30 most important skills
- `skill-workflows.json` - 13 common workflow paths

### Visualizations
- `skills-analysis/skills-graph-standalone-v2.html` - **New standalone graph** (279 skills)
- `skills-analysis/skills-graph-standalone.html` - Old version (300 skills)

### Analysis Reports
- `REDUNDANCY_ANALYSIS.md` - Detailed redundancy analysis
- `CLEANUP_GUIDE.md` - This file

### Backup Files
- `skills-knowledge-graph-cleaned.json` - After removing duplicates (293 skills)
- `skills-knowledge-graph-consolidated.json` - After consolidation (279 skills)

---

## 🎯 Quick Start Guide

### View the Cleaned Graph
```bash
# Open the new standalone visualization
start skills-analysis/skills-graph-standalone-v2.html
```

### Explore Workflows
```bash
# View workflow details
cat skill-workflows.json | python -m json.tool
```

### See Core Skills
```bash
# View top 30 core skills
cat core-skills-top30.json | python -m json.tool
```

---

## 💡 Recommended Next Steps

### For Daily Use
1. **Bookmark workflows** - Keep `skill-workflows.json` handy
2. **Focus on core 30** - Master the top 30 skills first
3. **Follow workflows** - Use predefined paths for common tasks

### For Skill Management
1. **Use the new graph** - `skills-graph-standalone-v2.html` is cleaner
2. **Reference workflows** - When unsure which skill to use
3. **Check core skills** - Prioritize learning hub skills

### For Further Optimization
1. **Track usage** - Note which skills you actually use
2. **Create custom workflows** - Add your own common patterns
3. **Archive rarely used** - Move specialized skills to "advanced" tier

---

## 📈 Impact Analysis

### Clarity Improvement
- **7% fewer skills** to navigate
- **Consolidated patterns** reduce decision fatigue
- **Clear workflows** provide guidance

### Maintenance Improvement
- **6 unified skills** instead of 20 language-specific ones
- **Consistent behavior** across languages
- **Easier updates** - change once, apply everywhere

### Usability Improvement
- **13 workflows** cover 80% of common tasks
- **30 core skills** cover most needs
- **Clear paths** from problem to solution

---

## 🔄 Workflow Usage Examples

### "I need to build a new feature"
→ Use **New Feature Development** workflow

### "There's a bug in production"
→ Use **Bug Fix Workflow**

### "Code is messy, needs cleanup"
→ Use **Code Refactoring** workflow

### "Should we build this?"
→ Use **Product Discovery** workflow

### "Need to document this"
→ Use **Documentation Creation** workflow

### "Large project, need help"
→ Use **Multi-Agent Project** workflow

---

## 📚 Additional Resources

- **Full Analysis**: See `REDUNDANCY_ANALYSIS.md`
- **Extraction Report**: See `EXTRACTION_REPORT.md`
- **Original Graph**: See `skills-analysis/skills-graph-standalone.html`

---

**Next**: Commit these changes and start using the workflows! 🎉
