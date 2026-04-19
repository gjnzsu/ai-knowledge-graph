# Skills Redundancy Analysis Report

**Generated**: 2026-04-19  
**Total Skills Analyzed**: 300  
**Issues Found**: 80+ redundancies and overlaps

---

## 🔴 Critical Issues: Exact Duplicates (7 skills)

These skills appear in multiple categories with identical names and purposes. **Action: Consolidate immediately.**

### 1. **dispatching-parallel-agents**
- **Appears in**: Agent Orchestration, Core Superpowers
- **Recommendation**: Keep in Agent Orchestration (more specific), remove from Core Superpowers
- **Impact**: Reduces confusion about which to use

### 2. **subagent-driven-development**
- **Appears in**: Agent Orchestration, Core Superpowers
- **Recommendation**: Keep in Agent Orchestration, remove from Core Superpowers
- **Impact**: Clear ownership in agent-specific category

### 3. **database-reviewer**
- **Appears in**: Code Review, Infrastructure and DevOps
- **Recommendation**: Keep in Code Review (it's a reviewer), remove from Infrastructure
- **Impact**: Aligns with other reviewer skills

### 4. **remotion-video-creation**
- **Appears in**: Documentation and Content, Framework and Language Patterns
- **Recommendation**: Keep in Documentation and Content (it's about creating content), remove from Framework
- **Impact**: Better categorization

### 5. **healthcare-phi-compliance**
- **Appears in**: Domain Specialized, Infrastructure and DevOps
- **Recommendation**: Keep in Domain Specialized (healthcare-specific), remove from Infrastructure
- **Impact**: Domain expertise stays together

### 6. **feature-investment-advisor**
- **Appears in**: Financial and Business, Product Management
- **Recommendation**: Keep in Product Management (it's about feature decisions), remove from Financial
- **Impact**: Product decisions stay with product skills

### 7. **recommendation-canvas**
- **Appears in**: Financial and Business, Product Management
- **Recommendation**: Keep in Product Management (it's a PM framework), remove from Financial
- **Impact**: Framework stays with its primary domain

---

## 🟡 High Priority: Near-Duplicates (24 skills)

Skills with >80% name similarity - likely serving the same purpose.

### Language-Specific Build Resolvers (Consolidation Opportunity)
**Pattern**: `{language}-build-resolver` - all do the same thing for different languages

- cpp-build-resolver (C++)
- go-build-resolver (Go)
- java-build-resolver (Java)
- kotlin-build-resolver (Kotlin)
- rust-build-resolver (Rust)
- pytorch-build-resolver (PyTorch)

**Recommendation**: Create a **unified-build-resolver** skill that handles all languages
- **Benefit**: Single skill to maintain, consistent behavior
- **Implementation**: Detect language from project files, apply language-specific fixes
- **Savings**: 6 skills → 1 skill

### Language-Specific Test Skills (Consolidation Opportunity)
**Pattern**: `{language}-test` - all enforce TDD for different languages

- cpp-test (C++)
- go-test (Go)
- kotlin-test (Kotlin)
- rust-test (Rust)

**Recommendation**: Create a **language-agnostic-tdd** skill
- **Benefit**: Unified TDD workflow across all languages
- **Implementation**: Detect language, apply appropriate test framework
- **Savings**: 4 skills → 1 skill

### Coding Standards (3 skills doing the same thing)
- cpp-coding-standards
- java-coding-standards
- coding-standards (general)

**Recommendation**: Merge into single **coding-standards** skill with language-specific sections
- **Savings**: 3 skills → 1 skill

### Continuous Learning (2 versions)
- continuous-learning
- continuous-learning-v2

**Recommendation**: Deprecate v1, keep only v2 (instinct-based system)
- **Savings**: 2 skills → 1 skill

### Code Review Pairs
- requesting-code-review
- receiving-code-review

**Recommendation**: Keep separate (different workflows), but ensure they reference each other

### Instinct Management
- instinct-export
- instinct-import

**Recommendation**: Merge into single **instinct-manager** skill
- **Savings**: 2 skills → 1 skill

---

## 🟠 Medium Priority: Overlapping Domains (45 skills)

Skills in the same category with 60-95% similar purposes.

### Pattern-Based Overlaps

#### 1. **Language Patterns** (highly similar)
All follow pattern: "Idiomatic {language} patterns, best practices, and conventions"

- golang-patterns (94.6% similar to kotlin-patterns)
- kotlin-patterns
- python-patterns (83.9% similar to pytorch-patterns)
- rust-patterns
- perl-patterns

**Recommendation**: Keep separate (language-specific knowledge is valuable)
- **But**: Create a template/framework they all follow for consistency

#### 2. **Security Skills** (91.5% similar)
- laravel-security
- springboot-security
- django-security

**Recommendation**: Extract common security patterns into **web-security-patterns** skill
- Keep framework-specific skills for unique features
- Reference the common patterns skill

#### 3. **Workshop Skills** (88.3% similar)
- customer-journey-mapping-workshop
- user-story-mapping-workshop
- positioning-workshop
- workshop-facilitation (general)

**Recommendation**: Consolidate into **workshop-facilitation** with specific templates
- **Savings**: 3 skills → 1 skill with templates

#### 4. **Career Transition Skills** (81.1% similar)
- director-readiness-advisor
- vp-cpo-readiness-advisor

**Recommendation**: Merge into **pm-career-advisor** with level-specific guidance
- **Savings**: 2 skills → 1 skill

#### 5. **Database Skills** (84.7% similar)
- postgres-patterns
- database-reviewer

**Recommendation**: Keep separate (one is patterns, one is review)
- **But**: Ensure they reference each other

---

## 📊 Consolidation Impact Summary

### Immediate Wins (Exact Duplicates)
- **Remove**: 7 duplicate skills
- **Effort**: Low (just delete)
- **Impact**: High (eliminates confusion)

### High-Value Consolidations
| Current | Proposed | Savings |
|---------|----------|---------|
| 6 build resolvers | 1 unified-build-resolver | 5 skills |
| 4 test skills | 1 language-agnostic-tdd | 3 skills |
| 3 coding standards | 1 coding-standards | 2 skills |
| 3 workshop skills | 1 workshop-facilitation | 2 skills |
| 2 continuous learning | 1 continuous-learning-v2 | 1 skill |
| 2 instinct skills | 1 instinct-manager | 1 skill |
| 2 career skills | 1 pm-career-advisor | 1 skill |

**Total Potential Savings**: 7 (duplicates) + 15 (consolidations) = **22 skills**

### After Cleanup
- **Current**: 300 skills
- **After cleanup**: ~278 skills
- **Reduction**: 7.3%
- **Benefit**: Clearer, easier to navigate, less maintenance

---

## 🎯 Recommended Action Plan

### Phase 1: Quick Wins (1-2 hours)
1. Remove 7 exact duplicates
2. Update references in related skills
3. Test that nothing breaks

### Phase 2: High-Value Consolidations (1 day)
1. Create unified-build-resolver
2. Create language-agnostic-tdd
3. Merge coding standards
4. Consolidate workshop skills
5. Deprecate continuous-learning v1

### Phase 3: Documentation (2 hours)
1. Update skill graph visualization
2. Document consolidation decisions
3. Create migration guide for users

### Phase 4: Pattern Extraction (optional, 1 day)
1. Extract common security patterns
2. Create skill templates for consistency
3. Document best practices

---

## 🔍 Skills That Should Stay Separate

Despite similarities, these should remain separate:

1. **Language-specific patterns** - Each language has unique idioms
2. **Framework-specific security** - Each has unique vulnerabilities
3. **Requesting vs Receiving code review** - Different workflows
4. **Healthcare EMR vs CDSS** - Different systems, different regulations

---

## 📈 Next Steps

Would you like me to:
1. **Generate the cleanup script** to remove duplicates automatically?
2. **Create consolidated skills** (unified-build-resolver, etc.)?
3. **Update the knowledge graph** with the cleaned-up skills?
4. **Create a migration guide** for users of deprecated skills?

Let me know which phase you'd like to tackle first!
