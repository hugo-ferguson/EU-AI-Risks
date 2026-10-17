# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 14

### Overall analysis

Overall, the assessment reviewed 16 requirements and rated 2 as high risk and 14 as medium risk. The main review focus areas are transparency, human oversight, data governance, record keeping and risk management. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 2 high, 14 medium, 0 low.
- Most frequent mapped obligation areas: transparency (9), human oversight (7), data governance (6), record keeping (5), risk management (5).

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

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 12 Record-keeping (art:12)

**Analysis:** FR-1 only covers ingestion of resumes, cover letters and form responses. It sets no input validation, malicious-file or poisoning protection, or input-data relevance and representativeness checks. Poor or manipulated inputs could corrupt candidate scores in a high-risk recruitment system.

**Risks:**

- No input-integrity or security controls on ingested documents (file validation, malware scanning, adversarial or manipulated content such as hidden-text keyword stuffing or prompt injection). Manipulated inputs could alter scoring outputs, and no other SRS requirement covers this. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add ingestion safeguards: file type/size validation, malware scanning, sanitisation of hidden or injected text, and adversarial-input detection, with rejected inputs logged.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not define input data specifications or quality checks at ingestion (completeness, parse errors, language or format coverage, relevance to the job). NFR-1 validates only training and evaluation datasets, not live inputs, so parsing errors on unusual resume formats or languages could skew results for some candidate groups. [medium] - Article 26(4) (`art:26:p4`)
  - Category: `data_governance`
  - Action: Define input data specifications and runtime checks for parse failures, missing fields and unsupported formats or languages. Flag low-quality extractions for human review, and document the specifications in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The requirement does not say that candidates are informed, at the point of submission through the portal, that an AI system will analyse their application. FR-5 notifies recruiters only, and FR-10 covers review requests after a decision. [medium] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Add a notice in the portal submission flow that AI is used to analyse and rank applications, and record the candidate's acknowledgement.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Obligations of deployers of high-risk AI systems, Article 26(4)**
  > 4. Without prejudice to paragraphs 1 and 2, to the extent the deployer exercises control over the input data, that deployer shall ensure that input data is relevant and sufficiently representative in view of the intended purpose of the high-risk AI system.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Add ingestion safeguards: file validation, malware scanning, sanitisation of hidden or injected text, and adversarial-input detection.
- Define input data specifications and runtime quality checks, and route low-confidence parses to human review.
- Show candidates an AI-use notice at submission and log their acknowledgement.

---

### FR-2

**Risk level:** medium

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9)

**Analysis:** FR-2 generates the suitability score used to filter candidates, but it does not say how proxy bias is handled in the data-driven scoring, nor does it set accuracy metrics for the score. Several controls already exist elsewhere in the SRS (NFR-1, NFR-2, NFR-3, NFR-5, FR-4, FR-6), so only the remaining gaps are flagged.

**Risks:**

