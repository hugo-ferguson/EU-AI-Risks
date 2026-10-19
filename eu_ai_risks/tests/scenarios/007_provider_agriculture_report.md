# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Medium: 1
- Low: 8

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 1 as medium risk and 8 as low risk. The main review focus areas are accuracy robustness cybersecurity, ai literacy, data governance and post market monitoring. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 0 high, 1 medium, 8 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (2), ai literacy (1), data governance (1), post market monitoring (1).
- 2 low-risk requirements appear to describe a control or safeguard, but still needs clarification/evidence review.

**Recommended follow-up actions:**

- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** low

**Requirement:** The system shall ingest historical rental data, including equipment type, rental start and end dates, rental duration, location, rate charged, and customer segment, from uploaded files (CSV/Excel) or connected rental management systems.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 2 Scope (art:2)

**Analysis:** FR-01 is a data-ingestion requirement for a demand-forecasting system with no Annex III classification, so the high-risk provisions in Articles 10 and 15 do not clearly apply. No requirement-level gap is supported by the supplied provisions.

---

### FR-02

**Risk level:** low

**Requirement:** The system shall integrate external data sources that influence agricultural demand, including weather data, planting and harvest calendars, crop type and acreage statistics, commodity prices, and regional holidays.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 4 AI literacy (art:4); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-02 ingests external agricultural data for demand forecasting, but the system is not Annex III high-risk and no supplied provision applies to it at requirement level. The Article 10 and 15 obligations apply only to high-risk systems, so no requirement-level gap is raised.

---

### FR-03

**Risk level:** low

**Requirement:** The system shall clean and validate incoming data by detecting missing values, duplicates, and outliers, and shall flag or correct them according to configurable rules before use in forecasting.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 4 AI literacy (art:4)

**Analysis:** FR-03 provides a configurable cleaning and validation control for missing values, duplicates and outliers. The system is not classified high-risk (no Annex III point applies), so Article 10 and 15 apply only by analogy. The remaining gap is documentation: cleaning rules and the changes they make are not recorded.

**Risks:**

- Cleaning rules are configurable and flag or correct data, but the requirement does not say that rules, thresholds and corrections are documented or logged. Data-preparation operations such as cleaning are then not traceable, and the effect of outlier correction on forecast quality cannot be evidenced. [low] - Article 10(2)(c) (`art:10:p2:c`)
  - Category: `data_governance`
  - Action: Version the cleaning rule configuration and log per run the counts of records flagged, corrected and removed, with the rule applied. Retain these as data-governance evidence.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;

**Recommendations:**

- Version cleaning rules and log flagged, corrected and removed records per run so data preparation is traceable and its effect on forecasts can be reviewed.

---

### FR-04

**Risk level:** low

**Requirement:** The system shall generate demand forecasts for each equipment category (e.g., tractors, harvesters, balers, sprayers) at daily, weekly, and monthly granularity over a user-selected horizon of up to 24 months.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-04 is a demand forecasting function for agricultural equipment rentals. The system has no Annex III classification, so the high-risk obligations in Arts. 9, 13 and 15 do not clearly apply. The Art. 50 transparency provisions are not triggered either, because the output is numeric forecasts rather than synthetic content or direct interaction with natural persons. No requirement-level compliance gap is supported by the supplied provisions.

---

### FR-05

**Risk level:** low

**Requirement:** The system shall model seasonality, trends, and external drivers, and shall allow users to run what-if scenarios by adjusting inputs such as weather conditions, rental pricing, or fleet size.

**Articles selected from the index:** Article 4 AI literacy (art:4); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 6 Classification rules for high-risk AI systems (art:6); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-05 (seasonality modelling and what-if scenarios) describes a demand-forecasting function for agricultural equipment rentals. No Annex III point applies, so the system is not high-risk and the Article 15 obligations do not bind it. It does not interact with natural persons in a way that triggers Article 50, and it generates no synthetic content. No requirement-level compliance gap is supported by the supplied provisions.

---

### FR-06

**Risk level:** low

