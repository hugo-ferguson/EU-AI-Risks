# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 9

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 9 as high risk. The main review focus areas are other, transparency, accuracy robustness cybersecurity, data governance and risk management. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 9 high, 0 medium, 0 low.
- Most frequent mapped obligation areas: other (8), transparency (7), accuracy robustness cybersecurity (6), data governance (4), risk management (4).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** high

**Requirement:** The system shall capture a user’s facial video or image input through the device camera while the user browses adult-content material on the platform.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-01 captures facial images/video as the input to a system that infers sexual preference (sex life/orientation) from biometric data, and emotions. This falls under the Article 5(1)(g) prohibition on biometric categorisation inferring sex life or sexual orientation. Consent and encryption controls elsewhere do not remove the prohibition.

**Risks:**

- The captured facial data is the biometric input for a system that categorises individuals to infer sexual preference/orientation (sex life), a prohibited practice under Article 5(1)(g); consent in FR-09 does not lift the prohibition. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy facial capture for inferring sexual preference or orientation. Remove FR-01 and the dependent FR-02/03/04 chain, or redefine the purpose so no biometric inference of sex life or orientation occurs, and obtain legal review.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- The requirement does not state that users are informed they are interacting with an AI system that analyses their face at the time capture begins; FR-09 covers only a consent request, not AI-interaction disclosure. [medium] - Article 50(1) (`art:50:p1`)
  - Partly addressed by: FR-09 (explicit consent request shown before camera capture begins (partial: consent, not AI-interaction disclosure))
  - Category: `transparency`
  - Action: Add a clear notice, shown before or at first camera activation, that an AI system is analysing the user's face and what it infers, conforming to accessibility requirements.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- The requirement sets no input-quality criteria for captured video/images (e.g. lighting, occlusion, spoofing or injected feeds), so unreliable or manipulated input can corrupt downstream inferences. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify camera input integrity checks (liveness/anti-spoofing, quality thresholds, rejection of injected streams) and robustness tests for degraded capture conditions.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Remove or fundamentally redesign the sexual-preference inference purpose, since it is prohibited under Article 5(1)(g); obtain legal review before any further development.
- Add an AI-interaction and facial-analysis notice at first camera activation, in addition to the FR-09 consent.
- Define capture-input integrity, liveness and quality requirements, with robustness tests.

---

### FR-02

**Risk level:** high

**Requirement:** The system shall detect and extract facial features and expressions (e.g., micro-expressions, gaze direction, pupil dilation, and emotional valence) from the captured input in real time.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-02 extracts facial features and emotional responses in real time as the first stage of a pipeline that infers sexual preference categories, which is a prohibited biometric categorisation practice under Art. 5(1)(g) (inference of sex life or sexual orientation). The requirement also lacks accuracy, data governance and transparency controls for emotion recognition. Prohibition risk dominates and cannot be fixed by controls alone.

**Risks:**

- The facial and expression extraction feeds a pipeline (FR-03/FR-04) that categorises individuals by biometric data to infer sex life or sexual orientation, which falls under the Art. 5(1)(g) prohibition, so the system as specified cannot be lawfully placed on the market or used in the EU. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Remove or redesign the feature chain so that biometric and facial data are not used to infer sexual preference or orientation. Escalate to legal/compliance before further development. Consent (FR-09) and age verification (FR-08) do not lift the prohibition.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- The requirement does not define accuracy or robustness targets for extracting micro-expressions, gaze, pupil dilation and emotional valence, so reliability across lighting, camera quality, demographics and spoofing is unspecified. [medium] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify accuracy and robustness metrics and thresholds for feature and emotion extraction. Test across demographic groups and capture conditions, and declare the metrics in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement says nothing about the training, validation and testing data for the extraction models, such as provenance, labelling of emotional valence, representativeness and bias examination across demographic groups. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Document dataset origin, labelling assumptions about what expressions represent, and bias examination and mitigation for the extraction models. Set representativeness acceptance criteria.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(c))
- Real-time emotion and biometric analysis of users is not tied to any notice that the individuals are subject to a high-risk AI system. FR-09 covers consent but not disclosure of the system's emotion-recognition operation. [low] - Article 26(11) (`art:26:p11`)
  - Partly addressed by: FR-09 (explicit consent request before camera capture and ability to disable analysis)
  - Category: `transparency`
  - Action: Add a clear notice at first interaction that facial and emotion analysis is performed by an AI system, covering what is extracted and why. Align it with the FR-09 consent flow.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Eliminate the sexual-preference inference chain and obtain legal review, since this is a prohibited practice under Art. 5(1)(g).
