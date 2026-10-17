# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 5
- Medium: 11

### Overall analysis

Overall, the assessment reviewed 16 requirements and rated 5 as high risk and 11 as medium risk. The main review focus areas are data governance, accuracy robustness cybersecurity, transparency, human oversight and record keeping. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 5 high, 11 medium, 0 low.
- Most frequent mapped obligation areas: data governance (10), accuracy robustness cybersecurity (9), transparency (8), human oversight (7), record keeping (5).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12)

**Analysis:** FR-1 ingests untrusted, free-form candidate documents with no input validation, integrity or malicious-content controls, and no stated input-data quality or relevance criteria. This leaves a robustness/cybersecurity gap and a gap in input-data governance for a high-risk recruitment system.

**Risks:**

- Candidate-submitted resumes, cover letters and form responses are ingested with no stated integrity or sanitisation controls against malformed files, manipulated content or adversarial inputs (e.g. hidden text or prompt injection) that could alter scores. [high] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: NFR-5 (detecting data quality deviations after the fact (partial 15(4) resilience, not input attack prevention))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add input validation: file type/size limits, malware scanning, text normalisation, and detection of hidden or adversarial content, with quarantine and logging of rejected inputs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No requirement defines handling of erroneous, incomplete or inconsistent application data at ingestion (parsing failures, missing fields, unsupported formats), so errors may silently distort scores. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify ingestion error handling: parse-confidence checks, flagging incomplete applications for human review, and fail-safe behaviour instead of scoring on corrupted data.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Ingested application data is not constrained to what is relevant and representative for the intended purpose; free-text and form responses may carry protected-attribute information or proxies into the pipeline, and data origin and format assumptions are undocumented. [medium] - Article 10(2) (`art:10:p2`)
  - Partly addressed by: NFR-3 (excluding protected attributes as ranking inputs (bias prevention under 10(2)(g))); NFR-1 (validating training and evaluation datasets for quality (10(3) errors/completeness), though not live ingested inputs)
  - Category: `data_governance`
  - Action: Define the permitted input fields and data-collection assumptions, document data origin and preparation steps, and filter or redact fields irrelevant to job suitability before scoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Candidates are not told at ingestion (the portal submission point) that their application will be processed by a high-risk AI system; no requirement covers this notice. [medium] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-10 (candidate review channel only; does not inform candidates of AI use); FR-5 (notifies recruiters, not candidates)
  - Category: `transparency`
  - Action: Show a notice in the portal at submission that AI-assisted screening and ranking is used, and link to the review-request channel.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Add input validation, sanitisation and adversarial-content detection to ingestion.
- Define ingestion error handling and route incomplete or unparsable applications to human review.
- Specify permitted input fields, document data origin and preparation, and filter irrelevant or sensitive content.
- Add a candidate-facing notice in the portal that AI-assisted screening is used.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9)

**Analysis:** FR-2 generates a suitability score for candidates but declares no accuracy metrics or acceptance thresholds, and does not constrain the scoring model to relevant, job-related features or require bias examination of the training data. Without these, scores that drive recruitment decisions could be unreliable or discriminatory, and the system could not be shown to meet Art. 15 or Art. 10.

**Risks:**

