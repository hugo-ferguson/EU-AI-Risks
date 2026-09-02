# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Medium: 11
- Low: 5

## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** Requirement FR-1 does not specify data processing and storage practices, leaving a gap in data_governance with Article 10(2).

**Risks:**

- Does not specify data processing and storage practices [medium] — Article 10(2)
  - Category: `data_governance`
  - Suggested engineering action: Define data processing and storage practices for resume, cover letter, and application form responses.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Define data processing and storage practices

---

### FR-2

**Risk level:** medium

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** The requirement FR-2 may not meet data quality criteria, creating a data governance compliance gap with art:10(3) and (4).

**Risks:**

- Does not specify data quality properties for training, validation and testing datasets [medium] — Article 10(3)
  - Category: `data_governance`
  - Suggested engineering action: Define and document data quality properties for training, validation and testing datasets.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Define and document data quality properties for training, validation and testing datasets

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** The requirement lacks clarity on data governance and transparency for human oversight, and does not specify the statistical properties of the suitability score data, creating a missing compliance gap with Article 10 and 13.

**Risks:**

- Does not specify data governance practices for suitability score data [medium] — Article 10(3)
  - Category: `data_governance`
  - Suggested engineering action: Implement data quality checks and validation procedures for suitability score data.
- Lacks transparency in human oversight for recruiter review, creating a gap with Article 13(1) [medium] — Article 13(1)
  - Category: `transparency`
  - Suggested engineering action: Provide clear instructions for use and transparency requirements for human oversight in recruiter review.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Implement data quality checks and validation procedures for suitability score data.
- Provide clear instructions for use and transparency requirements for human oversight in recruiter review.

---

### FR-4

**Risk level:** low

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** The requirement FR-4 is partially addressed by provisions in art:13 and art:50, but the main factor explanation is not specified, creating a missing compliance gap with art:13(1).

**Risks:**

- Does not specify main factor explanation for scores [low] — art:13(1)
  - Category: `transparency`
  - Suggested engineering action: Clarify the explanation for scores in the requirement or technical documentation.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Clarify the explanation for scores in the requirement or technical documentation

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** The requirement does not specify how the transparency of the automated decision-support model used in candidate ranking is ensured, creating a missing gap in transparency, and does not explicitly address the data quality of the candidate data used for ranking, which could lead to biased outcomes.

**Risks:**

- The requirement does not specify how the transparency of the automated decision-support model used in candidate ranking is ensured [medium] — Article 13(1)
  - Category: `transparency`
  - Suggested engineering action: Specify the methodology for model interpretability and explainability.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Specify the methodology for model interpretability and explainability, and ensure data quality of candidate data.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** Requirement FR-6 does not specify competency requirements for human reviewers, and monitoring expectations, creating a remaining gap with Article 14(4).

**Risks:**

- Does not specify competency requirements for human reviewers [medium] — Article 14(4)
  - Category: `human_oversight`
  - Suggested engineering action: Add reviewer competency, escalation, and monitoring requirements

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Define reviewer competency, escalation, and monitoring requirements

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement already describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Does not specify information on recruiter override, final screening decision, and model-generated scores in logging capabilities [low] — Article 12(3)
  - Category: `record_keeping`
  - Suggested engineering action: Add information on recruiter override, final screening decision, and model-generated scores to the logging capabilities.

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Add information on recruiter override, final screening decision, and model-generated scores to the logging capabilities.

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement already describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Does not specify the storage duration for the audit records [low] — art:19(2)
  - Category: `record_keeping`
  - Suggested engineering action: Define the storage duration for the audit records

**Cited provisions:**

- **Automatically generated logs, Article 19(2)**
  > 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.

**Recommendations:**

- Define the storage duration for the audit records

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** No requirement-level risk was retained because the requirement is framed as an existing safeguard/control that prevents a sensitive or prohibited feature. Manual review may still confirm how the control is implemented.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** The requirement FR-10 lacks clarity on the review process criteria and does not ensure competency requirements for human reviewers, creating a missing gap with Article 14(4).

**Risks:**

- Does not specify criteria for review of automated decision-making by human reviewers [medium] — Article 14(4)
  - Category: `human_oversight`
  - Suggested engineering action: Define clear review criteria and competency requirements for human reviewers.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Define clear review criteria, competency requirements and monitoring expectations for human reviewers

---

### NFR-1

**Risk level:** low

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** Requirement NFR-1 does not explicitly require validation of dataset quality for missing values, duplicate records, or inconsistent labels, which is covered by art:10(3) and art:10(4).

**Risks:**

- Does not specify requirements for dataset quality validation [low] — Article 10(3)
  - Category: `data_governance`
  - Suggested engineering action: Implement data quality validation for missing values, duplicate records, and inconsistent labels.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Implement data quality validation for missing values, duplicate records, and inconsistent labels.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** Requirement NFR-2 lacks demographic data validation, missing a critical safeguard to ensure fairness and unbiased model performance across demographic groups.

**Risks:**

- Does not specify demographic data validation [medium] — Article 10(4)
  - Category: `data_governance`
  - Suggested engineering action: Include data validation to account for characteristics or elements that are particular to specific geographical, contextual, behavioural or functional settings within which the high-risk AI system is intended to be used.

**Cited provisions:**

- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

**Recommendations:**

- Include demographic data validation to address potential bias in model performance across demographic groups

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** Requirement does not specify how protected attributes will be handled, raising concerns under art:10(2) about data governance and management practices.

**Risks:**

- Does not specify handling of protected attributes [medium] — Article 10(2)
  - Category: `data_governance`
  - Suggested engineering action: Specify data handling and protection mechanisms in the requirement.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Specify data handling and protection mechanisms for protected attributes

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** Requirement NFR-4 does not explicitly address cybersecurity measures for the recruitment system, leaving a gap in the protection of authorized recruitment staff from unauthorized access to candidate data and model explanations, which relates to Article 15(1) and 15(4) of the AI Act.

**Risks:**

- Does not specify technical cybersecurity measures to prevent unauthorized access to candidate data and model explanations [medium] — Article 15(1)
  - Category: `accuracy_robustness_cybersecurity`
  - Suggested engineering action: Implement a multi-layered security framework, including encryption, secure data storage, and access controls.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Implement a multi-layered security framework, including encryption, secure data storage, and access controls.

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement on monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds does not address the need for an analysis of interaction between the AI system and other systems, creating a remaining gap with art:72, paragraph 2. 

**Risks:**

- Does not address interaction analysis with other systems [medium] — art:72
  - Category: `post_market_monitoring`
  - Suggested engineering action: Implement an interaction analysis module to monitor and report on interactions between the AI system and other systems.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other

**Recommendations:**

- Implement interaction analysis module
- Analyze interactions between AI system and other systems

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The system lacks specific requirements for model version rollback and post-deployment monitoring, creating a gap with art:15(4) and art:72(2).

**Risks:**

- Does not specify rollback procedures for model version failures [medium] — Article 15(4)
  - Category: `accuracy_robustness_cybersecurity`
  - Suggested engineering action: Implement model version rollback procedures

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con

**Recommendations:**

- Define model version rollback procedures
- Establish post-deployment monitoring plans

---
