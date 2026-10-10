# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 5
- Low: 9

### Overall analysis

Overall, the assessment reviewed 16 requirements and identified 2 high-risk findings, 5 medium-risk findings, 9 low-risk findings. The main review focus areas are data governance, record keeping, accuracy robustness cybersecurity, transparency, human oversight. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 2 high, 5 medium, 9 low.
- Most frequent mapped obligation areas: data governance (13), record keeping (5), accuracy robustness cybersecurity (4), transparency (4), human oversight (2).
- 7 low-risk requirements appear to describe a control or safeguard, but still needs clarification/evidence review.

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.


## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** FR-1 ingests candidate resumes, cover letters and form responses for a likely Annex III employment system but defines no data governance controls (provenance, relevance, representativeness, bias examination, quality). Ingested data feeds scoring and ranking (FR-2, FR-3), so ungoverned inputs could propagate errors or bias into candidate decisions.

**Risks:**

- No data collection process, data origin, or data-preparation practices (cleaning, annotation, labelling) are defined for ingested resumes, cover letters and form responses that may be used for training, validation or testing. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Document data sources, collection flow through the portal, and preprocessing steps; record provenance metadata for each ingested item and flag which data is reused for training/validation/testing.
- No examination or mitigation of possible biases is specified for ingested free-text and form data, which may contain or proxy protected characteristics (name, gender, age, nationality, photo, career gaps) and feed downstream scoring in FR-2. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Add ingestion-stage bias checks: identify and minimise protected-attribute fields and proxies, and run representativeness analysis on historical and incoming candidate data before use in model development.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Document data origin, collection process and preprocessing, with provenance metadata, for all ingested candidate data.
- Add bias examination and protected-attribute/proxy handling at ingestion, with representativeness checks.
- Define data quality and validation rules, and record the ingestion pipeline in the technical documentation.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 generates candidate suitability scores in a recruitment (Annex III) context without specifying data governance for the scoring data and model (representativeness, bias examination, data quality). Transparency, human oversight, and review controls exist in related requirements (FR-4, FR-5, FR-6, FR-10), so the main remaining gap is data governance, plus a minor gap in documenting score semantics.

**Risks:**

- No requirement for training/validation/testing data sets to be relevant, representative, error-free and statistically appropriate for the candidate groups being scored; skewed data could produce discriminatory suitability scores. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Add acceptance criteria for dataset representativeness, completeness and statistical properties across candidate groups; document validation results per model release.
- No data governance practices (design choices, data origin, preparation, bias examination and mitigation) are specified for how skills, education and experience are extracted and used in scoring. [medium] - Article 10(2)
  - Category: `data_governance`
  - Action: Define and record data provenance, extraction/labeling steps, and a bias examination and mitigation process (e.g., proxy-feature checks on education/experience) as part of the scoring pipeline.
- Score meaning, scale, intended use and known limitations are not defined in FR-2; FR-4 explains factors but does not cover score documentation or instructions for use for deployers. [low] - Article 13(2)
  - Category: `transparency`
  - Action: Document the score definition, range, performance metrics and limitations in the instructions for use, and cross-reference FR-4 and FR-5.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.

**Recommendations:**

- Specify dataset representativeness, completeness and statistical-property criteria for training, validation and testing data, with per-release validation evidence.
- Establish documented data governance covering provenance, extraction design choices, and bias examination/mitigation for scoring features.
- Include score definition, accuracy metrics and limitations in the deployer instructions for use, linked to FR-4 and FR-5.

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 ranks candidates in an Annex III employment context, but it does not specify data governance for the ranking inputs or accuracy declaration for the ranking output. Transparency and human oversight are partly covered by FR-4, FR-5 and FR-6, so only the remaining gaps are flagged.

**Risks:**

- No requirement ensures that the data behind the suitability score and ranking is relevant, representative, and examined for bias across candidate groups. Biased rankings could systematically disadvantage candidates. [high] - Article 10(3)
  - Category: `data_governance`
  - Action: Add requirements for validating training, validation and testing data for representativeness and errors. Include bias testing of ranking outcomes across protected groups and document the data governance practices.
- FR-3 sets no accuracy or robustness targets for the ranking, and no metrics are declared in the instructions for use. Rank-order quality and consistency cannot be verified or communicated. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define ranking accuracy metrics, such as rank correlation or error rates per group, with acceptance thresholds. Add robustness tests and declare the metrics in the instructions for use.
- FR-4 and FR-5 explain scores and notify recruiters, but nothing requires the instructions for use to document the ranking logic, its limitations, or the known circumstances in which it performs poorly. Recruiters may over-rely on the ranking. [low] - Article 13(3)
  - Category: `transparency`
  - Action: Add a requirement for instructions for use covering the ranking's intended purpose, performance limitations, and the input data specifications. Link it to FR-4 and FR-5.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 

