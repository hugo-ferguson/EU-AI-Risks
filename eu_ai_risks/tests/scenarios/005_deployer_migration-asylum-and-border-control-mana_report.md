# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 3
- Medium: 6

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 3 as high risk and 6 as medium risk. The main review focus areas are accuracy robustness cybersecurity, data governance, human oversight, record keeping and transparency. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 3 high, 6 medium, 0 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (17), data governance (4), human oversight (4), record keeping (2), transparency (2).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** medium

**Requirement:** The system shall capture travel document data by scanning the passport’s visual inspection zone (VIZ), machine-readable zone (MRZ), and embedded chip, and by accepting images taken under visible, infrared, and ultraviolet light.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** FR-01 is a data-capture requirement that feeds downstream AI forgery detection and risk scoring. It names no input-quality, robustness or tamper-resistance controls for captured images and chip reads, and no per-modality accuracy targets. Poor or manipulated captures could silently degrade outputs for affected travelers.

**Risks:**

- No integrity or adversarial-input controls for captured images and scans (e.g., spoofed, injected or manipulated IR/UV/visible images, or tampered scanner feeds) that feed the AI models. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-03 (verifies chip data authenticity and integrity via digital signatures, protecting the chip-read input)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify authenticated capture devices, tamper-evident image provenance, and input checks for injected or adversarial images. Add detection of anomalous captures before they reach AI models.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No error-handling or quality requirements for capture (poor lighting, damaged or worn passports, failed chip reads, unreadable MRZ) and no fail-safe behaviour, so errors may propagate into forgery detection and scoring. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-02 (flags inconsistencies between MRZ/VIZ/chip data, which partly detects faulty reads)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define capture-quality thresholds, rejection and re-capture flows, and fallback to manual inspection when a modality fails. Flag low-quality input in the result passed to the officer.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not specify input data characteristics (image resolution, wavelength ranges, document types and variants) or the diversity of documents and capture conditions that the AI models must handle, which is needed for representative data sets and for the input-data specifications in the instructions for use. [low] - Article 10(4) (`art:10:p4`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: Document supported document types, issuing states, capture conditions and input specifications. Make sure the training, validation and testing data reflect them, and include them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(4)**
  > 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

**Recommendations:**

- Add capture-source authentication, image provenance and adversarial/injection detection to FR-01.
- Define capture quality thresholds, re-capture handling and manual fallback for failed or degraded scans.
- Document input specifications and supported document and condition coverage, and align training and test data with them.

---

### FR-02

**Risk level:** medium

**Requirement:** The system shall extract and cross-validate the data from the MRZ, VIZ, and RFID chip, including checking MRZ check digits and flagging any inconsistencies between the printed data and the electronically stored data.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 9 Risk management system (art:9)

**Analysis:** FR-02 is a deterministic cross-validation function (MRZ check digits, VIZ/chip consistency). It does not state how inconsistency flags handle OCR/read errors or tampered inputs, and it sets no accuracy targets. The main gap is under Article 15, where the declared accuracy and error-handling behaviour is unspecified.

**Risks:**

- No accuracy or error-rate metrics are defined for MRZ/VIZ OCR extraction and cross-field matching, so false inconsistency flags and missed mismatches are unmeasured and cannot be declared in the instructions for use. [medium] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics and acceptance thresholds for extraction and cross-validation (e.g. OCR character error rate, false mismatch rate, missed mismatch rate). Test them on varied document types and capture conditions, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not say how the system behaves on unreadable MRZ, degraded VIZ, chip read failure, or partial data. It also does not say how benign read errors are told apart from real tampering, so it is unclear whether the system fails safe or silently passes or rejects. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify fault-handling behaviour: distinguish 'unreadable' from 'inconsistent', define fallback and retry paths, and require that failed reads or checks always route to manual officer review rather than defaulting to a pass.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement says nothing about the integrity of the extracted MRZ/VIZ/chip data that feeds the cross-checks. Check-digit validation does not protect against deliberately crafted inputs that pass the checks, such as forged data or adversarial images. [low] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-03 (verifies chip digital signatures and certificate chain to detect altered chip data)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add input validation and tamper-resistance requirements for the capture and extraction pipeline, and test with adversarial and forged samples. Chip authenticity is handled by FR-03, so reference it.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define and declare accuracy metrics and thresholds for extraction and cross-validation, and test them across document types and capture conditions.
- Specify fail-safe handling for unreadable, partial, or inconsistent reads, with mandatory routing to officer review.
- Add input-integrity and adversarial testing requirements for the extraction pipeline, building on FR-03 for chip authenticity.

---

### FR-03

**Risk level:** medium

**Requirement:** The system shall verify the chip’s digital signatures and certificate chain against trusted issuing-authority certificates (e.g., the ICAO Public Key Directory) to confirm that the chip data is genuine and has not been altered.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 11 Technical documentation (art:11); Article 17 Quality management system (art:17); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-03 is itself a cybersecurity/integrity control (chip signature and certificate chain verification), so its core is sound. Remaining gaps: no specified behaviour when verification fails or trust anchors are unavailable, and no declared verification performance or robustness metrics.

**Risks:**

- The requirement does not define fail-safe behaviour when certificate verification cannot complete (expired or revoked certificates, missing PKD/CSCA entries, unreachable trust-store, malformed chip data), so errors could silently pass or be mis-scored as forgery. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify distinct outcomes for 'invalid signature', 'verification unavailable' and 'unsupported chip/certificate', never defaulting to 'genuine'. Require trust-store update, CRL/revocation handling and offline fallback. Pass the outcome explicitly to the risk score (FR-07).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Trust-anchor handling (source, update, integrity of the ICAO PKD/CSCA certificates) and resilience against manipulated chip inputs (malformed certificates, parser attacks) are not specified, leaving the verification step open to tampering by unauthorised parties. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-09 (encryption of stored and transmitted data and role-based access control, which protect the system's data and access but not the verification trust anchors)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require authenticated, integrity-protected trust-store distribution, strict input validation and fuzz testing of the chip data/certificate parser, and monitoring for verification-bypass attempts.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No accuracy metrics (e.g., false reject/accept rate of signature verification across chip types and issuing states) are defined or to be declared in the instructions for use. [low] - Article 15(3) (`art:15:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define verification success/failure metrics per document type and issuer, test them before release, and include them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.

**Recommendations:**

- Define fail-safe outcomes and error handling for verification failures and unavailable trust anchors, and pass them explicitly to the risk score.
- Specify secure trust-store provisioning, revocation checking, and robust parsing/fuzz testing of chip data and certificates.
- Declare verification accuracy metrics per chip type and issuing state in the instructions for use.

---

### FR-04

**Risk level:** high

**Requirement:** The system shall analyze the document’s physical and visual security features, such as holograms, watermarks, microprinting, fonts, laminate integrity, and photo substitution, and use AI models to detect signs of forgery, tampering, or counterfeiting.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14)

**Analysis:** FR-04 specifies AI forgery detection but sets no accuracy or robustness targets, no resilience to adversarial or degraded document images, and no governance of the training data for forgery and counterfeit samples. Without these, false positives or missed forgeries can lead to wrongful refusals of travelers or admission on forged documents.

**Risks:**

- No accuracy metrics or performance thresholds (false accept/reject rates per security feature) are defined for the forgery/tampering detection models, so an appropriate level of accuracy cannot be verified or declared. [high] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test per-feature and overall detection metrics (FAR/FRR, per document type and issuing state) with acceptance thresholds. Record the metrics for the instructions for use (Art. 15(3)).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No resilience requirements for adversarial or degraded inputs, such as presentation attacks, crafted forgeries designed to evade the model, worn or poorly lit documents, or varied laminates and sensors. [high] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add requirements for adversarial and evasion testing, input quality checks, sensor and condition variability, and fail-safe or manual-inspection fallback when image quality or model confidence is low.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Training, validation and testing data for forgery and counterfeit detection are not governed. Coverage of document types, issuing countries, document versions, and genuine-versus-forged samples may be unrepresentative, causing biased error rates for certain nationalities or document issuers. [medium] - Article 10(3) (`art:10:p3`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: Specify dataset provenance, representativeness across issuing states and document generations, and labeling quality. Add bias testing of error rates by issuing country, and handling for rare or new document templates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- FR-04 sets no requirement for risk management covering the foreseeable risks of false forgery flags, such as wrongful refusal of entry or discrimination against travelers from particular countries, or of missed forgeries. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-08 (officer confirm/override/escalate path that mitigates the impact of erroneous model outputs)
  - Category: `risk_management`
  - Action: Establish a documented risk management process covering the forgery detection model's error modes, residual risk acceptance, and testing against predefined metrics before deployment.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;

**Recommendations:**

- Define accuracy metrics and acceptance thresholds for each forgery detection capability, and declare them in the instructions for use.
- Add adversarial, degraded-input and sensor-variability robustness requirements with a low-confidence fallback to manual inspection.
- Document dataset governance and test bias in error rates across issuing states and document types.
- Establish a risk management process for false-positive and false-negative forgery outcomes with predefined test thresholds.

---

### FR-05

**Risk level:** high

**Requirement:** The system shall compare the photograph in the document with the traveler’s live-captured face image using facial recognition, and return a match confidence score.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 9 Risk management system (art:9)

**Analysis:** FR-05 returns a face-match confidence score but declares no accuracy metrics or thresholds, no demographic performance testing, and no robustness controls against spoofing or poor capture conditions. Unchecked error rates could wrongly flag or clear travelers, with disparate impact on particular groups.

**Risks:**

- No accuracy metrics (e.g. FMR/FNMR), decision thresholds or target performance levels are specified for the face match, so accuracy cannot be declared or tested against defined criteria. [high] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and document face-match accuracy metrics (FMR, FNMR, thresholds) and target levels, validate them against them before deployment, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No robustness or cybersecurity measures are stated for the live-captured image, such as presentation-attack (liveness) detection, injection or morphing attacks, or degraded image quality, so outputs could be manipulated. [high] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add liveness/presentation-attack detection, image-quality checks and adversarial/morphing-attack testing, and define fail-safe behaviour (e.g. refer to manual verification) when capture quality is insufficient.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not require testing or bias examination of the face-matching model across demographic groups (skin tone, age, sex), so performance disparities that could lead to discrimination in border decisions would go undetected. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: Require training/validation/test datasets to be representative of the traveler population, report match error rates per demographic group, and set acceptance thresholds and mitigation measures for disparities.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The bare confidence score gives officers no stated guidance on its meaning, thresholds, limitations or error likelihood, which risks misinterpretation and automation bias. FR-08 lets officers confirm or override, and FR-07 explains authenticity indicators, but neither covers interpreting the face-match score. [medium] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-08 (officer can confirm, override or escalate each decision (14(4)(d)))
  - Category: `human_oversight`
  - Action: Present the score with calibrated bands, known limitations and a prompt for the officer to review the images, and document score interpretation in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;

**Recommendations:**

- Define and declare face-match accuracy metrics, thresholds and target levels.
- Add liveness/presentation-attack detection, image-quality gating and adversarial testing with a manual-verification fallback.
- Test and report match performance per demographic group, with acceptance criteria and mitigations.
- Provide score interpretation guidance, calibrated confidence bands and automation-bias warnings in the officer interface and instructions.

---

### FR-06

**Risk level:** high

**Requirement:** The system shall check document and traveler details against lost, stolen, and revoked document databases and watchlists (e.g., Interpol SLTD) in near real time.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12)

**Analysis:** FR-06 matches traveler and document data against lost/stolen/revoked databases and watchlists in near real time, but gives no accuracy, data-quality or integrity requirements for those external reference sources or the matching. Stale, erroneous or tampered watchlist data, or poor name matching, could cause false matches that feed the risk assessment of travelers.

**Risks:**

- No accuracy or error-rate targets (false-match/false-non-match) are specified for watchlist and database matching, and none are declared for instructions of use. Fuzzy name or biographic matching can wrongly flag travelers. [high] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test matching accuracy metrics (false-match and miss rates, per name-transliteration and demographic group) for watchlist and SLTD checks. Declare them in the instructions of use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not address resilience when external databases are unavailable, slow, stale or inconsistent. 'Near real time' is undefined, and there is no fail-safe behavior or indication to the officer that a check was not completed. [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify latency and freshness targets, fallback and retry behavior, and an explicit 'check incomplete' state surfaced to the officer. Never silently return 'no hit' on a failed lookup.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- There are no integrity or authenticity controls for the external watchlist and SLTD feeds and query channels. Tampered or poisoned reference data or responses could alter outputs. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-09 (encryption of transmitted personal data and role-based access control)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require authenticated, integrity-protected connections to the feeds, signed or validated data updates, and anomaly detection on feed content and responses.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement sets no quality, relevance or currency criteria, and no data governance, for the watchlist and database data used for matching. Outdated or erroneous entries and unexamined bias in matching can adversely affect travelers. [medium] - Article 10(3) (`art:10:p3`)
  - Category: `data_governance`
  - Action: Document the source, update cadence and error-handling for each reference database. Add data-quality checks and a bias examination of matching across names and nationalities, in line with Article 10(2)(b) and (f).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.

**Recommendations:**

- Define and declare accuracy metrics and targets for watchlist and SLTD matching, including per-group error rates.
- Specify latency, freshness and fail-safe behavior, and show an explicit 'check incomplete' state to officers.
- Add authentication and integrity protection for external feeds and query channels, plus anomaly detection.
- Establish data governance and bias examination for reference data and name matching, with update and correction procedures.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall produce an authenticity assessment for each document, including an overall risk score, a classification (genuine, suspicious, or likely forged), and an explanation of the specific indicators behind the result, so officers can review the reasoning.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 86 Right to explanation of individual decision-making (art:86); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-07 provides a score, classification and indicator-level explanation, which supports interpretability. Remaining gaps: no declared accuracy metrics or score calibration/limitations for officers, and no explanation or notice mechanism for affected travelers.

**Risks:**

- Risk score and classification thresholds (genuine/suspicious/likely forged) have no declared accuracy metrics, error rates, calibration or known limitations, so officers cannot interpret the output appropriately or rely on declared performance in the instructions for use. [medium] - Article 13(3)(b) (`art:13:p3:b`)
  - Category: `transparency`
  - Action: Define and document score semantics, classification thresholds, accuracy metrics (e.g., FAR/FRR per classification), confidence indication and known limiting conditions (document types, image quality), and surface them in the output and instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers (closest match: Article 13(3)(f))
- The explanation is only for officers' review; there is no mechanism to cover automation-bias awareness or to let officers interpret indicators properly (e.g., indicator-level contributions, uncertainty), and no stated link to prevent over-reliance on the 'likely forged' label. [low] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-08 (officer ability to confirm, override or escalate each decision (14(4)(d)) and flagged areas on the document image supporting interpretation)
  - Category: `human_oversight`
  - Action: Specify that explanations show indicator-level evidence with confidence/uncertainty, and add automation-bias cues and officer guidance for interpreting each classification.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))
