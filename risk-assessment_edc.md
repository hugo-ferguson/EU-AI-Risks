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

**Analysis:** FR-1 ingests candidate resumes, cover letters, and form responses for an Annex III employment recruitment system, but it does not define data governance for these inputs: provenance, collection purpose, quality checks, or bias examination. Without this, ingested data may feed downstream processing or training without the traceability and suitability controls expected for high-risk employment AI.

**Risks:**

- The requirement does not specify how ingested candidate data is governed: provenance, original collection purpose, preparation steps, or whether it is used for training, validation, or testing. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Define a data governance spec for portal-ingested documents covering source and provenance tagging, collection purpose, preprocessing (parsing, cleaning, labelling), quality checks, and a bias examination of free-text content that may proxy protected attributes. State whether ingested data may enter training, validation, or testing sets.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Document data provenance, collection purpose, preprocessing, and quality and bias examination procedures for all ingested candidate documents, and specify whether they may be used for model training, validation, or testing.
- Implement a deployer-configurable AI-use notice in the recruitment portal at the point of submission.

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

**Analysis:** FR-2 defines candidate suitability scoring for recruitment (Annex III employment, likely high-risk under Art. 6(2)) but specifies no data governance for the training and scoring data and no interpretability of scores for deployers. Without these, scores may be biased or unrepresentative and cannot be meaningfully interpreted or contested.

**Risks:**

- The requirement does not specify governance for the data used to train and validate the scoring model, including data origin, design choices, and examination for bias across candidate groups. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Define data governance practices for scoring datasets, covering provenance, representativeness criteria across candidate populations, error and completeness checks, and bias examination. Link these to NFR-2 demographic performance evaluation.
- Suitability scores are generated without any requirement that deployers can interpret how job requirements, experience, education, and skills contribute to each score. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Add a requirement for per-candidate score explanations showing factor contributions. Document the score's meaning, limitations, and intended use in the instructions for use.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Specify Art. 10-aligned dataset documentation, representativeness targets, and bias examination procedures for the scoring model before training.
- Require interpretable score outputs with factor-level breakdowns, and document scoring logic and limitations in the deployer instructions.

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 ranks candidates in a high-risk employment context. It specifies no data representativeness or bias controls, no interpretability of rankings for recruiters, and no declared accuracy metrics. Without these, rankings may systematically disadvantage groups and recruiters cannot judge when to rely on or override them.

**Risks:**

- The ranking relies on suitability scores whose underlying training, validation and test data have no stated requirements for representativeness, error-freeness or appropriate statistical properties across candidate groups. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Define dataset representativeness and bias-examination criteria across relevant candidate groups for the scoring and ranking model, and validate them before release.
- No requirement makes the ranking interpretable to recruiters, such as score drivers, rank rationale, or known limitations, so deployers cannot appropriately interpret the output. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Display per-candidate score factors and ranking rationale in the recruiter view, and document ranking limitations in the instructions for use.
- No accuracy level or ranking-quality metric is specified or declared, for example precision at top-k or rank correlation with validated outcomes. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify ranking accuracy metrics and acceptance thresholds, test against them, and declare the results in the instructions for use.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Add a data governance requirement covering representativeness and bias analysis for the datasets behind the suitability score and ranking.
- Add a requirement for recruiter-facing explanations of ranking position and score contributors, plus documented limitations.
- Add measurable ranking accuracy and robustness criteria, and include them in the instructions for use.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 is an explainability control that supports recruiter understanding, but it does not say whether the explained factors have been checked for bias, or whether explanations faithfully match the FR-2 scoring model. Without this, explanations could legitimise proxy discrimination or mislead recruiters in a high-risk Annex III employment context.

**Risks:**

