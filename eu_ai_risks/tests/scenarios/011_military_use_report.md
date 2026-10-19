# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 5
- Medium: 5

### Overall analysis

Overall, the assessment reviewed 10 requirements and rated 5 as high risk and 5 as medium risk. The main review focus areas are accuracy robustness cybersecurity, human oversight, data governance, record keeping and transparency. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 10 requirements reviewed in total.
- Risk distribution: 5 high, 5 medium, 0 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (9), human oversight (7), data governance (5), record keeping (2), transparency (2).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** high

**Requirement:** The system shall ingest data from authorized military and intelligence sources, including surveillance feeds, signals intelligence, travel and border records, open-source information, and informant reports, and normalize it into a unified format for analysis.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 2 Scope (art:2); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 12 Record-keeping (art:12); Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-01 ingests heterogeneous intelligence data (informant reports, SIGINT, open-source, travel records) with no stated provenance, quality, or integrity controls. Those data feed profiling and risk scoring and retraining (FR-10), so unvetted or poisoned inputs could cause biased or erroneous designations of individuals.

**Risks:**

- No data governance for ingested sources: origin, original collection purpose, and preparation/normalization operations are not recorded or assessed, nor are suitability, representativeness, or error/completeness of data later used for training, validation, and testing. [medium] - Article 10(2)(b) (`art:10:p2:b`)
  - Category: `data_governance`
  - Action: Add per-source provenance metadata (origin, collection purpose, legal basis), documented normalization/cleaning steps, and source-quality and completeness checks before data enter profiles or training sets.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(c))
- Requirement does not examine ingested data for bias (e.g., nationality, ethnicity, travel patterns, unreliable informant or open-source content) that could lead to discriminatory profiling, nor mitigate it. FR-10 only monitors bias after model updates. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: FR-10 (monitoring for bias in feedback-driven retraining (post-update), not examination or mitigation of source data at ingestion)
  - Category: `data_governance`
  - Action: Define bias examination of each source and feature (including proxies for protected characteristics), with mitigation and acceptance criteria applied at ingestion and before data are used for training.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(c))
- No integrity, authenticity, or validation controls on external feeds; untrusted or manipulated inputs (e.g., fabricated informant or open-source data) could poison data or alter outputs, especially given retraining on this data. [high] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-08 (access restriction for users, not integrity of ingested inputs)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add source authentication, schema/anomaly validation, quarantine of suspect records, and data-poisoning detection at ingestion; keep a reliability rating per source.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(b)**
  > (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Record provenance, collection purpose and normalization steps per source, and set data quality criteria for ingestion.
- Add bias examination and mitigation of source data and features before they reach profiling or training.
- Implement input authentication, validation, quarantine and poisoning detection for all ingested feeds.

---

### FR-02

**Risk level:** high

**Requirement:** The system shall resolve and link records that refer to the same individual or entity across multiple data sources, maintaining a consolidated profile for each person of interest.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 2 Scope (art:2); Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-02 links records across sources into consolidated person profiles but sets no entity-resolution accuracy targets, no handling for false merges, and no data-governance practices for the matching process. Wrongly merged profiles would feed risk scores and designations for the wrong individuals.

**Risks:**

- No accuracy or error-rate metrics are defined for entity resolution (false merges and missed links), and none are to be declared. A false merge puts one person's data into another's profile and carries into risk scoring. [high] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test precision/recall targets for record linkage, set confidence thresholds for automatic merges, route low-confidence matches to analyst review, and declare the metrics in the instructions of use (15(3)).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The resolution and consolidation steps (matching rules, enrichment, aggregation across heterogeneous sources) have no governance requirements for data origin, quality, errors, completeness or bias, for example name-transliteration mismatches that affect some nationalities more than others. [medium] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: FR-10 (monitoring for bias and performance degradation on model updates (10(2)(f)-(g)); does not address linkage)
  - Category: `data_governance`
  - Action: Document the matching and aggregation operations, record the provenance of each linked record, and test linkage error rates across nationality, ethnicity and language groups, with mitigation for any disparities found.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(b))
- The requirement offers no way to detect, review or reverse wrongly merged or split profiles, so analysts cannot spot or correct linkage errors that distort the outputs they rely on. [medium] - Article 14(4)(a) (`art:14:p4:a`)
  - Partly addressed by: FR-06 (analyst confirm/override/dismiss of AI-generated assessments (14(4)(d)); applies to assessments, not profile linkage)
  - Category: `human_oversight`
  - Action: Show match confidence and the contributing source records on each profile, and let analysts split, merge or unlink records with a logged justification.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