- Define and declare accuracy and robustness metrics for facial and emotion extraction.
- Document data governance and bias examination for the extraction model datasets.
- Add explicit AI-system and emotion-analysis disclosure at first interaction, linked to the FR-09 consent flow.

---

### FR-03

**Risk level:** high

**Requirement:** The system shall use a trained machine-learning model to map the extracted facial-expression data to inferred sexual preference categories for each user.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** FR-03 infers sexual preference categories from facial biometric data. This is biometric categorisation of sex life or sexual orientation, prohibited under Art. 5(1)(g), and consent (FR-09) or age verification (FR-08) cannot make it compliant. Beyond the prohibition, the requirement has no data governance or accuracy provisions for the model.

**Risks:**

- The requirement maps facial biometric data to inferred sexual preference categories. This is biometric categorisation to infer sex life or sexual orientation, a prohibited practice that cannot be placed on the market or used. FR-09 consent and FR-08 age verification do not lift the prohibition. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - Category: `other`
  - Action: Remove or redesign FR-03 so no biometric data is used to infer sexual orientation or sex life, and drop the dependent profile functions (FR-04, FR-05, FR-06). Seek legal review before any further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(g))
- The ML model has no stated training, validation or testing data governance. The ground truth for 'sexual preference' labels from facial expressions is undefined, so the assumptions, label validity, bias examination and mitigation are unspecified. Expression-to-preference inference has no scientific validity, and bias across demographics risks discrimination. [high] - Article 10(2) (`art:10:p2`)
  - Category: `data_governance`
  - Action: If any categorisation survives legal review, document dataset provenance, labelling method, assumptions about what the data measure, and bias examination and mitigation across demographic groups.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No accuracy or robustness metrics, thresholds or error handling are specified for the inference model. Misclassification of sensitive attributes could harm individuals, and the accuracy levels are not declared in the instructions of use. [medium] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics and acceptance thresholds for the model, test robustness across demographic groups and capture conditions, and declare the levels in the instructions of use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No risk management process covers the fundamental-rights risks of inferring sensitive characteristics, such as privacy, discrimination, outing and exposure of profiles. This risk analysis and testing is a system-level gap. [medium] - Article 9(2) (`art:9:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented risk management process that identifies and evaluates fundamental-rights risks of the inference and defines tested mitigation measures.
  - Trace:
    - referenced by Article 9(5) (Article 9(2)(d))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).

**Recommendations:**

- Remove or redesign FR-03 so it does not infer sexual orientation or sex life from biometric data, and obtain legal review before proceeding.
- If any inference remains in scope, document dataset provenance, label validity, and bias detection and mitigation.
- Define and declare accuracy and robustness metrics with acceptance thresholds, tested across demographic groups.
- Set up a risk management process covering fundamental-rights harms from sensitive-attribute inference.

---

### FR-04

**Risk level:** high

**Requirement:** The system shall maintain a user preference profile that is updated continuously as new facial-expression data is analyzed across sessions.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 12 Record-keeping (art:12); Article 9 Risk management system (art:9)

**Analysis:** FR-04 continuously updates a profile of inferred sexual preferences from facial-expression data. That is biometric categorisation inferring sex life or sexual orientation, which Art. 5(1)(g) prohibits, so the requirement cannot be made compliant by adding controls. It also creates an unmitigated feedback loop and has no bias, accuracy or logging controls.

**Risks:**

- The continuously updated profile stores inferences about sex life or sexual orientation derived from biometric data (facial expressions). This is a prohibited biometric categorisation practice, and the cross-session profile makes it persistent. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Remove the profile update from facial-expression-derived sexual-preference inference. Escalate to legal review and redesign the feature to use only explicit, user-provided preferences or non-biometric signals.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
- The profile is updated continuously from the model's own inferences, and those inferences drive recommendations (FR-05/FR-06) that shape later behaviour and inputs. No mitigation is specified for biased outputs feeding back into future updates. [high] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: If the profile is retained in any form, define feedback-loop controls: bounded update rates, decay or reset of the profile, drift monitoring, and exclusion of model-inferred labels from retraining or update inputs without validation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The continuous update has no specified data governance: no bias examination for the data the profile accumulates, no data-quality criteria, and no handling of the sensitive-inference error and discrimination risk, especially where outputs influence future inputs. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Document the data origin, labelling assumptions and bias examination for the profile data. Add bias detection and mitigation measures and acceptance criteria for profile updates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(a))
- The profile is updated automatically across sessions, but no event logging is specified for updates, which weakens traceability and the identification of risk situations. [medium] - Article 12(2)(a) (`art:12:p2:a`)
  - Partly addressed by: FR-07 (encrypted, access-controlled storage of inferred preference profiles (storage only, not event logging))
  - Category: `record_keeping`
  - Action: Log each profile update (timestamp, model version, input reference, change delta) in tamper-evident, access-controlled logs. Retain them under a defined retention period consistent with deletion rights in FR-09.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(a))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Record-keeping, Article 12(2)(a)**
  > (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification;

**Recommendations:**

- Do not build the sexual-preference inference profile. Obtain legal review and redesign around explicit user-provided preferences.
- If any profile persists, add feedback-loop mitigation: bounded updates, decay/reset, and drift monitoring.
- Define data governance and bias examination for profile data, with acceptance criteria.
- Add automatic logging of every profile update with model version and retention rules.

---

### FR-05

**Risk level:** high

**Requirement:** The system shall match each user’s inferred preference profile against a catalogue of tagged adult-content items and generate a ranked list of personalized recommendations.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-05 turns profiles inferred from facial biometrics (sexual preference categories) into personalized recommendations. This falls squarely within the Art. 5(1)(g) prohibition on biometric categorisation that infers sex life or sexual orientation, so the requirement cannot be remediated with controls and should not be built as specified. Even setting that aside, it has no stated transparency, bias, or risk controls.

**Risks:**

- Recommendations are generated from a profile of sexual preference categories inferred from facial biometric data (FR-02/03/04). This is biometric categorisation to infer sex life or sexual orientation, a prohibited practice, and FR-05 operationalises the output. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not deploy this pipeline. Remove biometric-derived sexual-preference inference and base recommendations on non-biometric signals such as explicit user choices or viewing history. Have legal counsel confirm the redesigned scope.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(g))
- Ranking and profile matching on inferred sensitive attributes are not accompanied by any bias examination or mitigation, such as error rates across demographic groups, or feedback loops where recommendations influence future inferred profiles. This risks discriminatory or harmful outcomes. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: If any profiling remains after redesign, document bias examination of the training and matching data, including feedback-loop effects, and define mitigation and acceptance criteria.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Nothing in FR-05 makes the ranking logic interpretable to deployers or documents the accuracy limits of the inferred profile. Emotion-to-preference inference has weak validity, and no instructions for use cover its limitations. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Produce instructions for use stating the intended purpose, accuracy metrics, known limitations and misuse risks. Expose the ranking factors to deployers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- No human oversight capability is specified for the recommendation function. There is no way to disregard or override the profile-driven ranking, or to stop the profiling. [medium] - Article 14(4)(d) (`art:14:p4:d`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-09 (user can disable analysis and delete inferred profiles (a user-side control, not deployer oversight))
  - Category: `human_oversight`
  - Action: Add operator controls to disable profile-based ranking, fall back to non-inferred ranking, and review or override the profile. Add a stop mechanism.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;

**Recommendations:**

- Remove biometric inference of sexual preference and redesign recommendations on non-biometric inputs.
- Document bias examination and mitigation for any retained profiling, including feedback loops.
- Provide instructions for use covering accuracy, limitations and the ranking rationale.
- Add deployer-level override, disable and stop controls for profile-based ranking.

---

### FR-06

**Risk level:** high

**Requirement:** The system shall display the ranked recommendations to the user through the platform interface and refresh them dynamically as the user’s inferred preferences change.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-06 delivers recommendations driven by sexual-preference inference from facial biometrics, which Art. 5(1)(g) prohibits (biometric categorisation inferring sex life or sexual orientation). The display and dynamic refresh layer has no AI-interaction disclosure, no explanation or oversight interface, and no override, so it carries the prohibited output to the user.

**Risks:**

- The requirement operationalises output from biometric categorisation that infers sexual preferences or sexual orientation from facial data, which falls under the Art. 5(1)(g) prohibition. Displaying and refreshing these recommendations is use of the prohibited system, and no other requirement removes or restricts that inference. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Escalate to a legal/compliance decision before build. Remove or redesign the facial-expression-to-sexual-preference inference chain (FR-02/03/04/05) so that FR-06 does not consume biometric-derived sexual preference or orientation inferences. Use only explicit, user-provided preferences or non-biometric behavioural signals.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(c))
- The interface gives no clear notice at first exposure that recommendations are AI-generated from inferred, live-updating emotional and biometric analysis. Users cannot tell that their reactions are driving changes to what they see. [high] - Article 50(1) (`art:50:p1`)
  - Partly addressed by: FR-09 (explicit consent request before camera capture, which informs the user that analysis occurs)
  - Category: `transparency`
  - Action: Add a persistent, accessible UI notice, shown at or before first interaction, stating that an AI system analyses facial responses to personalise and refresh recommendations. Show a visible indicator whenever dynamic refresh is driven by inferred preferences.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- Recommendations refresh automatically with no interface tools for users or operators to understand why items are shown, to disregard or reverse the inferred-preference output, or to pause the dynamic refresh. This risks automation bias and a feedback loop that reinforces inferred sensitive profiles. [medium] - Article 14(4)(d) (`art:14:p4:d`)
  - Partly addressed by: FR-09 (user can disable analysis at any time (partial stop capability, 14(4)(e)))
  - Category: `human_oversight`
  - Action: Add UI controls to dismiss or reset recommendations, pause dynamic refresh, and revert to non-inferred browsing. Give operators a stop mechanism and an interpretable view of what drives each refresh. Log refresh events.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement does not tell deployers how to interpret the displayed output. Nothing documents the limits and accuracy of inferring preferences from expressions, or the foreseeable fundamental-rights risks of continuous profile-driven refresh. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Document in the instructions for use the accuracy metrics, limitations and refresh behaviour, and the foreseeable fundamental-rights risks of the recommendation output. Expose interpretability info to deployers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(c))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;
- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;

**Recommendations:**

- Block or redesign the sexual-preference inference pipeline feeding FR-06 pending a legal decision under Art. 5(1)(g).
- Add a clear, accessible AI-use notice in the recommendation UI at first exposure, and show it again when refresh is driven by inferred preferences.
- Provide user and operator controls to override, reset, pause refresh and stop the system, plus an explanation of why each item is shown.
- Document the output interpretation guidance, accuracy limits and fundamental-rights risks in the instructions for use.

---

### FR-07

**Risk level:** high

**Requirement:** The system shall store captured facial data, inferred preference profiles, and recommendation history in encrypted, access-controlled storage.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 12 Record-keeping (art:12); Article 9 Risk management system (art:9)

**Analysis:** FR-07 provides encrypted, access-controlled storage, which is a partial cybersecurity control. However, it does not cover AI-specific attacks (e.g. confidentiality attacks) or define storage-level logging. The system as a whole infers sexual orientation from biometric data, which Art 5(1)(g) prohibits; this is a system-level issue that storage controls cannot fix.

**Risks:**

- The system infers sexual preference categories from facial biometric data, which falls under the Art 5(1)(g) prohibition on biometric categorisation to infer sex life or sexual orientation. FR-07 persists the prohibited biometric data and profiles, and no requirement removes or limits this practice. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Escalate to legal and product owners. Do not store or build profiles that infer sexual orientation or sex life from biometric data. Redesign or remove the inference function (FR-02, FR-03, FR-04) and drop storage of those profiles in FR-07.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- 'Encrypted, access-controlled' is unspecific. FR-07 sets no cybersecurity measures against confidentiality attacks, model or profile exfiltration, or tampering with stored profiles and history that would alter outputs. Breach of this extremely sensitive data could cause severe harm. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify encryption at rest and in transit, key management, role-based access, integrity protection of stored profiles, and anomaly detection for access. Add threat-model coverage for confidentiality attacks and manipulation of stored profiles. Add backup and fail-safe recovery requirements.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- FR-07 does not require logging of access to, or changes in, stored facial data and profiles. This limits traceability for identifying risk situations and for post-market monitoring. [low] - Article 12(2) (`art:12:p2`)
  - Category: `record_keeping`
  - Action: Add automatic, tamper-evident logging of access, modification, export and deletion events on the stored biometric data and profiles, with defined retention.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(c))
- The SRS has no risk management process covering the risks of storing sensitive inferred profiles, such as leakage, profiling harm, or adverse impact on vulnerable persons. [medium] - Article 9(1) (`art:9:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented risk management process that includes the data-at-rest hazards, residual-risk acceptance, and testing against predefined metrics.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Risk management system, Article 9(1)**
  > 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.

**Recommendations:**

- Resolve the Art 5(1)(g) prohibition first: remove or redesign sexual-preference inference and stop storing those profiles.
- Define concrete security controls (encryption, key management, access, integrity, resilience) and a threat model including confidentiality attacks.
- Add tamper-evident access and change logging for stored biometric data and profiles.
- Establish a documented risk management system covering storage and retention of sensitive inferred data.

---

### FR-08

**Risk level:** high

**Requirement:** The system shall verify that users are adults through an age-verification mechanism before enabling camera capture or any recommendation features.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9)

