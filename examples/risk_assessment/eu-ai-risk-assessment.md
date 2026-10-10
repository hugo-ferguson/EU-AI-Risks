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

**Analysis:** FR-1 ingests candidate resumes, cover letters and form responses in a recruitment context (Annex III employment) but states no data governance practices for data collection, origin, or quality. Without these, the ingested data could introduce bias or poor-quality inputs into downstream scoring (FR-2).

**Risks:**

- No data governance practices are specified for ingested candidate data (collection process, origin, purpose of collection, preparation such as cleaning/annotation, and quality/suitability checks). [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Define and document data collection and origin, preprocessing steps (parsing, normalisation, cleaning), and data quality checks for ingested resumes, cover letters and form responses, and record them in a data governance specification.
- Requirement does not address examination of ingested data for possible biases (e.g., proxies for protected attributes in free-text resumes, cover letters, or form fields) that could lead to discrimination in recruitment. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Add ingestion-stage requirements to identify and flag or exclude sensitive or proxy attributes, and run bias examination on the ingested data before it is used for scoring or model training/validation.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Create a data governance specification covering collection process, origin, preprocessing, and quality checks for candidate data ingested via the portal.
- Add ingestion-stage bias and protected-attribute proxy checks, and document their results as input to technical documentation.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 generates candidate suitability scores in an Annex III employment recruitment context but specifies no data governance, representativeness/bias examination, or transparency of score logic. Without these, scores may encode biased or unrepresentative patterns and deployers cannot interpret them.

**Risks:**

- No requirement for training/validation/testing data to be relevant, representative, error-free and statistically appropriate for the candidate groups being scored. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Define dataset quality criteria (representativeness across candidate groups, completeness, error rates) and document validation and testing of the scoring model's data.
- Scoring from extracted resume features (experience, education, skills) lacks stated data governance practices covering data origin, preparation, and bias examination. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Add a data governance procedure covering data collection/origin, feature extraction design choices, and bias detection and mitigation for the scoring pipeline.
- No requirement that score outputs be interpretable by recruiters, or that instructions for use describe score meaning, factors, and limitations. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Output per-candidate factor contributions with each score and provide deployer documentation on score interpretation, accuracy and known limitations.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Define and document data quality and representativeness criteria for training, validation and testing data, with results reviewed before release.
- Establish data governance and bias examination practices for the feature extraction and scoring pipeline.
- Expose score explanations and ship instructions for use describing the score's meaning, limits and performance.

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 ranks candidates in an Annex III employment context using a suitability score, but it specifies no data quality or bias controls, no accuracy declaration, no explanation of the ranking, and no recruiter oversight. Without these, ranking could be unrepresentative, biased or opaque, and recruiters could over-rely on it.

**Risks:**

- The ranking depends on a suitability score, but the requirement does not specify that the training, validation and testing data are relevant, representative, error-free or examined for bias against candidate groups. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Add data governance criteria for the scoring model: representativeness checks across candidate groups, bias examination, data quality validation and documented dataset provenance.
- The requirement does not state that accuracy levels and metrics for the score and ranking will be measured and declared in the instructions for use, so recruiters cannot judge how reliable the ranking is. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy and robustness metrics for the ranking, test them (including per-group performance), and declare them in the instructions for use.
- The requirement does not say the ranking output will be interpretable by recruiters or accompanied by documentation of the system's capabilities, limitations and intended purpose. [medium] - Article 13(3)
  - Category: `transparency`
  - Action: Show the main factors behind each score and ranking, and write instructions for use covering intended purpose, performance limitations and known failure modes.
- Recruiters review the ranked list, but the requirement defines no oversight measures such as the ability to override or disregard the ranking, or guidance on automation bias. The ranking could therefore become the de facto decision. [medium] - Article 14(4)
  - Category: `human_oversight`
  - Action: Let recruiters override or re-order rankings and see the basis for each rank. Add automation-bias guidance and log overrides.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Specify data governance and bias examination for the scoring model's datasets (representativeness, quality, group-level checks).
- Define and declare accuracy and robustness metrics for the ranking, including per-group performance.
- Provide per-candidate score explanations and instructions for use covering limitations.
- Add recruiter override capability, automation-bias safeguards and override logging.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 provides explanations for candidate scores in an Annex III recruitment context but does not specify that explanations are faithful to the model, nor does it address the quality of the data driving them or declared accuracy. Unfaithful or unrepresentative-data-driven explanations could mislead recruiters and obscure bias.

**Risks:**

- No requirement that the data sets behind the scores (and thus the explained factors) are relevant, representative and error-free, so explanations may surface factors reflecting biased or unrepresentative data. [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Define data quality and representativeness checks for training/validation data and verify that explained factors are not proxies for protected attributes.
- Requirement does not account for the specific contextual or functional setting (recruitment roles, regions, job types) in which factor explanations must be valid. [low] - Article 10(4)
  - Category: `data_governance`
  - Action: Specify the deployment context (roles, geographies, languages) and validate that explanations are meaningful within it.
- No accuracy or fidelity metric is defined for the explanations or scores, and nothing indicates that accuracy levels will be declared in the instructions for use, so recruiters cannot gauge reliability. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define explanation fidelity and score accuracy metrics, test them, and document the declared levels in the instructions for use.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Add data quality, representativeness and proxy-bias checks for the data behind the explained factors.
- Specify the deployment context for which explanations must be valid and test within it.
- Define and declare accuracy and explanation-fidelity metrics in the instructions for use.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 discloses to recruiters that a ranking is AI-generated, but it does not say what information accompanies the notice. Recruiters may not be able to interpret the ranking or use it appropriately in an Annex III employment context.

**Risks:**

- The notification only flags that a ranking is model-generated. It does not require accompanying information on the ranking's purpose, accuracy, limitations, or how to interpret the output, so recruiters may over-rely on it. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Extend the notification to link to or show interpretability information (key ranking factors, confidence or score meaning, known limitations). Align it with the instructions for use required by Art. 13(2).

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Specify the notification content and add interpretive context and a link to the instructions for use, so recruiters can interpret and appropriately use the ranking output.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 provides a human review/override control for rankings, but it does not specify how recruiters are enabled to understand, interpret, and avoid over-relying on the ranking. Without these supports, the oversight may be nominal rather than effective for a high-risk recruitment system.

**Risks:**

- The requirement does not ensure the reviewing recruiter can understand the system's capacities and limitations or guard against automation bias when reviewing rankings. [medium] - Article 14(4)
  - Category: `human_oversight`
  - Action: Add UI and training requirements covering ranking limitations, a warning on automation bias, and a requirement for recruiters to confirm they have reviewed the ranking rationale before it is finalised.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Define recruiter-facing oversight measures (limitations notice, automation-bias safeguards, training, escalation criteria) and record override/reject actions for auditability.
- Require interpretable ranking explanations in the review interface and cover them in the deployer instructions for use.

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Logged items cover outputs and overrides only, and omit events that identify risk situations, substantial modifications, and post-market monitoring inputs required for traceability. [low] - Article 12(2)
  - Category: `record_keeping`
  - Action: Extend the log schema to capture risk-relevant events (e.g., low-confidence outputs, drift alerts, model version changes) and make them available for post-market monitoring.
- Minimum logging for Annex III point 1(a) systems is not addressed: period of each use, reference database checked, input data leading to a match, and identity of persons verifying results. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Add fields for session start/end timestamps, reference data version, input data reference, and reviewer identity, and confirm which of these apply to the screening use case.
- No log retention period, integrity protection or access control is specified, so logs may not be retained or kept reliably for the period appropriate to the intended purpose. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define a retention period (minimum six months unless other law requires longer), tamper-evident storage, and role-based access to logs under the provider's control.

**Cited provisions:**

- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Extend the log schema to cover risk-relevant, modification and monitoring events per Article 12(2).
- Add the Article 12(3) minimum fields (use period, reference database, input data, verifier identity) where applicable.
- Specify log retention, integrity and access-control requirements aligned with Article 19.

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement does not state a log retention period, so audit records may be deleted before the minimum period for automatically generated logs. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define a retention period for audit logs, with a minimum of six months or longer where other law requires. Enforce it through retention policy and deletion controls.
- The log content is limited to input data, model version, and human actions. It does not mention events that identify risk situations or substantial modifications, or events needed for post-market monitoring. [low] - Article 12(2)
  - Category: `record_keeping`
  - Action: Extend the log schema to capture risk-relevant events, such as anomalies, low-confidence outputs, overrides, and model changes. Link these events to post-market monitoring inputs.
- The requirement does not say that logs are recorded automatically over the system lifetime or that they include usage period timestamps and the reference database used for input checks, as expected for Annex III systems. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Specify automatic, tamper-evident logging that records start and end time of each use, the reference data or database checked, matches that led to the decision, and the identity of the human verifier.

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Set and enforce an explicit audit log retention period.
- Expand the log schema to cover risk-relevant events and model changes.
- Specify automatic, tamper-evident logging with usage timestamps, reference data, and verifier identity.

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** No requirement-level risk retained; the requirement prevents a sensitive or prohibited feature.

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

### NFR-1

**Risk level:** low

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Validation checks are limited to missing values, duplicates, and label inconsistency, so they do not cover representativeness or statistical properties across relevant persons or groups. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Add dataset checks for representativeness and subgroup statistical properties, and define pass/fail thresholds that block training when they are not met.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Extend NFR-1 beyond basic data-quality checks to cover representativeness and subgroup statistics, define acceptance thresholds, and record validation results and data provenance as part of the data governance documentation.

---

### NFR-2

**Risk level:** low

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement does not define how test datasets are checked for representativeness and statistical properties across the relevant groups, nor what happens where demographic data is unavailable, so coverage gaps may go undetected. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Define the demographic groups and minimum sample sizes, and document dataset representativeness checks and coverage gaps. State a fallback when lawful demographic data is unavailable, such as proxy-free alternatives or documented limitations.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Add dataset representativeness checks, group definitions and a documented fallback for when demographic evaluation data is unavailable.
- Define per-group metrics, disparity thresholds and a release gate, and document the results alongside declared accuracy levels.

---

### NFR-3

**Risk level:** low

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement bans direct use of protected attributes but does not require examination of datasets for biases or proxy features (e.g., postcode, name, language) that could reproduce discrimination in rankings. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Add a requirement for bias examination of training, validation and testing data, including proxy-feature analysis and documented mitigation measures.
- No mechanism is specified to verify that protected attributes are actually absent from ranking inputs, or to handle their exceptional processing for bias detection and correction, which Article 10(5) allows only under strict conditions. [low] - Article 10(5)
  - Category: `data_governance`
  - Action: Clarify whether protected attributes may be held in a segregated store for bias testing only, with access controls, and add automated checks that they are excluded from the ranking feature set.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Add bias examination and proxy-feature analysis requirements for datasets used in ranking.
- Define controlled handling of protected attributes for bias testing and add automated exclusion checks on ranking inputs.
- Link NFR-3 to the risk management system and add periodic disparate-impact testing of ranking outputs.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 states an access-control safeguard for a likely high-risk recruitment system but leaves the cybersecurity implementation unspecified: no authentication strength, role definitions, or threat coverage beyond viewing. Without these, resilience against unauthorised third parties cannot be verified.

**Risks:**

- The requirement restricts viewing to authorised staff but does not address resilience against unauthorised third parties altering system use, outputs or performance (e.g., tampering with candidate data, model outputs or explanations), so protection is limited to read access. [medium] - Article 15(5)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend the requirement to cover write/modify access and integrity protection, and define the threat model (role-based access, strong authentication, audit logging of access, integrity checks on candidate data, models and explanations), with security testing against it.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Define the role model, authentication strength and integrity controls, and add penetration/security tests tied to a threat model covering tampering as well as viewing.

---

### NFR-5

**Risk level:** low

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system or plan covering what data is collected, how it is analysed, and how performance is evaluated across the system lifetime, including deployer-provided data. [low] - Article 72(2)
  - Category: `post_market_monitoring`
  - Action: Link alerting to a documented monitoring plan that defines metrics, data sources (including deployer feedback), review cadence, and retention of alert records.
- No defined response to threshold breaches (triage, risk re-assessment, mitigation, or corrective action), so alerts are not integrated into the continuous iterative risk management process. [low] - Article 9(2)
  - Category: `risk_management`
  - Action: Define alert severity levels, owners, escalation paths, and a workflow that feeds breaches into risk register updates and corrective actions.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Document a post-market monitoring plan that specifies metrics, thresholds rationale, data sources, and review cadence, and trace NFR-5 alerts to it.
- Add an alert-response procedure with owners, escalation, and risk-register updates for every threshold breach.

---

### NFR-6

**Risk level:** low

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Rollback is triggered by 'safety, robustness, or fairness checks', but no thresholds, metrics, or detection mechanism are defined, so degraded accuracy or robustness may go undetected or be inconsistently handled. [low] - Article 15(4)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define measurable pass/fail thresholds for accuracy, robustness and fairness checks, and automate rollback triggers. Ensure the rollback target version is verified and integrity-protected.
- The requirement does not link rollback to a risk management process, so failed checks may not trigger root-cause analysis, risk re-evaluation, or confirmation that the prior version still meets risk controls. [low] - Article 20(1)
  - Category: `risk_management`
  - Action: Add a workflow in which each rollback creates an incident record, triggers root-cause investigation, re-validates the restored version against current risk controls, and escalates to the provider's compliance function when non-conformity is suspected.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ

**Recommendations:**

- Specify quantitative rollback trigger thresholds and verify the integrity of approved fallback versions.
- Tie rollback to an incident and risk-management workflow with root-cause analysis and re-validation of the restored version.
- Feed rollback and failed-check data into the post-market monitoring plan.

---
