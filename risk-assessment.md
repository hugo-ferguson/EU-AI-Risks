# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 5
- Medium: 3
- Low: 8

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** FR-1 ingests personal data (resumes, cover letters, application responses) for employment recruitment—a high-risk Annex III context—but lacks explicit data governance practices, quality standards, and documentation controls required by Art. 10(2). The requirement does not address data collection processes, origin validation, or management practices appropriate to the intended purpose.

**Risks:**

- Requirement does not specify data governance and management practices (collection processes, data origin validation, quality standards, retention) required for training, validation, and testing datasets used in the high-risk employment recruitment system. [high] - Article 10(2): Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system.
  - Category: `data_governance`
  - Action: Define and document data governance policy covering: data collection process, origin and provenance of resumes/cover letters, data quality checks, retention schedules, and lifecycle management. Link to intended purpose (suitability scoring per FR-2).
- Requirement does not specify how candidate personal data will be handled in compliance with data protection and security obligations inherent in employment recruitment ingestion. [medium] - Article 10(2): data governance and management practices appropriate for the intended purpose.
  - Category: `data_governance`
  - Action: Establish and document data protection measures: access controls, encryption, audit logging, and data minimization principles aligned with GDPR and employment law.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Develop a data governance specification for candidate data: document collection process, consent/legal basis, origin validation, quality standards, retention, and deletion rules.
- Create technical documentation detailing design choices for ingestion (field extraction, validation logic) and data provenance traceability for audit compliance.
- Implement data protection controls: access logging, encryption at rest and in transit, and role-based access aligned with employment law and GDPR.
- Confirm Annex III high-risk status and execute registration with the relevant authority before system deployment.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** Semantic profile indicates a remaining transparency gap. Conservative risk retained for manual review.

**Risks:**