- The requirement does not ensure that the factors surfaced in explanations come from data examined for representativeness and bias, so the system could explain scores driven by factors that act as proxies for protected groups. [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Link explanation factors to the validated FR-2 feature set, and add a check that flags explanation factors correlated with protected attributes across candidate groups.
- No fidelity, consistency or accuracy criteria are defined for the explanations, so the stated factors may not reflect the model's actual scoring behaviour. [low] - Article 15(1)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test explanation fidelity metrics, such as agreement with feature attribution and stability across similar candidates, and show score accuracy context alongside explanations.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Require bias and proxy screening of all factors eligible to appear in recruiter-facing explanations, and document the results under data governance practices.
- Add acceptance criteria for explanation fidelity and consistency, and include declared score accuracy levels in the recruiter view.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 is a partial transparency control: it tells recruiters that a ranking is AI-generated, but it does not give them the information they need to interpret the ranking and use it appropriately. In a high-risk recruitment context, recruiters may over-rely on rankings they cannot understand.

**Risks:**

- The notification flags that a ranking came from an automated model but gives no interpretive information, such as key ranking factors, confidence, or limitations. Recruiters therefore cannot interpret the output as Article 13(1) requires. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Extend the notification to include the main ranking factors, a confidence or score context, and known limitations, plus a link to guidance on appropriate use.
- The requirement does not specify how the notification is delivered: when it appears, where in the UI, and whether it persists on exported or shared rankings. This creates a risk of inconsistent or missed disclosure. [low] - Article 50(1)
  - Category: `transparency`
  - Action: Define acceptance criteria requiring the notice to be displayed on every ranking view and every export, before the recruiter acts on the ranking.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, i

**Recommendations:**

- Add interpretability content (key factors, confidence, limitations) to the ranking notification, and link it to the instructions for use.
- Specify the trigger, placement, and persistence of the notification across views and exports, and verify these through UI tests.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 already provides a human review/override control before a candidate is removed. The remaining gaps are narrower: the requirement does not say how recruiters will understand ranking limitations and avoid automation bias, and it does not specify what explanatory output supports the override decision. Without these, oversight may be nominal rather than effective in a high-risk recruitment context.

**Risks:**

- The override capability exists, but the requirement does not ensure recruiters can understand ranking capacities and limitations or recognise automation bias, which risks rubber-stamp approvals. [medium] - Article 14(4)
  - Category: `human_oversight`
  - Action: Add oversight UI elements showing ranking limitations and confidence, add automation-bias prompts, and define recruiter training and competence criteria.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Extend FR-6 with acceptance criteria for recruiter-facing limitation and confidence displays, automation-bias safeguards, and documented recruiter training.
- Define the minimum interpretable ranking information shown at review time and document it in the instructions for use.

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Log retention duration, storage controls and access governance are not specified, so logs may not be kept for the required minimum period. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define a log retention policy of at least six months or longer where applicable, with secure storage, access control and deletion rules aligned with data protection requirements.
- The requirement does not state that logging is automatic, tamper-evident, and kept across the system lifetime, or that it captures context for traceability, such as model version, timestamps, input data references and risk-relevant events. [low] - Article 12(2)
  - Category: `record_keeping`
  - Action: Specify a log schema with timestamp, model/version ID, input reference, candidate/session ID, actor ID for overrides, and anomaly flags. Make the logs append-only or integrity-protected so they support post-market monitoring.

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s

**Recommendations:**

- Add a retention and access-control requirement for screening logs, with a minimum period, storage location and authorised roles.
- Extend FR-7 with a mandatory log schema and integrity protection so each decision can be traced to the model version and inputs and fed into post-market monitoring.

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement does not state that audit records are generated automatically over the system's lifetime, so logging could rely on manual capture and leave traceability gaps. [low] - Article 12(1)
  - Category: `record_keeping`
  - Action: Specify automatic, tamper-evident event logging that is enabled by default for every screening decision across all deployed model versions.
- The requirement does not define a retention duration or retention controls, so records could be deleted before the minimum period required for provider-kept logs. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define a retention period of at least six months (or longer where applicable law requires), with access controls and deletion governance aligned to data protection rules.

**Cited provisions:**

- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Amend FR-8 to require automatic, tamper-evident logging of each screening event throughout the system lifecycle.
- Add a retention clause setting a minimum six-month log retention, with documented access controls and a deletion policy.

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

- Validation covers technical errors only and omits checks that training and evaluation datasets are relevant and sufficiently representative, with appropriate statistical properties for the persons or groups affected (e.g., learners or candidates). [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Extend the validation pipeline with representativeness and subgroup distribution checks against the intended population, using defined acceptance thresholds.
- The requirement does not specify recording or documenting data governance practices, such as data origin, validation results, identified gaps and remediation, so its compliance cannot be evidenced. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Persist validation reports per dataset version, including data provenance, detected issues and the remediation taken, and link each report to the model training run.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Add representativeness and bias examination of training and evaluation datasets, with acceptance thresholds tied to the education use context.
- Generate versioned, auditable data validation reports covering data provenance, detected issues and remediation.
- Specify measurable failure thresholds and a training-gate behaviour that stops model training when validation fails.

---

### NFR-2

**Risk level:** low

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Per-group performance is measured, but there are no disparity thresholds and no required mitigation when a gap is found, so the requirement does not ensure biases are detected, prevented and mitigated. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Define fairness metrics and maximum allowable inter-group performance gaps, and require documented mitigation and re-evaluation before release when gaps exceed them.
- The condition 'where lawful demographic evaluation data is available' leaves no fallback when such data is missing, so representativeness for affected groups may go unverified. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Document which demographic groups are covered, record data gaps, and specify alternative assessment methods or a risk acceptance process for groups without data.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Set quantitative inter-group disparity thresholds with mandatory remediation and sign-off before deployment.
- Maintain a demographic coverage register, and define alternative assessment methods for groups that lack lawful evaluation data.
- Report subgroup accuracy alongside the declared overall accuracy, and repeat the evaluation at every retraining cycle.

---

### NFR-3

**Risk level:** low

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The exclusion covers only direct protected attributes, with no requirement to examine the data for proxy features or for biases that could still produce discriminatory rankings. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Add a data governance step that analyses training and ranking inputs for proxy correlations with protected attributes, and document mitigation measures.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Specify proxy-variable detection and bias examination of ranking input data. If special-category data must be processed for bias testing, apply the Article 10(5) safeguards.
- Add bias risk to the risk management file, with defined fairness metrics, test frequency and remediation triggers.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 provides a confidentiality control (role-based read access) but does not address the Art. 15(5) obligation to make the system resilient against unauthorised attempts to alter its use, outputs or performance, such as tampering with models, rankings or candidate data. Without integrity protections, manipulated outputs could silently affect high-risk recruitment decisions.

**Risks:**

- The access control covers only viewing of candidate data and explanations; it does not cover protection against unauthorised modification of model artefacts, ranking outputs, configuration or input data, so integrity is left unaddressed. [medium] - Article 15(5)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend NFR-4 to cover write/modify permissions for models, configs and candidate records, and add integrity checks such as signed model artefacts and tamper-evident audit logs of changes.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Broaden NFR-4 from read access to full integrity protection: role-based write controls, signed model and config artefacts, and tamper-evident change logging.
- Document the authorisation lifecycle (role definitions, approval, periodic review, revocation) and a threat model, and apply stricter, logged access to any special-category data used for bias detection.

---

### NFR-5

**Risk level:** low

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Alerts fire on threshold breaches, but the requirement does not specify that alert events and underlying metrics are recorded, analysed and retained across the system lifetime, including data from deployers. [low] - Article 72(2)
  - Category: `post_market_monitoring`
  - Action: Persist alert events, metric time series and deployer-reported performance data. Add periodic trend analysis linked to the documented post-market monitoring plan.
- There is no defined path from a triggered alert, such as a breach in accuracy, bias or data quality, to risk re-assessment or corrective risk measures. Threshold values are also not justified against identified risks. [low] - Article 9(1)
  - Category: `risk_management`
  - Action: Derive alert thresholds from the risk register. Define an alert-to-risk-review workflow with owners, response times and documented corrective actions.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Risk management system, Article 9(1)**
  > 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.

**Recommendations:**

- Extend NFR-5 so that alert logs and metrics are stored and analysed under a documented post-market monitoring plan covering the full lifecycle.
- Link threshold configuration and alert handling to the risk management system, with traceable rationale and an escalation and corrective-action process.

---

### NFR-6

**Risk level:** low

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The rollback is optional ('should'), and the requirement defines no measurable failure criteria for safety, robustness, or fairness checks and no target time to restore the approved version, so the resilience fallback cannot be verified. [low] - Article 15(4)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Change 'should' to 'shall', define pass/fail thresholds for each check, and set a maximum rollback time with automated tests that verify the fallback works.
- Rollback is described only as a technical revert, with no link to corrective-action duties such as investigating the cause, informing distributors and deployers, or deciding to withdraw or disable the system when non-conformity is found. [low] - Article 20(1)
  - Category: `risk_management`
  - Action: Link each rollback event to a corrective-action workflow covering root-cause investigation, a non-conformity decision, notification of affected parties, and a withdraw/disable option.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ

**Recommendations:**

- Make rollback mandatory, with quantified trigger thresholds and a tested recovery time objective.
- Connect rollback to a documented corrective-action procedure that includes investigation and stakeholder notification.
- Feed rollback triggers and events into the post-market monitoring data collection and analysis.

---
