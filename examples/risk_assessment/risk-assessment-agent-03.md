# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 15
- Medium: 1

## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** FR-1 only specifies raw data ingestion for a recruitment system that squarely falls under Annex III as high-risk AI (employment/recruitment screening), but it omits the data governance, transparency, and documentation obligations that must attach to that ingestion step, exposing the system to non-compliance from the very first processing stage.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** FR-10 only offers candidates a channel to 'request' review of an automated ranking decision but does not guarantee the substantive rights and processes the AI Act requires around such review, creating exposure under transparency, explanation and human-oversight provisions.

**Risks:**

- The requirement does not obligate the system/deployer to provide the affected candidate with a 'clear and meaningful explanation' of the AI system's role and the main elements of the decision, which is the core content Article 86 mandates be given upon request, not merely a channel to ask for review. [high] - Article 86(1)
- FR-10 does not require that the candidate first be informed that they are subject to a decision made or assisted by a high-risk AI system, a precondition for candidates to know they even have a basis to request review. [high] - Article 26(11)
- Providing a 'channel to request review' does not ensure that a competent human recruiter with authority actually reviews, can override, or disregard the automated ranking output, so the requirement does not satisfy the human oversight obligation of ensuring meaningful human intervention. [high] - Article 14(4)
- The requirement lacks any tie to human oversight being assigned to persons with necessary competence, training and authority to act on review requests, leaving the review channel potentially superficial (a 'rubber stamp'). [medium] - Article 26(2)
- FR-10 does not reference or preserve the candidate's independent right to lodge a complaint with a market surveillance authority, so the internal review channel could be mistaken as the sole remedy, understating the candidate's statutory rights. [low] - Article 85

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Right to lodge a complaint with a market surveillance authority**
  > Without prejudice to other administrative or judicial remedies, any natural or legal person having grounds to consider that there has been an infringement of the provisions of this Regulation may submit complaints to the relevant market surveillance authority. In accordance with Regulation (EU) 2019/1020, such complaints shall be taken into account for the purpose of conducting market surveillance activities, and shall be handled in line with the dedicated procedures established therefor by the 

**Recommendations:**

- Extend FR-10 to require the deployer to provide, on request, a clear and meaningful explanation of the AI system's role and the main decision elements (Art. 86(1)).
- Add a requirement to notify candidates upfront that an automated ranking system influenced their evaluation, before any review is requested (Art. 26(11)).
- Define that the review channel routes to a human recruiter with authority and competence to override, reject, or reverse the automated ranking, not just log a request (Art. 14(4), Art. 26(2)).
- Specify SLAs/process for handling review requests, including documentation of the outcome for audit purposes.
- Add disclosure text informing candidates of their independent right to lodge a complaint with the relevant market surveillance authority (Art. 85).

---















































### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** FR-2 defines a candidate-scoring function for employment decisions without addressing the data quality, bias-mitigation, risk-management, or fundamental-rights safeguards mandated for high-risk AI systems used in recruitment (Annex III, point 4), creating exposure to discriminatory outcomes and non-compliance.

**Risks:**

- The requirement does not specify data governance or bias examination/mitigation for the training, validation and testing data used to compute the score, risking discriminatory outcomes against protected groups in violation of Article 10(2)(f)-(g). [high] - Article 10(2)(f)-(g)
- No accuracy, robustness or predefined testing metrics/thresholds are specified for the scoring model, failing the risk-management and testing obligations that require systematic risk identification and validation throughout the lifecycle. [high] - Article 9(8)
- There is no continuous risk-management process (identification, estimation, mitigation of health/safety/fundamental-rights risks) established for the scoring system as required for high-risk AI systems. [high] - Article 9(2)
- The requirement omits provider instructions for use (accuracy metrics, known limitations, foreseeable misuse) needed to allow deployers to interpret and appropriately act on the suitability score, undermining transparency obligations. [medium] - Article 13(3)
- No mechanism is included for informing affected candidates/workers that they are subject to an automated high-risk scoring system, a deployer transparency obligation tied to this functionality. [medium] - Article 26(7)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.

