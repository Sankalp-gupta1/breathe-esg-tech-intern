# DECISIONS.md

## Why Django REST Framework?

Django REST Framework was selected because:

- rapid backend development
- built-in admin panel
- easy serialization
- strong ORM support
- fast API prototyping

The admin interface also helped validate ingestion records quickly.

## Why React Frontend?

React was selected because:

- simple component-based UI
- fast iteration
- good API integration
- lightweight dashboard implementation

The frontend focuses on analyst review workflows.

## Why Separate DataSource and EmissionRecord?

The design intentionally separates:

- ingestion metadata
- normalized emissions rows

This improves traceability.

A normalized row can always be traced back to:

- original source
- upload file
- company
- ingestion timestamp

## Why Store Raw + Normalized Values?

Both raw and normalized values are stored to preserve:

- source-of-truth integrity
- auditability
- analyst visibility

This prevents loss of original imported values.

## Why Use Audit Logs?

Audit logs were added because ESG review workflows require traceability.

Every review decision should be visible later during audit.

The system stores:

- old status
- new status
- analyst comment
- timestamp

## Why Lock Approved Records?

Approved records become locked to simulate audit sign-off controls.

This prevents accidental modification after analyst approval.

## Why Simple Rule-Based Emission Factors?

This prototype uses static emission factors because:

- assignment focus is workflow design
- no external emission factor APIs were required
- deterministic calculations simplify testing

## Why REST APIs?

REST APIs were used because:

- frontend/backend separation
- easy testing
- scalable architecture
- integration-friendly design

## Why SQLite?

SQLite was used for simplicity and fast local development.

In production this could be replaced by:

- PostgreSQL
- MySQL
- Snowflake
