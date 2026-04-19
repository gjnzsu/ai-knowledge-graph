# Infrastructure, DevOps, and Database Skills

## Overview
Skills for infrastructure, deployment, containerization, databases, and system architecture.

## Architecture and Design

### architect
**Purpose**: Software architecture specialist for system design, scalability, technical decisions
**When to use**: PROACTIVELY when planning new features, refactoring large systems
**Dependencies**: None
**Related**: backend-patterns, api-design, hexagonal-architecture
**Domain**: Software architecture

### hexagonal-architecture
**Purpose**: Design, implement, and refactor Ports & Adapters systems
**When to use**: Implementing clean architecture
**Dependencies**: None
**Related**: architect, backend-patterns
**Domain**: Hexagonal architecture

### backend-patterns
**Purpose**: Backend architecture patterns, API design, database optimization
**When to use**: Backend development
**Dependencies**: None
**Related**: api-design, database-migrations
**Domain**: Backend patterns

### api-design
**Purpose**: REST API design patterns including resource naming, status codes, pagination
**When to use**: Designing APIs
**Dependencies**: None
**Related**: backend-patterns
**Domain**: API design

## Deployment and CI/CD

### deployment-patterns
**Purpose**: Deployment workflows, CI/CD pipeline patterns, Docker containerization
**When to use**: Setting up deployments
**Dependencies**: None
**Related**: docker-patterns, git-workflow
**Domain**: Deployment

### git-workflow
**Purpose**: Git workflow patterns including branching strategies, commit conventions
**When to use**: Setting up git workflows
**Dependencies**: None
**Related**: deployment-patterns, finishing-a-development-branch
**Domain**: Git workflows

### docker-patterns
**Purpose**: Docker and Docker Compose patterns for local development
**When to use**: Docker usage
**Dependencies**: None
**Related**: deployment-patterns
**Domain**: Docker

### bun-runtime
**Purpose**: Bun as runtime, package manager, bundler, and test runner
**When to use**: Using Bun instead of Node
**Dependencies**: None
**Related**: frontend-patterns
**Domain**: Bun runtime

## Database

### postgres-patterns
**Purpose**: PostgreSQL database patterns for query optimization, schema design, indexing
**When to use**: PostgreSQL development
**Dependencies**: None
**Related**: database-migrations, database-reviewer
**Domain**: PostgreSQL

### clickhouse-io
**Purpose**: ClickHouse database patterns, query optimization, analytics
**When to use**: ClickHouse usage
**Dependencies**: None
**Related**: postgres-patterns
**Domain**: ClickHouse

### database-migrations
**Purpose**: Database migration best practices for schema changes, data migrations
**When to use**: Database schema changes
**Dependencies**: None
**Related**: postgres-patterns, database-reviewer
**Domain**: Database migrations

### database-reviewer
**Purpose**: PostgreSQL database specialist for query optimization, schema design
**When to use**: PROACTIVELY when writing SQL, creating migrations, designing schemas
**Dependencies**: None
**Related**: postgres-patterns, database-migrations
**Domain**: Database review

## Search and Data

### exa-search
**Purpose**: Neural search via Exa MCP for web, code, and company research
**When to use**: When the user needs advanced search
**Dependencies**: Exa MCP
**Related**: multi-search-engine, deep-research
**Domain**: Neural search

### multi-search-engine
**Purpose**: Multi search engine integration with 16 engines (7 CN + 9 Global)
**When to use**: Multi-engine search needs
**Dependencies**: None
**Related**: exa-search, deep-research
**Domain**: Search engines

### deep-research
**Purpose**: Multi-source deep research using firecrawl and exa MCPs
**When to use**: Comprehensive research tasks
**Dependencies**: Firecrawl, Exa MCPs
**Related**: exa-search, market-research
**Domain**: Deep research

### search-first
**Purpose**: Research-before-coding workflow
**When to use**: Before implementing, search for existing tools and patterns
**Dependencies**: None
**Related**: exa-search, documentation-lookup
**Domain**: Research workflow

## Performance and Optimization

### benchmark
**Purpose**: Measure performance baselines, detect regressions before/after changes
**When to use**: Performance testing
**Dependencies**: None
**Related**: verification-loop
**Domain**: Benchmarking

### cost-aware-llm-pipeline
**Purpose**: Cost optimization patterns for LLM API usage
**When to use**: Optimizing LLM costs
**Dependencies**: None
**Related**: claude-api
**Domain**: LLM cost optimization