- Explanations are generated for officers only; nothing ensures that the role of the AI score in a decision can be conveyed to the affected traveler, or that the explanation is retained so the deployer can provide it on request. [medium] - Article 86(1) (`art:86:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-09 (auditable logs of verification transactions, which could retain the assessment record)
  - Category: `transparency`
  - Action: Persist the score, classification and indicator explanation per decision in an exportable form so deployers can give affected persons a meaningful explanation of the AI's role; define the deployer notice process (Art. 26(11)).
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(3)(b)**
  > (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately;
- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.

**Recommendations:**

- Declare accuracy metrics, thresholds, calibration and limitations for the risk score and classifications in the output specification and instructions for use.
- Add indicator-level confidence and automation-bias guidance so officers can correctly interpret and challenge the classification.
- Retain per-decision explanations in an exportable form and define the process for informing and explaining to affected travelers.

---

### FR-08

**Risk level:** medium

**Requirement:** The system shall present results to immigration officers through an interface that highlights flagged areas on the document image, and shall allow officers to confirm, override, or escalate each decision, with their feedback recorded to improve model accuracy.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 12 Record-keeping (art:12); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-08 supplies a strong oversight interface (highlighting, confirm/override/escalate), but it does not address automation-bias awareness or a stop/interrupt capability. Recording officer feedback to 'improve model accuracy' also creates an uncontrolled feedback loop that could entrench biased outputs.

**Risks:**

- Officer feedback is recorded to improve model accuracy with no safeguards against feedback loops (e.g., confirmations of biased flags reinforcing bias in later model updates). [medium] - Article 15(4) (`art:15:p4`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define how feedback enters retraining: validate and bias-test labels, separate officer overrides from confirmations, require change control and revalidation before any model update, and monitor drift and bias.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement offers no measures to make officers aware of automation bias (e.g., a risk of rubber-stamping confirmations of a flagged or 'likely forged' result), and no uncertainty or limitation cues beyond highlights. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-07 (explanation of specific indicators supporting officer interpretation of the output (14(4)(c)))
  - Category: `human_oversight`
  - Action: Add UI measures against over-reliance: show confidence and known limitations, require a reasoned justification for confirmations of adverse results, and monitor confirmation rates per officer. Include automation-bias content in the oversight instructions.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))
- No ability to halt or interrupt the system or to decline using it for a case is specified; only per-decision confirm/override/escalate is provided, and the effect of an override on downstream actions is undefined. [low] - Article 14(4)(e) (`art:14:p4:e`)
  - Category: `human_oversight`
  - Action: Add a stop/suspend function and a manual-only fallback mode that places the system in a safe state. Specify that an override takes precedence and blocks any automated adverse action.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.

**Recommendations:**

- Specify safeguards for feedback-driven retraining: label validation, bias testing, change control and revalidation before deployment.
- Add automation-bias countermeasures to the interface: confidence and limitation display, justification for confirmations, and per-officer monitoring.
- Add a stop/suspend and manual-only fallback capability, and define that an override overrides all downstream automated actions.

---

### FR-09

**Risk level:** medium

**Requirement:** The system shall maintain secure, auditable logs of all verification transactions, enforce role-based access control, and encrypt stored and transmitted personal data in compliance with applicable data protection regulations.

**Classified as:** Annex III point 7(b) (annex:III:7:b): (b) AI systems intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a natural person who intends to enter or who has entered into the territory of a Member State;; Annex III point 7(d) (annex:III:7:d): (d) AI systems intended to be used by or on behalf of competent public authorities, or by Union institutions, bodies, offices or agencies, in the context of migration, asylum or border control management, for the purpose of detecting, recognising or identifying natural persons, with the exception of the verification of travel documents.

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10)

**Analysis:** FR-09 provides auditable logs, RBAC and encryption, but does not specify log content or retention for Article 12 traceability. It also omits the identity of the officers who verify results. Cybersecurity is only partly covered because log integrity and protection against tampering are not specified.

**Risks:**

- Logs are limited to 'verification transactions' and do not specify event content that supports traceability, such as risk-relevant situations, post-market monitoring, and deployer operational monitoring (e.g., overrides, model version, reference databases checked, match inputs, officer identity). [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-08 (officer confirm/override/escalate feedback is recorded, which supplies part of the oversight event data)
  - Category: `record_keeping`
  - Action: Define a log event schema covering use period, model/version, reference databases checked (watchlists, SLTD), inputs leading to matches, risk score and classification, and officer actions. Map each field to Art. 12(2)(a)-(c).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- No log retention period is stated, and no alignment between a minimum of six months and data protection law (e.g., maximum storage) is specified. [medium] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Specify a log retention period of at least six months, or a justified period under applicable law, with automatic deletion and documented legal basis.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- The requirement says logs are 'secure', but specifies no tamper-evidence or integrity protection, and no detection of attempts to alter logs, outputs or performance, which Article 15(5) requires to be addressed with appropriate cybersecurity measures. [low] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add append-only or WORM log storage, cryptographic integrity checks, and alerting on unauthorised access or modification, and document the threat model, including AI-specific attacks.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define a log schema that covers Art. 12(2) traceability events, including model version, reference databases, matches, and officer actions.
- Set a log retention period of at least six months, aligned with data protection law, with automatic deletion.
- Add tamper-evident, integrity-protected log storage and security alerting.

---
