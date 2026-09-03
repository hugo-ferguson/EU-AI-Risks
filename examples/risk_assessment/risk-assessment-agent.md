# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 7
- Medium: 9

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** FR-1 only specifies raw ingestion of candidate resumes, cover letters and application data without any of the data governance, quality, bias-mitigation, or transparency safeguards mandated for high-risk AI systems used in recruitment (Annex III, point 4 – employment/worker management), leaving the ingestion pipeline non-compliant with Articles 10, 13 and 26.

**Risks:**

- The requirement does not specify any data governance and management practices (design choices, provenance, purpose limitation, bias examination) for the ingested resume/cover-letter/application data as required for high-risk AI training/validation/testing data sets. [high] — Article 10(2)
- No requirement ensures the ingested data sets are relevant, sufficiently representative, and statistically appropriate for the population of candidates, risking discriminatory outcomes. [high] — Article 10(3)
- Resumes and cover letters may reveal special category data (e.g., name-based ethnicity, religious affiliation, disability disclosures, gender); FR-1 contains no safeguards, minimization, or handling controls for such data as required when special categories are processed for bias detection/correction. [high] — Article 10(5)
- The deployer's obligation to ensure that input data it controls is relevant and sufficiently representative for the intended purpose is not reflected in the ingestion requirement. [medium] — Article 26(4)
- There is no provision for informing candidates that their application materials will be processed/ingested by an automated/AI system, which is required for transparency toward affected natural persons in high-risk employment contexts. [medium] — Article 13(3)
- The ingestion function itself is not linked to the mandatory automatic event-logging capability required for high-risk AI systems, creating a traceability gap from the very first data-intake step. [low] — Article 12(1)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv
- **Obligations of deployers of high-risk AI systems, Article 26(4)**
  > 4. Without prejudice to paragraphs 1 and 2, to the extent the deployer exercises control over the input data, that deployer shall ensure that input data is relevant and sufficiently representative in view of the intended purpose of the high-risk AI system.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

**Recommendations:**

- Define and document data governance practices (origin, purpose, preparation, bias examination) for all ingested resume/cover-letter/application data per Art. 10(2).
- Implement data quality checks at ingestion to verify representativeness and statistical adequacy of candidate data per Art. 10(3).
- Add explicit controls (pseudonymisation, access restriction, deletion triggers) for any special category data detected during ingestion, per Art. 10(5) safeguards.
- Require deployer-side validation that ingested input data is relevant and representative before use, per Art. 26(4).
- Add a transparency notice at the application portal informing candidates that an AI system will process their submissions, per Art. 13(3)/Art. 50 transparency obligations.
- Extend the ingestion module to write immutable log entries (timestamp, source, data type) to satisfy the record-keeping requirement in Art. 12(1).

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 defines the core suitability-scoring logic for a recruitment AI system (classified high-risk under Annex III as it affects employment/access to self-employment) but omits the mandated data governance, bias-mitigation, accuracy, and risk-management safeguards that must underpin that scoring logic before it can be lawfully used to rank candidates.

**Risks:**

- The requirement does not specify examination of training/scoring data (education, experience, skills) for biases that could produce discriminatory outcomes or indirect proxies for protected characteristics such as age, gender or disability. [high] — Article 10(2)(f)-(g)
- No requirement that the data used to derive the suitability score be relevant, sufficiently representative and statistically appropriate for the population of candidates being scored. [high] — Article 10(3)
- The scoring function lacks any defined accuracy metrics or declared accuracy levels, and no robustness/consistency requirement is specified for the scoring model across its lifecycle. [medium] — Article 15(1)
- No accuracy metrics are required to be declared in accompanying instructions of use for the scoring feature, undermining transparency to deployers/recruiters. [medium] — Article 15(3)
- The requirement does not tie the scoring functionality into a risk management process that identifies and mitigates foreseeable risks to health, safety or fundamental rights arising from automated candidate scoring. [medium] — Article 9(2)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Add bias examination and mitigation steps (Art. 10(2)(f)-(g)) for the features (experience, education, skills) used to compute the suitability score, including testing for proxy discrimination.
- Define and document dataset representativeness and statistical quality criteria for the data feeding the scoring model per Art. 10(3).
- Define target accuracy/robustness metrics for the suitability score and declare them in instructions of use per Art. 15(1) and 15(3).
- Incorporate the scoring functionality into the system's risk management process to identify and mitigate fundamental rights risks per Art. 9(2).

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 implements the core ranking function of a recruitment AI system that falls under Annex III as a high-risk employment/recruitment use case, but the requirement as written only specifies that candidates be ranked by score for recruiter review without any safeguards to ensure that human oversight remains meaningful, that the ranking presentation does not induce automation bias, or that the underlying scoring/ranking logic is checked for bias before being surfaced.

