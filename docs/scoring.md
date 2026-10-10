# Scoring details

## Published weights

The paper provides the following dimension weights:

- D1 People & Culture = 0.39
- D2 Awareness on Industry 5.0 Production = 0.19
- D3 Organizational Strategy = 0.16
- D4 Value Chain & Processes = 0.10
- D5 Smart Manufacturing Technology = 0.07
- D6 Technology-Based Products & Services = 0.06
- D7 Industry 4.0 Technologies = 0.05

Their displayed sum is 1.02 and is therefore normalized internally before aggregation.

## Item weight structure

Each item includes a weight within its parent dimension. These are used to calculate the dimension score as a weighted mean.

## Formula

Dimension score:

$$
\text{Dimension Score} = \frac{\sum (\text{item score} \times \text{item weight})}{\sum (\text{item weights within dimension})}
$$

Overall score:

$$
\text{Overall Score} = \sum (\text{normalized dimension weight} \times \text{dimension score})
$$

The project uses a 1–5 maturity scale where:

- 1 = Absent / Very Low Maturity
- 2 = Initial / Ad Hoc
- 3 = Defined / Partially Systematic
- 4 = Managed / Integrated
- 5 = Optimized / Continuously Improved

## Transparency

The app makes the contributing items and dimension weights visible so a user can see why a score was produced. The logic is designed to be explainable and not opaque.