- NFR-1 checks data quality (missing values, duplicates, labels) and NFR-3 excludes protected attributes, but nothing requires a bias examination of training data or mitigation of proxy features (e.g. education, experience gaps, institution names) that FR-2 extracts and scores on. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add a documented bias examination of training data and extracted features, with proxy-variable testing and mitigation steps for education, experience and skills inputs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- FR-2 does not define the accuracy metrics, or the thresholds for them, against which the suitability score is validated; NFR-5 alerts on configured thresholds, but none are specified, and the accuracy levels are not declared for the instructions for use. [medium] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define score validity and accuracy metrics and acceptance thresholds, test against them before release, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Scoring depends on features extracted from free-text applications, and no requirement addresses resilience to extraction errors or to inputs manipulated to inflate scores (e.g. keyword stuffing, hidden text, adversarial resumes). [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add robustness tests for parsing and extraction errors and adversarial inputs, with detection of manipulated applications and handling of low-confidence extractions.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Document bias examination and proxy-feature mitigation for training data and extracted features, extending NFR-1 and NFR-3.
- Specify accuracy metrics and thresholds for the suitability score, test against them, and declare them in the instructions for use (link to NFR-5).
- Add adversarial and extraction-error robustness testing and input manipulation detection for the scoring pipeline.

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-3 ranks candidates from the suitability score. The SRS already covers most oversight and transparency controls (FR-4, FR-5, FR-6, FR-7, FR-10), so only narrow gaps remain: no automation-bias safeguard in the ranking output and no declared ranking accuracy or limitations in the instructions for use.

**Risks:**

- The ranking presents candidates in an ordered list without any requirement for automation-bias safeguards (e.g. showing score uncertainty or limitations next to the ranking, or preventing the rank order alone from driving shortlisting). FR-5 and FR-6 provide a notice and an override, but nothing addresses over-reliance on the ranking itself. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Category: `human_oversight`
  - Action: Show score confidence or uncertainty and a limitations note alongside the ranking. Avoid hard cut-offs that hide lower-ranked candidates. Add reviewer guidance on automation bias, and consider sampling lower-ranked candidates for review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No requirement states that ranking accuracy metrics, known limitations and the ranking logic are declared in the instructions for use. NFR-2 and NFR-5 measure performance, but nothing ties the results to the deployer documentation. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Add a requirement to document ranking accuracy metrics, performance across groups, known limitations and foreseeable misuse in the instructions for use, and to update them with each model version.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- Ranking accuracy and robustness are not specified. There is no target for ranking quality (e.g. rank stability under input variation) and no requirement to declare it, so degraded or inconsistent rankings could go undetected despite NFR-5 alerts. [low] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness`
  - Action: Define ranking-level accuracy and consistency metrics and thresholds (e.g. rank stability, agreement with human reviewers) and feed them into the NFR-5 monitoring alerts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Add automation-bias safeguards to the ranking output: uncertainty display, limitations note and reviewer guidance.
- Document ranking accuracy metrics, limitations and foreseeable misuse in the instructions for use.
- Define ranking-specific accuracy and robustness metrics and thresholds, and link them to monitoring.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-4 gives recruiters plain-language explanations of score drivers, which supports Art. 13 transparency. It does not say how explanation fidelity is validated, how its limits are communicated, or how it counters automation bias, so recruiters may misread or over-rely on the scores.

**Risks:**

- FR-4 has no accuracy or fidelity criterion for the explanations and does not state their limitations (e.g. approximation, confidence, groups where performance differs). Recruiters may misread the output, and the Art. 13(3)(b)(iv)/(vii) information on explanation capabilities and output interpretation is not covered. [medium] - Article 13(3) (`art:13:p3`)
  - Category: `transparency`
  - Action: Define explanation fidelity tests and show confidence or limitation notes with each explanation. Document the explanation capabilities and limits in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
    - requirement term 'main factors' is an instance of the defined term 'input data' (Article 3(33)), which Article 13 uses
- FR-4 does not require explanations to help recruiters spot over-reliance on scores (automation bias) or to interpret outputs correctly, for example by flagging low-confidence scores or showing the factors that were not considered. FR-6 provides override but not interpretive support. [medium] - Article 14(4) (`art:14:p4`)
  - Category: `human_oversight`
  - Action: Add UI cues in the explanation view such as confidence indicators and an automation-bias reminder. Add recruiter guidance on interpreting the factors, and show the explanation alongside the override control from FR-6.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The explanations are recruiter-facing only. Nothing says they can support the deployer's duty to give an affected candidate a clear, meaningful account of the AI's role in a decision; FR-10 provides only a review channel. [low] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Make explanations exportable or reusable in a candidate-facing format. Include the AI's role and the main decision elements so the deployer can answer FR-10 requests.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Add explanation fidelity validation and documented limitations, and cover them in the instructions for use.
- Add confidence indicators and automation-bias safeguards to the explanation interface.
- Provide a candidate-facing explanation format that supports FR-10 review requests.

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-5 notifies recruiters that a ranking is automated, which partly supports Art. 13 interpretability. The requirement does not address informing candidates that they are subject to the high-risk system, and the notification content is undefined. Candidates would not learn that automated ranking is used in their screening.

**Risks:**

- FR-5 notifies only recruiters. No requirement in the SRS informs candidates (the affected natural persons) that they are subject to a high-risk AI system used to assist decisions about them. FR-10 gives a review channel but does not provide advance notice. [high] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Add a requirement to disclose automated ranking to candidates in the recruitment portal, in clear language, no later than at application submission. Record that the notice was shown.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The notification content is unspecified. A bare 'generated by an automated model' flag does not help recruiters interpret the output appropriately, for example with respect to accuracy, limitations and the meaning of the score. FR-4 covers factor explanations but not the system's limitations or performance characteristics. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Define the notification content. Include a link to the instructions for use, the score's meaning, known limitations and accuracy metrics. Tie it to the FR-4 explanations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- The notification is not tied to automation-bias awareness. FR-6 provides override, but the notice does not prompt recruiters to review rankings critically or remind them they may disregard the output. [low] - Article 14(4) (`art:14:p4`)
  - Category: `human_oversight`
  - Action: Add to the notification a statement that the ranking is advisory and can be overridden under FR-6. Add recruiter guidance on automation bias.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.

**Recommendations:**

- Add a candidate-facing disclosure that automated ranking is used, shown in the portal at or before application submission.
- Specify the notification content and link it to the instructions for use, limitations and FR-4 explanations.
- Make the notification state that the ranking is advisory and overridable, and add automation-bias guidance for recruiters.

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 86 Right to explanation of individual decision-making (art:86); Article 12 Record-keeping (art:12)

**Analysis:** FR-6 provides a strong human review, override and reject control for rankings, which is the core of Art. 14(4)(d). Remaining gaps are narrow: no stop/interrupt capability for the system as a whole, no automation-bias safeguards, and no requirement that reviewers are competent and authorised to use the override.

**Risks:**

- FR-6 covers overriding individual rankings but not automation-bias awareness; no requirement addresses reviewer prompts, requiring a reviewed rationale before accepting rejections, or other measures against over-reliance on rankings used to screen candidates out. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Category: `human_oversight`
  - Action: Add UI safeguards against over-reliance: show score uncertainty and limitations, require reviewer confirmation with a reason for auto-recommended rejections, and monitor override and acceptance rates for rubber-stamping (FR-4 and FR-5 only partly cover this).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No requirement provides a stop or interrupt mechanism to halt automated ranking or filtering in a safe state, and FR-6 is limited to per-candidate overrides. Rollback in NFR-6 is tied to failed checks and is not an operator-triggered halt. [medium] - Article 14(4)(e) (`art:14:p4:e`)
  - Category: `human_oversight`
  - Action: Add an operator-accessible control to suspend automated ranking or removal, falling back to fully manual screening without losing candidate data.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement does not specify that review and override authority is limited to recruiters with the necessary competence, training and authority, or that they have support to exercise it. NFR-4 covers data access only. [low] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Define reviewer roles and permissions for override and reject actions, and document required training in the instructions for use or deployer guidance.
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

- Add anti-automation-bias design measures and track override and acceptance rates.
- Add an operator-triggered stop or suspend function with a manual screening fallback.
- Define role-based reviewer authority and training prerequisites for override and reject actions.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 18 Documentation keeping (art:18)

**Analysis:** FR-7 logs scores, rankings, explanations, overrides and decisions, which covers most of the event logging expected by Art. 12(1), and FR-8 adds audit records. It does not specify log retention, use-period timestamps, or which events support risk identification and post-market monitoring, so traceability and retention obligations are only partly met.

**Risks:**

- FR-7 and FR-8 do not set a log retention period (at least six months, or longer if appropriate to the intended purpose), so logs could be deleted too early or kept without a defined period. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Define and implement a log retention policy of at least six months, configurable per deployer. Align it with data-protection retention limits and protect logs from deletion or tampering.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- FR-7 lists logged output events but does not state that logs support identifying risk situations or substantial modifications, post-market monitoring, or deployer operational monitoring. Model version, input data reference, and timestamps are covered only in FR-8 and not for every FR-7 event type. [medium] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Extend FR-7 so each logged event carries a timestamp, model version, input reference and user or actor ID. Add log fields or events that feed NFR-5 alerts and post-market monitoring, such as drift, anomalies, and override rates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Deployers must keep the automatically generated logs and use them to monitor operation, but FR-7 does not state that deployers can access or export the logs. [low] - Article 26(6) (`art:26:p6`)
  - Category: `record_keeping`
  - Action: Provide deployer access to, and export of, the logs. Restrict access consistently with NFR-4 and document the retention responsibilities in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.

**Recommendations:**

- Implement a configurable log retention policy of at least six months with tamper protection.
- Add timestamp, model version, input reference, and actor ID to every FR-7 event, and feed the logs into monitoring and post-market processes.
- Give deployers controlled access to and export of logs, and document retention responsibilities.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 18 Documentation keeping (art:18); Article 14 Human oversight (art:14)

**Analysis:** FR-8 and FR-7 together cover most traceability needs (input data, model version, human actions). The remaining gaps are a defined retention period for the audit records and logging that supports risk identification and post-market monitoring.

**Risks:**

- FR-8 says audit records are 'retained' but sets no retention period; Articles 19(1) and 26(6) require logs to be kept for a period appropriate to the intended purpose, and at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Specify a configurable minimum retention period of at least six months (longer if justified by the intended purpose), reconcile it with data-protection deletion rules, and add automated retention enforcement and tests.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The audit records are scoped to tracing individual screening decisions. Neither FR-8 nor FR-7 states that logs capture events relevant to identifying risk situations or substantial modifications, supporting post-market monitoring, or enabling deployer monitoring of operation (e.g. model version changes, rollbacks, threshold alerts, period of each use). [medium] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Extend the logging spec to record system-level events (model deployments and rollbacks, NFR-5 alert triggers, session start and end times) and document how these logs feed post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Define and enforce a log retention period of at least six months, aligned with data-protection law.
- Extend logging to system-level events that support risk identification, post-market monitoring and deployer monitoring.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-9 is a protective control that blocks facial recognition, biometric identification and emotion recognition in screening, which supports the Article 5(1)(f) prohibition on workplace emotion inference. It is stated only as a functional intent, with no defined scope, enforcement mechanism or verification, so the control may not be reliably effective.

**Risks:**

- FR-9 does not say how the prevention is enforced or verified (e.g. blocking biometric or video/audio inputs, disabling emotion or biometric inference models, testing for inference of emotion-related traits from text or other inputs), and its scope is limited to 'candidate screening' rather than the whole recruitment flow (e.g. interviews). Emotion inference could remain possible outside that scope, and the Article 5(1)(f) prohibition would then be breached. [medium] - Article 5(1) (`art:5:p1`)
  - Category: `prohibited_practices`
  - Action: Define FR-9 scope to cover all recruitment stages. Enforce it technically with input-type allow-listing (no image, video or audio ingestion), no biometric or emotion models in the pipeline, and release-gate tests confirming the system cannot infer emotions or biometric traits. Check this in each model release.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
    - requirement term 'facial recognition' is the defined term 'biometric identification' (Article 3(35)), which this provision uses
- The SRS has no risk management step that treats misuse or drift toward biometric or emotion inference (e.g. a later feature addition or a deployer enabling a video-interview add-on) as a foreseeable risk and tracks it as a risk control. FR-9 is not tied to any documented risk management process. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Record biometric or emotion-recognition misuse in the risk register as a foreseeable misuse scenario. Link FR-9 to it as a mitigation. Add a change-control check that blocks releases introducing biometric or emotion-inference capability, and review it periodically.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system (closest match: Article 9(2)(a))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm; (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm; (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following: (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity; (d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence, based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity; (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage; (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons; (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement; (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years. Point (h) of the first subparagraph is without prejudice to Article 9 of Regulation (EU) 2016/679 for the processing of biometric data for purposes other than law enforcement.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Broaden FR-9 to the whole recruitment lifecycle and add technical enforcement plus release-gate tests proving no emotion or biometric inference occurs.
- Add biometric and emotion-recognition misuse to the risk register, link FR-9 as its mitigation, and add change-control gating for new inputs or models.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 85 Right to lodge a complaint with a market surveillance authority (art:85)

**Analysis:** FR-10 gives candidates a review-request channel, but it does not give them the explanation of the AI system's role and the main decision elements that Article 86 requires, and it does not inform them that the system is being used. FR-4 explains scores only to recruiters, so affected candidates cannot meaningfully contest a decision.

**Risks:**

- The requirement provides a review channel only. No requirement gives affected candidates a clear and meaningful explanation of the AI system's role and the main elements of the decision; FR-4 explanations are written for recruiters and NFR-4 restricts explanations to staff. [high] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Add a requirement to give candidates, on request or with the review channel, a plain-language explanation of how the ranking was used and the main factors behind the decision, derived from FR-4 and FR-7 data. Define how this is released to candidates despite the NFR-4 access restriction.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- No requirement informs candidates up front that they are subject to a high-risk AI system for screening and ranking, so candidates may not know the review channel applies to them. FR-5 notifies recruiters only. [medium] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Add a candidate-facing notice in the recruitment portal at application time that automated scoring and ranking is used, with a link to the review request channel.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The requirement does not specify who handles review requests, with what competence and authority, or how the outcome can reverse the automated result. FR-6 covers recruiter override only before removal, not post-decision candidate challenges. [medium] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Specify that review requests are routed to a trained reviewer with authority to override the ranking, with outcomes and rationale logged under FR-7/FR-8, a response-time target, and the result communicated to the candidate.
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

- Provide candidates with a clear explanation of the AI system's role and the main decision factors, separate from the recruiter-only explanations.
- Notify candidates at application time that AI-based ranking is used and how to request review.
- Define the review workflow: reviewer competence and authority, ability to reverse the decision, logging, response time, and outcome communication.

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 11 Technical documentation (art:11); Article 17 Quality management system (art:17)

**Analysis:** NFR-1 is a data-quality control covering missing values, duplicates and inconsistent labels, so it should not be treated as absent. It does not address representativeness, bias examination or mitigation, or documented data governance practices. Those gaps matter because the system ranks job applicants, where biased training data can cause discrimination.

**Risks:**

- Validation covers only technical hygiene (missing values, duplicates, label inconsistency). It does not require examining datasets for biases likely to cause discrimination or detecting and mitigating them. NFR-2 measures model performance by demographic group and NFR-3 excludes protected attributes, but neither examines the datasets themselves for bias, such as proxy variables or historical hiring bias. [medium] - Article 10(2) (`art:10:p2`)
  - Category: `data_governance`
  - Action: Add dataset bias examination (representation skew, proxy features, label bias from past hiring decisions) with documented mitigation before training.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- Checks do not assess whether datasets are relevant, sufficiently representative, or have appropriate statistical properties for the groups of candidates the system will evaluate, or reflect the geographic, contextual and functional setting of use. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Define and automate representativeness checks (distribution by job family, region, and candidate groups where lawful) with pass/fail thresholds, and record the results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'training dataset' is an instance of the defined term 'training data' (Article 3(29)), which Article 10 uses
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- The requirement does not say that validation rules, thresholds, data-preparation operations (cleaning, labelling) and their outcomes are documented and retained as part of data management procedures. Without this, compliance with data governance cannot be demonstrated. [low] - Article 17(1) (`art:17:p1`)
  - Category: `quality_management`
  - Action: Produce a validation report per training run (checks, thresholds, remediation) and link it to the QMS data-management procedures and technical documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(f))

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Quality management system, Article 17(1)**
  > 1. Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system; (b) techniques, procedures and systematic actions to be used for the design, design control and design verification of the high-risk AI system; (c) techniques, procedures and systematic actions to be used for the development, quality control and quality assurance of the high-risk AI system; (d) examination, test and validation procedures to be carried out before, during and after the development of the high-risk AI system, and the frequency with which they have to be carried out; 62/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (e) technical specifications, including standards, to be applied and, where the relevant harmonised standards are not applied in full or do not cover all of the relevant requirements set out in Section 2, the means to be used to ensure that the high-risk AI system complies with those requirements; (f) systems and procedures for data management, including data acquisition, data collection, data analysis, data labelling, data storage, data filtration, data mining, data aggregation, data retention and any other operation regarding the data that is performed before and for the purpose of the placing on the market or the putting into service of high-risk AI systems; (g) the risk management system referred to in Article 9; (h) the setting-up, implementation and maintenance of a post-market monitoring system, in accordance with Article 72; (i) procedures related to the reporting of a serious incident in accordance with Article 73; (j) the handling of communication with national competent authorities, other relevant authorities, including those providing or supporting the access to data, notified bodies, other operators, customers or other interested parties; (k) systems and procedures for record-keeping of all relevant documentation and information; (l) resource management, including security-of-supply related measures; (m) an accountability framework setting out the responsibilities of the management and other staff with regard to all the aspects listed in this paragraph.

**Recommendations:**

- Extend dataset validation with bias examination and mitigation steps, including proxy-feature and historical label bias analysis.
- Add representativeness and statistical-property checks against the intended candidate population and setting.
- Document validation criteria and results per training run and link them to QMS data-management records and technical documentation.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 17 Quality management system (art:17)

**Analysis:** NFR-2 requires per-group performance measurement, which is a useful bias/accuracy control. Remaining gaps are that it lacks pre-defined metrics and thresholds, is conditional on data availability with no fallback, and has no link to documenting results for deployers.

**Risks:**

- Group-level testing is only required 'where lawful demographic data is available', with no fallback (e.g. proxy methods, synthetic or audit samples) and no requirement to document bias examination or mitigation, so bias may go unexamined for a recruitment system. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Define a fallback bias-evaluation method when demographic data is unavailable, and require documented bias examination and mitigation actions tied to NFR-2 results. NFR-1 covers only data quality checks and NFR-3 only excludes protected attributes.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- The requirement does not define the performance and fairness metrics, per-group acceptance thresholds, or when the measurement runs (before release, throughout development), so testing is not against prior defined metrics and probabilistic thresholds. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Specify metrics (e.g. selection rate, false negative rate per group), pass/fail thresholds, and a mandatory pre-release testing gate. Reuse the threshold configuration from NFR-5 and the rollback from NFR-6.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Per-group results are not required to be declared in the instructions for use, so deployers will not know the accuracy metrics or the performance for specific groups. [low] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Add a requirement to publish accuracy metrics and per-group performance results, with known limitations, in the instructions for use.
  - Trace:
    - requirement term 'demographic evaluation data' is an instance of the defined term 'testing data' (Article 3(32)), which Article 13 uses

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Define a fallback bias-evaluation method and require documented bias examination and mitigation tied to NFR-2 results.
- Specify the fairness and accuracy metrics, thresholds and a pre-release testing gate, linked to NFR-5 and NFR-6.
- Include per-group performance results and limitations in the instructions for use.

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 5 Prohibited AI practices (art:5); Article 14 Human oversight (art:14)

**Analysis:** NFR-3 excludes protected attributes as direct ranking inputs, which is a useful bias control. It does not address proxy features or bias in the training data, so discriminatory outcomes could persist through correlated inputs such as names, gaps in employment, or postcodes.

**Risks:**

- NFR-3 covers only direct protected attributes and does not require examining or mitigating proxy variables (e.g. name, address, photo, extracurriculars, employment gaps) that could reproduce discrimination. FR-2 extracts features from free-text resumes, and NFR-2 measures group performance but does not mitigate proxy bias. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add a proxy-feature analysis (correlation and feature-attribution tests against protected attributes) to feature extraction and training data review. Define mitigation steps, such as removing or masking proxy fields, and document the results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- NFR-3 is not tied to the risk management process: there is no documented risk analysis of discrimination, no defined test metrics or thresholds for verifying exclusion, and no pre-release test that protected attributes (including those inferred from text) do not influence rankings. [medium] - Article 9(2) (`art:9:p2`)
  - Category: `risk_management`
  - Action: Record discrimination risk and the protected-attribute exclusion measure in the risk management file. Add pre-release tests with defined fairness metrics and thresholds (e.g. counterfactual tests) covering inferred attributes, and re-run them on every model version.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Add proxy-variable detection and mitigation to feature extraction and training data governance, and document the outcome.
- Link NFR-3 to the risk management system with testable fairness acceptance criteria, including counterfactual tests for inferred attributes, run before each release.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** NFR-4 restricts viewing of candidate data and explanations to authorised recruiters, which is a sound confidentiality control. The remaining gap is that it names no technical measures against unauthorised third-party access or manipulation of the system, and it does not extend to the logs and audit records in FR-7 and FR-8.

**Risks:**

- NFR-4 covers only viewing of candidate data and explanations. It does not specify resilience to unauthorised third parties exploiting vulnerabilities, such as authentication hardening, protection against confidentiality attacks, or tamper protection for scores and outputs. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `cybersecurity`
  - Action: Add security requirements: strong authentication and MFA, role-based least-privilege access, encryption in transit and at rest, integrity protection of scores and outputs, and testing against confidentiality and model-extraction attacks. Cover the FR-7 logs and FR-8 audit records in the same access policy.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Extend NFR-4 into a cybersecurity requirement covering authentication, least-privilege roles, encryption, output integrity and confidentiality-attack testing, applied to candidate data, explanations, and the FR-7/FR-8 logs and audit records.

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** NFR-5 provides threshold-based alerts for accuracy, bias and data quality, which supports post-market monitoring. It does not say who receives the alerts, how they feed a documented monitoring plan and risk management process, or what happens after an alert fires.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system or plan. Nothing says that alert and performance data are systematically collected, retained and analysed over the lifetime of the system to evaluate continuing compliance. [medium] - Article 72(2) (`art:72:p2`)
  - Category: `post_market_monitoring`
  - Action: Persist alert events and underlying metrics in a monitoring data store. Document them in a post-market monitoring plan that is part of the technical documentation, and add a periodic compliance review of that data.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- Thresholds are only 'configured', with no requirement that they be set against predefined metrics and probabilistic thresholds suited to the intended purpose. The response to a breach is also undefined: no escalation path to risk management, and no link to NFR-6 rollback or to suspension. The other SRS requirements do not cover this. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Define and version-control the metrics and thresholds, with rationale, in the risk management file. Specify alert severity levels, named owners, response SLAs, and triggers for rollback (NFR-6) or suspension of use. Feed alert outcomes into the periodic risk review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
    - requirement term 'model accuracy' is an instance of the defined term 'performance of an AI system' (Article 3(18)), which Article 9 uses
- Accuracy alerts are not linked to the accuracy levels and metrics declared in the instructions for use. It is also unclear whether they cover robustness and feedback-loop drift, so the system may not stay consistent with its declared performance over its lifecycle. [low] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness`
  - Action: Derive the alert thresholds from the declared accuracy metrics. Add robustness and drift or feedback-loop indicators to the monitored set, and state them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not say whether alerts reach the deployer or how deployers can pass monitoring findings or risk signals to the provider. Deployers must monitor operation and inform providers, and must suspend use and report where a risk is identified. [low] - Article 26(5) (`art:26:p5`)
  - Category: `deployer_monitoring`
  - Action: Route alerts to the deployer's responsible staff and to the provider. Document in the instructions for use how to act on an alert, including when to report a risk or serious incident and when to suspend use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Obligations of deployers of high-risk AI systems, Article 26(5)**
  > 5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and shall suspend the use of that system. Where deployers have identified a serious incident, they shall also immediately inform first the provider, and then the importer or distributor and the relevant market surveillance authorities of that incident. If the deployer is not able to reach the provider, Article 73 shall apply mutatis mutandis. This obligation shall not cover sensitive operational data of deployers of AI systems which are law enforcement authorities. For deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law, the monitoring obligation set out in the first subparagraph shall be deemed to be fulfilled by complying with the rules on internal governance arrangements, processes and mechanisms pursuant to the relevant financial service law.

**Recommendations:**

- Store alert and metric history and define a post-market monitoring plan in the technical documentation.
- Define metrics, thresholds, escalation owners and response actions, and link them to NFR-6 rollback and the risk management process.
- Align the alert thresholds with the declared accuracy metrics and add robustness and drift indicators.
- Add alert routing to deployers and providers, and document the reporting and suspension procedure.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 20 Corrective actions and duty of information (art:20)

**Analysis:** NFR-6 provides a technical rollback control, but it does not say who decides to roll back, which approved version is restored, or how a rollback ties into corrective-action duties and incident handling. As a result, rollback may happen ad hoc, without being documented or linked to the provider's risk management and corrective-action processes.

**Risks:**

- The rollback trigger is stated as 'fails safety, robustness, or fairness checks', but no pre-defined metrics or thresholds are tied to it. NFR-5 alerts on thresholds but is not linked to rollback, and NFR-2 covers measurement only. Rollback decisions may therefore be inconsistent or untestable. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Define acceptance thresholds for accuracy, robustness and fairness metrics, consistent with NFR-2 and NFR-5. Specify the rollback trigger and decision authority, and record the rollback as a risk management measure.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The requirement does not specify that the restored version must remain accurate, robust and consistent in performance. It does not require re-validating the previous version against current data or thresholds, or checking that a fallback exists if the earlier version is also degraded. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require that rollback targets are approved versions with stored validation results. Run a smoke test and fairness check after rollback. Define a fail-safe state, such as suspending automated ranking, if no version passes.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- A rollback caused by a failed check is not linked to the provider's duty to take corrective action and to inform deployers when the system may be non-conforming. Nothing covers notification, investigation or escalation. [medium] - Article 20(1) (`art:20:p1`)
  - Category: `corrective_actions`
  - Action: Add a rollback workflow that records the cause, notifies deployers, opens a non-conformity investigation, and escalates to the incident process where the failure may be a serious incident.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 20 Corrective actions and duty of information
    - requirement term 'rollback' is an instance of the defined term 'recall of an AI system' (Article 3(16)), which Article 20 uses
- Model change management is not covered. The requirement does not say that rollbacks are documented as modifications under the QMS, or that FR-7 and FR-8 version traceability records the rollback event, who approved it, and the affected screening decisions. [low] - Article 17(1)(a) (`art:17:p1:a`)
  - Category: `quality_management`
  - Action: Add a change-control record for each rollback covering approver, reason, versions involved, and candidates scored by the faulty version. Extend FR-8 audit records to include it.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(b))

**Cited provisions:**

- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.
- **Quality management system, Article 17(1)(a)**
  > (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system;

**Recommendations:**

- Define metric thresholds and decision authority for rollback triggers, linked to NFR-2 and NFR-5.
- Validate the restored model version after rollback and define a fail-safe state if no version passes.
- Link rollback to the corrective-action and deployer-notification process.
- Record rollbacks under QMS change control, with traceability through FR-7 and FR-8.

---
