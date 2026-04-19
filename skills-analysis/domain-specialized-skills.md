# Domain-Specific and Specialized Skills

## Overview
Skills for specialized domains including healthcare, logistics, supply chain, energy, customs, and other industry-specific applications.

## Healthcare

### healthcare-emr-patterns
**Purpose**: EMR/EHR development patterns for healthcare applications
**When to use**: Healthcare application development
**Dependencies**: None
**Related**: healthcare-cdss-patterns, healthcare-phi-compliance, healthcare-eval-harness
**Domain**: Healthcare EMR

### healthcare-cdss-patterns
**Purpose**: Clinical Decision Support System (CDSS) development patterns
**When to use**: Building CDSS systems
**Dependencies**: None
**Related**: healthcare-emr-patterns, healthcare-eval-harness
**Domain**: Healthcare CDSS

### healthcare-phi-compliance
**Purpose**: Protected Health Information (PHI) and PII compliance
**When to use**: Healthcare data handling
**Dependencies**: None
**Related**: healthcare-emr-patterns, security-reviewer
**Domain**: Healthcare compliance

### healthcare-eval-harness
**Purpose**: Patient safety evaluation harness for healthcare application deployments
**When to use**: Healthcare application testing
**Dependencies**: None
**Related**: healthcare-emr-patterns, healthcare-cdss-patterns, eval-harness
**Domain**: Healthcare testing

## Logistics and Supply Chain

### logistics-exception-management
**Purpose**: Codified expertise for handling freight exceptions, shipment delays, damages
**When to use**: Logistics exception handling
**Dependencies**: None
**Related**: carrier-relationship-management, returns-reverse-logistics
**Domain**: Logistics exceptions

### carrier-relationship-management
**Purpose**: Codified expertise for managing carrier portfolios, negotiating freight rates
**When to use**: Carrier management
**Dependencies**: None
**Related**: logistics-exception-management
**Domain**: Carrier management

### returns-reverse-logistics
**Purpose**: Codified expertise for returns authorization, receipt and inspection, disposition
**When to use**: Returns processing
**Dependencies**: None
**Related**: logistics-exception-management
**Domain**: Reverse logistics

### inventory-demand-planning
**Purpose**: Codified expertise for demand forecasting, safety stock optimization, replenishment
**When to use**: Inventory planning
**Dependencies**: None
**Related**: production-scheduling
**Domain**: Inventory planning

### production-scheduling
**Purpose**: Codified expertise for production scheduling, job sequencing, line balancing
**When to use**: Production planning
**Dependencies**: None
**Related**: inventory-demand-planning, quality-nonconformance
**Domain**: Production scheduling

### quality-nonconformance
**Purpose**: Codified expertise for quality control, non-conformance investigation, root cause
**When to use**: Quality management
**Dependencies**: None
**Related**: production-scheduling
**Domain**: Quality control

## Trade and Compliance

### customs-trade-compliance
**Purpose**: Codified expertise for customs documentation, tariff classification, duty optimization
**When to use**: International trade compliance
**Dependencies**: None
**Related**: None
**Domain**: Customs compliance

### visa-doc-translate
**Purpose**: Translate visa application documents (images) to English
**When to use**: Visa document translation
**Dependencies**: None
**Related**: nutrient-document-processing
**Domain**: Document translation

## Energy

### energy-procurement
**Purpose**: Codified expertise for electricity and gas procurement, tariff optimization
**When to use**: Energy procurement
**Dependencies**: None
**Related**: None
**Domain**: Energy procurement

## Customer Operations

### customer-billing-ops
**Purpose**: Operate customer billing workflows such as subscriptions, refunds, churn triage
**When to use**: Billing operations
**Dependencies**: None
**Related**: saas-revenue-growth-metrics
**Domain**: Billing operations

## Skill Management

### skill-creator
**Purpose**: Guide for creating effective skills
**When to use**: When users want to create new skills
**Dependencies**: None
**Related**: writing-skills, skill-authoring-workflow, skill-stocktake
**Domain**: Skill creation

### skill-authoring-workflow
**Purpose**: Turn raw PM content into a compliant, publish-ready skill
**When to use**: Creating or refining skills
**Dependencies**: None
**Related**: skill-creator, writing-skills
**Domain**: Skill authoring

### skill-stocktake
**Purpose**: Audit Claude skills and commands for quality
**When to use**: Auditing skills
**Dependencies**: None
**Related**: skill-creator, skill-health, skill-comply
**Domain**: Skill auditing

### skill-health
**Purpose**: Show skill portfolio health dashboard with charts and analytics
**When to use**: Analyzing skill portfolio
**Dependencies**: None
**Related**: skill-stocktake, skill-comply
**Domain**: Skill analytics

### skill-comply
**Purpose**: Visualize whether skills, rules, and agent definitions are actually followed
**When to use**: Checking skill compliance
**Dependencies**: None
**Related**: skill-health, skill-stocktake
**Domain**: Skill compliance

### find-skills
**Purpose**: Helps users discover and install agent skills
**When to use**: When users ask "how do I...", "can Claude...", "is there a skill for..."
**Dependencies**: None
**Related**: skill-creator
**Domain**: Skill discovery

## Context and Memory

### context-budget
**Purpose**: Audits Claude Code context window consumption
**When to use**: Understanding context usage
**Dependencies**: None
**Related**: strategic-compact, token-budget-advisor
**Domain**: Context management

### strategic-compact
**Purpose**: Suggests manual context compaction at logical intervals
**When to use**: Managing long sessions
**Dependencies**: None
**Related**: context-budget
**Domain**: Context compaction