- No accuracy level or metrics are defined for the suitability score, so it cannot be tested against prior-defined thresholds or declared in the instructions for use. [high] - Article 15(3) (`art:15:p3`)
  - Partly addressed by: NFR-5 (monitoring of model accuracy against configured thresholds after deployment); NFR-2 (measuring performance separately across demographic groups)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics and minimum acceptance thresholds for the scoring model (e.g. ranking agreement with expert assessments, per-group error rates). Test against them before release and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Scoring based on experience, education and skills extracted from applications has no stated data-governance basis (relevance of features, representativeness of training data, bias examination and mitigation, and extraction errors). [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: NFR-1 (dataset checks for missing values, duplicates and inconsistent labels (10(3) error-freeness and completeness)); NFR-3 (exclusion of protected attributes as ranking inputs); NFR-2 (measuring performance across demographic groups (detection of bias))
  - Category: `data_governance`
  - Action: Document the feature design choices and the assumptions about what each feature represents. Examine education and experience proxies for bias, apply mitigation, and check the accuracy of extracted attributes on a labelled sample.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement does not state that scoring must stay consistent and resilient to errors in extracted application data or to manipulated inputs (e.g. keyword stuffing in resumes). [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: NFR-6 (rollback to an approved model version when robustness checks fail)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add robustness requirements and tests for malformed, adversarial or manipulated application content, and for extraction failures, with a fallback to manual review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define and test accuracy metrics and thresholds for the suitability score, and declare them in the instructions for use.
- Document feature design and bias examination for the scoring inputs, and validate the accuracy of extracted attributes.
- Add robustness and adversarial-input requirements and tests for score generation, with a manual-review fallback.

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10)

**Analysis:** FR-3 ranks candidates from the suitability score. Human review, explanation, notification and logging are covered by FR-4, FR-5, FR-6 and FR-7. What remains is that FR-3 itself does not say how the ranking is presented to limit automation bias, and that the accuracy of the ranking is not declared for deployers.

**Risks:**

- The ranking is presented without any stated safeguards against automation bias, such as showing the score as advisory, displaying confidence or uncertainty, or avoiding a hard cut-off. Recruiters may over-rely on the rank order. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-6 (recruiter can review, override or reject the automated ranking (14(4)(d))); FR-5 (recruiters are told the ranking is model-generated, which supports awareness of its automated origin)
  - Category: `human_oversight`
  - Action: Specify that the ranking interface shows the score as advisory, with uncertainty or confidence indicators and no automatic exclusion. Add recruiter guidance on automation bias.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No accuracy or ranking-quality metrics are declared for the ranking function in the instructions for use. Deployers cannot tell how reliable the ranking is. [medium] - Article 15(3) (`art:15:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: NFR-5 (monitoring alerts when accuracy falls outside configured thresholds (15(1) consistent performance)); NFR-2 (performance measured across demographic groups)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define ranking-quality metrics (e.g. NDCG, rank correlation with expert judgement) and target thresholds. Declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Add automation-bias safeguards to the ranking presentation: advisory labelling, uncertainty display and no automatic cut-off.
- Declare ranking accuracy metrics and expected levels in the instructions for use.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 11 Technical documentation (art:11)

**Analysis:** FR-4 gives recruiters per-candidate factor explanations, which supports output interpretation. It does not cover explanation limits (accuracy, known limitations), the documentation of explanation capabilities for deployers, or explanations for affected candidates.

**Risks:**

- FR-4 does not require the explanation to state its own limits (e.g. confidence, fidelity of the factor attribution, or known circumstances that reduce reliability), so recruiters may over-rely on it (automation bias). [medium] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-6 (ability to disregard, override or reject the ranking (14(4)(d))); FR-5 (recruiters are made aware that the ranking is model-generated (partly 14(4)(b)))
  - Category: `human_oversight`
  - Action: Extend FR-4 so each explanation includes score confidence or uncertainty, a note on the explanation method's limits, and an automation-bias caution. Document the interpretation guidance for recruiters.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))
- The explanation capability and its characteristics (what factors are shown, how derived, limitations) are not required to be described in the instructions for use, so deployers cannot interpret outputs appropriately. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a documentation requirement: the instructions for use describe the explanation feature, its technical characteristics and limits, accuracy metrics, and guidance for interpreting scores.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- FR-4 only targets recruiters. Nothing ensures the deployer can give affected candidates a clear, meaningful explanation of the AI system's role in a decision and the main elements of that decision. [medium] - Article 86(1) (`art:86:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-10 (channel for candidates to request review of decisions influenced by automated ranking); FR-7 (explanations are logged, so they can be retrieved later)
  - Category: `transparency`
  - Action: Define an exportable, candidate-appropriate explanation of the system's role and the main decision elements, which the deployer can provide on request, e.g. via the FR-10 review channel.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Extend FR-4 so explanations include confidence, method limits, and an over-reliance caution.
- Document the explanation capabilities, limits, and interpretation guidance in the instructions for use.
- Provide a candidate-facing explanation of the AI system's role and the main decision elements, linked to the FR-10 review channel.

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-5 tells recruiters that a ranking is model-generated, which supports deployer-side interpretation and automation-bias awareness. It does not notify the affected candidates that a high-risk system is used in decisions about them. It also does not indicate the model's limitations or how far the output can be relied on.

**Risks:**

- FR-5 notifies only recruiters. Nothing in the SRS informs candidates that they are subject to a high-risk AI system used to assist decisions about them. FR-10 only offers a review channel after a decision has been made. [high] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a requirement to inform candidates, clearly and at or before application or screening, that an automated ranking model assists in assessing them. Keep a record that the notice was delivered.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The recruiter notice only flags that a model produced the ranking. It does not state the model's limitations, expected accuracy, or the need to verify the output. This weakens the recruiter's awareness of automation bias and ability to interpret the output. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-4 (explains the main factors behind each score, supporting correct interpretation of the output (14(4)(c))); FR-6 (lets the recruiter review, override or reject the ranking (14(4)(d)))
  - Category: `human_oversight`
  - Action: Extend the notification to say the ranking is advisory and link it to documented performance limitations. Add an automation-bias warning in the recruiter UI, shown with the score explanation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))