**Recommendations:**

- Define and document data governance measures, including bias detection/mitigation and representativeness checks, for all data used to generate the suitability score (Art. 10).
- Establish a documented, lifecycle-wide risk management process identifying and mitigating fundamental rights risks from the scoring logic (Art. 9).
- Set and test explicit accuracy/robustness metrics and thresholds for the scoring model prior to deployment (Art. 9(8)/Art. 15).
- Produce instructions for use covering intended purpose, accuracy metrics, limitations and foreseeable misuse so deployers can correctly interpret scores (Art. 13).
- Add a workflow step to notify workers/candidates that a high-risk AI scoring system is being used, per employer transparency duties (Art. 26(7)).

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** FR-3 implements a core function of a high-risk employment AI system (Annex III recruitment use) but, taken on its own, lacks safeguards against automation bias and does not ensure the ranking remains a genuine decision-support aid rather than a de facto automated exclusion mechanism, risking violation of the human oversight and accuracy obligations of Articles 14 and 15.

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** FR-4 covers recruiter-facing score explanations but omits the candidate's statutory right to an explanation of automated employment decisions and lacks the fuller transparency/instructions-for-use content required for high-risk AI systems used in recruitment.

**Risks:**

- FR-4 only addresses explanations for the recruiter, but Article 86 gives the affected candidate a right to obtain from the deployer a clear and meaningful explanation of the AI system's role in the decision and the main elements of the decision, which is entirely unaddressed. [high] - Article 86(1)
- FR-4 does not specify that the system must produce instructions for use/documentation on its technical capacity to explain outputs, its intended purpose, accuracy metrics, and known risks to fundamental rights, as required for transparency to deployers under Article 13(2)-(3), so the recruiter cannot fully interpret and use the score appropriately. [medium] - Article 13(3)
- The requirement does not ensure the explanation supports correct interpretation of output to counter automation bias or enable recruiters to detect anomalies/dysfunctions, a core human oversight enabler under Article 14(4)(a)-(c) for recommendation systems used in decisions about people. [medium] - Article 14(4)
- There is no requirement that the explanation be tied to bias detection/mitigation in the scoring, even though recruitment scoring based on resumes/cover letters is highly susceptible to discriminatory bias that Article 10(2)(f)-(g) requires be examined and mitigated in data governance, and the explanation should surface such bias-relevant factors. [medium] - Article 10(2)
- FR-4 does not require informing candidates that they are subject to an AI-based decision system, a separate deployer obligation under Article 26(11) that is a precondition for candidates being able to exercise their explanation rights. [low] - Article 26(11)

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.

**Recommendations:**

- Add a requirement implementing Article 86: enable deployers to provide affected candidates, upon request, with a clear and meaningful explanation of the AI system's role and the main elements of the ranking/rejection decision.
- Extend instructions-for-use/documentation to include intended purpose, accuracy/robustness metrics, known risks to fundamental rights, and the system's technical capacity to explain outputs, per Article 13(2)-(3).
- Design explanations to flag automation-bias risk indicators and support anomaly detection by recruiters, per Article 14(4)(a)-(c).
- Ensure explained 'main factors' are cross-checked against bias examination/mitigation measures from data governance (Article 10) so discriminatory factors are surfaced and mitigated, not just described.
- Add a requirement to notify candidates that they are subject to an AI-based scoring/ranking system, per Article 26(11).

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** FR-5 only notifies recruiters that a ranking was AI-generated but omits the mandatory transparency obligations toward the affected job candidates themselves, creating a significant compliance gap for a high-risk recruitment AI system under Annex III.

**Risks:**