### token-budget-advisor
**Purpose**: Offers informed choice about response depth before consuming tokens
**When to use**: Managing token usage
**Dependencies**: None
**Related**: context-budget
**Domain**: Token management

## Planning and Execution

### plan
**Purpose**: Restate requirements, assess risks, create step-by-step implementation plan
**When to use**: Planning implementation
**Dependencies**: None
**Related**: writing-plans, executing-plans, blueprint
**Domain**: Planning

### blueprint
**Purpose**: Turn a one-line objective into a step-by-step construction plan
**When to use**: Multi-session project planning
**Dependencies**: None
**Related**: plan, writing-plans
**Domain**: Blueprint planning

### prp-plan
**Purpose**: Create comprehensive feature implementation plan with codebase analysis
**When to use**: Feature planning
**Dependencies**: None
**Related**: prp-implement, plan
**Domain**: PRP planning

### prp-implement
**Purpose**: Execute an implementation plan with rigorous validation loops
**When to use**: Executing PRP plans
**Dependencies**: None
**Related**: prp-plan, executing-plans
**Domain**: PRP implementation

## Session Management

### resume-session
**Purpose**: Load the most recent session file and resume work
**When to use**: Resuming previous work
**Dependencies**: None
**Related**: save-session, sessions
**Domain**: Session management

### save-session
**Purpose**: Save current session state to a dated file
**When to use**: Preserving session state
**Dependencies**: None
**Related**: resume-session, sessions
**Domain**: Session management

### sessions
**Purpose**: Manage Claude Code session history, aliases, and session metadata
**When to use**: Session management
**Dependencies**: None
**Related**: resume-session, save-session
**Domain**: Session management

## Specialized Tools

### aside
**Purpose**: Answer a quick side question without interrupting or losing context
**When to use**: Quick questions during work
**Dependencies**: None
**Related**: None
**Domain**: Context preservation

### evolve
**Purpose**: Analyze instincts and suggest or generate evolved structures
**When to use**: Evolving learned patterns
**Dependencies**: None
**Related**: continuous-learning, continuous-learning-v2
**Domain**: Pattern evolution

### instinct-export
**Purpose**: Export instincts from project/global scope to a file
**When to use**: Sharing learned patterns
**Dependencies**: None
**Related**: instinct-import, instinct-status
**Domain**: Instinct management

### instinct-import
**Purpose**: Import instincts from file or URL into project/global scope
**When to use**: Loading learned patterns
**Dependencies**: None
**Related**: instinct-export, instinct-status
**Domain**: Instinct management

### instinct-status
**Purpose**: Show learned instincts (project + global) with confidence
**When to use**: Reviewing learned patterns
**Dependencies**: None
**Related**: instinct-export, instinct-import
**Domain**: Instinct management

### projects
**Purpose**: List known projects and their instinct statistics
**When to use**: Project overview
**Dependencies**: None
**Related**: instinct-status
**Domain**: Project management

### promote
**Purpose**: Promote project-scoped instincts to global scope
**When to use**: Generalizing patterns
**Dependencies**: None
**Related**: instinct-status, projects
**Domain**: Instinct promotion

### prune
**Purpose**: Delete pending instincts older than 30 days that were never promoted
**When to use**: Cleaning up old patterns
**Dependencies**: None
**Related**: instinct-status
**Domain**: Instinct cleanup

### prompt-optimize
**Purpose**: Analyze raw prompts, identify intent and gaps, match ECC components
**When to use**: Optimizing prompts
**Dependencies**: None
**Related**: None
**Domain**: Prompt optimization

### rules-distill
**Purpose**: Scan skills to extract cross-cutting principles and distill them into rules
**When to use**: Extracting patterns from skills
**Dependencies**: None
**Related**: skill-stocktake
**Domain**: Rule extraction

### opensource-pipeline
**Purpose**: Open-source pipeline: fork, sanitize, and package private projects
**When to use**: Preparing code for open source
**Dependencies**: None
**Related**: security-scan
**Domain**: Open source preparation

### harness-optimizer
**Purpose**: Analyze and improve the local agent harness configuration
**When to use**: Optimizing agent harness
**Dependencies**: None
**Related**: autonomous-agent-harness
**Domain**: Harness optimization

### product-lens
**Purpose**: Validate the "why" before building, run product diagnostics
**When to use**: Product validation
**Dependencies**: None
**Related**: discovery-process, problem-statement
**Domain**: Product validation

### agentic-engineering
**Purpose**: Operate as an agentic engineer using eval-first execution
**When to use**: Agentic development approach
**Dependencies**: None
**Related**: eval-harness, ai-first-engineering
**Domain**: Agentic engineering

### ai-first-engineering
**Purpose**: Engineering operating model for teams where AI agents generate code
**When to use**: AI-first development
**Dependencies**: None
**Related**: agentic-engineering
**Domain**: AI-first engineering

### openclaw-persona-forge
**Purpose**: 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案
**When to use**: Creating OpenClaw personas
**Dependencies**: None
**Related**: None
**Domain**: OpenClaw personas

### nanoclaw-repl
**Purpose**: Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL
**When to use**: Using NanoClaw REPL
**Dependencies**: None
**Related**: None
**Domain**: NanoClaw REPL

### google-workspace-ops
**Purpose**: Operate across Google Drive, Docs, Sheets, and Slides as one workflow
**When to use**: Google Workspace operations
**Dependencies**: Google Workspace MCP
**Related**: docx, xlsx, pptx
**Domain**: Google Workspace