### content-hash-cache-pattern
**Purpose**: Cache expensive file processing results using SHA-256 content hashes
**When to use**: Implementing content-based caching
**Dependencies**: None
**Related**: None
**Domain**: Caching patterns

## Code Quality

### plankton-code-quality
**Purpose**: Write-time code quality enforcement using Plankton
**When to use**: Enforcing code quality standards
**Dependencies**: Plankton
**Related**: code-reviewer, verification-loop
**Domain**: Code quality

### coding-standards
**Purpose**: Universal coding standards, best practices, and patterns
**When to use**: Establishing coding standards
**Dependencies**: None
**Related**: Language-specific coding standards
**Domain**: Coding standards

### simplify
**Purpose**: Review changed code for reuse, quality, and efficiency
**When to use**: Code simplification and cleanup
**Dependencies**: None
**Related**: refactor-cleaner, code-reviewer
**Domain**: Code simplification

### refactor-cleaner
**Purpose**: Dead code cleanup and consolidation specialist
**When to use**: PROACTIVELY for removing unused code, duplicates, and refactoring
**Dependencies**: None
**Related**: simplify
**Domain**: Code cleanup

## Monitoring and Observability

### microservices-layer-tracing
**Purpose**: Debugging issues in multi-service architectures
**When to use**: Debugging distributed systems
**Dependencies**: None
**Related**: backend-patterns
**Domain**: Distributed tracing

### ai-regression-testing
**Purpose**: Regression testing strategies for AI-assisted development
**When to use**: Testing AI-generated code
**Dependencies**: None
**Related**: verification-loop, tdd-workflow
**Domain**: AI testing

### click-path-audit
**Purpose**: Trace every user-facing button/touchpoint through its full state change sequence
**When to use**: Auditing UI interactions
**Dependencies**: None
**Related**: webapp-testing, e2e-testing
**Domain**: UI auditing

## Configuration and Setup

### update-config
**Purpose**: Configure the Claude Code harness via settings.json
**When to use**: Automated behaviors, permissions, env vars, hooks
**Dependencies**: None
**Related**: keybindings-help, configure-ecc
**Domain**: Configuration

### keybindings-help
**Purpose**: Customize keyboard shortcuts, rebind keys, add chord bindings
**When to use**: When the user wants to customize keybindings
**Dependencies**: None
**Related**: update-config
**Domain**: Keybindings

### configure-ecc
**Purpose**: Interactive installer for Everything Claude Code
**When to use**: Setting up ECC
**Dependencies**: None
**Related**: update-config
**Domain**: ECC setup

### fewer-permission-prompts
**Purpose**: Scan transcripts for common read-only calls, add allowlist
**When to use**: Reducing permission prompts
**Dependencies**: None
**Related**: update-config
**Domain**: Permissions

## Workspace Management

### workspace-surface-audit
**Purpose**: Audit the active repo, MCP servers, plugins, connectors, env surfaces
**When to use**: Understanding workspace configuration
**Dependencies**: None
**Related**: update-config, repo-scan
**Domain**: Workspace audit

### repo-scan
**Purpose**: Cross-stack source code asset audit
**When to use**: Auditing repository contents
**Dependencies**: None
**Related**: workspace-surface-audit
**Domain**: Repository scanning

### codebase-onboarding
**Purpose**: Analyze an unfamiliar codebase and generate a structured onboarding guide
**When to use**: Onboarding to new codebases
**Dependencies**: None
**Related**: graphify, repo-scan
**Domain**: Codebase onboarding

### ck
**Purpose**: Persistent per-project memory for Claude Code
**When to use**: Auto-loads project context on session start
**Dependencies**: None
**Related**: None
**Domain**: Project memory

## Security

### security-scan
**Purpose**: Scan Claude Code configuration for security vulnerabilities
**When to use**: Security auditing
**Dependencies**: None
**Related**: security-reviewer, safety-guard
**Domain**: Security scanning

### safety-guard
**Purpose**: Prevent destructive operations when working on production systems
**When to use**: Working on production
**Dependencies**: None
**Related**: security-scan
**Domain**: Safety checks

### healthcare-phi-compliance
**Purpose**: Protected Health Information (PHI) and PII compliance
**When to use**: Healthcare applications
**Dependencies**: None
**Related**: security-reviewer, healthcare-*
**Domain**: Healthcare compliance
