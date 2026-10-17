# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 1
- Medium: 15

### Overall analysis

Overall, the assessment reviewed 16 requirements and identified 1 high-risk finding, 15 medium-risk findings. The main review focus areas are transparency, data governance, record keeping, risk management, human oversight. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 1 high, 15 medium, 0 low.
- Most frequent mapped obligation areas: transparency (13), data governance (10), record keeping (7), risk management (7), human oversight (5).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.


## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 6 Classification rules for high-risk AI systems (art:6); Article 13 Transparency and provision of information to deployers (art:13); Article 12 Record-keeping (art:12)

**Analysis:** FR-1 ingests candidate resumes, cover letters and form responses for a recruitment AI system (Annex III 4(a)) but defines no input-data governance, such as data quality, minimisation, or bias examination, and no logging of ingestion events. Unvalidated or unrepresentative inputs could propagate bias into downstream scoring and ranking (FR-2, FR-3).

**Risks:**

- FR-1 sets no governance or quality rules for ingested application data (origin, original collection purpose, cleaning/parsing operations, representativeness, bias examination of free-text and form fields), so bias or errors may enter the pipeline and any data later used for training, validation or testing. [medium] - Article 10(2) (`art:10:p2`)
  - Category: `data_governance`
  - Action: Define data governance for ingested application data: document sources and parsing/cleaning steps, run bias examination on ingested fields and extracted features, and validate representativeness across candidate groups before the data is used for training, validation or testing.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No ingestion-level logging is specified (submission events, parsing failures, input data provenance), which limits traceability of what input data fed each candidate's score and weakens post-market monitoring and deployer log retention. [medium] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Add automatic logging of each ingestion event (timestamp, input document references, parsing outcome, errors) linked to downstream scoring records. Make the logs available to deployers with retention of at least six months.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- The requirement does not address the risks specific to ingesting applicant data, such as discriminatory proxies in resumes or cover letters, or parsing errors disadvantaging certain groups. Nothing in it links to a lifecycle risk assessment of the input stage. [low] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Add ingestion-stage risks (parsing errors, proxy attributes, foreseeable misuse such as keyword stuffing) to the risk management file, with mitigations and periodic review.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Establish and document data governance and bias examination for ingested application data.
- Implement traceable ingestion logging linked to scoring records, with at least six months retention.
- Include input-stage risks in the continuous risk management process.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 6 Classification rules for high-risk AI systems (art:6); Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-2 generates suitability scores for recruitment (Annex III 4(a), high-risk) but does not address training/testing data quality, representativeness and bias, score transparency for deployers, or risk identification for the scoring logic. Without these, scores may be unreliable or discriminatory and recruiters cannot interpret them properly.

**Risks:**

- The scoring model uses experience, education and skills features without any stated requirement for training, validation and testing data to be relevant, representative, error-free and statistically appropriate across candidate groups, so bias in scores is possible. [high] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Add requirements for dataset validation and representativeness checks, and for per-group performance and bias testing of the suitability score, with documented results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'application' is an instance of the defined term 'personal data' (Article 3(50)), which Article 10 uses
- The requirement does not say that score outputs must be interpretable (contributing factors, accuracy metrics, limitations), so deployers may be unable to use the score appropriately. NFR-4 mentions model explanations only in terms of access control, not their content. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Specify that each score ships with feature-level explanations, and document accuracy metrics, known limitations and group-level performance in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- No risk identification is specified for the scoring logic, such as proxy discrimination from education or experience features, misuse as an automatic rejection filter, or drift. These risks to fundamental rights need continuous analysis and mitigation. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Add a risk register covering score-related fundamental-rights risks, including foreseeable misuse, with mitigations and post-deployment monitoring of score distributions.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))
- Applicants and workers are not required to be told that a scoring system evaluates them. Employer deployers must inform affected workers and their representatives, but no such notice is specified for this scoring function. [low] - Article 26(7) (`art:26:p7`)
  - Category: `transparency`
  - Action: Provide deployer documentation and notice templates telling candidates and workers' representatives that automated suitability scoring is used.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.

**Recommendations:**

- Add dataset validation, representativeness and per-group bias testing requirements for the scoring model.
- Require per-score explanations and document accuracy and limitations in the instructions for use.
- Create and maintain a risk register for the scoring function covering proxy bias, misuse and drift.
- Supply deployers with notice templates informing candidates and workers of automated scoring.

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 6 Classification rules for high-risk AI systems (art:6); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10)

