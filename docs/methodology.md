# Methodology

## Research-derived foundation

The main research-informed baseline is the Latino (2025) maturity model for Industry 5.0 in manufacturing SMEs. This model proposes seven dimensions and 38 maturity items, with weights that reflect relative importance within the assessment framework.

The project adopts the seven dimensions and item structure from the paper, but makes its own software-layer extensions explicit in the interface and documentation.

## Project-specific extensions

The following are project additions and are not presented as validated scientific methodology from the paper:

1. Evidence capture for each item.
2. Interactive dashboarding and visualisation.
3. What-if simulator and sensitivity analysis.
4. Gap prioritisation heuristics.
5. Recommendation engine.
6. Model-based roadmap generation.
7. Synthetic SME validation scenarios.
8. Downloadable HTML/PDF reports.

## Scoring logic

The scoring engine computes dimension-level weighted means using the item weights within each dimension, then aggregates these to an overall score using normalized dimension weights.

All calculations remain deterministic and reproducible.

## Maturity interpretation

The maturity model uses four bands:

- Level 1 — Outsider
- Level 2 — Beginner
- Level 3 — Advanced
- Level 4 — Senior

These bands are implemented as project-level interpretation zones aligned with the research-informed score range.

## Academic integrity

This software is a research-informed prototype and not a validated audit tool. The differentiation between the research-derived framework and the project extension layer is explicit throughout the application.
