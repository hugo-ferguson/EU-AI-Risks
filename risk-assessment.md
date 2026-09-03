# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 15
- Medium: 1

## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** {"summary":"FR-1 only specifies raw ingestion of resumes, cover letters, and application data for a recruitment system without any data-quality, governance, bias-mitigation, or candidate-transparency controls, despite recruitment/selection tools being classified as high-risk under Annex III(4)(a), creating multiple unmet binding obligations at the data intake stage.","risks":[{"description":"FR-1 does not require verification that ingested resume/cover-letter/application data is relevant, sufficiently representative, and examined for biases before being used to train or feed the scoring model, as mandated for high-risk AI training/input data.","severity":"high","article_id":"art:10","paragraph_num":2,"provision":"Article 10(2)(f)-(g)"},{"description":"The requirement gives the deployer no obligation to ensure that ingested input data is relevant and sufficiently representative for the intended purpose, which is required wherever the deployer controls input data for a high-risk system.","severity":"high","article_id":"art:26","paragraph_num":4,"provision":"Article 26(4)"},{"description":"FR-1 contains no provision to inform candidates that their resumes/cover letters/application data will be processed by a high-risk AI system before or at the point of ingestion, omitting the deployer's transparency duty to affected natural persons.","severity":"high","article_id":"art:26","paragraph_num":11,"provision":"Article 26(11)"},{"description":"There is no requirement to document why the recruitment tool is classified as high-risk (or, if claimed exempt, to record that assessment), leaving the ingestion function's risk classification undocumented as required before any Annex III system is put into service.","severity":"medium","article_id":"art:6","paragraph_num":4,"provision":"Article 6(4)"},"severity":"medium","article_id":"art:9","paragraph_num":2,"provision":"Article 9(2)"},{"description":"FR-1 does not address logging of ingestion events (timestamps, data source, version

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** FR-10 provides a bare 'request review' channel but omits the mandatory content, timing, and scope elements required under Article 86 (right to explanation) and Article 26(11)/13(3) transparency duties, leaving candidates unable to exercise a meaningful right to contest an automated ranking decision used in this high-risk (Annex III, employment) AI system.

**Risks:**

- Article 86(1) requires that affected persons receive, on request, 'clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.' FR-10 only creates a channel to 'request review' but does not obligate the system/deployer to actually furnish this explanation content, so the right is not operationalized — a candidate could submit a request and receive no substantive explanation. [high] - Article 86(1)
- Article 26(11) requires deployers to proactively inform natural persons that they are subject to a high-risk AI system's decision-making before/at the point of use. FR-10 assumes candidates already know automated ranking influenced their outcome, but there is no linked requirement ensuring candidates are notified of this fact in the first place, so they may never know to invoke the review channel. [high] - Article 26(11)
- Article 14 human oversight requires that a natural person can 'disregard, override or reverse' the AI output. FR-10's 'review channel' is candidate-facing but does not specify that the review must be conducted by a competent human recruiter with authority to override the score (this is partially covered by FR-6, but FR-10 itself does not link the request mechanism to a defined human-oversight actor or SLA for response), risking the review being a nominal formality rather than genuine human reconsideration. [medium] - Article 14(4)(d)
- FR-10 does not reference or preserve the candidate's independent right under Article 85 to lodge a complaint with the national market surveillance authority regardless of the outcome of the internal review channel; presenting the internal channel as the remedy could imply it is the only avenue, undermining awareness of statutory external redress. [medium] - Article 85
- No timing requirement is specified for when the review request/explanation must be provided; Article 50(5) principles (info given at latest at first interaction) and general due-process expectations imply explanations/responses should be timely, but FR-10 is silent on response deadlines, risking indefinite delay that defeats the purpose of the review right. [low] - Article 86(1)

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Right to lodge a complaint with a market surveillance authority**
  > Without prejudice to other administrative or judicial remedies, any natural or legal person having grounds to consider that there has been an infringement of the provisions of this Regulation may submit complaints to the relevant market surveillance authority. In accordance with Regulation (EU) 2019/1020, such complaints shall be taken into account for the purpose of conducting market surveillance activities, and shall be handled in line with the dedicated procedures established therefor by the 

**Recommendations:**

- Amend FR-10 to explicitly require that upon a review request, the system/deployer supplies a clear, meaningful explanation of the AI system's role and the main decision factors, satisfying Article 86(1) content requirements.
- Add a requirement (or strengthen FR-1 family) mandating that candidates are proactively informed, before or at first interaction, that an automated ranking system is used in their evaluation, per Article 26(11).
- Link FR-10 to FR-6 explicitly so the 'review' is defined as a human-recruiter-led override capability with documented authority and competence, not just a passive complaint intake.
- Add a requirement stating that use of the internal review channel does not preclude and must inform candidates of their right to lodge a complaint with the competent market surveillance authority under Article 85.
- Add a defined maximum response time (SLA) for providing the explanation/review outcome to the candidate after a request is submitted.

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 defines a candidate suitability-scoring function without any of the safeguards mandated for high-risk recruitment AI (Annex III, point 4) — data governance/bias control, human oversight, transparency, and accuracy/robustness are all absent, creating multiple binding compliance gaps.

**Risks:**