**Recommendations:**

- Add data governance and bias-testing requirements for the data feeding FR-2 scoring and FR-3 ranking.
- Specify ranking accuracy and robustness metrics and thresholds, and declare them in the instructions for use.
- Document ranking limitations and logic in the instructions for use, cross-referencing FR-4 and FR-5.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 provides recruiter-facing explanations of suitability scores, but does not state that the explanations faithfully reflect the model's actual drivers, nor that they are built on validated, representative data or have a declared accuracy. Misleading or unvalidated explanations could cause recruiters to over-trust biased scores in a high-risk employment context.

**Risks:**

- Nothing ensures the explained factors are derived from data sets that are representative, relevant and checked for bias; explanations built on skewed data could present discriminatory factors as legitimate. [medium] - Article 10(3)
  - Category: `data_governance`
  - Action: Document data set representativeness and bias checks for the features that appear in explanations, and exclude or flag proxies for protected attributes.
- The requirement does not define accuracy or fidelity metrics for the explanations, or declare them in the instructions for use, so recruiters cannot gauge how reliable the explanations are. [medium] - Article 15(3)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test explanation fidelity and stability metrics, and declare them with the score accuracy metrics in the instructions for use.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Validate the data behind the explained features for representativeness and bias, and screen for proxy variables.
- Set explanation fidelity and accuracy metrics, test them, and declare them in the instructions for use.
- Treat FR-6 (human override) as the oversight control and FR-5 (automation notice) as the transparency control; keep FR-4 consistent with both, and review whether the explanations meet Article 13 information needs.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 notifies recruiters that a ranking is model-generated, but it does not require the information recruiters need to interpret and use the output appropriately (e.g., limitations, confidence, ranking factors). A bare notification may not give deployers enough transparency in a high-risk recruitment context.

**Risks:**

- The notification only flags that a ranking is automated; it does not require interpretability information (ranking factors, confidence/accuracy, known limitations) that lets recruiters interpret and appropriately use the output. [medium] - Article 13(1)
  - Category: `transparency`
  - Action: Extend FR-5 so each notification links to an explanation of the main ranking factors, score/confidence indication, and known limitations. Make it available in the recruiter UI at the point of use.
- The requirement does not specify that recruiters receive instructions for use covering intended purpose, performance, accuracy limits and human oversight measures. FR-5 is a runtime notice, not provider-to-deployer documentation. [low] - Article 13(2)
  - Category: `transparency`
  - Action: Add a deliverable for instructions for use for deployers (intended purpose, accuracy metrics, limitations, oversight guidance) and reference it from the notification. Clarify the notification timing, e.g. before the recruiter acts on the ranking.

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.

**Recommendations:**

- Extend FR-5 to supply interpretability information (key factors, confidence, limitations) alongside the automated-ranking notice.
- Provide deployer instructions for use under Art. 13(2) and link them from the notification. Specify the notification timing and format so it is shown before recruiters act on a ranking.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 provides a review/override/reject control, which addresses the core of Art. 14, but it does not specify the supporting oversight enablers (understanding of limitations, automation-bias awareness, interpretability of outputs, ability to disregard output). Without these, the override may be nominal and reviewers may over-rely on rankings.

**Risks:**

- The requirement does not specify that recruiters are given the information and tooling to understand the ranking model's capacities and limitations or to interpret its outputs (e.g. score drivers), so override may be uninformed. [medium] - Article 14(4)
  - Category: `human_oversight`
  - Action: Show per-candidate score rationale and model limitation notes in the review UI, and include reviewer guidance in the instructions for use. Add acceptance criteria that reviewers can see the inputs and factors behind each ranking.
- No measures against automation bias are stated, and the scope is unclear: 'before a candidate is removed' does not say whether review is mandatory or optional, or whether overrides and rejections are recorded. Rankings may therefore effectively drive decisions without meaningful human assessment. [medium] - Article 14(3)
  - Category: `human_oversight`
  - Action: Define a mandatory review gate before any rejection or removal, with no auto-rejection path. Log reviewer decisions and overrides with reasons, and monitor override rates to detect rubber-stamping. Add automation-bias warnings and reviewer training.

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Human oversight, Article 14(3)**
  > 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and t

**Recommendations:**

- Provide score rationale and limitation information in the recruiter review interface.
- Enforce a mandatory human review gate with no auto-rejection, log overrides, and add automation-bias safeguards.
- Add explanation of ranking outputs and instructions for use for the override workflow, linked to FR-5.