**Risks:**

- Presenting candidates as a definitive score-based ranking, without design measures to counter over-reliance, risks recruiters mechanically accepting the automated order instead of exercising genuine independent judgment, violating the requirement to keep staff aware of automation bias. [high] — Article 14(4)(b)
- The ranking mechanism as specified does not guarantee that, in each individual case, the recruiter is enabled to disregard, override or reverse the automatically generated order rather than simply working down the ranked list, undermining the effectiveness of human oversight for this specific function. [medium] — Article 14(4)(d)
- FR-3 defines ranking purely on the suitability score without requiring bias detection/mitigation checks on how that score translates into candidate ordering, risking propagation of discriminatory patterns from training data into the visible ranking. [medium] — Article 10(2)(f)-(g)
- The requirement does not specify that the ranking output be accompanied by sufficiently transparent information (e.g., accuracy/limitations, confidence) to enable the recruiter to correctly interpret and use the ranked output, as required for high-risk system outputs feeding human decisions. [low] — Article 13(1)
- As a high-risk employment AI system feature that materially influences candidate progression, the ranking function should be covered by a deployer fundamental rights impact assessment before deployment, which FR-3 does not reference or require. [medium] — Article 27(1)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Add explicit UI/UX and workflow controls (e.g., unordered/blind review mode, confidence indicators) that mitigate automation bias when presenting the ranked list to recruiters.
- Require that recruiters can freely override, reorder, or disregard the automated ranking for any individual candidate, and log that this capability was exercised or available.
- Incorporate bias detection and mitigation checks on the scoring-to-ranking logic itself, not just on the score generation, and document these checks per Article 10 data governance requirements.
- Attach interpretability metadata (accuracy metrics, known limitations, intended use conditions) to the ranking output so recruiters can correctly interpret it per Article 13.
- Ensure a fundamental rights impact assessment is completed and documented before deploying the ranking feature in a live recruitment workflow.

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 only provides explanations of suitability scores to the recruiter, but fails to address the affected candidate's right to a clear and meaningful explanation of an AI-assisted employment decision, and lacks detail on how explanations support correct interpretation and provider-level documentation obligations required for high-risk AI systems used in recruitment.

**Risks:**

- The system provides explanations only to the recruiter, not to candidates who are subject to the score-based decision, failing the affected person's right to obtain a clear and meaningful explanation of the AI system's role and the main elements of the decision. [high] — Article 86(1) - Right to explanation of individual decision-making
- There is no requirement that the provider document or supply the technical capabilities and characteristics enabling explanation of outputs as part of instructions for use to deployers, risking incomplete transparency documentation for the recruitment system. [medium] — Article 13(3)(b)(iv) - Transparency and provision of information to deployers
- The requirement does not specify that explanations must be sufficiently accurate and complete to allow the human overseer to correctly interpret the system's output and counteract automation bias, which is necessary for effective human oversight of a high-risk recruitment AI system. [medium] — Article 14(4)(b)-(c) - Human oversight
- No mention of ensuring the explanation is 'sufficiently transparent' to enable the recruiter to interpret and use the output appropriately as opposed to merely listing 'main factors', which may not meet the required depth of interpretability mandated for high-risk systems. [low] — Article 13(1) - Transparency and provision of information to deployers

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add a requirement for the system (or deployer process) to provide candidates with a clear, meaningful explanation of the AI system's role and the main elements of the suitability decision upon request, per Article 86(1).
- Ensure provider technical documentation and instructions for use describe the system's technical capacity to explain outputs, per Article 13(3)(b)(iv).
- Specify that explanations must be detailed and accurate enough to let recruiters correctly interpret system output, detect anomalies, and avoid over-reliance (automation bias), per Article 14(4).
- Define minimum content/quality standards for the 'main factors' explanation (e.g., feature attribution, confidence, limitations) to ensure sufficient transparency per Article 13(1).

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 only notifies recruiters that a ranking was automated, but the AI Act requires deployers of high-risk recruitment AI systems to also inform the affected natural persons (candidates) that they are subject to an automated decision, and to provide recruiters with more comprehensive transparency information than a simple notification.