- The requirement notifies recruiters but does not require informing the affected natural persons (job candidates) that they are subject to a high-risk AI system, which Article 26(11) mandates for deployers of Annex III systems that make or assist decisions about individuals. [high] - Article 26(11)
- The requirement does not provide affected candidates with a right to obtain clear and meaningful explanations of the AI system's role in adverse ranking/rejection decisions, as required for individuals significantly affected by high-risk AI outputs. [high] - Article 86(1)
- For workplace deployment, the requirement does not address the deployer's obligation to inform workers' representatives and affected workers before putting the system into service, which is distinct from merely notifying recruiters. [medium] - Article 26(7)
- The requirement lacks any reference to conducting or supporting a fundamental rights impact assessment prior to first use, which is required for certain employment-related Annex III deployments and should be reflected in system documentation/notification workflows. [medium] - Article 27(1)
- The notification to recruiters does not specify that it must occur in a manner enabling recruiters to properly interpret system output and avoid automation bias, a transparency element required to be built into system design. [low] - Article 13(1)

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(7)**
  > 7. Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers’ representatives and the affected workers that they will be subject to the use of the high-risk AI system. This information shall be provided, where applicable, in accordance with the rules and procedures laid down in Union and national law and practice on information of workers and their representatives.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add a requirement that the system informs each affected candidate, before or at the point of decision, that a high-risk AI system was used in ranking/evaluating their application.
- Implement a candidate-facing explanation feature that provides clear, meaningful reasons for adverse ranking outcomes, satisfying the Article 86 right to explanation.
- Add a requirement for the deployer workflow to notify workers' representatives and affected employees/candidates before the system is put into service, per Article 26(7).
- Incorporate a fundamental rights impact assessment step (or reference to one) into the deployment process prior to first use of the ranking model.
- Extend the recruiter-notification feature to include design elements that mitigate automation bias and confirm recruiters can properly interpret the AI-generated explanation, per Article 13(1).

---

### FR-6

**Risk level:** high

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** FR-6 satisfies the narrow 'override/reverse output' element of Article 14(4)(d), but the recruitment AI system (an Annex III high-risk employment/candidate-selection system) also requires competence and training of the human reviewer, safeguards against automation bias, explainability to affected candidates, audit logging, and a fundamental rights impact assessment — none of which are addressed by this requirement alone.

**Risks:**

- The requirement does not ensure the recruiter has the necessary competence, training, authority and support to properly exercise oversight, as mandated for deployers assigning human oversight of high-risk AI systems. [high] - Article 26(2)
- The requirement lacks any provision to make the recruiter aware of automation bias / over-reliance on the automated ranking, or to ensure they can correctly interpret the ranking output before deciding to override or reject a candidate, which Article 14 requires to be designed into the human oversight interface. [high] - Article 14(4)(b)-(c)
- There is no mechanism ensuring rejected/deprioritized candidates receive a clear and meaningful explanation of the AI's role in the decision, which is required whenever a high-risk AI decision produces legal or similarly significant effects on a person, as recruitment decisions do. [high] - Article 86(1)
- The requirement omits any obligation to retain automatically generated logs of ranking outputs and recruiter overrides, which deployers of high-risk AI systems must keep for at least six months to enable auditability and incident investigation. [medium] - Article 26(6)
- The requirement does not address the prerequisite fundamental rights impact assessment that must be performed before deploying a high-risk recruitment AI system, including description of human oversight implementation and risk mitigation measures. [medium] - Article 27(1)

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI syst
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Add a functional requirement mandating documented competence/training criteria and authority for recruiters assigned to oversee the ranking system, per Art. 26(2).
- Add UI/process controls that surface automation-bias warnings and interpretability aids (e.g., ranking rationale, confidence scores) to the recruiter before any override decision, per Art. 14(4)(b)-(c).
- Add a requirement to generate and deliver a clear, meaningful explanation of the AI's role and decision factors to any candidate removed from consideration, per Art. 86(1).
- Add a logging requirement capturing ranking outputs, recruiter reviews, and override/reject actions with a minimum 6-month retention period, per Art. 26(6).
- Add a pre-deployment fundamental rights impact assessment covering the recruitment use case, affected candidate groups, and oversight design, per Art. 27(1).

---

### FR-7

**Risk level:** high

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** FR-7 lists the events to be logged but omits the mandatory technical, retention, and traceability characteristics required for high-risk AI logging under the Act, leaving the recruitment screening system's audit trail legally insufficient.

