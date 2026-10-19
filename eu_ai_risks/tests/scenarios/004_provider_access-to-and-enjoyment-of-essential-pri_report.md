# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 8

### Overall analysis

Overall, the assessment reviewed 10 requirements and rated 2 as high risk and 8 as medium risk. The main review focus areas are data governance, accuracy robustness cybersecurity, transparency, human oversight and risk management. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 10 requirements reviewed in total.
- Risk distribution: 2 high, 8 medium, 0 low.
- Most frequent mapped obligation areas: data governance (8), accuracy robustness cybersecurity (5), transparency (5), human oversight (4), risk management (4).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** medium

**Requirement:** The system shall collect and ingest applicant data from authorized sources, including application forms, credit bureau records, bank transaction histories, income and employment verification, and existing debt obligations.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 12 Record-keeping (art:12)

**Analysis:** FR-01 defines which data sources are ingested but not their provenance, original collection purpose, or representativeness for the credit-scoring population. It also says nothing about integrity or authenticity of ingested inputs. Validation (FR-02) and bias monitoring (FR-07) cover only part of this.

**Risks:**

- No documented data governance for collected data: origin, original purpose of personal data (bank transactions, bureau records), collection process, and data gaps or shortcomings are not specified. [medium] - Article 10(2)(b) (`art:10:p2:b`)
  - Category: `data_governance`
  - Action: Define and document per-source provenance, original collection purpose, legal basis, collection process and known data gaps, and keep this as a data-source register that governs what FR-01 may ingest.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(b))
- No requirement that the data collected for training, validation and testing is relevant, representative and suitable for the target applicant population and lending context (geography, behaviour, thin-file applicants). [medium] - Article 10(3) (`art:10:p3`)
  - Partly addressed by: FR-02 (cleaning and flagging of missing/inconsistent values (error-freeness and completeness, 10(3)))
  - Category: `data_governance`
  - Action: Add acceptance criteria for source coverage and representativeness (e.g., thin-file and underbanked groups, regional differences) and document the suitability assessment for each source, including the data it was designed to measure.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Ingestion from external sources (bureau, bank, employer verification) lacks integrity and authenticity controls against tampered or manipulated inputs, and data poisoning of data later used for retraining. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-02 (flagging anomalous values before scoring)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require authenticated, encrypted source connections, source authentication, input integrity checks, and anomaly detection on ingested data feeding scoring and retraining.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not examine ingested data for bias-prone proxies (e.g., transaction patterns correlating with protected attributes), so bias examination at the data stage is not specified. [low] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: FR-07 (bias monitoring of outcomes across protected groups and exclusion of protected attributes as inputs)
  - Category: `data_governance`
  - Action: Add a pre-ingestion bias and proxy-variable review of each data source, and record it in data governance documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(b))

**Cited provisions:**

