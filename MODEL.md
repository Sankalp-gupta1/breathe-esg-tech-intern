# MODEL.md

## Overview

This prototype models an ESG data ingestion and review workflow for enterprise emissions data.

The system is designed around four core entities:

1. Company
2. DataSource
3. EmissionRecord
4. AuditLog

The goal is to keep source data traceable while allowing analysts to review normalized emissions records before audit sign-off.

## Company

Represents a tenant/client company.

This supports multi-tenancy because every data source and emission record belongs to a company.

Example:

- Tesla India

## DataSource

Represents the origin of imported data.

Supported source types:

- SAP
- Utility
- Travel

Each data source stores:

- company
- source type
- file name
- uploaded timestamp

This helps track where a row came from.

## EmissionRecord

This is the normalized emissions row.

It stores:

- company
- source
- activity date
- category
- scope
- raw quantity
- raw unit
- normalized quantity
- normalized unit
- emission factor
- estimated emissions in kgCO2e
- status
- notes
- lock status

## Scope Mapping

- Scope 1: Direct fuel usage from SAP fuel data
- Scope 2: Purchased electricity from utility data
- Scope 3: Business travel data

## Unit Normalization

The model stores both raw and normalized values.

Example:

- raw quantity: 500
- raw unit: liters
- normalized quantity: 500
- normalized unit: liters

This allows the system to preserve source truth while still giving analysts clean comparable data.

## Source of Truth Tracking

Each EmissionRecord links back to a DataSource.

This means every normalized record can be traced to:

- source type
- file name
- upload time
- client company

## Review Workflow

Records can have these statuses:

- PENDING
- APPROVED
- REJECTED
- SUSPICIOUS
- FAILED

When a record is approved, it is locked for audit.

## Audit Trail

AuditLog records every status change.

It stores:

- record
- action
- old status
- new status
- comment
- timestamp

This makes the analyst review process traceable.