**Analysis:** FR-3 ranks candidates in a high-risk recruitment system (Annex III 4(a)). Human review (FR-6), explanations (FR-4) and logging (FR-7) already exist, so the remaining gaps are bias risk in ranking and the transparency information deployers need to interpret ranks.

**Risks:**

- Ranking amplifies any bias in the suitability score, and no bias examination or mitigation is specified for the data behind the ranking. FR-2 and FR-3 contain no bias testing across candidate groups, so discriminatory ranking outcomes may go undetected. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add bias testing of rankings across protected groups on validation and test data, with documented mitigation and re-testing after model changes.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- Rank output lacks specified interpretability aids (score meaning, rank-order limitations, accuracy and known failure conditions) for recruiters. FR-4 explains score factors but does not cover how to interpret rankings or the system's limitations. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Show rank confidence and ties, and document in the instructions for use the ranking accuracy metrics, limitations and appropriate use. Reference FR-4 for the factor explanations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- Ranking-specific risks (automation bias from rank order, systematic exclusion of candidate groups, misuse of ranks as automatic cut-offs) are not identified in the risk management process. [low] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Add ranking-specific risks, including foreseeable misuse such as auto-rejecting low ranks, to the risk register with mitigations. Reference FR-6 as the existing control.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Add group-level bias testing and mitigation for ranking outputs, with documented results.
- Provide recruiter-facing rank interpretation guidance and document ranking accuracy and limitations in the instructions for use.
- Extend the risk register to cover ranking-specific risks and foreseeable misuse, linked to the FR-6 override control.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-4 gives recruiters per-score explanations, which supports deployer interpretability. It does not state that explanations are faithful to the model, that their limits are documented, or that the explanation capability is described in the instructions for use. It also covers only the recruiter, not the affected candidate.

**Risks:**

- FR-4 does not require the explanation capability, its limits, or guidance on interpreting the explanations to be documented in the instructions for use. Without this, recruiters may over-trust or misread the factors. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Document the explanation method, its fidelity and known limitations, and how to interpret the factors in the instructions for use. Add acceptance criteria that the factors reflect actual model drivers, not post-hoc rationalisations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- Explanations are directed only at recruiters. Nothing ensures the deployer can give affected candidates clear and meaningful explanations of the AI's role and the main elements of a decision. FR-10 provides a review channel but no explanation content for the candidate. [medium] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Make FR-4 explanations exportable in a candidate-facing form. Link them to the FR-7 logs and the FR-10 review process so deployers can answer explanation requests.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- FR-4 does not require that explanations help recruiters spot unreliable scores or automation bias, so the explanations may not support effective oversight. FR-6 supplies the override control itself, and the remaining gap is the interpretability aids. [low] - Article 14(3) (`art:14:p3`)
  - Category: `human_oversight`
  - Action: Show confidence or uncertainty indicators and the data limitations alongside the factors. Test with recruiters that the explanations support informed overrides under FR-6.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(3)(b))

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Human oversight, Article 14(3)**
  > 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer.

**Recommendations:**

- Document the explanation method, its fidelity and its limits in the instructions for use, and validate that the factors reflect real model drivers.
- Provide a candidate-facing explanation output tied to the FR-7 logs and the FR-10 review channel.
- Add uncertainty indicators and usability testing so recruiters can use the explanations to override scores under FR-6.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-5 notifies recruiters that a ranking is automated, which supports transparency, but it does not make the output interpretable (accuracy, limitations, explanation). It also does not cover candidate-facing explanation or worker information. FR-6, FR-7 and FR-10 already cover override, logging and review, so those are not flagged.

**Risks:**

- The notification only flags that a ranking is automated. It does not require the output to carry information (confidence, key factors, known limitations) that lets recruiters interpret and appropriately use the ranking. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Extend the notification to show the ranking rationale or main factors, a confidence or accuracy indicator, and a link to documented limitations, and make sure instructions for use cover these per Art. 13(3).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- The notification does not address automation bias. It does not warn recruiters against over-relying on the ranking or help them interpret it, and FR-6 gives override ability but no awareness or interpretation support. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Category: `human_oversight`
  - Action: Add in-UI cautions about automation bias and interpretation guidance next to the notification, and link it to the FR-6 review and override workflow.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))