- The requirement does not specify data governance or bias-examination/mitigation measures for the training, validation and testing data used to derive experience/education/skills-based scores, despite Article 10(2)(f)-(g) mandating examination for biases affecting fundamental rights or leading to prohibited discrimination in exactly this kind of candidate-evaluation use case. [high] - Article 10(2)(f)-(g)
- FR-2 gives no mechanism for human oversight of the generated score (e.g., preventing automation bias, enabling a recruiter to understand, monitor, and override the score) even though scoring/ranking candidates is a decision-support function subject to Article 14's effective human oversight requirement. [high] - Article 14(1)
- There is no requirement to inform candidates that they are being scored/evaluated by an AI system, which is a binding deployer obligation for high-risk systems affecting natural persons in recruitment decisions. [high] - Article 26(11)
- No accuracy, robustness or performance-metric requirements are specified for the suitability-scoring logic, so there is no basis to demonstrate the system 'achieves an appropriate level of accuracy' and resists erroneous or biased outputs over its lifecycle as required for high-risk systems. [medium] - Article 15(1)
- FR-2 omits any linkage to a documented risk-management process (identification/estimation/mitigation of risks to fundamental rights, e.g., discriminatory scoring) that must exist and be maintained for the lifecycle of a high-risk recruitment AI system. [medium] - Article 9(2)
- The requirement does not exclude or control use of protected/special-category attributes in deriving the score, risking unlawful discrimination through proxies in 'experience/education/skills' features, which Article 10(2)(f) requires providers to actively examine and prevent. [medium] - Article 10(5)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Add explicit data governance/bias-testing requirements (representativeness checks, bias detection and mitigation) for all data feeding the suitability score, per Art 10(2)(f)-(g).
- Define a human-oversight interface (recruiter review, override, and rationale display) before any score-based decision is finalized, per Art 14.
- Add a transparency requirement to notify candidates that an AI system is used to evaluate/score their application, per Art 26(11) and Art 13.
- Specify accuracy/robustness metrics and testing/validation criteria for the scoring model, and document them in instructions for use, per Art 15.
- Link FR-2 to a documented risk-management process covering fundamental-rights risks (e.g., discriminatory scoring) across the system lifecycle, per Art 9.
- Explicitly prohibit use of protected characteristics (or their proxies) in score computation and document justification/safeguards if special-category data is processed for bias correction, per Art 10(5).

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 implements only the ranking output of a high-risk employment AI system without embedding safeguards against automation bias, bias-driven disparate impact in the ranking itself, or accuracy/transparency guarantees required for candidate-affecting decisions, creating non-compliance with human oversight, data governance, accuracy and transparency obligations under the AI Act.

**Risks:**

- The requirement lets recruiters review a ranked list but does not specify any design measure to prevent automation bias (e.g., recruiters over-relying on rank order and only reviewing top-ranked candidates). Article 14 requires that human oversight measures be built in to counter the tendency to over-rely on system output, especially for systems that provide recommendations for human decisions such as recruitment ranking. [high] - Article 14(4)(b)
- Ranking candidates by a suitability score can produce discriminatory outcomes through proxy variables even if protected attributes are excluded as direct inputs (per NFR-3). The requirement does not mandate bias examination and mitigation of the ranking output itself, which Article 10 requires for training/validation/testing data and downstream outputs of high-risk systems used in employment contexts. [high] - Article 10(2)(f)-(g)
- The requirement does not tie the ranking function to any accuracy, robustness or performance validation. Since ranking directly determines which candidates get recruiter attention, inaccurate or unstable scoring could systematically disadvantage some candidates without any accuracy threshold or testing obligation being referenced, violating the accuracy and robustness requirement for high-risk AI systems. [medium] - Article 15(1)
- The requirement does not require that ranking output be accompanied by information enabling the recruiter (deployer) to correctly interpret it (e.g., accuracy metrics, known limitations, or circumstances affecting reliability), which is mandated for high-risk system outputs used to inform human decisions. [medium] - Article 13(3)(b)
- There is no explicit linkage of the ranking function to the system's overarching risk management process (identification/mitigation of risks to fundamental rights arising from ranking, e.g., unfair exclusion of qualified candidates), leaving a gap in demonstrating that ranking-specific risks were assessed and mitigated as part of the continuous risk management system required for this Annex III (employment) high-risk use case. [medium] - Article 9(2)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Add a design constraint requiring recruiters to review all candidates (or a representative set), not just top-ranked ones, and present ranking as advisory with visible uncertainty indicators to mitigate automation bias (Art 14(4)(b)).
- Extend requirement to mandate periodic bias testing of ranking outputs across protected-characteristic-correlated groups, with corrective action if disparate impact is detected (Art 10(2)(f)-(g)).
- Define and document accuracy/robustness acceptance criteria for the suitability scoring/ranking algorithm, validated before deployment and monitored post-deployment (Art 15(1)).
- Require the system to expose accuracy metrics and known limitations of the ranking alongside the score so recruiters can correctly interpret results (Art 13(3)(b)).
- Incorporate ranking-specific risks (e.g., unfair exclusion, proxy discrimination) explicitly into the system's risk management documentation and mitigation measures (Art 9(2)).

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 only provides post-hoc score explanations to recruiters, but omits the mandatory explanation rights of the candidates themselves and the broader transparency/instructions-for-use content required for a high-risk recruitment AI system, creating both fundamental-rights and provider-documentation gaps.

**Risks:**