**Requirement:** The system shall display forecasts with confidence intervals on an interactive dashboard that supports filtering by equipment type, location, and time period, and comparison of forecasts against actual rentals.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-06 is a forecast dashboard for a system with no Annex III classification, so the high-risk transparency duties of Article 13 do not clearly apply and Article 50 is not triggered (no direct interaction with natural persons, no synthetic media). The only remaining gap is minor: AI literacy support for users who interpret confidence intervals.

**Risks:**

- The dashboard shows confidence intervals but does not require guidance on what they mean or on the forecast's limits, which users need to interpret AI outputs appropriately (AI literacy). [low] - Article 4(1) (`art:4:p1`)
  - Category: `ai_literacy`
  - Action: Add in-dashboard help text and user documentation explaining confidence intervals, how they are computed, accuracy limits (e.g. MAPE/RMSE from FR-07) and appropriate use of the forecasts.
  - Trace:
    - selected from the Act's index: ch:I GENERAL PROVISIONS > Article 4 AI literacy

**Cited provisions:**

- **AI literacy, Article 4(1)**
  > Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used.

**Recommendations:**

- Add in-dashboard explanations of confidence intervals and forecast limitations, plus short user training material, to support users' AI literacy.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall measure forecast accuracy using metrics such as MAPE and RMSE, and shall retrain or recalibrate models automatically as new rental data becomes available.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 4 AI literacy (art:4)

**Analysis:** FR-07 measures accuracy and automatically retrains models, but it sets no acceptance thresholds, no validation gate before a retrained model goes live, and no feedback-loop safeguards. The system is not classified under Annex III, so these gaps are low-impact and mostly good-practice items if Article 15 is applied voluntarily or by analogy.

**Risks:**

- Automatic retraining on new rental data has no stated validation gate, performance threshold, rollback, or feedback-loop mitigation. Forecasts and fleet recommendations feed back into rental behaviour, which could degrade performance or reinforce bias without detection. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-03 (validation of incoming data (missing values, duplicates, outliers) before it is used in forecasting)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add a champion/challenger gate so a retrained model is promoted only if it meets predefined MAPE/RMSE thresholds. Add versioning and rollback, and monitor for feedback loops between recommendations and the rental data used for retraining.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Accuracy metrics are measured, but no target levels are defined, and there is no requirement to declare the metrics and achieved accuracy to users in the instructions of use. [low] - Article 15(3) (`art:15:p3`)
  - Partly addressed by: FR-06 (displays confidence intervals and compares forecasts against actual rentals)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define target MAPE/RMSE levels per equipment category and horizon. Document the metrics and the achieved accuracy in the user documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Measured accuracy is not tied to a post-market monitoring process that collects and analyses performance data over the system's lifetime, for example drift detection or reporting of degradation. [low] - Article 72(2) (`art:72:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `post_market_monitoring`
  - Action: Log accuracy metrics per model version over time, with drift alerts and a periodic review process documented in a monitoring plan.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.

**Recommendations:**

- Add a validation gate with predefined thresholds, versioning and rollback for automatic retraining, and monitor for feedback loops.
- Define target accuracy levels and declare the metrics in user documentation.
- Track accuracy and drift per model version over time within a documented monitoring plan.

---

### FR-08

**Risk level:** low

**Requirement:** The system shall provide fleet and inventory recommendations, such as identifying expected shortages or surpluses by season and location, and shall alert users when forecasted demand exceeds available fleet capacity.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-08 is a demand-forecast and fleet recommendation feature for business planning, with no Annex III classification and no direct interaction with natural persons or synthetic content. No supplied provision creates a requirement-level compliance gap. The Article 9, 13 and 15 obligations apply only to high-risk systems, so they are not cited here.

---

### FR-09

**Risk level:** low

**Requirement:** The system shall export forecasts and reports in common formats (CSV, Excel, PDF) and shall provide an API for integration with other business systems, with role-based access control restricting data and features by user role.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 4 AI literacy (art:4); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-09 covers export formats, an integration API and role-based access control. The system has no Annex III classification, so the high-risk obligations in Article 15 are not clearly triggered by this requirement. No requirement-level gap is supported by the supplied provisions.

---
