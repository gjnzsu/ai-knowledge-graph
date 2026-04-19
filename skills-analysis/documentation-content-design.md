# Documentation, Content, and Design Skills

## Overview
Skills for creating documentation, content, presentations, diagrams, and visual designs.

## Documentation

### doc-coauthoring
**Purpose**: Guide users through a structured workflow for co-authoring documentation
**When to use**: Creating documentation collaboratively
**Dependencies**: None
**Related**: article-writing
**Domain**: Documentation

### article-writing
**Purpose**: Write articles, guides, blog posts, tutorials, newsletter issues
**When to use**: Long-form content creation
**Dependencies**: None
**Related**: doc-coauthoring, content-engine
**Domain**: Content writing

### documentation-lookup
**Purpose**: Use up-to-date library and framework docs via Context7 MCP
**When to use**: Need current documentation for libraries
**Dependencies**: Context7 MCP
**Related**: None
**Domain**: Documentation lookup

### docs-lookup
**Purpose**: When the user asks how to use a library, framework, or API
**When to use**: Fetching current documentation and code examples
**Dependencies**: Context7 MCP
**Related**: documentation-lookup
**Domain**: Documentation lookup

## Document Formats

### docx
**Purpose**: Comprehensive document creation, editing, and analysis with tracked changes
**When to use**: Working with Word documents
**Dependencies**: None
**Related**: pdf, pptx
**Domain**: Word documents

### pdf
**Purpose**: Comprehensive PDF manipulation toolkit
**When to use**: Working with PDF files
**Dependencies**: None
**Related**: docx, nutrient-document-processing
**Domain**: PDF processing

### pptx
**Purpose**: Use any time a .pptx file is involved
**When to use**: Working with PowerPoint files
**Dependencies**: None
**Related**: ppt-generator, huashu-slides
**Domain**: PowerPoint

### xlsx
**Purpose**: Comprehensive spreadsheet creation, editing, and analysis
**When to use**: Working with Excel files
**Dependencies**: None
**Related**: None
**Domain**: Excel spreadsheets

### nutrient-document-processing
**Purpose**: Process, convert, OCR, extract, redact, sign, and fill documents
**When to use**: Advanced document processing
**Dependencies**: Nutrient API
**Related**: pdf, docx
**Domain**: Document processing

## Presentations

### ppt-generator
**Purpose**: Create professional PowerPoint presentations with enhanced styling
**When to use**: Generating presentations
**Dependencies**: None
**Related**: pptx, huashu-slides, frontend-slides
**Domain**: Presentation generation

### huashu-slides
**Purpose**: AI演示文稿全流程制作：内容结构化→设计选型→AI插画/HTML构建→PPTX导出
**When to use**: Creating Chinese presentations with AI illustrations
**Dependencies**: None
**Related**: ppt-generator, pptx
**Domain**: Chinese presentations

### frontend-slides
**Purpose**: Create stunning, animation-rich HTML presentations
**When to use**: Creating web-based presentations
**Dependencies**: None
**Related**: ppt-generator, web-artifacts-builder
**Domain**: HTML presentations

## Diagrams and Visualization

### drawio
**Purpose**: Always use when user asks to create, generate, draw, or design a diagram
**When to use**: Creating diagrams, flowcharts, architecture diagrams
**Dependencies**: None
**Related**: graphify
**Domain**: Diagram creation

### graphify
**Purpose**: Turn any folder of files into a navigable knowledge graph
**When to use**: Creating knowledge graphs from codebases or documents
**Dependencies**: Python, graphify package
**Related**: drawio
**Domain**: Knowledge graphs

### design-system
**Purpose**: Generate or audit design systems, check visual consistency
**When to use**: Design system work
**Dependencies**: None
**Related**: frontend-design, canvas-design
**Domain**: Design systems

### canvas-design
**Purpose**: Create beautiful visual art in .png and .pdf documents
**When to use**: Creating visual designs
**Dependencies**: None
**Related**: design-system, frontend-design
**Domain**: Visual design