- The requirement gives no mechanism for candidates (the affected persons whose suitability scores determine ranking) to obtain an explanation. Article 86 grants any person subject to a legally/significantly impactful decision from an Annex III high-risk system the right to a clear, meaningful explanation of the AI's role and the main elements of the decision. FR-4 restricts explanation delivery to the recruiter only, leaving candidates without any means to request or receive an explanation of an adverse suitability score. [high] - Article 86(1)
- FR-4 does not require informing candidates that they are subject to an automated/high-risk AI system in the first place, a precondition to exercising any explanation or contestation rights. Deployers of Annex III systems that make or assist decisions about natural persons must proactively notify those persons, independent of any explanation feature. [high] - Article 26(11)
- The explanation is scoped only to 'main factors' influencing a score, but Article 13 requires the provider to supply full instructions for use that are 'concise, complete, correct and clear', covering the system's capabilities/limitations and, where applicable, its technical capacity to explain outputs (Art.13(3)(b)(iv)) and performance on specific groups. FR-4 does not ensure the explanation content meets this completeness/correctness standard or covers foreseeable risks and performance limitations, risking inadequate transparency for the deployer to interpret and use the score appropriately. [medium] - Article 13(2)
- By only stating factors are explained 'in language understandable to a recruiter', FR-4 does not address human oversight safeguards under Article 14(4)(b)-(c): enabling recruiters to remain aware of automation bias/over-reliance and to correctly interpret output using available interpretation tools/methods. An explanation feature that is not designed to counter automation bias may create a false sense of correctness and lead recruiters to over-rely on the score. [medium] - Article 14(4)
- FR-4 does not specify that the explanation must be sufficient to allow detection of discriminatory patterns tied to protected attributes in the underlying scoring logic, which is central to the risk-mitigation purpose of explainability for employment-related high-risk systems; without this, the explanation may satisfy a literal 'understandability' bar while failing to support bias detection obligations tied elsewhere in the system (e.g., prohibition on using protected attributes). [low] - Article 13(1)

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Transparency and provision of information to deployers, Article 13(2)**
  > 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add a candidate-facing explanation channel satisfying Article 86: upon request, provide affected candidates with a clear, meaningful explanation of the AI system's role and the main elements of the suitability decision.
- Add a separate notification requirement informing candidates that a high-risk AI system is used in the recruitment/scoring process, independent of and prior to any explanation request (Article 26(11)).
- Expand the explanation content requirement to align with Article 13(3) instructions for use — covering accuracy metrics, known limitations, and foreseeable risks — so the recruiter-facing explanation meets completeness and correctness standards.
- Require the explanation UI/design to include automation-bias mitigation cues (e.g., confidence indicators, prompts to review low-confidence factors) so recruiters correctly interpret output rather than over-rely on it, per Article 14(4)(b)-(c).
- Specify that explanations must surface factor-level detail sufficient to enable detection of proxy discrimination against protected attributes, linking explainability to the system's non-discrimination safeguards.

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 only requires a bare notification to recruiters that a ranking was AI-generated, without the substantive human oversight, explanation, and affected-person transparency obligations the AI Act mandates for high-risk recruitment AI systems.

**Risks:**

- A simple notification does not satisfy Article 14 human oversight requirements, which demand that overseers be enabled to understand the system's capabilities/limitations, detect automation bias, correctly interpret outputs, and have the ability to override, disregard or halt the system. FR-5 provides no mechanism for recruiters to do any of this beyond knowing a model was involved. [high] - Article 14(4)
- Deployers must assign human oversight to natural persons with necessary competence, training and authority (Art 26(2)); merely notifying recruiters that a ranking is AI-generated does not ensure they are qualified or empowered to meaningfully review or contest it, risking automation bias and rubber-stamping of scores. [high] - Article 26(2)
- The requirement omits any obligation to provide job candidates (affected persons) with an explanation of the AI's role and the main factors behind an adverse decision, which Article 86 grants as a right to explanation when a high-risk AI system's output significantly affects them. [high] - Article 86(1)
- FR-5 does not address the deployer's obligation to inform workers' representatives and affected workers before putting a high-risk AI system into use at the workplace, which is mandatory for recruitment AI under Article 26(7); recruiters alone are not the correct notification target. [medium] - Article 26(7)
- The system must be accompanied by clear instructions for use enabling deployers to interpret outputs appropriately (Art 13); a one-line notification event does not meet this transparency-of-operation standard needed for recruiters to use rankings correctly. [medium] - Article 13(1)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Extend FR-5 to require recruiters be given interpretable explanations of ranking factors and clear guidance enabling them to override, disregard, or halt the automated ranking (Art 14(4)).
- Define and assign human oversight roles to trained, authorized personnel rather than passive notification recipients (Art 26(2)).
- Add a requirement to notify and provide explanations to affected job candidates on request, covering the AI's role and main decision factors (Art 86(1)).
- Add a requirement to inform workers' representatives/affected workers prior to deployment per applicable Union/national information rules (Art 26(7)).
- Accompany the system with documented instructions for use describing capabilities, limitations, and correct interpretation methods for recruiters (Art 13(1)-(2)).

---

### FR-6

**Risk level:** high

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 provides a basic override/reject function for automated candidate rankings but lacks the interpretability, competence-assurance, explanation, and system-halt safeguards the AI Act mandates for human oversight of high-risk recruitment AI, so a recruiter could technically override without meaningfully understanding or being empowered to do so.

**Risks:**

- The requirement does not ensure the recruiter can properly understand the ranking system's capabilities/limitations, correctly interpret its output, or is made aware of automation-bias risk before deciding to override — Article 14(4)(a)-(c) requires the system be designed so overseers meaningfully comprehend and interpret outputs, not merely have a button to reject them. Without this, recruiters may rubber-stamp automated rankings, defeating the purpose of oversight. [high] - Article 14(4)(a)-(c)
- FR-6 gives no mechanism to interrupt or halt the ranking system's operation (a 'stop' function), only to override a per-candidate outcome. Article 14(4)(e) requires the ability to intervene in or interrupt the system's overall operation, which is a distinct oversight capability not covered here. [medium] - Article 14(4)(e)
- The requirement does not require that the recruiter assigned to review/override has the necessary competence, training, authority, and support, which deployers of high-risk AI systems must guarantee. Absent this, override capability may exist technically but be exercised ineffectively, undermining genuine human oversight. [high] - Article 26(2)
- There is no requirement to log the recruiter's oversight actions (review, override, reject) as distinct traceable events, which is needed to demonstrate effective human oversight and support post-market monitoring/incident investigation under the record-keeping obligation for high-risk systems. [medium] - Article 12(1)
- FR-6 does not provide for giving the rejected candidate a clear and meaningful explanation of the AI system's role and the main elements of the decision, which is a right of affected persons subject to decisions based on high-risk AI output in recruitment contexts. [medium] - Article 86(1)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst

**Recommendations:**

- Add UI/design elements enabling the recruiter to view ranking rationale, confidence, and key contributing factors so they can correctly interpret output and detect automation bias before overriding (Art. 14(4)(a)-(c)).
- Add a system-level intervene/stop capability allowing suspension of the ranking process, separate from per-candidate override (Art. 14(4)(e)).
- Define and enforce role-based access ensuring only recruiters with documented competence, training, and authority can perform overrides, and provide ongoing training on system limitations (Art. 26(2)).
- Extend the logging requirement to explicitly capture every review/override/reject action with timestamp, recruiter identity, and rationale as part of the automatic event log (Art. 12(1)).
- Implement a candidate-facing explanation feature disclosing the AI's role and decision rationale upon request for any candidate removed from consideration (Art. 86(1)).

---

### FR-7

**Risk level:** high

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** FR-7 requires logging of key events but omits mandatory retention periods, lifecycle-wide automatic recording, and log-security/traceability safeguards required by Articles 12, 19 and 26 for this Annex III (employment/recruitment) high-risk AI system, creating record-keeping and auditability gaps.

**Risks:**

- FR-7 specifies what to log but sets no retention period; Article 19(1) and Article 26(6) require providers/deployers to keep automatically generated logs for at least six months (or longer if appropriate to intended purpose). Without a defined retention obligation, logs could be deleted prematurely, defeating traceability and audit purposes. [high] - Article 19(1)
- Article 12(1) requires that the system 'technically allow for automatic recording of events (logs) over the lifetime of the system,' i.e. continuous, system-level logging infrastructure, not just logging of five enumerated event types on a per-decision basis. FR-7 is scoped narrowly to score/ranking/explanation/override/decision events and does not guarantee comprehensive lifetime event capture (e.g., system errors, configuration changes, anomalies) needed for risk and substantial-modification detection. [medium] - Article 12(1)
- Article 12(2) requires logging capability to specifically support (a) identifying situations presenting risk under Art.79(1) or substantial modification, (b) post-market monitoring under Art.72, and (c) deployer monitoring under Art.26(5). FR-7 does not tie the logged data elements to these traceability purposes, so logs may be insufficient for post-market monitoring or incident detection obligations. [medium] - Article 12(2)
- Article 26(6) places the retention/control obligation for logs on the deployer 'to the extent such logs are under their control.' FR-7 does not allocate responsibility for log custody, access, or protection between provider and deployer (the recruiting organisation), risking ambiguity over who ensures logs remain available for six months and who secures them against tampering. [medium] - Article 26(6)
- No provision in FR-7 addresses log integrity/security (e.g., tamper-evidence, access control) even though logs of scores, overrides and decisions constitute sensitive personal-data records relevant to non-discrimination claims; absence of integrity safeguards undermines evidentiary value for audits and fundamental-rights impact assessments (Art.27) and market surveillance reviews. [low] - Article 12(2)

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements

**Recommendations:**

- Add an explicit log retention requirement of at least six months (configurable longer per intended purpose), consistent with Article 19(1)/26(6), with automatic enforcement against premature deletion.
- Extend logging scope beyond the five named events to continuous, system-level event capture (errors, anomalies, configuration/version changes) to satisfy Article 12(1)'s lifetime automatic-recording mandate.
- Map each logged data element to its traceability purpose (risk detection, post-market monitoring, deployer operational monitoring) per Article 12(2), and ensure logs feed into the post-market monitoring plan (Art.72).
- Define and document which party (provider vs. deployer/recruiter organisation) controls, stores, and secures each log category, per Article 26(6).
- Implement tamper-evidence/access-control controls on stored logs (e.g., write-once storage, role-based access, cryptographic integrity checks) to preserve audit trail reliability.

---

### FR-8

**Risk level:** high

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** FR-8 requires retaining audit records but omits the mandatory automatic, lifetime logging capability, the minimum six‑month retention period, and the broader event categories (risk‑identification, post‑market monitoring, deployer operational monitoring) that Article 12 and Article 19 require for high‑risk AI systems such as this recruitment screening tool.

**Risks:**

- FR-8 speaks of retaining audit records 'for each screening decision' but does not require the system to technically support automatic recording of events over its entire lifetime, as mandated. Without an explicit automatic, continuous logging capability, the system could rely on manual or selective logging, which would fail the technical requirement that logging be built-in and automatic. [high] - Article 12(1)
- The requirement does not specify any retention duration for audit records. Article 19(1) mandates that logs be kept for a period appropriate to the intended purpose and at least six months. Absent a defined retention period, the implementation risks premature deletion or indefinite retention without justification, both non-compliant. [high] - Article 19(1)
- FR-8 limits traceable content to input data, model version, and human actions. Article 12(2) requires logging capabilities to also capture events relevant to (a) identifying situations that may indicate risk or necessitate substantial modification, (b) facilitating post-market monitoring, and (c) supporting deployer monitoring obligations under Article 26(5). These event categories are not addressed, leaving gaps in risk detection and monitoring support. [medium] - Article 12(2)
- Because logs will be used by deployers (recruiters) to monitor the AI system's operation per Article 26(5), FR-8 does not establish that the audit records are structured or accessible in a way that enables deployer-side operational monitoring (e.g., detecting anomalies, bias drift, or repeated erroneous rankings). This creates a gap between record-keeping and the deployer's statutory monitoring duty. [medium] - Article 26(5)
- The requirement does not clarify who controls/retains the logs (provider vs. deployer) nor how logs will be made available to authorities or the provider upon request, which is implied by Article 19's allocation of log-keeping responsibility to the provider 'to the extent such logs are under their control.' Ambiguous ownership could lead to logs being lost or inaccessible during an audit or incident investigation. [medium] - Article 19(1)

