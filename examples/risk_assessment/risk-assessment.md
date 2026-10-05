# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 6
- Low: 8

## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** The requirement ingests candidate data for a high-risk recruitment AI system without specifying data governance practices (quality checks, provenance, bias examination) or documentation of data origin/collection processes.

**Risks:**

- No data governance or quality criteria defined for ingested resumes, cover letters, and application data feeding a high-risk recruitment system. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Define and document data collection provenance, quality checks, and relevance/representativeness criteria for ingested application data.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Implement documented data governance controls (validation, provenance tracking, quality checks) for all ingested application data.
- Add technical documentation covering design choices and data collection origin for the ingestion module.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** The requirement provides a review request channel but lacks specification of what disclosure candidates receive about the automated ranking's role and logic, which is needed to make review requests meaningful; no matching transparency-specific provision was supplied to fully ground this gap.

**Risks:**

- The review channel does not specify that candidates are informed of the ranking system's involvement, its role in the decision, and how to interpret/contest it, limiting the effectiveness of the requested review. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Define disclosure content (notice of automated ranking use, decision impact, and review request process) delivered to candidates before or at the point of decision.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Specify the transparency notice content and timing that accompanies the review channel so candidates understand the automated ranking's role before requesting review.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 scores candidates for employment recruitment (Annex III high-risk context) without specifying data governance, transparency, or accuracy controls for the scoring model, risking biased or opaque suitability decisions.

**Risks:**

- No specification of data quality, representativeness, or bias checks for training/scoring data used to derive suitability scores. [high] - Article 10(2)
  - Category: `data_governance`
  - Action: Define and document data governance practices covering data collection, provenance, and representativeness of applicant data used for scoring.