- The requirement covers recruiters only. It does not provide the information needed for deployers to give affected candidates a clear and meaningful explanation of the AI system's role in a decision, since FR-10 only provides a review channel. [medium] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Generate a per-candidate explanation record of the AI's role and main ranking elements that the deployer can share on request, and trace it through FR-7 logs and FR-10 reviews.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- The system has no mechanism or documentation support for deployers who are employers to inform workers' representatives and affected workers about use of the system before it is used in recruitment. [low] - Article 26(7) (`art:26:p7`)
  - Category: `transparency`
  - Action: Provide deployer-facing documentation or a notice template for informing workers' representatives and affected persons before go-live, and clarify the scope of FR-5 notifications.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.

**Recommendations:**

- Make the notification interpretable: include main factors, confidence and limitations.
- Add automation-bias warnings and interpretation guidance in the recruiter UI.
- Produce per-candidate explanation records that deployers can share to support Art. 86 requests.
- Supply deployer notice templates and documentation for informing workers' representatives and affected workers.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13); Article 6 Classification rules for high-risk AI systems (art:6)

**Analysis:** FR-6 gives recruiters review, override and reject capability, which covers the core of Art. 14(4)(d). Remaining gaps: it does not address automation-bias awareness or output interpretation support, and it does not assign oversight to competent, trained and authorised staff.

**Risks:**

- FR-6 provides override capability, but nothing in FR-6 or the related requirements (FR-5 only notifies that a ranking is automated) supports recruiters in interpreting rankings, understanding system limitations, or guarding against automation bias, so overrides may be nominal. [medium] - Article 14(4) (`art:14:p4`)
  - Category: `human_oversight`
  - Action: Show score drivers and confidence or limitation indicators next to each ranking, add automation-bias warnings, and document the oversight measures in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- FR-6 does not require that reviewing recruiters have the competence, training and authority to override, nor does it define who may reject rankings, so oversight could be assigned to unqualified or unauthorised users. [medium] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Add role-based permissions limiting override and reject rights to trained recruiters, and provide deployer guidance and training material on the oversight role.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- FR-6 does not require the system to log or explain the human review outcome (override, reject, or confirm). FR-10 gives candidates a review channel, but without the recruiter's rationale and the AI's role being recorded, the deployer cannot give a clear explanation of the AI's role in a decision. [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Record each recruiter action with a rationale and the ranking shown, so deployers can explain the AI's role and the main elements of the decision.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Add interpretability aids and automation-bias safeguards to the review interface, and document them in the instructions for use.
- Enforce role-based override and reject permissions and supply oversight training guidance for deployers.
- Log recruiter decisions and rationale so the AI's role in each decision can be explained to affected candidates.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-7 covers the logged event types well (scores, rankings, explanations, overrides, decisions), but it does not specify log retention, log integrity, or event metadata such as timestamps and system version. Without these, logs may be insufficient for traceability and post-hoc review, and may not be kept for the required period.

**Risks:**