- **Data and data governance, Article 10(2)(b)**
  > (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection;
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;

**Recommendations:**

- Create a data-source register documenting origin, original purpose, collection process and data gaps for each ingested source.
- Add representativeness and suitability acceptance criteria for ingested data per applicant segment.
- Add authentication and integrity controls on all external data feeds, including poisoning detection for retraining data.
- Add a proxy and bias review for each data source before it is approved for ingestion.

---

### FR-02

**Risk level:** medium

**Requirement:** The system shall validate, clean, and standardize all ingested applicant data, flagging missing, inconsistent, or anomalous values for correction or manual review before scoring.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-02 provides input-data validation, cleaning and flagging before scoring, which is a solid data-quality control for inference data. Remaining gaps: it does not define documented data-preparation practices or acceptance criteria, and it does not address input integrity against manipulation.

**Risks:**

- Validation and cleaning rules are not tied to documented data-preparation practices (cleaning operations, assumptions, data gaps). The requirement also does not apply the same quality controls to training, validation and testing datasets, since it covers only ingested applicant data. [medium] - Article 10(2)(c) (`art:10:p2:c`)
  - Category: `data_governance`
  - Action: Document the cleaning, standardization and imputation rules as versioned data-preparation practices. Apply the same pipeline and quality checks to training, validation and testing datasets. Record assumptions and identified data gaps.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Standardization and imputation of missing or anomalous values could introduce or amplify bias against groups, for example through proxy variables or thin-file applicants. The requirement does not examine or mitigate this. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Partly addressed by: FR-07 (monitoring outcomes across protected groups, which partly supports bias detection)
  - Category: `data_governance`
  - Action: Assess cleaning and imputation rules for differential impact across groups. Log how many records are flagged or altered per group, and define mitigation measures.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Anomaly flagging has no defined thresholds, handling of records that fail validation, or rules for blocking scoring. It also has no integrity checks against deliberately manipulated or adversarial inputs, so quality and robustness are not demonstrably met. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify validation rules, anomaly thresholds and fail-safe behaviour: block scoring or refer to manual review when critical fields fail validation. Add input integrity and tampering checks, and test them.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

**Recommendations:**

- Document data-preparation and cleaning practices and extend them to training, validation and testing data.
- Assess cleaning and imputation for group-level bias and define mitigations.
- Define anomaly thresholds, fail-safe handling for failed validation, and input integrity checks.

---

### FR-03

**Risk level:** high

**Requirement:** The system shall use a trained AI model to calculate a numeric credit score for each applicant, along with a risk category (e.g., low, medium, high), based on the processed applicant data.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 13 Transparency and provision of information to deployers (art:13); Article 11 Technical documentation (art:11)

**Analysis:** FR-03 defines the core credit scoring model but sets no accuracy or robustness targets, no pre-defined test metrics or thresholds, and no training-data governance requirements. A high-risk scoring function therefore has no declared performance level and nothing to test against before deployment.

**Risks:**

- FR-03 sets no required accuracy level or metrics (e.g., AUC, calibration, per-group error) for the score and risk category, so none can be declared in the instructions for use. FR-10 tracks performance but does not define or declare targets. [high] - Article 15(3) (`art:15:p3`)
  - Partly addressed by: FR-10 (ongoing tracking of accuracy and drift over time (15(1) consistency throughout lifecycle))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify accuracy metrics and minimum thresholds for the score and risk category, including calibration and per-group performance, and require them to be declared in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No requirement states that the scoring model is trained, validated and tested on governed datasets (representativeness, error-freeness, bias examination, design choices and assumptions). FR-02 cleans inference-time inputs only, and FR-07 monitors outputs rather than training data. [high] - Article 10(2) (`art:10:p2`)
  - Partly addressed by: FR-07 (detection of outcome disparities across protected groups (partial input to 10(2)(f)/(g)))
  - Category: `data_governance`
  - Action: Add requirements for documented training, validation and testing dataset governance: provenance, representativeness for the applicant population, bias examination and mitigation, and data gap identification.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement defines no pre-release testing against pre-defined metrics and probabilistic thresholds for the model, and no risk-based acceptance criteria for the score and category boundaries. [medium] - Article 9(8) (`art:9:p8`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Define pre-deployment test plans with metrics and acceptance thresholds for score accuracy, risk-category assignment and fairness. Link the results to the risk management file.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- No robustness or cybersecurity expectations are stated for the model, such as resilience to manipulated applicant inputs, adversarial examples, data or model poisoning, or feedback loops from retraining. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-02 (flagging anomalous input values before scoring (partial resilience to input errors, 15(4)))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add requirements for adversarial and robustness testing, input manipulation defences, protection of training data and model artefacts, and feedback-loop controls on retraining.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define and declare accuracy metrics and thresholds, including calibration and per-group performance, for the score and risk category.
- Add training, validation and testing dataset governance requirements covering provenance, representativeness and bias examination.
- Specify pre-deployment testing against pre-defined metrics and thresholds, tied to the risk management process.
- Add robustness and AI-specific security requirements: adversarial and poisoning defences, and feedback-loop controls on retraining.

---

### FR-04

**Risk level:** medium

**Requirement:** The system shall provide an explanation for each credit score, identifying the key factors and their relative influence on the result, in a form understandable to loan officers and applicants.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 86 Right to explanation of individual decision-making (art:86); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-04 provides per-score explanations with key factors and relative influence, which substantially supports interpretability. Remaining gaps are minor: the explanation's fidelity and limits are not specified, and it is not tied to the Article 13 instructions for use or to the Article 86 right to explanation.

**Risks:**

- The requirement does not state that the explanation must describe the AI system's role in the decision and the main elements of the decision; it covers score factors only. Applicant-facing explanation of the final decision (including after a human override) is left to FR-09's adverse action notice, which covers only declined applications. [medium] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-09 (principal reasons for declined applications in an adverse action notice)
  - Category: `transparency`
  - Action: Extend FR-04 so the applicant-facing explanation states the role of the AI score in the decision and the main elements of the final decision, including cases where a loan officer overrode the recommendation, and is available on request, not only on decline.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- The requirement does not specify explanation method, fidelity or limitations (e.g., how faithfully factor attributions reflect the model, or conditions where they are unreliable). The deployer-facing instructions for use must document the explanation capabilities and the information needed to interpret outputs. [low] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Define the explanation method and its validated fidelity and limitations, and include them in the instructions for use alongside accuracy metrics and guidance on interpreting the factors and their relative influence.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Extend FR-04 so applicant-facing explanations describe the AI system's role and the main elements of the final decision, including overrides and non-decline outcomes.
- Specify the explanation method, its fidelity testing and known limitations, and document them in the Article 13 instructions for use.

---

### FR-05

**Risk level:** medium

**Requirement:** The system shall generate a creditworthiness recommendation (approve, decline, or refer for manual review) by comparing the credit score and risk category against configurable lending policy thresholds.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-05 generates approve/decline/refer recommendations from configurable thresholds, but its wording sets no controls on who may change those thresholds, no threshold validation, and nothing to counter automation bias. Threshold changes can silently alter credit outcomes for natural persons without testing or traceability.

**Risks:**

- Configurable lending policy thresholds drive approve/decline outcomes, but the requirement defines no pre-defined metrics, testing or acceptance criteria for threshold changes and no residual-risk evaluation of their effect on applicants. [medium] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: FR-07 (outcome disparity monitoring across protected groups with alerts when limits are exceeded); FR-10 (model performance tracking, versioning and rollback)
  - Category: `risk_management`
  - Action: Require threshold changes to be tested against predefined metrics (accuracy, approval-rate disparity across groups) before release, with documented approval and residual-risk review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The recommendation output does not state that it is advisory, and the requirement has no automation-bias safeguard such as showing the score, thresholds applied and the reason for a 'refer' outcome next to the recommendation. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-06 (loan officer review, override and escalation of recommendations with documented justification (14(4)(d))); FR-04 (explanation of key factors behind the credit score, supporting interpretation of the output (14(4)(c)))
  - Category: `human_oversight`
  - Action: Present each recommendation as advisory with the score, risk category, applied threshold and triggering rule. Add reviewer guidance on over-reliance, and define the criteria for 'refer for manual review'.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(b))
- The threshold configuration and decision-rule logic are not required to be documented for deployers, including the default thresholds, the permitted ranges and their effect on accuracy and on groups of applicants. [low] - Article 13(3)(b) (`art:13:p3:b`)
  - Partly addressed by: FR-04 (explanation of factors behind the credit score for loan officers (13(3)(b)(iv)))
  - Category: `transparency`
  - Action: Document the recommendation logic, configurable parameters, defaults and the expected effect of threshold changes in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(b))