- No requirement that scoring data reflect statistical properties needed to avoid discriminatory outcomes across candidate groups. [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Add validation checks ensuring datasets are sufficiently representative across protected and relevant candidate subgroups.
- Scoring logic lacks transparency provisions to let recruiters interpret how scores are derived. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Provide documentation/instructions explaining scoring factors and their relative weighting to deployers.
- No mechanism described for human review or override of automatically generated suitability scores before hiring decisions. [medium] - Article 13(2)
  - Category: `human_oversight`
  - Action: Specify workflow allowing recruiters to review, adjust, or override scores with rationale logging.
- No accuracy or robustness criteria defined for the scoring algorithm against varying application formats or adversarial inputs. [low] - Article 10(4)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy/robustness testing plan for scoring model across diverse application contexts.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

**Recommendations:**

- Implement documented data governance and validation pipeline for scoring datasets.
- Add subgroup representativeness testing to detect bias in training data.
- Publish transparency documentation describing scoring criteria and logic.
- Introduce human review step before finalizing candidate suitability scores.
- Establish accuracy/robustness testing protocol for the scoring model.

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** The requirement ranks candidates for recruiter review using a suitability score in an employment context but specifies no data governance, transparency, or accuracy controls for the ranking function, creating high-risk gaps in a recruitment scenario.

**Risks:**

- No requirement for training/validation data used in scoring to be representative and checked for bias affecting ranking outcomes. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Document dataset representativeness and bias checks for the scoring model feeding the ranking function.
- Ranking output lacks specified accuracy metrics or robustness declarations, risking undetected performance degradation in candidate ordering. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and log accuracy/robustness metrics for the ranking output and include in system documentation.
- No transparency mechanism ensures recruiters can interpret how the suitability score translates into rank order. [medium] - Article 13(2)
  - Category: `transparency`
  - Action: Provide instructions/documentation explaining ranking logic and score-to-rank mapping for recruiter users.
- Recruiter review step is not defined as a substantive human oversight control (e.g., override, escalation, or non-reliance on rank alone). [medium] - Article 13(3)
  - Category: `human_oversight`
  - Action: Specify recruiter override capability and criteria to prevent automated rank from being treated as final decision.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 

**Recommendations:**

- Add dataset representativeness and bias validation checks for ranking-relevant data.
- Publish accuracy and robustness metrics for the ranking function in system documentation.
- Include clear instructions for recruiters on interpreting suitability scores and rank order.
- Define explicit recruiter override and escalation procedures for ranked candidate review.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 provides recruiter-facing explanations of scoring factors but lacks data governance basis for those factors and declared accuracy metrics, both required for a high-risk employment AI system.

**Risks:**

- No requirement that explanation factors are derived from representative, error-checked training data, risking misleading or biased explanations. [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Trace explanation factors to validated dataset attributes and document representativeness checks.
- Explanation content is not tied to declared accuracy/performance metrics of the scoring model. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Publish accuracy metrics for the suitability score alongside factor explanations in system documentation.
- No specification of how explanations support recruiter decision review or override of the score. [low] - Article 10(4)
  - Category: `human_oversight`
  - Action: Define recruiter workflow for reviewing/overriding scores using the provided explanations.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

**Recommendations:**

- Link explanation factors to governed, validated data attributes.
- Include declared accuracy metrics in explanation output or documentation.
- Add recruiter override/review workflow tied to explanations.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** The requirement notifies recruiters that a ranking was automated but lacks specification of the content needed for recruiters to interpret and appropriately use the output, as required for high-risk employment AI systems.

**Risks:**

- Notification lacks defined content on how recruiters should interpret and act on the automated ranking (e.g., scope, limitations, confidence level). [medium] - Article 13(2)
  - Category: `transparency`
  - Action: Extend notification/instructions to include ranking rationale, limitations, and intended use guidance for recruiters.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.

**Recommendations:**

- Define and implement instructions-for-use content accompanying the notification per Article 13(2).

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** The requirement establishes human override capability but lacks specificity on recruiter competence, understanding of system limitations, and transparency of ranking rationale needed for meaningful oversight.

**Risks:**

- No mention of ensuring recruiters understand the ranking system's capabilities/limitations before exercising override authority. [medium] - Article 14(4)
  - Category: `human_oversight`
  - Action: Define recruiter training/competency requirements and document system capability disclosures provided to reviewers.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Add recruiter training/documentation on system capabilities and limitations per Article 14(4).
- Provide ranking explanation/feature details in the override interface per Article 13(1).

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement does not specify log retention period or storage governance aligned with provider record-keeping duties. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define log retention duration and storage ownership consistent with provider obligations.
- Logging scope omits minimum traceability elements such as start/end time of each use and reference data checked, needed for Annex III high-risk systems. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Extend log schema to include usage timestamps and reference dataset identifiers.

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Specify log retention period and responsible party for storage.
- Add usage timestamp and reference dataset fields to the logging schema.

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement does not specify the minimum log content set (e.g., usage start/end, reference data checked, input data leading to decision) mandated for traceability. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Define and implement minimum logged fields per Article 12(3): session timestamps, reference dataset version, and input data checked.
- No defined retention period or storage governance for automatically generated logs as provider obligation. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Specify log retention duration and provider responsibility for log storage consistent with Article 19(1).

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Add explicit minimum log field list matching Article 12(3) requirements.
- Define log retention period and ownership per Article 19(1).

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** No requirement-level risk retained; the requirement prevents a sensitive or prohibited feature.

---

### NFR-1

**Risk level:** low

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Validation criteria omit checks for representativeness and statistical bias across relevant persons/groups as required for high-risk dataset governance. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Extend validation pipeline to include representativeness and subgroup statistical property checks.
- No mention of documenting design choices, data origin, or collection process as part of governance practices. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Add data provenance and design-choice documentation to the validation workflow.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Add representativeness and subgroup bias checks to dataset validation logic.
- Log data provenance and design rationale alongside validation results.
- Tie dataset validation completion to defined accuracy/robustness acceptance criteria.

---

### NFR-2

**Risk level:** low

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- No defined process for ensuring demographic evaluation datasets meet representativeness and quality criteria when available, or for mitigating bias assessment gaps when unavailable. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Define dataset quality/representativeness criteria for demographic evaluation data and a documented fallback method (e.g., proxy analysis) when lawful data is unavailable.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Establish documented data governance criteria for demographic evaluation datasets, including handling of unavailable lawful data.
- Specify performance metrics and thresholds for cross-group robustness comparisons.

---

### NFR-3

**Risk level:** low

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- No mechanism specified to detect proxy attributes (e.g., zip code, name) that could indirectly encode protected characteristics despite their explicit exclusion. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Implement proxy-variable correlation analysis and document data governance measures verifying no indirect encoding of protected attributes.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Add proxy-variable detection and correlation testing to data governance controls.
- Include ranking bias monitoring in the ongoing risk management process.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** Access control requirement lacks specificity on technical robustness measures (authentication strength, audit logging, resilience testing) needed to meet cybersecurity obligations for a high-risk recruitment system.

**Risks:**

- Requirement states access control intent but does not specify technical safeguards (authentication, audit logging, resilience against unauthorised alteration) required for high-risk system cybersecurity. [medium] - Article 15(5)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and document authentication mechanisms, access logging, and resilience testing against unauthorised access attempts.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Specify technical controls (multi-factor authentication, session logging, intrusion detection) and periodic security testing to demonstrate resilience per Article 15(5).

---

### NFR-5

**Risk level:** low

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- No documented post-market monitoring plan governing how alert thresholds, data collection, and analysis are structured over the system lifetime. [low] - Article 72(1)
  - Category: `post_market_monitoring`
  - Action: Document a post-market monitoring plan defining threshold sources, review cadence, and data collection scope.
- Unclear whether alert data is systematically analyzed and fed back to update risk assessments, as required for continuous evaluation of high-risk AI performance. [low] - Article 72(2)
  - Category: `post_market_monitoring`
  - Action: Define a process to log, analyze, and report monitoring data to compliance/risk owners on a scheduled basis.
- Threshold breaches are not explicitly linked to the risk management system, so triggered alerts may not feed into risk mitigation updates. [low] - Article 9(1)
  - Category: `risk_management`
  - Action: Integrate alert outputs into the risk management system to trigger reassessment when thresholds are breached.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Risk management system, Article 9(1)**
  > 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.

**Recommendations:**

- Establish and document a formal post-market monitoring plan per Article 72(1).
- Implement systematic logging/analysis pipeline for monitoring data per Article 72(2).
- Link alert triggers to risk management reassessment workflow per Article 9(1).

---

### NFR-6

**Risk level:** low

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- No specified thresholds or conditions defining what constitutes a safety/robustness/fairness failure triggering rollback. [low] - Article 15(1)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define measurable failure thresholds and validation checks that trigger rollback.
- No requirement for logging, investigating root causes, or notifying affected parties when rollback occurs. [low] - Article 20(2)
  - Category: `risk_management`
  - Action: Add procedure to investigate root cause and document corrective actions upon rollback event.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Corrective actions and duty of information, Article 20(2)**
  > 2. Where the high-risk AI system presents a risk within the meaning of Article 79(1) and the provider becomes aware of that risk, it shall immediately investigate the causes, in collaboration with the reporting deployer, where applicable, and inform the market surveillance authorities competent for the high-risk AI system concerned and, where applicable, the notified body that issued a certificate for that high-risk AI system in accordance with Article 44, in particular, of the nature of the non

**Recommendations:**

- Define explicit failure thresholds for safety, robustness, and fairness checks.
- Link rollback triggers to a formal post-market monitoring pipeline.
- Establish root-cause investigation and reporting workflow for each rollback event.

---