**Analysis:** FR-08 adds an age gate, which is a useful control for the minors' consideration in Article 9(9). However, it does not address that the system as a whole appears to fall under the Article 5(1)(g) prohibition on biometric categorisation inferring sexual orientation or sex life, and that age verification is not part of a risk management process.

**Risks:**

- The system infers sexual preference categories from facial biometric data, which falls within the prohibited practice of biometric categorisation to infer sex life or sexual orientation. An age gate in FR-08 does not remove this prohibition, so the system as specified cannot be lawfully placed on the market or used. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Escalate to legal/compliance before further development. Remove or redesign the sexual-preference inference from biometric data (FR-02, FR-03, FR-04) rather than gating it behind age verification.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- FR-08 specifies only that users are verified as adults. It gives no accuracy or failure-handling criteria, no handling of bypass, spoofing or misclassification of minors, and no documented risk assessment of adverse impact on under-18s. Because camera capture and emotion/biometric profiling of a minor would be especially harmful, this control needs defined acceptance criteria. [medium] - Article 9(9) (`art:9:p9`)
  - Category: `risk_management`
  - Action: Document the minor-impact risk in the risk management file. Define target false-accept rates for the age check, anti-spoofing/bypass controls, a re-verification policy, and a fail-closed behaviour that blocks capture and recommendations when verification fails or is inconclusive. Test against these thresholds before release.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The age-verification mechanism is an input-gating control whose robustness against circumvention (for example spoofed documents, shared accounts, or replayed sessions) and against tampering is unspecified. A weak gate would expose minors to camera capture and profiling. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify resilience requirements for the age-verification mechanism: server-side enforcement before any capture or recommendation API is enabled, liveness/anti-spoofing checks, session binding, and logging of verification outcomes with alerts on abnormal bypass attempts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Risk management system, Article 9(9)**
  > 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Treat the sexual-orientation/sex-life inference as a potential Article 5(1)(g) prohibition and resolve it with legal review before building on FR-08.