**Cited provisions:**

- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Obligations of deployers of high-risk AI systems, Article 26(5)**
  > 5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and sh

**Recommendations:**

- Explicitly require the system to automatically record all relevant events (logs) continuously over its operational lifetime, not just at the point of a screening decision.
- Add a defined minimum retention period of at least six months (or longer per intended purpose/applicable data-protection law) for all audit records, with a documented deletion/retention policy.
- Extend logged event categories to include indicators of potential risk (e.g., anomalous score distributions, model drift) and data needed for post-market monitoring and deployer operational monitoring, not just input data/model version/human actions.
- Define clear responsibility and access controls for log storage (provider vs. deployer) and ensure logs are retrievable by deployers, market surveillance authorities, and the provider on request.
- Ensure the human oversight and audit-trail records also capture how human reviewers interacted with and could override the system's output, in line with Article 14 human oversight obligations, not only that actions were logged.

---

### FR-9

**Risk level:** high

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** FR-9 only bans certain biometric identification techniques during screening but fails to address that the underlying candidate-scoring/ranking system is itself a high-risk AI system under Annex III(4)(a), leaving mandatory risk-management, human-oversight, transparency and fundamental-rights-impact obligations unaddressed, and it omits the related prohibition on biometric categorisation to infer protected characteristics.

**Risks:**

- FR-9 prohibits 'biometric identification' and 'emotion recognition' but does not prohibit biometric categorisation systems that infer or classify candidates by race, political opinion, trade union membership, religious belief, sex life or sexual orientation from biometric data — a practice separately and absolutely prohibited. As written, the requirement leaves a gap allowing a biometric categorisation module to operate undetected during screening. [high] - Article 5(1)
- The requirement treats biometric/emotion-recognition exclusion as sufficient safeguard but does not acknowledge that a candidate screening and suitability-scoring tool falls within Annex III as a high-risk AI system used for recruitment/selection. Without this classification, the SRS gives no indication that the mandatory risk management system (identification, estimation, evaluation and mitigation of risks over the lifecycle) has been established for the tool, so the broader obligation is effectively unmet. [high] - Article 9(1)
- Although the system routes suitability scores to a 'human recruiter,' FR-9 does not specify human oversight design requirements (ability to understand system limits, detect automation bias, override or halt the system) mandated for high-risk recruitment AI. Merely allowing a human to review output does not satisfy the specific oversight-enablement criteria. [medium] - Article 14(4)
- No provision requires informing candidates or workers that they are subject to a high-risk AI screening/ranking system, which is mandatory for deployers using Annex III recruitment AI, and is distinct from merely avoiding biometric methods. [medium] - Article 26(7)
- There is no requirement to conduct a fundamental rights impact assessment before deploying the candidate-ranking system, which is required for private entities providing public-facing employment services or public bodies using Annex III systems; omitting this leaves unassessed risks of discriminatory impact from the scoring/ranking logic even after biometric methods are excluded. [medium] - Article 27(1)

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have othe
- **Risk management system, Article 9(1)**
  > 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Add an explicit prohibition on biometric categorisation systems inferring protected characteristics (race, political opinion, religion, sexual orientation, etc.) from biometric data, not just facial/biometric identification and emotion recognition, per Article 5(1)(g).
- Classify the candidate screening/ranking system as high-risk under Annex III(4)(a) in the SRS and derive linked requirements from Articles 9, 11, 12, 15 and 17 (risk management, technical documentation, logging, accuracy/robustness, QMS).
- Specify concrete human oversight capabilities (interpret output, detect anomalies/automation bias, override/stop function) per Article 14(4) rather than only 'allow human recruiter review.'
- Add a requirement to notify candidates/workers that a high-risk AI system is used in the recruitment process, per Article 26(7) and Article 13 transparency obligations.
- Add a requirement to perform and document a fundamental rights impact assessment prior to first deployment of the scoring/ranking system per Article 27.

---

### NFR-1

**Risk level:** high

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** NFR-1 only covers basic technical data-cleaning checks (missing values, duplicates, inconsistent labels) but omits the substantive Article 10 data governance obligations—representativeness, bias examination/mitigation, and provenance documentation—that are mandatory for this high-risk recruitment AI system, creating a significant compliance gap for discrimination and fundamental-rights risks.

**Risks:**

