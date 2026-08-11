# EU AI Act Requirements Risk Report

This report maps extracted software requirements to candidate EU AI Act paragraphs using semantic similarity. It is an engineering review aid, not legal advice.

## Summary

- High: 6
- Medium: 10
- Low: 0
- Unmapped: 0

## Requirement Findings

### FR-1

**Risk level:** Medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 113, paragraph 3 with score 0.771. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 113, paragraph 3 (art:113:p3), score 0.771
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 113, paragraph 4 (art:113:p4), score 0.762
  - Entry into force and application
  - 4. Control of the technical documentation. 4.1. In addition to the application referred to in point 3, an application with a notified body of their choice shall be lodged by the provider for the assessment of the technical documentation relating to the AI system which the provider intends to place on the market or put into service and which is covered by the quality management system referred to under point 3. 4.2. The application shall include: (a) the name and address of the provider; (b) a written declaration that the same application has not been lodged with any other notified body; (c) the technical documentation referred to in Annex IV. 134/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj 4.3. The technical documentation shall be examined by the notified body. Where relevant, and limited to what is necessary to fulfil its tasks, the notified body shall be granted full access to the training, validation, and testing data sets used, including, where appropriate and subject to security safeguards, through API or other relevant technical means and tools enabling remote access. 4.4. In examining the technical documentation, the notified body may require that the provider supply further evidence or carry out further tests so as to enable a proper assessment of the conformity of the AI system with the requirements set out in Chapter III, Section 2. Where the notified body is not satisfied with the tests carried out by the provider, the notified body shall itself directly carry out adequate tests, as appropriate. 4.5. Where necessary to assess the conformity of the high-risk AI system with the requirements set out in Chapter III, Section 2, after all other reasonable means to verify conformity have been exhausted and have proven to be insufficient, and upon a reasoned request, the notified body shall also be granted access to the training and trained models of the AI system, including its relevant parameters. Such access shall be subject to existing Union law on the protection of intellectual property and trade secrets. 4.6. The decision of the notified body shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the technical documentation and the reasoned assessment decision. Where the AI system is in conformity with the requirements set out in Chapter III, Section 2, the notified body shall issue a Union technical documentation assessment certificate. The certificate shall indicate the name and address of the provider, the conclusions of the examination, the conditions (if any) for its validity and the data necessary for the identification of the AI system. The certificate and its annexes shall contain all relevant information to allow the conformity of the AI system to be evaluated, and to allow for control of the AI system while in use, where applicable. Where the AI system is not in conformity with the requirements set out in Chapter III, Section 2, the notified body shall refuse to issue a Union technical documentation assessment certificate and shall inform the applicant accordingly, giving detailed reasons for its refusal. Where the AI system does not meet the requirement relating to the data used to train it, re-training of the AI system will be needed prior to the application for a new conformity assessment. In this case, the reasoned assessment decision of the notified body refusing to issue the Union technical documentation assessment certificate shall contain specific considerations on the quality data used to train the AI system, in particular on the reasons for non-compliance. 4.7. Any change to the AI system that could affect the compliance of the AI system with the requirements or its intended purpose shall be assessed by the notified body which issued the Union technical documentation assessment certificate. The provider shall inform such notified body of its intention to introduce any of the abovementioned changes, or if it otherwise becomes aware of the occurrence of such changes. The intended changes shall be assessed by the notified body, which shall decide whether those changes require a new conformity assessment in accordance with Article 43(4) or whether they could be addressed by means of a supplement to the Union technical documentation assessment certificate. In the latter case, the notified body shall assess the changes, notify the provider of its decision and, where the changes are approved, issue to the provider a supplement to the Union technical documentation assessment certificate.
- Article 113, paragraph 7 (art:113:p7), score 0.762
  - Entry into force and application
  - 7. Where applicable, the name and identification number of the notified body, a description of the conformity assessment procedure performed, and identification of the certificate issued;
- Article 31, paragraph 11 (art:31:p11), score 0.760
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 31, paragraph 8 (art:31:p8), score 0.756
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.

### FR-2

**Risk level:** Medium

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 10, paragraph 3 with score 0.802. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 10, paragraph 3 (art:10:p3), score 0.802
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 113, paragraph 1 (art:113:p1), score 0.799
  - Entry into force and application
  - 1. Introduction Conformity based on an assessment of the quality management system and an assessment of the technical documentation is the conformity assessment procedure based on points 2 to 5.