**Risks:**

- The requirement notifies only recruiters and does not ensure that candidates (the natural persons subject to the automated ranking decision) are informed that a high-risk AI system was used, as required for deployers of Annex III employment/recruitment AI systems. [high] — Article 26(11)
- No mechanism is specified to inform workers' representatives or affected individuals in line with employment-context transparency obligations before the AI system is put into use for candidate screening. [medium] — Article 26(7)
- Merely notifying recruiters that a ranking is 'automated' does not satisfy the broader Article 13 transparency-to-deployer obligation, which requires instructions covering the system's characteristics, capabilities, limitations, accuracy/robustness metrics, and foreseeable risks so recruiters can properly interpret and use the output. [medium] — Article 13(3)
- The notification requirement does not address whether recruiters have the competence, training, and authority needed to exercise meaningful human oversight, a related deployer obligation not captured by a bare notification. [low] — Article 26(2)

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Add a requirement for the system/deployer process to directly inform candidates that a decision or ranking affecting them was generated or assisted by an automated high-risk AI system, satisfying Article 26(11).
- Extend deployer procedures to inform workers' representatives and affected individuals prior to deployment where the recruitment AI is used at the workplace, per Article 26(7).
- Enhance recruiter-facing information to include system characteristics, accuracy/robustness metrics, and known limitations, not just a flag that ranking was automated, to meet Article 13(3).
- Confirm and document that recruiters assigned to oversee the system have the necessary competence, training, and authority per Article 26(2).

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 addresses only the ability to override/reject a ranking, but does not ensure the recruiter has the competence, training, understanding of system capabilities/limitations, or awareness of automation bias needed to exercise that override meaningfully, nor does it require a 'stop' mechanism or safeguards against blind reliance on the automated ranking as mandated for high-risk AI systems used in recruitment (Annex III employment use case).

**Risks:**

- The requirement does not ensure recruiters are enabled to properly understand the system's capacities and limitations before overriding, as required for effective human oversight. [medium] — Article 14(4)(a)
- There is no provision ensuring recruiters remain aware of automation bias (over-reliance on automated rankings), risking rubber-stamping of AI outputs rather than genuine override. [high] — Article 14(4)(b)
- The requirement does not guarantee the override capability is commensurate with system risk/autonomy or built-in as technically feasible per the oversight design obligations on providers. [medium] — Article 14(3)
- No mechanism described to interrupt or halt the system ('stop' function) if the automated ranking process malfunctions, only a post-hoc override on individual candidates. [medium] — Article 14(4)(e)
- The requirement does not address the deployer obligation to assign human oversight only to persons with necessary competence, training, and authority, which is separate from merely allowing an override action in the UI. [high] — Article 26(2)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Human oversight, Article 14(3)**
  > 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and t
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Add a requirement that recruiters assigned oversight duties receive documented training on the system's capabilities, limitations, and known failure modes before being authorized to override rankings.
- Implement UI/UX safeguards (e.g., mandatory rationale entry, bias warnings) that counter automation bias and prompt critical review rather than passive acceptance of rankings.
- Define oversight measures commensurate with the risk level of the ranking model, including provider-supplied guidance on when built-in versus deployer-side overrides apply.
- Add a 'stop/halt' capability allowing recruiters or administrators to suspend the automated ranking process entirely, not just override individual candidate outcomes.
- Add an organizational requirement that only recruiters with verified competence, training, and authority are permitted to perform overrides, with access controls enforcing this.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** FR-7 correctly identifies the core log content (scores, rankings, explanations, overrides, decisions) but does not specify a minimum retention period, timestamping/sequencing of events, or protection of log integrity, leaving gaps against the Article 12 and Article 19/26 record-keeping obligations for this Annex III high-risk (employment) AI system.

**Risks:**