- Add measurable accuracy, fail-closed and re-verification criteria for age verification, and record the under-18 risk in the risk management system.
- Define anti-spoofing and server-side enforcement requirements so camera capture and recommendations cannot be reached without a passed age check.

---

### FR-09

**Risk level:** high

**Requirement:** The system shall present users with an explicit consent request before camera capture begins, and shall allow users to withdraw consent, disable analysis, and delete their stored facial data and inferred profiles at any time.

**Classified as:** Annex III point 1(b) (annex:III:1:b): (b) AI systems intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics;; Annex III point 1(c) (annex:III:1:c): (c) AI systems intended to be used for emotion recognition.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14)

**Analysis:** FR-09 supplies consent, withdrawal and deletion controls, but it cannot make the system lawful: inferring sexual preference from facial biometrics is a prohibited practice under Art. 5(1)(g), which consent does not cure. The requirement also does not inform users that an AI system is analysing their emotions and biometrics, and does not set out what that analysis involves.

**Risks:**

- The system categorises individuals from facial biometric data to infer sexual orientation or sex life (sexual preference categories). This is prohibited under Art. 5(1)(g), and the Act provides no consent exception, so the FR-09 consent flow does not make the practice permissible. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Escalate to a legal and product decision to remove or redesign the biometric inference of sexual preference (FR-02, FR-03, FR-04). Do not rely on user consent as a compliance basis for this feature.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- FR-09 requests consent before capture but does not require clear disclosure that an AI system is analysing facial expressions and emotions, or what is inferred and how it is used. Consent without this information is not informed, and Art. 50 requires users to be told when they interact with an AI system. [medium] - Article 50(5) (`art:50:p5`)
  - Category: `transparency`
  - Action: Extend the consent request to state, in clear and accessible language and before the first capture, that AI-based emotion and biometric analysis is performed. It should also state which categories are inferred, how they are used for recommendations, and how to withdraw consent.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- The deployer must inform natural persons that they are subject to a high-risk Annex III system (emotion recognition, biometric categorisation) that assists in decisions about them. FR-09 does not specify notice of this high-risk use or of the effect of the inferred profile on the recommendations they receive. [low] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Add to the consent notice an explicit statement that the user is subject to a high-risk emotion-recognition and biometric-categorisation system, and that the inferred profile drives the recommendations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Remove or redesign the sexual-preference inference from facial biometrics; consent does not legitimise a prohibited practice.
- Make the consent screen disclose the AI emotion and biometric analysis, the inferred categories, their use, and the withdrawal and deletion options.
- Add a deployer notice that the user is subject to a high-risk Annex III system whose inferred profile influences their recommendations.

---
