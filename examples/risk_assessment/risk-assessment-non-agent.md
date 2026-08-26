# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 10
- Medium: 6

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** Requirement does not address data governance, risk management, or transparency for processing resumes and application data, creating gaps with Articles 10, 9, and 13. No mention of fundamental rights impact assessments required by Article 27.

**Risks:**

- No safeguards for processing personal data in resumes and applications [high] — Article 10(1)
- No risk management system for processing sensitive application data [high] — Article 9(1)
- No requirement for transparency in processing application data [medium] — Article 13(1)
- No fundamental rights impact assessment for candidate data processing [high] — Article 27(1)

**Cited provisions:**

- **Data and data governance, Article 10(1)**
  > 1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used.
- **Risk management system, Article 9(1)**
  > 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Implement data governance controls for processing resumes and applications
- Establish risk management procedures for candidate data processing
- Add transparency requirements for automated processing of application data
- Conduct fundamental rights impact assessments for recruitment AI processing

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** Requirement lacks transparency and human oversight in scoring logic, missing alignment with Articles 13, 14, and 27.

**Risks:**

- No requirement to explain the scoring algorithm to users [medium] — Article 13(1)
- No mechanism for human review of automated suitability scores [high] — Article 14(1)
- No fundamental rights impact assessment for scoring logic [high] — Article 27(1)

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Add requirement to document and explain the scoring algorithm
- Implement human review process for suitability scores
- Conduct fundamental rights impact assessment for scoring logic

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** The requirement to rank candidates based on a suitability score introduces potential risks related to transparency and human oversight, which may not be adequately addressed.

**Risks:**

- Lacks transparency in the ranking methodology and suitability score calculation [high] — Article 50 (Transparency obligations)
- Does not ensure human reviewers can override automated ranking decisions [high] — Article 14(1) (Human oversight)
- May not account for the potential adverse impact on fundamental rights if not properly evaluated [medium] — Article 27 (Fundamental rights impact assessment)
- Does not specify the need for ongoing post-market monitoring of the ranking system's performance and impact [medium] — Article 72 (Post-market monitoring)

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, i
- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.

**Recommendations:**

- Implement transparent documentation of the ranking algorithm and suitability score calculation
- Provide a mechanism for human reviewers to override automated rankings
- Conduct a fundamental rights impact assessment to evaluate potential adverse effects
- Establish a post-market monitoring plan for ongoing evaluation of the ranking system's performance and impact

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** The requirement for explaining candidate suitability scores aligns with transparency obligations but does not address the need for human oversight to override automated decisions, as required by Article 14(1).

**Risks:**

- No override mechanism for automated decisions [high] — Article 14(1)

**Cited provisions:**

- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.

**Recommendations:**

- Add ability for reviewers to override automated outputs based on explanations provided

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** Requirement FR-5 addresses transparency by notifying recruiters of automated decision use, aligning with Article 13. However, it does not specify requirements for the content or format of these notifications, which is required under Article 13(3).

**Risks:**

- Does not specify content or format of notifications about automated decisions [medium] — Article 13(3)

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(3)**
  > 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated 

**Recommendations:**

- Define specific content and format requirements for notifications about automated decision use

---

### FR-6

**Risk level:** high

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** The requirement allows human recruiters to review, override, or reject automated rankings but does not address the need for proper understanding of the system's limitations or the implementation of oversight measures by the provider or deployer, creating a gap with Article 14(4) and Article 14(3).

**Risks:**

- No requirement for recruiters to understand the system's limitations [medium] — Article 14(4)
- Lacks implementation of oversight measures by the provider or deployer [high] — Article 14(3)

**Cited provisions:**

- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss
- **Human oversight, Article 14(3)**
  > 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and t

**Recommendations:**

- Ensure recruiters receive training on the system's limitations
- Specify oversight measures to be implemented by the provider or deployer

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** The requirement logs scores, rankings, explanations, overrides, and final decisions but misses specific data elements required by Article 12(3) for certain high-risk systems.

**Risks:**

- Does not record the period of each use of the system (start and end times) [medium] — Article 12(3) (a)
- Does not log the reference database against which input data is checked [medium] — Article 12(3) (b)
- Does not record the identification of natural persons involved in verifying results [medium] — Article 12(3) (d)

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Include recording of system usage start and end times
- Log the reference database used for data checks
- Record identities of personnel verifying results

---

### FR-8

**Risk level:** high

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement for retaining audit records for screening decisions aligns partially with Article 12's record-keeping obligations but omits specific data elements and purposes. This creates gaps in traceability and post-market monitoring compliance.

**Risks:**

- Audit records do not include system use periods (start/end times) [medium] — Article 12(3)
- No mention of reference databases used for input data checks [medium] — Article 12(3)
- Failure to log events relevant to risk identification and substantial modifications [high] — Article 12(2)
- Does not ensure logs facilitate post-market monitoring [high] — Article 12(2)

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI s

**Recommendations:**

- Include system use start and end times in audit records
- Log reference databases used for input data checks
- Expand logging to capture events indicating risks or system modifications
- Ensure logs support post-market monitoring requirements

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** Requirement FR-9 prohibits specific biometric uses during candidate screening, aligning with Article 5(1)’s ban on harmful practices but lacks enforcement clarity.

**Risks:**

- Requirement does not specify how enforcement of the prohibition is ensured [medium] — Article 5(4)
- No mechanism outlined for informing candidates about biometric system operations [medium] — Article 50(3)
- Lack of transparency in prohibited system usage may hinder compliance verification [low] — Article 5(7)