- The requirement does not say when or where the notice appears or how it is kept. It is unclear whether every ranking view is flagged and whether the flag is logged, which weakens evidence that recruiters were told the output is model-generated. [low] - Article 13(1) (`art:13:p1`)
  - Partly addressed by: FR-7 (logs model-generated rankings and explanations, which could carry the notification record (13(3)(f)))
  - Category: `transparency`
  - Action: State that the notification is persistent on every ranking view and export, and record its display in the audit log.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add a requirement to notify candidates that an automated ranking model is used in assessing them, and log delivery.
- Extend the recruiter notification with an advisory and limitations statement and an automation-bias warning.
- Make the recruiter notification persistent on all ranking views and exports, and log its display.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 12 Record-keeping (art:12); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-6 provides review/override/reject before candidate removal, which substantially covers Art 14(4)(d). Remaining gaps are minor: no automation-bias safeguards or qualification requirements for the reviewing recruiter, and no stop/interrupt capability.

**Risks:**

- FR-6 lets recruiters override rankings but does not require measures that make reviewers aware of automation bias or ensure the review is meaningful rather than rubber-stamping; for example, it does not require a recorded reviewer decision or a check that the review took place before removal. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-4 (explanation of main score factors supports the reviewer's interpretation of the output (14(4)(c))); FR-5 (notifies recruiters that the ranking is machine-generated, supporting awareness of automated output (14(4)(b)))
  - Category: `human_oversight`
  - Action: Add automation-bias safeguards: UI warnings, ranking presented alongside the underlying factors, a mandatory reviewer action or confirmation before any removal, and tracking of override/acceptance rates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement covers per-ranking override but not a system-level stop/interrupt capability that lets overseers halt the model safely (for example, suspending automated ranking and filtering). [low] - Article 14(4)(e) (`art:14:p4:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: NFR-6 (rollback to a previously approved model version when checks fail, a partial intervention capability (14(4)(e)))
  - Category: `human_oversight`
  - Action: Add a mechanism for authorised staff to suspend automated ranking or filtering and fall back to manual screening.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement does not specify who may perform the review, so the competence, training and authority of the assigned overseers (Art 26(2)) cannot be assured, and reviewers may not understand the model's limitations. [low] - Article 26(2) (`art:26:p2`)
  - Partly addressed by: NFR-4 (access control limiting access to authorised recruitment staff)
  - Category: `human_oversight`
  - Action: Restrict the review/override role to designated recruiters, and document required training and authority in the instructions for use and role configuration.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Add automation-bias safeguards and a mandatory, recorded reviewer confirmation before any candidate removal.
- Provide a safe suspend/stop function for automated ranking and filtering, with fallback to manual screening.
- Define the reviewer role with required competence, training and authority, and document it in the instructions for use.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-7 logs scores, rankings, explanations, overrides and decisions, which is a solid base for traceability. It does not specify automatic lifetime recording of events relevant to risk, post-market monitoring or deployer monitoring, nor a log retention period of at least six months.

**Risks:**

- The logged items cover outputs and decisions only. They do not cover events that identify risk or substantial modification situations, or that support post-market and deployer monitoring (for example model version, use period, anomalies, threshold alerts). [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-8 (audit records tracing input data, model version and human actions (partial traceability under 12(2)))
  - Category: `record_keeping`
  - Action: Extend the log schema to record use period, model version, input references, monitoring or threshold alert events, and model changes. Document how these support Art. 72 and Art. 26(5) monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- No retention period is specified for the logs. Providers and deployers must keep them for a period appropriate to the intended purpose, at least six months, subject to data protection law. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Add a retention requirement of at least six months, or a longer period justified by the recruitment context and GDPR. Include tamper-evident storage and deletion rules.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs

**Cited provisions:**

- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Extend FR-7 to log use period, model version, input references, alert events and model changes so events relevant to risk and monitoring are captured.
- Specify a log retention period of at least six months, aligned with data protection law, with integrity protection.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 18 Documentation keeping (art:18); Article 14 Human oversight (art:14)

**Analysis:** FR-8 provides traceability of input data, model version and human actions per screening decision, and FR-7 logs scores and overrides. The remaining gaps are an undefined retention period and missing event coverage for risk identification, post-market monitoring and deployer monitoring.

**Risks:**

- No retention period is specified for audit records; Articles 19(1) and 26(6) require logs to be kept for a period appropriate to the intended purpose, and at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Add a configurable retention period of at least six months, aligned to GDPR minimisation and applicable employment-law limits. Include deletion/expiry handling and make records available to deployers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The requirement scopes audit records to screening decisions and does not state that logging captures events relevant to identifying risk situations or substantial modifications, post-market monitoring, and deployer operation monitoring. [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-7 (logs model scores, rankings, explanations, overrides and final decisions (automatic event recording, 12(1)))
  - Category: `record_keeping`
  - Action: Extend the logged event set to include model-version changes, rollbacks, threshold-breach alerts, data-quality failures and system errors. Define these as inputs to post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))
- The wording does not require automatic recording of events over the system lifetime, nor say that audit records are tamper-evident and linked to the identity of the human reviewer and the time of each use. [low] - Article 12(1) (`art:12:p1`)
  - Partly addressed by: FR-7 (logs recruiter overrides and final screening decisions); NFR-4 (access control on candidate data and explanations)
  - Category: `record_keeping`
  - Action: State that records are generated automatically for the whole system lifetime. Include reviewer identity, timestamps and the model version, and protect the records with integrity controls (append-only or hash-chained).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

**Recommendations:**

- Specify a log retention period of at least six months, with expiry and deletion handling.
- Broaden the logged events to cover risk situations, model changes and monitoring needs.
- State automatic lifetime logging with reviewer identity, timestamps and tamper-evidence.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-9 is a protective control that blocks facial recognition, biometric identification and emotion recognition in screening, which supports Article 5(1)(f). It does not say how the block is enforced or verified, and it does not cover biometric categorisation (Art 5(1)(g)), which the system could also infer from candidate inputs.

**Risks:**

- FR-9 omits biometric categorisation (inferring race, political opinion, religion, sexual orientation etc. from biometric data), which Article 5(1)(g) prohibits. Its list covers only facial recognition, biometric identification and emotion recognition. [medium] - Article 5(1)(g) (`art:5:p1:g`)
  - Partly addressed by: NFR-3 (excludes protected attributes such as race, religion and political opinion as ranking inputs (partial; does not address biometric inference))
  - Category: `other`
  - Action: Extend FR-9 to prohibit biometric categorisation and any inference of sensitive traits from biometric data. Define 'biometric data' to include facial images, voice and video in application materials.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
- FR-9 says 'prevent' but does not specify the technical enforcement, such as blocking video, image or voice inputs or emotion and affect inference from interview media. It also has no verification test, so compliance with the Article 5(1)(f) emotion inference ban in recruitment (a workplace context) cannot be shown. [medium] - Article 5(1)(f) (`art:5:p1:f`)
  - Partly addressed by: FR-1 (limits ingestion to resumes, cover letters and application form responses (implicitly excludes biometric media, but not stated as a control))
  - Category: `other`
  - Action: Specify enforcement controls: input-type allow-list for ingestion, no biometric or affect-inference model components, and a release-gate test confirming no emotion or biometric features reach scoring. Document the control in the risk management file.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
- No requirement ties the misuse prevention in FR-9 to a risk management process that identifies and tests the foreseeable misuse of the system with biometric or emotion inputs, for example if a deployer adds video interviews. [low] - Article 9(2)(b) (`art:9:p2:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Add the foreseeable misuse scenario (biometric or emotion analysis added by the deployer) to the risk register, with FR-9 as the mitigation and a defined test against prior-defined metrics.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system (closest match: Article 9(2)(a))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Prohibited AI practices, Article 5(1)(f)**
  > (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons;
- **Risk management system, Article 9(2)(b)**
  > (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse;

**Recommendations:**

- Extend FR-9 to prohibit biometric categorisation and inference of sensitive attributes from biometric data.
- Specify and test the technical enforcement of FR-9 (input restrictions, no affect-inference components, release-gate check).
- Record biometric and emotion-recognition misuse in the risk management file, linked to FR-9 as the mitigation.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 85 Right to lodge a complaint with a market surveillance authority (art:85)

**Analysis:** FR-10 gives candidates a review channel, but it does not state that candidates are told an AI system was used, nor that they can obtain an explanation of the AI's role and the main elements of the decision. Without these, candidates cannot meaningfully contest an adverse decision.

**Risks:**

- The review channel does not give the candidate a clear and meaningful explanation of the AI system's role in the decision and the main elements of the decision. FR-4 explains score factors to recruiters only. [high] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-4 (generates the main factors behind each suitability score, which can feed a candidate-facing explanation (recruiter-facing only))
  - Category: `transparency`
  - Action: Extend FR-10 so a candidate who requests review also receives, from the deployer, an explanation of how the automated ranking figured in the decision and its main elements. Draw this from the FR-4 factors and the FR-7/FR-8 records, in candidate-readable language.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- Nothing requires informing candidates up front that they are subject to a high-risk AI system in recruitment, so candidates may not know a review channel exists or applies. FR-5 notifies recruiters only. [high] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a requirement to notify candidates at application time that AI-based scoring and ranking is used. The notice should point to the FR-10 review channel and say how to use it.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- FR-10 does not say who handles review requests, with what competence and authority, or whether they can reverse the outcome. FR-6 covers recruiter override before removal but is not tied to candidate-initiated review. [medium] - Article 26(2) (`art:26:p2`)
  - Partly addressed by: FR-6 (recruiter can review, override or reject any automated ranking (14(4)(d)))
  - Category: `human_oversight`
  - Action: Specify that candidate review requests are assigned to a competent, trained and authorised human reviewer. The reviewer must be able to disregard or override the ranking (reusing FR-6), the outcome and rationale must be logged (FR-7), and a response time limit should be set.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Provide candidates with an explanation of the AI system's role and the main elements of the decision when they request review.
- Notify candidates at application time that an AI system is used and how to request review.
- Define the reviewer role, authority, override capability, logging and response time for candidate review requests.

---

### NFR-1

**Risk level:** high

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 11 Technical documentation (art:11)

**Analysis:** NFR-1 covers basic data quality checks (missing values, duplicates, label consistency) but not the wider Article 10 governance practices: bias examination and mitigation, representativeness, provenance and documentation of data preparation. Without these, discriminatory bias in recruitment training data could go undetected.

**Risks:**

- No examination of training/validation/test data for biases likely to cause discrimination, and no measures to detect, prevent or mitigate them; NFR-1 checks only technical data quality. [high] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: NFR-2 (measures model performance across demographic groups (output-level bias check, not data-level examination or mitigation))
  - Category: `data_governance`
  - Action: Add dataset-level bias examination (e.g. label and outcome distribution across lawful protected groups and proxies) before training, with documented mitigation steps and acceptance criteria.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Data quality criteria stop at missing values, duplicates and label inconsistency; there is no check that datasets are relevant, representative of the applicant population, or have appropriate statistical properties, with no pass/fail thresholds. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Define representativeness and completeness criteria and thresholds for the job families, roles and applicant groups served, and block training when validation fails.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'training dataset' is an instance of the defined term 'training data' (Article 3(29)), which Article 10 uses
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- The requirement does not specify recording of data origin, collection purpose, labelling and cleaning operations, assumptions, or identified data gaps, so validation results cannot be evidenced for conformity assessment. [medium] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: FR-8 (retains audit records tracing input data and model version for screening decisions (not training-data governance records))
  - Category: `data_governance`
  - Action: Generate and retain a dataset validation report per training run covering provenance, preparation steps, detected issues, remediation and residual data gaps, linked to the model version.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;

**Recommendations:**

- Add data-level bias examination and mitigation to pre-training validation, with acceptance criteria.
- Define representativeness and statistical-property criteria with pass/fail thresholds that gate training.
- Produce a versioned dataset validation and provenance report for each training run to support technical documentation.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** NFR-2 measures performance per demographic group but only where lawful data exists, and sets no metrics, acceptance thresholds, or mitigation steps, and nothing ties results to the instructions for use. Bias findings could therefore go unacted on and undeclared to deployers.

**Risks:**

- Per-group measurement has no defined fairness metrics, pre-set acceptance thresholds, or required mitigation when disparities are found, so bias is examined but not necessarily detected, prevented or mitigated. [medium] - Article 10(2)(g) (`art:10:p2:g`)
  - Partly addressed by: NFR-5 (alerts when bias metrics fall outside configured thresholds (detection only, in operation)); NFR-3 (excludes protected attributes as ranking inputs (prevention of direct use))
  - Category: `data_governance`
  - Action: Define fairness metrics and acceptance thresholds per group, and require documented mitigation (re-sampling, re-weighting, retraining) and re-test when thresholds are breached. Make this a release gate.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- x [low] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: x
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'demographic evaluation data' is an instance of the defined term 'testing data' (Article 3(32)), which Article 10 uses
- The 'where lawful data is available' qualifier has no fallback, so groups may go unevaluated with no documented data gap or remediation plan, and representativeness of test data across groups is not assured. [medium] - Article 10(2)(h) (`art:10:p2:h`)
  - Partly addressed by: NFR-1 (dataset validation for missing values, duplicates and inconsistent labels (not representativeness or group coverage))
  - Category: `data_governance`
  - Action: Require documenting which groups could not be evaluated and why. Add alternative approaches (lawful proxy or synthetic evaluation, deployer-supplied data) and a representativeness check on test sets.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- Group-level performance results are not required to be declared in the instructions for use, so deployers may not learn about performance differences across groups or known limitations. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Require group-level performance results, metrics and known limitations to be included in the instructions for use and updated with each model version.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(b))
    - requirement term 'demographic evaluation data' is an instance of the defined term 'testing data' (Article 3(32)), which Article 13 uses

**Cited provisions:**

- **Data and data governance, Article 10(2)(g)**
  > (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Data and data governance, Article 10(2)(h)**
  > (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Define per-group fairness metrics, acceptance thresholds and mandatory mitigation with re-test as a release gate.
- Document unevaluated groups and data gaps, provide a fallback evaluation approach, and check representativeness of test sets.
- Publish group-level performance results and limitations in the instructions for use for each model version.

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** NFR-3 excludes protected attributes as direct ranking inputs, which is a real control. However, it does not address proxy features (e.g., names, postcodes, gaps in employment) or the bias examination and mitigation that Article 10 requires, so indirect discrimination could persist.

**Risks:**

- Excluding protected attributes as direct inputs does not cover proxy variables or features extracted from resumes and cover letters that correlate with protected characteristics. NFR-3 also sets no process to examine, detect, and mitigate resulting bias in the data and model. [medium] - Article 10(2)(g) (`art:10:p2:g`)
  - Partly addressed by: NFR-2 (measurement of performance across demographic groups, supporting bias examination (10(2)(f))); NFR-5 (alerts when bias metrics fall outside thresholds, supporting ongoing detection of bias)
  - Category: `data_governance`
  - Action: Extend NFR-3 to cover proxy and derived features. Add a documented proxy-feature analysis (correlation or feature-attribution tests against protected attributes) with defined mitigation and acceptance thresholds before release and at each retraining.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement is not tied to any risk management step that identifies discrimination risk from ranking logic and verifies, against predefined metrics, that the exclusion works in testing. [low] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: NFR-5 (threshold-based monitoring of bias metrics after deployment)
  - Category: `risk_management`
  - Action: Add a verification criterion to NFR-3, such as a test showing that ranking output is invariant to protected attributes or to inferred proxies, run against predefined thresholds before deployment.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Data and data governance, Article 10(2)(g)**
  > (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.

**Recommendations:**

- Extend NFR-3 to proxy and derived features, and add a documented proxy-feature analysis with mitigation and acceptance thresholds before release and at each retraining.
- Add a testable verification criterion to NFR-3 (ranking invariance to protected attributes and proxies) with predefined thresholds, run before deployment.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** NFR-4 provides role-based access to candidate data and explanations, which is a basic cybersecurity control. Its wording does not cover the other Article 15(5) protections (confidentiality attacks, tampering with outputs, or integrity of model and data), and it does not say how 'authorised' is defined or enforced.

**Risks:**

- Access control is limited to viewing candidate data and explanations. It does not cover unauthorised alteration of scores, rankings, outputs, model or data, and gives no authentication, role-definition, or access-review criteria. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-7 (logging of scores, rankings, explanations and overrides, which supports detecting unauthorised changes to outputs); FR-8 (audit records tracing input data, model version and human actions)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend NFR-4 to define roles and least-privilege, require strong authentication, apply write/modify controls to scores, rankings, models and datasets, and add periodic access reviews and attempt logging.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No AI-specific confidentiality or manipulation protections (e.g. against model extraction, data poisoning, or adversarial inputs via application documents) are specified. Access control only limits human viewers, not attacks on the model. [medium] - Article 15(5) (`art:15:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: NFR-1 (validation of training and evaluation datasets for quality issues, which partly limits corrupted training data)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add system-level cybersecurity requirements covering data/model poisoning, adversarial or malicious-input handling for uploaded applications, and confidentiality attacks, with a threat model and test evidence.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Extend NFR-4 with authentication, role definitions, least-privilege, write-access controls on outputs and models, and periodic access reviews.
- Add system-level requirements and tests for AI-specific attacks (poisoning, adversarial inputs, confidentiality attacks) under Article 15(5).

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** NFR-5 provides threshold-based alerting on accuracy, bias and data quality, which is a useful post-deployment control. It does not define a post-market monitoring plan, say how alerts feed corrective action, or tie thresholds to declared accuracy metrics.

**Risks:**

- Alerting is not tied to a documented post-market monitoring system and plan that systematically collects and analyses performance data over the lifecycle to evaluate continuous compliance. [medium] - Article 72(3) (`art:72:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-8 (retained audit records of inputs, model version and human actions, which can serve as monitoring data); NFR-2 (per-group performance measurement as monitoring data)
  - Category: `post_market_monitoring`
  - Action: Define a post-market monitoring plan (data sources, metrics, review cadence, owners) in the technical documentation, and have NFR-5 alerts feed it as one input.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- Thresholds are only 'configured'. No requirement says they derive from the accuracy metrics declared in the instructions for use or from predefined metrics and probabilistic thresholds, and no accuracy, robustness or consistency target is set for the lifecycle. [medium] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require thresholds to derive from the declared accuracy and fairness metrics and the pre-defined test thresholds, be versioned and change-controlled, and be stated in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement stops at alert generation. It defines no response (triage, escalation, suspension, rollback, risk reassessment) and no link to the risk management process, so alerts may not trigger corrective action. [medium] - Article 9(2)(c) (`art:9:p2:c`)
  - Partly addressed by: NFR-6 (rollback to an approved model version when checks fail (corrective measure))
  - Category: `risk_management`
  - Action: Specify alert recipients, severity levels, response SLAs and escalation (including NFR-6 rollback). Record alert outcomes as inputs to the risk management review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system (closest match: Article 9(2)(c))
- Data quality alerting covers monitoring, but it is unclear whether it detects bias in data and input drift over time, including feedback from recruiter decisions that influence future inputs. [low] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: NFR-1 (pre-training validation of missing values, duplicates and inconsistent labels); NFR-2 (performance measured across demographic groups)
  - Category: `data_governance`
  - Action: Specify the data-quality and bias checks monitored in production (representativeness, drift, label feedback loops) and the demographic groups covered.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(3)**
  > 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Risk management system, Article 9(2)(c)**
  > (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;

**Recommendations:**

- Create and document a post-market monitoring plan that uses NFR-5 alerts as an input.
- Derive alert thresholds from declared accuracy and fairness metrics and put them under change control.
- Define alert triage, escalation and corrective action, linked to NFR-6 rollback and risk management review.
- Extend production monitoring to cover bias, drift and feedback loops in the data.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 20 Corrective actions and duty of information (art:20); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 17 Quality management system (art:17)

**Analysis:** NFR-6 provides a rollback control, which supports Art. 15 fail-safe/robustness and Art. 20 corrective action. It does not define the failure criteria, who authorises rollback, or how rollback is governed and recorded, so rollback could be unmeasurable or ad hoc.

**Risks:**

- The rollback trigger relies on undefined 'safety, robustness, or fairness checks', with no declared metrics or pass/fail thresholds, so the failure condition is not testable. NFR-5 alerts on accuracy, bias and data quality thresholds but does not tie them to rollback or cover robustness or safety. [medium] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: NFR-5 (threshold-based detection of accuracy and bias deviations (partial input to the trigger)); NFR-2 (per-group performance measurement used for fairness checks)
  - Category: `risk_management`
  - Action: Define the checks, metrics and probabilistic thresholds (accuracy, robustness, per-group fairness) that constitute failure and trigger rollback. Link them to the NFR-5 thresholds and the NFR-2 group metrics.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The requirement does not specify that the rollback target must be an approved version with intact validation evidence, or that rollback is subject to change control and recorded. Without this, consistent performance over the lifecycle and corrective-action traceability are not assured. FR-8 traces model version per decision but does not cover rollback events. [medium] - Article 15(1) (`art:15:p1`)
  - Partly addressed by: FR-8 (traceability of model version used in each screening decision)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require a versioned registry of approved models with stored validation results, an authorised-approver workflow for rollback, and logging of rollback events (who, when, why, from/to version). Verify the target version still passes checks before reactivation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Rollback is not linked to a corrective-action process that assesses whether a failed model is non-conforming, investigates causes, and informs deployers or authorities where required. [low] - Article 20(1) (`art:20:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `quality_management`
  - Action: Document a procedure connecting rollback to root-cause investigation, deployer notification and, where a risk under Art. 79(1) arises, authority notification. Include it in the QMS.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 20 Corrective actions and duty of information

**Cited provisions:**

- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.

**Recommendations:**

- Define measurable failure criteria and thresholds for the safety, robustness and fairness checks that trigger rollback, aligned with NFR-5 and NFR-2.
- Add a model registry with approved-version validation evidence, an authorisation workflow, and logging of rollback events.
- Link rollback to a documented corrective-action and notification procedure within the QMS.

---