- The requirement does not specify that logs must be retained for at least six months (or longer per applicable law), risking non-compliance with the mandatory retention period for high-risk AI system logs. [high] — Article 19(1)
- As a deployer-operated recruitment system, the requirement omits the deployer's own obligation to keep the automatically generated logs under its control for the same minimum six-month period. [high] — Article 26(6)
- FR-7 does not require timestamps or a documented sequence/period of use for each logged event, undermining the traceability needed to identify risk-presenting situations or substantial modifications. [medium] — Article 12(2)(a)
- The requirement does not ensure logs support post-market monitoring data collection, e.g. linking logged events to monitoring obligations under Article 72. [medium] — Article 12(2)(b)
- No mention of measures to ensure log integrity/tamper-resistance, which is necessary for logs to reliably support human oversight monitoring under Article 26(5) and later audits. [low] — Article 26(5)

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Obligations of deployers of high-risk AI systems, Article 26(5)**
  > 5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and sh

**Recommendations:**

- Add an explicit minimum retention period (≥6 months, or longer if required by applicable law) for all logged events.
- Specify that the deployer (recruiter/employer) must retain logs under its control for the mandated retention period, separate from provider-side log retention.
- Require each logged event (score, ranking, explanation, override, decision) to include a timestamp and sequential/session identifier to support traceability and risk detection.
- Ensure log data is structured to feed post-market monitoring processes (Article 72) and human oversight monitoring (Article 26(5)).
- Add tamper-evidence or integrity-protection controls (e.g., write-once storage, hashing) for audit logs.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** FR-8 requires retention of audit records for traceability but omits the EU AI Act's mandatory minimum retention period, the requirement that logging be automatic and lifecycle-wide, and the specific categories of events (risk, substantial modification, post-market monitoring) that must be captured — creating record-keeping compliance gaps for this high-risk (employment/recruitment) AI system.

**Risks:**

- FR-8 does not specify a minimum retention period for audit records, whereas the Act requires logs to be kept for at least six months (or longer per applicable law). [high] — Article 19(1)
- The same six-month minimum retention obligation applies to deployers, but FR-8 does not distinguish provider vs. deployer log-retention responsibilities or reference this deployer duty. [medium] — Article 26(6)
- FR-8 describes manual/after-the-fact retention of 'audit records' rather than a technical capability for automatic recording of events (logs) over the entire lifetime of the system, as mandated for high-risk AI systems. [medium] — Article 12(1)
- FR-8 does not ensure the logging captures events relevant to identifying risk situations, substantial modifications, or supporting post-market monitoring and operational oversight, as required for traceability. [medium] — Article 12(2)
- No mention of integrating audit records into the technical documentation required to demonstrate compliance to regulators and notified bodies. [low] — Article 11(1)

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Technical documentation, Article 11(1)**
  > 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI syste

**Recommendations:**

- Add an explicit minimum log retention period of at least six months (or longer if required by applicable Union/national law).
- Clarify provider and deployer responsibilities for keeping and controlling automatically generated logs under Articles 19 and 26(6).
- Specify that logging occurs automatically and continuously over the system's operational lifetime, not just as a retained audit record.
- Expand log content requirements to include events needed for risk/substantial-modification detection and post-market monitoring, not only input data, model version, and human actions.
- Reference audit record content and retention design in the technical documentation to support conformity assessment.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** FR-9 correctly reflects the Article 5(1)(f) ban on emotion-recognition and biometric identification in employment/recruitment contexts, but it lacks the technical and procedural detail needed to actually enforce and evidence that prohibition, and it omits the related ban on biometric categorisation of sensitive traits, creating gaps between stated intent and enforceable controls.

**Risks:**