- FR-7 sets no log retention period; logs containing candidate data must be kept for at least six months, balanced against data protection law. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Define a configurable retention policy of at least 6 months (longer where the intended purpose requires), with documented GDPR-aligned deletion and automated enforcement.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- FR-7 lists what is logged but does not require automatic recording of events over the system lifetime with metadata (timestamp, model version, input reference, user ID) or tamper-evident storage, so logs may not support traceability or investigation of risk events. [medium] - Article 12(1) (`art:12:p1`)
  - Category: `record_keeping`
  - Action: Specify automatic, append-only event logging with timestamp, model/version ID, input reference, and actor ID for each event, plus integrity protection and lifetime coverage.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Deployer-side log handling is unspecified: FR-7 does not state that logs are accessible to the deployer for monitoring and kept under its control for the required period. NFR-4 restricts access to candidate data and explanations but does not cover log access or export. [low] - Article 26(6) (`art:26:p6`)
  - Category: `record_keeping`
  - Action: Add a requirement for deployer access to and export of logs, with role-based access (cf. NFR-4) and retention configurable by the deployer.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- FR-7 does not state that logged explanations and decision records are retrievable per candidate, which limits the deployer's ability to give affected persons meaningful explanations of the AI system's role in a decision (related to FR-10 review requests). [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Make logs queryable per candidate and decision so the score, explanation, override, and final decision can be reconstructed for FR-10 review requests and explanation responses.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Define a log retention period of at least 6 months with data-protection-aligned deletion.
- Specify automatic, tamper-evident logging with timestamps, model version, input reference, and actor ID.
- Add deployer access and export of logs under role-based controls.
- Make logs queryable per candidate so decisions can be reconstructed and explained.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 18 Documentation keeping (art:18)

**Analysis:** FR-8 covers audit traceability of input data, model version and human actions, but does not specify retention duration, event logging for risk identification and post-market monitoring, or deployer-side log access. Without these, logs may be kept too briefly or lack the events needed to detect risk and support monitoring.

**Risks:**

- FR-8 gives no retention period for audit records. Article 19(1) and Article 26(6) require logs to be kept for a period appropriate to the intended purpose, and for at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Define a configurable log retention policy of at least 6 months, aligned with GDPR minimisation and deletion rules, and enforce it with automated retention and purge jobs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- FR-8 records per-decision traceability only. It does not require logging of events relevant to identifying risk situations or substantial modifications, supporting post-market monitoring, or enabling deployer monitoring of operation (e.g. anomalies, drift, overrides, failures). [medium] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Extend the logging spec to capture system-level events (model changes, score anomalies, error and override rates, input anomalies) and make them exportable for post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))
- The requirement does not say that logs must be accessible to deployers or exportable in an interpretable form, so deployers may be unable to collect, store and interpret them as the instructions for use must describe. [low] - Article 13(3) (`art:13:p3`)
  - Category: `transparency`
  - Action: Specify a log schema and export or access interface, and document it in the instructions for use. Restrict access consistently with NFR-4 and protect log integrity.
  - Trace:
    - requirement term 'input data' is an instance of the defined term 'input data' (Article 3(33)), which Article 13 uses
    - requirement term 'input data' is the defined term 'input data' (Article 3(33)), which this provision uses

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.

**Recommendations:**

- Define a log retention policy of at least six months, with automated enforcement and GDPR alignment.
- Add system-level event logging for risk identification, post-market monitoring and deployer monitoring.
- Provide a documented log schema and export interface for deployers, with access controls (NFR-4) and tamper protection.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9); Article 4 AI literacy (art:4)

**Analysis:** FR-9 is a protective control that blocks facial recognition, biometric identification and emotion recognition in screening, which supports compliance with Art. 5(1)(f). Remaining gaps are that the requirement does not state how the block is enforced or tested, and it does not cover biometric categorisation.

**Risks:**

- FR-9 does not name biometric categorisation (Art. 5(1)(g)) or inference of emotions from text, voice or video, so a screening feature could still infer prohibited traits or emotions without being caught by the block. [medium] - Article 5(1) (`art:5:p1`)
  - Category: `prohibited_practices`
  - Action: Extend FR-9 to cover biometric categorisation and any inference of emotions or sensitive traits, including from video interviews, voice and text. Add a design-time check that rejects such features.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
    - requirement term 'facial recognition' is the defined term 'biometric identification' (Article 3(35)), which this provision uses
    - requirement term 'candidate screening' is the defined term 'profiling' (Article 3(52)), which this provision uses
