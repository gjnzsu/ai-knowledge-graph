# Code Review Skills

## Overview
Comprehensive code review across multiple languages and frameworks, ensuring quality, security, and best practices.

## Universal Skills

### code-reviewer
**Purpose**: Comprehensive code review for TypeScript, JavaScript, Python, Swift, Kotlin
**When to use**: After writing or modifying code, MUST BE USED for all code changes
**Dependencies**: None
**Invokes**: Read, Grep, Glob, Bash tools
**Related**: All language-specific reviewers

## Language-Specific Reviewers

### typescript-reviewer
**Purpose**: TypeScript/JavaScript code review - type safety, async correctness, Node/web security
**When to use**: For all TypeScript and JavaScript code changes, MUST BE USED
**Dependencies**: None
**Overlaps**: code-reviewer (general purpose)
**Domain**: TypeScript, JavaScript, Node.js, web

### python-reviewer
**Purpose**: Python code review - PEP 8 compliance, Pythonic idioms, type hints, security
**When to use**: For all Python code changes, MUST BE USED
**Dependencies**: None
**Overlaps**: code-reviewer (general purpose)
**Domain**: Python

### cpp-reviewer
**Purpose**: C++ code review - memory safety, modern C++ idioms, concurrency, performance
**When to use**: For all C++ code changes, MUST BE USED for C++ projects
**Dependencies**: None
**Domain**: C++, memory management, concurrency

### go-reviewer
**Purpose**: Go code review - idiomatic Go, concurrency patterns, error handling, performance
**When to use**: For all Go code changes, MUST BE USED for Go projects
**Dependencies**: None
**Domain**: Go, concurrency

### rust-reviewer
**Purpose**: Rust code review - ownership, lifetimes, error handling, unsafe usage, idiomatic patterns
**When to use**: For all Rust code changes, MUST BE USED for Rust projects
**Dependencies**: None
**Domain**: Rust, ownership, memory safety

### kotlin-reviewer
**Purpose**: Kotlin and Android/KMP code review - idiomatic patterns, coroutine safety, Compose best practices
**When to use**: For Kotlin code changes
**Dependencies**: None
**Domain**: Kotlin, Android, KMP, Compose

### flutter-reviewer
**Purpose**: Flutter and Dart code review - widget best practices, state management, Dart idioms
**When to use**: For Flutter code changes
**Dependencies**: None
**Domain**: Flutter, Dart, mobile

### java-reviewer
**Purpose**: Java and Spring Boot code review - layered architecture, JPA patterns, security, concurrency
**When to use**: For all Java code changes, MUST BE USED for Spring Boot projects
**Dependencies**: None
**Domain**: Java, Spring Boot, JPA

## Specialized Reviewers

### database-reviewer
**Purpose**: PostgreSQL database specialist - query optimization, schema design, security, performance
**When to use**: PROACTIVELY when writing SQL, creating migrations, designing schemas
**Dependencies**: None
**Domain**: PostgreSQL, Supabase, database design

### security-reviewer
**Purpose**: Security vulnerability detection and remediation
**When to use**: PROACTIVELY after writing code that handles user input, authentication, API endpoints
**Dependencies**: None
**Overlaps**: All language reviewers check security, but this is specialized
**Domain**: Security, OWASP Top 10, vulnerabilities