- Transparency expectations not fully specified [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Define explanation detail, user information, and instructions for use.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Define explanation detail, user information, and instructions for use.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 specifies scoring logic but omits critical data governance practices and transparency mechanisms required for high-risk AI in employment. The requirement lacks documented data quality standards, bias representation controls, and explainability provisions—all binding under Art. 10(2–4) and Art. 13(1) for recruitment systems.

**Risks:**

- No documented data governance or management practices specified for training, validation, and testing datasets used to generate suitability scores. [high] - Article 10(2)
  - Category: `data_governance`
  - Action: Define and document data governance plan covering data collection origin, design choices, data cleaning, version control, and audit trails for all datasets used in model training.
- Requirement does not specify whether training data is representative of protected groups (e.g., gender, ethnicity, age) or free of biases that could discriminate in employment decisions. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Conduct demographic parity analysis on training data; document representation of protected groups; establish minimum representation thresholds and bias testing procedures.
- No transparency mechanism described to enable deployers (recruiters) to interpret how the suitability score is derived or what factors influence each candidate's score. [high] - Article 13(1)
  - Category: `transparency`
  - Action: Implement score explainability feature (e.g., feature importance, decision factors) and include interpretation guidance in system documentation.
- Requirement does not confirm whether the scoring model accounts for geographical, contextual, or behavioral settings relevant to the recruitment domain (e.g., role-specific competency variations). [medium] - Article 10(4)
  - Category: `data_governance`
  - Action: Document validation that training data reflects the specific job roles, organizational contexts, and labor markets where scores will be deployed; adjust data stratification if needed.
- Requirement does not specify accuracy, robustness, or cybersecurity testing for the scoring model prior to deployment. [medium] - Article 10(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Establish performance baselines (precision, recall, fairness metrics) and define model validation gates; document adversarial and edge-case testing.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

**Recommendations:**

- Draft a data governance charter specifying dataset provenance, curation standards, version control, and audit logging for all training and validation datasets.
- Perform demographic parity and intersectionality analysis on candidate pools; document representation gaps and mitigation strategies (e.g., synthetic data, rebalancing).
- Add score explanation output to the system (feature attribution, top decision factors) and include interpretation limits in user documentation.
- Validate model performance across job roles and geographic/organizational contexts; document any context-specific retraining or score adjustment mechanisms.
- Define and execute a model validation plan covering accuracy metrics, fairness thresholds, adversarial robustness, and rollback procedures before production deployment.

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 implements scoring and ranking for employment recruitment (Annex III high-risk), but lacks explicit data governance, accuracy metrics, and transparency controls. The requirement does not specify training data validation, performance measurement, or deployer instructions—all binding obligations under art:10, art:15, and art:13.

**Risks:**

- No data governance or validation practices defined for the suitability score training, validation, and testing datasets. [high] - Article 10(2)
  - Category: `data_governance`
  - Action: Document dataset lineage, representativeness checks, error/bias audits, and version control for training, validation, and test data.
- Accuracy, robustness, and performance metrics for the suitability score are not declared or measured. [high] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and measure accuracy metrics (e.g., precision, recall, fairness gaps); declare them in instructions for use.
- No instructions for use provided to deployers on suitability score characteristics, limitations, or interpretation. [high] - Article 13(2)
  - Category: `transparency`
  - Action: Create instructions for use specifying score methodology, intended purpose, performance characteristics, and known limitations for recruiters.
- Requirement does not specify how recruiters will interpret, validate, or override the ranking; no human oversight mechanism documented. [medium] - Article 13(1)
  - Category: `human_oversight`
  - Action: Define recruiter review workflow: require candidate review, comparison against score rationale, and documented override capability.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Establish and document data governance: representative datasets, error detection, bias testing, and statistical property validation for recruitment-specific demographics.
- Measure and declare accuracy metrics (false positive/negative rates, performance by protected attributes); include benchmarks in instructions for use.
- Author deployer instructions: explain score derivation, performance bounds, when scores may fail, and how to interpret ranking in context of recruiter judgment.
- Design recruiter review interface to show score rationale, comparative candidate profiles, and enable documented justification for overrides or tie-breaking.

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 requires explainability of candidate suitability scores but does not address data governance obligations (Art. 10) for the datasets underlying the scoring model, nor does it declare accuracy metrics as required by Art. 15(3). The requirement focuses on output explanation without ensuring the input data and model performance meet high-risk AI standards.

**Risks:**

- Requirement does not specify data governance and management practices for training, validation, and testing datasets used to develop the scoring model, leaving Art. 10(2) unmet. [high] - Article 10(2)
  - Category: `data_governance`
  - Action: Document dataset provenance, representativeness checks, error/completeness validation, and management practices specific to recruitment scoring; ensure datasets account for geographical, contextual, and behavioural variation in candidate populations.
- Requirement does not mandate declaration of accuracy metrics and performance levels for the suitability scoring model, violating Art. 15(3). [high] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and declare relevant accuracy metrics (e.g., precision, recall, fairness metrics across protected groups) in system instructions for recruiters; include baseline performance thresholds and known limitations.
- Requirement specifies explanations for recruiters but does not address whether the system's predictions are sufficiently accurate and robust under Art. 15(1), or how explanations enable meaningful human review. [medium] - Article 15(1)
  - Category: `human_oversight`
  - Action: Pair explanations with confidence intervals or uncertainty quantification; define escalation thresholds triggering mandatory human review of borderline or low-confidence scores.
- Requirement does not specify that training data is sufficiently representative and free of errors for the recruitment context, risking bias against underrepresented candidate groups under Art. 10(3). [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Conduct representativeness analysis across demographic groups and employment sectors; document data quality checks; perform bias audits before deployment.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Establish and document data governance practices including dataset audits, error detection, and representativeness validation for recruitment-specific populations.
- Publish accuracy metrics and performance benchmarks for the suitability scoring model in recruiter-facing instructions.
- Link explanations to confidence levels and define human review triggers for low-confidence or anomalous scores.
- Perform bias testing across protected groups and document data representativeness to ensure fairness in candidate evaluation.

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 requires notification of automated ranking generation but does not specify to whom, when, or with what depth of information. Article 13(1) mandates sufficient transparency for deployers to interpret system output and use it appropriately; Article 13(2) requires instructions for use with complete and clear information. The requirement lacks evidence of transparency mechanisms meeting these obligations.

**Risks:**

- Notification alone does not establish 'sufficiently transparent operation' as required by Art. 13(1); deployers (recruiters) need information to interpret the ranking output and understand its basis, but the requirement specifies only a notification trigger without information content. [high] - Article 13(1)
  - Category: `transparency`
  - Action: Extend notification to include mandatory disclosure: model type/version, input features used, confidence/uncertainty measures, and limitations. Document in instructions for use (Art. 13(2)).
- Article 13(2) requires high-risk AI systems to be accompanied by instructions for use with 'concise, complete, correct and clear information'; the requirement does not reference or commit to such instructions, leaving a gap in transparency obligations. [medium] - Article 13(2)
  - Category: `transparency`
  - Action: Create and maintain instructions for use document covering model logic, training data scope, performance metrics, known biases, and appropriate use of rankings in hiring decisions.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.

**Recommendations:**

- Expand notification payload to include model identifier, key input features, confidence level, and a link to full instructions for use.
- Draft Art. 13(2) instructions for use and integrate into recruiter onboarding and system help documentation.
- Formally document the high-risk classification decision (Art. 6(4)) and attach compliance evidence to deployment records.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 establishes human override capability but lacks explicit safeguards on override decision-making and deployer understanding of system limitations. Article 14(4) requires deployers to understand AI capacities and limitations; Article 14(5) mandates separate identification confirmation for Annex III point 1(a) systems (biometric/identification). Implementation gaps exist around oversight training, decision documentation, and system transparency.

**Risks:**

- Requirement does not specify that human reviewers must understand the system's capacities, limitations, and decision basis before exercising override authority. [medium] - Article 14(4)(a)
  - Category: `human_oversight`
  - Action: Document how deployer training, system capability statements, and confidence scores or explanations are provided to reviewers to enable informed override decisions.
- Requirement does not clarify whether the system qualifies as Annex III point 1(a) (biometric identification); if so, Article 14(5) requires separate identification confirmation, not yet addressed. [medium] - Article 14(5)
  - Category: `human_oversight`
  - Action: Confirm classification under Annex III and, if applicable to biometric/identification use, ensure separate confirmation step distinct from ranking override.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natur

**Recommendations:**

- Add deployer training curriculum and competency sign-off; include system capability documentation in deployment package.
- Integrate audit logging for all override actions with decision rationale capture and searchable records.
- Classify the system against Annex III point 1(a); if biometric, implement separate identification verification step before override acceptance.
- Integrate explainability layer into reviewer UI showing top decision factors, data sources, and confidence/uncertainty metrics.

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement does not confirm logs are automatically generated by the system; manual or semi-manual logging would violate Art. 12(1) mandatory automatic recording. [low] - Article 12(1)
  - Category: `record_keeping`
  - Action: Explicitly confirm system architecture enables automatic, real-time log capture without human intervention for all specified events (scores, rankings, explanations, overrides, decisions).
- Requirement does not specify log retention duration, storage location, or provider custody responsibility; Art. 19(1) requires providers to keep logs under their control. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Document log retention period, storage infrastructure, access control, and confirmation that provider maintains custody of all logs throughout system lifetime.
- Requirement lists logging content but does not confirm Art. 12(3)(a) minimum: recording start/end date-time of each use for employment AI systems. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Ensure logging explicitly captures use session start and end timestamps (date and time) for every system invocation in recruitment workflow.

**Cited provisions:**

- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Confirm technical design uses automatic event capture (e.g., event streaming, database triggers) for all logged entities; prohibit manual log entry.
- Define and document log retention policy (e.g., duration, deletion schedule, immutability controls) and designate provider as custodian.
- Add explicit requirement to log session timestamps (start/end date-time) for each recruitment decision cycle per Art. 12(3)(a).

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement does not mandate automatic recording of 'period of each use' (start/end timestamps) as required by Art. 12(3)(a) for employment-screening high-risk systems. [low] - Article 12(3)(a)
  - Category: `record_keeping`
  - Action: Extend audit schema to include use-session start and end timestamps; confirm automatic capture without manual trigger.
- Requirement does not explicitly require logging of 'reference database' against which input data was checked, as mandated by Art. 12(3)(b) for high-risk employment systems. [low] - Article 12(3)(b)
  - Category: `record_keeping`
  - Action: Add logging of database name, version, and query scope for each screening decision; link to audit record.
- Requirement omits confirmation that logging is automatic and continuous per Art. 12(1); manual or event-triggered logging does not satisfy the 'automatic recording' requirement. [low] - Article 12(1)
  - Category: `record_keeping`
  - Action: Document and test that audit logging is automatic (not user-initiated) and covers all screening decisions without gaps; verify log integrity (tamper-evidence, immutability).

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

**Recommendations:**

- Extend audit record schema to capture use-session timestamps (start and end) for each screening batch or individual decision.
- Document which reference database(s) and versions were queried for each candidate; log database selection rationale if multiple are available.
- Verify that logging is triggered automatically upon screening decision (not dependent on user action); add system-level tests to confirm no screening decisions bypass the audit trail.

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

- Requirement lacks documented data governance and management practices (design choices, collection processes, data origin) mandated by Article 10(2) for high-risk systems in education training context. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Add requirement to document data governance policies covering dataset origin, collection methodology, design rationale, and retention/lineage practices before model training begins.
- Requirement does not verify statistical representativeness or appropriate statistical properties of datasets as required by Article 10(3), focusing only on syntactic data quality. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Extend validation to include statistical profiling and representativeness checks (e.g., demographic balance for education training, class distribution, subgroup coverage) and document acceptance criteria.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Create a data governance policy document referencing dataset origin, collection processes, and design rationale; link it to model training approval workflows.
- Add statistical validation module to assess dataset representativeness for education cohorts; define and log pass/fail thresholds.
- Establish performance baseline requirements and validation metrics; require evidence of accuracy/robustness targets before training approval.

---

### NFR-2

**Risk level:** low

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement does not specify data governance and management practices for demographic data collection and storage, including design choices, data origin documentation, and collection process controls mandated by Article 10(2). [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Document data governance framework: specify lawful basis for demographic data collection, define retention/deletion policies, establish data lineage tracking, and implement access controls for demographic datasets.
- Requirement does not ensure demographic evaluation data is sufficiently representative, free of errors, and complete, or confirm appropriate statistical properties across demographic groups as required by Article 10(3). [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Add validation checks: confirm demographic dataset completeness, document statistical representativeness per group, establish error detection and remediation procedures before performance measurement.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Establish a data governance policy for demographic datasets covering collection basis, retention, access controls, and audit trails.
- Implement data quality validation pipeline confirming representativeness, completeness, and error rates before demographic performance analysis.
- Define performance acceptance criteria per demographic group and link measurement results to model robustness verification and risk mitigation decisions.

---

### NFR-3

**Risk level:** low

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- No documented data governance and management practices specified for how protected attributes are identified, excluded, and validated in the training, validation, and testing datasets. [low] - Article 10(2): Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose
  - Category: `data_governance`
  - Action: Define and document data governance procedures: attribute inventory (which attributes qualify as protected), exclusion rules (how they are removed or masked), and validation checkpoints (pre-training, pre-deployment audits).
- Requirement does not address how protected attributes will be detected if they appear indirectly (e.g., as proxies via other features like postal code or name-based inferences). [low] - Article 10(2): Data governance and management practices appropriate for the intended purpose
  - Category: `data_governance`
  - Action: Add proxy-attribute detection methodology: identify correlated features that may serve as protected-attribute proxies, document exclusion or decorrelation logic, and validate effectiveness before deployment.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Document the data governance procedures for protected-attribute management: list protected attributes in scope, specify exclusion/masking techniques, and define validation gates (pre-training and pre-deployment).
- Embed protected-attribute bias monitoring into the risk management system with defined review frequency and escalation thresholds for detected correlations.
- Conduct proxy-attribute analysis during data preparation and model development; document findings and mitigation (e.g., feature engineering or removal) in the data governance record.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 specifies access control implementation but does not address cybersecurity resilience against unauthorised alteration or exploitation of system vulnerabilities, which is a binding requirement under Art. 15(5) for high-risk AI systems in employment recruitment. The requirement also lacks explicit safeguards for candidate data protection and governance practices mandated under Art. 10.

**Risks:**

- Requirement does not specify technical or organisational measures to protect the system against unauthorised third-party exploitation of vulnerabilities, alteration of outputs, or manipulation of model explanations. [medium] - Article 15(5)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define threat model for candidate data and model outputs; implement vulnerability scanning, input validation, output integrity checks, and audit logging for access and modification attempts.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Conduct cybersecurity risk assessment and implement defences against unauthorised access and output manipulation (logging, checksums, rate limiting).
- Establish data governance policy covering candidate data lifecycle, quality standards, bias detection triggers, and compliance audit procedures.
- Define and enforce competence-based access roles with mandatory training sign-off before granting explanation-viewing permissions.

---

### NFR-5

**Risk level:** low

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Requirement specifies alert triggers but does not require documentation of the post-market monitoring system, its proportionality rationale, or lifecycle integration. [low] - Article 72(1)
  - Category: `post_market_monitoring`
  - Action: Document the post-market monitoring system design: define scope, proportionality justification (tied to healthcare safety risk level), data sources, alert thresholds, and roles/responsibilities.
- Monitoring alerts address detection but do not explicitly define response procedures, remediation triggers, or escalation paths required by continuous risk management. [low] - Article 9(2)
  - Category: `risk_management`
  - Action: Define alert handling workflow: specify conditions triggering model retraining, revalidation, deployment halt, or user notification; link to ongoing risk assessment cycles.
- Alert thresholds for bias and accuracy are configured but lack explicit criteria for what constitutes acceptable performance variance or failure in healthcare context. [low] - Article 72(2)
  - Category: `post_market_monitoring`
  - Action: Specify threshold-setting methodology: document how accuracy/bias bounds are derived from clinical safety requirements, validation data, or regulatory guidance.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other

**Recommendations:**

- Create a post-market monitoring plan document that maps NFR-5 alerts to the system lifecycle, healthcare context, and proportionality rationale.
- Add a requirement that alerts trigger formal incident review and risk mitigation decision (e.g., model rollback, retraining, notification) with documented ownership.
- Define threshold derivation: baseline performance metrics from pre-deployment validation and acceptable drift tolerances for healthcare use.

---

### NFR-6

**Risk level:** low

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Rollback procedure lacks documented trigger criteria (safety/robustness/fairness thresholds) and decision logic required to execute corrective actions immediately upon non-conformity detection. [low] - Article 20(1) – Corrective actions and duty of information
  - Category: `risk_management`
  - Action: Define and document quantified performance thresholds and automated escalation rules that trigger rollback; link to post-market monitoring metrics.
- Rollback operation does not explicitly include root-cause investigation, incident documentation, or deployer notification as mandated for non-conformity situations. [low] - Article 20(2) – Corrective actions and duty of information
  - Category: `risk_management`
  - Action: Add mandatory logging of rollback events with root-cause analysis workflow and automatic notification to deployers and competent authorities if serious incident criteria are met.
- Requirement does not specify technical resilience measures (error handling, consistency checks, environment adaptation) required to achieve robustness before rollback becomes necessary. [low] - Article 15(4) – Accuracy, robustness and cybersecurity
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Document preventive technical and organisational measures (input validation, drift detection, adversarial testing) designed to prevent degradation; clarify rollback as last-resort corrective action.

**Cited provisions:**

- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ
- **Corrective actions and duty of information, Article 20(2)**
  > 2. Where the high-risk AI system presents a risk within the meaning of Article 79(1) and the provider becomes aware of that risk, it shall immediately investigate the causes, in collaboration with the reporting deployer, where applicable, and inform the market surveillance authorities competent for the high-risk AI system concerned and, where applicable, the notified body that issued a certificate for that high-risk AI system in accordance with Article 44, in particular, of the nature of the non
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con

**Recommendations:**

- Define quantified performance thresholds (e.g., accuracy drop >X%, fairness metric deviation >Y%) and automated escalation rules that trigger rollback without manual delay.
- Implement structured logging and root-cause analysis for every rollback event; integrate with incident reporting pipeline to competent authorities (art:73).
- Connect rollback capability to active post-market monitoring system that tracks model performance continuously and surfaces degradation signals before critical failures.
- Document preventive robustness controls (drift detection, input sanitization, edge-case testing) that reduce reliance on rollback; position rollback as remedial, not primary safeguard.

---