- Article 113, paragraph 3 (art:113:p3), score 0.796
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 113, paragraph 2 (art:113:p2), score 0.789
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 112, paragraph 11 (art:112:p11), score 0.785
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.

### FR-3

**Risk level:** Medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 113, paragraph 1 with score 0.795. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 113, paragraph 1 (art:113:p1), score 0.795
  - Entry into force and application
  - 1. Introduction Conformity based on an assessment of the quality management system and an assessment of the technical documentation is the conformity assessment procedure based on points 2 to 5.
- Article 113, paragraph 3 (art:113:p3), score 0.794
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 113, paragraph 2 (art:113:p2), score 0.790
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 112, paragraph 11 (art:112:p11), score 0.781
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
- Article 7, paragraph 2 (art:7:p2), score 0.779
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### FR-4

**Risk level:** High

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 113, paragraph 3 with score 0.789. Detected signals: Automated decision-making; Transparency and user information. Estimated risk level: High.

**Risk signals:** Automated decision-making, Transparency and user information

**Candidate EU AI Act provisions:**

- Article 113, paragraph 3 (art:113:p3), score 0.789
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 113, paragraph 1 (art:113:p1), score 0.773
  - Entry into force and application
  - 1. Introduction Conformity based on an assessment of the quality management system and an assessment of the technical documentation is the conformity assessment procedure based on points 2 to 5.
- Article 113, paragraph 2 (art:113:p2), score 0.772
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 7, paragraph 2 (art:7:p2), score 0.771
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 82, paragraph 4 (art:82:p4), score 0.770
  - Compliant AI systems which present a risk
  - 4. The Commission shall without undue delay enter into consultation with the Member States concerned and the relevant operators, and shall evaluate the national measures taken. On the basis of the results of that evaluation, the Commission shall decide whether the measure is justified and, where necessary, propose other appropriate measures.

### FR-5

**Risk level:** High

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.800. Detected signals: Automated decision-making; Transparency and user information. Estimated risk level: High.

**Risk signals:** Automated decision-making, Transparency and user information

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.800
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 52, paragraph 1 (art:52:p1), score 0.800
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 27, paragraph 3 (art:27:p3), score 0.797
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.
- Article 31, paragraph 11 (art:31:p11), score 0.791
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 113, paragraph 3 (art:113:p3), score 0.786
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.

### FR-6

**Risk level:** High

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 81, paragraph 2 with score 0.807. Detected signals: Automated decision-making; Human oversight. Estimated risk level: High.

**Risk signals:** Automated decision-making, Human oversight

**Candidate EU AI Act provisions:**

- Article 81, paragraph 2 (art:81:p2), score 0.807
  - Union safeguard procedure
  - 2. Where the Commission considers the measure taken by the relevant Member State to be justified, all Member States shall ensure that they take appropriate restrictive measures in respect of the AI system concerned, such as requiring the withdrawal of the AI system from their market without undue delay, and shall inform the Commission accordingly. Where the Commission considers the national measure to be unjustified, the Member State concerned shall withdraw the measure and shall inform the Commission accordingly.
- Article 14, paragraph 4 (art:14:p4), score 0.804
  - Human oversight
  - 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- Article 14, paragraph 5 (art:14:p5), score 0.801
  - Human oversight
  - 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- Article 113, paragraph 2 (art:113:p2), score 0.800
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 79, paragraph 5 (art:79:p5), score 0.798
  - Procedure at national level for dealing with AI systems presenting a risk
  - 5. Where the operator of an AI system does not take adequate corrective action within the period referred to in paragraph 2, the market surveillance authority shall take all appropriate provisional measures to prohibit or restrict the AI system’s being made available on its national market or put into service, to withdraw the product or the standalone AI system from that market or to recall it. That authority shall without undue delay notify the Commission and the other Member States of those measures.

### FR-7

**Risk level:** High

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.798. Detected signals: Automated decision-making; Human oversight; Transparency and user information; Logging and traceability. Estimated risk level: High.

**Risk signals:** Automated decision-making, Human oversight, Transparency and user information, Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.798
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 19, paragraph 2 (art:19:p2), score 0.798
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.
- Article 19, paragraph 1 (art:19:p1), score 0.798
  - Automatically generated logs
  - 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- Article 12, paragraph 1 (art:12:p1), score 0.793
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 2 (art:12:p2), score 0.786
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

### FR-8