- NFR-1 does not require examining datasets for biases likely to cause discrimination or negatively affect fundamental rights, nor implementing measures to detect/prevent/mitigate such biases, despite this being a recruitment scoring system that ranks candidates (FR-2, NFR-3). Data cleaning for missing values/duplicates does not equate to bias examination. [high] - Article 10(2)(f)-(g)
- The requirement does not mandate that datasets be relevant, sufficiently representative, and statistically appropriate for the persons/groups affected (candidates from different demographic groups). Duplicate/missing-value checks do not ensure representativeness, risking skewed or unrepresentative training data that produces discriminatory suitability scores. [high] - Article 10(3)
- No requirement to document data governance practices such as design choices, data collection origin/purpose, and data-preparation operations (annotation, labelling, cleaning, enrichment). Without this documentation, the provider cannot demonstrate compliance during conformity assessment. [medium] - Article 10(2)(a)-(c)
- NFR-1 does not require identifying data gaps or shortcomings that could prevent compliance with the Regulation and how they will be addressed, leaving unresolved data adequacy issues that could propagate into biased or inaccurate candidate rankings. [medium] - Article 10(2)(h)
- If bias correction requires processing special category data (e.g., to test for discrimination on protected attributes), NFR-1 has no provision for the strict safeguards (data minimization, security, deletion after correction) required when processing such special categories, risking unlawful processing under Article 10(5) and GDPR. [medium] - Article 10(5)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Extend validation logic to include statistical bias testing across protected/proxy attributes (e.g., disparate impact analysis) before training, tying into NFR-3 and NFR-5 bias-metric monitoring.
- Add a representativeness assessment step verifying that training/validation/test data adequately reflect the population of candidates the system will screen, with documented statistical properties.
- Require documentation of data provenance, collection purpose, and preparation operations (labelling, annotation, cleaning) as part of the technical documentation package to satisfy Article 10(2)(a)-(c).
- Add a data-gap identification and remediation step, logging any known shortcomings in the dataset and mitigation plans, feeding into ongoing risk management (Article 9).
- If special category data is used for bias detection/correction, implement the safeguards required by Article 10(5) (necessity test, pseudonymisation, restricted access, deletion after correction) and document the justification in records of processing.

---

### NFR-2

**Risk level:** high

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** NFR-2 only requires passive performance measurement across demographic groups contingent on data availability, but fails to mandate the mitigation, continuous monitoring, and lawful-basis safeguards that Articles 9, 10, 15 and 72 require for high-risk AI (this is a recruitment/employment system falling under Annex III), leaving discriminatory bias undetected or uncorrected and creating regulatory non-compliance.

**Risks:**

- The requirement stops at 'measuring' disparities but Article 10(2)(g) mandates providers take 'appropriate measures to detect, prevent and mitigate' identified biases. Measurement without a mandated mitigation/correction action leaves the obligation to actually reduce discriminatory bias unmet. [high] - Article 10(2)(f)-(g)
- By conditioning demographic performance evaluation on 'lawful demographic evaluation data availability,' the requirement provides no fallback or process for the case where such data is unavailable, even though Article 10(5) explicitly permits providers to exceptionally process special category data (with safeguards) specifically to enable bias detection and correction. The requirement does not instruct the system/organization to establish this lawful basis, so bias testing could be perpetually skipped due to data unavailability. [high] - Article 10(5)
- The requirement does not tie demographic performance measurement into the mandatory continuous, lifecycle-wide risk management process (identification, estimation, evaluation, and mitigation of risks to fundamental rights), so disparate performance findings may not feed back into risk controls as required. [high] - Article 9(2)
- Article 15(1) and (3) require high-risk systems to achieve and maintain an appropriate, declared level of accuracy/performance throughout their lifecycle, including declaring accuracy metrics in the instructions of use. NFR-2 only measures group-level performance internally with no requirement to declare metrics or set/maintain minimum accuracy thresholds per group. [medium] - Article 15(3)
- There is no requirement to continuously and systematically monitor for demographic performance drift post-deployment (post-market monitoring), meaning bias emerging after deployment (e.g., due to feedback loops per Art 15(4)) would not be detected or documented over the system's lifetime. [medium] - Article 72(2)
- As a recruitment/employment-related high-risk AI system (Annex III use case), demographic disparate-impact findings should inform the Fundamental Rights Impact Assessment; NFR-2 does not reference or feed results into this assessment, risking an incomplete or stale FRIA. [medium] - Article 27(1)
- The requirement does not specify that biases examined must cover impacts on health, safety, or fundamental rights, or discrimination prohibited under Union law, as Article 10(2)(f) requires; without this scope, 'measuring performance' could be limited to generic accuracy stats rather than discrimination-relevant metrics (e.g., false positive/negative rate parity). [medium] - Article 10(2)(f)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Add an explicit bias mitigation/correction workflow triggered whenever demographic performance disparities exceed a defined threshold, per Art 10(2)(g).
- Define a lawful data governance process (with safeguards) for collecting special-category demographic data for bias testing under Art 10(5), rather than leaving evaluation optional based on ad hoc data availability.
- Integrate demographic performance monitoring into the continuous risk management system (Art 9) so findings trigger risk re-evaluation and mitigation measures.
- Require declaration of accuracy/performance metrics, including per-group metrics, in the system's instructions of use per Art 15(3).
- Extend demographic performance checks into the mandatory post-market monitoring plan to detect drift and feedback-loop bias after deployment (Art 72).
- Link demographic bias findings to the Fundamental Rights Impact Assessment update cycle for this employment-related high-risk system (Art 27).
- Specify that bias measurement must cover discrimination-relevant metrics (e.g., error-rate parity, false negative/positive rates by group) tied to health, safety and fundamental-rights impacts, not just generic accuracy (Art 10(2)(f)).

---

### NFR-3

**Risk level:** high

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** NFR-3 only bans direct use of protected attributes as ranking inputs but fails to address proxy/indirect discrimination and the broader data governance and bias-mitigation obligations required for this high-risk recruitment AI system under Article 10, leaving the system exposed to discriminatory outcomes through correlated variables.

**Risks:**