- **Human oversight, Article 14(4)(a)**
  > (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance;

**Recommendations:**

- Set and declare entity-resolution accuracy metrics and thresholds, with low-confidence matches sent to human review.
- Document linkage data governance and test for bias in matching across demographic groups.
- Provide match-confidence display and analyst split/unlink controls with logged justification.

---

### FR-03

**Risk level:** high

**Requirement:** The system shall analyze each profile using configurable behavioral, relational, and movement-pattern indicators to detect anomalies and activities associated with hostile or foreign-agent behavior.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 2 Scope (art:2); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-03 profiles individuals using behavioral, relational and movement indicators to flag hostile or foreign-agent behavior, but sets no basis requirement (objective, verifiable facts) and no data-quality, bias or accuracy criteria for the indicators. Profiling-based risk assessment could fall under Art. 5(1)(d) or (c) if used in a law-enforcement or social-scoring context. Indicator choice and thresholds are also left unvalidated.

**Risks:**

- Indicators are configurable and profile-based, with no constraint that anomaly or hostile-agent flags rest on objective, verifiable facts linked to specific activity. Flags driven solely by profiling or personality or behavioral characteristics risk the Art. 5(1)(d) prohibition on predicting criminal offences, or Art. 5(1)(c) social-scoring-type unfavourable treatment. [high] - Article 5(1)(d) (`art:5:p1:d`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-06 (human review and authorization before a designation is finalized, supporting human assessment of the person's involvement)
  - Category: `other`
  - Action: Define the use context and confirm whether Art. 5 applies (law enforcement vs. purely military or national-security use). Require that flags are supported by objective, verifiable facts directly linked to specific activity. Prohibit indicators based solely on personality traits or characteristics, and document this exclusion in the indicator configuration policy.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
- Behavioral, relational and movement indicators are configurable, but there is no requirement for data governance over the indicators and underlying data. This covers design choices, assumptions about what the indicators represent, bias examination for protected or proxy attributes (e.g., ethnicity or nationality via movement and relationship patterns), and representativeness. [medium] - Article 10(2) (`art:10:p2`)
  - Partly addressed by: FR-10 (monitoring for bias and false positives on retraining; does not examine the initial indicator design)
  - Category: `data_governance`
  - Action: Document the design rationale and assumptions for each indicator. Add a bias examination covering proxy features for protected characteristics and mitigation measures. Require governed change control and validation before any indicator configuration reaches production.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No accuracy or robustness expectations are specified for anomaly detection. This includes false-positive rates, handling of noisy or adversarially planted data (e.g., spoofed movement or informant data), and consistency when indicators are reconfigured. [medium] - Article 15(1) (`art:15:p1`)
  - Partly addressed by: FR-10 (monitoring performance degradation and false positives after deployment)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics and target false-positive and false-negative thresholds for anomaly detection and declare them in the instructions of use. Add robustness tests against manipulated inputs (adversarial or poisoned data), and re-validate after any indicator configuration change.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(d)**
  > (d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence, based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity;
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Establish the Art. 5 applicability analysis and require objective, verifiable factual grounding for flags; exclude profiling-only or trait-based flags.
- Add documented design, assumption and bias-examination controls for each indicator, with validated change control for configuration.
- Declare accuracy metrics and thresholds, and add robustness and adversarial testing for the anomaly detection.

---

### FR-04

**Risk level:** high

**Requirement:** The system shall assign each individual a risk score and risk category (e.g., low, moderate, high), along with a confidence level and a human-readable explanation of the factors that contributed to the assessment.

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 86 Right to explanation of individual decision-making (art:86); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-04 provides a score, category, confidence level and explanation, but does not specify accuracy metrics or calibration for the score and confidence, or the limitations and instructions deployers need to interpret them. Without these, analysts could over-rely on opaque profiling outputs that affect individuals' rights.

**Risks:**

- The requirement does not define how the confidence level is calibrated, nor the accuracy metrics and error rates (e.g., false positives) behind the score and categories, so these cannot be declared in the instructions for use. [high] - Article 15(3) (`art:15:p3`)
  - Partly addressed by: FR-10 (monitoring for false positives and performance degradation (15(1) consistent performance across lifecycle))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy and calibration metrics for the score, category and confidence (including per-category false-positive and false-negative rates and subgroup performance). Set acceptance thresholds and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The explanation is only required to be 'human-readable'. The requirement sets no content standard (feature attribution, data provenance, known limitations) that would let deployers interpret the output and its limits correctly. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Specify the explanation content: top contributing factors with weights, source records and their reliability, confidence meaning, and known limitations. Document these in the instructions for use under Art. 13(3)(b)(iv),(vii).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- The requirement does not support oversight interpretation, such as warnings against automation bias or presenting scores as advisory. The score and category could be over-relied on, and FR-06 covers only the review/override step. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-06 (ability to confirm, override or dismiss assessments (14(4)(d)))
  - Category: `human_oversight`
  - Action: Display scores with advisory labelling, confidence and uncertainty ranges, and limitation notices. Add analyst training on automation bias and on interpreting the outputs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;

**Recommendations:**

- Define and declare accuracy, calibration and error-rate metrics, with acceptance thresholds, for the score, category and confidence level.
- Specify the explanation content and limitations needed for deployers to interpret outputs, and document them in the instructions for use.
- Add automation-bias safeguards and interpretation aids to the score presentation, and provide analyst training.

---

### FR-05

**Risk level:** medium

**Requirement:** The system shall generate real-time alerts to designated analysts and commanders when an individual’s risk score crosses a defined threshold or when a high-priority pattern is detected.

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-05 pushes real-time threshold and pattern alerts to analysts and commanders, but does not require the alert to carry context (score confidence, explanation, limitations) or any automation-bias safeguard. Alerts could be over-relied upon before the FR-06 review gate applies.

**Risks:**

- Alerts are triggered purely on a score threshold or pattern, with no requirement that they include confidence, contributing factors, or limitation notices. Recipients may be unable to correctly interpret the alert or may over-rely on it (automation bias). [medium] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-04 (confidence level and human-readable explanation of factors, which support output interpretation (14(4)(c)) but are not stated to be carried in the alert); FR-06 (analyst ability to confirm, override or dismiss AI assessments with recorded justification (14(4)(d)))
  - Category: `human_oversight`
  - Action: Require each alert payload to include the score, confidence level, top contributing factors, data provenance and a link to the profile. Add a short automation-bias and limitations notice, and show the threshold that was crossed.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The threshold and the high-priority pattern definitions are unspecified. No accuracy or false-positive metrics are tied to alerting, so alert reliability (and the cost of false alerts for the individuals flagged) is not assessed or declared. [medium] - Article 15(1) (`art:15:p1`)
  - Partly addressed by: FR-10 (monitoring of bias, false positives and performance degradation after model updates)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define threshold-setting governance and validate alert precision and recall against target values. Declare the alert accuracy metrics in the instructions for use. Monitor alert false-positive rates and re-validate whenever thresholds or models change.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Alert delivery is real-time, but there is no requirement for operators to pause or halt alerting, or for alert-driven workflows to fail safe, if the system malfunctions or produces anomalous alert volumes. [low] - Article 14(4)(e) (`art:14:p4:e`)
  - Category: `human_oversight`
  - Action: Add an authorized control to suspend or throttle alerting, with anomaly detection on alert volume, and fail to a safe state that leaves existing reviews unaffected.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.

**Recommendations:**

- Specify the alert payload contents (score, confidence, factors, limitations notice, automation-bias warning).
- Define threshold governance and validate and declare alert accuracy and false-positive metrics.
- Add an operator control to suspend or throttle alerting, with anomaly detection on alert volume.

---

### FR-06

**Risk level:** medium

**Requirement:** The system shall require human analyst review and authorization before any high-risk designation is finalized or any operational action is recommended, and shall allow analysts to confirm, override, or dismiss AI-generated assessments with recorded justification.

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 12 Record-keeping (art:12); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-06 provides a strong human authorization, confirm/override/dismiss and justification-recording control. The remaining gaps are that it has no measures against automation bias or for interpreting outputs (Art. 14(4)(b),(c)), and no stop/interrupt capability for the system as a whole (Art. 14(4)(e)).

**Risks:**

- No measure keeps analysts aware of automation bias or helps them interpret scores and confidence, even though the system recommends high-risk designations and operational actions. Nothing requires analyst training, warnings or anchoring safeguards, and the explanation in FR-04 does not address over-reliance. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-04 (human-readable explanation and confidence level that support interpreting the output (14(4)(c)))
  - Category: `human_oversight`
  - Action: Add to FR-06 automation-bias safeguards: display of limitations and confidence next to each recommendation, a requirement that the analyst records independent reasoning before confirming, and periodic monitoring of override and confirmation rates. Define the competence and training required of authorizing analysts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- Analysts can override individual assessments, but no requirement lets them halt or suspend the system, or stop it generating alerts and recommendations, and bring it to a safe state. [low] - Article 14(4)(e) (`art:14:p4:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-06 (override or dismissal of individual outputs (14(4)(d)))
  - Category: `human_oversight`
  - Action: Add a requirement for an authorized-role control to pause or stop scoring, alerting and recommendation generation, with the system left in a safe state and the action logged.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.

**Recommendations:**

- Add automation-bias safeguards, output-interpretation aids and analyst competence criteria to FR-06.
- Add a system-level stop/suspend function for scoring and alerting, with logging.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall provide analysts with a dashboard for searching, filtering, and visualizing profiles, relationship networks, geographic activity, and risk trends.

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 12 Record-keeping (art:12); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-07 defines a dashboard for searching and visualizing profiles, networks, geography and risk trends, but says nothing about presenting accuracy limits, uncertainty or interpretation aids, or about countering automation bias. Analysts could over-rely on visualized risk trends and network graphs without understanding the system's limitations.

**Risks:**

- The dashboard does not require showing the information analysts need to interpret outputs correctly (confidence, accuracy limits, data provenance, explanation of network and trend visualizations); FR-04 supplies this only for the individual risk score, not for the dashboard's other views. [medium] - Article 13(1) (`art:13:p1`)
  - Partly addressed by: FR-04 (confidence level and human-readable explanation of factors for each risk score (13(3)(b)(iv),(vii) at the score level only))
  - Category: `transparency`
  - Action: Specify that dashboard views of risk trends, relationship networks and geographic activity display confidence levels, data source and recency, known limitations, and drill-down to contributing factors, using the FR-04 explanation outputs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- As the main human-machine interface, the dashboard has no stated features to make oversight effective, such as anomaly or dysfunction indicators, automation-bias warnings, or aids for interpreting outputs. FR-06 covers review and override, but not the interface support for them. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-06 (ability to confirm, override or dismiss AI assessments with recorded justification (14(4)(d)))
  - Category: `human_oversight`
  - Action: Add dashboard requirements for model-health and anomaly indicators, automation-bias cautions on scores and trends, and access to interpretation tools. Place confirm, override and dismiss controls from FR-06 directly in the profile views.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;

**Recommendations:**

- Require the dashboard to show confidence, provenance, limitations and factor drill-down for every visualization, not just the individual score.
- Add oversight-supporting interface features: anomaly and performance indicators, automation-bias warnings, interpretation aids, and in-view override controls.

---

### FR-08

**Risk level:** medium

**Requirement:** The system shall enforce role-based and clearance-based access control, ensuring users can view only the data and profiles permitted by their authorization level.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10); Article 12 Record-keeping (art:12)

**Analysis:** FR-08 provides role- and clearance-based access control, which substantively supports Article 15 cybersecurity. The remaining gap is that it does not cover authentication strength or protection against attacks beyond authorization. The audit log in FR-09 covers part of the access accountability.

**Risks:**

- Access control is limited to authorization-level view restrictions. It does not specify authentication strength, protection against unauthorised third parties altering the system's use, outputs or profile data, or AI-specific attack controls (data poisoning, model evasion, confidentiality attacks), so the cybersecurity resilience demanded by Art. 15(5) is only partly implemented. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-09 (tamper-proof logging of data access and system changes, which supports detecting unauthorised alteration)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend FR-08 with strong authentication (MFA), least-privilege and segregation of duties for write/modify rights over data, thresholds and models, session controls, and a threat model covering data/model poisoning, evasion and confidentiality attacks, with security testing against it.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Extend FR-08 with strong authentication, least-privilege write controls over data, thresholds and models, and a threat model plus security tests for AI-specific attacks.

---

### FR-09

**Risk level:** medium

**Requirement:** The system shall maintain a tamper-proof audit log of all data access, risk assessments, analyst decisions, and system changes to support accountability and oversight.

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-09 provides a tamper-proof audit log of access, assessments, decisions and changes, which largely supports traceability. It does not specify the Article 12(2) event purposes (risk/substantial-modification detection, post-market monitoring, deployer monitoring) or a retention period, so it may not meet record-keeping obligations for a high-risk system.

**Risks:**

- The log scope is access, assessments, decisions and changes, but it is not tied to events relevant for identifying risk situations or substantial modifications, post-market monitoring, or deployer operation monitoring (e.g., anomalies, score drift, overrides, errors, incidents). [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-06 (records analyst confirm/override/dismiss decisions with justification (a subset of the events to be logged))
  - Category: `record_keeping`
  - Action: Define the log event schema around Art. 12(2)(a)-(c): model version and configuration changes, threshold crossings, anomalous or out-of-distribution inputs, override rates, errors, and suspected incidents. Make the logs exportable for post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- No retention period is specified for the audit logs. Providers and deployers must keep automatically generated logs for a period appropriate to the intended purpose, and for at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Add a configurable retention requirement of at least six months, longer where the intended purpose or applicable law requires it. Reconcile it with data protection law, and enforce it with retention and deletion controls that preserve log integrity.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- 'Tamper-proof' is asserted without specifying integrity mechanisms or access restrictions on the log itself. The log must resist alteration by unauthorised parties and remain reliable for accountability. [low] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-08 (role- and clearance-based access control that can restrict who may access data, including logs)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify the mechanisms, e.g. append-only or WORM storage, hash chaining or signing, separate log administration, and integrity verification and alerting. Document them as evidence.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define the audit event schema against Art. 12(2)(a)-(c), including model changes, threshold events, anomalies, overrides and incidents.
- Add a log retention requirement of at least six months, reconciled with data protection law.
- Specify the log integrity mechanisms (append-only storage, hash chaining or signing, restricted log administration) and document them as evidence.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall support feedback-driven model updates, allowing confirmed outcomes and analyst corrections to be used to retrain and evaluate the models, while monitoring for bias, false positives, and performance degradation.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** FR-10 retrains models on analyst corrections and confirmed outcomes and monitors for bias and degradation. It leaves out feedback-loop mitigation, quality governance of the retraining data, pre-deployment acceptance criteria for updated models, and protection of the feedback channel against poisoning. Because analyst-confirmed designations feed future model behaviour, biased outputs could reinforce themselves.

**Risks:**

- Retraining on analyst-confirmed outcomes, which themselves rest on the system's earlier risk scores, creates a feedback loop. The requirement monitors for bias but defines no mitigation to stop biased outputs from influencing future training inputs. [high] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add feedback-loop controls: separate ground truth from model-influenced labels, correct for selection and confirmation bias, cap the weight of feedback-derived samples, and set bias thresholds that halt retraining when exceeded.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Feedback data (analyst corrections and confirmed outcomes) is used for retraining with no stated governance. Nothing covers provenance, labelling quality, representativeness, error checks, or bias examination and mitigation for the retraining sets. [high] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: FR-09 (records analyst decisions and system changes, which gives provenance for feedback labels only)
  - Category: `data_governance`
  - Action: Define data governance for retraining sets: record the origin and labelling process of feedback data, test for representativeness and bias across affected groups, document mitigations, and version the datasets.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement says models are retrained and evaluated but sets no predefined metrics, thresholds, or release gate for updated models. Accuracy could degrade or change across updates without being caught before redeployment. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Define accuracy, false-positive and subgroup-parity metrics and thresholds. Require updated models to pass them before deployment, with rollback to the prior version on failure, and re-run the risk assessment for each material update.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Analyst corrections and outcome labels flow into training, but the requirement has no integrity controls against data or model poisoning, whether malicious or from compromised insiders or sources. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-08 (role-based and clearance-based access control that can limit who accesses data, though it does not address training-data poisoning)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Validate and authenticate feedback inputs, detect anomalous label patterns, restrict who can submit training feedback, and require approval before feedback enters retraining.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Monitoring for bias, false positives and degradation is stated, but it is not tied to a documented post-market monitoring plan. No collection scope, cadence, or escalation path is defined for evaluating continued compliance. [low] - Article 72(2) (`art:72:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `post_market_monitoring`
  - Action: Link the monitoring to a documented post-market monitoring plan that specifies metrics, frequency, thresholds, and escalation, and feeds the risk management review.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.

**Recommendations:**

- Add feedback-loop mitigation: separate ground truth from model-influenced labels, correct for confirmation bias, and halt retraining on bias thresholds.
- Establish data governance for retraining datasets: provenance, labelling quality, representativeness, bias examination and mitigation.
- Define predefined metrics and thresholds as a release gate for retrained models, with rollback and a risk assessment per update.
- Add integrity controls on the feedback channel to detect and prevent data and model poisoning.
- Tie the monitoring to a documented post-market monitoring plan with defined cadence, thresholds and escalation.

---
