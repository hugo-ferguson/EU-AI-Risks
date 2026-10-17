# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 4
- Medium: 10
- Low: 2

### Overall analysis

Overall, the assessment reviewed 16 requirements and rated 4 as high risk, 10 as medium risk and 2 as low risk. The main review focus areas are accuracy robustness cybersecurity, data governance, human oversight, transparency and record keeping. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 16 requirements reviewed in total.
- Risk distribution: 4 high, 10 medium, 2 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (9), data governance (8), human oversight (7), transparency (7), record keeping (5).
- 2 low-risk requirements appear to describe a control or safeguard, but still needs clarification/evidence review.

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

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 12 Record-keeping (art:12); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-1 ingests untrusted candidate documents and form responses with no stated input validation or integrity controls. This leaves a cybersecurity and robustness gap (malicious or malformed files, adversarial or manipulated content) in a high-risk recruitment system.

**Risks:**

- Candidate-submitted resumes, cover letters and form responses are untrusted inputs; the requirement specifies no file validation, malware scanning, sanitisation, or detection of manipulated or adversarial content (e.g. hidden text, prompt injection) that could skew scoring. [high] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add ingestion controls: file type/size limits, malware scanning, parsing sanitisation, detection of hidden or adversarial content, and quarantine plus logging of rejected submissions.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not handle malformed, incomplete or inconsistent submissions (parsing failures, unreadable documents), so ingestion errors could silently degrade scores and disadvantage candidates. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: NFR-5 (alerts when data quality checks fall outside thresholds (partial, monitoring only))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define error handling for parse failures: flag incomplete extractions, route them to human review rather than scoring them, and record the parse status per application.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Ingested application data is not constrained for relevance and representativeness, and the requirement does not say whether free-text or form fields may carry protected-attribute proxies or special-category data; the data-governance practices of Article 10 therefore do not clearly cover ingested inputs. [low] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: NFR-3 (exclusion of protected attributes as ranking inputs); NFR-1 (dataset validation for missing values, duplicates and inconsistent labels (training/evaluation data only))
  - Category: `data_governance`
  - Action: Document the ingested fields and their purpose, minimise collected data, and specify preprocessing that strips or flags protected-attribute content before scoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'candidate resumes' is an instance of the defined term 'personal data' (Article 3(50)), which Article 10 uses

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;

**Recommendations:**

- Add input validation, sanitisation, malware scanning and adversarial-content detection at ingestion.
- Define handling of malformed or partial submissions, with human-review routing and per-application parse status.
- Document ingested fields and data-minimisation rules, and strip or flag protected-attribute content and proxies before scoring.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9)

**Analysis:** FR-2 defines the scoring function but sets no accuracy target or metrics, and it does not require validity evidence that the extracted features (education, experience) are suitable proxies for job suitability. Without these, the score could be unreliable or discriminatory, and the system could not support declared accuracy in instructions for use.

**Risks:**

