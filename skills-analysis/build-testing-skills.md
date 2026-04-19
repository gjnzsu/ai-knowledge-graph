# Build and Testing Skills

## Overview
Skills for resolving build errors and implementing testing strategies across multiple languages and frameworks.

## Build Error Resolvers

### build-error-resolver
**Purpose**: Build and TypeScript error resolution specialist
**When to use**: PROACTIVELY when build fails or type errors occur
**Dependencies**: None
**Invokes**: Read, Write, Edit, Bash, Grep, Glob
**Domain**: TypeScript, JavaScript, build systems

### cpp-build-resolver
**Purpose**: C++ build, CMake, and compilation error resolution
**When to use**: When C++ builds fail
**Dependencies**: None
**Related**: cpp-reviewer, cpp-test
**Domain**: C++, CMake, linker, compilation

### go-build-resolver
**Purpose**: Go build, vet, and compilation error resolution
**When to use**: When Go builds fail
**Dependencies**: None
**Related**: go-reviewer, go-test
**Domain**: Go, go vet, linter

### java-build-resolver
**Purpose**: Java/Maven/Gradle build, compilation, and dependency error resolution
**When to use**: When Java or Spring Boot builds fail
**Dependencies**: None
**Related**: java-reviewer, springboot-*
**Domain**: Java, Maven, Gradle, Spring Boot

### kotlin-build-resolver
**Purpose**: Kotlin/Gradle build, compilation, and dependency error resolution
**When to use**: When Kotlin builds fail
**Dependencies**: None
**Related**: kotlin-reviewer, kotlin-test, gradle-build
**Domain**: Kotlin, Gradle, Android

### rust-build-resolver
**Purpose**: Rust build, compilation, and dependency error resolution
**When to use**: When Rust builds fail
**Dependencies**: None
**Related**: rust-reviewer, rust-test
**Domain**: Rust, Cargo, borrow checker

### pytorch-build-resolver
**Purpose**: PyTorch runtime, CUDA, and training error resolution
**When to use**: When PyTorch training or inference crashes
**Dependencies**: None
**Domain**: PyTorch, CUDA, deep learning

### gradle-build
**Purpose**: Fix Gradle build errors for Android and KMP projects
**When to use**: Android/KMP Gradle build failures
**Dependencies**: None
**Related**: kotlin-build-resolver
**Domain**: Gradle, Android, KMP

## Testing Skills

### tdd-guide
**Purpose**: Test-Driven Development specialist enforcing write-tests-first methodology
**When to use**: PROACTIVELY when writing new features, fixing bugs, or refactoring code
**Dependencies**: None
**Related**: test-driven-development (superpowers), language-specific TDD skills
**Domain**: TDD methodology

### cpp-test
**Purpose**: Enforce TDD workflow for C++, write GoogleTest tests first
**When to use**: Only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest
**Dependencies**: None
**Related**: cpp-reviewer, cpp-build-resolver
**Domain**: C++, GoogleTest, CTest

### go-test
**Purpose**: Enforce TDD workflow for Go, write table-driven tests first
**When to use**: For Go testing
**Dependencies**: None
**Related**: go-reviewer, go-build-resolver
**Domain**: Go, table-driven tests

### kotlin-test
**Purpose**: Enforce TDD workflow for Kotlin, write Kotest tests first
**When to use**: For Kotlin testing
**Dependencies**: None
**Related**: kotlin-reviewer, kotlin-build-resolver
**Domain**: Kotlin, Kotest, MockK

### python-testing
**Purpose**: Python testing strategies using pytest, TDD methodology
**When to use**: For Python testing
**Dependencies**: None
**Related**: python-reviewer
**Domain**: Python, pytest, fixtures, mocking

### rust-test
**Purpose**: Enforce TDD workflow for Rust, write tests first
**When to use**: For Rust testing
**Dependencies**: None
**Related**: rust-reviewer, rust-build-resolver
**Domain**: Rust, unit tests, integration tests

### e2e-runner
**Purpose**: End-to-end testing using Vercel Agent Browser with Playwright fallback
**When to use**: PROACTIVELY for generating, maintaining, and running E2E tests
**Dependencies**: None
**Related**: e2e-testing, webapp-testing
**Domain**: E2E testing, Playwright, browser automation

### e2e-testing
**Purpose**: Playwright E2E testing patterns, Page Object Model, configuration
**When to use**: For E2E test implementation
**Dependencies**: None
**Related**: e2e-runner, webapp-testing
**Domain**: Playwright, E2E patterns

### webapp-testing
**Purpose**: Toolkit for interacting with and testing local web applications using Playwright
**When to use**: Testing web applications
**Dependencies**: None
**Related**: e2e-testing, e2e-runner
**Domain**: Web testing, Playwright

## Framework-Specific Testing

### laravel-tdd
**Purpose**: Test-driven development for Laravel with PHPUnit and Pest
**When to use**: Laravel testing
**Dependencies**: None
**Related**: laravel-patterns, laravel-verification
**Domain**: Laravel, PHPUnit, Pest

### django-tdd
**Purpose**: Django testing strategies with pytest-django, TDD methodology
**When to use**: Django testing
**Dependencies**: None
**Related**: django-patterns, django-verification
**Domain**: Django, pytest-django

### springboot-tdd
**Purpose**: Test-driven development for Spring Boot using JUnit 5, Mockito
**When to use**: Spring Boot testing
**Dependencies**: None
**Related**: springboot-patterns, springboot-verification
**Domain**: Spring Boot, JUnit 5, Mockito

## Verification Skills

### verification-loop
**Purpose**: Comprehensive verification system for Claude Code sessions
**When to use**: Verification of completed work
**Dependencies**: None
**Related**: verification-before-completion
**Domain**: Quality assurance

### laravel-verification
**Purpose**: Verification loop for Laravel projects: env checks, linting, static analysis, tests
**When to use**: Laravel project verification
**Dependencies**: None
**Related**: laravel-tdd, laravel-patterns
**Domain**: Laravel

### django-verification
**Purpose**: Verification loop for Django projects: migrations, linting, tests with coverage
**When to use**: Django project verification
**Dependencies**: None
**Related**: django-tdd, django-patterns
**Domain**: Django

### springboot-verification
**Purpose**: Verification loop for Spring Boot projects: build, static analysis, tests
**When to use**: Spring Boot project verification
**Dependencies**: None
**Related**: springboot-tdd, springboot-patterns
**Domain**: Spring Boot
