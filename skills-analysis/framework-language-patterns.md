# Framework and Language Pattern Skills

## Overview
Comprehensive patterns, best practices, and idioms for specific frameworks and languages.

## Backend Frameworks

### laravel-patterns
**Purpose**: Laravel architecture patterns, routing/controllers, Eloquent ORM, service layer
**When to use**: Laravel development
**Dependencies**: None
**Related**: laravel-tdd, laravel-verification, laravel-security, laravel-plugin-discovery
**Domain**: Laravel, PHP, Eloquent

### laravel-security
**Purpose**: Laravel security best practices for authn/authz, validation, CSRF
**When to use**: Laravel security concerns
**Dependencies**: None
**Related**: laravel-patterns, security-reviewer
**Domain**: Laravel security

### laravel-plugin-discovery
**Purpose**: Discover and evaluate Laravel packages via LaraPlugins.io MCP
**When to use**: When the user needs Laravel packages
**Dependencies**: MCP server
**Related**: laravel-patterns
**Domain**: Laravel ecosystem

### django-patterns
**Purpose**: Django architecture patterns, REST API design with DRF, ORM best practices
**When to use**: Django development
**Dependencies**: None
**Related**: django-tdd, django-verification, django-security
**Domain**: Django, Python, DRF

### django-security
**Purpose**: Django security best practices, authentication, authorization, CSRF protection
**When to use**: Django security concerns
**Dependencies**: None
**Related**: django-patterns, security-reviewer
**Domain**: Django security

### springboot-patterns
**Purpose**: Spring Boot architecture patterns, REST API design, layered services
**When to use**: Spring Boot development
**Dependencies**: None
**Related**: springboot-tdd, springboot-verification, springboot-security, jpa-patterns
**Domain**: Spring Boot, Java

### springboot-security
**Purpose**: Spring Security best practices for authn/authz, validation, CSRF
**When to use**: Spring Boot security concerns
**Dependencies**: None
**Related**: springboot-patterns, security-reviewer
**Domain**: Spring Security

### jpa-patterns
**Purpose**: JPA/Hibernate patterns for entity design, relationships, query optimization
**When to use**: JPA/Hibernate usage
**Dependencies**: None
**Related**: springboot-patterns, java-reviewer
**Domain**: JPA, Hibernate, ORM

## Frontend Frameworks

### frontend-patterns
**Purpose**: Frontend development patterns for React, Next.js, state management, performance
**When to use**: Frontend development
**Dependencies**: None
**Related**: frontend-design, nextjs-turbopack, nuxt4-patterns
**Domain**: React, Next.js, frontend

### nextjs-turbopack
**Purpose**: Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed
**When to use**: Next.js 16+ projects
**Dependencies**: None
**Related**: frontend-patterns
**Domain**: Next.js, Turbopack

### nuxt4-patterns
**Purpose**: Nuxt 4 app patterns for hydration safety, performance, route rules
**When to use**: Nuxt 4 development
**Dependencies**: None
**Related**: frontend-patterns
**Domain**: Nuxt, Vue

### swiftui-patterns
**Purpose**: SwiftUI architecture patterns, state management with @Observable, view composition
**When to use**: SwiftUI development
**Dependencies**: None
**Related**: swift-protocol-di-testing, swift-concurrency-6-2
**Domain**: SwiftUI, iOS

### compose-multiplatform-patterns
**Purpose**: Compose Multiplatform and Jetpack Compose patterns for KMP projects
**When to use**: Compose development
**Dependencies**: None
**Related**: kotlin-patterns, kotlin-reviewer
**Domain**: Compose, KMP, Android

## Language Patterns

### python-patterns
**Purpose**: Pythonic idioms, PEP 8 standards, type hints, best practices
**When to use**: Python development
**Dependencies**: None
**Related**: python-reviewer, python-testing
**Domain**: Python

### golang-patterns
**Purpose**: Idiomatic Go patterns, best practices, and conventions
**When to use**: Go development
**Dependencies**: None
**Related**: go-reviewer, golang-testing
**Domain**: Go

### golang-testing
**Purpose**: Go testing patterns including table-driven tests, subtests, benchmarks
**When to use**: Go testing
**Dependencies**: None
**Related**: golang-patterns, go-test
**Domain**: Go testing

