# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 12
- Medium: 3
- Low: 1

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** Requirement FR-1 does not address data governance, transparency, or record-keeping obligations under the EU AI Act, which are critical for high-risk AI systems in recruitment.

**Risks:**

- No mention of data governance for processing resumes and application data [high] — Article 10 (Data governance)
- Lacks transparency requirements for processing of applicant information [medium] — Article 13 (Transparency obligation)
- Does not specify record-keeping for application data and processing activities [medium] — Article 12 (Record keeping)

**Cited provisions:**

- **Data and data governance, Article 10(1)**
  > 1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Record-keeping, Article 12(1)**
  > 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

**Recommendations:**

- Implement data governance policies for applicant data processing
- Add transparency mechanisms for how applicant data is used
- Establish record-keeping procedures for recruitment data

---

### FR-2

**Risk level:** high

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** The requirement for generating a suitability score does not ensure data quality and representativeness as required by Article 10(3), potentially leading to biased or inaccurate outcomes. It also lacks provisions for a fundamental rights impact assessment required under Article 27.

**Risks:**

- Suitability score generation does not specify requirements for training data to be representative and free of errors [high] — Article 10(3)
- No mention of conducting a fundamental rights impact assessment for the suitability scoring system [medium] — Article 27(1)

**Cited provisions:**

- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina
- **Fundamental rights impact assessment for high-risk AI systems, Article 27(1)**
  > 1. Prior to deploying a high-risk AI system referred to in Article 6(2), with the exception of high-risk AI systems intended to be used in the area listed in point 2 of Annex III, deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high-risk AI systems referred to in points 5 (b) and (c) of Annex III, shall perform an assessment of the impact on fundamental rights that the use of such system may produce. For that purpose, deployer

**Recommendations:**

- Define data quality criteria for training data to ensure representativeness and error-freedom as per Article 10(3)
- Implement a fundamental rights impact assessment as required by Article 27(1)

---

### FR-3

**Risk level:** high

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** The requirement to rank candidates using a suitability score may not address transparency and human oversight obligations, potentially conflicting with Article 13 and Article 14. Additionally, there is no mention of evaluating the risk level or considering the criteria outlined in Article 7, which could lead to non-compliance with evaluation and review obligations under Article 112.

**Risks:**

- No provision for ensuring transparency in the ranking algorithm used for candidate suitability scores [high] — Article 13(1)
- Lack of human oversight mechanism for decisions made by the AI system in candidate ranking [high] — Article 14(1)
- Failure to consider the criteria for evaluating risk levels as outlined in Article 7, particularly regarding the possibility of human override and potential harm [medium] — Article 7(2)
- No mechanism to evaluate and review the AI system's ranking process in accordance with Article 112 [medium] — Article 112(11)

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- **Amendments to Annex III, Article 7(2)**
  > 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decisi
- **Evaluation and review, Article 112(11)**
  > 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; an

**Recommendations:**

- Implement transparency measures for the ranking algorithm and suitability score calculation
- Ensure human oversight in the form of a review process for AI-generated candidate rankings
- Incorporate criteria for risk evaluation, including human override possibilities and potential harm assessment
- Establish a process for evaluating and reviewing the AI system's ranking functionality as per Article 112

---

### FR-4

**Risk level:** high

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** The requirement mandates explanations for candidate suitability scores but does not address transparency for users or the ability to override decisions, missing key obligations under Article 13 and Article 14.

**Risks:**