- The requirement excludes protected attributes as direct inputs but does not require examination for proxies (e.g., postal code, name, employment gaps, school attended) that correlate with race, disability, religion or political opinion. Article 10(2)(f) mandates examination of possible biases 'likely to...lead to discrimination prohibited under Union law', which covers indirect/proxy discrimination, not just explicit protected-attribute fields. Without this, the ranking model can still produce discriminatory suitability scores while technically satisfying NFR-3. [high] - Article 10(2)(f)-(g)
- NFR-3 sets a static prohibition but does not require the mandated data governance practices (design choices, data origin, data-preparation operations, assumptions, gap identification) needed to substantiate that ranking inputs are actually free of embedded bias. A bare non-use rule for named attributes does not satisfy the documented governance process Article 10(2) requires for training/validation/testing data of a high-risk system. [medium] - Article 10(2)
- The requirement does not reference the statistical representativeness and completeness obligations for datasets used to rank candidates. Article 10(3) requires that training/validation/testing data be relevant, sufficiently representative and have appropriate statistical properties as regards persons or groups affected by the system's use — necessary to detect skewed outcomes even when protected attributes are excluded from inputs. [medium] - Article 10(3)
- There is no explicit tie between NFR-3 and an ongoing risk-management process. Article 9 requires continuous identification, estimation, and mitigation of risks to fundamental rights (including discrimination risk) throughout the AI system's lifecycle, not merely a one-time design constraint on ranking inputs. NFR-3 as written is a static feature rule, not a lifecycle risk control. [medium] - Article 9(2)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est

**Recommendations:**

- Extend the requirement to mandate bias examination and mitigation for proxy/correlated variables (not just explicitly named protected attributes), per Article 10(2)(f)-(g).
- Add a requirement for documented data governance practices covering data origin, preparation, and assumptions for all ranking-input features, per Article 10(2).
- Add a requirement to validate statistical representativeness of training/validation/testing datasets across protected groups per Article 10(3), including periodic bias metric testing (tie into NFR-5 monitoring).
- Incorporate the non-use-of-protected-attributes rule into the documented risk management system (Article 9) as a continuously monitored control rather than a static design-time exclusion.

---

### NFR-4

**Risk level:** high

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 defines access control only in terms of authorisation to view candidate data and explanations but omits the competence/training criteria for human overseers, audit-trail/log-access requirements, and cybersecurity resilience obligations that the AI Act mandates for high-risk recruitment AI systems, leaving the control functionally incomplete and unauditable.

**Risks:**

- The requirement restricts viewing to 'authorised recruitment staff' but does not require that these staff have the necessary competence, training and authority to exercise human oversight, as mandated for deployers assigning oversight of high-risk AI systems. Merely granting view access does not ensure the person can properly interpret outputs, detect anomalies or override the system. [high] - Article 26(2)
- Access control as specified only gates 'viewing' of data and explanations; it does not address resilience against unauthorised alteration of the system's outputs, model, or access records by third parties exploiting vulnerabilities, which is a mandatory cybersecurity requirement for high-risk AI systems used in recruitment. [high] - Article 15(5)
- The requirement does not tie access restriction to the mandatory event-logging/traceability capability; there is no requirement to record who accessed candidate data/explanations and when, which is necessary to identify risk-presenting situations and to support post-market monitoring and audits. [medium] - Article 12(2)
- Candidate data likely includes personal and potentially special-category data used for bias detection; the requirement lacks the documented, strict-control access regime (e.g., logging of access, confidentiality obligations, restrictions on re-use/transfer) required when such data is processed under the data-governance provisions, creating a gap in demonstrable compliance with data protection safeguards. [medium] - Article 10(5)(c)
- No retention or access-log-keeping period is specified for records of who accessed candidate data/explanations, risking failure to meet the deployer obligation to retain automatically generated logs for at least six months (or a period appropriate to intended purpose), undermining traceability for audits or incident investigations. [medium] - Article 26(6)

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements

**Recommendations:**

- Define and document the competence, training and authority criteria that 'authorised recruitment staff' must meet before being granted access, aligned with human oversight assignment duties.
- Extend access controls to explicitly prevent unauthorised modification/tampering of candidate data, scores and explanations, not just unauthorized viewing, and apply state-of-the-art cybersecurity measures (encryption, integrity checks).
- Integrate access events (who viewed candidate data/explanations, when) into the system's automatic event-logging capability to support traceability and post-market monitoring.
- Establish documented access-control procedures for any special-category data used in bias detection, including confidentiality obligations and restrictions on re-use/transfer, per Article 10(5).
- Set and enforce a minimum retention period (at least six months) for access/audit logs tied to candidate data and explanation views, consistent with deployer log-retention obligations.

---

### NFR-5

**Risk level:** high

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** NFR-5 only specifies threshold-based alerting but omits the documented post-market monitoring system, incident-reporting triggers, logging/retention, risk-management feedback loop, and human-oversight accountability that the AI Act requires around such monitoring, leaving the requirement non-compliant on its own.

**Risks:**