### rust-patterns
**Purpose**: Idiomatic Rust patterns, ownership, error handling, traits, concurrency
**When to use**: Rust development
**Dependencies**: None
**Related**: rust-reviewer, rust-testing
**Domain**: Rust

### rust-testing
**Purpose**: Rust testing patterns including unit tests, integration tests, async testing
**When to use**: Rust testing
**Dependencies**: None
**Related**: rust-patterns, rust-test
**Domain**: Rust testing

### kotlin-patterns
**Purpose**: Idiomatic Kotlin patterns, best practices, and conventions
**When to use**: Kotlin development
**Dependencies**: None
**Related**: kotlin-reviewer, kotlin-testing, kotlin-coroutines-flows
**Domain**: Kotlin

### kotlin-testing
**Purpose**: Kotlin testing patterns with Kotest, MockK, coroutine testing
**When to use**: Kotlin testing
**Dependencies**: None
**Related**: kotlin-patterns, kotlin-test
**Domain**: Kotlin testing

### kotlin-coroutines-flows
**Purpose**: Kotlin Coroutines and Flow patterns for Android and KMP
**When to use**: Kotlin async programming
**Dependencies**: None
**Related**: kotlin-patterns, kotlin-reviewer
**Domain**: Kotlin coroutines, Flow

### kotlin-ktor-patterns
**Purpose**: Ktor server patterns including routing DSL, plugins, authentication
**When to use**: Ktor development
**Dependencies**: None
**Related**: kotlin-patterns
**Domain**: Ktor, Kotlin server

### kotlin-exposed-patterns
**Purpose**: JetBrains Exposed ORM patterns including DSL queries, DAO pattern
**When to use**: Exposed ORM usage
**Dependencies**: None
**Related**: kotlin-patterns
**Domain**: Exposed, Kotlin ORM

### cpp-coding-standards
**Purpose**: C++ coding standards based on the C++ Core Guidelines
**When to use**: When writing or reviewing C++ code
**Dependencies**: None
**Related**: cpp-reviewer, cpp-test
**Domain**: C++ standards

### java-coding-standards
**Purpose**: Java coding standards for Spring Boot services: naming, immutability, Optional
**When to use**: Java development
**Dependencies**: None
**Related**: java-reviewer, springboot-patterns
**Domain**: Java standards

### perl-patterns
**Purpose**: Modern Perl 5.36+ idioms, best practices, and conventions
**When to use**: Perl development
**Dependencies**: None
**Related**: perl-testing, perl-security
**Domain**: Perl

### perl-testing
**Purpose**: Perl testing patterns using Test2::V0, Test::More, prove runner
**When to use**: Perl testing
**Dependencies**: None
**Related**: perl-patterns
**Domain**: Perl testing

### perl-security
**Purpose**: Comprehensive Perl security covering taint mode, input validation
**When to use**: Perl security concerns
**Dependencies**: None
**Related**: perl-patterns, security-reviewer
**Domain**: Perl security

## Swift Specialized

### swift-protocol-di-testing
**Purpose**: Protocol-based dependency injection for testable Swift code
**When to use**: Swift testing and DI
**Dependencies**: None
**Related**: swiftui-patterns
**Domain**: Swift, DI, testing

### swift-concurrency-6-2
**Purpose**: Swift 6.2 Approachable Concurrency — single-threaded by default
**When to use**: Swift 6.2 async programming
**Dependencies**: None
**Related**: swiftui-patterns
**Domain**: Swift concurrency

### swift-actor-persistence
**Purpose**: Thread-safe data persistence in Swift using actors
**When to use**: Swift data persistence
**Dependencies**: None
**Related**: swift-concurrency-6-2
**Domain**: Swift actors, persistence

### foundation-models-on-device
**Purpose**: Apple FoundationModels framework for on-device LLM
**When to use**: On-device AI in Swift
**Dependencies**: None
**Related**: swiftui-patterns
**Domain**: Swift, on-device AI

## Specialized Frameworks

### pytorch-patterns
**Purpose**: PyTorch deep learning patterns and best practices
**When to use**: PyTorch development
**Dependencies**: None
**Related**: pytorch-build-resolver
**Domain**: PyTorch, deep learning

### remotion-video-creation
**Purpose**: Best practices for Remotion - Video creation in React
**When to use**: Remotion video projects
**Dependencies**: None
**Related**: frontend-patterns
**Domain**: Remotion, video, React