**Cited provisions:**

- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Gate threshold changes behind testing against predefined metrics, documented approval and residual-risk review.
- Label recommendations as advisory, show the applied threshold and rule, and define the criteria for 'refer for manual review'.
- Document the decision logic, configurable parameters and their effects in the instructions for use.

---

### FR-06

**Risk level:** medium

**Requirement:** The system shall allow authorized loan officers to review, override, or escalate AI-generated recommendations, requiring a documented justification for every override.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 12 Record-keeping (art:12); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-06 provides review, override and escalation with documented justification, which substantially covers Art. 14(4)(d). The remaining gaps are the lack of automation-bias safeguards and oversight competence/authority, plus no stop/interrupt capability.

**Risks:**

- No measures to make loan officers aware of automation bias or to help them interpret outputs and limitations, e.g. warnings, confidence indicators, or checks on override and acceptance rates. The requirement only enables override and does not support critical review of recommendations. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-04 (explanation of key factors that helps officers interpret the output (14(4)(c)))
  - Category: `human_oversight`
  - Action: Add UI prompts that surface model limitations, show the FR-04 explanation next to the recommendation before the officer acts, and track acceptance and override rates to detect over-reliance. Include automation-bias guidance in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- 'Authorized' loan officers are not defined by competence, training or authority, so oversight may be assigned to people who cannot meaningfully challenge the recommendation. [low] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Specify role-based access tied to documented training and competence, with authority to override without adverse consequences. Document these as deployer measures in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The requirement covers per-case override but gives no ability to halt or suspend the system's operation, such as a stop control or a fallback to fully manual processing, if anomalies or dysfunctions appear. [low] - Article 14(4)(e) (`art:14:p4:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-07 (alerting administrators on bias disparities, which can trigger intervention (14(4)(a) monitoring))
  - Category: `human_oversight`
  - Action: Add an authorized control to suspend AI recommendations, either globally or per segment, and move cases to manual review in a safe state. Log each use of this control.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.