**Risk level:** Medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.829. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.829
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.821
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 12, paragraph 1 (art:12:p1), score 0.814
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 113, paragraph 5 (art:113:p5), score 0.804
  - Entry into force and application
  - 5. Surveillance of the approved quality management system. 5.1. The purpose of the surveillance carried out by the notified body referred to in Point 3 is to make sure that the provider duly complies with the terms and conditions of the approved quality management system. 5.2. For assessment purposes, the provider shall allow the notified body to access the premises where the design, development, testing of the AI systems is taking place. The provider shall further share with the notified body all necessary information. 5.3. The notified body shall carry out periodic audits to make sure that the provider maintains and applies the quality management system and shall provide the provider with an audit report. In the context of those audits, the notified body may carry out additional tests of the AI systems for which a Union technical documentation assessment certificate was issued. ANNEX VIII Information to be submitted upon the registration of high-risk AI systems in accordance with
- Article 10, paragraph 2 (art:10:p2), score 0.800
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.

### FR-9

**Risk level:** Medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 50, paragraph 3 with score 0.815. Detected signals: Biometric identification or categorisation. Estimated risk level: Medium.

**Risk signals:** Biometric identification or categorisation

**Candidate EU AI Act provisions:**

- Article 50, paragraph 3 (art:50:p3), score 0.815
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 5, paragraph 7 (art:5:p7), score 0.806
  - Prohibited AI practices
  - 7. The Commission shall publish annual reports on the use of real-time remote biometric identification systems in publicly accessible spaces for law enforcement purposes, based on aggregated data in Member States on the basis of the annual reports referred to in paragraph 6. Those annual reports shall not include sensitive operational data of the related law enforcement activities.
- Article 5, paragraph 4 (art:5:p4), score 0.805
  - Prohibited AI practices
  - 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- Article 79, paragraph 5 (art:79:p5), score 0.802
  - Procedure at national level for dealing with AI systems presenting a risk
  - 5. Where the operator of an AI system does not take adequate corrective action within the period referred to in paragraph 2, the market surveillance authority shall take all appropriate provisional measures to prohibit or restrict the AI system’s being made available on its national market or put into service, to withdraw the product or the standalone AI system from that market or to recall it. That authority shall without undue delay notify the Commission and the other Member States of those measures.
- Article 46, paragraph 2 (art:46:p2), score 0.801
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.

### FR-10

**Risk level:** Medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 92, paragraph 3 with score 0.808. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 92, paragraph 3 (art:92:p3), score 0.808
  - Power to conduct evaluations
  - 3. For the purposes of paragraph 1, the Commission may request access to the general-purpose AI model concerned through APIs or further appropriate technical means and tools, including source code.
- Article 93, paragraph 2 (art:93:p2), score 0.806
  - Power to request measures
  - 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 112, paragraph 10 (art:112:p10), score 0.804
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 91, paragraph 3 (art:91:p3), score 0.804
  - Power to request documentation and information
  - 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
- Article 92, paragraph 7 (art:92:p7), score 0.803
  - Power to conduct evaluations
  - 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.

### NFR-1

**Risk level:** High

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 10, paragraph 3 with score 0.843. Detected signals: Transparency and user information; Logging and traceability; Data governance and quality. Estimated risk level: High.

**Risk signals:** Transparency and user information, Logging and traceability, Data governance and quality

**Candidate EU AI Act provisions:**

- Article 10, paragraph 3 (art:10:p3), score 0.843
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 10, paragraph 2 (art:10:p2), score 0.838
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 10, paragraph 1 (art:10:p1), score 0.829
  - Data and data governance
  - 1. High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5 whenever such data sets are used.
- Article 10, paragraph 6 (art:10:p6), score 0.807
  - Data and data governance
  - 6. For the development of high-risk AI systems not using techniques involving the training of AI models, paragraphs 2 to 5 apply only to the testing data sets.
- Article 15, paragraph 4 (art:15:p4), score 0.792
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

### NFR-2

**Risk level:** Medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 10, paragraph 3 with score 0.787. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 3 (art:10:p3), score 0.787
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 10, paragraph 2 (art:10:p2), score 0.783
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 112, paragraph 11 (art:112:p11), score 0.773
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
- Article 92, paragraph 1 (art:92:p1), score 0.773
  - Power to conduct evaluations
  - 1. The AI Office, after consulting the Board, may conduct evaluations of the general-purpose AI model concerned: (a) to assess compliance of the provider with obligations under this Regulation, where the information gathered pursuant to Article 91 is insufficient; or (b) to investigate systemic risks at Union level of general-purpose AI models with systemic risk, in particular following a qualified alert from the scientific panel in accordance with Article 90(1), point (a).
