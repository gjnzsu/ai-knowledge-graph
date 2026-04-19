# Financial Analysis and Business Skills

## Overview
Skills for financial modeling, analysis, business metrics, and investment evaluation.

## Financial Models

### 3-statement-model
**Purpose**: Fill out a 3-statement financial model template
**When to use**: Creating income statement, balance sheet, cash flow models
**Dependencies**: None
**Related**: dcf, lbo
**Domain**: Financial modeling

### dcf
**Purpose**: Build a DCF valuation model with comps-informed terminal multiples
**When to use**: Equity valuation
**Dependencies**: None
**Related**: comps, 3-statement-model
**Domain**: DCF valuation

### lbo
**Purpose**: Build an LBO model for a PE acquisition
**When to use**: Leveraged buyout analysis
**Dependencies**: None
**Related**: 3-statement-model
**Domain**: LBO modeling

### comps
**Purpose**: Build a comparable company analysis with trading multiples
**When to use**: Valuation via comparables
**Dependencies**: None
**Related**: dcf, competitive-analysis
**Domain**: Comps analysis

### comps-analysis
**Purpose**: Build institutional-grade comparable company analyses
**When to use**: Detailed comps work
**Dependencies**: None
**Related**: comps, dcf
**Domain**: Comps analysis

### lbo-model
**Purpose**: Complete LBO model templates
**When to use**: LBO modeling
**Dependencies**: None
**Related**: lbo, 3-statement-model
**Domain**: LBO modeling

### dcf-model
**Purpose**: Real DCF model creation for equity valuation
**When to use**: DCF valuation
**Dependencies**: None
**Related**: dcf, comps-analysis
**Domain**: DCF modeling

## Business Analysis

### competitive-analysis (financial)
**Purpose**: Framework for building competitive landscape decks
**When to use**: Competitive positioning analysis
**Dependencies**: None
**Related**: market-research, comps
**Domain**: Competitive analysis

### check-deck
**Purpose**: QC a presentation deck for errors and consistency
**When to use**: Reviewing presentations
**Dependencies**: None
**Related**: ib-check-deck, ppt-generator
**Domain**: Deck review

### ib-check-deck
**Purpose**: Investment banking presentation quality checker
**When to use**: Reviewing IB pitch decks
**Dependencies**: None
**Related**: check-deck
**Domain**: IB deck review

### debug-model
**Purpose**: Debug and audit a financial model for errors
**When to use**: Model QA
**Dependencies**: None
**Related**: audit-xls
**Domain**: Model debugging

### audit-xls
**Purpose**: Audit a spreadsheet for formula accuracy, errors, common mistakes
**When to use**: Spreadsheet auditing
**Dependencies**: None
**Related**: debug-model, xlsx
**Domain**: Spreadsheet audit

### clean-data-xls
**Purpose**: Clean up messy spreadsheet data
**When to use**: Data cleaning
**Dependencies**: None
**Related**: xlsx, audit-xls
**Domain**: Data cleaning

## SaaS Metrics

### saas-revenue-growth-metrics
**Purpose**: Calculate SaaS revenue, retention, and growth metrics
**When to use**: Diagnosing momentum and growth
**Dependencies**: None
**Related**: saas-economics-efficiency-metrics, business-health-diagnostic
**Domain**: SaaS revenue

### saas-economics-efficiency-metrics
**Purpose**: Evaluate SaaS unit economics and capital efficiency
**When to use**: Deciding whether to scale
**Dependencies**: None
**Related**: saas-revenue-growth-metrics, business-health-diagnostic
**Domain**: SaaS economics

### business-health-diagnostic
**Purpose**: Diagnose SaaS business health across growth, retention, efficiency, capital
**When to use**: Overall business health assessment
**Dependencies**: None
**Related**: saas-revenue-growth-metrics, saas-economics-efficiency-metrics
**Domain**: Business diagnostics