**Risks:**

- FR-7 does not specify a minimum retention period for the logs, whereas Article 19(1)/26(6) require providers/deployers to keep automatically generated logs for at least six months (or longer per applicable law). [high] - Article 19(1)
- The requirement does not state that logs must be automatically and technically generated over the system's lifetime, only that certain events are 'logged', missing the Article 12(1) mandate for built-in automatic event recording capability. [high] - Article 12(1)
- FR-7 does not capture timestamps for the start/end of each use session or link logs to the model version and input data used, so it cannot support traceability for risk/incident detection or post-market monitoring as required by Article 12(2)(a)-(c). [high] - Article 12(2)
- The requirement does not assign responsibility for keeping logs 'to the extent under their control' as deployer, creating ambiguity on who (provider vs. employer/deployer) is obligated to retain and secure the recruitment screening logs under Article 26(6). [medium] - Article 26(6)
- FR-7 does not require identification of the natural person(s) who performed the human oversight/override, undermining accountability for human review events mandated alongside logging obligations. [medium] - Article 12(3)

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements
- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Add explicit minimum 6-month (or longer, per applicable law) log retention requirement, with configurable extension, per Article 19(1)/26(6).
- Ensure logging is implemented as an automatic, tamper-evident technical capability spanning the full system lifetime per Article 12(1), not just an application-level record of listed events.
- Extend log schema to capture session start/end timestamps, model version, and input data references to enable traceability for risk detection and post-market monitoring per Article 12(2).
- Clarify in the requirement which party (provider vs. deploying employer) is responsible for log retention and control, aligning with Article 26(6) deployer obligations.
- Include the identity/role of the human reviewer performing each override in the logged record to satisfy human-oversight traceability expectations.

---

### FR-8

**Risk level:** high

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** FR-8 requires audit-record retention but omits the mandatory minimum retention period, automatic lifecycle logging, and the specific log content categories mandated for high-risk AI systems used in recruitment, creating a compliance gap under Articles 12, 19 and 26.

**Risks:**

- FR-8 does not specify any retention period for audit records, while Article 19(1) and Article 26(6) require providers/deployers to keep automatically generated logs for at least six months (or longer if appropriate to the intended purpose), risking premature deletion of records needed for oversight. [high] - Article 19(1)
- The requirement does not mandate that logging be automatic and continuous 'over the lifetime of the system' as required by Article 12(1); relying only on 'retaining audit records for each screening decision' may miss system-level events (e.g., configuration changes, downtime) needed for full traceability. [high] - Article 12(1)
- FR-8 does not ensure logging captures events relevant to identifying risk situations, substantial modifications, or supporting post-market monitoring as required by Article 12(2), limiting the audit trail's usefulness for regulatory oversight beyond individual decision traceability. [medium] - Article 12(2)
- As a deployer-side obligation, the requirement does not address that deployers of this employment-related high-risk AI system must themselves keep the logs under their control for the statutory period, distinct from provider retention, leaving deployer compliance unaddressed. [medium] - Article 26(6)
- The requirement does not tie audit records to enabling human overseers to properly understand and monitor the system's operation (e.g., detecting anomalies or unexpected performance), so the audit trail may not support the oversight obligations imposed on deployers/recruiters. [low] - Article 14(4)

**Cited provisions:**

- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s
- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Add an explicit minimum retention period of at least six months (or longer per intended purpose/GDPR constraints) for all audit/log records per Article 19(1)/26(6).
- Specify that logging must be automatic and run continuously over the entire operational lifetime of the system, not just per screening decision, per Article 12(1).
- Expand log content requirements to include events relevant to risk detection, substantial modification identification, and post-market monitoring per Article 12(2).
- Add a distinct deployer-side requirement confirming logs remain under deployer control and are retained per statutory minimums, separate from provider retention duties.
- Link audit record content/design to human oversight needs (e.g., enabling detection of anomalies/dysfunctions) so records support Article 14(4) oversight capabilities.

---

### FR-9

