# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 14

### Overall analysis

Overall, the assessment reviewed 16 requirements and identified 2 high-risk findings, 14 medium-risk findings. The main review focus areas are transparency, data governance, human oversight, record keeping, risk management. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 2 high, 14 medium, 0 low.
- Most frequent mapped obligation areas: transparency (11), data governance (9), human oversight (6), record keeping (6), risk management (6).

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

**Analysis:** FR-1 defines ingestion of resumes, cover letters and application form responses for a recruitment AI system (Annex III 4(a)) but states no input-data governance (provenance, quality, bias examination) and no event logging for ingestion. This could let unrepresentative or biased input data, and untraceable ingestion events, flow into scoring and ranking (FR-2, FR-3).

**Risks:**

- FR-1 has no data governance requirements for ingested application data (origin and original purpose of personal data, preparation operations such as parsing and cleaning, assumptions about what the data represent, bias examination of free-text and form fields). Any reuse of ingested data for validation, testing or retraining is also ungoverned. [medium] - Article 10(2) (`art:10:p2`)
  - Category: `data_governance`
  - Action: Document data provenance, parsing and cleaning steps, and assumptions for each ingested field. Add a bias examination of ingested data, including form fields and cover letter text, as proxies for protected attributes. Define whether ingested applications are reused for training, validation or testing.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No requirement ensures that ingested data is relevant, sufficiently representative and as error-free as possible, for example by handling parsing failures, incomplete submissions or varied resume formats and languages that could disadvantage groups of candidates. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Add input validation and parsing-quality metrics. Test ingestion accuracy across formats, languages and candidate groups. Flag and route unparseable or incomplete applications for manual handling instead of silently scoring them.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- FR-1 does not require automatic logging of ingestion events (what was received, when, and in which version of the pipeline). This limits traceability and post-market monitoring of the system's input data. [low] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Log ingestion events with timestamp, application ID, input-source type, parsing outcome and pipeline version. Set retention to at least six months, in line with Art. 26(6) and data-protection law. Protect the logs under the NFR-4 access controls.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Document the provenance, preparation and bias examination of ingested application data, and its reuse for training or testing.
- Add input validation and parsing-quality checks, and test them across formats, languages and candidate groups.
- Log ingestion events with a defined retention period (at least six months, subject to data-protection law).

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 6 Classification rules for high-risk AI systems (art:6); Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-2 scores candidates in a recruitment system classified as high-risk under Annex III 4(a), but it does not specify data quality and representativeness, explainability of the score, or risk analysis for score-driven bias. Human override (FR-6), review channel (FR-10) and access control (NFR-4) exist, so the remaining gaps are in the scoring logic itself.

**Risks:**

- The score is derived from extracted experience, education and skills, but the requirement does not say that training, validation and testing data are representative, error-free and statistically appropriate for the applicant groups, so the score could be biased or inaccurate. [high] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Define dataset validation for representativeness and error rates across applicant groups. Test the extraction and scoring outputs for subgroup performance disparities, and document the results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'application' is an instance of the defined term 'personal data' (Article 3(50)), which Article 10 uses
- The requirement does not say how the score is made interpretable (for example, per-factor contributions or accuracy metrics and limitations), so deployers and recruiters may be unable to interpret and use it appropriately. NFR-4 covers access to explanations but not their content. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Add a requirement that each score comes with the contributing factors and a confidence or accuracy indication. Document the score's limitations and performance metrics in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- Risks from scoring (discrimination, proxy variables in education or experience, misuse as an automatic filter) are not tied to a risk management process, and the requirement does not cover foreseeable misuse. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Add scoring-specific fundamental-rights risks to the risk register. Include foreseeable misuse such as reliance on the score alone, and set up post-market monitoring of score outcomes.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Define dataset validation and subgroup bias testing for the scoring model and the extraction of experience, education and skills.
- Make score explanations specific (factors, metrics, limitations) and include them in the instructions for use.
- Add scoring-related risks and foreseeable misuse to the risk management process, with ongoing monitoring of outcomes.

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 10 Data and data governance (art:10); Article 6 Classification rules for high-risk AI systems (art:6)