**Recommendations:**

- Add automation-bias safeguards and interpretation aids to the review UI, and monitor acceptance and override rates.
- Define competence, training and authority criteria for officers authorized to do oversight.
- Add a stop/suspend control with a manual-processing fallback.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall monitor the model for bias and fairness by evaluating outcomes across protected demographic groups, excluding protected attributes (e.g., race, gender, religion) as scoring inputs, and alerting administrators when disparities exceed defined limits.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 14 Human oversight (art:14)

**Analysis:** FR-07 provides bias monitoring and protected-attribute exclusion, but it does not define the fairness metrics, the disparity limits, or any mitigation after an alert. It also ignores proxy variables and the use of protected data for bias evaluation, so discrimination risk in credit scoring could go undetected or unaddressed.

**Risks:**

- Alerts are raised when disparities exceed limits, but the requirement defines no fairness metrics or acceptance thresholds, and no mitigation or remediation workflow (e.g., retraining, rollback, threshold adjustment) follows an alert. [medium] - Article 10(2)(g) (`art:10:p2:g`)
  - Partly addressed by: FR-10 (controlled retraining, versioning and rollback that could serve as a mitigation mechanism)
  - Category: `data_governance`
  - Action: Specify fairness metrics (e.g., demographic parity difference, equalized odds), numeric disparity limits with rationale, and a documented response workflow (investigation, mitigation, retraining or rollback, re-test) triggered by alerts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(g))
- Excluding protected attributes as scoring inputs does not address proxy variables (e.g., postcode, employment history) that correlate with protected groups. The requirement also does not say how the group data needed for outcome evaluation is lawfully sourced and governed. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add proxy and feature-correlation analysis for the training, validation and testing data, and define a governed, access-restricted source of demographic labels used only for bias evaluation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(g))
- Bias evaluation is described as ongoing monitoring only. There is no pre-deployment bias testing against predefined metrics and thresholds, and no integration into a documented risk management process for discrimination risks to fundamental rights. [medium] - Article 9(8) (`art:9:p8`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Add pre-release bias testing against predefined fairness metrics and thresholds, and record bias risks, residual risk acceptance and mitigation measures in the risk management file.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Fairness results are not tied to a post-market monitoring plan: it is unspecified how often evaluation runs, how results are documented, or whether they feed compliance evaluation over the system's lifetime. [low] - Article 72(2) (`art:72:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-10 (tracking of model performance over time (accuracy, drift, default prediction rates))
  - Category: `post_market_monitoring`
  - Action: Define evaluation cadence, retention of fairness reports, and inclusion of fairness metrics in the post-market monitoring plan within the technical documentation.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems

**Cited provisions:**

- **Data and data governance, Article 10(2)(g)**
  > (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f);
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.

**Recommendations:**

- Define fairness metrics, numeric disparity limits and an alert-triggered mitigation workflow.
- Add proxy-variable analysis and governed sourcing of demographic labels for bias evaluation.
- Add pre-deployment bias testing against predefined thresholds and record bias risks in the risk management file.
- Include fairness metrics, cadence and reporting in the post-market monitoring plan.

---

### FR-08

**Risk level:** medium

**Requirement:** The system shall maintain an immutable audit log of all inputs, model versions, scores, explanations, recommendations, and human overrides to support regulatory compliance and dispute resolution.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-08 provides an immutable audit log of inputs, model versions, scores, explanations, recommendations and overrides, which substantially meets Art. 12/19 record-keeping. Remaining gaps are an unspecified retention period and no stated logging of events relevant to risk identification and post-market monitoring.

**Risks:**

- No retention period is specified for the immutable audit log; Art. 19/26(6) require retention appropriate to the purpose and at least six months, and 'immutable' storage may conflict with GDPR erasure and storage-limitation requirements. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Define a log retention policy (minimum 6 months, aligned to financial services record rules and GDPR), with a documented approach to personal data in immutable logs (e.g. pseudonymisation or crypto-shredding) and a defined expiry.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The logged event set covers decision data but not events that support identifying risk situations, post-market monitoring and deployer monitoring (e.g. anomaly or data-quality flags, bias alerts, drift or performance alerts, system errors, usage periods). [low] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-06 (override events with documented justification supply human-intervention data to the log); FR-10 (model performance and drift tracking produces monitoring events relevant to Art. 12(2)(b))
  - Category: `record_keeping`
  - Action: Extend the log schema to include session start/end timestamps, data-validation flags, bias and drift alerts, model errors and the identity of the reviewing officer, and state that the logs feed post-market monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Specify the log retention period and reconcile immutability with GDPR erasure and minimisation.
- Broaden the logged event types to cover risk-relevant, monitoring and usage-period events and identify the human reviewer.

---

### FR-09

**Risk level:** high

**Requirement:** The system shall enable applicants to access the data used in their assessment, request corrections, and contest decisions, and shall generate adverse action notices stating the principal reasons for any declined application.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10)