- Article 10, paragraph 4 (art:10:p4), score 0.771
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

### NFR-3

**Risk level:** Medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 6, paragraph 3 with score 0.786. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 6, paragraph 3 (art:6:p3), score 0.786
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- Article 5, paragraph 1 (art:5:p1), score 0.785
  - Prohibited AI practices
  - 1. The following AI practices shall be prohibited: (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm; (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm; (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to either or both of the following: (i) detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity; (d) the placing on the market, the putting into service for this specific purpose, or the use of an AI system for making risk assessments of natural persons in order to assess or predict the risk of a natural person committing a criminal offence, based solely on the profiling of a natural person or on assessing their personality traits and characteristics; this prohibition shall not apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity; (e) the placing on the market, the putting into service for this specific purpose, or the use of AI systems that create or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage; (f) the placing on the market, the putting into service for this specific purpose, or the use of AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons; (g) the placing on the market, the putting into service for this specific purpose, or the use of biometric categorisation systems that categorise individually natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation; this prohibition does not cover any labelling or filtering of lawfully acquired biometric datasets, such as images, based on biometric data or categorizing of biometric data in the area of law enforcement; (h) the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as such use is strictly necessary for one of the following objectives: (i) the targeted search for specific victims of abduction, trafficking in human beings or sexual exploitation of human beings, as well as the search for missing persons; (ii) the prevention of a specific, substantial and imminent threat to the life or physical safety of natural persons or a genuine and present or genuine and foreseeable threat of a terrorist attack; (iii) the localisation or identification of a person suspected of having committed a criminal offence, for the purpose of conducting a criminal investigation or prosecution or executing a criminal penalty for offences referred to in Annex II and punishable in the Member State concerned by a custodial sentence or a detention order for a maximum period of at least four years. Point (h) of the first subparagraph is without prejudice to Article 9 of Regulation (EU) 2016/679 for the processing of biometric data for purposes other than law enforcement.
- Article 46, paragraph 2 (art:46:p2), score 0.783
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.
- Article 80, paragraph 1 (art:80:p1), score 0.780
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 1. Where a market surveillance authority has sufficient reason to consider that an AI system classified by the provider as non-high-risk pursuant to Article 6(3) is indeed high-risk, the market surveillance authority shall carry out an evaluation of the AI system concerned in respect of its classification as a high-risk AI system based on the conditions set out in Article 6(3) and the Commission guidelines.
- Article 7, paragraph 2 (art:7:p2), score 0.780
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### NFR-4

**Risk level:** Medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 74, paragraph 13 with score 0.789. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 74, paragraph 13 (art:74:p13), score 0.789
  - Market surveillance and control of AI systems in the Union market
  - 13. Market surveillance authorities shall be granted access to the source code of the high-risk AI system upon a reasoned request and only when both of the following conditions are fulfilled: (a) access to source code is necessary to assess the conformity of a high-risk AI system with the requirements set out in Chapter III, Section 2; and (b) testing or auditing procedures and verifications based on the data and documentation provided by the provider have been exhausted or proved insufficient.
- Article 10, paragraph 5 (art:10:p5), score 0.784
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 75, paragraph 3 (art:75:p3), score 0.784
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 3. Where a market surveillance authority is unable to conclude its investigation of the high-risk AI system because of its inability to access certain information related to the general-purpose AI model despite having made all appropriate efforts to obtain that information, it may submit a reasoned request to the AI Office, by which access to that information shall be enforced. In that case, the AI Office shall supply to the applicant authority without delay, and in any event within 30 days, any information that the AI Office considers to be relevant in order to establish whether a high-risk AI system is non-compliant. Market surveillance authorities shall safeguard the confidentiality of the information that they obtain in accordance with Article 78 of this Regulation. The procedure provided for in Chapter VI of Regulation (EU) 2019/1020 shall apply mutatis mutandis.
- Article 74, paragraph 12 (art:74:p12), score 0.784
  - Market surveillance and control of AI systems in the Union market
  - 12. Without prejudice to the powers provided for under Regulation (EU) 2019/1020, and where relevant and limited to what is necessary to fulfil their tasks, the market surveillance authorities shall be granted full access by providers to the documentation as well as the training, validation and testing data sets used for the development of high-risk AI systems, including, where appropriate and subject to security safeguards, through application programming interfaces (API) or other relevant technical means and tools enabling remote access.
- Article 78, paragraph 3 (art:78:p3), score 0.783
  - Confidentiality
  - 3. Without prejudice to paragraphs 1 and 2, information exchanged on a confidential basis between the national competent authorities or between national competent authorities and the Commission shall not be disclosed without prior consultation of the originating national competent authority and the deployer when high-risk AI systems referred to in point 1, 6 or 7 of Annex III are used by law enforcement, border control, immigration or asylum authorities and when such disclosure would jeopardise public and national security interests. This exchange of information shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities. When the law enforcement, immigration or asylum authorities are providers of high-risk AI systems referred to in point 1, 6 or 7 of Annex III, the technical documentation referred to in Annex IV shall remain within the premises of those authorities. Those authorities shall ensure that the market surveillance authorities referred to in Article 74(8) and (9), as applicable, can, upon request, immediately access the documentation or obtain a copy thereof. Only staff of the market surveillance authority holding the appropriate level of security clearance shall be allowed to access that documentation or any copy thereof.

### NFR-5

**Risk level:** High

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 72, paragraph 1 with score 0.818. Detected signals: Logging and traceability; Data governance and quality. Estimated risk level: High.

**Risk signals:** Logging and traceability, Data governance and quality

**Candidate EU AI Act provisions:**

- Article 72, paragraph 1 (art:72:p1), score 0.818
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- Article 72, paragraph 2 (art:72:p2), score 0.809
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- Article 60, paragraph 8 (art:60:p8), score 0.807
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 8. Providers or prospective providers shall notify the national market surveillance authority in the Member State where the testing in real world conditions is to be conducted of the suspension or termination of the testing in real world conditions and of the final outcomes.
- Article 72, paragraph 3 (art:72:p3), score 0.803
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 10, paragraph 2 (art:10:p2), score 0.802
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.

### NFR-6

**Risk level:** Medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Source:** /Users/aditya/Desktop/EU-AI-Risks/examples/sample-srs.md

**Explanation:** Mapped to Article 43, paragraph 4 with score 0.818. Detected signals: Safety, robustness, and risk management. Estimated risk level: Medium.

**Risk signals:** Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 43, paragraph 4 (art:43:p4), score 0.818
  - Conformity assessment
  - 4. High-risk AI systems that have already been subject to a conformity assessment procedure shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer. For high-risk AI systems that continue to learn after being placed on the market or put into service, changes to the high-risk AI system and its performance that have been pre-determined by the provider at the moment of the initial conformity assessment and are part of the information contained in the technical documentation referred to in point 2(f) of Annex IV, shall not constitute a substantial modification.
- Article 15, paragraph 4 (art:15:p4), score 0.817
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- Article 72, paragraph 2 (art:72:p2), score 0.810
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.
- Article 52, paragraph 5 (art:52:p5), score 0.807
  - Procedure
  - 5. Upon a reasoned request of a provider whose model has been designated as a general-purpose AI model with systemic risk pursuant to paragraph 4, the Commission shall take the request into account and may decide to reassess whether the general-purpose AI model can still be considered to present systemic risks on the basis of the criteria set out in Annex XIII. Such a request shall contain objective, detailed and new reasons that have arisen since the designation decision. Providers may request reassessment at the earliest six months after the designation decision. Where the Commission, following its reassessment, decides to maintain the designation as a general-purpose AI model with systemic risk, providers may request reassessment at the earliest six months after that decision.
- Article 26, paragraph 5 (art:26:p5), score 0.799
  - Obligations of deployers of high-risk AI systems
  - 5. Deployers shall monitor the operation of the high-risk AI system on the basis of the instructions for use and, where relevant, inform providers in accordance with Article 72. Where deployers have reason to consider that the use of the high-risk AI system in accordance with the instructions may result in that AI system presenting a risk within the meaning of Article 79(1), they shall, without undue delay, inform the provider or distributor and the relevant market surveillance authority, and shall suspend the use of that system. Where deployers have identified a serious incident, they shall also immediately inform first the provider, and then the importer or distributor and the relevant market surveillance authorities of that incident. If the deployer is not able to reach the provider, Article 73 shall apply mutatis mutandis. This obligation shall not cover sensitive operational data of deployers of AI systems which are law enforcement authorities. For deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law, the monitoring obligation set out in the first subparagraph shall be deemed to be fulfilled by complying with the rules on internal governance arrangements, processes and mechanisms pursuant to the relevant financial service law.