- No accuracy level or metrics are specified for the suitability score. NFR-5 alerts on thresholds, but no thresholds or declared accuracy metrics are defined for the scoring function. [high] - Article 15(3) (`art:15:p3`)
  - Partly addressed by: NFR-5 (monitoring of model accuracy against configured thresholds (partial; thresholds not defined))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy and validity metrics and target levels for the suitability score (e.g. rank correlation with validated recruiter outcomes, per-group error rates), test against them before release, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The score is derived from features extracted from the application (education, experience, skills). The requirement has no design choices, assumptions or proxy-bias examination on what these features represent. The features can correlate with protected characteristics, and NFR-3 only excludes protected attributes as direct inputs. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: NFR-1 (dataset checks for missing values, duplicates and inconsistent labels (10(3) quality)); NFR-2 (measurement of performance across demographic groups (examination for bias, 10(2)(f))); NFR-3 (exclusion of protected attributes as direct ranking inputs)
  - Category: `data_governance`
  - Action: Document the feature selection rationale and the assumptions about what each feature measures. Run proxy-bias analysis on the extracted features and define mitigation and acceptance criteria for any bias found.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Scoring depends on extraction from unstructured resumes and forms. The requirement sets no robustness expectations for extraction errors or inconsistent formats, and none against manipulated inputs (e.g. keyword stuffing or hidden text). [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: NFR-6 (rollback to an approved model version after failed robustness checks (fail-safe, 15(4)))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify handling for extraction failures and low-confidence parses. Add adversarial input tests and detection of manipulated application content before scoring.
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

- Define and declare accuracy and validity metrics and thresholds for the suitability score.
- Document feature rationale and run proxy-bias analysis with mitigation criteria.
- Add robustness requirements for extraction errors and manipulated application content.

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-3 ranks candidates from the suitability score, and most surrounding controls exist (FR-4 explanations, FR-5 notification, FR-6 override, FR-7 logging). The remaining gaps are that the ranking itself does not state how recruiters are protected from automation bias, and that accuracy metrics for the ranking are not declared to deployers.

**Risks:**

- The ranking presents the output to recruiters with no stated measure to keep them aware of automation bias or over-reliance on the rank order (for example, presentation of rank as a recommendation rather than a decision, or score uncertainty). [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-6 (ability to override or reject the ranking (14(4)(d))); FR-4 (help recruiters interpret the output (14(4)(c))); FR-5 (makes recruiters aware that the ranking is model-generated)
  - Category: `human_oversight`
  - Action: Specify that the ranking UI shows scores as advisory with confidence/uncertainty, avoids hard cut-offs or auto-rejection, and includes automation-bias guidance for recruiters.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No requirement states the accuracy level and metrics of the ranking, or that they are declared in the instructions for use, so deployers cannot judge how far to trust the rank order. [medium] - Article 15(3) (`art:15:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: NFR-5 (monitors accuracy against configured thresholds (15(1) consistent performance)); NFR-2 (measures performance per demographic group)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define ranking-quality metrics (for example rank correlation or top-k precision against recruiter outcomes), set acceptance thresholds, and require their declaration in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Add to FR-3 that rankings are advisory, carry uncertainty indicators, and come with automation-bias safeguards for recruiters.
- Define ranking accuracy metrics and thresholds, and declare them in the instructions for use.

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 11 Technical documentation (art:11)

**Analysis:** FR-4 gives recruiters per-candidate score explanations, which largely supports interpretability. It does not state explanation fidelity or limitations, and does not provide a way to give affected candidates an explanation of the AI's role in a decision.

**Risks:**

- FR-4 requires explanations only for recruiters and does not require the explanation to cover the AI system's role in the decision and the main elements of the decision, so the deployer cannot give affected candidates the explanation they are entitled to; FR-10 offers only a review channel. [medium] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-10 (channel for candidates to request review of a decision influenced by automated ranking)
  - Category: `transparency`
  - Action: Extend FR-4 so explanations can be exported in a candidate-facing form describing the AI's role in the decision and the main elements of the decision, and link this to FR-10 review requests.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- FR-4 does not require the explanations to be faithful to the model's actual scoring logic or to state their limitations (e.g. confidence, known accuracy conditions), so recruiters may over-rely on or misread plausible but inaccurate explanations. [medium] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-6 (ability to disregard, override or reverse the ranking (14(4)(d))); FR-5 (recruiters are made aware the ranking is model-generated (14(4)(b)))
  - Category: `human_oversight`
  - Action: Specify that explanations derive from the actual model (with a fidelity check), show factor weights and uncertainty, and include a note on limitations and automation-bias risk.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))
- The explanation capability and its technical characteristics are not required to be documented in instructions for use for deployers (what the explanations show, their limits, how to interpret them). [low] - Article 13(3)(b) (`art:13:p3:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a documentation deliverable describing the explanation method, its outputs, interpretation guidance and limitations in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Make explanations exportable in candidate-facing form covering the AI's role and main decision elements, tied to the FR-10 review process.
- Require faithful, model-derived explanations with uncertainty and limitation notes to reduce over-reliance.
- Document the explanation method and its interpretation guidance in the Article 13 instructions for use.

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-5 notifies recruiters that a ranking is automated, which supports deployer-side interpretation and automation-bias awareness. It does not specify when or how the notice appears, and does not inform candidates they are subject to a high-risk AI system (Art. 26(11)).

**Risks:**

- FR-5 notifies only recruiters; no requirement informs candidates that they are subject to a high-risk AI system used to assist decisions about them. FR-10 gives a review channel but does not give notice of AI use. [high] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a requirement (or extend FR-5) so candidates are told in the application portal, before or at submission, that automated ranking/scoring supports screening decisions, in an accessible format.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
    - requirement term 'automated decision-support model' is the defined term 'AI system' (Article 3(1)), which this provision uses
- The notification only states that a ranking is model-generated. It does not make the output interpretable (limitations, confidence, intended-use caveats) or warn against over-reliance on the ranking (automation bias). [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-4 (explains main factors behind each score, supporting correct interpretation of output (14(4)(c))); FR-6 (recruiter can review, override or reject any ranking (14(4)(d)))
  - Category: `human_oversight`
  - Action: Extend the notice to include a brief automation-bias reminder, link to model limitations, and statement that the recruiter may disregard or override the ranking. Specify the notice appears alongside every ranking view.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))
    - requirement term 'automated decision-support model' is an instance of the defined term 'AI system' (Article 3(1)), which Article 14 uses
- Instructions for use for deployers (provider identity, accuracy metrics, limitations, human oversight measures, log mechanisms) are not required anywhere in the SRS; the in-product notice cannot replace them. [medium] - Article 13(3) (`art:13:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-4 (technical capability to explain output (13(3)(b)(iv)))
  - Category: `transparency`
  - Action: Add a requirement to deliver instructions for use covering Art. 13(3) content, and surface a link to them from the FR-5 notice.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
    - requirement term 'automated decision-support model' is an instance of the defined term 'AI system' (Article 3(1)), which Article 13 uses
- The wording does not state when or how the notification is delivered (every ranking view, each session, or once), or that it is clear and accessible, so effectiveness cannot be verified. [low] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Specify delivery timing, placement and format in FR-5, and add an acceptance test that the notice displays with every ranking output.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
    - requirement term 'automated decision-support model' is the defined term 'AI system' (Article 3(1)), which this provision uses

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add a candidate-facing notice that automated ranking/scoring is used in screening, at the latest at application submission.
- Extend FR-5 with an automation-bias warning, a link to model limitations, and a statement that the ranking can be overridden.
- Add a requirement to produce instructions for use covering Art. 13(3) content and link to it from the notice.
- Define delivery timing, placement and accessibility of the recruiter notification, with acceptance tests.

---

### FR-6

**Risk level:** low

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-6 gives recruiters review, override and reject capability before candidate removal, which substantially covers Art 14(4)(d). Remaining gaps are minor: no stop/interrupt capability and no safeguard against automation bias or against rubber-stamping the override step.

**Risks:**

- FR-6 covers override of individual rankings but does not provide a system-level stop/interrupt function to halt the ranking system in a safe state. [low] - Article 14(4)(e) (`art:14:p4:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: NFR-6 (rollback to a previously approved model version when checks fail (partial: a model-level fallback, not an operator stop))
  - Category: `human_oversight`
  - Action: Add a requirement for an authorised operator to suspend or halt automated scoring and ranking, with candidates routed to manual review. This can build on the NFR-6 rollback.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement permits review but does not ensure reviewers stay aware of automation bias, for example through a check that overrides are not routinely skipped. It also does not say that a reviewer sees the explanation before confirming a rejection. [low] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-4 (explanation of the main factors behind each score, supporting interpretation of the output (14(4)(c))); FR-5 (recruiter notified that a ranking is model-generated, supporting awareness of reliance on automated output)
  - Category: `human_oversight`
  - Action: Reword FR-6 so that a rejection requires a recorded recruiter action after the score explanation is displayed. Add reviewer guidance on automation bias and monitor override and acceptance rates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;

**Recommendations:**

- Add an operator-level stop or suspend function that routes candidates to manual review, building on NFR-6 rollback.
- Require a recorded recruiter action after the explanation is shown before any automated rejection takes effect, add automation-bias guidance, and monitor override rates.

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-7 logs scores, rankings, explanations, overrides and decisions, which is a strong base for traceability. It does not specify use-period timestamps, model version, event types for risk detection and post-market monitoring, identity of the reviewing recruiter, or a retention period.

**Risks:**

- The log scope covers outputs and decisions only. It does not say which events must be captured to identify risk situations (e.g. accuracy/bias drift, anomalies, substantial modification) or to support post-market monitoring and deployer monitoring. Model version and input references are not named in FR-7 and are only partly covered by FR-8. [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-8 (traceability of input data and model version for each screening decision)
  - Category: `record_keeping`
  - Action: Extend FR-7 to log event types relevant to risk identification, post-market monitoring and deployer monitoring: model version, input data reference, threshold/alert events, and model changes. Add timestamps for each event.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- No log retention period is specified. Logs must be kept for a period appropriate to the intended purpose, at least six months, by both provider and deployer to the extent the logs are under their control. [medium] - Article 19(1) (`art:19:p1`)
  - Partly addressed by: FR-8 (retention of audit records for screening decisions)
  - Category: `record_keeping`
  - Action: Add a retention requirement of at least six months, or longer as the purpose and data protection law require, with tamper-evident storage and deletion rules. Document which logs the provider controls and which the deployer controls.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- Override logging does not state that the identity of the human reviewer, their action and their rationale are captured. Oversight actions therefore cannot be reliably attributed or reviewed. [low] - Article 14(4)(d) (`art:14:p4:d`)
  - Partly addressed by: FR-6 (recruiter ability to review, override or reject automated ranking (14(4)(d))); FR-8 (tracing of human actions involved in each screening decision)
  - Category: `human_oversight`
  - Action: Specify that each override log entry records reviewer ID, timestamp, original and revised outcome, and a reason field.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;

**Recommendations:**

- Extend FR-7 to log risk-relevant and monitoring events, model version and input references, with timestamps.
- Define a log retention period of at least six months, with integrity protection and a provider/deployer responsibility split.
- Require override log entries to include reviewer identity, before/after outcome and rationale.

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 11 Technical documentation (art:11)

**Analysis:** FR-8 gives a good traceability basis (input data, model version, human actions), but it does not specify a retention period or the recording of events relevant to risk identification and post-market monitoring. Without these, logs may be deleted too early or may not support Article 12(2) purposes.

**Risks:**

- No retention period is stated for audit records; Articles 19(1) and 26(6) require logs to be kept for a period appropriate to the intended purpose, and at least six months. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Add a configurable retention period of at least six months for audit records, with deletion rules that respect data protection law and access to the records limited as in NFR-4.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The audit records are scoped to screening decisions only. They do not require recording events that identify risk situations or substantial modifications, or events that support post-market monitoring and deployer monitoring (e.g. period of each use, model changes, anomalies, threshold breaches). [low] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-7 (logging of scores, rankings, explanations, recruiter overrides and final decisions (12(1) automatic recording))
  - Category: `record_keeping`
  - Action: Extend the logged event set to cover session or use periods, model version changes and rollbacks, and monitoring-alert events. Link these to the decision-level audit trail so they support Article 72 post-market monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Specify an audit-record retention period of at least six months, with access controls and a data-protection-compliant deletion policy.
- Broaden audit records to include use periods, model changes and monitoring-alert events, so that the logs support risk identification and post-market monitoring.

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-9 is a protective control that blocks facial recognition, biometric identification and emotion recognition in screening, which supports the Article 5(1)(f) emotion-inference prohibition in the workplace. Only minor wording and evidence gaps remain: the prevention mechanism is unspecified, and biometric categorisation and inference of emotions from non-biometric inputs are not covered.

**Risks:**

- FR-9 names facial recognition, biometric identification and emotion recognition but omits biometric categorisation, which Art. 5(1)(g) prohibits when it infers race, political opinions, religion, etc. Screening of video, photo or voice inputs could therefore still categorise candidates without breaching FR-9 as worded. [low] - Article 5(1)(g) (`art:5:p1:g`)
  - Partly addressed by: NFR-3 (excludes protected attributes (race, religion, political opinion) as ranking inputs, but only for explicit attributes, not biometric inference)
  - Category: `other`
  - Action: Extend FR-9 to prohibit biometric categorisation and any inference of sensitive traits from biometric data. Reference NFR-3 for the protected-attribute exclusion.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses
- FR-9 says 'prevent' but does not specify the technical mechanism (e.g. input-modality allow-list, blocking of audio/video/image uploads, absence of biometric models) or how it is verified. Conformity evidence for the emotion-inference prohibition in recruitment is therefore weak. [low] - Article 5(1)(f) (`art:5:p1:f`)
  - Partly addressed by: FR-1 (limits ingestion to resumes, cover letters and application form responses, which implicitly excludes biometric media but is not stated as a control)
  - Category: `other`
  - Action: Specify enforcement in FR-9: restrict ingestion to text documents, reject biometric media at the portal, and add a release test that verifies no biometric or emotion-inference component is active. Document the result as compliance evidence.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
    - requirement term 'emotion recognition' is an instance of the defined term 'emotion recognition system' (Article 3(39)), which Article 5 uses

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Prohibited AI practices, Article 5(1)(f)**
  > (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons;

**Recommendations:**

- Extend FR-9 to prohibit biometric categorisation and inference of sensitive traits from biometric data.
- Define the technical enforcement of FR-9 (modality restriction and a release test) and keep the test results as evidence.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 85 Right to lodge a complaint with a market surveillance authority (art:85); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-10 gives candidates a review channel but does not make it an explanation right: candidates are not told the AI's role or the main elements of the decision, and are not informed up front that AI is used. The channel is also not tied to a human reviewer with authority to override.

**Risks:**

- The review channel does not give affected candidates a clear and meaningful explanation of the AI system's role in the decision and the main elements of the decision. FR-4 explains factors to recruiters only, not to candidates. [high] - Article 86(1) (`art:86:p1`)
  - Category: `transparency`
  - Action: Extend FR-10 so that a review request returns a candidate-facing explanation of the AI's role in the decision and the main elements of the decision taken, drawn from the FR-4 factors and the FR-7/FR-8 records.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- Nothing in the SRS informs candidates, before or during screening, that they are subject to a high-risk AI system. Without this notice candidates may not know a review channel exists or when to use it. [high] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a requirement to notify candidates in the recruitment portal that AI-assisted ranking is used, and link that notice to the FR-10 review channel.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- FR-10 does not say who handles a review request. It does not require a competent human with authority to disregard or reverse the AI-influenced outcome, or set a response timeline or outcome record. FR-6 covers only recruiter override before removal. [medium] - Article 14(4)(d) (`art:14:p4:d`)
  - Partly addressed by: FR-6 (human ability to review, override or reject an automated ranking before a candidate is removed (14(4)(d)))
  - Category: `human_oversight`
  - Action: Specify that review requests are routed to a competent human reviewer who is independent of the original ranking, can override or reverse the outcome, and whose decision is logged with a response deadline.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;

**Recommendations:**

- Provide candidates with an explanation of the AI's role and the main decision elements through the review channel.
- Add a candidate notice that an AI system is used in screening, linked to the review channel.
- Define review routing to a competent human reviewer with override authority, deadlines and logged outcomes.

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 11 Technical documentation (art:11)

**Analysis:** NFR-1 covers basic data quality checks (missing values, duplicates, label inconsistencies) but does not address bias examination or mitigation of datasets, representativeness, or documented data governance practices required for a high-risk recruitment system. Without these, discriminatory bias in training data could go undetected.

**Risks:**

- NFR-1 has no examination of training, validation and testing datasets for biases that could lead to discrimination, and no measures to detect, prevent or mitigate them. NFR-2 measures performance by group, but only on evaluation data and after training. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: NFR-2 (measurement of model performance across demographic groups (post-training detection only, partly supporting 10(2)(f)))
  - Category: `data_governance`
  - Action: Extend dataset validation with a pre-training bias examination (label and outcome distribution by group, proxy-feature checks), with documented mitigation steps and acceptance criteria that block training when they fail.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement does not check that datasets are relevant, representative of the candidate population and job contexts, or have appropriate statistical properties. It also does not state completeness and error-free thresholds or what happens on failure. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Add representativeness and statistical-property checks (coverage by role, region, and group where lawful) and define pass/fail thresholds for missing values, duplicates and label inconsistency, with a documented remediation step.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
    - requirement term 'training dataset' is an instance of the defined term 'training data' (Article 3(29)), which Article 10 uses
    - requirement term 'evaluation dataset' is the defined term 'testing data' (Article 3(32)), which this provision uses
- Validation results and data-preparation operations (cleaning, labelling, origin, assumptions, gaps) are not required to be recorded as data governance evidence, so Annex IV technical documentation and QMS data management procedures could not be demonstrated. [low] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: FR-8 (audit records tracing input data and model version for screening decisions (not training data governance))
  - Category: `data_governance`
  - Action: Require that each validation run produces a versioned report covering data origin, preparation operations, issues found, and identified data gaps. Link it to the model version in the audit records.
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

- Add pre-training bias examination and mitigation with acceptance criteria to dataset validation.
- Add representativeness and statistical-property checks with defined thresholds and a failure action.
- Produce versioned dataset validation reports covering origin, preparation and data gaps, as technical documentation evidence.

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** NFR-2 measures performance per demographic group, but only where lawful data is available. It sets no fallback when data is missing, no metrics or acceptance thresholds, and no mitigation or documentation of results, so bias evidence may be absent or may not be acted on.

**Risks:**

- Group-level evaluation is conditional on data availability, with no fallback (e.g. lawful proxy or synthetic data, or a documented data-gap assessment). Bias examination and data-gap identification could be skipped silently. [medium] - Article 10(2)(h) (`art:10:p2:h`)
  - Partly addressed by: NFR-1 (dataset quality validation (missing values, duplicates, inconsistent labels), which supports part of 10(2)(h) data shortcomings)
  - Category: `data_governance`
  - Action: Require a documented data-gap assessment when demographic evaluation data is unavailable. Define a fallback such as lawful proxy-based or synthetic evaluation, and a remediation plan.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- No metrics, groups, or acceptance thresholds are defined for the per-group measurement, and no bias mitigation follows from the results. The requirement does not lead to detection, prevention and mitigation of discriminatory bias. [medium] - Article 10(2)(g) (`art:10:p2:g`)
  - Partly addressed by: NFR-5 (alerts when bias metrics fall outside configured thresholds); NFR-6 (rollback of a model that fails fairness checks)
  - Category: `data_governance`
  - Action: Specify fairness and performance metrics per group and pass/fail thresholds. Require a mitigation workflow and sign-off when thresholds are breached.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(e))
- Per-group testing is not tied to pre-defined metrics and thresholds before release, or to repeating the testing over the lifecycle. It is also not tied to declaring group-level performance in the instructions for use. [low] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: State that per-group results are run pre-release and on each model update. Include the accuracy metrics and group-level performance in the instructions for use (Art. 13(3)(b)(ii),(v)).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(h)**
  > (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Data and data governance, Article 10(2)(g)**
  > (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Add a documented fallback and data-gap assessment for when demographic evaluation data is unavailable.
- Define per-group metrics, acceptance thresholds and a mitigation and sign-off process.
- Run per-group testing pre-release and on each model update, and declare the results in the instructions for use.

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** NFR-3 excludes protected attributes as direct ranking inputs, which is a real control. It does not cover proxy features or bias examination and mitigation, so the model could still discriminate indirectly through correlated inputs.

**Risks:**

- Excluding protected attributes only as direct inputs does not address proxy variables (e.g. name, postcode, employment gaps, graduation year, or text extracted from resumes) that can reproduce discrimination. NFR-3 contains no requirement to examine or mitigate proxy bias. [medium] - Article 10(2)(g) (`art:10:p2:g`)
  - Partly addressed by: NFR-2 (measures performance across demographic groups, which helps detect bias (10(2)(f))); NFR-5 (alerts when bias metrics exceed thresholds)
  - Category: `data_governance`
  - Action: Extend NFR-3 to cover proxy and inferred protected attributes. Add proxy-feature analysis (correlation and feature-attribution tests), exclude or mitigate flagged features, and document the bias examination and mitigation measures.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement lists only examples (race, religion, disability, political opinion) and gives no complete, verifiable definition of protected attributes. It also has no acceptance test showing they are not inferred from resumes, cover letters or application form responses. [low] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: NFR-2 (testing performance across demographic groups against bias)
  - Category: `risk_management`
  - Action: Define the full list of protected attributes under EU non-discrimination law. Add a pre-deployment test with predefined metrics and thresholds that verifies these attributes (and detectable proxies) have no influence on score or rank, and record the results.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Data and data governance, Article 10(2)(g)**
  > (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.

**Recommendations:**

- Add proxy-variable detection and mitigation to NFR-3, and document the bias examination under Article 10(2)(f)-(g).
- Specify the full protected-attribute list and add a predefined-threshold test, with recorded results, that these attributes and their proxies do not influence ranking.

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12)

**Analysis:** NFR-4 provides role-based access to candidate data and explanations, which is a legitimate control. The remaining gap is that it does not extend to the wider cybersecurity measures Article 15(5) expects (integrity and confidentiality protection against manipulation of the system, its outputs and its data), and it does not state how access is authenticated or audited.

**Risks:**

- The requirement only restricts viewing of candidate data and explanations. It does not cover protection against unauthorised alteration of model use, outputs or performance, or confidentiality attacks (e.g. write/modify access, model and training data access, authentication strength). [medium] - Article 15(5) (`art:15:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Extend NFR-4 or add a security requirement covering authentication (e.g. MFA), least-privilege write and admin access to scores, rankings, models and training data, and controls against tampering and confidentiality attacks. Add security testing.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not specify that access grants and access events (who viewed candidate data or explanations) are recorded. Without this, unauthorised access cannot be detected or traced. [low] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-7 (logging of model scores, rankings, explanations, overrides and decisions as events for traceability (but not access events))
  - Category: `record_keeping`
  - Action: Require that access events to candidate data and explanations are logged and reviewable, and that the access role list is periodically reviewed. Align this with the FR-7 and FR-8 logging.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Broaden NFR-4 into a cybersecurity requirement covering authentication, least-privilege write and admin access, and protection of models and data against tampering and confidentiality attacks.
- Add access-event logging and periodic access reviews for candidate data and explanations.

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** NFR-5 gives threshold-based alerts for accuracy, bias and data quality, which is a useful detection control. It does not say who is alerted, what response follows, or how alerts feed a documented post-market monitoring plan and risk management process, so drift or bias could go unaddressed after deployment.

**Risks:**

- Alerts are not tied to a documented post-market monitoring system or plan. No systematic collection and analysis of performance data over the system's lifetime is specified, and there is no link to technical documentation. [medium] - Article 72(3) (`art:72:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-7 (logging of model scores, rankings and decisions, which provides some performance data for monitoring (72(2))); NFR-2 (per-group performance measurement, which provides some monitoring data (72(2)))
  - Category: `post_market_monitoring`
  - Action: Define a post-market monitoring plan in the technical documentation. It should state which alert and performance data are collected, the sources including deployer feedback, the review cadence, and how alert history is retained and analysed.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- Thresholds and metrics are only 'configured'. There are no predefined accuracy, robustness or bias metrics and thresholds, and no named owner or response action when an alert fires (triage, corrective action, rollback trigger). [medium] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: NFR-6 (rollback to an approved model version when safety, robustness or fairness checks fail (9(5)(b) mitigation and control measures))
  - Category: `risk_management`
  - Action: Specify the metrics and threshold values, with their rationale, in the risk management documentation. Define alert severity levels, the responsible role, response time, and escalation. Link critical alerts to the rollback process and to risk register updates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
    - requirement term 'model accuracy' is an instance of the defined term 'performance of an AI system' (Article 3(18)), which Article 9 uses
- The requirement does not say that alert thresholds and accuracy metrics are declared in the instructions for use, or that alerts reach deployers or oversight staff so they can detect anomalies and unexpected performance. [low] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Name the alert recipients (recruiter or oversight roles and the provider). Document the declared accuracy metrics and the expected performance levels in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(3)**
  > 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Create a post-market monitoring plan that consumes NFR-5 alerts and the FR-7 logs, and include it in the technical documentation.
- Define concrete metrics, thresholds, alert owners and response and escalation procedures, linked to NFR-6 rollback and the risk register.
- Specify alert recipients and declare accuracy metrics and thresholds in the instructions for use.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 20 Corrective actions and duty of information (art:20)

**Analysis:** NFR-6 provides a rollback capability, which is a valid robustness and corrective control. It does not say who or what triggers rollback, which pass/fail thresholds apply, how a rollback is recorded, or how it links to corrective action and provider duties to notify downstream parties.

**Risks:**

- Rollback is triggered by 'fails safety, robustness, or fairness checks' with no defined metrics, thresholds, or trigger mechanism. NFR-5 alerts on accuracy, bias and data-quality thresholds, but nothing links an alert to a rollback decision, and 'safety' and 'robustness' checks are not defined. [medium] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: NFR-5 (configured thresholds for accuracy, bias and data-quality that detect degradation (supports testing against defined metrics)); NFR-2 (per-group performance measurement that can feed fairness checks)
  - Category: `risk_management`
  - Action: Define the pre-set metrics and probabilistic thresholds that count as a failed safety, robustness, or fairness check. State whether rollback is automatic or requires approval, and link it to the NFR-5 alerts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The requirement does not specify the approval status or criteria for a 'previously approved' version, or that the rollback target is itself re-verified for robustness and security. The rollback path could therefore restore a stale or vulnerable model. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Maintain a registry of approved model versions with their validation results. Verify the integrity and current security and fairness status of the target version before restoring it, and add a documented fail-safe fallback if no approved version qualifies.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Rollback is not tied to corrective-action procedures. The requirement does not say that a rollback event is recorded, that it prompts a non-conformity assessment, or that deployers are informed. [medium] - Article 20(1) (`art:20:p1`)
  - Partly addressed by: FR-8 (audit records tracing the model version used in each screening decision (helps identify affected decisions after a rollback))
  - Category: `quality_management`
  - Action: Define a procedure under which a rollback is logged with its cause and affected version, triggers a conformity review, and notifies deployers and, where required, authorities. Record it in the change-management process.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 20 Corrective actions and duty of information
- Model version management and modification control are not documented as part of a quality management procedure, such as approval, testing, and the re-validation frequency before and after a rollback. [low] - Article 17(1)(a) (`art:17:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `quality_management`
  - Action: Document model release, approval, and rollback in the QMS as a modification-management procedure, including the validation steps required before and after a version change.
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

- Define quantitative rollback triggers and connect them to the NFR-5 alerts, with a clear decision rule.
- Keep a registry of approved model versions and verify the rollback target's integrity and validation status before restoring it.
- Log every rollback with its cause, and run a corrective-action workflow that notifies deployers.
- Add model release and rollback to the QMS change-management procedures.

---