**Analysis:** FR-09 provides access, correction, contestation and adverse action notices, which largely implements Art. 86 explanation rights. Remaining gaps: the notice does not state the AI system's role in the decision, and applicants are never told up front that an AI system is used.

**Risks:**

- Adverse action notices state only 'principal reasons' and do not explain the AI system's role in the decision-making procedure or the main elements of the decision, as Art. 86(1) requires. Approved or referred applicants, and the human officer's override role, are not covered either. [medium] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-04 (key factors and their relative influence on the score, understandable to applicants (partial content of the explanation))
  - Category: `transparency`
  - Action: Extend the notice and explanation-on-request content to state the role of the AI score/recommendation versus loan officer judgment (including any override), the main decision elements, and how to obtain a human review. Make this available to any applicant with a significantly adverse decision, not only declined ones.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- No requirement informs applicants, at or before application, that they are subject to an AI-based credit assessment. FR-09 only acts after a decision and on request. [high] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a requirement to show a clear notice at application intake that an AI system is used to evaluate creditworthiness, and record that the notice was delivered.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Expand adverse action notices and explanations to cover the AI system's role in the decision, the main decision elements, and the human review route.
- Add an applicant-facing disclosure at intake that an AI system is used in the credit assessment.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall track model performance over time (e.g., accuracy, drift, default prediction rates) and support controlled retraining, versioning, and rollback of models by authorized administrators.

**Classified as:** Annex III point 5(b) (annex:III:5:b): (b) AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud;

**Articles selected from the index:** Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 17 Quality management system (art:17); Article 9 Risk management system (art:9); Article 12 Record-keeping (art:12)

**Analysis:** FR-10 tracks performance, drift and supports retraining/rollback, but does not define a post-market monitoring system/plan, does not address feedback-loop risk from retraining, and lacks validation criteria for retrained models. Without these, continuous compliance over the lifecycle cannot be evidenced.

**Risks:**

- Performance tracking is not tied to a documented post-market monitoring system and plan that collects and analyses data (including deployer-provided data) to evaluate continuous compliance with Chapter III Section 2. [medium] - Article 72(2) (`art:72:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-07 (ongoing monitoring of outcomes across protected groups, with alerts, as part of performance data collection); FR-08 (audit log of inputs, scores and model versions as data source for monitoring)
  - Category: `post_market_monitoring`
  - Action: Define a documented post-market monitoring plan (part of Annex IV documentation) specifying metrics, data sources incl. deployer feedback, thresholds, review cadence and how results evaluate compliance; link FR-10 metrics to it.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
- Retraining is allowed but no mitigation is specified against biased outputs feeding back into training data (feedback loops), e.g. decisions and overrides becoming future training labels. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-07 (bias and fairness evaluation of outcomes across protected groups)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add retraining controls: assess selection bias from past approve/decline outcomes, use bias checks on retraining data and a bias gate before release.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No pre-deployment testing against predefined metrics and thresholds is required for retrained models before they replace the production version; accuracy/drift acceptance limits are not defined. [medium] - Article 9(8) (`art:9:p8`)
  - Category: `risk_management`
  - Action: Require retrained models to pass validation against predefined accuracy, robustness, drift and fairness thresholds before promotion, with approval recorded and rollback triggers defined.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- Controlled retraining and versioning lack specified change-management and documentation procedures for modifications, and administrator authorization is not tied to logged approvals. [low] - Article 17(1)(a) (`art:17:p1:a`)
  - Partly addressed by: FR-08 (immutable audit log records model versions used)
  - Category: `quality_management`
  - Action: Record retraining, version promotion and rollback events with approver identity and rationale, and assess whether each change is a substantial modification needing reassessment.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(a))

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Quality management system, Article 17(1)(a)**
  > (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system;

**Recommendations:**

- Create a documented post-market monitoring plan linking FR-10 metrics, data sources and review cadence to continuous compliance evaluation.
- Add feedback-loop mitigation and bias gating to the retraining process.
- Define predefined acceptance thresholds and a validation gate for retrained models before promotion.
- Log retraining/promotion/rollback approvals and add a substantial-modification assessment step.

---