- FR-9 does not address the separate prohibition on biometric categorisation systems that infer or categorise natural persons by race, political opinions, trade union membership, religious/philosophical beliefs, sex life or sexual orientation, which could still be triggered via voice, text-sentiment, or video-based inference tools used in candidate screening. [medium] — Article 5(1)(g) - Prohibited AI practices (biometric categorisation)
- No technical control is specified to prevent biometric/facial/emotion data that may be inadvertently captured through FR-1's ingestion of resumes, cover letters, and application form responses (e.g., embedded photos or video links) from being processed by downstream scoring or ranking components, leaving a practical circumvention path for the prohibition. [high] — Article 5(1)(f) - Prohibition of emotion recognition in employment
- There is no logging, monitoring, or audit requirement tied specifically to verifying that prohibited biometric/emotion-recognition functionality is never invoked, making it difficult to demonstrate ongoing compliance with the Article 5 prohibition to market surveillance authorities. [medium] — Article 12 - Record-keeping and logging
- FR-9 does not account for the narrow statutory exception allowing emotion-recognition/biometric processing for medical or safety reasons, risking either an overly rigid implementation that blocks lawful safety-related uses or, conversely, ambiguity that could be exploited to justify prohibited processing under a mislabelled 'safety' rationale. [low] — Article 5(1)(f) exception clause

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have othe
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

**Recommendations:**

- Extend the prohibition scope to explicitly cover biometric categorisation of protected/sensitive attributes, not just biometric identification and emotion recognition.
- Implement data-ingestion filters/validation (linked to FR-1) that detect and strip or block any embedded photo, video, or biometric metadata before it reaches scoring/ranking models.
- Add a dedicated audit log capturing any attempted invocation of biometric/emotion-recognition components and periodic compliance verification reports for regulators.
- Define and document the narrow medical/safety exception handling process, requiring explicit approval and justification before any biometric processing is permitted under that carve-out.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** FR-10 only creates a generic 'request review' channel but does not guarantee that candidates receive the clear, meaningful explanation required by Art. 86, that a genuine human re-assessment with authority to change the outcome occurs, or that the mechanism is documented as part of the mandatory fundamental-rights-impact-assessment governance arrangements for this high-risk recruitment AI system (Annex III, point 4).

**Risks:**

- The review channel does not ensure candidates receive 'clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken', as required for high-risk AI decisions affecting a person's rights. [high] — Article 86(1) – Right to explanation of individual decision-making
- Requesting a review does not guarantee that a competent human overseer actually re-evaluates and can override the automated ranking output, risking automation bias and a purely cosmetic complaint channel. [medium] — Article 14(4) – Human oversight measures
- The requirement does not tie the review/complaint channel to the deployer's fundamental rights impact assessment, which must include 'arrangements for internal governance and complaint mechanisms' for this high-risk employment/recruitment use case. [medium] — Article 27(1)(f) – Fundamental rights impact assessment

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Redesign the channel so that every review request is accompanied by a clear, meaningful explanation of the AI system's role and the main factors behind the specific ranking decision, per Art. 86(1).
- Ensure the review process routes to a qualified human recruiter empowered to override or amend the ranking outcome, with documented competence and authority per Art. 14(4).
- Incorporate the review/complaint mechanism explicitly into the deployer's fundamental rights impact assessment and internal governance documentation as required by Art. 27(1)(f).

---

### NFR-1

**Risk level:** high

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** NFR-1 only checks for missing values, duplicates, and inconsistent labels, but Article 10 of the EU AI Act requires much broader data governance for high-risk (employment) AI systems, including bias examination/mitigation, representativeness, statistical adequacy, and documentation of data provenance and design choices — none of which are covered by this requirement.

**Risks:**