**Analysis:** FR-3 ranks candidates in a high-risk recruitment system (Annex III 4(a)). Human review (FR-6) and explanations (FR-4) exist, but the requirement does not define rank-presentation transparency, recruiter competence/training, or bias examination of the ranking. Without these, ranking can steer recruiters or discriminate, and recruiters may not be able to interpret it.

**Risks:**

- Ranking output has no specified transparency such as score meaning, accuracy limits, or uncertainty. FR-4 explains factors but does not say recruiters see rank-level limitations or confidence, so rank order could be over-trusted. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Show score meaning, known limitations and confidence or ties alongside the ranking. Document these in the instructions for use, including performance across groups where appropriate.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- FR-6 gives recruiters override ability but does not assign oversight to staff with defined competence, training and authority, nor guard against automation bias from a ranked list (e.g. only top-N reviewed). [medium] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Define reviewer roles and training requirements. Require review of candidates below the cut-off, or sampled review, and log override rates to detect automation bias.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- Ranking built on the suitability score is not tied to bias examination or mitigation, so systematic disadvantage to protected groups could pass into the rank order. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add bias testing of ranking outcomes across protected groups on validation and testing data. Define mitigation thresholds and re-test on model or data changes.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- The requirement does not link ranking-specific risks (e.g. systematic exclusion of lower-ranked candidates, misuse as an automatic filter) to the risk management process. [low] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Add ranking-related risks, including foreseeable misuse as auto-rejection, to the risk register. Monitor ranking outcomes post-deployment.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Display score meaning, limitations and confidence with rankings, and document them in the instructions for use.
- Define reviewer competence and training, and require review beyond top-ranked candidates with override-rate logging.
- Test ranking outcomes for bias across protected groups and define mitigation thresholds.
- Add ranking-specific risks and misuse scenarios to the risk management file and post-market monitoring.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-4 gives recruiters per-score explanations, which supports Art. 13 transparency. It leaves open whether the explanation is faithful and limited in a documented way, and whether it reaches affected candidates. Candidate-facing explanations of the AI's role are a deployer obligation under Art. 86 and are only partly addressed by FR-10.

**Risks:**

- FR-4 does not require the explanation to be faithful to the actual model drivers, nor to state its limitations (accuracy, confidence, known failure conditions). Recruiters could over-trust a plausible but unfaithful explanation, and the instructions for use do not yet have to document the explanation capability. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Define explanation fidelity tests and show confidence and limitations alongside each explanation. Document the explanation capabilities and their limits in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- Explanations are recruiter-facing only (NFR-4 restricts access to recruitment staff), and FR-10 covers review requests but not an explanation of the AI's role and the main elements of the decision. Affected candidates may therefore lack the clear, meaningful explanation Art. 86 requires from the deployer. [medium] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Add a function that exports a candidate-appropriate explanation of the AI's role and the main decision factors, so deployers can answer Art. 86 requests. Clarify in FR-10 or a new requirement how it is delivered.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Add explanation fidelity validation, confidence and limitation display, and matching instructions-for-use content.
- Provide a deployer-releasable, candidate-readable explanation of the AI's role and main decision factors to support Art. 86 requests.

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-5 notifies recruiters that a ranking is automated, but does not say what the notice contains, such as model limitations, confidence or interpretation guidance, or an automation-bias warning. Recruiters may over-rely on rankings, and workers and candidates are not covered by this requirement.

**Risks:**

- The notification only flags that a ranking is model-generated. It does not give recruiters the information needed to interpret the output, such as accuracy limits, known circumstances affecting performance, or explanation hints, so the transparency is thin. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Extend the notice to link to the instructions for use, show output interpretation guidance and known limitations (Art. 13(3)(b)), and show the explanation or score drivers where available. FR-7 already logs explanations, so reuse them.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- The notification does not warn against automatic over-reliance on the ranking (automation bias). FR-6 provides override and review, but nothing in FR-5 helps recruiters stay aware of the tendency to over-rely on the output or know when to disregard it. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Category: `human_oversight`
  - Action: Add automation-bias messaging and a prompt in the notification pointing to the FR-6 review and override actions. Add reviewer guidance on interpreting and disregarding rankings.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))
