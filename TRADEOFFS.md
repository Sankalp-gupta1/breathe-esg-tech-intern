# TRADEOFFS.md

## SQLite vs PostgreSQL

SQLite was selected for speed and simplicity during prototype development.

Tradeoff:

- easier setup
- faster local testing

But:

- not ideal for production concurrency
- limited scalability

Production recommendation:

- PostgreSQL

## Static Emission Factors vs External Factors API

The prototype uses static emission factors.

Advantages:

- deterministic calculations
- simple testing
- no external dependency

Tradeoff:

- not dynamically updated
- not region specific

Future improvement:

- integrate official emissions factor datasets

## Manual Review Workflow vs Full Automation

The system intentionally keeps analysts in the review loop.

Advantages:

- human verification
- suspicious data detection
- audit accountability

Tradeoff:

- slower processing
- requires reviewer actions

## Simple Role Model vs Enterprise RBAC

This prototype uses Django admin authentication only.

Advantages:

- fast implementation
- simpler architecture

Tradeoff:

- no granular permissions
- no reviewer hierarchy

Future improvement:

- role-based access control

## REST API vs GraphQL

REST APIs were selected because:

- easier implementation
- predictable endpoints
- simpler frontend integration

Tradeoff:

- less flexible querying

## Frontend Simplicity vs Full Enterprise UX

The frontend focuses only on core analyst workflows.

Advantages:

- rapid delivery
- easier debugging
- assignment-focused scope

Tradeoff:

- limited visual analytics
- limited filtering/search

## Hard Locking Approved Records

Approved records are locked permanently.

Advantages:

- stronger audit consistency
- prevents accidental edits

Tradeoff:

- requires admin override if mistakes happen

Future improvement:

- reversible approval workflow