---

### FR-7

**Risk level:** low

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Logged events cover outputs and recruiter actions but omit the Annex III point 1(a) minimum log fields: period of each use, reference database checked, input data leading to a match, and identity of persons verifying results. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Extend the log schema to record use start/end timestamps, reference databases and input data references, model version, and the identity of the reviewing recruiter for each verification.
- No retention period, log integrity protection, or provider access to logs is specified, so logs may not be kept for the period the Act requires or may be altered or deleted. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Define a retention policy (at least six months, or longer as sector or data-protection rules require), use append-only or tamper-evident storage, and restrict log access (consistent with NFR-4).

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Extend the log schema to cover the Annex III minimum fields and add model version and reviewer identity.
- Specify log retention, tamper-evidence and access controls, and align them with the NFR-4 access rules.

---

### FR-8

**Risk level:** low

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement does not specify the minimum log content for Annex III systems (period of each use, reference database checked, input data leading to a match, and identification of the natural persons verifying results), so traceability may be incomplete. [low] - Article 12(3)
  - Category: `record_keeping`
  - Action: Extend FR-8 to define a log schema covering session start/end timestamps, reference data/versions, input data references, model version, and reviewer identity and action for each screening decision.
- The requirement does not state that logs capture events relevant to identifying risk situations, substantial modifications, or post-market monitoring (e.g., model updates, anomalies, overrides), so logs cover only individual decisions. [low] - Article 12(2)
  - Category: `record_keeping`
  - Action: Add logging of model/version changes, anomalies, low-confidence outputs, and human overrides, and map each event type to Article 12(2)(a)-(c) purposes.
- The requirement says 'retain' but gives no retention period, automatic generation guarantee, or tamper-protection, so it cannot be verified against the obligation to keep automatically generated logs. [low] - Article 19(1)
  - Category: `record_keeping`
  - Action: Specify automatic log generation, a retention period of at least six months (or longer where other law requires), append-only/tamper-evident storage, and access controls for reviewers and authorities.

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Define a minimum log schema aligned with Article 12(3) for each screening decision.
- Log risk-relevant and modification events, including overrides, anomalies and model version changes.
- Specify retention period, automatic generation, and tamper-evident storage with access controls for logs.

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** No requirement-level risk retained; the requirement prevents a sensitive or prohibited feature.

---

### FR-10

**Risk level:** low

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** No requirement-level risk retained after aligning with the semantic profile.

---

### NFR-1

**Risk level:** low

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Validation covers only missing values, duplicates, and label inconsistency; it does not assess representativeness or statistical properties across relevant persons or groups, so dataset skew may go undetected. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Add checks for representativeness and group-level distribution/statistical properties on training, validation and test sets, with defined pass/fail thresholds.
- The requirement does not specify documented data governance practices (data origin, collection processes, preparation operations, bias examination) or retention of validation results as evidence of the controls applied. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Log validation outcomes per dataset version and record data provenance, preparation steps and bias examination results in a data governance record. NFR-5 covers runtime data quality alerts but not pre-training governance documentation.
- Failure handling is unspecified: it is unclear whether training is blocked or remediation is required when validation fails, nor are acceptable error and completeness thresholds defined, so the gate may not ensure data is 'free of errors and complete' for the intended purpose. [low] - Article 10(1)
  - Category: `data_governance`
  - Action: Define quantitative acceptance thresholds and make validation a blocking pipeline gate, with a documented remediation and re-validation workflow before model training.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(1)**
  > 1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used.

**Recommendations:**

- Extend dataset validation to representativeness and group-level statistical properties with defined thresholds.
- Persist validation results and data provenance/bias-examination records per dataset version as governance evidence.
- Make validation a blocking gate before training with explicit acceptance thresholds and a remediation workflow.

---

### NFR-2

**Risk level:** low

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement does not say which demographic groups, metrics, or representativeness criteria apply, so it does not show that test data are sufficiently representative or have appropriate statistical properties for the affected persons or groups. [low] - Article 10(3)
  - Category: `data_governance`
  - Action: Define the demographic groups, per-group metrics (e.g. error rates, selection rates) and minimum sample sizes. Document how representativeness of the evaluation data is checked against the intended population.
- The requirement is conditional on 'where lawful demographic evaluation data is available' and gives no fallback, no documented data origin or collection basis, and no handling of groups with insufficient data. Bias examination could be silently skipped. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Document the provenance and legal basis of demographic evaluation data. Define a fallback (e.g. proxy-free alternatives, synthetic or external test sets) and record a gap report when group data are unavailable.

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Specify the groups, metrics, sample-size criteria and representativeness checks for the per-group evaluation.
- Document the provenance and lawful basis of demographic evaluation data, and define a fallback and gap reporting when such data are unavailable.
- Define per-group acceptance thresholds, connect them to NFR-5 alerting, and require remediation before release.

