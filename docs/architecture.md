# Architecture documentation

## Overview

This project is a modular Streamlit application for assessing Industry 5.0 readiness in manufacturing SMEs. The primary objective is to operationalise a research-informed maturity model into a transparent and explainable decision-support tool.

## Design principles

- research-informed, not research-claiming,
- transparent calculations,
- modularity,
- evidence-aware assessment,
- practical SME usability,
- reproducibility.

## Modules

### App entrypoint

- app.py: loads the Streamlit navigation and starts the application.

### Pages

Each page is a Streamlit module under the pages directory. They separate the user experience into profile, assessment, analysis, simulation, recommendations, roadmap, validation, and reporting.

### Engine

The calculation layer handles dimension and item weight normalization, maturity scoring, gap classification, sensitivity analysis, recommendations, and roadmap generation.

### Data

The data folder contains the 38-item item catalogue, the synthetic SME dataset, and recommendation rule templates.

### Database

The database layer supports simple persistence for company profiles, assessments, and responses using SQLite.

### Reports

The report layer generates HTML and PDF outputs for executive and methodological reporting.

## Strengths

- deterministic calculations,
- modular separation of concerns,
- practical professor/student-friendly structure,
- transparent model assumptions,
- easier future extension.

## Limitations

This is intentionally a lightweight project architecture rather than a production-grade enterprise platform. The design is intentionally simple and suitable for academic demonstration and student development.