**Risk level:** high

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** FR-9 states a blanket prohibition but doesn't tie it to the specific legal basis (Art. 5(1)(f) emotion recognition in workplace) or address that the underlying recruitment/candidate-screening system itself is a high-risk AI system under Annex III, so the broader set of high-risk obligations (risk management, human oversight, data governance, transparency) is not triggered or verified by this requirement alone.

---

### NFR-1

**Risk level:** high

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** NFR-1 only checks basic data cleanliness (missing values, duplicates, inconsistent labels) but omits the substantive data governance and quality obligations mandated by Article 10 for high-risk AI systems, most notably bias examination/mitigation and representativeness assessment, exposing the system to non-compliance if it is high-risk.

**Risks:**

- The requirement contains no process to examine training/validation data for biases likely to affect health, safety, fundamental rights or lead to discrimination, nor measures to detect/prevent/mitigate such biases, which is a mandatory governance practice. [high] - Article 10(2)(f)-(g)
- The requirement does not verify that data sets are relevant, sufficiently representative, statistically appropriate, and complete for the intended purpose, focusing only on syntactic errors (missing values/duplicates) rather than substantive quality/representativeness required by law. [high] - Article 10(3)
- No governance practices are specified for documenting design choices, data collection origin/purpose, data-preparation operations (annotation, labelling, cleaning, enrichment), or identification of data gaps/shortcomings, all of which Article 10(2) requires as part of data governance. [medium] - Article 10(2)(a)-(e),(h)
- The requirement limits validation to 'before model training,' but Article 10 quality criteria apply to training, validation AND testing data sets whenever used, so testing-set validation and ongoing quality assurance are not addressed. [medium] - Article 10(1)
- There is no linkage to technical documentation obligations that must record the data governance measures and quality checks performed, risking incomplete documentation for conformity assessment. [medium] - Article 11(1)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Data and data governance, Article 10(1)**
  > 1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used.
- **Technical documentation, Article 11(1)**
  > 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI syste

**Recommendations:**

- Add explicit bias examination and mitigation checks (statistical parity, subgroup performance analysis) to the data validation pipeline, per Art.10(2)(f)-(g).
- Extend validation criteria to include representativeness, statistical property checks, and completeness assessment relative to intended use, not just structural errors.
- Document and implement governance practices covering data provenance, collection purpose, preparation operations, and identified data gaps as part of the pipeline design.
- Apply the same quality validation to testing data sets and any updated/retrained data, not only pre-training data.
- Ensure validation outputs and governance decisions are captured in technical documentation to satisfy Annex IV/Article 11 requirements.

---

### NFR-2

**Risk level:** high

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** NFR-2 conditions demographic performance measurement on data availability without establishing the mandatory bias-mitigation lifecycle, safeguards for processing special category data, or documentation obligations required for high-risk AI used in recruitment, leaving the system exposed to non-compliance with Articles 9, 10 and 15.

---

### NFR-3

**Risk level:** high

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** NFR-3 only bans direct use of protected attributes as ranking inputs, but the AI Act's employment/recruitment high-risk system obligations (Annex III(4)) require far broader bias governance—including detection of proxy/indirect discrimination, statistical representativeness testing, and lifecycle bias mitigation—none of which are addressed, leaving the system exposed to prohibited discriminatory outcomes via correlated features.

**Risks:**

- Excluding protected attributes as explicit inputs does not prevent proxy variables (e.g., zip code, name, school, gaps in employment) from encoding race, disability or religion, so the requirement fails to satisfy the Article 10(2)(f)-(g) obligation to examine and mitigate bias in training/validation/testing data that could lead to prohibited discrimination. [high] - Article 10(2)(f)-(g)
- There is no requirement to ensure the datasets are relevant, sufficiently representative and statistically balanced with respect to affected persons/groups, which Article 10(3) mandates for high-risk systems to prevent skewed outcomes for protected groups. [high] - Article 10(3)
- NFR-3 addresses only a single input-exclusion rule and omits the overarching, continuous risk management process (identification, evaluation and mitigation of fundamental-rights risks such as discrimination) required for this employment-related high-risk AI system throughout its lifecycle. [high] - Article 9(2)
- The requirement does not specify any testing, validation or ongoing monitoring for disparate impact on protected groups after deployment, missing the accuracy/robustness verification obligations tied to fundamental-rights risk mitigation. [medium] - Article 15(1)
- No provision requires documenting how bias-related design choices and data-preparation decisions were made, which is needed to demonstrate compliance with data governance and to support technical documentation under Article 11. [medium] - Article 10(2)(a)-(c)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