---

### NFR-3

**Risk level:** low

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- The requirement bans protected attributes as explicit inputs but does not require examination or mitigation of proxy features (e.g. names, photos, address, gaps in employment, extracted from resumes in FR-1/FR-2) that could indirectly encode protected characteristics. [low] - Article 10(2)
  - Category: `data_governance`
  - Action: Add a requirement for proxy-variable analysis and bias examination of training, validation and testing data and extracted features, with documented mitigation measures.
- Excluding protected attributes may prevent bias measurement across groups, and the requirement does not define how bias detection and correction is performed, including whether special-category data may be processed under strict safeguards for this purpose. [low] - Article 10(5)
  - Category: `data_governance`
  - Action: Define a bias-testing procedure (e.g. a separate, access-controlled evaluation dataset with protected attributes) with necessity justification, safeguards and deletion rules, kept out of the ranking inputs.

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Require proxy-feature analysis and documented bias examination of datasets and extracted features.
- Define a controlled bias-testing process using protected attributes only for evaluation, with safeguards.
- Add per-release verification of attribute exclusion and disparate-impact monitoring within the risk management process.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 states an access-control intent but leaves its scope and enforcement unspecified: no role definitions, authentication strength, or coverage of logs and model outputs, and no protection against tampering. This limits how far it can show resilience against unauthorised access to or alteration of a high-risk recruitment system.

**Risks:**

- The requirement restricts only viewing of candidate data and explanations. It does not address unauthorised alteration of system use, outputs, scores or rankings (e.g. write/modify permissions, integrity of FR-2 scores, FR-3 rankings and FR-7 logs). [medium] - Article 15(5)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend access control to write/modify operations on scores, rankings, explanations and FR-7 audit logs. Add integrity protection (e.g. tamper-evident logs, role-based write restrictions) and test against unauthorised-manipulation scenarios.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Extend NFR-4 to cover write/modify access and integrity protection for scores, rankings, explanations and logs, and add adversarial/unauthorised-access tests.
- Define authorised roles, authentication, least-privilege and access-review rules, with stricter controls and audit logging for sensitive candidate data.

---

### NFR-5

**Risk level:** low

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system or plan (data sources, deployer-provided performance data, analysis cadence, ownership), so threshold breaches may not support continuous evaluation of compliance over the system lifetime. [low] - Article 72(2)
  - Category: `post_market_monitoring`
  - Action: Link alerting to a documented monitoring plan that specifies metrics, data sources (including deployer feedback), review cadence, alert owners, and retention of alert records.
- No escalation, triage, or corrective-action workflow is defined for threshold breaches, and threshold-setting is not tied to identified risks (e.g., health-safety or bias risks), so alerts may not feed the iterative risk management process. [low] - Article 9(2)
  - Category: `risk_management`
  - Action: Define risk-derived threshold rationale and an alert-to-action workflow (severity levels, responders, SLAs, mitigation or rollback, risk register update), and review thresholds periodically.

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Link alerting to a documented post-market monitoring plan with metrics, data sources, cadence, owners, and alert record retention.
- Define risk-based threshold rationale and an escalation and corrective-action workflow that updates the risk management file.

---

### NFR-6

**Risk level:** low

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.

**Risks:**

- Failure thresholds and metrics for 'safety, robustness, or fairness checks' are not defined, so the rollback trigger is unclear and may be applied inconsistently or never fire. [low] - Article 15(4)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define measurable pass/fail thresholds per check (accuracy, robustness, fairness) and automatic or manual rollback triggers. Verify that the rollback target version meets the same thresholds and that fallback behaviour is safe.
- The requirement does not say that a failed check leads to the corrective-action and information workflow (investigation, notifying deployers or authorities) when the system may be non-conformant. It treats rollback as a purely technical step. [low] - Article 20(1)
  - Category: `risk_management`
  - Action: Add an escalation path from a failed check or rollback to the compliance owner. Include criteria for when a rollback must trigger a corrective-action review and a duty-of-information assessment, and keep versioned, approved model artefacts available as rollback targets.

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ

**Recommendations:**

- Define quantitative thresholds and triggers for safety, robustness and fairness checks, and validate the rollback target against them.
- Log rollback events and feed them into post-market monitoring, with a risk reassessment before re-promotion.
- Link failed checks and rollbacks to a documented corrective-action and escalation workflow.

---
