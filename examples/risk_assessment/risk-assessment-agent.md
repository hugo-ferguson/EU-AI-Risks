# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Medium: 16

## Requirement Findings

### FR-1

**Risk level:** medium

**Requirement:** The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.

**Analysis:** {"error": "invalid syntax"}

---

### FR-2

**Risk level:** medium

**Requirement:** The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.

**Analysis:** {"id": "art:14", "num": 14, "title": "Human oversight", "text": "1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section. 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer. 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state. 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.", "chapter_id": "ch:III", "chapter_title": "HIGH-RISK AI SYSTEMS", "paragraphs": [{"obligation_type": "requirement", "num": 1, "id": "art:14:p1", "text": "1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use."}, {"obligation_type": "requirement", "num": 2, "id": "art:14:p2", "text": "2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section."}, {"obligation_type": "requirement", "num": 3, "id": "art:14:p3", "text": "3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer."}, {"obligation_type": "requirement", "num": 4, "id": "art:14:p4", "text": "4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state."}, {"obligation_type": "requirement", "num": 5, "id": "art:14:p5", "text": "5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate."}], "dimensions": {"requirement_categories": ["human_oversight"], "responsible_parties": ["provider", "deployer"], "risk_categories": ["high_risk"], "data_categories": []} 

  








 








 








 








 








 








 








 








 








 








 








 








 








 








 

---

### FR-3

**Risk level:** medium

**Requirement:** The system shall rank candidates for recruiter review using the generated suitability score.

**Analysis:** {"id": "art:7", "num": 7, "title": "Amendments to Annex III", "text": "1. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend Annex III by adding or modifying use-cases of high-risk AI systems where both of the following conditions are fulfilled: (a) the AI systems are intended to be used in any of the areas listed in Annex III; (b) the AI systems pose a risk of harm to health and safety, or an adverse impact on fundamental rights, and that risk is equivalent to, or greater than, the risk of harm or of adverse impact posed by the high-risk AI systems already referred to in Annex III. 54/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks. 3. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend the list in Annex III by removing high-risk AI systems where both of the following conditions are fulfilled: (a) the high-risk AI system concerned no longer poses any significant risks to fundamental rights, health or safety, taking into account the criteria listed in paragraph 2; (b) the deletion does not decrease the overall level of protection of health, safety and fundamental rights under Union law.", "chapter_id": "ch:III", "chapter_title": "HIGH-RISK AI SYSTEMS", "paragraphs": [{"obligation_type": "permission", "num": 1, "id": "art:7:p1", "text": "1. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend Annex III by adding or modifying use-cases of high-risk AI systems where both of the following conditions are fulfilled: (a) the AI systems are intended to be used in any of the areas listed in Annex III; (b) the AI systems pose a risk of harm to health and safety, or an adverse impact on fundamental rights, and that risk is equivalent to, or greater than, the risk of harm or of adverse impact posed by the high-risk AI systems already referred to in Annex III. 54/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj"}, {"obligation_type": "requirement", "num": 2, "id": "art:7:p2", "text": "2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks."}, {"obligation_type": "permission", "num": 3, "id": "art:7:p3", "text": "3. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend the list in Annex III by removing high-risk AI systems where both of the following conditions are fulfilled: (a) the high-risk AI system concerned no longer poses any significant risks to fundamental rights, health or safety, taking into account the criteria listed in paragraph 2; (b) the deletion does not decrease the overall level of protection of health, safety and fundamental rights under Union law."}], "dimensions": {"requirement_categories": [], "responsible_parties": ["deployer", "national_competent_authority", "commission"], "risk_categories": ["high_risk"], "data_categories": ["personal_data", "special_category_personal_data"]}}

---

### FR-4

**Risk level:** medium

**Requirement:** The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.

**Analysis:** {"error": "Invalid tool call: search function requires at least one valid parameter"}

---

### FR-5

**Risk level:** medium

**Requirement:** The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.

**Analysis:** {}

---

### FR-6

**Risk level:** medium

**Requirement:** The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.

**Analysis:** {"id": "art:14", "num": "14", "title": "Human oversight", "text": "1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use. 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section. 3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer. 4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state. 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.", "chapter_id": "ch:III", "chapter_title": "HIGH-RISK AI SYSTEMS", "paragraphs": [{"obligation_type": "requirement", "num": "1", "id": "art:14:p1", "text": "1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use."}, {"obligation_type": "requirement", "num": "2", "id": "art:14:p2", "text": "2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section."}, {"obligation_type": "requirement", "num": "3", "id": "art:14:p3", "text": "3. The oversight measures shall be commensurate with the risks, level of autonomy and context of use of the high-risk AI system, and shall be ensured through either one or both of the following types of measures: (a) measures identified and built, when technically feasible, into the high-risk AI system by the provider before it is placed on the market or put into service; (b) measures identified by the provider before placing the high-risk AI system on the market or putting it into service and that are appropriate to be implemented by the deployer."}, {"obligation_type": "requirement", "num": "4", "id": "art:14:p4", "text": "4. For the purpose of implementing paragraphs 1, 2 and 3, the high-risk AI system shall be provided to the deployer in such a way that natural persons to whom human oversight is assigned are enabled, as appropriate and proportionate: (a) to properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation, including in view of detecting and addressing anomalies, dysfunctions and unexpected performance; (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons; (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available; 60/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system; (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state."}, {"obligation_type": "requirement", "num": "5", "id": "art:14:p5", "text": "5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate."}], "dimensions": {"requirement_categories": ["human_oversight"], "responsible_parties": ["provider", "deployer"], "risk_categories": ["high_risk"], "data_categories": []} 

  










 













 










 







 










 










 










 










 










 










 










 










 










 










 

---

### FR-7

**Risk level:** medium

**Requirement:** The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.

**Analysis:** {"id": "call_5f0861b2-8a49-420a-92bd-76725a42d8a1", "type": "function", "function": {"name": "get_references", "arguments": {"article_id": "art:12"}}}

---

### FR-8

**Risk level:** medium

**Requirement:** The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.

**Analysis:** The requirement for high-risk AI systems to maintain logs is outlined in Article 12. Specifically, paragraphs 1 and 3 detail that these systems must technically allow for the automatic recording of events over their lifetime, including the start and end times of each use, the reference database used for input data checks, the input data that led to matches, and the identification of individuals involved in result verification. The logs must be maintained throughout the system's lifecycle.

---

### FR-9

**Risk level:** medium

**Requirement:** The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.

**Analysis:** {"code": "```json\n{", "content": "```json\n{"}

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.

**Analysis:** This article outlines the Commission's responsibilities for evaluating and reviewing the Regulation to ensure its effectiveness and adaptability. It mandates annual assessments and periodic evaluations on specific topics, including the need for amendments to Annex III and Article 5, the functioning of the AI Office, and the development of voluntary codes of conduct. The Commission must submit reports to the European Parliament and the Council, considering input from various bodies and proposing amendments as necessary to address technological advancements and societal impacts.

---

### NFR-1

**Risk level:** medium

**Requirement:** The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.

**Analysis:** {"code": "1", "error": "Internal error", "message": "Internal error", "errorDetails": []}

---

### NFR-2

**Risk level:** medium

**Requirement:** The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.

**Analysis:** {"requirement": "Art. 10(3)", "dimension": "data_governance", "risk_category": "high_risk", "responsible_party": "provider", "data_category": "testing_data", "text": "3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof."}

---

### NFR-3

**Risk level:** medium

**Requirement:** The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.

**Analysis:** {"analysis": {"requirement": "Article 27 mandates a fundamental rights impact assessment (FRIA) for deployers of high-risk AI systems. This assessment includes evaluating the impact on specific categories of individuals and groups, particularly regarding risks of harm. The requirement aligns with the need to identify and mitigate potential negative consequences, including those related to protected attributes such as race, gender, or religion. The assessment must include an analysis of risks and corresponding mitigation measures.", "compliance_status": "The requirement in Article 27 is partially addressed by the given requirement. The requirement specifies avoiding decisions based on protected attributes, which is a key aspect of fundamental rights. However, the requirement does not explicitly mention conducting a FRIA or detailing the assessment process as outlined in Article 27. Therefore, it partially complies with the regulation.", "gap_analysis": "The requirement does not fully cover all aspects of Article 27. Specifically, it lacks explicit mention of the following elements required by Article 27: (1) the deployment-specific assessment of impact on fundamental rights, (2) the description of processes and usage frequency, (3) the identification of affected groups, (4) the analysis of specific risks and mitigation measures, and (5) the notification to market surveillance authorities. These omissions represent areas where the requirement does not fully align with the regulatory requirements."}}

---

### NFR-4

**Risk level:** medium

**Requirement:** The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.

**Analysis:** {"tool_response": {"output": "The content of Article 74 has been retrieved successfully."}}

---

### NFR-5

**Risk level:** medium

**Requirement:** The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.

**Analysis:** The requirement under Article 72 mandates providers to establish a post-market monitoring system that collects, documents, and analyzes data on high-risk AI systems' performance throughout their lifecycle. This system must enable providers to assess ongoing compliance with the requirements in Chapter III, Section 2, including interactions with other AI systems. However, it does not apply to sensitive operational data from law-enforcement deployers. The monitoring system must be based on a documented plan integrated into technical documentation, with a Commission-approved template to be finalized by 2026. For systems already under Union harmonization legislation, providers may integrate monitoring requirements if they achieve equivalent protection.

---

### NFR-6

**Risk level:** medium

**Requirement:** The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.

**Analysis:** {"analysis": {"compliance_status": "partially_compliant", "justification": "The requirement for a new conformity assessment procedure in the event of a substantial modification aligns with the provision in Article 43, paragraph 4. However, the requirement to rollback to a previous version or a validated state when a model fails safety checks is not explicitly covered under the provided text of Article 43. Therefore, the system is partially compliant."}, "risk_assessment": {"risk_level": "high", "justification": "The absence of a rollback mechanism for models that fail safety checks introduces a risk of continued deployment of non-compliant AI systems, which could lead to harm to health, safety, or fundamental rights."}, "recommendations": [{"action": "Implement a rollback mechanism that allows reverting to a previously validated state when a model fails safety checks.", "justification": "This would ensure compliance with the requirement for a new conformity assessment in the event of substantial modifications and prevent the deployment of non-compliant systems."}, {"action": "Document all modifications and their impact assessments as part of the technical documentation required under Annex IV, point 2(f).", "justification": "Proper documentation supports the conformity assessment process and ensures transparency and traceability of changes made to the AI system."}]}

---
