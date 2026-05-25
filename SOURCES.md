# SOURCES.md

## Supported Data Sources

This prototype supports three ingestion source types:

1. SAP exports
2. Utility provider files
3. Travel/vendor reports

These sources simulate real enterprise ESG workflows.

---

## SAP Source

Purpose:

- Scope 1 fuel activity ingestion

Examples:

- Diesel fuel
- Natural gas
- Generator fuel

Typical fields:

- fuel type
- liters consumed
- activity date

Mapped to:

- Scope 1 emissions

---

## Utility Source

Purpose:

- electricity usage ingestion

Examples:

- electricity bills
- utility CSV exports

Typical fields:

- kWh consumed
- billing period
- facility information

Mapped to:

- Scope 2 emissions

---

## Travel Source

Purpose:

- business travel activity ingestion

Examples:

- flight reports
- vendor travel exports

Typical fields:

- distance traveled
- travel class
- transport type

Mapped to:

- Scope 3 emissions

---

## Normalization Strategy

Different source formats are normalized into a common emissions schema.

The system standardizes:

- quantity
- unit
- scope
- emissions calculation

This allows analysts to compare records consistently across multiple ingestion sources.

---

## Emission Factors

The prototype currently uses simplified static emission factors.

Examples:

- Diesel fuel → 2.68
- Electricity → 0.82
- Flights → 0.15

These are placeholder factors intended for workflow demonstration only.

---

## Auditability

Every normalized record retains links to:

- source type
- upload file name
- company
- upload timestamp

This ensures traceability during analyst review and audit workflows.