- The requirement notifies recruiters only. It does not cover informing workers or candidates affected by the high-risk recruitment system. FR-10 provides a review channel, but no requirement explains the AI system's role in a decision, so the deployer-side duty to inform affected persons and give explanations is unaddressed. [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Clarify whether candidate-facing disclosure is handled elsewhere. Add a deployer-facing function that produces a clear explanation of the AI's role and the main elements of the decision, based on the FR-7 logs, for candidate requests under FR-10.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Enrich the recruiter notification with interpretation guidance, limitations and a link to the instructions for use.
- Add an automation-bias warning and a pointer to the FR-6 override workflow.
- Define candidate-facing explanation support, using the FR-7 logs, for requests made through FR-10.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13); Article 6 Classification rules for high-risk AI systems (art:6)

**Analysis:** FR-6 provides a recruiter review/override/reject control before candidate removal, which largely meets Art. 14(4)(d). Remaining gaps are limited to supporting measures: automation-bias awareness, reviewer competence and authority, and explanation support. These are not addressed by FR-6 or the related requirements.

**Risks:**

- FR-6 gives an override capability but does not require measures that make recruiters aware of automation bias or able to interpret ranking outputs and limitations, so reviews may become rubber-stamping. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Category: `human_oversight`
  - Action: Show score rationale, confidence and known limitations in the review UI. Add automation-bias warnings, and require a recorded reason when a recruiter confirms a rejection without independent review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- FR-6 does not specify that reviewers must have the competence, training and authority to override rankings, or that overrides are not discouraged. NFR-4 covers access control only. [medium] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Define reviewer roles with explicit override authority. Provide training material and deployer guidance, and add role-based permissions that make override available to all assigned reviewers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- FR-6 does not require recording the recruiter's review outcome or override reason. Without this record, the deployer cannot give affected candidates a meaningful explanation of the AI's role in a decision. FR-10 provides a review channel but not the decision-level explanation data. [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Log the ranking, reviewer, decision and override rationale per candidate. Make this data available to support explanations requested through the FR-10 channel.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Add output interpretation aids and automation-bias safeguards to the review workflow.
- Define reviewer roles with competence, training and override authority, and document them in deployer guidance.
- Capture review outcomes and override reasons so deployers can explain the AI's role in a decision.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-7 covers the main event types (scores, rankings, explanations, overrides, decisions) but does not specify log retention, log integrity, or the traceability metadata needed to support monitoring and incident investigation. Without retention and integrity controls, the logs may be unusable or deleted before they support oversight, post-market monitoring, or explanation requests.

**Risks:**

- No retention period is specified for the logs. Providers and deployers must keep automatically generated logs for a period appropriate to the intended purpose, and for at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Add a retention requirement of at least six months, or longer where the recruitment purpose or data protection law requires it. Add configurable retention and deletion rules, and keep them consistent with GDPR data minimisation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The requirement lists what is logged but not the lifetime-wide automatic capture of events (e.g. model version, input reference, timestamps, user identity). It also has no tamper-evidence or integrity protection, which limits traceability of the system's operation. [medium] - Article 12(1) (`art:12:p1`)
  - Category: `record_keeping`
  - Action: Specify that logging is automatic and runs over the system lifetime. Include model/version ID, input data reference, timestamp, and actor ID in each log entry. Use append-only or tamper-evident storage, with access limited as in NFR-4.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Recruiter overrides are logged, but the requirement does not capture override rationale or reviewer identity, or link entries to the explanation shown. This weakens the ability to monitor operation and to give affected candidates a meaningful explanation of the AI system's role in a decision. [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Record the reviewer ID, override reason, and the exact score and explanation version presented. Provide a retrieval function so the deployer can reconstruct the role of the AI system in an individual decision.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Define a log retention period of at least six months, with documented retention and deletion rules aligned with data protection law.
- Specify automatic lifetime logging with model version, input reference, timestamp and actor ID, stored in tamper-evident form.
- Capture override rationale, reviewer identity and the presented explanation version so individual decisions can be explained and reconstructed.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 11 Technical documentation (art:11)

**Analysis:** FR-8 already provides audit records covering input data, model version, and human actions, so the main gaps are retention duration and whether the logs capture risk and post-market monitoring events. Without a defined retention period, the logs may not meet the minimum six-month requirement.

**Risks:**

- FR-8 specifies no retention period for audit records; Articles 19(1) and 26(6) require logs to be kept for a period appropriate to the intended purpose and for at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Define a log retention policy of at least six months (longer if the intended purpose requires it), enforce it technically, and reconcile it with data-protection deletion limits for candidate data.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- FR-8 covers tracing individual decisions but does not state that logging captures events relevant to identifying risk or substantial modification situations, supporting post-market monitoring, or deployer monitoring of operation. [medium] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Extend the logging spec to record events such as model version changes, anomalous or low-confidence scores, overrides, and error conditions, and make them queryable for post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))
- FR-8 does not state that deployers get a mechanism or documentation to collect, store, and interpret the logs, so log access for deployers is unclear. [low] - Article 13(3)(f) (`art:13:p3:f`)
  - Category: `transparency`
  - Action: Document the log schema and provide export or query tooling for deployers in the instructions for use. Restrict access consistently with NFR-4.
  - Trace:
    - requirement term 'input data' is an instance of the defined term 'input data' (Article 3(33)), which Article 13 uses

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Transparency and provision of information to deployers, Article 13(3)(f)**
  > (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.

**Recommendations:**

- Define and enforce a log retention period of at least six months, aligned with data-protection law.
- Extend logging to cover risk-relevant, modification and monitoring events, not only per-decision traces.
- Document the log format and provide deployer access or export tooling in the instructions for use.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 9 Risk management system (art:9)

**Analysis:** FR-9 is a control that blocks facial recognition, biometric identification and emotion recognition in candidate screening, which supports Article 5(1)(f) avoidance. Remaining gaps are that the requirement does not say how the block is implemented or verified, and it does not cover foreseeable misuse or biometric categorisation.

**Risks:**

- FR-9 does not name biometric categorisation (inferring race, beliefs, sexual orientation, etc. from biometric data), which Article 5(1)(g) prohibits. The prevention scope could miss it. [medium] - Article 5(1)(g) (`art:5:p1:g`)
  - Category: `prohibited_practices`
  - Action: Extend FR-9 to block biometric categorisation. Add a technical control that rejects or ignores image, video or audio-derived biometric inputs in the screening pipeline.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
- FR-9 gives no mechanism or verification for 'prevent' (e.g. input filtering, feature exclusion, or blocking via configuration). Emotion or biometric inference could still enter through video interviews, photos in resumes, or voice. This is a risk of foreseeable misuse that has not been assessed. [medium] - Article 9(2)(b) (`art:9:p2:b`)
  - Category: `risk_management`
  - Action: Record the biometric and emotion inference misuse scenarios in the risk register. Specify the preventive mechanism, such as stripping photos and rejecting audio or video, and who can change it.
  - Trace:
    - referenced by Article 9(5) (Article 9(2))
- No test acceptance criteria show that the prohibited capabilities are absent or cannot be enabled, so the control may be unverified before the system is put into service. [low] - Article 9(8) (`art:9:p8`)
  - Category: `testing`
  - Action: Add tests that submit images, video and audio and confirm no biometric or emotion features are extracted. Add a regression check in CI and a release gate.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Risk management system, Article 9(2)(b)**
  > (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse;
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.

**Recommendations:**

- Extend FR-9 to cover biometric categorisation and inference of sensitive attributes from biometric data.
- Document the biometric and emotion misuse scenarios and the chosen technical block in the risk management file.
- Add verifiable tests and a release gate proving that biometric and emotion processing cannot occur or be enabled.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 85 Right to lodge a complaint with a market surveillance authority (art:85)

**Analysis:** FR-10 gives candidates a review channel but does not state that candidates can obtain a clear, meaningful explanation of the AI's role and the main elements of the decision. It also does not say who handles the review or how, so the channel could be a formality without real recourse.

**Risks:**

- The requirement covers requesting review but not delivering a clear and meaningful explanation of the AI system's role in the decision and the main elements of the decision. NFR-4 restricts model explanations to recruitment staff, so candidates may never receive them. [high] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Add a requirement to give candidates, on request, a plain-language explanation of the ranking's role and the main factors behind the decision. Add a candidate-facing path that does not conflict with NFR-4's staff-only access, and set a response time.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- The requirement does not say who handles review requests, or that reviewers have the competence, training and authority to override the automated ranking. FR-6 covers recruiter override before a candidate is removed, but not the handling of candidate-initiated reviews. [medium] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Route review requests to a named, trained reviewer who is independent of the original decision and has authority to reverse it, using the FR-6 override mechanism. Record the outcome in the FR-8 audit records.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Add a candidate-facing explanation of the AI's role and the main decision elements, delivered through the review channel, with a defined response time.
- Assign review requests to a trained, authorised reviewer who can override the ranking, and log each request and outcome in the FR-8 audit trail.

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 11 Technical documentation (art:11)

**Analysis:** NFR-1 already provides a data-quality control (missing values, duplicates, inconsistent labels) for training and evaluation data. It does not cover bias examination, representativeness, or documentation of data governance, which matter for a recruitment ranking system.

**Risks:**

- Validation covers only completeness, duplicates and label consistency; it does not require examination for biases likely to cause discrimination (e.g., by gender, age, ethnicity in recruitment data) or measures to detect and mitigate them. NFR-5 monitors bias metrics at runtime but does not address pre-training dataset bias. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add a pre-training dataset bias examination step (distribution and label-outcome analysis across protected groups) with documented mitigation actions and pass/fail criteria.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement does not check that datasets are relevant, sufficiently representative, or have appropriate statistical properties for the groups of candidates the system will be used on. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Add representativeness and statistical-property checks against the target candidate population, and block training when thresholds are not met.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'training dataset' is an instance of the defined term 'training data' (Article 3(29)), which Article 10 uses
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- The requirement does not say that validation rules, thresholds, results and remediation of identified data gaps are recorded as part of data-management procedures in the quality management system or technical documentation. [low] - Article 17(1)(f) (`art:17:p1:f`)
  - Category: `quality_management`
  - Action: Persist validation reports per dataset version (checks run, thresholds, failures, remediation) and link them to QMS data-management procedures and technical documentation.
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

- Add a pre-training bias examination and mitigation step with documented criteria.
- Add representativeness and statistical-property checks against the intended candidate population.
- Retain versioned validation reports as QMS and technical documentation evidence.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** NFR-2 already provides disaggregated performance measurement, a bias-evaluation control. The remaining gaps are that it is conditional on data availability with no fallback, and that nothing ties its results to declared accuracy metrics in the instructions for use.

**Risks:**

- Group-level evaluation applies only where lawful demographic data is available. There is no fallback (e.g. proxy or synthetic evaluation, documented data-gap handling) when it is unavailable, so bias examination and data-gap identification may go undone for some groups. [medium] - Article 10(2)(h) (`art:10:p2:h`)
  - Category: `data_governance`
  - Action: Document which groups lack lawful evaluation data. Define a fallback bias-assessment method and a data-gap remediation plan, and record both in the data governance documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- The requirement does not say that disaggregated results are reported in the instructions for use (performance regarding specific groups, accuracy metrics). Deployers may not learn about group-level performance limitations. [medium] - Article 13(3) (`art:13:p3`)
  - Category: `transparency`
  - Action: Include per-group metrics, the evaluation method and known limitations in the instructions for use and the technical documentation. Refresh them when the model is re-evaluated.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(b))
- The requirement does not specify the metrics, the group definitions or the acceptance thresholds that count as appropriate and consistent accuracy. NFR-5 alerts on thresholds, but it is unclear whether they are derived from these per-group measurements. [low] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness`
  - Action: Define per-group metrics and acceptable disparity thresholds. Link them to the NFR-5 monitoring alerts and the NFR-6 rollback criteria, and run the evaluation at each release and periodically in production.
  - Trace:
    - referenced by Article 15(2) (Article 15(1))

**Cited provisions:**

- **Data and data governance, Article 10(2)(h)**
  > (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Define a fallback bias-evaluation approach and document data gaps where lawful demographic data is unavailable.
- Report per-group performance and its limitations in the instructions for use.
- Specify per-group metrics and thresholds, and wire them into NFR-5 alerts and NFR-6 rollback.

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 9 Risk management system (art:9); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14)

**Analysis:** NFR-3 excludes protected attributes as direct ranking inputs, which is a useful control. It does not address proxy variables (e.g. names, postcodes, education or employment gaps inferred from resumes) or require bias testing, so indirect discrimination in ranking could go undetected.

**Risks:**

- Excluding protected attributes as explicit inputs does not cover proxy features extracted from resumes and cover letters (FR-1, FR-2) that can correlate with race, religion, disability or political opinion, and the requirement has no bias examination or mitigation step. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add a proxy-feature audit and bias testing of training, validation and test data and ranking outputs across protected groups. Define mitigation and acceptance thresholds.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No requirement ensures that data sets are sufficiently representative with appropriate statistical properties for the groups of candidates the ranking will be applied to, so exclusion of protected attributes could mask unequal performance across groups. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Document data set representativeness and per-group performance metrics. Where lawful, use a restricted-access fairness-evaluation data set to measure disparities without feeding the ranking model.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Discrimination against candidates with protected characteristics is a foreseeable fundamental-rights risk, but the requirement does not tie the exclusion to a risk-management process with ongoing monitoring of residual discriminatory impact after deployment. [low] - Article 9(2)(a) (`art:9:p2:a`)
  - Category: `risk_management`
  - Action: Record discriminatory ranking as an identified risk, with a control to verify NFR-3 (feature-exclusion checks, disparity monitoring in production) and review triggers.
  - Trace:
    - referenced by Article 9(5) (Article 9(2))

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;

**Recommendations:**

- Audit for proxy features and run bias tests on data and ranking outputs across protected groups.
- Document representativeness of data sets and measure per-group performance.
- Register discrimination as a risk in the risk management file and monitor disparity metrics after deployment.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10); Article 12 Record-keeping (art:12)

**Analysis:** NFR-4 states a role-based access restriction but gives no detail on how it resists unauthorised access or manipulation, nor on whether access to the data and explanations is itself logged. The remaining gap is cybersecurity hardening and access monitoring, not the absence of access control.

**Risks:**

- The requirement says only 'authorised recruitment staff' may view data and explanations. It does not specify authentication strength, role definitions, least-privilege scoping, or protection against confidentiality attacks and unauthorised alteration of outputs, so resilience against unauthorised third parties is not demonstrated. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `cybersecurity`
  - Action: Define roles and least-privilege permissions, require MFA and session controls, encrypt candidate data and explanations, and add threat-model and penetration tests for confidentiality and unauthorised-access attacks.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- FR-7 logs scores, explanations, overrides and decisions, but NFR-4 does not require access events (who viewed or exported candidate data and explanations) to be recorded and retained. Unauthorised access would therefore go undetected and could not be traced during deployer monitoring. [low] - Article 26(6) (`art:26:p6`)
  - Category: `record_keeping`
  - Action: Extend FR-7 logging to access, view and export events on candidate data and explanations, and retain these logs for at least six months, subject to data protection law.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.

**Recommendations:**

- Specify authentication, role-based least-privilege, encryption and attack-resistance measures for access to candidate data and explanations, and test them.
- Log all access to candidate data and explanations alongside the FR-7 logs and retain them for at least six months, subject to data protection law.

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14)

**Analysis:** NFR-5 provides threshold-based alerting but does not define alert routing, documented response/escalation, or how monitoring data feeds the post-market monitoring and risk management processes. Alerts without a defined response path or lifecycle data retention may not support continuous compliance evaluation.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system that systematically collects, retains and analyses performance data over the system's lifetime (including deployer-provided data) to evaluate continuous compliance. [medium] - Article 72(2) (`art:72:p2`)
  - Category: `post_market_monitoring`
  - Action: Persist alert and metric history, link it to a documented post-market monitoring plan, and define data intake from deployers and periodic compliance review.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- No requirement states that threshold breaches trigger risk-management review, corrective action or model updates, nor that thresholds are predefined and appropriate to the intended purpose. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Define threshold-setting rationale, alert severity levels, owners and an escalation workflow that feeds risk register updates; link to rollback (NFR-6).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system (closest match: Article 9(2)(c))
- Alert recipients and their ability to interpret alerts and act (investigate, override, halt) are unspecified, so monitoring may not enable overseers to detect anomalies and dysfunctions. [low] - Article 14(4)(a) (`art:14:p4:a`)
  - Category: `human_oversight`
  - Action: Specify alert recipients, include context and metric explanations in alerts, and document the response procedure including the ability to suspend the model.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).
- **Human oversight, Article 14(4)(a)**
  > (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance;

**Recommendations:**

- Persist alert and metric history and link it to a documented post-market monitoring plan.
- Document threshold rationale and an escalation workflow that feeds risk management updates and rollback (NFR-6).
- Define alert recipients, alert content and response procedures enabling intervention or halting.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 20 Corrective actions and duty of information (art:20); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 17 Quality management system (art:17)

**Analysis:** NFR-6 provides a rollback control for failed models, which supports Article 15(4) fail-safe resilience and Article 20 corrective action. Remaining gaps: it does not define who approves or triggers a rollback, and it lacks the downstream steps of escalation, notification and documentation.

**Risks:**

- Rollback is not linked to the corrective-action duty: no requirement to notify distributors/deployers or to investigate and escalate to authorities when a failed model signals non-conformity or risk. [medium] - Article 20(1) (`art:20:p1`)
  - Category: `corrective_actions`
  - Action: Add a rollback workflow step that records the trigger, notifies deployers/distributors, and escalates to the compliance owner to assess Article 20(2) and Article 73 reporting.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 20 Corrective actions and duty of information
- The pass/fail criteria for 'safety, robustness, or fairness checks' and the rollback trigger are undefined. NFR-5 alerts on thresholds but does not say they trigger rollback, and NFR-6 does not link the two. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Define metrics and thresholds for the safety, robustness and fairness checks. Link the NFR-5 alerts and NFR-2 group metrics to rollback decision criteria, and record them in the risk management file.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Rollback to a 'previously approved' version has no specified approval governance, version registry, or revalidation of the restored model. The prior version may itself have known robustness or bias issues or be vulnerable to tampering. [medium] - Article 17(1)(a) (`art:17:p1:a`)
  - Category: `quality_management`
  - Action: Maintain a signed, versioned registry of approved models with approval records. Require integrity verification and a smoke test of the restored version, and document the rollback as a change-management procedure.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(b))
- Rollback events are not fed into post-market monitoring, so the failures that caused them may not be analysed for continuous compliance. [low] - Article 72(2) (`art:72:p2`)
  - Category: `post_market_monitoring`
  - Action: Log each rollback with its cause and metrics, and feed these records into the post-market monitoring plan and periodic risk review.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems

**Cited provisions:**

- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Quality management system, Article 17(1)(a)**
  > (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system;
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.

**Recommendations:**

- Tie rollback to the corrective-action process: notify deployers and escalate to the compliance owner.
- Define quantitative rollback triggers and connect them to the NFR-5 alerts and NFR-2 fairness metrics.
- Add a version registry with approval records and integrity and revalidation checks on the restored model.
- Feed rollback events and root causes into post-market monitoring and risk management reviews.

---
