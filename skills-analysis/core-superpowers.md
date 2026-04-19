# Core Superpowers Skills

## Overview
Foundation skills that establish workflows and best practices across all development tasks.

## Skills

### brainstorming
**Purpose**: Creative work and feature planning
**When to use**: MUST use before any creative work - creating features, building components
**Dependencies**: None (entry point skill)
**Invokes**: May lead to writing-plans or executing-plans

### writing-plans
**Purpose**: Create implementation plans from specs
**When to use**: When you have a spec or requirements for a multi-step task, before touching code
**Dependencies**: Often follows brainstorming
**Invokes**: Leads to executing-plans or subagent-driven-development

### executing-plans
**Purpose**: Execute written implementation plans
**When to use**: When you have a written implementation plan to execute in a separate session
**Dependencies**: Requires a plan from writing-plans
**Related**: subagent-driven-development (parallel execution variant)

### systematic-debugging
**Purpose**: Structured debugging workflow
**When to use**: When encountering any bug, test failure, or unexpected behavior, before proceeding
**Dependencies**: None
**Overlaps**: verification-before-completion (both ensure correctness)

### test-driven-development
**Purpose**: TDD workflow enforcement
**When to use**: When implementing any feature or bugfix, before writing implementation code
**Dependencies**: None
**Related**: Language-specific TDD skills (cpp-test, go-test, kotlin-test, python-testing, rust-test)

### verification-before-completion
**Purpose**: Verify work before claiming completion
**When to use**: When about to claim work is complete, fixed, or passing, before committing
**Dependencies**: None
**Overlaps**: systematic-debugging (both ensure correctness)

### requesting-code-review
**Purpose**: Prepare code for review
**When to use**: When completing tasks, implementing major features, or before merging
**Dependencies**: None
**Invokes**: Leads to code-reviewer or language-specific reviewers

### receiving-code-review
**Purpose**: Process code review feedback
**When to use**: When receiving code review feedback, before implementing suggestions
**Dependencies**: Follows requesting-code-review
**Related**: code-reviewer

### using-git-worktrees
**Purpose**: Isolated development environments
**When to use**: When starting feature work that needs isolation from current workspace
**Dependencies**: None
**Related**: finishing-a-development-branch

### finishing-a-development-branch
**Purpose**: Decide how to finalize completed work
**When to use**: When implementation is complete, all tests pass
**Dependencies**: Follows development work
**Related**: using-git-worktrees

### dispatching-parallel-agents
**Purpose**: Multi-agent parallel execution
**When to use**: When facing 2+ independent tasks that can be worked on without shared state
**Dependencies**: None
**Invokes**: Agent tool with multiple subagents
**Related**: subagent-driven-development, team

### subagent-driven-development
**Purpose**: Execute plans with independent tasks in current session
**When to use**: When executing implementation plans with independent tasks
**Dependencies**: Requires a plan
**Related**: dispatching-parallel-agents, executing-plans

### using-superpowers
**Purpose**: Introduction to skills system
**When to use**: Starting any conversation - establishes how to find and use skills
**Dependencies**: None (meta-skill)
**Invokes**: Determines which other skills to use

### writing-skills
**Purpose**: Create and edit skills
**When to use**: When creating new skills, editing existing skills, or verifying skills work
**Dependencies**: None
**Related**: skill-creator, skill-authoring-workflow
