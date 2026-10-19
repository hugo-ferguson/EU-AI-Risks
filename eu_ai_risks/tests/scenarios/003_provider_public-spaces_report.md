# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 9

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 9 as high risk. The main review focus areas are other, human oversight, risk management, record keeping and transparency. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 9 high, 0 medium, 0 low.
- Most frequent mapped obligation areas: other (15), human oversight (7), risk management (6), record keeping (4), transparency (4).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** high

**Requirement:** The system shall continuously capture live video from cameras installed across designated public squares and process the streams in real time.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9)

**Analysis:** FR-01 is the live-capture entry point of a real-time remote biometric identification system in public squares. It feeds a system that identifies and profiles people for commercial purposes, and no deployer-side input-data, oversight, or risk-management controls are specified. Annex III 1(a) high-risk obligations are unaddressed, and the capture of untargeted CCTV-style footage for facial databases raises Article 5 prohibition concerns.

**Risks:**

- Continuous untargeted capture of public-square video feeds a pipeline that creates new facial profiles for every unmatched person (FR-02/FR-03). This risks the Article 5(1)(e) prohibition on creating or expanding facial recognition databases through untargeted scraping of CCTV footage, and no scope limitation is specified. [high] - Article 5(1)(e) (`art:5:p1:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Legal and engineering review of the capture-to-enrolment pipeline. Remove automatic creation of new profiles from untargeted footage, or restrict capture and enrolment to a lawful, targeted and documented scope. Do not deploy until the prohibition analysis is cleared.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Real-time remote biometric identification in publicly accessible spaces is specified with no restriction to the narrow exceptions, authorisation, or necessity and proportionality limits. If a law enforcement authority is a user, the Article 5(1)(h) prohibition and Article 5(2)-(3) conditions apply, and the stated commercial purpose has no lawful basis under the Act. [high] - Article 5(1)(h) (`art:5:p1:h`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Define and document permitted users and purposes. Technically block law-enforcement use unless prior authorisation, FRIA and registration are in place, and add temporal, geographic and personal limits to camera activation.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- No risk management process is defined for a high-risk remote biometric identification system capturing everyone in public squares. Fundamental-rights risks (privacy, discrimination, chilling effects) are not identified, evaluated or mitigated. [high] - Article 9(2) (`art:9:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented, iterative risk management process covering capture scope, camera placement, foreseeable misuse and vulnerable groups, with testing against defined metrics before deployment.
  - Trace:
    - referenced by Article 9(5) (Article 9(2)(d))
- The requirement defines no human oversight mechanism for live capture and processing: no stop/interrupt control, no monitoring of anomalies, and no two-person verification before any action is taken on an identification. [high] - Article 14(5) (`art:14:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `human_oversight`
  - Action: Add operator controls to pause or stop capture per camera or square. Require separate confirmation by two competent persons before any action based on an identification.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- Individuals in the squares are not informed that they are subject to a high-risk identification system. FR-09 mentions signage only where legally required, which is not specific to Article 26(11), and FR-01 itself has no notice trigger. [medium] - Article 26(11) (`art:26:p11`)
  - Partly addressed by: FR-09 (public notice signage, though only where legally required)
  - Category: `transparency`
  - Action: Require visible notice at every camera location before capture is activated. Make camera activation conditional on signage being deployed and recorded.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(e)**
  > (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
- **Prohibited AI practices, Article 5(1)(h)**
  > (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Review and remove or restrict the untargeted enrolment of unmatched faces to avoid the Article 5(1)(e) prohibition.
- Block or strictly gate any law-enforcement real-time use under Article 5(1)(h) and 5(2)-(3), and document permitted purposes.
- Establish an Article 9 risk management process covering capture scope and fundamental-rights risks.
- Add a stop control and two-person verification before any action is taken on an identification.
- Make camera activation conditional on signage that meets the Article 26(11) notice requirement.

---

### FR-02

**Risk level:** high

**Requirement:** The system shall detect all human faces appearing in each video frame and extract a facial feature template for each detected face.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** FR-02 performs untargeted face detection and template extraction on all people in public squares, feeding a remote biometric identification system for commercial profiling, with no stated purpose limitation, accuracy or bias controls, or oversight. This risks falling under the Article 5 prohibitions or, at minimum, high-risk Annex III 1(a) obligations that are unaddressed.

**Risks:**

- Mass face detection and template extraction from public-space video feeds a database of identities (FR-03) and cross-camera tracking (FR-04). The wording does not restrict the data to targeted use or exclude building a facial recognition database from untargeted CCTV capture, so it may fall under the Article 5(1)(e) prohibition. [high] - Article 5(1)(e) (`art:5:p1:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Escalate to legal/compliance review before build. Restrict template extraction to a lawful, targeted purpose and prohibit untargeted accumulation of face templates from CCTV. Redesign or remove the function if this cannot be shown.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- Real-time remote biometric identification in publicly accessible spaces is not limited to the narrow law-enforcement objectives with prior authorisation, and the system is described as being used for marketing and analytics. Face extraction as specified is a core step of that use, and the requirement has no gating by authorisation or purpose. [high] - Article 5(1)(h) (`art:5:p1:h`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-09 (legal-compliance support through signage, consent/opt-out and data subject requests, but not the Article 5(1)(h) authorisation conditions)
  - Category: `other`
  - Action: Add a purpose and authorisation gate so face extraction cannot run in publicly accessible spaces without a documented lawful basis and authorisation. Document that non-law-enforcement use is not supported.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- No accuracy, robustness or error-rate targets are specified for face detection and template extraction (for example across lighting, occlusion, crowds, or demographic groups). Errors propagate into misidentification and wrong profiles. [high] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and test detection and template-quality metrics (FNMR/FMR, detection recall) per condition and demographic group. Declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Nothing requires the face detection and template models to be built on representative, bias-examined datasets. Face recognition performance differs across demographic groups, which can lead to discriminatory misidentification. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: Document training, validation and test data provenance and representativeness. Run bias evaluation across demographic groups with mitigation and acceptance thresholds.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- No human oversight is specified over the automated identification output. Article 14(5) requires separate verification by two competent persons before any action is taken on an Annex III 1(a) identification. [medium] - Article 14(5) (`art:14:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-07 (authorized-user dashboard for viewing tracking, but no two-person verification or override)
  - Category: `human_oversight`
  - Action: Add a workflow in which no action is taken on an identification until two trained persons have separately confirmed it. Provide stop/override controls and operator guidance on limitations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(e)**
  > (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
- **Prohibited AI practices, Article 5(1)(h)**
  > (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.

**Recommendations:**

- Obtain legal review of the Article 5(1)(e) risk and redesign to avoid untargeted face template collection.
- Gate any real-time biometric identification in public spaces behind a documented lawful purpose and authorisation; do not support marketing use.
- Specify and test accuracy and robustness metrics for face detection and template extraction, and declare them in the instructions for use.
- Establish data governance and bias testing, with mitigation, for the face models.
- Implement two-person verification, override and stop controls before any action on identification results.

---

### FR-03

**Risk level:** high

**Requirement:** The system shall match each extracted template against a database of known identities and, where no match exists, create a new unique profile for the individual.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-03 matches facial templates against a database of known identities and automatically creates new profiles for unmatched individuals, which builds a facial recognition database from CCTV footage without targeting. This falls under the Art. 5(1)(e) prohibition. The system also performs real-time remote biometric identification (RBI) in public spaces, with no accuracy, verification or oversight controls specified for the matching step.

**Risks:**

- Automatic creation of a new unique profile for every unmatched face expands a facial recognition database through untargeted capture from public-square camera (CCTV) feeds, which is a prohibited practice. [high] - Article 5(1)(e) (`art:5:p1:e`)
  - Category: `other`
  - Action: Remove automatic enrolment of unmatched individuals. Restrict matching to a lawfully compiled, targeted watchlist, and escalate to legal review whether the system's purpose can be offered in the EU at all.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Real-time matching of people in public squares against an identity database is real-time remote biometric identification in publicly accessible spaces. If a deployer is a law enforcement authority, it is prohibited unless one of the narrow Art. 5(1)(h) objectives applies. FR-03 has no targeted-search limit, prior authorisation or necessity gating. [high] - Article 5(1)(h) (`art:5:p1:h`)
  - Category: `other`
  - Action: Add deployment gating that blocks law-enforcement use unless a specific permitted objective applies, a binding prior authorisation is recorded, and matching is limited to the specifically targeted individual, with time and geographic limits. Document the intended purpose as non-law-enforcement only if that is the case.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- No two-person separate verification is required before any action or decision is taken on an identification result. FR-03 outputs matches and new profiles that feed downstream profiling and analytics with no human confirmation. [high] - Article 14(5) (`art:14:p5`)
  - Category: `human_oversight`
  - Action: Add a workflow in which every identification match is separately verified and confirmed by at least two competent, trained and authorised persons before any action or decision is taken on it. Add override and reject controls for matches.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No accuracy or robustness targets are specified for identity matching, such as false match and false non-match rates, including across demographic groups. Misidentification could link a person to the wrong profile and history. [high] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define and declare the match threshold, FMR/FNMR and accuracy metrics. Test them by demographic group and under real camera conditions. Add resilience measures against spoofing and adversarial inputs.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(e)**
  > (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
- **Prohibited AI practices, Article 5(1)(h)**
  > (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years.
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Remove automatic creation of profiles for unmatched faces and limit matching to a lawful, targeted watchlist; obtain legal review of whether the system can be offered at all.
- Gate any law-enforcement deployment on a permitted Art. 5(1)(h) objective, a binding prior authorisation, and targeted, time-limited and geographically limited use.
- Require separate verification of each match by two competent persons before any action, with override controls.
- Specify, test and declare matching accuracy metrics (FMR/FNMR) per demographic group, plus spoofing and adversarial robustness.

---

### FR-04

**Risk level:** high

**Requirement:** The system shall track each identified individual across frames and across multiple camera views, maintaining a continuous movement path within and between monitored areas.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9)

**Analysis:** FR-04 adds persistent cross-camera tracking to a real-time remote biometric identification system in public squares used for commercial profiling. No human verification, oversight or risk controls are specified, and the purpose may fall under Article 5 prohibitions or at minimum high-risk obligations.

**Risks:**

- Persistent cross-camera tracking of identified individuals in publicly accessible spaces is an extension of real-time remote biometric identification; if any law-enforcement use is intended, Article 5(1)(h) prohibits it outside narrow, authorised objectives, and the tracking is not limited to a targeted individual. [high] - Article 5(1)(h) (`art:5:p1:h`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Constrain the deployment to non-law-enforcement use or add authorisation-gated, targeted-individual-only tracking. Block tracking of untargeted persons and record the legal basis for each deployment. Escalate the commercial profiling purpose for prohibited-practice review.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Tracking continuous movement paths feeds the per-person behavioural profiling and inference of interests in FR-05/FR-06, which risks unjustified or detrimental classification of people based on behaviour, and no safeguard on downstream use of the tracks is specified. [high] - Article 5(1)(c) (`art:5:p1:c`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Prohibit use of tracking paths for scoring or classification leading to unfavourable treatment. Document permitted purposes and enforce them through technical purpose limitation on track data.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- No human oversight is specified for identity-linked tracks: no verification of identifications by two competent persons before action, no ability to override or stop tracking, and no handling of tracking errors such as identity swaps across cameras. [high] - Article 14(5) (`art:14:p5`)
  - Partly addressed by: FR-07 (dashboard display of individual tracking for authorised users (monitoring interface only, no verification or override))
  - Category: `human_oversight`
  - Action: Add a requirement that no action is taken on a tracked identification until two authorised, trained persons separately confirm it. Provide stop/override controls, track-confidence display and anomaly review for cross-camera re-identification.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No risk identification or testing is defined for cross-camera tracking accuracy and its fundamental-rights impacts (mis-association, bias across demographic groups, chilling effects on movement), and no metrics or thresholds are declared. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented risk management process covering tracking. Test re-identification accuracy against predefined metrics and thresholds, including per-group error rates, before deployment.
  - Trace:
    - referenced by Article 9(4) (Article 9(2)(d))
- Deployer duties for a high-risk system are not reflected: there are no operation monitoring and incident or risk suspension procedures, and no log retention specific to tracking events. FR-08 provides audit logging and retention in general terms only. [medium] - Article 26(6) (`art:26:p6`)
  - Partly addressed by: FR-08 (audit logging and configurable retention of tracking history)
  - Category: `record_keeping`
  - Action: Specify that tracking events, matches and operator actions are logged and retained for at least six months, subject to data protection law. Define a procedure to suspend the system and report if tracking presents a risk.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(h)**
  > (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years.
- **Prohibited AI practices, Article 5(1)(c)**
  > (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following: (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity;
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.

**Recommendations:**

- Confirm the intended use against Article 5 prohibitions and restrict tracking to lawful, targeted, authorised scenarios, or do not build it.
- Block use of tracking data for behavioural scoring or unfavourable classification, and enforce purpose limitation technically.
- Add two-person verification, override and stop controls for identity-linked tracks.
- Establish a risk management process with declared accuracy and bias metrics for cross-camera re-identification.
- Define log content and retention of at least six months for tracking events, plus a suspension and incident-escalation procedure.

---

### FR-05

**Risk level:** high

**Requirement:** The system shall build and update a profile for each individual from observed data such as visit frequency, dwell time, locations visited, and movement patterns.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14)

**Analysis:** FR-05 builds persistent behavioral profiles of identified individuals in public squares for commercial use, which touches the Article 5 prohibitions (social-scoring-type profiling, real-time RBI) and has no risk assessment or bias controls. The system is a real-time remote biometric identification system (Annex III 1(a)); the requirement has no safeguards to prevent unrelated-context detrimental treatment and no oversight or verification controls.

**Risks:**

- Cross-camera behavioral profiling of identified individuals (visit frequency, dwell time, locations, movement) feeds commercial attributes and could be used to evaluate or classify persons over time, with unfavourable treatment in contexts unrelated to where the data was collected; nothing limits purpose or downstream use. [high] - Article 5(1)(c) (`art:5:p1:c`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Perform a prohibited-practice screening of the profiling function. Restrict profile use to a defined purpose, bar use for scoring or differential treatment, and remove or redesign person-level profiling if it cannot be shown to fall outside Art. 5(1)(c).
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- The profile-building function has no identified or analysed risks to fundamental rights (privacy, non-discrimination, chilling effects on public movement), no risk evaluation and no mitigation for continuous tracking-based profiling. [high] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented risk management process covering profiling harms, including residual-risk acceptance and misuse scenarios. Add data minimisation and a limit on profile scope and duration.
  - Trace:
    - referenced by Article 9(5) (Article 9(2)(d))
- Profiles are built from observed behavioural data with no examination for bias or representativeness (e.g. in identification error rates across groups, or in the behavioural patterns encoded in profiles) and no data governance practices for how data is collected and prepared. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Document data origin and preparation for profile building, run bias testing on identification and profile outputs across demographic groups, and define mitigation and acceptance criteria.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(b))
- Profile updates run automatically from identifications with no requirement that identifications be verified by two competent persons before any action is taken on a profile, and no ability for an overseer to disregard, override or stop profile creation. [high] - Article 14(5) (`art:14:p5`)
  - Category: `human_oversight`
  - Action: Require separate two-person verification of identifications before any action or decision is based on a profile. Add override, suspend and profile-deletion controls for overseers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- Individuals profiled by the system are not told they are subject to the high-risk system. FR-09 mentions signage and opt-out only where legally required, which is not a deployer notice for profile-based decisions. [medium] - Article 26(11) (`art:26:p11`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-09 (public notice signage and opt-out/consent mechanisms (partial notice to affected persons))
  - Category: `transparency`
  - Action: Add a mandatory notice that individuals are subject to biometric identification and profiling, covering the purpose and how profile data is used.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(c)**
  > (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following: (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity;
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Screen the profiling function against Art. 5(1)(c) and restrict or remove it if it cannot be shown to be outside the prohibition.
- Establish a risk management process for profiling harms with documented residual-risk acceptance.
- Add bias testing and data governance documentation for profile inputs and outputs.
- Require two-person verification and add override and stop controls before any action is taken on a profile.
- Add a mandatory notice to profiled individuals that explains the biometric identification and profiling.

---

### FR-06

**Risk level:** high

**Requirement:** The system shall derive commercial attributes for each profile, such as estimated demographics, interests, and behavioral segments, and make them available for marketing and analytics purposes.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-06 derives estimated demographics, interests and behavioural segments from biometrically identified, tracked individuals for marketing, with no safeguards against prohibited inference (e.g. biometric categorisation of sensitive traits, exploitation of vulnerabilities) and no bias examination of the inferences. FR-09 covers only privacy-law notice and consent, so the attribute derivation could fall under an Article 5 prohibition or discriminate without any control.

**Risks:**

- Estimated demographics and segments derived from biometric data could infer race, political opinions, religion, sexual orientation or similar traits, which Article 5(1)(g) prohibits as biometric categorisation. FR-06 has no exclusion or restriction on the attributes derived. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - Category: `other`
  - Action: Define a closed whitelist of permitted attributes. Technically block inference of race, political opinions, trade union membership, religious or philosophical beliefs, sex life and sexual orientation, including via proxies. Do not derive attributes from face or biometric data. Add a legal review gate before any new attribute is released.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
- Behavioural segments and interests profiled per person for marketing could exploit vulnerabilities (age, disability, economic situation) or distort behaviour, or feed a social-scoring-type classification used in unrelated contexts. FR-06 sets no purpose limitation or use restriction. [high] - Article 5(1)(b) (`art:5:p1:b`)
  - Category: `other`
  - Action: Exclude vulnerability-related segments (minors, disability, financial distress) from marketing outputs. Enforce purpose limitation so attributes cannot be reused for evaluation or treatment in unrelated contexts. Document a prohibited-practice assessment for each segment.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(d))
- No examination or mitigation of bias in the demographic and interest estimation models, which risks discriminatory marketing or analytics outcomes. FR-06 gives no accuracy or representativeness criteria for the inferences. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add bias testing of attribute estimators across demographic groups, with acceptance thresholds and mitigation. Document dataset provenance, representativeness for the deployment setting, and the assumptions about what each attribute measures.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(a))
- Individuals are not informed that biometric-derived commercial profiling is applied to them. FR-09 provides signage and opt-out only 'where legally required', with no content covering attribute derivation, and nothing makes the attributes' limitations interpretable for deployers. [medium] - Article 26(11) (`art:26:p11`)
  - Partly addressed by: FR-09 (public notice signage and opt-out mechanisms (partial: general notice to individuals))
  - Category: `transparency`
  - Action: Extend the notice mechanism to state that demographic and interest attributes are inferred and used for marketing. Provide per-attribute confidence and limitation information to deployers in the instructions for use and the dashboard.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The risk management process does not identify or evaluate fundamental-rights risks from commercial attribute inference and its downstream marketing and analytics use. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Add a documented risk assessment covering profiling, discrimination and misuse of derived attributes, with targeted mitigations. Review it iteratively across the lifecycle.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Prohibited AI practices, Article 5(1)(b)**
  > (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;

**Recommendations:**

- Whitelist permitted attributes and block inference of sensitive characteristics (Art. 5(1)(g)).
- Restrict marketing use to prevent vulnerability exploitation and out-of-context scoring, and document the prohibited-practice assessment.
- Add bias testing and data governance for the attribute estimators, with acceptance thresholds.
- Extend notices to cover attribute inference, and give deployers confidence and limitation information.
- Establish a lifecycle risk management process covering fundamental-rights risks of profiling.

---

### FR-07

**Risk level:** high

**Requirement:** The system shall provide an authorized-user dashboard that displays live crowd density, individual tracking, and aggregated and per-profile analytics, with search, filtering, and report export.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 5 Prohibited AI practices (art:5); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 12 Record-keeping (art:12)

**Analysis:** FR-07 is the human-machine interface for a real-time remote biometric identification system, yet it only provides display, search and export. It has no oversight features (stop/override, automation-bias awareness, interpretation aids, two-person verification), and its tracking and profiling outputs are exposed without safeguards. Separately, the system's purpose (commercial profiling and demographic inference from biometric tracking) raises Article 5 concerns that this dashboard facilitates.

**Risks:**

- The dashboard shows individual identification and tracking results with no requirement for separate verification and confirmation by two competent natural persons before any action or decision is taken on an identification. [high] - Article 14(5) (`art:14:p5`)
  - Category: `human_oversight`
  - Action: Add a dual-verification workflow to the dashboard. Identification-based actions, exports and alerts stay blocked until two distinct authorised, trained users have confirmed the match, and both confirmations are recorded.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The interface lacks oversight tooling: no stop/interrupt control, no ability to disregard or override a match, no confidence or limitation indicators, and no anomaly monitoring or automation-bias cues for operators. [high] - Article 14(4) (`art:14:p4`)
  - Category: `human_oversight`
  - Action: Add match confidence and known-limitation displays, anomaly and performance indicators, an override/disregard action per match, a system-wide stop button that halts safely, and automation-bias warnings in the UI.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(a))
- Per-profile analytics and individual tracking are exposed in the dashboard with no stated risk analysis of the fundamental-rights risks (surveillance, misuse by operators, inference of sensitive traits), so oversight measures are not commensurate with those risks. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Run a documented risk assessment covering dashboard misuse and foreseeable misuse. Derive restrictions from it, such as limiting individual-level views to authorised purposes and aggregating by default.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))
- The dashboard does not require operator interactions (searches, views, exports, and the persons verifying results) to be logged; the Annex III 1(a) minimum logging includes use periods, reference database, matched input data and verifiers' identities. FR-08 gives audit logging only generically. [medium] - Article 12(3) (`art:12:p3`)
  - Partly addressed by: FR-08 (audit logging and role-based access control for stored data, in general terms)
  - Category: `record_keeping`
  - Action: Log each dashboard session and search with timestamps, the reference database used, matched inputs, and the identities of verifying users. Make the logs exportable and retain them for at least six months.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Per-profile analytics built from tracking and commercial attributes, with report export, could support prohibited practices: classification of persons by inferred characteristics, or biometric categorisation to infer sensitive traits. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Review the system against the Article 5 prohibitions. Block export or display of attributes that infer sensitive traits or feed social-scoring-type use, and escalate the purpose and design to legal review.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))

**Cited provisions:**

- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;

**Recommendations:**

- Add a two-person verification gate before any identification-based action, export or alert.
- Add stop, override, confidence-display and automation-bias controls to the dashboard.
- Perform a documented risk assessment of dashboard misuse and restrict individual-level views and exports accordingly.
- Log operator sessions, searches, exports and verifier identities in line with the Annex III 1(a) logging minimums.
- Obtain legal review of the system's purpose against the Article 5 prohibitions and block prohibited inference and export functions.

---

### FR-08

**Risk level:** high

**Requirement:** The system shall securely store biometric templates, profiles, and tracking history, enforce role-based access control and audit logging, and apply configurable data retention and deletion policies.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-08 sets storage security, RBAC, audit logging and retention for biometric data, but it does not specify Article 12(3) minimum logging content, a log retention floor (Art. 19), or AI-specific cybersecurity measures (Art. 15(5)). The remaining gaps are mostly partial controls. The system's purpose (commercial profiling via real-time remote biometric identification in public squares) raises a more fundamental Article 5 question that this requirement cannot fix.

**Risks:**

- Audit logging covers data access only; it does not record the Annex III 1(a) minimum events: period of each use, reference database checked, input data leading to a match, and the persons verifying results. [medium] - Article 12(3) (`art:12:p3`)
  - Category: `record_keeping`
  - Action: Extend logging to record start/end of each use, the reference database queried, the input data for each match, and the identity of the verifying persons. Make the logs tamper-evident.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Configurable retention and deletion policies have no stated floor for system logs (at least six months), so the configuration could allow logs to be deleted early, or kept longer than data protection law allows. [low] - Article 19(1) (`art:19:p1`)
  - Category: `record_keeping`
  - Action: Set a minimum log retention of at least six months. Apply data protection law limits for logs containing personal data, and keep log retention separate from template and profile retention.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 19 Automatically generated logs
- 'Securely store' and RBAC are unspecified and do not address AI-specific attacks or confidentiality attacks on templates and profiles (for example template leakage, tampering with the reference database, or poisoning through enrolment of new profiles). [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify encryption at rest and in transit for templates, key management, and integrity protection of the reference database. Add write-access controls on enrolment, anomaly detection on database changes, and security testing that covers confidentiality and poisoning attacks.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The system stores and profiles biometric data for identification and commercial attribute derivation (FR-05, FR-06), and this requirement entrenches that storage with no purpose limits. Real-time remote biometric identification in public spaces is prohibited for law enforcement outside narrow exceptions, and biometric categorisation or untargeted face database building may also be prohibited. Retention of tracking history extends this exposure. [high] - Article 5(1)(e) (`art:5:p1:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Obtain a legal prohibited-practice assessment before build. Drop untargeted enrolment of faces from CCTV, and do not store data for inferring protected characteristics. If the purpose cannot be shown to be outside Article 5, descope storage of identification templates and tracking history.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Prohibited AI practices, Article 5(1)(e)**
  > (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;

**Recommendations:**

- Extend audit logs to cover the Article 12(3) minimum events: period of use, reference database, matched input data, and verifiers.
- Set a minimum log retention period of six months or more, separate from template and profile retention, within data protection limits.
- Specify encryption, key management, database integrity controls and security testing against AI-specific attacks on stored biometric data.
- Commission a legal assessment against Article 5 prohibitions and descope any storage that supports prohibited practices.

---

### FR-09

**Risk level:** high

**Requirement:** The system shall support compliance with applicable privacy and biometric data laws, including public notice signage, consent or opt-out mechanisms where legally required, and individual data access and deletion requests.

**Classified as:** Annex III point 1(a) (annex:III:1:a): (a) remote biometric identification systems. This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be;

**Articles selected from the index:** Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 10 Data and data governance (art:10); Article 5 Prohibited AI practices (art:5); Article 86 Right to explanation of individual decision-making (art:86)

**Analysis:** FR-09 treats biometric legality as a notice/consent/DSAR feature, but the system performs untargeted real-time facial recognition and cross-camera profiling in public squares for commercial use. Signage and opt-out cannot cure the Article 5 prohibitions that the SRS leaves unaddressed, and the requirement omits the deployer's transparency and DPIA duties for high-risk systems.

**Risks:**

- Untargeted face template creation for new profiles (FR-02/FR-03) from public-square CCTV risks the Art. 5(1)(e) prohibition on untargeted scraping of CCTV to build facial recognition databases, and FR-09 offers only notice/opt-out as a remedy, which does not lift the prohibition. [high] - Article 5(1)(e) (`art:5:p1:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Add a requirement to block enrolment of non-consented faces into the database. Run a legal prohibition screening before design freeze, restrict matching to targeted, lawfully enrolled watchlists, and make FR-09 explicitly subordinate to this screening.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Per-person behavioural profiles and inferred demographics/interests (FR-05/FR-06) may amount to prohibited social scoring or biometric categorisation. FR-09 treats this as a consent matter and does not require exclusion of sensitive inferences. [high] - Article 5(1)(g) (`art:5:p1:g`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Prohibit inference of race, political opinion, religion, sexual orientation or similar traits from biometric data. Add a technical control to enforce this and document the prohibited-practice assessment for FR-06 attributes.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- The requirement covers only signage and opt-out and does not require informing the natural persons subject to the high-risk system, or giving the deployer the information needed for a DPIA. Public signage is not specified to cover identification, tracking, profiling purposes or contact details. [high] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Specify notice content (identification, cross-camera tracking, profiling, purposes, retention, rights contact) at all entry points. Add a DPIA deliverable using Art. 13 provider information, per Art. 26(9).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- Opt-out and deletion are stated generically 'where legally required'. Because the system builds profiles of everyone passing by, it is not specified how non-enrolled bystanders can be identified to exercise rights, or how deletion propagates to templates, tracking paths and derived attributes. [medium] - Article 26(9) (`art:26:p9`)
  - Partly addressed by: FR-08 (configurable retention and deletion policies for biometric templates, profiles and tracking history)
  - Category: `fundamental_rights_impact_assessment`
  - Action: Define a rights-handling workflow (identity verification without extra biometric collection, SLAs, deletion across all derived data and exports). Align with the FR-08 retention and deletion policies.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- No risk management process identifies or mitigates fundamental-rights risks (privacy, non-discrimination, chilling effects) of mass public biometric identification. FR-09 relies on legal-compliance support rather than risk analysis. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a lifecycle risk management process that identifies fundamental-rights risks, evaluates misuse, and defines targeted mitigations. Link FR-09 controls to the identified risks.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(e)**
  > (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
- **Prohibited AI practices, Article 5(1)(g)**
  > (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement;
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Obligations of deployers of high-risk AI systems, Article 26(9)**
  > 9. Where applicable, deployers of high-risk AI systems shall use the information provided under Article 13 of this Regulation to comply with their obligation to carry out a data protection impact assessment under Article 35 of Regulation (EU) 2016/679 or Article 27 of Directive (EU) 2016/680.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;

**Recommendations:**

- Block non-consented, untargeted face enrolment and restrict matching to targeted, lawful watchlists after a prohibition screening.
- Prohibit sensitive-attribute inference from biometrics and document the Art. 5 assessment of FR-05/FR-06.
- Specify full notice content and a DPIA deliverable for affected persons and deployers.
- Define a rights-request workflow covering bystanders and deletion of all derived data, linked to FR-08.
- Set up a lifecycle fundamental-rights risk management process and link FR-09 controls to it.

---