### finance-metrics-quickref
**Purpose**: Look up SaaS finance metrics, formulas, and benchmarks fast
**When to use**: Quick metric reference
**Dependencies**: None
**Related**: saas-revenue-growth-metrics, saas-economics-efficiency-metrics
**Domain**: Metrics reference

### tam-sam-som-calculator
**Purpose**: Calculate TAM, SAM, and SOM with explicit assumptions
**When to use**: Market sizing
**Dependencies**: None
**Related**: market-research
**Domain**: Market sizing

## Pricing and Investment

### finance-based-pricing-advisor
**Purpose**: Evaluate pricing changes using ARPU, conversion, churn risk, NRR
**When to use**: Pricing decisions
**Dependencies**: None
**Related**: saas-revenue-growth-metrics
**Domain**: Pricing strategy

### feature-investment-advisor
**Purpose**: Evaluate feature investments using revenue impact, cost structure, ROI
**When to use**: Feature investment decisions
**Dependencies**: None
**Related**: finance-based-pricing-advisor
**Domain**: Feature economics

### acquisition-channel-advisor
**Purpose**: Evaluate acquisition channels using unit economics, customer quality
**When to use**: Channel evaluation
**Dependencies**: None
**Related**: saas-economics-efficiency-metrics
**Domain**: Acquisition channels

## Investor Relations

### investor-outreach
**Purpose**: Draft cold emails, warm intro blurbs, follow-ups, update emails
**When to use**: Investor communication
**Dependencies**: None
**Related**: investor-materials, lead-intelligence
**Domain**: Investor outreach

### investor-materials
**Purpose**: Create and update pitch decks, one-pagers, investor memos
**When to use**: Creating investor materials
**Dependencies**: None
**Related**: investor-outreach, ppt-generator
**Domain**: Investor materials

### lead-intelligence
**Purpose**: AI-native lead intelligence and outreach pipeline
**When to use**: Lead generation and research
**Dependencies**: None
**Related**: investor-outreach, social-graph-ranker
**Domain**: Lead intelligence

### social-graph-ranker
**Purpose**: Weighted social-graph ranking for warm intro discovery
**When to use**: Finding warm introductions
**Dependencies**: None
**Related**: lead-intelligence, connections-optimizer
**Domain**: Social graph analysis

### connections-optimizer
**Purpose**: Reorganize X and LinkedIn network with review-first pruning
**When to use**: Network optimization
**Dependencies**: None
**Related**: social-graph-ranker
**Domain**: Network management

## Presentation Templates

### ppt-template
**Purpose**: Create a reusable PPT template skill from a PowerPoint template file
**When to use**: Creating presentation templates
**Dependencies**: None
**Related**: ppt-generator, pptx
**Domain**: Template creation

### ppt-template-creator
**Purpose**: Creates self-contained PPT template SKILLS from user-provided files
**When to use**: Creating template skills
**Dependencies**: None
**Related**: ppt-template
**Domain**: Template skill creation

### deck-refresh
**Purpose**: Updates a presentation with new numbers
**When to use**: Quarterly refreshes, earnings updates
**Dependencies**: None
**Related**: check-deck, ppt-generator
**Domain**: Deck updates

## AI Product Evaluation

### ai-shaped-readiness-advisor
**Purpose**: Assess whether your product work is AI-first or AI-shaped
**When to use**: Evaluating AI product readiness
**Dependencies**: None
**Related**: recommendation-canvas, context-engineering-advisor
**Domain**: AI product strategy

### context-engineering-advisor
**Purpose**: Diagnose context stuffing vs. context engineering
**When to use**: When an AI workflow feels brittle
**Dependencies**: None
**Related**: ai-shaped-readiness-advisor
**Domain**: Context engineering

### recommendation-canvas
**Purpose**: Evaluate an AI product idea across outcomes, hypotheses, risks
**When to use**: AI product evaluation
**Dependencies**: None
**Related**: ai-shaped-readiness-advisor
**Domain**: AI product canvas