**Recommendations:**

- Extend the requirement to include proxy-variable detection and mitigation (e.g., correlation analysis between non-protected features and protected attributes) per Article 10(2)(f)-(g).
- Add a data governance control validating that training/validation/testing datasets are representative and statistically balanced across protected groups per Article 10(3).
- Integrate protected-attribute exclusion into a documented, iterative risk management system covering identification, evaluation and mitigation of discrimination risk per Article 9.
- Add post-deployment monitoring/testing for disparate impact on protected groups to satisfy accuracy/robustness obligations under Article 15.
- Require documentation of data-preparation and design choices related to bias mitigation to support technical documentation obligations under Article 10(2)(a)-(c) and Article 11.

---

### NFR-4

**Risk level:** high

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** NFR-4 only restricts data/explanation viewing to authorised staff but ignores mandatory obligations for employment-related high-risk AI systems (Annex III, point 4) such as competent human oversight, candidate transparency, logging, fundamental rights impact assessment, and broader cybersecurity resilience — leaving the system exposed to non-compliance beyond simple access authorisation.

**Risks:**

- Restricting viewing to 'authorised recruitment staff' does not ensure those staff have the necessary competence, training and authority to exercise meaningful human oversight of model explanations, as required for high-risk employment AI systems. [high] - Article 26(2)
- The requirement contains no mechanism to inform candidates that they are subject to an AI system's decision-making, a mandatory deployer transparency obligation for Annex III systems affecting natural persons. [high] - Article 26(11)
- Access control alone does not guarantee automatic logging of who accessed candidate data/explanations and when, undermining traceability and post-market monitoring obligations for high-risk systems. [medium] - Article 12(1)
- No provision addresses conducting a fundamental rights impact assessment before deployment, which is required for employment-related high-risk AI systems given discrimination/bias risks to candidates. [medium] - Article 27(1)
- Access controls address unauthorized viewing but do not satisfy the broader cybersecurity resilience requirement against manipulation, data poisoning, or confidentiality attacks mandated for high-risk AI systems. [medium] - Article 15(5)

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to 

**Recommendations:**

- Define human oversight roles with documented competence, training and authority requirements for staff reviewing model explanations (Art. 26(2)).
- Implement a candidate-facing notice mechanism informing individuals they are subject to an AI-assisted recruitment decision (Art. 26(11)).
- Extend logging so all access events to candidate data and explanations are automatically recorded with timestamps and user identity (Art. 12(1)).
- Conduct and document a fundamental rights impact assessment prior to first use of the recruitment AI system (Art. 27(1)).
- Implement broader cybersecurity controls (adversarial robustness, data/model poisoning protections) beyond role-based access control (Art. 15(5)).

---

### NFR-5

**Risk level:** high

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** NFR-5 only defines threshold-based alerting for accuracy, bias, and data quality but does not establish the underlying post-market monitoring system, declared performance metrics, or escalation/reporting workflow required for a high-risk AI recruitment system, so triggering an alert does not by itself satisfy the Act's continuous compliance, incident-reporting, and human-oversight obligations.

**Risks:**