**Cited provisions:**

- **Prohibited AI practices, Article 5(4)**
  > 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(3)**
  > 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject
- **Prohibited AI practices, Article 5(7)**
  > 7. The Commission shall publish annual reports on the use of real-time remote biometric identification systems in publicly accessible spaces for law enforcement purposes, based on aggregated data in Member States on the basis of the annual reports referred to in paragraph 6. Those annual reports shall not include sensitive operational data of the related law enforcement activities.

**Recommendations:**

- Define enforcement procedures for the prohibition
- Implement candidate notification processes for biometric systems
- Establish transparency protocols for prohibited system usage monitoring

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** Requirement allows candidate requests for review but does not specify mechanisms for handling these requests or ensuring effective oversight, conflicting with Article 14(1) and Article 14(4).

**Risks:**

- No specified process for handling candidate review requests [medium] — Article 14(1)
- Lack of competency requirements for individuals handling review requests [medium] — Article 14(4)

**Cited provisions:**

- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- **Human oversight, Article 14(4)**
  > 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the poss

**Recommendations:**

- Implement a defined process for handling candidate review requests
- Establish competency requirements for personnel handling review requests

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** The requirement addresses dataset validation for missing values, duplicates, and inconsistent labels but does not cover broader data governance practices required by Article 10(2).

**Risks:**

- Does not address data governance practices for data collection processes and origins [medium] — Article 10(2)
- Lacks assessment of possible biases affecting fundamental rights or causing discrimination [medium] — Article 10(2)
- Does not specify measures to detect, prevent, or mitigate identified biases [medium] — Article 10(2)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Include data governance practices for data collection origins and processes
- Add assessment for biases impacting fundamental rights or causing discrimination
- Specify measures to detect, prevent, and mitigate biases

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** Requirement ensures demographic performance measurement but does not address data bias mitigation as required by Article 10(2)(g).

**Risks:**

- Does not specify measures to detect, prevent and mitigate biases in data sets [medium] — Article 10(2)(g)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Include requirements for bias detection, prevention, and mitigation in data governance practices

---

### NFR-3

**Risk level:** high

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** Requirement prohibits using protected attributes for ranking, but does not address profiling based on these attributes, creating a gap with Article 5(1)(c).

**Risks:**

- Does not prohibit profiling based on protected attributes like race or religion [high] — Article 5(1)(c)
- No mention of preventing unjustified or disproportionate treatment based on protected attributes [medium] — Article 5(1)(c)

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have othe

**Recommendations:**

- Explicitly prohibit profiling based on protected attributes
- Include provisions to prevent unjustified or disproportionate treatment based on these attributes

---

### NFR-4

**Risk level:** high

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** Requirement does not address access control for market surveillance authorities to source code or documentation as specified in Article 74(12) and (13).

**Risks:**

- No provision for market surveillance authorities to access documentation and data sets when required [high] — Article 74(12)
- No mechanism for granting market surveillance authorities access to source code upon reasoned request [high] — Article 74(13)

**Cited provisions:**

- **Market surveillance and control of AI systems in the Union market, Article 74(12)**
  > 12. Without prejudice to the powers provided for under Regulation (EU) 2019/1020, and where relevant and limited to what is necessary to fulfil their tasks, the market surveillance authorities shall be granted full access by providers to the documentation as well as the training, validation and testing data sets used for the development of high-risk AI systems, including, where appropriate and subject to security safeguards, through application programming interfaces (API) or other relevant tech
- **Market surveillance and control of AI systems in the Union market, Article 74(13)**
  > 13. Market surveillance authorities shall be granted access to the source code of the high-risk AI system upon a reasoned request and only when both of the following conditions are fulfilled: (a) access to source code is necessary to assess the conformity of a high-risk AI system with the requirements set out in Chapter III, Section 2; and (b) testing or auditing procedures and verifications based on the data and documentation provided by the provider have been exhausted or proved insufficient.

**Recommendations:**

- Implement procedures to allow market surveillance authorities access to necessary documentation and data sets
- Establish process for granting access to source code upon a reasoned request by market surveillance authorities

---

### NFR-5

**Risk level:** high

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** Requirement NFR-5 addresses monitoring alerts for model performance but lacks a documented post-market monitoring plan as required by Article 72(3).

**Risks:**

- No explicit requirement to document the monitoring plan as part of technical documentation [high] — Article 72(3)

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(3)**
  > 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Ar

**Recommendations:**

- Include a post-market monitoring plan in the technical documentation as specified in Article 72(3)

---

### NFR-6

**Risk level:** high

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** Requirement allows rollback to a previously approved model version but does not ensure a new conformity assessment for substantial modifications, violating Article 43(4).

**Risks:**

- No new conformity assessment required for model rollbacks [high] — Article 43(4)
- Does not address robustness and fail-safe mechanisms for system resilience [medium] — Article 15(4)

**Cited provisions:**

- **Conformity assessment, Article 43(4)**
  > 4. High-risk AI systems that have already been subject to a conformity assessment procedure shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer. For high-risk AI systems that continue to learn after being placed on the market or put into service, changes to the high-risk AI system and its performance that have been pre-determi
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that con

**Recommendations:**

- Mandate a new conformity assessment for substantial model rollbacks
- Incorporate robustness and fail-safe mechanisms in rollback procedures

---
