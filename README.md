# Industry 5.0 SME Readiness Assessment and Decision-Support System

## Project title

Industry 5.0 SME Readiness Assessment and Decision-Support System

Alternative title:
An Interactive Industry 5.0 Maturity Assessment and Digital Transformation Roadmap for Manufacturing SMEs

## Problem statement

Manufacturing SMEs face a difficult transition from digitalisation-driven Industry 4.0 practices to broader Industry 5.0 priorities centred on human-centricity, sustainability, and resilience. The challenge is not only to adopt technology, but also to assess maturity in a structured, transparent, and evidence-aware way across strategy, people, processes, and technologies.

## Motivation

The project responds to the need for an accessible, research-informed decision-support tool for SMEs that are considering Industry 5.0 readiness. It is designed as an academic prototype to help decision-makers:

- understand the transition from Industry 4.0 to Industry 5.0,
- assess current maturity on a transparent 1–5 scale,
- interpret capability gaps,
- plan digital and organisational improvements,
- simulate change scenarios,
- and generate a structured roadmap without claiming formal scientific validation.

## Research background

The main research foundation is the maturity model proposed by Latino (2025): a seven-dimension Industry 5.0 assessment for manufacturing SMEs that integrates sustainability, resilience, and human-centred design. This project draws on that model while making its own software extensions explicit.

The conceptual framing for Industry 5.0 is informed by the European Commission's work on Industry 5.0 as a human-centric, sustainable, and resilient industrial model. It is positioned as a continuation and extension of Industry 4.0 and not as a replacement of it.

## Objectives

1. Assess current Industry 5.0 maturity in manufacturing SMEs.
2. Provide a transparent weighted scoring model with traceable calculations.
3. Capture optional evidence and notes for each assessment item.
4. Report scores across seven dimensions and three project-specific pillar diagnostics.
5. Show capability gaps and prioritise improvement opportunities.
6. Support what-if and sensitivity analysis.
7. Generate a practical, model-based roadmap.
8. Validate the logic using three synthetic SME scenarios.
9. Produce downloadable report outputs.
10. Clearly distinguish research-derived elements from project-specific extensions.

## Features

- 7-dimension maturity model based on Latino (2025)
- 38 research-derived maturity items
- 1–5 maturity scale with operational anchors
- weighted scoring with normalized dimension weights
- evidence and confidence capture
- gap analysis with project-defined thresholds
- recommendation engine
- what-if simulator
- sensitivity analysis
- personalised roadmap generator
- synthetic validation scenarios
- CSV and JSON export
- HTML/PDF reporting
- Streamlit dashboard with a single grouped navigation and interactive score visualisations

The dashboard presents maturity by dimension and pillar, prioritises capability gaps, and
compares current and simulated dimension scores. These visualisations are descriptive
decision-support tools and do not imply causal or forecasted business outcomes.

## Architecture

```text
project/
├── app.py
├── pages/
│   ├── home.py
│   ├── about.py
│   ├── company.py
│   ├── assessment.py
│   ├── results.py
│   ├── dimensions.py
│   ├── pillars.py
│   ├── gaps.py
│   ├── what_if.py
│   ├── sensitivity.py
│   ├── recommendations.py
│   ├── roadmap.py
│   ├── validation.py
│   ├── reports.py
│   └── methodology.py
├── data/
│   ├── questions.json
│   ├── companies.json
│   └── recommendations.json
├── engine/
│   ├── scoring.py
│   ├── maturity.py
│   ├── pillar_analysis.py
│   ├── gap_analysis.py
│   ├── sensitivity.py
│   ├── recommendations.py
│   └── roadmap.py
├── database/
│   ├── db.py
│   └── schema.sql
├── reports/
│   └── report_generator.py
├── tests/
│   ├── test_scoring.py
│   ├── test_weights.py
│   ├── test_validation.py
│   └── test_what_if.py
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── scoring.md
│   ├── validation.md
│   └── viva_questions.md
├── requirements.txt
├── README.md
├── .gitignore
├── utils.py
└── app.py
```

## Technology stack

- Python 3.11+
- Streamlit
- Plotly (used in the dashboard layer and extensible visualisation work)
- Pandas
- NumPy
- SQLite
- ReportLab
- Pytest

## Installation

1. Clone the project.
2. Open a terminal in the project folder.
3. Create a virtual environment if needed.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to run

```bash
streamlit run app.py
```

or:

```bash
python -m streamlit run app.py
```

## Scoring methodology

The project uses the published Latino (2025) dimension weights and item weights as the research-derived foundation. The displayed dimension weights are stored as published values, then normalized internally before calculating the overall score.

For each dimension:

Dimension score = weighted mean of item scores within the dimension.

Overall score = sum of normalized dimension weight × dimension score.

The score range is 1.00–5.00.

Maturity levels are defined as:

- 1.00–1.99 = Level 1 — Outsider
- 2.00–2.99 = Level 2 — Beginner
- 3.00–3.99 = Level 3 — Advanced
- 4.00–5.00 = Level 4 — Senior

This is a deterministic, transparent calculation and not a black-box model.

## Pillar methodology

The three pillars are:

- Sustainability
- Resilience
- Human-Centered Design / Human-Centricity

The project uses an explicit project-specific diagnostic aggregation to profile the pillars. This aggregation is not presented as the original paper's exact mathematical method. The UI labels it clearly as a software diagnostic extension.

## What-if methodology

The what-if simulator changes one or more dimension-level assumptions and recalculates the overall score. It is a mathematical scenario tool designed for decision support, not a real-world prediction model.

## Validation methodology

The system includes three synthetic SMEs to demonstrate how different capability profiles produce different maturity results. They are labelled explicitly as synthetic validation scenarios and are not presented as real companies.

Consistency validation checks include:

- all scores = 1
- all scores = 3
- all scores = 5
- score bounds
- dimension weight normalization
- item weight normalization
- what-if change calculation

## Limitations

- This is an academic prototype, not a certified audit instrument.
- The synthetic validation cases do not represent real manufacturing SMEs.
- The evidence confidence field is a project heuristic, not a validated scientific measure.
- The recommendation rules are rule-based heuristics and not scientifically validated.
- The roadmap is model-based and should be treated as decision support rather than a guaranteed implementation forecast.

## Sources

- Latino, M. E. (2025). A maturity model for assessing the implementation of Industry 5.0 in manufacturing SMEs: learning from theory and practice. Technological Forecasting and Social Change, 214, 124045.
- European Commission. Industry 5.0.
- European Commission. Industry 5.0 – Towards a sustainable, human-centric and resilient European industry.
- acatech. Industrie 4.0 Maturity Index Update 2020.

## Future work

Possible extensions include:

- integration with real SME data,
- richer analytics and uncertainty bands,
- assessment history and longitudinal tracking,
- more advanced recommendation logic,
- ontology or semantic linking of evidence to maturity items,
- and export features for institutional or consultancy use.

## Academic integrity statement

The software is research-informed and explicitly distinguishes between research-derived concepts and project-specific additions. It does not claim to reproduce the original research instrument verbatim, nor to provide statistically validated industry certification.
