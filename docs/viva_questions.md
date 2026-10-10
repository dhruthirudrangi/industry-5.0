# Viva Questions and Answers

1. What is Industry 5.0?  
   Industry 5.0 focuses on human-centricity, sustainability, and resilience while building upon Industry 4.0 capabilities.

2. How is Industry 5.0 different from Industry 4.0?  
   Industry 4.0 is about digitalisation and automation; Industry 5.0 adds social and ecological priorities into industrial transformation.

3. Why did you choose SMEs?  
   SMEs face different constraints and resource pressures than large companies, so a practical readiness model is valuable.

4. Why manufacturing SMEs?  
   The research foundation addresses manufacturing SMEs specifically, which have distinctive organisational and process maturity patterns.

5. What are the three Industry 5.0 pillars?  
   Sustainability, resilience, and human-centred design.

6. Why did you use Latino (2025)?  
   It provides the main maturity-model structure and weights used as the research-informed foundation for this project.

7. What are the seven dimensions?  
   People & Culture, Awareness on Industry 5.0 Production, Organizational Strategy, Value Chain & Processes, Smart Manufacturing Technology, Technology-Based Products & Services, and Industry 4.0 Technologies.

8. Why are the dimensions weighted?  
   They are weighted to reflect their relative importance in the maturity model and to make the final score transparent and explainable.

9. What is FAHP?  
   FAHP refers to fuzzy analytic hierarchy process, which is a method used in the research to derive importance weights.

10. How are item scores calculated?  
   Each item is scored on a 1–5 maturity scale, and the final item contributions are aggregated within the dimension using the published item weights.

11. How is the final score calculated?  
   A dimension score is calculated as a weighted mean of the item scores; then the overall score is the sum of the normalized dimension weights multiplied by each dimension score.

12. Why normalize weights?  
   Because the displayed dimension weights may sum to more than 1, so the score must be calculated using normalized internal weights.

13. What does maturity level mean?  
   It is a practical banding of overall readiness within the 1–5 scoring range.

14. Why use a 1–5 scale?  
   It provides a simple, interpretable maturity scale that allows both qualitative and quantitative assessment.

15. What is the role of evidence?  
   Evidence makes the assessment more credible and grounded in observable practice, though it is treated as an optional project-level feature.

16. What is your original contribution?  
   The original contribution is the implementation of a transparent digital decision-support system, including evidence capture, dashboards, what-if analysis, sensitivity analysis, prioritisation, and roadmap generation.

17. Are you copying the research paper?  
   No. The project uses the research model as a foundation, but it adds software features and explicit methodological caveats.

18. What parts come from the paper?  
   The seven dimensions, the item structure, the underlying weights, and the maturity concept are research-derived.

19. What parts did you develop?  
   The UI, evidence fields, scoring dashboard, recommendation logic, simulator, report generator, and synthetic validation scenarios were developed as project extensions.

20. How does the what-if simulator work?  
   It changes one or more dimension assumptions and recalculates the overall score to show the effect of potential improvement scenarios.

21. What is sensitivity analysis?  
   It tests how the overall maturity score changes when dimensions improve by a fixed amount, helping explain which dimensions most influence the final result.

22. Why did you use Streamlit?  
   It is lightweight, interactive, and suitable for building an academic decision-support prototype quickly and clearly.

23. Why Python?  
   Python is flexible, readable, and widely used for scientific and analytical software, including business decision-support systems.

24. Why did you use Plotly?  
   It provides interactive and professional visualisations suitable for readability and academic demonstration.

25. How did you validate the system?  
   Through automated tests, consistency checks, and three synthetic SME scenarios designed to show different maturity profiles.

26. Why use synthetic SMEs?  
   Because real SME data was not available within this academic prototype, and synthetic scenarios allow controlled demonstration without fabricating real company data.

27. What are the limitations?  
   It is a prototype rather than a validated audit tool, and the recommendation rules and evidence heuristics are design choices rather than scientific claims.

28. How could this be validated with real SMEs?  
   Through pilot deployment, expert review, longitudinal validation, and triangulation with interviews and operational performance data.

29. What happens if the user gives biased answers?  
   The tool still produces a deterministic score, but the result should be interpreted with caution because subjective self-assessment can bias the outcome.

30. How could machine learning be added in future?  
   It could enhance recommendation prioritisation, anomaly detection, and pattern analysis, but the core scoring should remain transparent and deterministic.