- FR-9 has no stated enforcement mechanism or verification, such as a technical block, a configuration lock or tests. Without these, misuse through a later feature or integration could go undetected, and the foreseeable-misuse risk is not evidenced as managed. [medium] - Article 9(2)(b) (`art:9:p2:b`)
  - Category: `risk_management`
  - Action: Record misuse of biometric or emotion features as a risk in the risk management file. Enforce the block technically, for example by disabling biometric inputs and blocking the related modules. Add regression tests that confirm the block holds before each release (see Art. 9(8)).
  - Trace:
    - referenced by Article 9(5) (Article 9(2))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm; (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm; (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following: (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity; (d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence, based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity; (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage; (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons; (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement; (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years. Point (h) of the first subparagraph is without prejudice to Article 9 of Regulation (EU) 2016/679 for the processing of biometric data for purposes other than law enforcement.
- **Risk management system, Article 9(2)(b)**
  > (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse;

**Recommendations:**

- Widen FR-9 to cover biometric categorisation and emotion or trait inference from any modality, and add a feature-review gate.
- Implement the block as a technical control, document it in the risk management system, and add release-gate tests that confirm biometric and emotion inputs are rejected.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 27 Fundamental rights impact assessment for high-risk AI systems (art:27)

**Analysis:** FR-10 gives candidates a review channel but does not state that candidates can obtain an explanation of the AI system's role and the main elements of the decision, nor how requests are handled. Without this, the channel may not satisfy the right to explanation for recruitment decisions.

**Risks:**

- The requirement provides a review request channel but does not require delivering clear and meaningful explanations of the AI system's role in the decision and the main elements of the decision to the affected candidate. [medium] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Add a requirement that candidate review requests return a plain-language explanation of the ranking's role and the main factors behind the decision, using FR-7 logs and model explanations. Define the response timeline and the roles that approve the explanation.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- The requirement does not say that reviews are performed by competent, trained and authorised people who can disregard or reverse the automated output. FR-6 covers recruiter override before removal, but not the post-decision review path. [low] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Specify that review requests are routed to a designated reviewer with authority to override the ranking outcome, reusing the FR-6 override mechanism. Record the reviewer's decision and rationale in the FR-7 logs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Require review responses to include an explanation of the AI system's role and the main elements of the decision, with a defined response time.
- Route review requests to trained reviewers with authority to reverse the outcome, and log their decisions via FR-7.

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 11 Technical documentation (art:11)

**Analysis:** NFR-1 provides a data-quality control (missing values, duplicates, inconsistent labels) but does not cover bias examination, representativeness, or documentation of data governance practices. These parts of Article 10 remain open for a recruitment (high-risk) system.

**Risks:**

- Validation covers only technical quality (missing, duplicate, inconsistent labels); it does not require examination for biases likely to cause discrimination, nor bias detection/mitigation measures, in training and evaluation data for candidate ranking. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add dataset bias checks (e.g., outcome and label distribution across protected groups, proxy features) with documented mitigation before training. Coordinate with the bias thresholds in NFR-5 and the fairness checks in NFR-6.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No check for relevance, representativeness, or statistical properties of the datasets relative to the candidate populations the system will be used on; completeness and error-freeness are only partly covered by the missing-value and duplicate checks. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Define and automate representativeness and statistical-property checks per relevant candidate group, with pass/fail criteria that gate model training.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'training dataset' is an instance of the defined term 'training data' (Article 3(29)), which Article 10 uses
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- The requirement does not state that validation results, data provenance, labelling and cleaning operations, and identified data gaps are recorded as documented data-management procedures. [low] - Article 17(1)(f) (`art:17:p1:f`)
  - Category: `quality_management`
  - Action: Log the dataset validation outputs, remediation actions, and data gaps as versioned artifacts and link them to the QMS data-management procedure and the technical documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(f))

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Quality management system, Article 17(1)(f)**
  > (f) systems and procedures for data management, including data acquisition, data collection, data analysis, data labelling, data storage, data filtration, data mining, data aggregation, data retention and any other operation regarding the data that is performed before and for the purpose of the placing on the market or the putting into service of high-risk AI systems;

**Recommendations:**

- Extend dataset validation with bias examination and mitigation steps for protected groups.
- Add representativeness and statistical-property checks that gate model training.
- Record validation results and data-preparation operations as versioned QMS and technical documentation artifacts.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 13 Transparency and provision of information to deployers (art:13); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72)

**Analysis:** NFR-2 supports bias examination through per-group performance measurement, but it is conditional on data availability and does not say what happens with the results (acceptance thresholds, mitigation, disclosure). Without these, subgroup disparities may be measured but not acted on or documented.

**Risks:**

- Per-group measurement is optional ('where lawful data is available') and defines no fallback (e.g., proxy-free alternatives, synthetic or audit sampling) or documented data-gap handling when demographic data is unavailable, so bias examination may be skipped for some groups. [medium] - Article 10(2)(h) (`art:10:p2:h`)
  - Category: `data_governance`
  - Action: Document which groups lack evaluation data, record these as data gaps with a remediation plan, and define a fallback bias-assessment method.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- The requirement measures group performance but sets no acceptance criteria, no bias mitigation step on disparities, and no link to the test and validation data representativeness. NFR-5 alerts on thresholds, but thresholds for group-level gaps are not specified here. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Define per-group metrics and maximum disparity thresholds, feed them into NFR-5 alerts, and require a mitigation/retest workflow when thresholds are breached.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'lawful demographic evaluation data' is an instance of the defined term 'testing data' (Article 3(32)), which Article 10 uses
    - requirement term 'lawful demographic evaluation data' is the defined term 'testing data' (Article 3(32)), which this provision uses
- Per-group accuracy results are not required to be recorded in the instructions for use, so deployers may not know performance limits for specific groups. [low] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Add a requirement to publish subgroup performance metrics and known limitations in the instructions for use and technical documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(b))
    - requirement term 'lawful demographic evaluation data' is an instance of the defined term 'testing data' (Article 3(32)), which Article 13 uses
    - requirement term 'lawful demographic evaluation data' is the defined term 'testing data' (Article 3(32)), which this provision uses

**Cited provisions:**

- **Data and data governance, Article 10(2)(h)**
  > (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Record demographic data gaps and define a fallback bias-assessment method.
- Set per-group disparity thresholds, connect them to NFR-5 alerts, and define a mitigation and retest workflow.
- Include subgroup performance results and limitations in the instructions for use.

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** NFR-3 excludes protected attributes as direct ranking inputs, which is a bias control. It does not address proxy variables in resume-derived features (education, experience, skills) or bias examination of the data, so indirect discrimination could remain undetected.

**Risks:**

- Excluding protected attributes as explicit inputs does not cover proxy features (e.g. names, gaps in employment, institution, location, free-text cues in resumes and cover letters) that can reproduce discriminatory outcomes. No bias examination or mitigation of training, validation and testing data is specified. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add proxy-variable and disparate-impact testing across protected groups on training, validation and test data. Define bias detection and mitigation steps, and document them in the data governance records.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement does not state how compliance is verified. It sets no representativeness or statistical-property checks for the groups of candidates the system will rank. [low] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Add acceptance criteria and automated tests showing protected attributes (and their inferred proxies) do not influence ranking. Check dataset representativeness for the intended candidate population.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Discriminatory ranking against protected groups is a foreseeable fundamental-rights risk. The requirement does not tie the exclusion to the risk management process, residual-risk acceptance, or ongoing post-deployment monitoring for biased outputs. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Record discrimination risk in the risk register. Link NFR-3 to a mitigation control with periodic fairness metrics monitoring on live rankings, and review the results regularly.
  - Trace:
    - referenced by Article 9(5) (Article 9(2))

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Test for proxy variables and disparate impact, and document bias detection and mitigation in the data governance records.
- Add verifiable acceptance criteria and representativeness checks for NFR-3.
- Add discrimination risk to the risk register with ongoing fairness monitoring of production rankings.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10); Article 12 Record-keeping (art:12)

**Analysis:** NFR-4 provides role-based access control over candidate data and explanations, which supports Article 15(5) cybersecurity. Remaining gaps are limited to unspecified scope (e.g., model/training-data/log access, attack detection) and access-event logging.

**Risks:**

- The requirement covers only viewing of candidate data and explanations; it does not address protection of the model, training data, or outputs against unauthorised alteration or confidentiality attacks, nor measures to detect and respond to such attempts. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `cybersecurity`
  - Action: Extend access control to write/modify rights on model, configuration, training data and score outputs; add authentication hardening, least-privilege roles, and monitoring/alerting for unauthorised access or manipulation attempts, covering confidentiality attacks.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- FR-7 logs scores, explanations and overrides, but it is not stated that access to candidate data and explanations (including denied attempts) is itself logged or that logs are access-protected and retained by the deployer for at least six months. [low] - Article 26(6) (`art:26:p6`)
  - Category: `record_keeping`
  - Action: Extend FR-7 logging to access events (user, role, record, timestamp, denials), restrict log access to authorised roles, and set retention of at least six months, subject to data-protection law.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
    - requirement term 'candidate data' is the defined term 'personal data' (Article 3(50)), which this provision uses

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.

**Recommendations:**

- Extend access control to model, training data, configuration and outputs, with least-privilege roles and detection/alerting of unauthorised access or manipulation.
- Log access events including denials under FR-7, protect the logs, and retain them for at least six months subject to data-protection law.

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** NFR-5 provides threshold-based alerts for accuracy, bias and data quality, which supports post-market monitoring. It does not specify alert routing, escalation, or how alert data feeds the documented post-market monitoring and risk management processes, so alerts may not trigger corrective action.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system that collects and analyses performance data across the lifecycle; the requirement does not state who receives alerts, how they are recorded, or how they feed corrective or preventive action. [medium] - Article 72(2) (`art:72:p2`)
  - Category: `post_market_monitoring`
  - Action: Persist alerts and underlying metrics in a monitoring log, define alert owners and escalation paths, and link alert records to the post-market monitoring plan and to corrective-action workflows (e.g. the NFR-6 rollback).
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- Thresholds are only 'configured' without a requirement that they derive from predefined metrics and probabilistic thresholds appropriate to the intended purpose (recruitment screening), or that changes to them are governed. [low] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Document threshold values and rationale in the risk management file, tie them to the accuracy metrics declared in the instructions for use, and put threshold changes under version control with approval.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
    - requirement term 'model accuracy' is an instance of the defined term 'performance of an AI system' (Article 3(18)), which Article 9 uses
- Alerts on 'bias metrics' do not specify which metrics or groups are covered or how they link to bias examination and mitigation (NFR-2 covers measurement only where demographic data is available). Alerts may be silent for groups lacking data. [low] - Article 10(2) (`art:10:p2`)
  - Category: `data_governance`
  - Action: Define bias metrics and per-group thresholds consistent with NFR-2, and add a data-gap alert for groups with insufficient evaluation data, with a mitigation procedure for triggered alerts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.

**Recommendations:**

- Persist alerts and route them to named owners with escalation into the post-market monitoring plan and corrective actions.
- Derive thresholds from predefined, intended-purpose-appropriate metrics, document them in the risk file, and version-control changes.
- Specify bias metrics and groups, add data-gap alerts, and link alerts to bias mitigation procedures.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 20 Corrective actions and duty of information (art:20); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 17 Quality management system (art:17)

**Analysis:** NFR-6 provides a rollback control for models that fail safety, robustness or fairness checks, but it does not define who decides, what triggers rollback, how the rollback is verified, or how it connects to corrective-action duties. Without these, rollback may be applied inconsistently and may not support provider obligations to correct non-conforming systems.

**Risks:**

- Rollback is not tied to defined triggers, acceptance thresholds or an approval/authority procedure; NFR-5 raises alerts but nothing links alerts to a rollback decision, and 'previously approved' is undefined. [medium] - Article 17(1)(a) (`art:17:p1:a`)
  - Category: `quality_management`
  - Action: Document a model change/rollback procedure covering approval criteria for rollback targets, trigger thresholds linked to NFR-5 alerts, decision authority, and versioned records of approved models.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(b))
- Requirement does not state that the rolled-back model is re-tested against predefined metrics and thresholds, nor that the rollback target still meets robustness and fairness criteria before redeployment. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Require automated validation of the rollback target against predefined safety, robustness and fairness thresholds before reactivation, and log the results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Rollback is not linked to corrective-action and information duties: no process to notify deployers or downstream parties, or to escalate to authorities when a failed check indicates a risk, and no fallback (disable/withdraw) if no approved prior version is available. [medium] - Article 20(1) (`art:20:p1`)
  - Category: `corrective_actions`
  - Action: Define rollback as a corrective-action workflow with deployer notification, an incident/escalation path, and a disable or fail-safe mode when no conforming prior version exists.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 20 Corrective actions and duty of information
    - requirement term 'rollback' is an instance of the defined term 'recall of an AI system' (Article 3(16)), which Article 20 uses
- The requirement does not specify fail-safe behaviour during rollback or protect model version storage and rollback operations against tampering, such as model poisoning or unauthorised version swaps. [low] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add integrity-protected model registry with signed artifacts, access-controlled rollback operations, audit logging, and defined fail-safe behaviour during rollback.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Quality management system, Article 17(1)(a)**
  > (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system;
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

**Recommendations:**

- Document rollback triggers, approval criteria and decision authority, linked to NFR-5 alerts.
- Validate rollback targets against predefined safety, robustness and fairness thresholds before redeployment.
- Integrate rollback into corrective-action workflows with deployer notification, escalation and a disable fallback.
- Secure the model registry and rollback operations with signing, access control and audit logging.

---