- NFR-1 does not require examination of training/validation/testing data for biases likely to cause discrimination or negative fundamental rights impacts, as recruitment is a high-risk use case under Annex III. [high] — Article 10(2)(f)
- NFR-1 lacks any requirement for measures to detect, prevent, and mitigate biases identified in the datasets, leaving a gap in bias mitigation controls prior to training. [high] — Article 10(2)(g)
- NFR-1 does not require datasets to be relevant, sufficiently representative, and statistically appropriate with respect to the persons/groups the system will be used on (candidates), risking skewed or unrepresentative training data for a recruitment tool. [high] — Article 10(3)
- NFR-1 omits documentation of data governance practices such as design choices, data collection processes/origin, and data-preparation operations (annotation, labelling, cleaning), which are mandated for high-risk AI training data. [medium] — Article 10(2)(a)-(c)
- NFR-1 does not require identification of data gaps or shortcomings that could prevent regulatory compliance, nor a plan to address them. [medium] — Article 10(2)(h)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Extend dataset validation to include bias examination for protected groups and characteristics likely to cause discrimination, not just structural data quality issues.
- Implement bias detection and mitigation measures (e.g., statistical parity checks, mitigation techniques) as part of the pre-training pipeline.
- Add representativeness and statistical adequacy checks for candidate demographic groups relevant to the recruitment context.
- Document data governance practices covering design choices, data origin/collection, and preparation operations (annotation, labelling, cleaning) for audit purposes.
- Establish a process to identify and log data gaps/shortcomings in training data and define remediation steps before model training proceeds.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** {"summary":"NFR-2 only requires demographic performance measurement 'where lawful demographic evaluation data is available', which is conditional and does not implement the mandatory bias-detection data governance regime, special-category-data safeguards, or documentation/risk-management integration required by Articles 10 and 9 of the EU AI Act for this high-risk (Annex III, employment) recruitment system.","risks":[{"description":"The requirement makes demographic bias evaluation conditional on data availability rather than mandating that providers establish data governance practices to examine and mitigate bias as required, creating a gap if suitable demographic data is deemed 'unavailable' and no fallback bias-mitigation measure is defined.","severity":"high","article_id":"art:10","paragraph_num":2,"provision":"Article 10(2)(f)-(g)"},"risks_cont":null,"risk_level":"high","recommendations":["placeholder"]}
</br>

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** NFR-3 only prohibits using explicit protected attributes as direct ranking inputs, but the EU AI Act's Article 10 data-governance obligations for this high-risk (recruitment) AI system require far more: proactive bias examination and mitigation, statistical representativeness testing, and a lawful basis for processing special-category data needed to detect and correct bias, none of which are addressed by a simple exclusion rule that leaves proxy-variable discrimination unmitigated.

**Risks:**

- Excluding named protected attributes does not satisfy the requirement to actively examine training/validation/testing data for biases likely to cause discrimination, including indirect/proxy discrimination via correlated features such as name, postcode, or employment gaps. [high] — Article 10(2)(f)
- The requirement lacks any mechanism to detect, prevent and mitigate biases once identified, as opposed to merely refusing to ingest protected attributes. [high] — Article 10(2)(g)
- No provision ensures the ranking model's training/validation/testing data sets are statistically representative of relevant persons or groups in relation to protected characteristics, which Article 10(3) requires. [medium] — Article 10(3)
- By categorically barring use of protected attributes, the system forecloses the narrow, safeguarded processing of special category data that Article 10(5) permits specifically to detect and correct bias, leaving no lawful audit mechanism to verify the ranking model is not discriminating. [medium] — Article 10(5)
- There is no continuous risk-management process identifying and mitigating fundamental-rights risks (e.g., discriminatory ranking outcomes) throughout the system lifecycle, as required for high-risk AI systems. [medium] — Article 9(2)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Add a bias examination and mitigation process covering both direct and indirect (proxy) discrimination in the ranking model's data and outputs, per Art 10(2)(f)-(g).
- Implement statistical representativeness checks on training/validation/testing datasets across protected characteristic groups per Art 10(3).
- Define a controlled, safeguarded procedure allowing exceptional processing of special category data solely for bias detection/correction, satisfying the conditions in Art 10(5) rather than a blanket exclusion.
- Integrate discriminatory-ranking risk identification and mitigation into the system's ongoing risk management system per Art 9(2).

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 only implements confidentiality-based access control for recruitment staff, but as an Annex III employment/recruitment high-risk AI system it must also satisfy broader cybersecurity, human-oversight competency, logging, and candidate-facing explanation obligations that are not addressed by simple staff-only access restriction.

**Risks:**

- Restricting explanation visibility to 'authorised recruitment staff' only, without provision for candidates (affected persons) to obtain explanations of decisions based on the AI output, conflicts with candidates' statutory right to an explanation. [high] — Article 86(1) - Right to explanation of individual decision-making
- The requirement addresses only authorisation/access control and does not specify technical measures to ensure resilience against attacks such as data poisoning, adversarial examples, or confidentiality attacks, which is required for high-risk AI system cybersecurity beyond user access restrictions. [medium] — Article 15(5) - Accuracy, robustness and cybersecurity
- Access is limited to 'authorised' staff but there is no requirement that those staff have the necessary competence, training, and authority for human oversight, as mandated for deployers of high-risk AI systems. [medium] — Article 26(2) - Obligations of deployers of high-risk AI systems
- No requirement to log or audit who accessed candidate data and model explanations, undermining traceability needed for post-market monitoring and incident detection. [medium] — Article 12(2) - Record-keeping
- If special category (protected attribute) data is processed for bias detection/correction, strict, documented access controls with confidentiality obligations are mandated, but NFR-4 does not reference documentation of access or confidentiality obligations tied to this specific processing. [low] — Article 10(5)(c) - Data and data governance

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Implement a mechanism allowing candidates to request and receive clear explanations of AI-influenced decisions affecting them, per Article 86.
- Extend security design to include AI-specific cybersecurity resilience measures (data/model poisoning, adversarial input detection), not just user-level access control.
- Define and enforce competence, training, and authority criteria for staff granted human-oversight access, and document this in deployer procedures.
- Add audit logging of every access event to candidate data and explanations, retained per Article 12 record-keeping requirements.
- If protected-attribute data is used for bias correction, implement documented, confidentiality-bound access controls and retention/deletion rules per Article 10(5).

---

### NFR-5

**Risk level:** high

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** NFR-5 only requires generating alerts when accuracy, bias, or data-quality thresholds are breached, but it lacks the documented post-market monitoring plan, defined accuracy/bias metrics, escalation to risk management and incident reporting, and human-oversight response mechanisms mandated by the AI Act for high-risk AI systems used in recruitment.

**Risks:**

- Alerting alone does not satisfy the requirement to establish and document a full post-market monitoring system and plan as part of the technical documentation, including systematic collection and analysis of performance data throughout the system's lifetime. [high] — Article 72(1)
- There is no requirement to declare the accuracy metrics and levels used to set the 'configured thresholds' in the instructions of use, as required for high-risk AI systems. [medium] — Article 15(3)
- The requirement does not specify how alert data feeds back into the risk management system for re-evaluation and adoption of mitigation measures when accuracy/bias/data-quality risks are detected. [high] — Article 9(2)(c)-(d)
- No mechanism is defined for escalating significant bias or accuracy deviations that pose fundamental rights risks to a serious incident report to market surveillance authorities. [medium] — Article 73(1)
- The requirement does not specify that threshold-breach alerts must be routed to a human overseer empowered to intervene, monitor, or halt the system, risking automation bias in the human oversight process. [medium] — Article 14(4)
- There is no methodology described for determining bias thresholds tied to the data governance obligation to examine, detect, prevent and mitigate biases likely to cause discrimination or harm to fundamental rights. [medium] — Article 10(2)(f)-(g)
- Alerts triggered by threshold breaches are not explicitly required to be captured in the automatic event logs needed for traceability and post-market monitoring. [low] — Article 12(2)

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Reporting of serious incidents, Article 73(1)**
  > 1. Providers of high-risk AI systems placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s

**Recommendations:**

- Define and document a formal post-market monitoring plan (per Annex IV) covering systematic collection, documentation, and analysis of accuracy/bias/data-quality data, not just threshold alerts.
- Declare the specific accuracy metrics and threshold levels in the system's instructions of use.
- Specify that threshold-breach alerts trigger a risk management review and, where needed, corrective/mitigation actions and model updates.
- Add an escalation path from severe threshold breaches to serious incident reporting to market surveillance authorities within the mandated timelines.
- Require that alerts be routed to a designated human overseer with authority and means to intervene, review, or suspend the system.
- Document the methodology for setting bias/data-quality thresholds tied to the data governance bias examination and mitigation process.
- Ensure all monitoring alerts and threshold breach events are captured in the system's automatic logging mechanism for traceability.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** {"summary":"NFR-6 introduces a rollback capability but only as a weak, undefined 'should support' feature with no linkage to the mandatory corrective-action, logging, risk-management or human-oversight obligations that apply once a high-risk AI system fails safety, robustness or fairness checks, leaving key compliance gaps.","risks":[{"description":"The requirement uses non-binding 'should' language and does not mandate that rollback actually occur, whereas Article 20 requires providers to immediately take necessary corrective actions (including disabling/withdrawing/recalling) once non-conformity is detected.","severity":"high","article_id":"art:20","paragraph_num":1,"provision":"Article 20(1)"},"description2placeholder"],"risk_level":"high","recommendations":["placeholder"]}

---