- The requirement describes ad-hoc alerting but does not establish a documented, systematic post-market monitoring system or plan that actively collects and analyses performance data throughout the system's lifetime, as mandated for providers of high-risk AI systems (this is a recruitment/employment system, which is Annex III high-risk). [high] - Article 72(1)
- No provision links threshold breaches (e.g., accuracy or bias degradation indicating a risk to fundamental rights) to the mandatory serious-incident reporting obligation, including the 15-day (or 10-day for death/serious harm) deadline to notify the provider, market surveillance authority, and to suspend use where risk is identified. [high] - Article 73(2)
- Alerts are not grounded in an automatic event-logging capability covering the system's lifetime, nor is a minimum 6-month log retention period specified, so the data needed to detect, investigate, and prove threshold breaches may not be technically captured or preserved. [medium] - Article 12(1)
- There is no mechanism feeding monitoring alert data back into the risk management system to re-evaluate and update risk mitigation measures, as required when post-market monitoring reveals new or evolving risks (e.g., bias drift). [medium] - Article 9(2)(c)
- The requirement does not assign responsibility to a competent human overseer to review, interpret, and act on the alerts (e.g., detecting anomalies/dysfunctions and avoiding automation bias), leaving a gap in the human oversight obligation. [medium] - Article 14(4)
- 'Configured thresholds' for accuracy are not tied to accuracy metrics and levels that must be declared in the instructions for use, so alert thresholds may be arbitrary rather than aligned with disclosed performance levels. [low] - Article 15(3)
- 'Data quality checks' are undefined relative to the data governance quality criteria (representativeness, bias examination, error-freeness) that training/validation/testing data sets must meet, risking checks that don't actually verify Article 10 compliance. [low] - Article 10(3)

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Reporting of serious incidents, Article 73(2)**
  > 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Define and document a post-market monitoring plan (per Article 72 and Annex IV) specifying data sources, analysis methods, and how alert data feeds continuous compliance evaluation.
- Add explicit incident-escalation logic: when alerts indicate a possible Article 79(1) risk or serious incident, trigger supplier/deployer notification and market surveillance authority reporting within the mandated 10/15-day windows, and require use suspension.
- Implement automatic event logging underlying all monitored metrics, retained for at least 6 months (or longer per Article 19), to support traceability of alert triggers.
- Establish a feedback process so alert outputs update the documented risk management system's risk estimation and mitigation measures.
- Assign a named, competent human overseer role responsible for reviewing and acting on alerts, with defined escalation authority.
- Align accuracy alert thresholds with the accuracy metrics/levels declared in the system's instructions for use.
- Specify that 'data quality checks' validate the Article 10(2)-(3) governance criteria (representativeness, completeness, bias detection) rather than generic quality metrics.

---

### NFR-6

**Risk level:** high

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** NFR-6 only vaguely commits to optional rollback capability without binding triggers, logging, human-oversight control, or incident/authority notification duties that the AI Act mandates when a high-risk AI system (this CV-screening/recruitment tool falls under Annex III employment use-cases) fails safety, robustness or fairness checks.

**Risks:**

- The requirement uses 'should support' rather than a mandatory 'shall', making rollback optional. Article 15(1) requires high-risk systems to 'achieve an appropriate level of accuracy, robustness and cybersecurity' and 'perform consistently... throughout their lifecycle' as a binding obligation, and Article 15(4) requires resilience measures including 'backup or fail-safe plans' to be actually implemented, not merely supported as a nice-to-have. [high] - Article 15(4)
- No defined thresholds/metrics for what constitutes a 'failed' safety, robustness or fairness check. Article 15(3) requires accuracy/robustness metrics to be declared in instructions of use, and Article 9's risk management system requires continuous, documented evaluation criteria; without these, the rollback trigger is undefined and unauditable. [high] - Article 9(2)
- No requirement to log rollback events or the anomaly/failure that triggered them. Article 12 mandates automatic recording of events relevant to identifying risk situations and facilitating post-market monitoring; NFR-6 has no logging obligation tied to rollback actions. [high] - Article 12(2)
- No obligation to notify deployers, distributors, importers or market surveillance authorities when a rollback/corrective action is taken. Article 20(1)-(2) requires providers to immediately take corrective action AND inform affected parties/authorities of non-conformity and the nature of the issue; NFR-6 stops at the technical rollback capability. [high] - Article 20(1)
- No linkage to serious incident reporting timelines. If a safety/fairness failure in a recruitment system constitutes a 'serious incident' (e.g., discriminatory harm), Article 73 requires reporting to market surveillance authorities within 15 days (or 2/10 days for severe cases) after becoming aware - NFR-6 has no such reporting trigger. [medium] - Article 73(2)
- No human oversight mechanism specified for authorizing, verifying, or manually triggering rollback. Article 14 requires human overseers to be able to detect and address anomalies/dysfunctions and intervene in system operation; NFR-6 describes an automated/system-level rollback without specifying human control or approval in the loop. [medium] - Article 14(4)
- Rollback is not integrated into the provider's quality management system's change-management and post-market monitoring procedures. Article 17(1)(a) and (h) require documented strategies for managing modifications and post-market monitoring; NFR-6 treats rollback as an isolated technical feature rather than a governed process. [medium] - Article 17(1)

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ
- **Reporting of serious incidents, Article 73(2)**
  > 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Quality management system, Article 17(1)**
  > 1. Providers of high-risk AI systems shall put a quality management system in place that ensures compliance with this Regulation. That system shall be documented in a systematic and orderly manner in the form of written policies, procedures and instructions, and shall include at least the following aspects: (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system; (b) techniq

**Recommendations:**

- Change 'should support' to a mandatory 'shall' and define rollback as a required fail-safe/backup mechanism per Article 15(4).
- Define explicit, documented thresholds and metrics for safety/robustness/fairness failures tied to the Article 9 risk management system and Article 15(3) declared accuracy metrics.
- Require automatic logging of all events leading to and resulting from a rollback, including timestamps, failure type, and model versions, per Article 12(2).
- Add a corrective-action workflow that notifies deployers, distributors, importers and market surveillance authorities per Article 20(1)-(2) whenever a rollback is triggered due to non-conformity.
- Add serious incident assessment and reporting logic (15/2/10-day deadlines per Article 73) triggered when a rollback follows a safety or fairness failure with potential harm.
- Specify human oversight controls allowing authorized personnel to review, approve, or manually initiate rollback, per Article 14(4).
- Document the rollback mechanism within the quality management system's change-management and post-market monitoring procedures per Article 17(1)(a) and (h).

---
