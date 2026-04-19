# Agent Orchestration and Workflow Skills

## Overview
Skills for managing multi-agent systems, autonomous loops, and complex workflow orchestration.

## Multi-Agent Orchestration

### team
**Purpose**: Run a structured multi-agent team with a tech lead orchestrator
**When to use**: When the user wants multiple agents working together
**Dependencies**: None
**Invokes**: TeamCreate, Agent, SendMessage, TaskUpdate
**Related**: dispatching-parallel-agents, subagent-driven-development
**Domain**: Team coordination

### dispatching-parallel-agents
**Purpose**: Multi-agent parallel execution for independent tasks
**When to use**: When facing 2+ independent tasks that can be worked on without shared state
**Dependencies**: None
**Invokes**: Agent tool with multiple subagents
**Related**: team, subagent-driven-development
**Domain**: Parallel execution

### subagent-driven-development
**Purpose**: Execute plans with independent tasks in current session
**When to use**: When executing implementation plans with independent tasks
**Dependencies**: Requires a plan
**Related**: dispatching-parallel-agents, executing-plans
**Domain**: Plan execution

### dmux-workflows
**Purpose**: Multi-agent orchestration using dmux (tmux pane manager for AI agents)
**When to use**: Complex multi-agent workflows
**Dependencies**: dmux installed
**Related**: team, autonomous-agent-harness
**Domain**: tmux-based orchestration

### claude-devfleet
**Purpose**: Orchestrate multi-agent coding tasks via Claude DevFleet
**When to use**: Planning projects, dispatching agents, monitoring progress
**Dependencies**: DevFleet MCP
**Related**: team, dmux-workflows
**Domain**: DevFleet orchestration

### team-builder
**Purpose**: Interactive agent picker for composing and dispatching parallel teams
**When to use**: Building custom agent teams
**Dependencies**: None
**Related**: team, dispatching-parallel-agents
**Domain**: Team composition

## Autonomous Loops

### loop
**Purpose**: Run a prompt or slash command on a recurring interval
**When to use**: When the user wants to set up a recurring task, poll for status
**Dependencies**: None
**Invokes**: CronCreate or ScheduleWakeup
**Related**: autonomous-loops, continuous-agent-loop
**Domain**: Scheduled tasks

### autonomous-loops
**Purpose**: Patterns and architectures for autonomous Claude Code loops
**When to use**: Designing autonomous agent systems
**Dependencies**: None
**Related**: loop, continuous-agent-loop, autonomous-agent-harness
**Domain**: Loop patterns

### continuous-agent-loop
**Purpose**: Patterns for continuous autonomous agent loops with quality gates, evals
**When to use**: Building production autonomous systems
**Dependencies**: None
**Related**: autonomous-loops, loop
**Domain**: Production loops

### autonomous-agent-harness
**Purpose**: Transform Claude Code into a fully autonomous agent system
**When to use**: Building autonomous agent infrastructure
**Dependencies**: None
**Related**: autonomous-loops, continuous-agent-loop
**Domain**: Agent infrastructure

### loop-operator
**Purpose**: Operate autonomous agent loops, monitor progress, intervene safely
**When to use**: Managing running loops
**Dependencies**: None
**Related**: autonomous-loops
**Domain**: Loop operations

## Workflow Patterns

### ralphinho-rfc-pipeline
**Purpose**: RFC-driven multi-agent DAG execution pattern with quality gates
**When to use**: Complex multi-stage workflows with reviews
**Dependencies**: None
**Related**: team, dmux-workflows
**Domain**: RFC workflow

### gan-style-harness
**Purpose**: GAN-inspired Generator-Evaluator agent harness
**When to use**: Building high-quality applications with adversarial review
**Dependencies**: None
**Related**: santa-method
**Domain**: Generator-Evaluator pattern

### santa-method
**Purpose**: Multi-agent adversarial verification with convergence loop
**When to use**: Critical code requiring multiple independent reviews
**Dependencies**: None
**Related**: gan-style-harness, code-reviewer
**Domain**: Adversarial verification

### iterative-retrieval
**Purpose**: Pattern for progressively refining context retrieval
**When to use**: Solving subagent context overflow
**Dependencies**: None
**Related**: Agent tool usage
**Domain**: Context management

## Agent Development

### agent-harness-construction
**Purpose**: Design and optimize AI agent action spaces, tool definitions
**When to use**: Building custom agent harnesses
**Dependencies**: None
**Related**: autonomous-agent-harness
**Domain**: Agent design

### mcp-builder
**Purpose**: Guide for creating high-quality MCP servers
**When to use**: Building MCP servers
**Dependencies**: None
**Related**: mcp-server-patterns
**Domain**: MCP development

### mcp-server-patterns
**Purpose**: Build MCP servers with Node/TypeScript SDK
**When to use**: MCP server implementation
**Dependencies**: None
**Related**: mcp-builder
**Domain**: MCP patterns

### claude-api
**Purpose**: Build, debug, and optimize Claude API / Anthropic SDK apps
**When to use**: Claude API development
**Dependencies**: None
**Related**: mcp-builder
**Domain**: Claude API

## Evaluation and Quality

### eval-harness
**Purpose**: Formal evaluation framework for Claude Code sessions
**When to use**: Implementing eval-driven development
**Dependencies**: None
**Related**: verification-loop, continuous-learning
**Domain**: Evaluation framework

### agent-eval
**Purpose**: Head-to-head comparison of coding agents
**When to use**: Comparing agent performance
**Dependencies**: None
**Related**: eval-harness
**Domain**: Agent benchmarking

### continuous-learning
**Purpose**: Automatically extract reusable patterns from Claude Code sessions
**When to use**: Building institutional knowledge
**Dependencies**: None
**Related**: continuous-learning-v2, eval-harness
**Domain**: Pattern extraction

### continuous-learning-v2
**Purpose**: Instinct-based learning system that observes sessions via hooks
**When to use**: Advanced pattern learning
**Dependencies**: None
**Related**: continuous-learning
**Domain**: Instinct learning

## Enterprise Operations

### enterprise-agent-ops
**Purpose**: Operate long-lived agent workloads with observability, security
**When to use**: Production agent operations
**Dependencies**: None
**Related**: autonomous-agent-harness, continuous-agent-loop
**Domain**: Enterprise operations

### project-flow-ops
**Purpose**: Operate execution flow across GitHub and Linear
**When to use**: Managing project workflow
**Dependencies**: GitHub, Linear
**Related**: team
**Domain**: Project operations

### agent-payment-x402
**Purpose**: Add x402 payment execution to AI agents
**When to use**: Monetizing agent actions
**Dependencies**: x402 protocol
**Related**: autonomous-agent-harness
**Domain**: Agent payments

## Specialized Agents

### data-scraper-agent
**Purpose**: Build a fully automated AI-powered data collection agent
**When to use**: Automated data collection needs
**Dependencies**: None
**Related**: autonomous-loops
**Domain**: Data scraping

### canary-watch
**Purpose**: Monitor a deployed URL for regressions after deploys
**When to use**: Post-deployment monitoring
**Dependencies**: None
**Related**: loop, webapp-testing
**Domain**: Monitoring

### browser-qa
**Purpose**: Automate visual testing and UI interaction verification
**When to use**: Automated UI testing
**Dependencies**: Playwright
**Related**: webapp-testing, e2e-testing
**Domain**: Browser automation
