# Validation and synthetic scenarios

## Synthetic validation scenarios

The application includes three synthetic manufacturing SMEs to demonstrate system behaviour under different capability profiles:

- Traditional Engineering Components SME
- Digitally Transitioning Automotive Supplier SME
- Advanced Smart Manufacturing SME

These are clearly labelled as synthetic validation scenarios and are not presented as real company data.

## Consistency checks

The validation layer checks:

- all ones -> overall score = 1,
- all threes -> overall score = 3,
- all fives -> overall score = 5,
- score bounds 1 to 5,
- normalization of dimension weights,
- normalization of item weights,
- overall score must remain in range.

## Purpose

These checks validate the deterministic logic of the scoring model and ensure that the dashboard and simulator are based on a consistent underlying framework.