### frontend-design
**Purpose**: Create distinctive, production-grade frontend interfaces
**When to use**: Frontend UI design
**Dependencies**: None
**Related**: design-system, canvas-design, liquid-glass-design
**Domain**: Frontend design

### liquid-glass-design
**Purpose**: iOS 26 Liquid Glass design system
**When to use**: iOS design with glass material effects
**Dependencies**: None
**Related**: frontend-design, swiftui-patterns
**Domain**: iOS design

### theme-factory
**Purpose**: Toolkit for styling artifacts with a theme
**When to use**: Applying themes to artifacts
**Dependencies**: None
**Related**: design-system
**Domain**: Theming

### brand-guidelines
**Purpose**: Applies Anthropic's official brand colors and typography
**When to use**: Creating Anthropic-branded artifacts
**Dependencies**: None
**Related**: theme-factory
**Domain**: Brand guidelines

## Content Creation

### content-engine
**Purpose**: Create platform-native content systems for X, LinkedIn, TikTok, YouTube
**When to use**: Multi-platform content creation
**Dependencies**: None
**Related**: article-writing, brand-voice, crosspost
**Domain**: Content systems

### brand-voice
**Purpose**: Build a source-derived writing style profile
**When to use**: Establishing brand voice
**Dependencies**: None
**Related**: content-engine
**Domain**: Brand voice

### crosspost
**Purpose**: Multi-platform content distribution across X, LinkedIn, Threads, Bluesky
**When to use**: Distributing content across platforms
**Dependencies**: Platform APIs
**Related**: content-engine, x-api
**Domain**: Content distribution

### x-api
**Purpose**: X/Twitter API integration for posting tweets, threads, reading timelines
**When to use**: Twitter/X integration
**Dependencies**: X API
**Related**: crosspost
**Domain**: Twitter API

## Video and Media

### manim-video
**Purpose**: Build reusable Manim explainers for technical concepts
**When to use**: Creating technical animation videos
**Dependencies**: Manim
**Related**: remotion-video-creation, video-editing
**Domain**: Technical animation

### remotion-video-creation
**Purpose**: Best practices for Remotion - Video creation in React
**When to use**: Creating videos with React
**Dependencies**: Remotion
**Related**: manim-video, video-editing
**Domain**: React video

### video-editing
**Purpose**: AI-assisted video editing workflows
**When to use**: Editing video content
**Dependencies**: None
**Related**: manim-video, remotion-video-creation, videodb
**Domain**: Video editing

### videodb
**Purpose**: See, Understand, Act on video and audio
**When to use**: Video/audio processing and analysis
**Dependencies**: VideoDB
**Related**: video-editing
**Domain**: Video/audio processing

### fal-ai-media
**Purpose**: Unified media generation via fal.ai MCP — image, video, and audio
**When to use**: AI media generation
**Dependencies**: fal.ai MCP
**Related**: video-editing
**Domain**: AI media generation

### ui-demo
**Purpose**: Record polished UI demo videos using Playwright
**When to use**: Creating UI demo videos
**Dependencies**: Playwright
**Related**: video-editing, webapp-testing
**Domain**: UI demos

### slack-gif-creator
**Purpose**: Knowledge and utilities for creating animated GIFs optimized for Slack
**When to use**: Creating Slack GIFs
**Dependencies**: None
**Related**: None
**Domain**: GIF creation

## Web Artifacts

### web-artifacts-builder
**Purpose**: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts
**When to use**: Creating complex web artifacts
**Dependencies**: None
**Related**: frontend-slides, frontend-design
**Domain**: Web artifacts

### algorithmic-art
**Purpose**: Creating algorithmic art using p5.js with seeded randomness
**When to use**: Generative art creation
**Dependencies**: p5.js
**Related**: canvas-design
**Domain**: Generative art

## Internal Communications

### internal-comms
**Purpose**: A set of resources to help write all kinds of internal communications
**When to use**: Writing internal company communications
**Dependencies**: None
**Related**: eol-message
**Domain**: Internal communications