- The requirement does not tie 'configured thresholds' to accuracy levels and metrics that must be formally declared in the instructions of use, so there is no documented basis for what constitutes an acceptable deviation. [high] - Article 15(3)
- Producing alerts is not equivalent to establishing and documenting a proportionate post-market monitoring system/plan that actively and systematically collects and analyses performance data to evaluate continuous compliance with Chapter III Section 2 requirements. [high] - Article 72(1)
- No mechanism is specified for escalating threshold breaches into the mandatory serious-incident reporting chain to the provider, distributor, and market surveillance authorities, risking failure to report incidents that could affect health, safety or fundamental rights. [high] - Article 73(1)
- The requirement lacks a defined human-oversight response when an alert fires (e.g., suspension of use, human review), leaving detection without the mandated corrective action deployers must take under Article 26(5) when a system may present a risk. [medium] - Article 26(5)
- Monitoring scope is limited to accuracy, bias, and data quality and omits robustness/cybersecurity performance monitoring and feedback-loop bias mitigation required for systems that continue to learn after deployment. [medium] - Article 15(4)

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Reporting of serious incidents, Article 73(1)**
  > 1. Providers of high-risk AI systems placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred.
- **Obligations of deployers of high-risk AI systems, Article 26(5)**
  > 5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and sh
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con

**Recommendations:**

- Declare specific accuracy/bias metrics and thresholds in the accompanying instructions of use per Article 15(3) before configuring alert thresholds.
- Implement a documented post-market monitoring plan (Article 72) that systematically collects and analyses alert data to evaluate ongoing compliance, not just fire notifications.
- Define and implement an incident-escalation workflow so threshold breaches that qualify as serious incidents are reported to the provider, distributor, and market surveillance authority under Article 73.
- Specify the human oversight action triggered by each alert type (e.g., suspend use, mandatory recruiter review) to satisfy Article 26(5) and Article 14 human oversight obligations.
- Extend monitoring scope to include robustness, cybersecurity, and feedback-loop bias effects for any continuously learning model component, per Article 15(1) and (4).

---

### NFR-6

**Risk level:** high

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** NFR-6 uses only a non-binding 'should' for rollback capability and lacks defined triggers, documentation, and regulatory reporting duties, so it does not satisfy the mandatory corrective-action, post-market monitoring, and incident-reporting obligations required for this high-risk recruitment AI system.

**Risks:**

- Rollback is phrased as optional ('should support') rather than mandatory, failing to guarantee the corrective action (bringing into conformity, disabling, or recalling) that Article 20(1) requires providers to implement immediately upon detecting non-conformity. [high] - Article 20(1)
- The requirement does not define what safety/robustness/fairness thresholds trigger rollback nor tie this to a documented post-market monitoring system and plan, as mandated by Article 72(1)-(3) for continuous compliance evaluation throughout the system's lifetime. [high] - Article 72(1)
- There is no obligation to notify market surveillance authorities when a rollback is triggered by a serious incident (e.g., systemic fairness failure affecting fundamental rights of candidates), omitting the mandatory serious-incident reporting duty under Article 73(1). [high] - Article 73(1)
- The requirement does not integrate rollback into a continuous risk management process that identifies, evaluates, and mitigates risks (including bias/fairness risks) throughout the AI system's lifecycle as required by Article 9(2). [medium] - Article 9(2)
- No requirement specifies logging/documentation of the rollback event itself (reason, prior version, approver), risking incomplete audit trails needed to demonstrate accuracy and robustness performance consistency under Article 15(1) and (4). [medium] - Article 15(4)

**Cited provisions:**

- **Corrective actions and duty of information, Article 20(1)**
  > 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representativ
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Reporting of serious incidents, Article 73(1)**
  > 1. Providers of high-risk AI systems placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred.
- **Risk management system, Article 9(2)**
  > 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the est
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con

**Recommendations:**

- Change 'should support' to a mandatory 'shall support' and define specific quantitative thresholds for safety, robustness, and fairness failures that automatically trigger rollback.
- Link rollback triggers to a documented post-market monitoring plan (Article 72) that continuously collects and analyses performance and fairness data across the model's lifecycle.
- Add a requirement to immediately notify the competent market surveillance authority and affected deployers when a rollback is triggered by a serious incident, per Article 73.
- Extend the risk management system to include bias/fairness risk monitoring feeding into rollback decisions, consistent with Article 9(2)(c)-(d).
- Require the system to log every rollback event (trigger reason, previous model version, timestamp, approver) as part of the audit trail alongside existing score/ranking logs.

---