- Explanation not provided in a clear and accessible manner to users [high] — Article 13(1)
- No provision for human override of automated decisions [high] — Article 14(1)

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Human oversight, Article 14(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.

**Recommendations:**

- Ensure explanations are presented in a user-friendly format
- Include a mechanism for recruiters to override automated suitability scores

---

### FR-5

**Risk level:** high

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** Requirement notifies recruiters about automated rankings but does not ensure transparency for candidates, missing Article 13(1) requirements.

**Risks:**

- No requirement to inform candidates about automated decision-making [high] — Article 13(1)

**Cited provisions:**

- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Add obligation to inform candidates about automated ranking process

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** Requirement allows human recruiters to review and override automated rankings but does not address the competency, training, and authority requirements for reviewers as outlined in Article 14(5).

**Risks:**

- Does not specify that at least two competent reviewers must verify candidate identification [medium] — Article 14(5)

**Cited provisions:**

- **Human oversight, Article 14(5)**
  > 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natur

**Recommendations:**

- Specify that at least two natural persons with necessary competence, training, and authority must verify and confirm candidate identification before removal from consideration

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** Requirement covers logging of model outputs and overrides but lacks specific details required by Articles 12 and 19.

**Risks:**

- Does not specify recording of system usage period (start and end times) [medium] — Article 12(3) (a)
- Does not specify reference database for input data verification [medium] — Article 12(3) (b)
- Does not specify minimum log retention period of six months [medium] — Article 19(1)

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5
- **Automatically generated logs, Article 19(1)**
  > 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.

**Recommendations:**

- Include logging of system usage start and end times
- Specify the reference database used for input data checks
- Define log retention period of at least six months

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** Requirement addresses logging of input data and model version but lacks logging of use periods and identification of reviewers, missing parts of Article 12(3).

**Risks:**

- No recording of the period of each system use (start and end times) [medium] — Article 12(3)
- Does not identify natural persons involved in verifying results [medium] — Article 12(3)

**Cited provisions:**

- **Record-keeping, Article 12(3)**
  > 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5

**Recommendations:**

- Add logging of system use start and end times
- Include identification of reviewers in audit records

---

### FR-9

**Risk level:** low

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** The requirement prohibits the use of facial recognition, biometric identification, and emotion recognition during candidate screening, which aligns with the EU AI Act’s restrictions on prohibited and high-risk AI practices. No compliance risks identified.

---

### FR-10

**Risk level:** high

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** Requirement allows candidates to request review of automated decisions but does not ensure access to the model for evaluation or specify structured dialogue with providers, conflicting with Articles 92 and 93.

**Risks:**

- No provision for Commission to access the AI model for evaluation [high] — Article 92(5)
- No structured dialogue with providers before requesting access or measures [medium] — Article 92(7)
- No mechanism for AI Office to initiate structured dialogue before requesting measures [medium] — Article 93(2)

**Cited provisions:**

- **Power to conduct evaluations, Article 92(5)**
  > 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- **Power to conduct evaluations, Article 92(7)**
  > 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.
- **Power to request measures, Article 93(2)**
  > 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.

**Recommendations:**

- Implement model access procedures for Commission evaluations
- Establish structured dialogue processes with providers before evaluations or measures
- Define structured dialogue requirements for the AI Office before requesting measures

---

### NFR-1

**Risk level:** high

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** The requirement addresses dataset validation for missing values, duplicates, and inconsistent labels but does not cover broader data governance and bias mitigation requirements in Article 10.

**Risks:**

- Does not ensure data sets are representative and free of biases as required by Article 10(2) and (3) [high] — Article 10(2) and (3)
- Lacks examination of data for possible biases affecting fundamental rights or safety, as required by Article 10(2)(f) [medium] — Article 10(2)(f)
- Does not address data governance practices for data collection processes and origins, as required by Article 10(2)(b) [medium] — Article 10(2)(b)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an

**Recommendations:**

- Expand dataset validation to include checks for representativeness and bias mitigation
- Include examination of data for biases affecting fundamental rights or safety
- Implement governance practices for tracking data collection processes and origins

---

### NFR-2

**Risk level:** high

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** The requirement addresses model performance measurement across demographic groups but lacks explicit provisions for bias detection and mitigation as required by Article 10(2)(f) and (g).

**Risks:**

- No explicit requirement to examine data for biases affecting fundamental rights or leading to discrimination [high] — Article 10(2)(f)
- No explicit requirement for measures to detect, prevent, and mitigate identified biases [high] — Article 10(2)(g)
- Does not ensure data representativeness across relevant demographic groups as required by Article 10(3) [medium] — Article 10(3)

**Cited provisions:**

- **Data and data governance, Article 10(2)**
  > 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment an
- **Data and data governance, Article 10(3)**
  > 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combina

**Recommendations:**

- Include explicit requirements to examine data for biases affecting fundamental rights or leading to discrimination
- Include explicit requirements for measures to detect, prevent, and mitigate identified biases
- Ensure data sets are sufficiently representative across relevant demographic groups

---

### NFR-3

**Risk level:** high

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** Requirement prohibits using protected attributes in ranking, aligning with Article 5(1)(c) and Article 5(1)(g), but does not address profiling or social scoring mechanisms that could indirectly incorporate these attributes, creating gaps with Article 5(1)(c) and Article 5(1)(g).

**Risks:**

- Does not restrict profiling techniques that could infer protected attributes for ranking [high] — Article 5(1)(c) and (g)
- No prohibition on social scoring based on characteristics that correlate with protected attributes [high] — Article 5(1)(c)

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)**
  > 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have othe

**Recommendations:**

- Explicitly ban profiling methods that could infer protected attributes in ranking processes
- Add restrictions on social scoring mechanisms that indirectly use protected attributes

---

### NFR-4

**Risk level:** high

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** The requirement mandates access controls for recruitment staff to view candidate data and model explanations but does not specify measures to ensure the security and privacy-preserving processing of special categories of personal data as required by Article 10(5)(b) and (c).

**Risks:**

- No technical limitations on re-use of personal data and state-of-the-art security measures for special categories of data [high] — Article 10(5)
- No strict controls and documentation of access to special categories of personal data [high] — Article 10(5)

**Cited provisions:**

- **Data and data governance, Article 10(5)**
  > 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directiv

**Recommendations:**

- Implement technical limitations on re-use of personal data with state-of-the-art security measures
- Enforce strict access controls and documentation for special categories of personal data

---

### NFR-5

**Risk level:** high

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement addresses alert generation for model performance metrics but does not specify the integration of these alerts into a documented post-market monitoring system as required by Article 72(1) and (3).

**Risks:**

- Alerts not linked to a documented post-market monitoring system [high] — Article 72(1)
- Lacks systematic collection and analysis of performance data in line with monitoring plan requirements [medium] — Article 72(2)
- Does not ensure monitoring plan is part of technical documentation [medium] — Article 72(3)

**Cited provisions:**

- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(1)**
  > 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(3)**
  > 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Ar

**Recommendations:**

- Ensure alerts are integrated into a documented post-market monitoring system
- Implement systematic data collection and analysis processes as part of the monitoring plan
- Verify that the monitoring plan is included in the technical documentation

---

### NFR-6

**Risk level:** high

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** The requirement allows rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks, but does not address the need for a new conformity assessment if the rollback constitutes a substantial modification, as required by Article 43(4).

**Risks:**

- No requirement for new conformity assessment after rollback if it constitutes a substantial modification [high] — Article 43(4)

**Cited provisions:**

- **Conformity assessment, Article 43(4)**
  > 4. High-risk AI systems that have already been subject to a conformity assessment procedure shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer. For high-risk AI systems that continue to learn after being placed on the market or put into service, changes to the high-risk AI system and its performance that have been pre-determi

**Recommendations:**

- Add a process to determine if a rollback constitutes a substantial modification and require a new conformity assessment if it does

---
