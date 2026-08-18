# EU AI Act Requirements Risk Report

This report maps extracted software requirements to candidate EU AI Act paragraphs using semantic similarity. It is an engineering review aid, not legal advice.

## Summary

- High: 4
- Medium: 168
- Low: 0
- Unmapped: 0

## Requirement Findings

### REQ-001

**Risk level:** Medium

**Requirement:** The system shall allow older adults to create an account using email, phone

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 5, paragraph 3 with score 0.786. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 5, paragraph 3 (art:5:p3), score 0.786
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 5, paragraph 5 (art:5:p5), score 0.786
  - Prohibited AI practices
  - 5. A Member State may decide to provide for the possibility to fully or partially authorise the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement within the limits and under the conditions listed in paragraph 1, first subparagraph, point (h), and paragraphs 2 and 3. Member States concerned shall lay down in their national law the necessary detailed rules for the request, issuance and exercise of, as well as supervision and reporting relating to, the authorisations referred to in paragraph 3. Those rules shall also specify in respect of which of the objectives listed in paragraph 1, first subparagraph, point (h), including which of the criminal offences referred to in point (h)(iii) thereof, the competent authorities may be authorised to use those systems for the purposes of law enforcement. Member States shall notify those rules to the Commission at the latest 30 days following the adoption thereof. Member States may introduce, in accordance with Union law, more restrictive laws on the use of remote biometric identification systems.
- Article 22, paragraph 1 (art:22:p1), score 0.784
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 50, paragraph 3 (art:50:p3), score 0.781
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 13, paragraph 3 (art:13:p3), score 0.778
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.

### REQ-002

**Risk level:** Medium

**Requirement:** The system shall allow users to enter basic profile information such as name, age,

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 71, paragraph 5 with score 0.814. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 71, paragraph 5 (art:71:p5), score 0.814
  - EU database for high-risk AI systems listed in Annex III
  - 5. The EU database shall contain personal data only in so far as necessary for collecting and processing information in accordance with this Regulation. That information shall include the names and contact details of natural persons who are responsible for registering the system and have the legal authority to represent the provider or the deployer, as applicable. 100/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 50, paragraph 3 (art:50:p3), score 0.808
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 5, paragraph 2 (art:5:p2), score 0.802
  - Prohibited AI practices
  - 2. The use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), shall be deployed for the purposes set out in that point only to confirm the identity of the specifically targeted individual, and it shall take into account the following elements: (a) the nature of the situation giving rise to the possible use, in particular the seriousness, probability and scale of the harm that would be caused if the system were not used; (b) the consequences of the use of the system for the rights and freedoms of all persons concerned, in particular the seriousness, probability and scale of those consequences. In addition, the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), of this Article shall comply with necessary and proportionate safeguards and conditions in relation to the use in accordance with the national law authorising the use thereof, in particular as regards the temporal, geographic and personal limitations. The use of the ‘real-time’ remote biometric identification system in publicly accessible spaces shall be authorised only if the law enforcement authority has completed a fundamental rights impact assessment as provided for in Article 27 and has registered the system in the EU database according to Article 49. However, in duly justified cases of urgency, the use of such systems may be commenced without the registration in the EU database, provided that such registration is completed without undue delay.
- Article 28, paragraph 7 (art:28:p7), score 0.799
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 9, paragraph 9 (art:9:p9), score 0.799
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.

### REQ-003

**Risk level:** Medium

**Requirement:** The system shall allow users to update their health profile at any time.

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 36, paragraph 9 with score 0.801. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 9 (art:36:p9), score 0.801
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 7, paragraph 2 (art:7:p2), score 0.798
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 112, paragraph 10 (art:112:p10), score 0.790
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 50, paragraph 1 (art:50:p1), score 0.788
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 28, paragraph 7 (art:28:p7), score 0.786
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.

### REQ-004

**Risk level:** Medium

**Requirement:** The system shall allow users to nominate caregivers, family members, or

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.818. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.818
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 28, paragraph 7 (art:28:p7), score 0.808
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 22, paragraph 2 (art:22:p2), score 0.806
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 26, paragraph 2 (art:26:p2), score 0.806
  - Obligations of deployers of high-risk AI systems
  - 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.
- Article 113, paragraph 3 (art:113:p3), score 0.802
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.

### REQ-005

**Risk level:** Medium

**Requirement:** The system shall support different user roles, including older adult, caregiver,

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 22, paragraph 2 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 22, paragraph 2 (art:22:p2), score 0.803
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 71, paragraph 6 (art:71:p6), score 0.797
  - EU database for high-risk AI systems listed in Annex III
  - 6. The Commission shall be the controller of the EU database. It shall make available to providers, prospective providers and deployers adequate technical and administrative support. The EU database shall comply with the applicable accessibility requirements.
- Article 22, paragraph 1 (art:22:p1), score 0.794
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 9, paragraph 9 (art:9:p9), score 0.793
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
- Article 54, paragraph 2 (art:54:p2), score 0.791
  - Authorised representatives of providers of general-purpose AI models
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.

### REQ-006

**Risk level:** Medium

**Requirement:** The system shall allow users to set accessibility preferences such as larger text,

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.805. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.805
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 7, paragraph 1 (art:7:p1), score 0.790
  - Amendments to Annex III
  - 1. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend Annex III by adding or modifying use-cases of high-risk AI systems where both of the following conditions are fulfilled: (a) the AI systems are intended to be used in any of the areas listed in Annex III; (b) the AI systems pose a risk of harm to health and safety, or an adverse impact on fundamental rights, and that risk is equivalent to, or greater than, the risk of harm or of adverse impact posed by the high-risk AI systems already referred to in Annex III. 54/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 71, paragraph 6 (art:71:p6), score 0.789
  - EU database for high-risk AI systems listed in Annex III
  - 6. The Commission shall be the controller of the EU database. It shall make available to providers, prospective providers and deployers adequate technical and administrative support. The EU database shall comply with the applicable accessibility requirements.
- Article 7, paragraph 2 (art:7:p2), score 0.786
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 92, paragraph 4 (art:92:p4), score 0.785
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.

### REQ-007

**Risk level:** Medium

**Requirement:** The system shall allow users to add prescribed medications, including dosage,

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.798. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.798
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 8, paragraph 2 (art:8:p2), score 0.794
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 112, paragraph 10 (art:112:p10), score 0.793
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 9, paragraph 4 (art:9:p4), score 0.792
  - Risk management system
  - 4. The risk management measures referred to in paragraph 2, point (d), shall give due consideration to the effects and possible interaction resulting from the combined application of the requirements set out in this Section, with a view to minimising risks more effectively while achieving an appropriate balance in implementing the measures to fulfil those requirements.
- Article 113, paragraph 3 (art:113:p3), score 0.791
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.

### REQ-008

**Risk level:** Medium

**Requirement:** The system shall send medication reminders at scheduled times.

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 31, paragraph 8 with score 0.828. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 31, paragraph 8 (art:31:p8), score 0.828
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 11 (art:31:p11), score 0.821
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 31, paragraph 6 (art:31:p6), score 0.818
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.
- Article 31, paragraph 2 (art:31:p2), score 0.813
  - Requirements relating to notified bodies
  - 2. Notified bodies shall satisfy the organisational, quality management, resources and process requirements that are necessary to fulfil their tasks, as well as suitable cybersecurity requirements.
- Article 28, paragraph 7 (art:28:p7), score 0.811
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.

### REQ-009

**Risk level:** Medium

**Requirement:** The system shall allow users to confirm whether they have taken, skipped, or

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 44, paragraph 3 with score 0.820. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 44, paragraph 3 (art:44:p3), score 0.820
  - Certificates
  - 3. Where a notified body finds that an AI system no longer meets the requirements set out in Section 2, it shall, taking account of the principle of proportionality, suspend or withdraw the certificate issued or impose restrictions on it, unless compliance with those requirements is ensured by appropriate corrective action taken by the provider of the system within an appropriate deadline set by the notified body. The notified body shall give reasons for its decision. An appeal procedure against decisions of the notified bodies, including on conformity certificates issued, shall be available.
- Article 36, paragraph 7 (art:36:p7), score 0.810
  - Changes to notifications
  - 7. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall: (a) assess the impact on the certificates issued by the notified body; (b) submit a report on its findings to the Commission and the other Member States within three months of having notified the changes to the designation; (c) require the notified body to suspend or withdraw, within a reasonable period of time determined by the authority, any certificates which were unduly issued, in order to ensure the continuing conformity of high-risk AI systems on the market; (d) inform the Commission and the Member States about certificates the suspension or withdrawal of which it has required; (e) provide the national competent authorities of the Member State in which the provider has its registered place of business with all relevant information about the certificates of which it has required the suspension or withdrawal; that authority shall take the appropriate measures, where necessary, to avoid a potential risk to health, safety or fundamental rights.
- Article 5, paragraph 3 (art:5:p3), score 0.806
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 27, paragraph 3 (art:27:p3), score 0.805
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.
- Article 36, paragraph 9 (art:36:p9), score 0.804
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.

### REQ-010

**Risk level:** Medium

**Requirement:** The system shall notify caregivers if a critical medication is repeatedly missed.

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.808. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.808
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 45, paragraph 2 (art:45:p2), score 0.804
  - Information obligations of notified bodies
  - 2. Each notified body shall inform the other notified bodies of: (a) quality management system approvals which it has refused, suspended or withdrawn, and, upon request, of quality system approvals which it has issued; (b) Union technical documentation assessment certificates or any supplements thereto which it has refused, withdrawn, suspended or otherwise restricted, and, upon request, of the certificates and/or supplements thereto which it has issued.
- Article 36, paragraph 4 (art:36:p4), score 0.803
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 31, paragraph 6 (art:31:p6), score 0.803
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.
- Article 28, paragraph 7 (art:28:p7), score 0.802
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.

### REQ-011

**Risk level:** Medium

**Requirement:** The system shall provide warnings for potential medication conflicts based on

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.819. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.819
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 90, paragraph 3 (art:90:p3), score 0.818
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 52, paragraph 1 (art:52:p1), score 0.813
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 6, paragraph 3 (art:6:p3), score 0.812
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- Article 79, paragraph 6 (art:79:p6), score 0.811
  - Procedure at national level for dealing with AI systems presenting a risk
  - 6. The notification referred to in paragraph 5 shall include all available details, in particular the information necessary for the identification of the non-compliant AI system, the origin of the AI system and the supply chain, the nature of the non-compliance alleged and the risk involved, the nature and duration of the national measures taken and the arguments put forward by the relevant operator. In particular, the market surveillance authorities shall indicate whether the non-compliance is due to one or more of the following: (a) non-compliance with the prohibition of the AI practices referred to in Article 5; (b) a failure of a high-risk AI system to meet requirements set out in Chapter III, Section 2; (c) shortcomings in the harmonised standards or common specifications referred to in Articles 40 and 41 conferring a presumption of conformity; (d) non-compliance with Article 50.

### REQ-012

**Risk level:** Medium

**Requirement:** The system shall allow healthcare professionals or caregivers to update

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.821. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.821
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 112, paragraph 10 (art:112:p10), score 0.818
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 31, paragraph 10 (art:31:p10), score 0.815
  - Requirements relating to notified bodies
  - 10. Notified bodies shall be capable of carrying out all their tasks under this Regulation with the highest degree of professional integrity and the requisite competence in the specific field, whether those tasks are carried out by notified bodies themselves or on their behalf and under their responsibility.
- Article 31, paragraph 11 (art:31:p11), score 0.814
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 22, paragraph 2 (art:22:p2), score 0.813
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.

### REQ-013

**Risk level:** Medium

**Requirement:** The system shall provide an AI-powered virtual assistant that can answer general

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 75, paragraph 1 with score 0.834. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 75, paragraph 1 (art:75:p1), score 0.834
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 92, paragraph 5 (art:92:p5), score 0.827
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 91, paragraph 2 (art:91:p2), score 0.827
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 92, paragraph 7 (art:92:p7), score 0.822
  - Power to conduct evaluations
  - 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.
- Article 93, paragraph 2 (art:93:p2), score 0.819
  - Power to request measures
  - 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.

### REQ-014

**Risk level:** Medium

**Requirement:** The system shall allow users to interact with the AI assistant using text or voice.

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.838. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.838
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 2 (art:50:p2), score 0.832
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 75, paragraph 1 (art:75:p1), score 0.825
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 91, paragraph 2 (art:91:p2), score 0.823
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 49, paragraph 1 (art:49:p1), score 0.822
  - Section A — Information to be submitted by providers of high-risk AI systems in accordance with Article 49(1)
  - 1. A general description of the general-purpose AI model including: (a) the tasks that the model is intended to perform and the type and nature of AI systems into which it can be integrated; (b) the acceptable use policies applicable; (c) the date of release and methods of distribution; (d) how the model interacts, or can be used to interact, with hardware or software that is not part of the model itself, where applicable; (e) the versions of relevant software related to the use of the general-purpose AI model, where applicable; (f) the architecture and number of parameters; (g) the modality (e.g. text, image) and format of inputs and outputs; (h) the licence for the model.

### REQ-015

**Risk level:** Medium

**Requirement:** The system shall provide health guidance based on the user’s profile, symptoms,

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.817. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.817
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 13, paragraph 3 (art:13:p3), score 0.809
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- Article 50, paragraph 3 (art:50:p3), score 0.805
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 6, paragraph 3 (art:6:p3), score 0.800
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- Article 9, paragraph 9 (art:9:p9), score 0.799
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.

### REQ-016

**Risk level:** Medium

**Requirement:** The system shall clearly advise users to contact a healthcare professional or

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 22, paragraph 1 with score 0.824. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 22, paragraph 1 (art:22:p1), score 0.824
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 22, paragraph 2 (art:22:p2), score 0.815
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 28, paragraph 7 (art:28:p7), score 0.814
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 50, paragraph 1 (art:50:p1), score 0.809
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 7, paragraph 2 (art:7:p2), score 0.807
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-017

**Risk level:** Medium

**Requirement:** The system shall not provide a final medical diagnosis without professional clinical

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 52, paragraph 2 with score 0.809. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 2 (art:52:p2), score 0.809
  - Procedure
  - 2. The provider of a general-purpose AI model that meets the condition referred to in Article 51(1), point (a), may present, with its notification, sufficiently substantiated arguments to demonstrate that, exceptionally, although it meets that requirement, the general-purpose AI model does not present, due to its specific characteristics, systemic risks and therefore should not be classified as a general-purpose AI model with systemic risk.
- Article 9, paragraph 7 (art:9:p7), score 0.805
  - Risk management system
  - 7. Testing procedures may include testing in real-world conditions in accordance with Article 60.
- Article 52, paragraph 3 (art:52:p3), score 0.804
  - Procedure
  - 3. Where the Commission concludes that the arguments submitted pursuant to paragraph 2 are not sufficiently substantiated and the relevant provider was not able to demonstrate that the general-purpose AI model does not present, due to its specific characteristics, systemic risks, it shall reject those arguments, and the general-purpose AI model shall be considered to be a general-purpose AI model with systemic risk.
- Article 73, paragraph 6 (art:73:p6), score 0.800
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 6, paragraph 4 (art:6:p4), score 0.799
  - Classification rules for high-risk AI systems
  - 4. A provider who considers that an AI system referred to in Annex III is not high-risk shall document its assessment before that system is placed on the market or put into service. Such provider shall be subject to the registration obligation set out in Article 49(2). Upon request of national competent authorities, the provider shall provide the documentation of the assessment.

### REQ-018

**Risk level:** Medium

**Requirement:** The system shall explain AI-generated suggestions in plain, understandable terms.

**Source:** examples\sample_srs_health_app.pdf, page 1

**Explanation:** Mapped to Article 50, paragraph 2 with score 0.804. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 50, paragraph 2 (art:50:p2), score 0.804
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 64, paragraph 1 (art:64:p1), score 0.796
  - AI Office
  - 1. The Commission shall develop Union expertise and capabilities in the field of AI through the AI Office.
- Article 50, paragraph 1 (art:50:p1), score 0.795
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 75, paragraph 1 (art:75:p1), score 0.795
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 1, paragraph 1 (art:1:p1), score 0.793
  - Subject matter`
  - 1. The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter, including democracy, the rule of law and environmental protection, against the harmful effects of AI systems in the Union and supporting innovation.

### REQ-019

**Risk level:** Medium

**Requirement:** The system shall allow users to record symptoms such as pain, dizziness,

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.803. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.803
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 12, paragraph 1 (art:12:p1), score 0.803
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 3 (art:12:p3), score 0.803
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.801
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 50, paragraph 3 (art:50:p3), score 0.787
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-020

**Risk level:** Medium

**Requirement:** The system shall ask follow-up questions to better understand reported symptoms.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 73, paragraph 6 with score 0.804. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 73, paragraph 6 (art:73:p6), score 0.804
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 45, paragraph 2 (art:45:p2), score 0.804
  - Information obligations of notified bodies
  - 2. Each notified body shall inform the other notified bodies of: (a) quality management system approvals which it has refused, suspended or withdrawn, and, upon request, of quality system approvals which it has issued; (b) Union technical documentation assessment certificates or any supplements thereto which it has refused, withdrawn, suspended or otherwise restricted, and, upon request, of the certificates and/or supplements thereto which it has issued.
- Article 45, paragraph 3 (art:45:p3), score 0.803
  - Information obligations of notified bodies
  - 3. Each notified body shall provide the other notified bodies carrying out similar conformity assessment activities covering the same types of AI systems with relevant information on issues relating to negative and, on request, positive conformity assessment results.
- Article 73, paragraph 2 (art:73:p2), score 0.798
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- Article 72, paragraph 1 (art:72:p1), score 0.798
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.

### REQ-021

**Risk level:** Medium

**Requirement:** The system shall classify symptoms by urgency, such as low, moderate, urgent, or

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 6, paragraph 3 with score 0.807. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 6, paragraph 3 (art:6:p3), score 0.807
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- Article 31, paragraph 8 (art:31:p8), score 0.806
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 28, paragraph 7 (art:28:p7), score 0.805
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 52, paragraph 1 (art:52:p1), score 0.805
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 31, paragraph 11 (art:31:p11), score 0.801
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.

### REQ-022

**Risk level:** Medium

**Requirement:** The system shall recommend next steps, such as self-care, booking an

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 9, paragraph 2 with score 0.797. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 9, paragraph 2 (art:9:p2), score 0.797
  - Risk management system
  - 2. The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating. It shall comprise the following steps: (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose; (b) the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse; (c) the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72; (d) the adoption of appropriate and targeted risk management measures designed to address the risks identified pursuant to point (a).
- Article 52, paragraph 1 (art:52:p1), score 0.792
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 31, paragraph 8 (art:31:p8), score 0.791
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 113, paragraph 3 (art:113:p3), score 0.789
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 112, paragraph 10 (art:112:p10), score 0.789
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.

### REQ-023

**Risk level:** Medium

**Requirement:** The system shall allow users to record daily health status, mood, sleep, appetite,

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.811. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.811
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 1 (art:12:p1), score 0.808
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 2 (art:12:p2), score 0.803
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 7, paragraph 2 (art:7:p2), score 0.801
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 50, paragraph 3 (art:50:p3), score 0.796
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-024

**Risk level:** Medium

**Requirement:** The system shall detect unusual changes in health patterns and notify the user or

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 36, paragraph 7 with score 0.813. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 36, paragraph 7 (art:36:p7), score 0.813
  - Changes to notifications
  - 7. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall: (a) assess the impact on the certificates issued by the notified body; (b) submit a report on its findings to the Commission and the other Member States within three months of having notified the changes to the designation; (c) require the notified body to suspend or withdraw, within a reasonable period of time determined by the authority, any certificates which were unduly issued, in order to ensure the continuing conformity of high-risk AI systems on the market; (d) inform the Commission and the Member States about certificates the suspension or withdrawal of which it has required; (e) provide the national competent authorities of the Member State in which the provider has its registered place of business with all relevant information about the certificates of which it has required the suspension or withdrawal; that authority shall take the appropriate measures, where necessary, to avoid a potential risk to health, safety or fundamental rights.
- Article 36, paragraph 6 (art:36:p6), score 0.809
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 27, paragraph 3 (art:27:p3), score 0.804
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.
- Article 72, paragraph 1 (art:72:p1), score 0.801
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- Article 36, paragraph 9 (art:36:p9), score 0.799
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.

### REQ-025

**Risk level:** Medium

**Requirement:** The system shall allow users to manually enter vital signs such as blood pressure,

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 50, paragraph 3 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 3 (art:50:p3), score 0.803
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 5, paragraph 5 (art:5:p5), score 0.803
  - Prohibited AI practices
  - 5. A Member State may decide to provide for the possibility to fully or partially authorise the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement within the limits and under the conditions listed in paragraph 1, first subparagraph, point (h), and paragraphs 2 and 3. Member States concerned shall lay down in their national law the necessary detailed rules for the request, issuance and exercise of, as well as supervision and reporting relating to, the authorisations referred to in paragraph 3. Those rules shall also specify in respect of which of the objectives listed in paragraph 1, first subparagraph, point (h), including which of the criminal offences referred to in point (h)(iii) thereof, the competent authorities may be authorised to use those systems for the purposes of law enforcement. Member States shall notify those rules to the Commission at the latest 30 days following the adoption thereof. Member States may introduce, in accordance with Union law, more restrictive laws on the use of remote biometric identification systems.
- Article 7, paragraph 2 (art:7:p2), score 0.802
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 5, paragraph 3 (art:5:p3), score 0.799
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 5, paragraph 2 (art:5:p2), score 0.796
  - Prohibited AI practices
  - 2. The use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), shall be deployed for the purposes set out in that point only to confirm the identity of the specifically targeted individual, and it shall take into account the following elements: (a) the nature of the situation giving rise to the possible use, in particular the seriousness, probability and scale of the harm that would be caused if the system were not used; (b) the consequences of the use of the system for the rights and freedoms of all persons concerned, in particular the seriousness, probability and scale of those consequences. In addition, the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), of this Article shall comply with necessary and proportionate safeguards and conditions in relation to the use in accordance with the national law authorising the use thereof, in particular as regards the temporal, geographic and personal limitations. The use of the ‘real-time’ remote biometric identification system in publicly accessible spaces shall be authorised only if the law enforcement authority has completed a fundamental rights impact assessment as provided for in Article 27 and has registered the system in the EU database according to Article 49. However, in duly justified cases of urgency, the use of such systems may be commenced without the registration in the EU database, provided that such registration is completed without undue delay.

### REQ-026

**Risk level:** Medium

**Requirement:** The system shall integrate with compatible wearable devices or home monitoring

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 5, paragraph 4 with score 0.792. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 5, paragraph 4 (art:5:p4), score 0.792
  - Prohibited AI practices
  - 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- Article 8, paragraph 2 (art:8:p2), score 0.790
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 72, paragraph 3 (art:72:p3), score 0.787
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 72, paragraph 1 (art:72:p1), score 0.785
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- Article 50, paragraph 3 (art:50:p3), score 0.781
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-027

**Risk level:** Medium

**Requirement:** The system shall display health trends over time using simple charts and

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 36, paragraph 9 with score 0.759. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 9 (art:36:p9), score 0.759
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 72, paragraph 3 (art:72:p3), score 0.759
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 10, paragraph 4 (art:10:p4), score 0.759
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- Article 10, paragraph 3 (art:10:p3), score 0.758
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 7, paragraph 2 (art:7:p2), score 0.756
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-028

**Risk level:** Medium

**Requirement:** The system shall alert users when recorded values fall outside safe or

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 12, paragraph 1 with score 0.824. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 1 (art:12:p1), score 0.824
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 2 (art:12:p2), score 0.823
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 72, paragraph 1 (art:72:p1), score 0.821
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- Article 60, paragraph 7 (art:60:p7), score 0.815
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 7. Any serious incident identified in the course of the testing in real world conditions shall be reported to the national market surveillance authority in accordance with Article 73. The provider or prospective provider shall adopt immediate mitigation measures or, failing that, shall suspend the testing in real world conditions until such mitigation takes place, or otherwise terminate it. The provider or prospective provider shall establish a procedure for the prompt recall of the AI system upon such termination of the testing in real world conditions.
- Article 73, paragraph 1 (art:73:p1), score 0.815
  - Reporting of serious incidents
  - 1. Providers of high-risk AI systems placed on the Union market shall report any serious incident to the market surveillance authorities of the Member States where that incident occurred.

### REQ-029

**Risk level:** Medium

**Requirement:** The system shall allow healthcare providers to review shared vital sign data with

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 113, paragraph 5 with score 0.819. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 113, paragraph 5 (art:113:p5), score 0.819
  - Entry into force and application
  - 5. Surveillance of the approved quality management system. 5.1. The purpose of the surveillance carried out by the notified body referred to in Point 3 is to make sure that the provider duly complies with the terms and conditions of the approved quality management system. 5.2. For assessment purposes, the provider shall allow the notified body to access the premises where the design, development, testing of the AI systems is taking place. The provider shall further share with the notified body all necessary information. 5.3. The notified body shall carry out periodic audits to make sure that the provider maintains and applies the quality management system and shall provide the provider with an audit report. In the context of those audits, the notified body may carry out additional tests of the AI systems for which a Union technical documentation assessment certificate was issued. ANNEX VIII Information to be submitted upon the registration of high-risk AI systems in accordance with
- Article 7, paragraph 2 (art:7:p2), score 0.817
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 10, paragraph 2 (art:10:p2), score 0.814
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 72, paragraph 3 (art:72:p3), score 0.812
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 72, paragraph 1 (art:72:p1), score 0.812
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.

### REQ-030

**Risk level:** Medium

**Requirement:** The system shall allow users to record upcoming medical appointments.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.816. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.816
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 1 (art:12:p1), score 0.805
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 31, paragraph 8 (art:31:p8), score 0.800
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 12, paragraph 2 (art:12:p2), score 0.796
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 52, paragraph 1 (art:52:p1), score 0.796
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.

### REQ-031

**Risk level:** Medium

**Requirement:** The system shall send reminders before scheduled appointments.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 31, paragraph 8 with score 0.830. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 31, paragraph 8 (art:31:p8), score 0.830
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 28, paragraph 7 (art:28:p7), score 0.824
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 31, paragraph 11 (art:31:p11), score 0.823
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 31, paragraph 6 (art:31:p6), score 0.819
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.
- Article 37, paragraph 2 (art:37:p2), score 0.812
  - Challenge to the competence of notified bodies
  - 2. The notifying authority shall provide the Commission, on request, with all relevant information relating to the notification or the maintenance of the competence of the notified body concerned.

### REQ-032

**Risk level:** Medium

**Requirement:** The system shall allow users to store appointment details such as doctor name,

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 71, paragraph 5 with score 0.812. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 71, paragraph 5 (art:71:p5), score 0.812
  - EU database for high-risk AI systems listed in Annex III
  - 5. The EU database shall contain personal data only in so far as necessary for collecting and processing information in accordance with this Regulation. That information shall include the names and contact details of natural persons who are responsible for registering the system and have the legal authority to represent the provider or the deployer, as applicable. 100/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 12, paragraph 3 (art:12:p3), score 0.793
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 113, paragraph 3 (art:113:p3), score 0.792
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 13, paragraph 3 (art:13:p3), score 0.792
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- Article 10, paragraph 5 (art:10:p5), score 0.791
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.

### REQ-033

**Risk level:** Medium

**Requirement:** The system shall allow caregivers to view or manage appointments with user

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.806. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.806
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 5 (art:50:p5), score 0.797
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 92, paragraph 5 (art:92:p5), score 0.795
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 50, paragraph 3 (art:50:p3), score 0.791
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 92, paragraph 4 (art:92:p4), score 0.791
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.

### REQ-034

**Risk level:** Medium

**Requirement:** The system shall support telehealth appointment links where available.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 22, paragraph 1 with score 0.789. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 22, paragraph 1 (art:22:p1), score 0.789
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 13, paragraph 3 (art:13:p3), score 0.784
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- Article 112, paragraph 10 (art:112:p10), score 0.784
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 50, paragraph 1 (art:50:p1), score 0.783
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 5, paragraph 5 (art:5:p5), score 0.781
  - Prohibited AI practices
  - 5. A Member State may decide to provide for the possibility to fully or partially authorise the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement within the limits and under the conditions listed in paragraph 1, first subparagraph, point (h), and paragraphs 2 and 3. Member States concerned shall lay down in their national law the necessary detailed rules for the request, issuance and exercise of, as well as supervision and reporting relating to, the authorisations referred to in paragraph 3. Those rules shall also specify in respect of which of the objectives listed in paragraph 1, first subparagraph, point (h), including which of the criminal offences referred to in point (h)(iii) thereof, the competent authorities may be authorised to use those systems for the purposes of law enforcement. Member States shall notify those rules to the Commission at the latest 30 days following the adoption thereof. Member States may introduce, in accordance with Union law, more restrictive laws on the use of remote biometric identification systems.

### REQ-035

**Risk level:** Medium

**Requirement:** The system shall allow users to record questions they want to ask their doctor.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.809. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.809
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 91, paragraph 2 (art:91:p2), score 0.805
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 91, paragraph 3 (art:91:p3), score 0.804
  - Power to request documentation and information
  - 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
- Article 12, paragraph 1 (art:12:p1), score 0.803
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 93, paragraph 2 (art:93:p2), score 0.800
  - Power to request measures
  - 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.

### REQ-036

**Risk level:** Medium

**Requirement:** The system shall provide a clearly visible emergency assistance button.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.794. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.794
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 73, paragraph 11 (art:73:p11), score 0.788
  - Reporting of serious incidents
  - 11. National competent authorities shall immediately notify the Commission of any serious incident, whether or not they have taken action on it, in accordance with Article 20 of Regulation (EU) 2019/1020. SECTION 3 Enforcement
- Article 90, paragraph 3 (art:90:p3), score 0.785
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 28, paragraph 3 (art:28:p3), score 0.781
  - Notifying authorities
  - 3. Notifying authorities shall be established, organised and operated in such a way that no conflict of interest arises with conformity assessment bodies, and that the objectivity and impartiality of their activities are safeguarded.
- Article 70, paragraph 5 (art:70:p5), score 0.776
  - Designation of national competent authorities and single points of contact
  - 5. When performing their tasks, the national competent authorities shall act in accordance with the confidentiality obligations set out in Article 78.

### REQ-037

**Risk level:** Medium

**Requirement:** The system shall allow users to contact emergency services from within the app.

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.784. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.784
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 31, paragraph 11 (art:31:p11), score 0.779
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 92, paragraph 4 (art:92:p4), score 0.779
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.
- Article 70, paragraph 2 (art:70:p2), score 0.779
  - Designation of national competent authorities and single points of contact
  - 2. Member States shall communicate to the Commission the identity of the notifying authorities and the market surveillance authorities and the tasks of those authorities, as well as any subsequent changes thereto. Member States shall make publicly available information on how competent authorities and single points of contact can be contacted, through electronic communication means by 2 August 2025. Member States shall designate a market surveillance authority to act as the single point of contact for this Regulation, and shall notify the Commission of the identity of the single point of contact. The Commission shall make a list of the single points of contact publicly available.
- Article 73, paragraph 9 (art:73:p9), score 0.775
  - Reporting of serious incidents
  - 9. For high-risk AI systems referred to in Annex III that are placed on the market or put into service by providers that are subject to Union legislative instruments laying down reporting obligations equivalent to those set out in this Regulation, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c).

### REQ-038

**Risk level:** Medium

**Requirement:** The system shall allow users to notify emergency contacts during a health

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.850. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.850
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 28, paragraph 6 (art:28:p6), score 0.834
  - Notifying authorities
  - 6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 31, paragraph 11 (art:31:p11), score 0.833
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 31, paragraph 8 (art:31:p8), score 0.830
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 6 (art:31:p6), score 0.829
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.

### REQ-039

**Risk level:** Medium

**Requirement:** The system shall share critical medical information with emergency contacts if the

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 73, paragraph 4 with score 0.816. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 73, paragraph 4 (art:73:p4), score 0.816
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 45, paragraph 4 (art:45:p4), score 0.812
  - Information obligations of notified bodies
  - 4. Notified bodies shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 28, paragraph 7 (art:28:p7), score 0.810
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 78, paragraph 3 (art:78:p3), score 0.810
  - Confidentiality
  - 3. Without prejudice to paragraphs 1 and 2, information exchanged on a confidential basis between the national competent authorities or between national competent authorities and the Commission shall not be disclosed without prior consultation of the originating national competent authority and the deployer when high-risk AI systems referred to in point 1, 6 or 7 of Annex III are used by law enforcement, border control, immigration or asylum authorities and when such disclosure would jeopardise public and national security interests. This exchange of information shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities. When the law enforcement, immigration or asylum authorities are providers of high-risk AI systems referred to in point 1, 6 or 7 of Annex III, the technical documentation referred to in Annex IV shall remain within the premises of those authorities. Those authorities shall ensure that the market surveillance authorities referred to in Article 74(8) and (9), as applicable, can, upon request, immediately access the documentation or obtain a copy thereof. Only staff of the market surveillance authority holding the appropriate level of security clearance shall be allowed to access that documentation or any copy thereof.
- Article 38, paragraph 3 (art:38:p3), score 0.810
  - Coordination of notified bodies
  - 3. The Commission shall provide for the exchange of knowledge and best practices between notifying authorities.

### REQ-040

**Risk level:** Medium

**Requirement:** The system shall detect emergency keywords or severe symptoms and

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 73, paragraph 9 with score 0.818. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 73, paragraph 9 (art:73:p9), score 0.818
  - Reporting of serious incidents
  - 9. For high-risk AI systems referred to in Annex III that are placed on the market or put into service by providers that are subject to Union legislative instruments laying down reporting obligations equivalent to those set out in this Regulation, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c).
- Article 73, paragraph 10 (art:73:p10), score 0.813
  - Reporting of serious incidents
  - 10. For high-risk AI systems which are safety components of devices, or are themselves devices, covered by Regulations (EU) 2017/745 and (EU) 2017/746, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c) of this Regulation, and shall be made to the national competent authority chosen for that purpose by the Member States where the incident occurred.
- Article 73, paragraph 2 (art:73:p2), score 0.808
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- Article 73, paragraph 6 (art:73:p6), score 0.808
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 90, paragraph 3 (art:90:p3), score 0.807
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.

### REQ-041

**Risk level:** Medium

**Requirement:** The system shall provide location-sharing support during emergencies, subject to

**Source:** examples\sample_srs_health_app.pdf, page 2

**Explanation:** Mapped to Article 73, paragraph 4 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 73, paragraph 4 (art:73:p4), score 0.803
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 12, paragraph 2 (art:12:p2), score 0.794
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 5, paragraph 2 (art:5:p2), score 0.792
  - Prohibited AI practices
  - 2. The use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), shall be deployed for the purposes set out in that point only to confirm the identity of the specifically targeted individual, and it shall take into account the following elements: (a) the nature of the situation giving rise to the possible use, in particular the seriousness, probability and scale of the harm that would be caused if the system were not used; (b) the consequences of the use of the system for the rights and freedoms of all persons concerned, in particular the seriousness, probability and scale of those consequences. In addition, the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), of this Article shall comply with necessary and proportionate safeguards and conditions in relation to the use in accordance with the national law authorising the use thereof, in particular as regards the temporal, geographic and personal limitations. The use of the ‘real-time’ remote biometric identification system in publicly accessible spaces shall be authorised only if the law enforcement authority has completed a fundamental rights impact assessment as provided for in Article 27 and has registered the system in the EU database according to Article 49. However, in duly justified cases of urgency, the use of such systems may be commenced without the registration in the EU database, provided that such registration is completed without undue delay.
- Article 73, paragraph 3 (art:73:p3), score 0.791
  - Reporting of serious incidents
  - 3. Notwithstanding paragraph 2 of this Article, in the event of a widespread infringement or a serious incident as defined in Article 3, point (49)(b), the report referred to in paragraph 1 of this Article shall be provided immediately, and not later than two days after the provider or, where applicable, the deployer becomes aware of that incident.
- Article 12, paragraph 3 (art:12:p3), score 0.791
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).

### REQ-042

**Risk level:** Medium

**Requirement:** The system shall allow users to invite trusted caregivers or family members.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 22, paragraph 2 with score 0.800. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 22, paragraph 2 (art:22:p2), score 0.800
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 50, paragraph 1 (art:50:p1), score 0.795
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 22, paragraph 1 (art:22:p1), score 0.795
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 28, paragraph 7 (art:28:p7), score 0.795
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 21, paragraph 1 (art:21:p1), score 0.792
  - Cooperation with competent authorities
  - 1. Providers of high-risk AI systems shall, upon a reasoned request by a competent authority, provide that authority all the information and documentation necessary to demonstrate the conformity of the high-risk AI system with the requirements set out in Section 2, in a language which can be easily understood by the authority in one of the official languages of the institutions of the Union as indicated by the Member State concerned.

### REQ-043

**Risk level:** Medium

**Requirement:** The system shall allow users to control what information caregivers can see.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.817. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.817
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 5 (art:50:p5), score 0.812
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 75, paragraph 1 (art:75:p1), score 0.808
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 50, paragraph 2 (art:50:p2), score 0.806
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 28, paragraph 7 (art:28:p7), score 0.804
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.

### REQ-044

**Risk level:** Medium

**Requirement:** The system shall notify caregivers about missed medication, abnormal health

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 45, paragraph 2 with score 0.813. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 45, paragraph 2 (art:45:p2), score 0.813
  - Information obligations of notified bodies
  - 2. Each notified body shall inform the other notified bodies of: (a) quality management system approvals which it has refused, suspended or withdrawn, and, upon request, of quality system approvals which it has issued; (b) Union technical documentation assessment certificates or any supplements thereto which it has refused, withdrawn, suspended or otherwise restricted, and, upon request, of the certificates and/or supplements thereto which it has issued.
- Article 28, paragraph 7 (art:28:p7), score 0.812
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 31, paragraph 6 (art:31:p6), score 0.812
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.
- Article 31, paragraph 8 (art:31:p8), score 0.809
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 52, paragraph 1 (art:52:p1), score 0.809
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.

### REQ-045

**Risk level:** Medium

**Requirement:** The system shall allow caregivers to send reminders or supportive messages to

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.823. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.823
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 37, paragraph 2 (art:37:p2), score 0.813
  - Challenge to the competence of notified bodies
  - 2. The notifying authority shall provide the Commission, on request, with all relevant information relating to the notification or the maintenance of the competence of the notified body concerned.
- Article 31, paragraph 10 (art:31:p10), score 0.811
  - Requirements relating to notified bodies
  - 10. Notified bodies shall be capable of carrying out all their tasks under this Regulation with the highest degree of professional integrity and the requisite competence in the specific field, whether those tasks are carried out by notified bodies themselves or on their behalf and under their responsibility.
- Article 31, paragraph 11 (art:31:p11), score 0.810
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 31, paragraph 6 (art:31:p6), score 0.809
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.

### REQ-046

**Risk level:** Medium

**Requirement:** The system shall allow caregivers to view health summaries and trends.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 112, paragraph 10 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 112, paragraph 10 (art:112:p10), score 0.790
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 7, paragraph 2 (art:7:p2), score 0.788
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 112, paragraph 11 (art:112:p11), score 0.783
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
- Article 112, paragraph 2 (art:112:p2), score 0.782
  - Evaluation and review
  - 2. By 2 August 2028 and every four years thereafter, the Commission shall evaluate and report to the European Parliament and to the Council on the following: (a) the need for amendments extending existing area headings or adding new area headings in Annex III; (b) amendments to the list of AI systems requiring additional transparency measures in Article 50; (c) amendments enhancing the effectiveness of the supervision and governance system.
- Article 9, paragraph 9 (art:9:p9), score 0.781
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.

### REQ-047

**Risk level:** Medium

**Requirement:** The system shall maintain an activity log of caregiver actions for transparency.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 12, paragraph 2 with score 0.814. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 2 (art:12:p2), score 0.814
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 12, paragraph 3 (art:12:p3), score 0.812
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 89, paragraph 1 (art:89:p1), score 0.804
  - Monitoring actions
  - 1. For the purpose of carrying out the tasks assigned to it under this Section, the AI Office may take the necessary actions to monitor the effective implementation and compliance with this Regulation by providers of general-purpose AI models, including their adherence to approved codes of practice.
- Article 50, paragraph 5 (art:50:p5), score 0.800
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 31, paragraph 7 (art:31:p7), score 0.800
  - Requirements relating to notified bodies
  - 7. Notified bodies shall have documented procedures in place ensuring that their personnel, committees, subsidiaries, subcontractors and any associated body or personnel of external bodies maintain, in accordance with Article 78, the confidentiality of the information which comes into their possession during the performance of conformity assessment activities, except when its disclosure is required by law. The staff of notified bodies shall be bound to observe professional secrecy with regard to all information obtained in carrying out their tasks under this Regulation, except in relation to the notifying authorities of the Member State in which their activities are carried out.

### REQ-048

**Risk level:** Medium

**Requirement:** The system shall provide educational content on healthy ageing, fall prevention,

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 9, paragraph 9 with score 0.789. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 9, paragraph 9 (art:9:p9), score 0.789
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
- Article 17, paragraph 2 (art:17:p2), score 0.788
  - Quality management system
  - 2. The implementation of the aspects referred to in paragraph 1 shall be proportionate to the size of the provider’s organisation. Providers shall, in any event, respect the degree of rigour and the level of protection required to ensure the compliance of their high-risk AI systems with this Regulation.
- Article 70, paragraph 3 (art:70:p3), score 0.785
  - Designation of national competent authorities and single points of contact
  - 3. Member States shall ensure that their national competent authorities are provided with adequate technical, financial and human resources, and with infrastructure to fulfil their tasks effectively under this Regulation. In particular, the national competent authorities shall have a sufficient number of personnel permanently available whose competences and expertise shall include an in-depth understanding of AI technologies, data and data computing, personal data protection, cybersecurity, fundamental rights, health and safety risks and knowledge of existing standards and legal requirements. Member States shall assess and, if necessary, update competence and resource requirements referred to in this paragraph on an annual basis.
- Article 1, paragraph 1 (art:1:p1), score 0.784
  - Subject matter`
  - 1. The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter, including democracy, the rule of law and environmental protection, against the harmful effects of AI systems in the Union and supporting innovation.
- Article 7, paragraph 2 (art:7:p2), score 0.782
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-049

**Risk level:** Medium

**Requirement:** The system shall personalise educational content based on user profile and health

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.804. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.804
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 10, paragraph 3 (art:10:p3), score 0.800
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 10, paragraph 4 (art:10:p4), score 0.798
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- Article 10, paragraph 5 (art:10:p5), score 0.795
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 10, paragraph 2 (art:10:p2), score 0.795
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.

### REQ-050

**Risk level:** Medium

**Requirement:** The system shall present educational material in simple language with large text

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 11, paragraph 1 with score 0.789. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 11, paragraph 1 (art:11:p1), score 0.789
  - Technical documentation
  - 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of small and microenterprises. Where an SME, including a start-up, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.
- Article 11, paragraph 2 (art:11:p2), score 0.780
  - Technical documentation
  - 2. Where a high-risk AI system related to a product covered by the Union harmonisation legislation listed in Section A of Annex I is placed on the market or put into service, a single set of technical documentation shall be drawn up containing all the information set out in paragraph 1, as well as the information required under those legal acts.
- Article 31, paragraph 8 (art:31:p8), score 0.776
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 113, paragraph 3 (art:113:p3), score 0.774
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 30, paragraph 3 (art:30:p3), score 0.773
  - Notification procedure
  - 3. The notification referred to in paragraph 2 of this Article shall include full details of the conformity assessment activities, the conformity assessment module or modules, the types of AI systems concerned, and the relevant attestation of competence. Where a notification is not based on an accreditation certificate as referred to in Article 29(2), the notifying authority shall provide the Commission and the other Member States with documentary evidence which attests to the competence of the conformity assessment body and to the arrangements in place to ensure that that body will be monitored regularly and will continue to satisfy the requirements laid down in Article 31.

### REQ-051

**Risk level:** Medium

**Requirement:** The system shall allow users to save helpful articles or videos.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 12, paragraph 1 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 12, paragraph 1 (art:12:p1), score 0.803
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 3 (art:12:p3), score 0.792
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.790
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 91, paragraph 3 (art:91:p3), score 0.790
  - Power to request documentation and information
  - 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
- Article 18, paragraph 3 (art:18:p3), score 0.790
  - Documentation keeping
  - 3. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the technical documentation as part of the documentation kept under the relevant Union financial services law.

### REQ-052

**Risk level:** Medium

**Requirement:** The system shall provide reminders for healthy habits such as hydration, walking,

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 31, paragraph 8 with score 0.791. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 31, paragraph 8 (art:31:p8), score 0.791
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 11 (art:31:p11), score 0.787
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 45, paragraph 3 (art:45:p3), score 0.786
  - Information obligations of notified bodies
  - 3. Each notified body shall provide the other notified bodies carrying out similar conformity assessment activities covering the same types of AI systems with relevant information on issues relating to negative and, on request, positive conformity assessment results.
- Article 31, paragraph 3 (art:31:p3), score 0.785
  - Requirements relating to notified bodies
  - 3. The organisational structure, allocation of responsibilities, reporting lines and operation of notified bodies shall ensure confidence in their performance, and in the results of the conformity assessment activities that the notified bodies conduct.
- Article 31, paragraph 6 (art:31:p6), score 0.785
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.

### REQ-053

**Risk level:** Medium

**Requirement:** The system shall allow users to record mood and emotional wellbeing.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 50, paragraph 3 with score 0.813. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 50, paragraph 3 (art:50:p3), score 0.813
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 12, paragraph 1 (art:12:p1), score 0.806
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 3 (art:12:p3), score 0.801
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.798
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 7, paragraph 2 (art:7:p2), score 0.789
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-054

**Risk level:** Medium

**Requirement:** The system shall detect signs of loneliness, anxiety, or low mood based on user

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 50, paragraph 3 with score 0.812. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 3 (art:50:p3), score 0.812
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 7, paragraph 2 (art:7:p2), score 0.784
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 50, paragraph 1 (art:50:p1), score 0.781
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 27, paragraph 5 (art:27:p5), score 0.780
  - Fundamental rights impact assessment for high-risk AI systems
  - 5. The AI Office shall develop a template for a questionnaire, including through an automated tool, to facilitate deployers in complying with their obligations under this Article in a simplified manner. SECTION 4 Notifying authorities and notified bodies
- Article 28, paragraph 7 (art:28:p7), score 0.778
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.

### REQ-055

**Risk level:** Medium

**Requirement:** The system shall suggest supportive actions such as contacting a friend, doing a

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.799. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.799
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 28, paragraph 1 (art:28:p1), score 0.796
  - Notifying authorities
  - 1. Each Member State shall designate or establish at least one notifying authority responsible for setting up and carrying out the necessary procedures for the assessment, designation and notification of conformity assessment bodies and for their monitoring. Those procedures shall be developed in cooperation between the notifying authorities of all Member States.
- Article 91, paragraph 2 (art:91:p2), score 0.796
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 91, paragraph 5 (art:91:p5), score 0.795
  - Power to request documentation and information
  - 5. The provider of the general-purpose AI model concerned, or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall supply the information requested on behalf of the provider of the general-purpose AI model concerned. Lawyers duly authorised to act may supply information on behalf of their clients. The clients shall nevertheless remain fully responsible if the information supplied is incomplete, incorrect or misleading.
- Article 30, paragraph 5 (art:30:p5), score 0.794
  - Notification procedure
  - 5. Where objections are raised, the Commission shall, without delay, enter into consultations with the relevant Member States and the conformity assessment body. In view thereof, the Commission shall decide whether the authorisation is justified. The Commission shall address its decision to the Member State concerned and to the relevant conformity assessment body.

### REQ-056

**Risk level:** Medium

**Requirement:** The system shall provide access to mental health helplines or support resources.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 69, paragraph 2 with score 0.797. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 69, paragraph 2 (art:69:p2), score 0.797
  - Access to the pool of experts by the Member States
  - 2. The Member States may be required to pay fees for the advice and support provided by the experts. The structure and the level of fees as well as the scale and structure of recoverable costs shall be set out in the implementing act referred to in Article 68(1), taking into account the objectives of the adequate implementation of this Regulation, cost-effectiveness and the necessity of ensuring effective access to experts for all Member States.
- Article 92, paragraph 4 (art:92:p4), score 0.794
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.
- Article 70, paragraph 3 (art:70:p3), score 0.789
  - Designation of national competent authorities and single points of contact
  - 3. Member States shall ensure that their national competent authorities are provided with adequate technical, financial and human resources, and with infrastructure to fulfil their tasks effectively under this Regulation. In particular, the national competent authorities shall have a sufficient number of personnel permanently available whose competences and expertise shall include an in-depth understanding of AI technologies, data and data computing, personal data protection, cybersecurity, fundamental rights, health and safety risks and knowledge of existing standards and legal requirements. Member States shall assess and, if necessary, update competence and resource requirements referred to in this paragraph on an annual basis.
- Article 22, paragraph 2 (art:22:p2), score 0.786
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 50, paragraph 3 (art:50:p3), score 0.785
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-057

**Risk level:** Medium

**Requirement:** The system shall allow caregivers to receive alerts if serious wellbeing concerns

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.835. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.835
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 90, paragraph 3 (art:90:p3), score 0.833
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 73, paragraph 9 (art:73:p9), score 0.826
  - Reporting of serious incidents
  - 9. For high-risk AI systems referred to in Annex III that are placed on the market or put into service by providers that are subject to Union legislative instruments laying down reporting obligations equivalent to those set out in this Regulation, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c).
- Article 73, paragraph 10 (art:73:p10), score 0.823
  - Reporting of serious incidents
  - 10. For high-risk AI systems which are safety components of devices, or are themselves devices, covered by Regulations (EU) 2017/745 and (EU) 2017/746, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c) of this Regulation, and shall be made to the national competent authority chosen for that purpose by the Member States where the incident occurred.
- Article 31, paragraph 11 (art:31:p11), score 0.820
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.

### REQ-058

**Risk level:** Medium

**Requirement:** The system shall generate personalised health reminders based on the user’s age,

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.790
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 9, paragraph 9 (art:9:p9), score 0.789
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
- Article 59, paragraph 1 (art:59:p1), score 0.784
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 36, paragraph 9 (art:36:p9), score 0.782
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 10, paragraph 5 (art:10:p5), score 0.779
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.

### REQ-059

**Risk level:** Medium

**Requirement:** The system shall recommend daily wellness activities suited to the user’s mobility

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.790
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 50, paragraph 3 (art:50:p3), score 0.783
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 34, paragraph 2 (art:34:p2), score 0.782
  - Operational obligations of notified bodies
  - 2. Notified bodies shall avoid unnecessary burdens for providers when performing their activities, and take due account of the size of the provider, the sector in which it operates, its structure and the degree of complexity of the high-risk AI system concerned, in particular in view of minimising administrative burdens and compliance costs for micro- and small enterprises within the meaning of Recommendation 2003/361/EC. The notified body shall, nevertheless, respect the degree of rigour and the level of protection required for the compliance of the high-risk AI system with the requirements of this Regulation.
- Article 31, paragraph 8 (art:31:p8), score 0.780
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 6, paragraph 3 (art:6:p3), score 0.777
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.

### REQ-060

**Risk level:** Medium

**Requirement:** The system shall adapt recommendations based on user feedback and past

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 112, paragraph 10 with score 0.787. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 112, paragraph 10 (art:112:p10), score 0.787
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 63, paragraph 1 (art:63:p1), score 0.775
  - Derogations for specific operators
  - 1. Microenterprises within the meaning of Recommendation 2003/361/EC may comply with certain elements of the quality management system required by Article 17 of this Regulation in a simplified manner, provided that they do not have partner enterprises or linked enterprises within the meaning of that Recommendation. For that purpose, the Commission shall develop guidelines on the elements of the quality management system which may be complied with in a simplified manner considering the needs of microenterprises, without affecting the level of protection or the need for compliance with the requirements in respect of high-risk AI systems.
- Article 112, paragraph 11 (art:112:p11), score 0.774
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
- Article 56, paragraph 8 (art:56:p8), score 0.773
  - Codes of practice
  - 8. The AI Office shall, as appropriate, also encourage and facilitate the review and adaptation of the codes of practice, in particular in light of emerging standards. The AI Office shall assist in the assessment of available standards.
- Article 15, paragraph 4 (art:15:p4), score 0.771
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

### REQ-061

**Risk level:** Medium

**Requirement:** The system shall avoid recommendations that conflict with known medical

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 46, paragraph 2 with score 0.814. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 46, paragraph 2 (art:46:p2), score 0.814
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.
- Article 6, paragraph 3 (art:6:p3), score 0.811
  - Classification rules for high-risk AI systems
  - 3. By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making. The first subparagraph shall apply where any of the following conditions is fulfilled: (a) the AI system is intended to perform a narrow procedural task; (b) the AI system is intended to improve the result of a previously completed human activity; (c) the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review; or (d) the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III. Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.
- Article 80, paragraph 4 (art:80:p4), score 0.810
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 79, paragraph 9 (art:79:p9), score 0.810
  - Procedure at national level for dealing with AI systems presenting a risk
  - 9. The market surveillance authorities shall ensure that appropriate restrictive measures are taken in respect of the product or the AI system concerned, such as withdrawal of the product or the AI system from their market, without undue delay.
- Article 63, paragraph 1 (art:63:p1), score 0.810
  - Derogations for specific operators
  - 1. Microenterprises within the meaning of Recommendation 2003/361/EC may comply with certain elements of the quality management system required by Article 17 of this Regulation in a simplified manner, provided that they do not have partner enterprises or linked enterprises within the meaning of that Recommendation. For that purpose, the Commission shall develop guidelines on the elements of the quality management system which may be complied with in a simplified manner considering the needs of microenterprises, without affecting the level of protection or the need for compliance with the requirements in respect of high-risk AI systems.

### REQ-062

**Risk level:** Medium

**Requirement:** The system shall clearly indicate when recommendations are AI-generated.

**Source:** examples\sample_srs_health_app.pdf, page 3

**Explanation:** Mapped to Article 113, paragraph 2 with score 0.837. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 113, paragraph 2 (art:113:p2), score 0.837
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 50, paragraph 2 (art:50:p2), score 0.831
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 75, paragraph 1 (art:75:p1), score 0.830
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 7, paragraph 2 (art:7:p2), score 0.824
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 14, paragraph 1 (art:14:p1), score 0.821
  - Human oversight
  - 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.

### REQ-063

**Risk level:** Medium

**Requirement:** The system shall send notifications for medication, appointments, hydration,

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 31, paragraph 8 with score 0.839. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 31, paragraph 8 (art:31:p8), score 0.839
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 11 (art:31:p11), score 0.833
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 28, paragraph 7 (art:28:p7), score 0.828
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 31, paragraph 2 (art:31:p2), score 0.826
  - Requirements relating to notified bodies
  - 2. Notified bodies shall satisfy the organisational, quality management, resources and process requirements that are necessary to fulfil their tasks, as well as suitable cybersecurity requirements.
- Article 34, paragraph 3 (art:34:p3), score 0.825
  - Operational obligations of notified bodies
  - 3. Notified bodies shall make available and submit upon request all relevant documentation, including the providers’ documentation, to the notifying authority referred to in Article 28 to allow that authority to conduct its assessment, designation, notification and monitoring activities, and to facilitate the assessment outlined in this Section.

### REQ-064

**Risk level:** Medium

**Requirement:** The system shall allow users to customise notification frequency and style.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 36, paragraph 1 with score 0.809. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 1 (art:36:p1), score 0.809
  - Changes to notifications
  - 1. The notifying authority shall notify the Commission and the other Member States of any relevant changes to the notification of a notified body via the electronic notification tool referred to in Article 30(2).
- Article 28, paragraph 7 (art:28:p7), score 0.806
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 36, paragraph 2 (art:36:p2), score 0.805
  - Changes to notifications
  - 2. The procedures laid down in Articles 29 and 30 shall apply to extensions of the scope of the notification. For changes to the notification other than extensions of its scope, the procedures laid down in paragraphs (3) to (9) shall apply.
- Article 28, paragraph 4 (art:28:p4), score 0.805
  - Notifying authorities
  - 4. Notifying authorities shall be organised in such a way that decisions relating to the notification of conformity assessment bodies are taken by competent persons different from those who carried out the assessment of those bodies.
- Article 36, paragraph 6 (art:36:p6), score 0.804
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.

### REQ-065

**Risk level:** Medium

**Requirement:** The system shall support voice reminders for users with visual difficulties.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.796. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.796
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 28, paragraph 7 (art:28:p7), score 0.782
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 50, paragraph 1 (art:50:p1), score 0.782
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 2 (art:50:p2), score 0.781
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 50, paragraph 3 (art:50:p3), score 0.779
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-066

**Risk level:** Medium

**Requirement:** The system shall repeat critical reminders if no response is received.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 37, paragraph 4 with score 0.808. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 37, paragraph 4 (art:37:p4), score 0.808
  - Challenge to the competence of notified bodies
  - 4. Where the Commission ascertains that a notified body does not meet or no longer meets the requirements for its notification, it shall inform the notifying Member State accordingly and request it to take the necessary corrective measures, including the suspension or withdrawal of the notification if necessary. Where the Member State fails to take the necessary corrective measures, the Commission may, by means of an implementing act, suspend, restrict or withdraw the designation. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 36, paragraph 4 (art:36:p4), score 0.800
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 31, paragraph 6 (art:31:p6), score 0.799
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.
- Article 45, paragraph 2 (art:45:p2), score 0.799
  - Information obligations of notified bodies
  - 2. Each notified body shall inform the other notified bodies of: (a) quality management system approvals which it has refused, suspended or withdrawn, and, upon request, of quality system approvals which it has issued; (b) Union technical documentation assessment certificates or any supplements thereto which it has refused, withdrawn, suspended or otherwise restricted, and, upon request, of the certificates and/or supplements thereto which it has issued.
- Article 37, paragraph 2 (art:37:p2), score 0.797
  - Challenge to the competence of notified bodies
  - 2. The notifying authority shall provide the Commission, on request, with all relevant information relating to the notification or the maintenance of the competence of the notified body concerned.

### REQ-067

**Risk level:** Medium

**Requirement:** The system shall avoid excessive notifications to reduce confusion or alarm.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 36, paragraph 6 with score 0.830. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 6 (art:36:p6), score 0.830
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 36, paragraph 4 (art:36:p4), score 0.827
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 36, paragraph 7 (art:36:p7), score 0.818
  - Changes to notifications
  - 7. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall: (a) assess the impact on the certificates issued by the notified body; (b) submit a report on its findings to the Commission and the other Member States within three months of having notified the changes to the designation; (c) require the notified body to suspend or withdraw, within a reasonable period of time determined by the authority, any certificates which were unduly issued, in order to ensure the continuing conformity of high-risk AI systems on the market; (d) inform the Commission and the Member States about certificates the suspension or withdrawal of which it has required; (e) provide the national competent authorities of the Member State in which the provider has its registered place of business with all relevant information about the certificates of which it has required the suspension or withdrawal; that authority shall take the appropriate measures, where necessary, to avoid a potential risk to health, safety or fundamental rights.
- Article 28, paragraph 7 (art:28:p7), score 0.817
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 34, paragraph 2 (art:34:p2), score 0.815
  - Operational obligations of notified bodies
  - 2. Notified bodies shall avoid unnecessary burdens for providers when performing their activities, and take due account of the size of the provider, the sector in which it operates, its structure and the degree of complexity of the high-risk AI system concerned, in particular in view of minimising administrative burdens and compliance costs for micro- and small enterprises within the meaning of Recommendation 2003/361/EC. The notified body shall, nevertheless, respect the degree of rigour and the level of protection required for the compliance of the high-risk AI system with the requirements of this Regulation.

### REQ-068

**Risk level:** Medium

**Requirement:** The system shall generate daily, weekly, or monthly health summaries.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 112, paragraph 2 with score 0.791. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 112, paragraph 2 (art:112:p2), score 0.791
  - Evaluation and review
  - 2. By 2 August 2028 and every four years thereafter, the Commission shall evaluate and report to the European Parliament and to the Council on the following: (a) the need for amendments extending existing area headings or adding new area headings in Annex III; (b) amendments to the list of AI systems requiring additional transparency measures in Article 50; (c) amendments enhancing the effectiveness of the supervision and governance system.
- Article 7, paragraph 2 (art:7:p2), score 0.787
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 31, paragraph 8 (art:31:p8), score 0.786
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 3 (art:31:p3), score 0.784
  - Requirements relating to notified bodies
  - 3. The organisational structure, allocation of responsibilities, reporting lines and operation of notified bodies shall ensure confidence in their performance, and in the results of the conformity assessment activities that the notified bodies conduct.
- Article 70, paragraph 6 (art:70:p6), score 0.782
  - Designation of national competent authorities and single points of contact
  - 6. By 2 August 2025, and once every two years thereafter, Member States shall report to the Commission on the status of the financial and human resources of the national competent authorities, with an assessment of their adequacy. The Commission shall transmit that information to the Board for discussion and possible recommendations.

### REQ-069

**Risk level:** Medium

**Requirement:** The system shall allow users to export health reports for healthcare appointments.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.811. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.811
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 113, paragraph 3 (art:113:p3), score 0.805
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 57, paragraph 8 (art:57:p8), score 0.800
  - AI regulatory sandboxes
  - 8. Subject to the confidentiality provisions in Article 78, and with the agreement of the provider or prospective provider, the Commission and the Board shall be authorised to access the exit reports and shall take them into account, as appropriate, when exercising their tasks under this Regulation. If both the provider or prospective provider and the national competent authority explicitly agree, the exit report may be made publicly available through the single information platform referred to in this Article.
- Article 31, paragraph 8 (art:31:p8), score 0.789
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 31, paragraph 11 (art:31:p11), score 0.788
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.

### REQ-070

**Risk level:** Medium

**Requirement:** The system shall provide simple explanations of health trends.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.791. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.791
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 52, paragraph 1 (art:52:p1), score 0.789
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 1, paragraph 1 (art:1:p1), score 0.784
  - Subject matter`
  - 1. The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter, including democracy, the rule of law and environmental protection, against the harmful effects of AI systems in the Union and supporting innovation.
- Article 31, paragraph 8 (art:31:p8), score 0.780
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 112, paragraph 10 (art:112:p10), score 0.779
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.

### REQ-071

**Risk level:** Medium

**Requirement:** The system shall allow caregivers and doctors to access reports only with user

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.802. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.802
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 7, paragraph 2 (art:7:p2), score 0.801
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 92, paragraph 4 (art:92:p4), score 0.799
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.
- Article 92, paragraph 5 (art:92:p5), score 0.796
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 57, paragraph 8 (art:57:p8), score 0.796
  - AI regulatory sandboxes
  - 8. Subject to the confidentiality provisions in Article 78, and with the agreement of the provider or prospective provider, the Commission and the Board shall be authorised to access the exit reports and shall take them into account, as appropriate, when exercising their tasks under this Regulation. If both the provider or prospective provider and the national competent authority explicitly agree, the exit report may be made publicly available through the single information platform referred to in this Article.

### REQ-072

**Risk level:** Medium

**Requirement:** The system shall highlight important changes, missed medications, abnormal

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 112, paragraph 10 with score 0.797. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 112, paragraph 10 (art:112:p10), score 0.797
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 52, paragraph 1 (art:52:p1), score 0.795
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 73, paragraph 5 (art:73:p5), score 0.793
  - Reporting of serious incidents
  - 5. Where necessary to ensure timely reporting, the provider or, where applicable, the deployer, may submit an initial report that is incomplete, followed by a complete report.
- Article 72, paragraph 3 (art:72:p3), score 0.791
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 7, paragraph 2 (art:7:p2), score 0.790
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-073

**Risk level:** Medium

**Requirement:** The system shall allow users to provide feedback about app usability and AI

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 27, paragraph 5 with score 0.823. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 27, paragraph 5 (art:27:p5), score 0.823
  - Fundamental rights impact assessment for high-risk AI systems
  - 5. The AI Office shall develop a template for a questionnaire, including through an automated tool, to facilitate deployers in complying with their obligations under this Article in a simplified manner. SECTION 4 Notifying authorities and notified bodies
- Article 113, paragraph 2 (art:113:p2), score 0.817
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 92, paragraph 5 (art:92:p5), score 0.816
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 92, paragraph 7 (art:92:p7), score 0.815
  - Power to conduct evaluations
  - 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.
- Article 112, paragraph 11 (art:112:p11), score 0.809
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.

### REQ-074

**Risk level:** Medium

**Requirement:** The system shall allow users to report incorrect or unsafe AI advice.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 20, paragraph 1 with score 0.861. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 20, paragraph 1 (art:20:p1), score 0.861
  - Corrective actions and duty of information
  - 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.
- Article 73, paragraph 6 (art:73:p6), score 0.852
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 20, paragraph 2 (art:20:p2), score 0.850
  - Corrective actions and duty of information
  - 2. Where the high-risk AI system presents a risk within the meaning of Article 79(1) and the provider becomes aware of that risk, it shall immediately investigate the causes, in collaboration with the reporting deployer, where applicable, and inform the market surveillance authorities competent for the high-risk AI system concerned and, where applicable, the notified body that issued a certificate for that high-risk AI system in accordance with Article 44, in particular, of the nature of the non-compliance and of any relevant corrective action taken.
- Article 15, paragraph 4 (art:15:p4), score 0.849
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- Article 60, paragraph 7 (art:60:p7), score 0.847
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 7. Any serious incident identified in the course of the testing in real world conditions shall be reported to the national market surveillance authority in accordance with Article 73. The provider or prospective provider shall adopt immediate mitigation measures or, failing that, shall suspend the testing in real world conditions until such mitigation takes place, or otherwise terminate it. The provider or prospective provider shall establish a procedure for the prompt recall of the AI system upon such termination of the testing in real world conditions.

### REQ-075

**Risk level:** Medium

**Requirement:** The system shall provide access to technical support.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 71, paragraph 6 with score 0.823. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 71, paragraph 6 (art:71:p6), score 0.823
  - EU database for high-risk AI systems listed in Annex III
  - 6. The Commission shall be the controller of the EU database. It shall make available to providers, prospective providers and deployers adequate technical and administrative support. The EU database shall comply with the applicable accessibility requirements.
- Article 69, paragraph 2 (art:69:p2), score 0.818
  - Access to the pool of experts by the Member States
  - 2. The Member States may be required to pay fees for the advice and support provided by the experts. The structure and the level of fees as well as the scale and structure of recoverable costs shall be set out in the implementing act referred to in Article 68(1), taking into account the objectives of the adequate implementation of this Regulation, cost-effectiveness and the necessity of ensuring effective access to experts for all Member States.
- Article 67, paragraph 1 (art:67:p1), score 0.817
  - Advisory forum
  - 1. An advisory forum shall be established to provide technical expertise and advise the Board and the Commission, and to contribute to their tasks under this Regulation.
- Article 70, paragraph 3 (art:70:p3), score 0.817
  - Designation of national competent authorities and single points of contact
  - 3. Member States shall ensure that their national competent authorities are provided with adequate technical, financial and human resources, and with infrastructure to fulfil their tasks effectively under this Regulation. In particular, the national competent authorities shall have a sufficient number of personnel permanently available whose competences and expertise shall include an in-depth understanding of AI technologies, data and data computing, personal data protection, cybersecurity, fundamental rights, health and safety risks and knowledge of existing standards and legal requirements. Member States shall assess and, if necessary, update competence and resource requirements referred to in this paragraph on an annual basis.
- Article 11, paragraph 1 (art:11:p1), score 0.815
  - Technical documentation
  - 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of small and microenterprises. Where an SME, including a start-up, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.

### REQ-076

**Risk level:** Medium

**Requirement:** The system shall include a help section with step-by-step instructions.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 49, paragraph 3 with score 0.806. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 49, paragraph 3 (art:49:p3), score 0.806
  - Section A — Information to be submitted by providers of high-risk AI systems in accordance with Article 49(1)
  - 3. Where applicable, a detailed description of the system architecture explaining how software components build or feed into each other and integrate into the overall processing. 142/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj ANNEX XII Transparency information referred to in Article 53(1), point (b) — technical documentation for providers of general-purpose AI models to downstream providers that integrate the model into their AI system The information referred to in Article 53(1), point (b) shall contain at least the following:
- Article 91, paragraph 2 (art:91:p2), score 0.804
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 91, paragraph 3 (art:91:p3), score 0.800
  - Power to request documentation and information
  - 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).
- Article 11, paragraph 1 (art:11:p1), score 0.799
  - Technical documentation
  - 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of small and microenterprises. Where an SME, including a start-up, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.
- Article 11, paragraph 2 (art:11:p2), score 0.799
  - Technical documentation
  - 2. Where a high-risk AI system related to a product covered by the Union harmonisation legislation listed in Section A of Annex I is placed on the market or put into service, a single set of technical documentation shall be drawn up containing all the information set out in paragraph 1, as well as the information required under those legal acts.

### REQ-077

**Risk level:** Medium

**Requirement:** The system shall allow users to request human assistance where available.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 92, paragraph 4 with score 0.824. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 92, paragraph 4 (art:92:p4), score 0.824
  - Power to conduct evaluations
  - 4. The request for access shall state the legal basis, the purpose and reasons of the request and set the period within which the access is to be provided, and the fines provided for in Article 101 for failure to provide access.
- Article 28, paragraph 7 (art:28:p7), score 0.819
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 70, paragraph 3 (art:70:p3), score 0.819
  - Designation of national competent authorities and single points of contact
  - 3. Member States shall ensure that their national competent authorities are provided with adequate technical, financial and human resources, and with infrastructure to fulfil their tasks effectively under this Regulation. In particular, the national competent authorities shall have a sufficient number of personnel permanently available whose competences and expertise shall include an in-depth understanding of AI technologies, data and data computing, personal data protection, cybersecurity, fundamental rights, health and safety risks and knowledge of existing standards and legal requirements. Member States shall assess and, if necessary, update competence and resource requirements referred to in this paragraph on an annual basis.
- Article 21, paragraph 2 (art:21:p2), score 0.816
  - Cooperation with competent authorities
  - 2. Upon a reasoned request by a competent authority, providers shall also give the requesting competent authority, as applicable, access to the automatically generated logs of the high-risk AI system referred to in Article 12(1), to the extent such logs are under their control.
- Article 91, paragraph 3 (art:91:p3), score 0.815
  - Power to request documentation and information
  - 3. Upon a duly substantiated request from the scientific panel, the Commission may issue a request for information to a provider of a general-purpose AI model, where the access to information is necessary and proportionate for the fulfilment of the tasks of the scientific panel under Article 68(2).

### REQ-078

**Risk level:** Medium

**Requirement:** The app shall use a simple and intuitive interface suitable for older adults.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.755. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.755
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 29, paragraph 2 (art:29:p2), score 0.752
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.
- Article 7, paragraph 2 (art:7:p2), score 0.751
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 50, paragraph 1 (art:50:p1), score 0.751
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 52, paragraph 1 (art:52:p1), score 0.750
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.

### REQ-079

**Risk level:** Medium

**Requirement:** The app shall minimise the number of steps required to complete common tasks.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 9, paragraph 4 with score 0.779. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 9, paragraph 4 (art:9:p4), score 0.779
  - Risk management system
  - 4. The risk management measures referred to in paragraph 2, point (d), shall give due consideration to the effects and possible interaction resulting from the combined application of the requirements set out in this Section, with a view to minimising risks more effectively while achieving an appropriate balance in implementing the measures to fulfil those requirements.
- Article 52, paragraph 1 (art:52:p1), score 0.770
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 101, paragraph 6 (art:101:p6), score 0.768
  - Fines for providers of general-purpose AI models
  - 6. The Commission shall adopt implementing acts containing detailed arrangements and procedural safeguards for proceedings in view of the possible adoption of decisions pursuant to paragraph 1 of this Article. Those implementing acts shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 62, paragraph 3 (art:62:p3), score 0.763
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 3. The AI Office shall undertake the following actions: (a) provide standardised templates for areas covered by this Regulation, as specified by the Board in its request; (b) develop and maintain a single information platform providing easy to use information in relation to this Regulation for all operators across the Union; 94/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (c) organise appropriate communication campaigns to raise awareness about the obligations arising from this Regulation; (d) evaluate and promote the convergence of best practices in public procurement procedures in relation to AI systems.
- Article 99, paragraph 10 (art:99:p10), score 0.763
  - Penalties
  - 10. The exercise of powers under this Article shall be subject to appropriate procedural safeguards in accordance with Union and national law, including effective judicial remedies and due process.

### REQ-080

**Risk level:** Medium

**Requirement:** The app shall use clear labels, large buttons, and plain language.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 48, paragraph 3 with score 0.769. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 48, paragraph 3 (art:48:p3), score 0.769
  - CE marking
  - 3. The CE marking shall be affixed visibly, legibly and indelibly for high-risk AI systems. Where that is not possible or not warranted on account of the nature of the high-risk AI system, it shall be affixed to the packaging or to the accompanying documentation, as appropriate.
- Article 13, paragraph 2 (art:13:p2), score 0.765
  - Transparency and provision of information to deployers
  - 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- Article 30, paragraph 3 (art:30:p3), score 0.764
  - Notification procedure
  - 3. The notification referred to in paragraph 2 of this Article shall include full details of the conformity assessment activities, the conformity assessment module or modules, the types of AI systems concerned, and the relevant attestation of competence. Where a notification is not based on an accreditation certificate as referred to in Article 29(2), the notifying authority shall provide the Commission and the other Member States with documentary evidence which attests to the competence of the conformity assessment body and to the arrangements in place to ensure that that body will be monitored regularly and will continue to satisfy the requirements laid down in Article 31.
- Article 50, paragraph 2 (art:50:p2), score 0.764
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 29, paragraph 2 (art:29:p2), score 0.762
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.

### REQ-081

**Risk level:** Medium

**Requirement:** The app shall avoid technical medical jargon where possible.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 46, paragraph 2 with score 0.760. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 46, paragraph 2 (art:46:p2), score 0.760
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.
- Article 80, paragraph 4 (art:80:p4), score 0.759
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 80, paragraph 7 (art:80:p7), score 0.757
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 7. Where, in the course of the evaluation pursuant to paragraph 1 of this Article, the market surveillance authority establishes that the AI system was misclassified by the provider as non-high-risk in order to circumvent the application of requirements in Chapter III, Section 2, the provider shall be subject to fines in accordance with Article 99.
- Article 80, paragraph 5 (art:80:p5), score 0.756
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 5. The provider shall ensure that all appropriate corrective action is taken in respect of all the AI systems concerned that it has made available on the Union market.
- Article 83, paragraph 2 (art:83:p2), score 0.754
  - Formal non-compliance
  - 2. Where the non-compliance referred to in paragraph 1 persists, the market surveillance authority of the Member State concerned shall take appropriate and proportionate measures to restrict or prohibit the high-risk AI system being made available on the market or to ensure that it is recalled or withdrawn from the market without delay.

### REQ-082

**Risk level:** Medium

**Requirement:** The app shall provide confirmation messages after important actions, such as

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 30, paragraph 2 with score 0.808. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 30, paragraph 2 (art:30:p2), score 0.808
  - Notification procedure
  - 2. Notifying authorities shall notify the Commission and the other Member States, using the electronic notification tool developed and managed by the Commission, of each conformity assessment body referred to in paragraph 1.
- Article 44, paragraph 3 (art:44:p3), score 0.807
  - Certificates
  - 3. Where a notified body finds that an AI system no longer meets the requirements set out in Section 2, it shall, taking account of the principle of proportionality, suspend or withdraw the certificate issued or impose restrictions on it, unless compliance with those requirements is ensured by appropriate corrective action taken by the provider of the system within an appropriate deadline set by the notified body. The notified body shall give reasons for its decision. An appeal procedure against decisions of the notified bodies, including on conformity certificates issued, shall be available.
- Article 36, paragraph 6 (art:36:p6), score 0.806
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 30, paragraph 1 (art:30:p1), score 0.806
  - Notification procedure
  - 1. Notifying authorities may notify only conformity assessment bodies which have satisfied the requirements laid down in Article 31.
- Article 30, paragraph 3 (art:30:p3), score 0.803
  - Notification procedure
  - 3. The notification referred to in paragraph 2 of this Article shall include full details of the conformity assessment activities, the conformity assessment module or modules, the types of AI systems concerned, and the relevant attestation of competence. Where a notification is not based on an accreditation certificate as referred to in Article 29(2), the notifying authority shall provide the Commission and the other Member States with documentary evidence which attests to the competence of the conformity assessment body and to the arrangements in place to ensure that that body will be monitored regularly and will continue to satisfy the requirements laid down in Article 31.

### REQ-083

**Risk level:** Medium

**Requirement:** The app shall support guided onboarding for first-time users.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 62, paragraph 1 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 62, paragraph 1 (art:62:p1), score 0.790
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 1. Member States shall undertake the following actions: (a) provide SMEs, including start-ups, having a registered office or a branch in the Union, with priority access to the AI regulatory sandboxes, to the extent that they fulfil the eligibility conditions and selection criteria; the priority access shall not preclude other SMEs, including start-ups, other than those referred to in this paragraph from access to the AI regulatory sandbox, provided that they also fulfil the eligibility conditions and selection criteria; (b) organise specific awareness raising and training activities on the application of this Regulation tailored to the needs of SMEs including start-ups, deployers and, as appropriate, local public authorities; (c) utilise existing dedicated channels and where appropriate, establish new ones for communication with SMEs including start-ups, deployers, other innovators and, as appropriate, local public authorities to provide advice and respond to queries about the implementation of this Regulation, including as regards participation in AI regulatory sandboxes; (d) facilitate the participation of SMEs and other relevant stakeholders in the standardisation development process.
- Article 62, paragraph 3 (art:62:p3), score 0.783
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 3. The AI Office shall undertake the following actions: (a) provide standardised templates for areas covered by this Regulation, as specified by the Board in its request; (b) develop and maintain a single information platform providing easy to use information in relation to this Regulation for all operators across the Union; 94/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (c) organise appropriate communication campaigns to raise awareness about the obligations arising from this Regulation; (d) evaluate and promote the convergence of best practices in public procurement procedures in relation to AI systems.
- Article 58, paragraph 3 (art:58:p3), score 0.781
  - Detailed arrangements for, and functioning of, AI regulatory sandboxes
  - 3. Prospective providers in the AI regulatory sandboxes, in particular SMEs and start-ups, shall be directed, where relevant, to pre-deployment services such as guidance on the implementation of this Regulation, to other value-adding services such as help with standardisation documents and certification, testing and experimentation facilities, European Digital Innovation Hubs and centres of excellence. 90/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 62, paragraph 2 (art:62:p2), score 0.775
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 2. The specific interests and needs of the SME providers, including start-ups, shall be taken into account when setting the fees for conformity assessment under Article 43, reducing those fees proportionately to their size, market size and other relevant indicators.
- Article 54, paragraph 1 (art:54:p1), score 0.773
  - Authorised representatives of providers of general-purpose AI models
  - 1. Prior to placing a general-purpose AI model on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.

### REQ-084

**Risk level:** Medium

**Requirement:** The app shall be usable by people with limited digital literacy.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.752. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.752
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 48, paragraph 2 (art:48:p2), score 0.751
  - CE marking
  - 2. For high-risk AI systems provided digitally, a digital CE marking shall be used, only if it can easily be accessed via the interface from which that system is accessed or via an easily accessible machine-readable code or other electronic means.
- Article 92, paragraph 5 (art:92:p5), score 0.748
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 95, paragraph 2 (art:95:p2), score 0.747
  - Codes of conduct for voluntary application of specific requirements
  - 2. The AI Office and the Member States shall facilitate the drawing up of codes of conduct concerning the voluntary application, including by deployers, of specific requirements to all AI systems, on the basis of clear objectives and key performance indicators to measure the achievement of those objectives, including elements such as, but not limited to: (a) applicable elements provided for in Union ethical guidelines for trustworthy AI; (b) assessing and minimising the impact of AI systems on environmental sustainability, including as regards energy-efficient programming and techniques for the efficient design, training and use of AI; (c) promoting AI literacy, in particular that of persons dealing with the development, operation and use of AI; (d) facilitating an inclusive and diverse design of AI systems, including through the establishment of inclusive and diverse development teams and the promotion of stakeholders’ participation in that process; (e) assessing and preventing the negative impact of AI systems on vulnerable persons or groups of vulnerable persons, including as regards accessibility for persons with a disability, as well as on gender equality.
- Article 91, paragraph 5 (art:91:p5), score 0.744
  - Power to request documentation and information
  - 5. The provider of the general-purpose AI model concerned, or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall supply the information requested on behalf of the provider of the general-purpose AI model concerned. Lawyers duly authorised to act may supply information on behalf of their clients. The clients shall nevertheless remain fully responsible if the information supplied is incomplete, incorrect or misleading.

### REQ-085

**Risk level:** Medium

**Requirement:** The app shall comply with recognised accessibility guidelines such as WCAG 2.2

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 29, paragraph 2 with score 0.813. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 29, paragraph 2 (art:29:p2), score 0.813
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.
- Article 8, paragraph 2 (art:8:p2), score 0.812
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 50, paragraph 5 (art:50:p5), score 0.808
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 95, paragraph 2 (art:95:p2), score 0.801
  - Codes of conduct for voluntary application of specific requirements
  - 2. The AI Office and the Member States shall facilitate the drawing up of codes of conduct concerning the voluntary application, including by deployers, of specific requirements to all AI systems, on the basis of clear objectives and key performance indicators to measure the achievement of those objectives, including elements such as, but not limited to: (a) applicable elements provided for in Union ethical guidelines for trustworthy AI; (b) assessing and minimising the impact of AI systems on environmental sustainability, including as regards energy-efficient programming and techniques for the efficient design, training and use of AI; (c) promoting AI literacy, in particular that of persons dealing with the development, operation and use of AI; (d) facilitating an inclusive and diverse design of AI systems, including through the establishment of inclusive and diverse development teams and the promotion of stakeholders’ participation in that process; (e) assessing and preventing the negative impact of AI systems on vulnerable persons or groups of vulnerable persons, including as regards accessibility for persons with a disability, as well as on gender equality.
- Article 40, paragraph 2 (art:40:p2), score 0.794
  - Harmonised standards and standardisation deliverables
  - 2. In accordance with Article 10 of Regulation (EU) No 1025/2012, the Commission shall issue, without undue delay, standardisation requests covering all requirements set out in Section 2 of this Chapter and, as applicable, standardisation requests covering obligations set out in Chapter V, Sections 2 and 3, of this Regulation. The standardisation request shall also ask for deliverables on reporting and documentation processes to improve AI systems’ resource performance, such as reducing the high-risk AI system’s consumption of energy and of other resources during its lifecycle, and on the energy-efficient development of general-purpose AI models. When preparing a standardisation request, the Commission shall consult the Board and relevant stakeholders, including the advisory forum. When issuing a standardisation request to European standardisation organisations, the Commission shall specify that standards have to be clear, consistent, including with the standards developed in the various sectors for products covered by the existing Union harmonisation legislation listed in Annex I, and aiming to ensure that high-risk AI systems or general-purpose AI models placed on the market or put into service in the Union meet the relevant requirements or obligations laid down in this Regulation. The Commission shall request the European standardisation organisations to provide evidence of their best efforts to fulfil the objectives referred to in the first and the second subparagraph of this paragraph in accordance with Article 24 of Regulation (EU) No 1025/2012.

### REQ-086

**Risk level:** Medium

**Requirement:** The app shall support large text sizes.

**Source:** examples\sample_srs_health_app.pdf, page 4

**Explanation:** Mapped to Article 17, paragraph 2 with score 0.767. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 17, paragraph 2 (art:17:p2), score 0.767
  - Quality management system
  - 2. The implementation of the aspects referred to in paragraph 1 shall be proportionate to the size of the provider’s organisation. Providers shall, in any event, respect the degree of rigour and the level of protection required to ensure the compliance of their high-risk AI systems with this Regulation.
- Article 19, paragraph 2 (art:19:p2), score 0.765
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.
- Article 31, paragraph 8 (art:31:p8), score 0.763
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 50, paragraph 2 (art:50:p2), score 0.763
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 10, paragraph 4 (art:10:p4), score 0.762
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.

### REQ-087

**Risk level:** Medium

**Requirement:** The app shall support screen readers.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 29, paragraph 2 with score 0.763. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 29, paragraph 2 (art:29:p2), score 0.763
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.
- Article 113, paragraph 4 (art:113:p4), score 0.762
  - Entry into force and application
  - 4. Control of the technical documentation. 4.1. In addition to the application referred to in point 3, an application with a notified body of their choice shall be lodged by the provider for the assessment of the technical documentation relating to the AI system which the provider intends to place on the market or put into service and which is covered by the quality management system referred to under point 3. 4.2. The application shall include: (a) the name and address of the provider; (b) a written declaration that the same application has not been lodged with any other notified body; (c) the technical documentation referred to in Annex IV. 134/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj 4.3. The technical documentation shall be examined by the notified body. Where relevant, and limited to what is necessary to fulfil its tasks, the notified body shall be granted full access to the training, validation, and testing data sets used, including, where appropriate and subject to security safeguards, through API or other relevant technical means and tools enabling remote access. 4.4. In examining the technical documentation, the notified body may require that the provider supply further evidence or carry out further tests so as to enable a proper assessment of the conformity of the AI system with the requirements set out in Chapter III, Section 2. Where the notified body is not satisfied with the tests carried out by the provider, the notified body shall itself directly carry out adequate tests, as appropriate. 4.5. Where necessary to assess the conformity of the high-risk AI system with the requirements set out in Chapter III, Section 2, after all other reasonable means to verify conformity have been exhausted and have proven to be insufficient, and upon a reasoned request, the notified body shall also be granted access to the training and trained models of the AI system, including its relevant parameters. Such access shall be subject to existing Union law on the protection of intellectual property and trade secrets. 4.6. The decision of the notified body shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the technical documentation and the reasoned assessment decision. Where the AI system is in conformity with the requirements set out in Chapter III, Section 2, the notified body shall issue a Union technical documentation assessment certificate. The certificate shall indicate the name and address of the provider, the conclusions of the examination, the conditions (if any) for its validity and the data necessary for the identification of the AI system. The certificate and its annexes shall contain all relevant information to allow the conformity of the AI system to be evaluated, and to allow for control of the AI system while in use, where applicable. Where the AI system is not in conformity with the requirements set out in Chapter III, Section 2, the notified body shall refuse to issue a Union technical documentation assessment certificate and shall inform the applicant accordingly, giving detailed reasons for its refusal. Where the AI system does not meet the requirement relating to the data used to train it, re-training of the AI system will be needed prior to the application for a new conformity assessment. In this case, the reasoned assessment decision of the notified body refusing to issue the Union technical documentation assessment certificate shall contain specific considerations on the quality data used to train the AI system, in particular on the reasons for non-compliance. 4.7. Any change to the AI system that could affect the compliance of the AI system with the requirements or its intended purpose shall be assessed by the notified body which issued the Union technical documentation assessment certificate. The provider shall inform such notified body of its intention to introduce any of the abovementioned changes, or if it otherwise becomes aware of the occurrence of such changes. The intended changes shall be assessed by the notified body, which shall decide whether those changes require a new conformity assessment in accordance with Article 43(4) or whether they could be addressed by means of a supplement to the Union technical documentation assessment certificate. In the latter case, the notified body shall assess the changes, notify the provider of its decision and, where the changes are approved, issue to the provider a supplement to the Union technical documentation assessment certificate.
- Article 29, paragraph 1 (art:29:p1), score 0.758
  - Application of a conformity assessment body for notification
  - 1. Conformity assessment bodies shall submit an application for notification to the notifying authority of the Member State in which they are established. 70/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 50, paragraph 5 (art:50:p5), score 0.757
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 29, paragraph 4 (art:29:p4), score 0.757
  - Application of a conformity assessment body for notification
  - 4. For notified bodies which are designated under any other Union harmonisation legislation, all documents and certificates linked to those designations may be used to support their designation procedure under this Regulation, as appropriate. The notified body shall update the documentation referred to in paragraphs 2 and 3 of this Article whenever relevant changes occur, in order to enable the authority responsible for notified bodies to monitor and verify continuous compliance with all the requirements laid down in Article 31.

### REQ-088

**Risk level:** Medium

**Requirement:** The app shall provide high contrast display options.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 48, paragraph 3 with score 0.754. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 48, paragraph 3 (art:48:p3), score 0.754
  - CE marking
  - 3. The CE marking shall be affixed visibly, legibly and indelibly for high-risk AI systems. Where that is not possible or not warranted on account of the nature of the high-risk AI system, it shall be affixed to the packaging or to the accompanying documentation, as appropriate.
- Article 13, paragraph 1 (art:13:p1), score 0.753
  - Transparency and provision of information to deployers
  - 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- Article 50, paragraph 2 (art:50:p2), score 0.753
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 11, paragraph 2 (art:11:p2), score 0.753
  - Technical documentation
  - 2. Where a high-risk AI system related to a product covered by the Union harmonisation legislation listed in Section A of Annex I is placed on the market or put into service, a single set of technical documentation shall be drawn up containing all the information set out in paragraph 1, as well as the information required under those legal acts.
- Article 80, paragraph 2 (art:80:p2), score 0.750
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 2. Where, in the course of that evaluation, the market surveillance authority finds that the AI system concerned is high-risk, it shall without undue delay require the relevant provider to take all necessary actions to bring the AI system into compliance with the requirements and obligations laid down in this Regulation, as well as take appropriate corrective action within a period the market surveillance authority may prescribe.

### REQ-089

**Risk level:** Medium

**Requirement:** The app shall support voice input and audio output.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 50, paragraph 2 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 2 (art:50:p2), score 0.790
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 50, paragraph 3 (art:50:p3), score 0.768
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 8, paragraph 2 (art:8:p2), score 0.768
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 50, paragraph 5 (art:50:p5), score 0.768
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 50, paragraph 4 (art:50:p4), score 0.766
  - Transparency obligations for providers and deployers of certain AI systems
  - 4. Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated. This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offence. Where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme, the transparency obligations set out in this paragraph are limited to disclosure of the existence of such generated or manipulated content in an appropriate manner that does not hamper the display or enjoyment of the work. Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated. This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offences or where the AI-generated content has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication of the content. 82/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj

### REQ-090

**Risk level:** Medium

**Requirement:** The app shall avoid relying solely on colour to communicate important information.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.761. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.761
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 10, paragraph 5 (art:10:p5), score 0.759
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 36, paragraph 4 (art:36:p4), score 0.754
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 28, paragraph 6 (art:28:p6), score 0.752
  - Notifying authorities
  - 6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 28, paragraph 5 (art:28:p5), score 0.751
  - Notifying authorities
  - 5. Notifying authorities shall offer or provide neither any activities that conformity assessment bodies perform, nor any consultancy services on a commercial or competitive basis.

### REQ-091

**Risk level:** Medium

**Requirement:** The app shall support users with reduced vision, hearing, dexterity, or cognitive

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.803
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 50, paragraph 1 (art:50:p1), score 0.788
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 95, paragraph 2 (art:95:p2), score 0.784
  - Codes of conduct for voluntary application of specific requirements
  - 2. The AI Office and the Member States shall facilitate the drawing up of codes of conduct concerning the voluntary application, including by deployers, of specific requirements to all AI systems, on the basis of clear objectives and key performance indicators to measure the achievement of those objectives, including elements such as, but not limited to: (a) applicable elements provided for in Union ethical guidelines for trustworthy AI; (b) assessing and minimising the impact of AI systems on environmental sustainability, including as regards energy-efficient programming and techniques for the efficient design, training and use of AI; (c) promoting AI literacy, in particular that of persons dealing with the development, operation and use of AI; (d) facilitating an inclusive and diverse design of AI systems, including through the establishment of inclusive and diverse development teams and the promotion of stakeholders’ participation in that process; (e) assessing and preventing the negative impact of AI systems on vulnerable persons or groups of vulnerable persons, including as regards accessibility for persons with a disability, as well as on gender equality.
- Article 50, paragraph 3 (art:50:p3), score 0.783
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 7, paragraph 2 (art:7:p2), score 0.783
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-092

**Risk level:** Medium

**Requirement:** The app shall allow users to slow down or repeat voice instructions.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 36, paragraph 5 with score 0.773. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 5 (art:36:p5), score 0.773
  - Changes to notifications
  - 5. Where its designation has been suspended, restricted, or fully or partially withdrawn, the notified body shall inform the providers concerned within 10 days.
- Article 112, paragraph 10 (art:112:p10), score 0.769
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 50, paragraph 5 (art:50:p5), score 0.767
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 36, paragraph 7 (art:36:p7), score 0.767
  - Changes to notifications
  - 7. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall: (a) assess the impact on the certificates issued by the notified body; (b) submit a report on its findings to the Commission and the other Member States within three months of having notified the changes to the designation; (c) require the notified body to suspend or withdraw, within a reasonable period of time determined by the authority, any certificates which were unduly issued, in order to ensure the continuing conformity of high-risk AI systems on the market; (d) inform the Commission and the Member States about certificates the suspension or withdrawal of which it has required; (e) provide the national competent authorities of the Member State in which the provider has its registered place of business with all relevant information about the certificates of which it has required the suspension or withdrawal; that authority shall take the appropriate measures, where necessary, to avoid a potential risk to health, safety or fundamental rights.
- Article 36, paragraph 6 (art:36:p6), score 0.763
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.

### REQ-093

**Risk level:** Medium

**Requirement:** The app shall clearly state that AI advice does not replace professional medical

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 2, paragraph 10 with score 0.819. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 2, paragraph 10 (art:2:p10), score 0.819
  - Scope
  - 10. This Regulation does not apply to obligations of deployers who are natural persons using AI systems in the course of a purely personal non-professional activity.
- Article 52, paragraph 2 (art:52:p2), score 0.808
  - Procedure
  - 2. The provider of a general-purpose AI model that meets the condition referred to in Article 51(1), point (a), may present, with its notification, sufficiently substantiated arguments to demonstrate that, exceptionally, although it meets that requirement, the general-purpose AI model does not present, due to its specific characteristics, systemic risks and therefore should not be classified as a general-purpose AI model with systemic risk.
- Article 2, paragraph 6 (art:2:p6), score 0.805
  - Scope
  - 6. This Regulation does not apply to AI systems or AI models, including their output, specifically developed and put into service for the sole purpose of scientific research and development.
- Article 80, paragraph 6 (art:80:p6), score 0.800
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 6. Where the provider of the AI system concerned does not take adequate corrective action within the period referred to in paragraph 2 of this Article, Article 79(5) to (9) shall apply.
- Article 80, paragraph 4 (art:80:p4), score 0.800
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.

### REQ-094

**Risk level:** Medium

**Requirement:** The app shall escalate potentially serious symptoms to emergency or professional

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 73, paragraph 6 with score 0.804. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 73, paragraph 6 (art:73:p6), score 0.804
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 73, paragraph 2 (art:73:p2), score 0.803
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- Article 73, paragraph 4 (art:73:p4), score 0.800
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 73, paragraph 11 (art:73:p11), score 0.793
  - Reporting of serious incidents
  - 11. National competent authorities shall immediately notify the Commission of any serious incident, whether or not they have taken action on it, in accordance with Article 20 of Regulation (EU) 2019/1020. SECTION 3 Enforcement
- Article 73, paragraph 9 (art:73:p9), score 0.792
  - Reporting of serious incidents
  - 9. For high-risk AI systems referred to in Annex III that are placed on the market or put into service by providers that are subject to Union legislative instruments laying down reporting obligations equivalent to those set out in this Regulation, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c).

### REQ-095

**Risk level:** Medium

**Requirement:** The app shall avoid providing unsafe, overconfident, or unsupported medical

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 46, paragraph 2 with score 0.805. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 46, paragraph 2 (art:46:p2), score 0.805
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.
- Article 6, paragraph 4 (art:6:p4), score 0.804
  - Classification rules for high-risk AI systems
  - 4. A provider who considers that an AI system referred to in Annex III is not high-risk shall document its assessment before that system is placed on the market or put into service. Such provider shall be subject to the registration obligation set out in Article 49(2). Upon request of national competent authorities, the provider shall provide the documentation of the assessment.
- Article 80, paragraph 4 (art:80:p4), score 0.804
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 23, paragraph 2 (art:23:p2), score 0.803
  - Obligations of importers
  - 2. Where an importer has sufficient reason to consider that a high-risk AI system is not in conformity with this Regulation, or is falsified, or accompanied by falsified documentation, it shall not place the system on the market until it has been brought into conformity. Where the high-risk AI system presents a risk within the meaning of Article 79(1), the importer shall inform the provider of the system, the authorised representative and the market surveillance authorities to that effect.
- Article 24, paragraph 2 (art:24:p2), score 0.802
  - Obligations of distributors
  - 2. Where a distributor considers or has reason to consider, on the basis of the information in its possession, that a high-risk AI system is not in conformity with the requirements set out in Section 2, it shall not make the high-risk AI system available on the market until the system has been brought into conformity with those requirements. Furthermore, where the high-risk AI system presents a risk within the meaning of Article 79(1), the distributor shall inform the provider or the importer of the system, as applicable, to that effect.

### REQ-096

**Risk level:** Medium

**Requirement:** The app shall include safeguards against hallucinated medical advice.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 80, paragraph 8 with score 0.790. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 80, paragraph 8 (art:80:p8), score 0.790
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 8. In exercising their power to monitor the application of this Article, and in accordance with Article 11 of Regulation (EU) 2019/1020, market surveillance authorities may perform appropriate checks, taking into account in particular information stored in the EU database referred to in Article 71 of this Regulation.
- Article 52, paragraph 6 (art:52:p6), score 0.787
  - Procedure
  - 6. The Commission shall ensure that a list of general-purpose AI models with systemic risk is published and shall keep that list up to date, without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law. SECTION 2 Obligations for providers of general-purpose AI models
- Article 14, paragraph 2 (art:14:p2), score 0.784
  - Human oversight
  - 2. Human oversight shall aim to prevent or minimise the risks to health, safety or fundamental rights that may emerge when a high-risk AI system is used in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, in particular where such risks persist despite the application of other requirements set out in this Section.
- Article 79, paragraph 9 (art:79:p9), score 0.781
  - Procedure at national level for dealing with AI systems presenting a risk
  - 9. The market surveillance authorities shall ensure that appropriate restrictive measures are taken in respect of the product or the AI system concerned, such as withdrawal of the product or the AI system from their market, without undue delay.
- Article 13, paragraph 3 (art:13:p3), score 0.781
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.

### REQ-097

**Risk level:** Medium

**Requirement:** The app shall provide clear emergency instructions when urgent symptoms are

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 90, paragraph 3 with score 0.802. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 90, paragraph 3 (art:90:p3), score 0.802
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 73, paragraph 11 (art:73:p11), score 0.800
  - Reporting of serious incidents
  - 11. National competent authorities shall immediately notify the Commission of any serious incident, whether or not they have taken action on it, in accordance with Article 20 of Regulation (EU) 2019/1020. SECTION 3 Enforcement
- Article 73, paragraph 4 (art:73:p4), score 0.794
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 52, paragraph 1 (art:52:p1), score 0.793
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 73, paragraph 2 (art:73:p2), score 0.790
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.

### REQ-098

**Risk level:** High

**Requirement:** The app shall log AI-generated advice for auditing and safety review.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 12, paragraph 1 with score 0.840. Detected signals: Logging and traceability; Safety, robustness, and risk management. Estimated risk level: High.

**Risk signals:** Logging and traceability, Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 12, paragraph 1 (art:12:p1), score 0.840
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 12, paragraph 2 (art:12:p2), score 0.828
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 19, paragraph 2 (art:19:p2), score 0.826
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.
- Article 19, paragraph 1 (art:19:p1), score 0.821
  - Automatically generated logs
  - 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- Article 89, paragraph 1 (art:89:p1), score 0.818
  - Monitoring actions
  - 1. For the purpose of carrying out the tasks assigned to it under this Section, the AI Office may take the necessary actions to monitor the effective implementation and compliance with this Regulation by providers of general-purpose AI models, including their adherence to approved codes of practice.

### REQ-099

**Risk level:** Medium

**Requirement:** The app shall prioritise user safety over engagement or convenience.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 73, paragraph 6 with score 0.790. Detected signals: Safety, robustness, and risk management. Estimated risk level: Medium.

**Risk signals:** Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 73, paragraph 6 (art:73:p6), score 0.790
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 82, paragraph 4 (art:82:p4), score 0.788
  - Compliant AI systems which present a risk
  - 4. The Commission shall without undue delay enter into consultation with the Member States concerned and the relevant operators, and shall evaluate the national measures taken. On the basis of the results of that evaluation, the Commission shall decide whether the measure is justified and, where necessary, propose other appropriate measures.
- Article 73, paragraph 10 (art:73:p10), score 0.786
  - Reporting of serious incidents
  - 10. For high-risk AI systems which are safety components of devices, or are themselves devices, covered by Regulations (EU) 2017/745 and (EU) 2017/746, the notification of serious incidents shall be limited to those referred to in Article 3, point (49)(c) of this Regulation, and shall be made to the national competent authority chosen for that purpose by the Member States where the incident occurred.
- Article 7, paragraph 2 (art:7:p2), score 0.784
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 28, paragraph 3 (art:28:p3), score 0.784
  - Notifying authorities
  - 3. Notifying authorities shall be established, organised and operated in such a way that no conflict of interest arises with conformity assessment bodies, and that the objectivity and impartiality of their activities are safeguarded.

### REQ-100

**Risk level:** Medium

**Requirement:** The app shall collect only the health data necessary for its intended functions.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 78, paragraph 2 with score 0.773. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 78, paragraph 2 (art:78:p2), score 0.773
  - Confidentiality
  - 2. The authorities involved in the application of this Regulation pursuant to paragraph 1 shall request only data that is strictly necessary for the assessment of the risk posed by AI systems and for the exercise of their powers in accordance with this Regulation and with Regulation (EU) 2019/1020. They shall put in place adequate and effective cybersecurity measures to protect the security and confidentiality of the information and data obtained, and shall delete the data collected as soon as it is no longer needed for the purpose for which it was obtained, in accordance with applicable Union or national law.
- Article 10, paragraph 2 (art:10:p2), score 0.769
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 10, paragraph 5 (art:10:p5), score 0.764
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 59, paragraph 1 (art:59:p1), score 0.764
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 7, paragraph 2 (art:7:p2), score 0.757
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.

### REQ-101

**Risk level:** Medium

**Requirement:** The app shall obtain user consent before collecting, storing, or sharing health

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 13, paragraph 3 with score 0.801. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 13, paragraph 3 (art:13:p3), score 0.801
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- Article 60, paragraph 5 (art:60:p5), score 0.799
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 5. Any subjects of the testing in real world conditions, or their legally designated representative, as appropriate, may, without any resulting detriment and without having to provide any justification, withdraw from the testing at any time by revoking their informed consent and may request the immediate and permanent deletion of their personal data. The withdrawal of the informed consent shall not affect the activities already carried out.
- Article 59, paragraph 1 (art:59:p1), score 0.797
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 28, paragraph 6 (art:28:p6), score 0.797
  - Notifying authorities
  - 6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 21, paragraph 2 (art:21:p2), score 0.797
  - Cooperation with competent authorities
  - 2. Upon a reasoned request by a competent authority, providers shall also give the requesting competent authority, as applicable, access to the automatically generated logs of the high-risk AI system referred to in Article 12(1), to the extent such logs are under their control.

### REQ-102

**Risk level:** Medium

**Requirement:** The app shall allow users to view, edit, export, or delete their personal data.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.818. Detected signals: Data governance and quality. Estimated risk level: Medium.

**Risk signals:** Data governance and quality

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.818
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 59, paragraph 3 (art:59:p3), score 0.813
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 3. Paragraph 1 is without prejudice to Union or national law which excludes processing of personal data for other purposes than those explicitly mentioned in that law, as well as to Union or national law laying down the basis for the processing of personal data which is necessary for the purpose of developing, testing or training of innovative AI systems or any other legal basis, in compliance with Union law on the protection of personal data.
- Article 59, paragraph 2 (art:59:p2), score 0.811
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 2. For the purposes of the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including safeguarding against and preventing threats to public security, under the control and responsibility of law enforcement authorities, the processing of personal data in AI regulatory sandboxes shall be based on a specific Union or national law and subject to the same cumulative conditions as referred to in paragraph 1.
- Article 59, paragraph 1 (art:59:p1), score 0.811
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 2, paragraph 7 (art:2:p7), score 0.808
  - Scope
  - 7. Union law on the protection of personal data, privacy and the confidentiality of communications applies to personal data processed in connection with the rights and obligations laid down in this Regulation. This Regulation shall not affect Regulation (EU) 2016/679 or (EU) 2018/1725, or Directive 2002/58/EC or (EU) 2016/680, without prejudice to Article 10(5) and Article 59 of this Regulation.

### REQ-103

**Risk level:** Medium

**Requirement:** The app shall allow users to control which caregivers or clinicians can access their

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.801. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.801
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 92, paragraph 5 (art:92:p5), score 0.797
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 22, paragraph 2 (art:22:p2), score 0.797
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 74, paragraph 12 (art:74:p12), score 0.797
  - Market surveillance and control of AI systems in the Union market
  - 12. Without prejudice to the powers provided for under Regulation (EU) 2019/1020, and where relevant and limited to what is necessary to fulfil their tasks, the market surveillance authorities shall be granted full access by providers to the documentation as well as the training, validation and testing data sets used for the development of high-risk AI systems, including, where appropriate and subject to security safeguards, through application programming interfaces (API) or other relevant technical means and tools enabling remote access.
- Article 50, paragraph 3 (art:50:p3), score 0.794
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-104

**Risk level:** Medium

**Requirement:** The app shall not share personal health data with third parties without explicit

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.815. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.815
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 59, paragraph 3 (art:59:p3), score 0.809
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 3. Paragraph 1 is without prejudice to Union or national law which excludes processing of personal data for other purposes than those explicitly mentioned in that law, as well as to Union or national law laying down the basis for the processing of personal data which is necessary for the purpose of developing, testing or training of innovative AI systems or any other legal basis, in compliance with Union law on the protection of personal data.
- Article 59, paragraph 1 (art:59:p1), score 0.808
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 78, paragraph 3 (art:78:p3), score 0.805
  - Confidentiality
  - 3. Without prejudice to paragraphs 1 and 2, information exchanged on a confidential basis between the national competent authorities or between national competent authorities and the Commission shall not be disclosed without prior consultation of the originating national competent authority and the deployer when high-risk AI systems referred to in point 1, 6 or 7 of Annex III are used by law enforcement, border control, immigration or asylum authorities and when such disclosure would jeopardise public and national security interests. This exchange of information shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities. When the law enforcement, immigration or asylum authorities are providers of high-risk AI systems referred to in point 1, 6 or 7 of Annex III, the technical documentation referred to in Annex IV shall remain within the premises of those authorities. Those authorities shall ensure that the market surveillance authorities referred to in Article 74(8) and (9), as applicable, can, upon request, immediately access the documentation or obtain a copy thereof. Only staff of the market surveillance authority holding the appropriate level of security clearance shall be allowed to access that documentation or any copy thereof.
- Article 2, paragraph 7 (art:2:p7), score 0.805
  - Scope
  - 7. Union law on the protection of personal data, privacy and the confidentiality of communications applies to personal data processed in connection with the rights and obligations laid down in this Regulation. This Regulation shall not affect Regulation (EU) 2016/679 or (EU) 2018/1725, or Directive 2002/58/EC or (EU) 2016/680, without prejudice to Article 10(5) and Article 59 of this Regulation.

### REQ-105

**Risk level:** Medium

**Requirement:** The app shall anonymise or de-identify data where used for analytics or model

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 78, paragraph 2 with score 0.824. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 78, paragraph 2 (art:78:p2), score 0.824
  - Confidentiality
  - 2. The authorities involved in the application of this Regulation pursuant to paragraph 1 shall request only data that is strictly necessary for the assessment of the risk posed by AI systems and for the exercise of their powers in accordance with this Regulation and with Regulation (EU) 2019/1020. They shall put in place adequate and effective cybersecurity measures to protect the security and confidentiality of the information and data obtained, and shall delete the data collected as soon as it is no longer needed for the purpose for which it was obtained, in accordance with applicable Union or national law.
- Article 10, paragraph 5 (art:10:p5), score 0.822
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 10, paragraph 2 (art:10:p2), score 0.805
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 53, paragraph 7 (art:53:p7), score 0.799
  - Obligations for providers of general-purpose AI models
  - 7. Any information or documentation obtained pursuant to this Article, including trade secrets, shall be treated in accordance with the confidentiality obligations set out in Article 78.
- Article 50, paragraph 3 (art:50:p3), score 0.799
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-106

**Risk level:** Medium

**Requirement:** The app shall clearly explain how user data is used.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.785. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.785
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 50, paragraph 3 (art:50:p3), score 0.778
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 50, paragraph 1 (art:50:p1), score 0.778
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 2 (art:50:p2), score 0.778
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 10, paragraph 3 (art:10:p3), score 0.778
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.

### REQ-107

**Risk level:** Medium

**Requirement:** The app shall encrypt sensitive data in transit and at rest.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 78, paragraph 2 with score 0.788. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 78, paragraph 2 (art:78:p2), score 0.788
  - Confidentiality
  - 2. The authorities involved in the application of this Regulation pursuant to paragraph 1 shall request only data that is strictly necessary for the assessment of the risk posed by AI systems and for the exercise of their powers in accordance with this Regulation and with Regulation (EU) 2019/1020. They shall put in place adequate and effective cybersecurity measures to protect the security and confidentiality of the information and data obtained, and shall delete the data collected as soon as it is no longer needed for the purpose for which it was obtained, in accordance with applicable Union or national law.
- Article 78, paragraph 1 (art:78:p1), score 0.779
  - Confidentiality
  - 1. The Commission, market surveillance authorities and notified bodies and any other natural or legal person involved in the application of this Regulation shall, in accordance with Union or national law, respect the confidentiality of information and data obtained in carrying out their tasks and activities in such a manner as to protect, in particular: (a) the intellectual property rights and confidential business information or trade secrets of a natural or legal person, including source code, except in the cases referred to in Article 5 of Directive (EU) 2016/943 of the European Parliament and of the Council (57); (b) the effective implementation of this Regulation, in particular for the purposes of inspections, investigations or audits; (c) public and national security interests; (d) the conduct of criminal or administrative proceedings; (e) information classified pursuant to Union or national law.
- Article 45, paragraph 4 (art:45:p4), score 0.778
  - Information obligations of notified bodies
  - 4. Notified bodies shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 78, paragraph 3 (art:78:p3), score 0.777
  - Confidentiality
  - 3. Without prejudice to paragraphs 1 and 2, information exchanged on a confidential basis between the national competent authorities or between national competent authorities and the Commission shall not be disclosed without prior consultation of the originating national competent authority and the deployer when high-risk AI systems referred to in point 1, 6 or 7 of Annex III are used by law enforcement, border control, immigration or asylum authorities and when such disclosure would jeopardise public and national security interests. This exchange of information shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities. When the law enforcement, immigration or asylum authorities are providers of high-risk AI systems referred to in point 1, 6 or 7 of Annex III, the technical documentation referred to in Annex IV shall remain within the premises of those authorities. Those authorities shall ensure that the market surveillance authorities referred to in Article 74(8) and (9), as applicable, can, upon request, immediately access the documentation or obtain a copy thereof. Only staff of the market surveillance authority holding the appropriate level of security clearance shall be allowed to access that documentation or any copy thereof.
- Article 10, paragraph 5 (art:10:p5), score 0.775
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.

### REQ-108

**Risk level:** Medium

**Requirement:** The app shall support secure authentication, such as passwords, PINs, biometrics,

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 5, paragraph 5 with score 0.795. Detected signals: Biometric identification or categorisation. Estimated risk level: Medium.

**Risk signals:** Biometric identification or categorisation

**Candidate EU AI Act provisions:**

- Article 5, paragraph 5 (art:5:p5), score 0.795
  - Prohibited AI practices
  - 5. A Member State may decide to provide for the possibility to fully or partially authorise the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement within the limits and under the conditions listed in paragraph 1, first subparagraph, point (h), and paragraphs 2 and 3. Member States concerned shall lay down in their national law the necessary detailed rules for the request, issuance and exercise of, as well as supervision and reporting relating to, the authorisations referred to in paragraph 3. Those rules shall also specify in respect of which of the objectives listed in paragraph 1, first subparagraph, point (h), including which of the criminal offences referred to in point (h)(iii) thereof, the competent authorities may be authorised to use those systems for the purposes of law enforcement. Member States shall notify those rules to the Commission at the latest 30 days following the adoption thereof. Member States may introduce, in accordance with Union law, more restrictive laws on the use of remote biometric identification systems.
- Article 5, paragraph 2 (art:5:p2), score 0.790
  - Prohibited AI practices
  - 2. The use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), shall be deployed for the purposes set out in that point only to confirm the identity of the specifically targeted individual, and it shall take into account the following elements: (a) the nature of the situation giving rise to the possible use, in particular the seriousness, probability and scale of the harm that would be caused if the system were not used; (b) the consequences of the use of the system for the rights and freedoms of all persons concerned, in particular the seriousness, probability and scale of those consequences. In addition, the use of ‘real-time’ remote biometric identification systems in publicly accessible spaces for the purposes of law enforcement for any of the objectives referred to in paragraph 1, first subparagraph, point (h), of this Article shall comply with necessary and proportionate safeguards and conditions in relation to the use in accordance with the national law authorising the use thereof, in particular as regards the temporal, geographic and personal limitations. The use of the ‘real-time’ remote biometric identification system in publicly accessible spaces shall be authorised only if the law enforcement authority has completed a fundamental rights impact assessment as provided for in Article 27 and has registered the system in the EU database according to Article 49. However, in duly justified cases of urgency, the use of such systems may be commenced without the registration in the EU database, provided that such registration is completed without undue delay.
- Article 50, paragraph 3 (art:50:p3), score 0.789
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 5, paragraph 4 (art:5:p4), score 0.786
  - Prohibited AI practices
  - 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- Article 5, paragraph 3 (art:5:p3), score 0.784
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.

### REQ-109

**Risk level:** Medium

**Requirement:** The app shall automatically log users out after a period of inactivity where

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 19, paragraph 1 with score 0.801. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 19, paragraph 1 (art:19:p1), score 0.801
  - Automatically generated logs
  - 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- Article 26, paragraph 6 (art:26:p6), score 0.795
  - Obligations of deployers of high-risk AI systems
  - 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
- Article 19, paragraph 2 (art:19:p2), score 0.794
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.
- Article 12, paragraph 1 (art:12:p1), score 0.779
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 36, paragraph 3 (art:36:p3), score 0.778
  - Changes to notifications
  - 3. Where a notified body decides to cease its conformity assessment activities, it shall inform the notifying authority and the providers concerned as soon as possible and, in the case of a planned cessation, at least one year before ceasing its activities. The certificates of the notified body may remain valid for a period of nine months after cessation of the notified body’s activities, on condition that another notified body has confirmed in writing that it will assume responsibilities for the high-risk AI systems covered by those certificates. The latter notified body shall complete a full assessment of the high-risk AI systems affected by the end of that nine-month-period before issuing new certificates for those systems. Where the notified body has ceased its activity, the notifying authority shall withdraw the designation.

### REQ-110

**Risk level:** Medium

**Requirement:** The app shall protect against unauthorised access to health records.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.793. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.793
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 80, paragraph 8 (art:80:p8), score 0.785
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 8. In exercising their power to monitor the application of this Article, and in accordance with Article 11 of Regulation (EU) 2019/1020, market surveillance authorities may perform appropriate checks, taking into account in particular information stored in the EU database referred to in Article 71 of this Regulation.
- Article 5, paragraph 4 (art:5:p4), score 0.780
  - Prohibited AI practices
  - 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- Article 77, paragraph 1 (art:77:p1), score 0.779
  - Powers of authorities protecting fundamental rights
  - 1. National public authorities or bodies which supervise or enforce the respect of obligations under Union law protecting fundamental rights, including the right to non-discrimination, in relation to the use of high-risk AI systems referred to in Annex III shall have the power to request and access any documentation created or maintained under this Regulation in accessible language and format when access to that documentation is necessary for effectively fulfilling their mandates within the limits of their jurisdiction. The relevant public authority or body shall inform the market surveillance authority of the Member State concerned of any such request.
- Article 77, paragraph 3 (art:77:p3), score 0.777
  - Powers of authorities protecting fundamental rights
  - 3. Where the documentation referred to in paragraph 1 is insufficient to ascertain whether an infringement of obligations under Union law protecting fundamental rights has occurred, the public authority or body referred to in paragraph 1 may make a reasoned request to the market surveillance authority, to organise testing of the high-risk AI system through technical means. The market surveillance authority shall organise the testing with the close involvement of the requesting public authority or body within a reasonable time following the request.

### REQ-111

**Risk level:** Medium

**Requirement:** The app shall maintain audit logs for access to sensitive information.

**Source:** examples\sample_srs_health_app.pdf, page 5

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.819. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.819
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.818
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 12, paragraph 1 (art:12:p1), score 0.799
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 19, paragraph 1 (art:19:p1), score 0.794
  - Automatically generated logs
  - 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- Article 19, paragraph 2 (art:19:p2), score 0.792
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.

### REQ-112

**Risk level:** Medium

**Requirement:** The app shall use role-based access control for older adults, caregivers, clinicians,

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 71, paragraph 6 with score 0.781. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 71, paragraph 6 (art:71:p6), score 0.781
  - EU database for high-risk AI systems listed in Annex III
  - 6. The Commission shall be the controller of the EU database. It shall make available to providers, prospective providers and deployers adequate technical and administrative support. The EU database shall comply with the applicable accessibility requirements.
- Article 22, paragraph 2 (art:22:p2), score 0.776
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 74, paragraph 12 (art:74:p12), score 0.775
  - Market surveillance and control of AI systems in the Union market
  - 12. Without prejudice to the powers provided for under Regulation (EU) 2019/1020, and where relevant and limited to what is necessary to fulfil their tasks, the market surveillance authorities shall be granted full access by providers to the documentation as well as the training, validation and testing data sets used for the development of high-risk AI systems, including, where appropriate and subject to security safeguards, through application programming interfaces (API) or other relevant technical means and tools enabling remote access.
- Article 10, paragraph 5 (art:10:p5), score 0.774
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 59, paragraph 1 (art:59:p1), score 0.774
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.

### REQ-113

**Risk level:** Medium

**Requirement:** The app shall regularly undergo security testing and vulnerability assessments.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 9, paragraph 8 with score 0.798. Detected signals: Safety, robustness, and risk management. Estimated risk level: Medium.

**Risk signals:** Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 9, paragraph 8 (art:9:p8), score 0.798
  - Risk management system
  - 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- Article 9, paragraph 6 (art:9:p6), score 0.788
  - Risk management system
  - 6. High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose and that they are in compliance with the requirements set out in this Section.
- Article 26, paragraph 6 (art:26:p6), score 0.777
  - Obligations of deployers of high-risk AI systems
  - 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
- Article 27, paragraph 5 (art:27:p5), score 0.775
  - Fundamental rights impact assessment for high-risk AI systems
  - 5. The AI Office shall develop a template for a questionnaire, including through an automated tool, to facilitate deployers in complying with their obligations under this Article in a simplified manner. SECTION 4 Notifying authorities and notified bodies
- Article 60, paragraph 6 (art:60:p6), score 0.774
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 6. In accordance with Article 75, Member States shall confer on their market surveillance authorities the powers of requiring providers and prospective providers to provide information, of carrying out unannounced remote or on-site inspections, and of performing checks on the conduct of the testing in real world conditions and the related high-risk AI systems. Market surveillance authorities shall use those powers to ensure the safe development of testing in real world conditions.

### REQ-114

**Risk level:** Medium

**Requirement:** The app shall be available whenever users need to access critical health features.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.784. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.784
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 7, paragraph 2 (art:7:p2), score 0.781
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 36, paragraph 9 (art:36:p9), score 0.778
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 52, paragraph 1 (art:52:p1), score 0.774
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 31, paragraph 11 (art:31:p11), score 0.771
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.

### REQ-115

**Risk level:** Medium

**Requirement:** The app shall continue to provide basic reminders even during temporary network

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 36, paragraph 9 with score 0.779. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 9 (art:36:p9), score 0.779
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 36, paragraph 8 (art:36:p8), score 0.779
  - Changes to notifications
  - 8. With the exception of certificates unduly issued, and where a designation has been suspended or restricted, the certificates shall remain valid in one of the following circumstances: (a) the notifying authority has confirmed, within one month of the suspension or restriction, that there is no risk to health, safety or fundamental rights in relation to certificates affected by the suspension or restriction, and the notifying authority has outlined a timeline for actions to remedy the suspension or restriction; or (b) the notifying authority has confirmed that no certificates relevant to the suspension will be issued, amended or re-issued during the course of the suspension or restriction, and states whether the notified body has the capability of continuing to monitor and remain responsible for existing certificates issued for the period of the suspension or restriction; in the event that the notifying authority determines that the notified body does not have the capability to support existing certificates issued, the provider of the system covered by the certificate shall confirm in writing to the national competent authorities of the Member State in which it has its registered place of business, within three months of the suspension or restriction, that another qualified notified body is temporarily assuming the functions of the notified body to monitor and remain responsible for the certificates during the period of suspension or restriction. 74/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 28, paragraph 7 (art:28:p7), score 0.772
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 31, paragraph 11 (art:31:p11), score 0.769
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 36, paragraph 3 (art:36:p3), score 0.765
  - Changes to notifications
  - 3. Where a notified body decides to cease its conformity assessment activities, it shall inform the notifying authority and the providers concerned as soon as possible and, in the case of a planned cessation, at least one year before ceasing its activities. The certificates of the notified body may remain valid for a period of nine months after cessation of the notified body’s activities, on condition that another notified body has confirmed in writing that it will assume responsibilities for the high-risk AI systems covered by those certificates. The latter notified body shall complete a full assessment of the high-risk AI systems affected by the end of that nine-month-period before issuing new certificates for those systems. Where the notified body has ceased its activity, the notifying authority shall withdraw the designation.

### REQ-116

**Risk level:** Medium

**Requirement:** The app shall recover gracefully from system errors.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 15, paragraph 4 with score 0.773. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 15, paragraph 4 (art:15:p4), score 0.773
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- Article 73, paragraph 4 (art:73:p4), score 0.759
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 73, paragraph 2 (art:73:p2), score 0.759
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.
- Article 73, paragraph 6 (art:73:p6), score 0.758
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.
- Article 73, paragraph 5 (art:73:p5), score 0.756
  - Reporting of serious incidents
  - 5. Where necessary to ensure timely reporting, the provider or, where applicable, the deployer, may submit an initial report that is incomplete, followed by a complete report.

### REQ-117

**Risk level:** Medium

**Requirement:** The app shall prevent data loss during crashes or connectivity interruptions.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 12, paragraph 1 with score 0.792. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 12, paragraph 1 (art:12:p1), score 0.792
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 10, paragraph 2 (art:10:p2), score 0.787
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 12, paragraph 2 (art:12:p2), score 0.785
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 73, paragraph 4 (art:73:p4), score 0.784
  - Reporting of serious incidents
  - 4. Notwithstanding paragraph 2, in the event of the death of a person, the report shall be provided immediately after the provider or the deployer has established, or as soon as it suspects, a causal relationship between the high-risk AI system and the serious incident, but not later than 10 days after the date on which the provider or, where applicable, the deployer becomes aware of the serious incident.
- Article 15, paragraph 4 (art:15:p4), score 0.783
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

### REQ-118

**Risk level:** Medium

**Requirement:** The app shall clearly inform users when a feature is unavailable.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 36, paragraph 4 with score 0.804. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 4 (art:36:p4), score 0.804
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 36, paragraph 5 (art:36:p5), score 0.802
  - Changes to notifications
  - 5. Where its designation has been suspended, restricted, or fully or partially withdrawn, the notified body shall inform the providers concerned within 10 days.
- Article 52, paragraph 1 (art:52:p1), score 0.801
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 36, paragraph 6 (art:36:p6), score 0.800
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 27, paragraph 3 (art:27:p3), score 0.798
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.

### REQ-119

**Risk level:** Medium

**Requirement:** The app shall maintain accurate reminder scheduling across time zones and

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 30, paragraph 2 with score 0.764. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 30, paragraph 2 (art:30:p2), score 0.764
  - Notification procedure
  - 2. Notifying authorities shall notify the Commission and the other Member States, using the electronic notification tool developed and managed by the Commission, of each conformity assessment body referred to in paragraph 1.
- Article 31, paragraph 11 (art:31:p11), score 0.763
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 28, paragraph 1 (art:28:p1), score 0.763
  - Notifying authorities
  - 1. Each Member State shall designate or establish at least one notifying authority responsible for setting up and carrying out the necessary procedures for the assessment, designation and notification of conformity assessment bodies and for their monitoring. Those procedures shall be developed in cooperation between the notifying authorities of all Member States.
- Article 31, paragraph 2 (art:31:p2), score 0.762
  - Requirements relating to notified bodies
  - 2. Notified bodies shall satisfy the organisational, quality management, resources and process requirements that are necessary to fulfil their tasks, as well as suitable cybersecurity requirements.
- Article 31, paragraph 6 (art:31:p6), score 0.760
  - Requirements relating to notified bodies
  - 6. Notified bodies shall be organised and operated so as to safeguard the independence, objectivity and impartiality of their activities. Notified bodies shall document and implement a structure and procedures to safeguard impartiality and to promote and apply the principles of impartiality throughout their organisation, personnel and assessment activities.

### REQ-120

**Risk level:** Medium

**Requirement:** The app shall load key screens within a reasonable time on older smartphones.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.747. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.747
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 5, paragraph 3 (art:5:p3), score 0.731
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 79, paragraph 8 (art:79:p8), score 0.731
  - Procedure at national level for dealing with AI systems presenting a risk
  - 8. Where, within three months of receipt of the notification referred to in paragraph 5 of this Article, no objection has been raised by either a market surveillance authority of a Member State or by the Commission in respect of a provisional measure taken by a market surveillance authority of another Member State, that measure shall be deemed justified. This shall be without prejudice to the procedural rights of the concerned operator in accordance with Article 18 of Regulation (EU) 2019/1020. The three-month period referred to in this paragraph shall be reduced to 30 days in the event of non-compliance with the prohibition of the AI practices referred to in Article 5 of this Regulation.
- Article 99, paragraph 2 (art:99:p2), score 0.728
  - Penalties
  - 2. The Member States shall, without delay and at the latest by the date of entry into application, notify the Commission of the rules on penalties and of other enforcement measures referred to in paragraph 1, and shall notify it, without delay, of any subsequent amendment to them.
- Article 111, paragraph 3 (art:111:p3), score 0.727
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 3. Providers of general-purpose AI models that have been placed on the market before 2 August 2025 shall take the necessary steps in order to comply with the obligations laid down in this Regulation by 2 August 2027. (58) Directive (EU) 2020/1828 of the European Parliament and of the Council of 25 November 2020 on representative actions for the protection of the collective interests of consumers and repealing Directive 2009/22/EC (OJ L 409, 4.12.2020, p. 1).

### REQ-121

**Risk level:** Medium

**Requirement:** The app shall respond quickly to user interactions.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.774. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.774
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 93, paragraph 2 (art:93:p2), score 0.765
  - Power to request measures
  - 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 50, paragraph 5 (art:50:p5), score 0.763
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 91, paragraph 2 (art:91:p2), score 0.761
  - Power to request documentation and information
  - 2. Before sending the request for information, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 50, paragraph 1 (art:50:p1), score 0.759
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

### REQ-122

**Risk level:** Medium

**Requirement:** The AI assistant shall provide responses within an acceptable timeframe.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.837. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.837
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 93, paragraph 2 (art:93:p2), score 0.836
  - Power to request measures
  - 2. Before a measure is requested, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model.
- Article 21, paragraph 1 (art:21:p1), score 0.829
  - Cooperation with competent authorities
  - 1. Providers of high-risk AI systems shall, upon a reasoned request by a competent authority, provide that authority all the information and documentation necessary to demonstrate the conformity of the high-risk AI system with the requirements set out in Section 2, in a language which can be easily understood by the authority in one of the official languages of the institutions of the Union as indicated by the Member State concerned.
- Article 92, paragraph 7 (art:92:p7), score 0.826
  - Power to conduct evaluations
  - 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.
- Article 92, paragraph 5 (art:92:p5), score 0.826
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.

### REQ-123

**Risk level:** Medium

**Requirement:** The app shall minimise battery usage, especially when connected to wearable

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 5, paragraph 4 with score 0.754. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 5, paragraph 4 (art:5:p4), score 0.754
  - Prohibited AI practices
  - 4. Without prejudice to paragraph 3, each use of a ‘real-time’ remote biometric identification system in publicly accessible spaces for law enforcement purposes shall be notified to the relevant market surveillance authority and the national data protection authority in accordance with the national rules referred to in paragraph 5. The notification shall, as a minimum, contain the information specified under paragraph 6 and shall not include sensitive operational data.
- Article 34, paragraph 2 (art:34:p2), score 0.746
  - Operational obligations of notified bodies
  - 2. Notified bodies shall avoid unnecessary burdens for providers when performing their activities, and take due account of the size of the provider, the sector in which it operates, its structure and the degree of complexity of the high-risk AI system concerned, in particular in view of minimising administrative burdens and compliance costs for micro- and small enterprises within the meaning of Recommendation 2003/361/EC. The notified body shall, nevertheless, respect the degree of rigour and the level of protection required for the compliance of the high-risk AI system with the requirements of this Regulation.
- Article 5, paragraph 3 (art:5:p3), score 0.745
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 10, paragraph 5 (art:10:p5), score 0.745
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 79, paragraph 8 (art:79:p8), score 0.740
  - Procedure at national level for dealing with AI systems presenting a risk
  - 8. Where, within three months of receipt of the notification referred to in paragraph 5 of this Article, no objection has been raised by either a market surveillance authority of a Member State or by the Commission in respect of a provisional measure taken by a market surveillance authority of another Member State, that measure shall be deemed justified. This shall be without prejudice to the procedural rights of the concerned operator in accordance with Article 18 of Regulation (EU) 2019/1020. The three-month period referred to in this paragraph shall be reduced to 30 days in the event of non-compliance with the prohibition of the AI practices referred to in Article 5 of this Regulation.

### REQ-124

**Risk level:** Medium

**Requirement:** The app shall operate efficiently on devices with limited processing power or

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 59, paragraph 3 with score 0.773. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 59, paragraph 3 (art:59:p3), score 0.773
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 3. Paragraph 1 is without prejudice to Union or national law which excludes processing of personal data for other purposes than those explicitly mentioned in that law, as well as to Union or national law laying down the basis for the processing of personal data which is necessary for the purpose of developing, testing or training of innovative AI systems or any other legal basis, in compliance with Union law on the protection of personal data.
- Article 5, paragraph 3 (art:5:p3), score 0.768
  - Prohibited AI practices
  - 3. For the purposes of paragraph 1, first subparagraph, point (h) and paragraph 2, each use for the purposes of law enforcement of a ‘real-time’ remote biometric identification system in publicly accessible spaces shall be subject to a prior authorisation granted by a judicial authority or an independent administrative authority whose decision is binding of the Member State in which the use is to take place, issued upon a reasoned request and in accordance with the detailed rules of national law referred to in paragraph 5. However, in a duly justified situation of urgency, the use of such system may be commenced without an authorisation provided that such authorisation is requested without undue delay, at the latest within 24 hours. If such authorisation is rejected, the use shall be stopped with immediate effect and all the data, as well as the results and outputs of that use shall be immediately discarded and deleted. The competent judicial authority or an independent administrative authority whose decision is binding shall grant the authorisation only where it is satisfied, on the basis of objective evidence or clear indications presented to it, that the use of the ‘real-time’ remote biometric identification system concerned is necessary for, and proportionate to, achieving one of the 52/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj objectives specified in paragraph 1, first subparagraph, point (h), as identified in the request and, in particular, remains limited to what is strictly necessary concerning the period of time as well as the geographic and personal scope. In deciding on the request, that authority shall take into account the elements referred to in paragraph 2. No decision that produces an adverse legal effect on a person may be taken based solely on the output of the ‘real-time’ remote biometric identification system.
- Article 10, paragraph 5 (art:10:p5), score 0.767
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 59, paragraph 2 (art:59:p2), score 0.766
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 2. For the purposes of the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including safeguarding against and preventing threats to public security, under the control and responsibility of law enforcement authorities, the processing of personal data in AI regulatory sandboxes shall be based on a specific Union or national law and subject to the same cumulative conditions as referred to in paragraph 1.
- Article 79, paragraph 9 (art:79:p9), score 0.765
  - Procedure at national level for dealing with AI systems presenting a risk
  - 9. The market surveillance authorities shall ensure that appropriate restrictive measures are taken in respect of the product or the AI system concerned, such as withdrawal of the product or the AI system from their market, without undue delay.

### REQ-125

**Risk level:** Medium

**Requirement:** The app shall support offline access to essential information such as medication

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 50, paragraph 5 with score 0.785. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 5 (art:50:p5), score 0.785
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 91, paragraph 5 (art:91:p5), score 0.782
  - Power to request documentation and information
  - 5. The provider of the general-purpose AI model concerned, or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall supply the information requested on behalf of the provider of the general-purpose AI model concerned. Lawyers duly authorised to act may supply information on behalf of their clients. The clients shall nevertheless remain fully responsible if the information supplied is incomplete, incorrect or misleading.
- Article 71, paragraph 4 (art:71:p4), score 0.775
  - EU database for high-risk AI systems listed in Annex III
  - 4. With the exception of the section referred to in Article 49(4) and Article 60(4), point (c), the information contained in the EU database registered in accordance with Article 49 shall be accessible and publicly available in a user-friendly manner. The information should be easily navigable and machine-readable. The information registered in accordance with Article 60 shall be accessible only to market surveillance authorities and the Commission, unless the prospective provider or provider has given consent for also making the information accessible the public.
- Article 75, paragraph 3 (art:75:p3), score 0.775
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 3. Where a market surveillance authority is unable to conclude its investigation of the high-risk AI system because of its inability to access certain information related to the general-purpose AI model despite having made all appropriate efforts to obtain that information, it may submit a reasoned request to the AI Office, by which access to that information shall be enforced. In that case, the AI Office shall supply to the applicant authority without delay, and in any event within 30 days, any information that the AI Office considers to be relevant in order to establish whether a high-risk AI system is non-compliant. Market surveillance authorities shall safeguard the confidentiality of the information that they obtain in accordance with Article 78 of this Regulation. The procedure provided for in Chapter VI of Regulation (EU) 2019/1020 shall apply mutatis mutandis.
- Article 92, paragraph 5 (art:92:p5), score 0.774
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.

### REQ-126

**Risk level:** Medium

**Requirement:** The app shall provide health recommendations based on reliable medical

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 7, paragraph 2 with score 0.791. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 7, paragraph 2 (art:7:p2), score 0.791
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 8, paragraph 2 (art:8:p2), score 0.779
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 13, paragraph 3 (art:13:p3), score 0.777
  - Transparency and provision of information to deployers
  - 3. The instructions for use shall contain at least the following information: (a) the identity and the contact details of the provider and, where applicable, of its authorised representative; (b) the characteristics, capabilities and limitations of performance of the high-risk AI system, including: (i) its intended purpose; (ii) the level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity; (iii) any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2); (iv) where applicable, the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output; (v) when appropriate, its performance regarding specific persons or groups of persons on which the system is intended to be used; (vi) when appropriate, specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the high-risk AI system; (vii) where applicable, information to enable deployers to interpret the output of the high-risk AI system and use it appropriately; (c) the changes to the high-risk AI system and its performance which have been pre-determined by the provider at the moment of the initial conformity assessment, if any; (d) the human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of the high-risk AI systems by the deployers; (e) the computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates; (f) where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs in accordance with Article 12.
- Article 113, paragraph 3 (art:113:p3), score 0.777
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 31, paragraph 11 (art:31:p11), score 0.776
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.

### REQ-127

**Risk level:** Medium

**Requirement:** The app shall distinguish between confirmed user data and AI-inferred information.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.827. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.827
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 57, paragraph 10 (art:57:p10), score 0.827
  - AI regulatory sandboxes
  - 10. National competent authorities shall ensure that, to the extent the innovative AI systems involve the processing of personal data or otherwise fall under the supervisory remit of other national authorities or competent authorities providing or supporting access to data, the national data protection authorities and those other national or competent authorities are associated with the operation of the AI regulatory sandbox and involved in the supervision of those aspects to the extent of their respective tasks and powers.
- Article 50, paragraph 1 (art:50:p1), score 0.825
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 50, paragraph 3 (art:50:p3), score 0.825
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 50, paragraph 2 (art:50:p2), score 0.825
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

### REQ-128

**Risk level:** Medium

**Requirement:** The app shall avoid presenting uncertain AI outputs as facts.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 52, paragraph 3 with score 0.804. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 3 (art:52:p3), score 0.804
  - Procedure
  - 3. Where the Commission concludes that the arguments submitted pursuant to paragraph 2 are not sufficiently substantiated and the relevant provider was not able to demonstrate that the general-purpose AI model does not present, due to its specific characteristics, systemic risks, it shall reject those arguments, and the general-purpose AI model shall be considered to be a general-purpose AI model with systemic risk.
- Article 15, paragraph 4 (art:15:p4), score 0.803
  - Accuracy, robustness and cybersecurity
  - 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- Article 6, paragraph 4 (art:6:p4), score 0.802
  - Classification rules for high-risk AI systems
  - 4. A provider who considers that an AI system referred to in Annex III is not high-risk shall document its assessment before that system is placed on the market or put into service. Such provider shall be subject to the registration obligation set out in Article 49(2). Upon request of national competent authorities, the provider shall provide the documentation of the assessment.
- Article 52, paragraph 2 (art:52:p2), score 0.801
  - Procedure
  - 2. The provider of a general-purpose AI model that meets the condition referred to in Article 51(1), point (a), may present, with its notification, sufficiently substantiated arguments to demonstrate that, exceptionally, although it meets that requirement, the general-purpose AI model does not present, due to its specific characteristics, systemic risks and therefore should not be classified as a general-purpose AI model with systemic risk.
- Article 50, paragraph 2 (art:50:p2), score 0.801
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

### REQ-129

**Risk level:** Medium

**Requirement:** The app shall provide confidence levels or uncertainty indicators where

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 15, paragraph 3 with score 0.800. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 15, paragraph 3 (art:15:p3), score 0.800
  - Accuracy, robustness and cybersecurity
  - 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- Article 30, paragraph 3 (art:30:p3), score 0.796
  - Notification procedure
  - 3. The notification referred to in paragraph 2 of this Article shall include full details of the conformity assessment activities, the conformity assessment module or modules, the types of AI systems concerned, and the relevant attestation of competence. Where a notification is not based on an accreditation certificate as referred to in Article 29(2), the notifying authority shall provide the Commission and the other Member States with documentary evidence which attests to the competence of the conformity assessment body and to the arrangements in place to ensure that that body will be monitored regularly and will continue to satisfy the requirements laid down in Article 31.
- Article 28, paragraph 2 (art:28:p2), score 0.793
  - Notifying authorities
  - 2. Member States may decide that the assessment and monitoring referred to in paragraph 1 is to be carried out by a national accreditation body within the meaning of, and in accordance with, Regulation (EC) No 765/2008.
- Article 60, paragraph 6 (art:60:p6), score 0.793
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 6. In accordance with Article 75, Member States shall confer on their market surveillance authorities the powers of requiring providers and prospective providers to provide information, of carrying out unannounced remote or on-site inspections, and of performing checks on the conduct of the testing in real world conditions and the related high-risk AI systems. Market surveillance authorities shall use those powers to ensure the safe development of testing in real world conditions.
- Article 29, paragraph 2 (art:29:p2), score 0.793
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.

### REQ-130

**Risk level:** Medium

**Requirement:** The app shall regularly update its medical knowledge base.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 96, paragraph 2 with score 0.775. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 96, paragraph 2 (art:96:p2), score 0.775
  - Guidelines from the Commission on the implementation of this Regulation
  - 2. At the request of the Member States or the AI Office, or on its own initiative, the Commission shall update guidelines previously adopted when deemed necessary.
- Article 31, paragraph 11 (art:31:p11), score 0.774
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 36, paragraph 9 (art:36:p9), score 0.771
  - Changes to notifications
  - 9. With the exception of certificates unduly issued, and where a designation has been withdrawn, the certificates shall remain valid for a period of nine months under the following circumstances: (a) the national competent authority of the Member State in which the provider of the high-risk AI system covered by the certificate has its registered place of business has confirmed that there is no risk to health, safety or fundamental rights associated with the high-risk AI systems concerned; and (b) another notified body has confirmed in writing that it will assume immediate responsibility for those AI systems and completes its assessment within 12 months of the withdrawal of the designation. In the circumstances referred to in the first subparagraph, the national competent authority of the Member State in which the provider of the system covered by the certificate has its place of business may extend the provisional validity of the certificates for additional periods of three months, which shall not exceed 12 months in total. The national competent authority or the notified body assuming the functions of the notified body affected by the change of designation shall immediately inform the Commission, the other Member States and the other notified bodies thereof.
- Article 52, paragraph 1 (art:52:p1), score 0.769
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 52, paragraph 6 (art:52:p6), score 0.767
  - Procedure
  - 6. The Commission shall ensure that a list of general-purpose AI models with systemic risk is published and shall keep that list up to date, without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law. SECTION 2 Obligations for providers of general-purpose AI models

### REQ-131

**Risk level:** Medium

**Requirement:** The app shall allow clinical review of high-risk AI outputs.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 9, paragraph 8 with score 0.837. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 9, paragraph 8 (art:9:p8), score 0.837
  - Risk management system
  - 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- Article 60, paragraph 2 (art:60:p2), score 0.834
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 2. Providers or prospective providers may conduct testing of high-risk AI systems referred to in Annex III in real world conditions at any time before the placing on the market or the putting into service of the AI system on their own or in partnership with one or more deployers or prospective deployers.
- Article 9, paragraph 6 (art:9:p6), score 0.832
  - Risk management system
  - 6. High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose and that they are in compliance with the requirements set out in this Section.
- Article 80, paragraph 2 (art:80:p2), score 0.830
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 2. Where, in the course of that evaluation, the market surveillance authority finds that the AI system concerned is high-risk, it shall without undue delay require the relevant provider to take all necessary actions to bring the AI system into compliance with the requirements and obligations laid down in this Regulation, as well as take appropriate corrective action within a period the market surveillance authority may prescribe.
- Article 60, paragraph 3 (art:60:p3), score 0.828
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 3. The testing of high-risk AI systems in real world conditions under this Article shall be without prejudice to any ethical review that is required by Union or national law.

### REQ-132

**Risk level:** Medium

**Requirement:** The app shall correct or remove inaccurate recommendations once identified.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 112, paragraph 10 with score 0.778. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 112, paragraph 10 (art:112:p10), score 0.778
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 20, paragraph 1 (art:20:p1), score 0.778
  - Corrective actions and duty of information
  - 1. Providers of high-risk AI systems which consider or have reason to consider that a high-risk AI system that they have placed on the market or put into service is not in conformity with this Regulation shall immediately take the necessary corrective actions to bring that system into conformity, to withdraw it, to disable it, or to recall it, as appropriate. They shall inform the distributors of the high-risk AI system concerned and, where applicable, the deployers, the authorised representative and importers accordingly.
- Article 10, paragraph 5 (art:10:p5), score 0.774
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 89, paragraph 2 (art:89:p2), score 0.773
  - Monitoring actions
  - 2. Downstream providers shall have the right to lodge a complaint alleging an infringement of this Regulation. A complaint shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model concerned; (b) a description of the relevant facts, the provisions of this Regulation concerned, and the reason why the downstream provider considers that the provider of the general-purpose AI model concerned infringed this Regulation; (c) any other information that the downstream provider that sent the request considers relevant, including, where appropriate, information gathered on its own initiative.
- Article 43, paragraph 4 (art:43:p4), score 0.770
  - Conformity assessment
  - 4. High-risk AI systems that have already been subject to a conformity assessment procedure shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer. For high-risk AI systems that continue to learn after being placed on the market or put into service, changes to the high-risk AI system and its performance that have been pre-determined by the provider at the moment of the initial conformity assessment and are part of the information contained in the technical documentation referred to in point 2(f) of Annex IV, shall not constitute a substantial modification.

### REQ-133

**Risk level:** Medium

**Requirement:** The system shall be designed using modular components.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 8, paragraph 2 with score 0.799. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 8, paragraph 2 (art:8:p2), score 0.799
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 25, paragraph 3 (art:25:p3), score 0.796
  - Responsibilities along the AI value chain
  - 3. In the case of high-risk AI systems that are safety components of products covered by the Union harmonisation legislation listed in Section A of Annex I, the product manufacturer shall be considered to be the provider of the high-risk AI system, and shall be subject to the obligations under Article 16 under either of the following circumstances: (a) the high-risk AI system is placed on the market together with the product under the name or trademark of the product manufacturer; (b) the high-risk AI system is put into service under the name or trademark of the product manufacturer after the product has been placed on the market.
- Article 17, paragraph 2 (art:17:p2), score 0.796
  - Quality management system
  - 2. The implementation of the aspects referred to in paragraph 1 shall be proportionate to the size of the provider’s organisation. Providers shall, in any event, respect the degree of rigour and the level of protection required to ensure the compliance of their high-risk AI systems with this Regulation.
- Article 43, paragraph 3 (art:43:p3), score 0.794
  - Conformity assessment
  - 3. For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I, the provider shall follow the relevant conformity assessment procedure as required under those legal acts. The requirements set out in Section 2 of this Chapter shall apply to those high-risk AI systems and shall be part of that assessment. Points 4.3., 4.4., 4.5. and the fifth paragraph of point 4.6 of Annex VII shall also apply. For the purposes of that assessment, notified bodies which have been notified under those legal acts shall be entitled to control the conformity of the high-risk AI systems with the requirements set out in Section 2, provided that the compliance of those notified bodies with requirements laid down in Article 31(4), (5), (10) and (11) has been assessed in the context of the notification procedure under those legal acts. Where a legal act listed in Section A of Annex I enables the product manufacturer to opt out from a third-party conformity assessment, provided that that manufacturer has applied all harmonised standards covering all the relevant requirements, that manufacturer may use that option only if it has also applied harmonised standards or, where applicable, common specifications referred to in Article 41, covering all requirements set out in Section 2 of this Chapter.
- Article 6, paragraph 1 (art:6:p1), score 0.793
  - Classification rules for high-risk AI systems
  - 1. Irrespective of whether an AI system is placed on the market or put into service independently of the products referred to in points (a) and (b), that AI system shall be considered to be high-risk where both of the following conditions are fulfilled: (a) the AI system is intended to be used as a safety component of a product, or the AI system is itself a product, covered by the Union harmonisation legislation listed in Annex I; (b) the product whose safety component pursuant to point (a) is the AI system, or the AI system itself as a product, is required to undergo a third-party conformity assessment, with a view to the placing on the market or the putting into service of that product pursuant to the Union harmonisation legislation listed in Annex I.

### REQ-134

**Risk level:** Medium

**Requirement:** The system shall allow updates to AI models without disrupting core app functions.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 80, paragraph 4 with score 0.808. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 80, paragraph 4 (art:80:p4), score 0.808
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 111, paragraph 1 (art:111:p1), score 0.808
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 1. Without prejudice to the application of Article 5 as referred to in Article 113(3), point (a), AI systems which are components of the large-scale IT systems established by the legal acts listed in Annex X that have been placed on the market or put into service before 2 August 2027 shall be brought into compliance with this Regulation by 31 December 2030. The requirements laid down in this Regulation shall be taken into account in the evaluation of each large-scale IT system established by the legal acts listed in Annex X to be undertaken as provided for in those legal acts and where those legal acts are replaced or amended.
- Article 80, paragraph 5 (art:80:p5), score 0.807
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 5. The provider shall ensure that all appropriate corrective action is taken in respect of all the AI systems concerned that it has made available on the Union market.
- Article 52, paragraph 6 (art:52:p6), score 0.802
  - Procedure
  - 6. The Commission shall ensure that a list of general-purpose AI models with systemic risk is published and shall keep that list up to date, without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law. SECTION 2 Obligations for providers of general-purpose AI models
- Article 50, paragraph 1 (art:50:p1), score 0.801
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

### REQ-135

**Risk level:** Medium

**Requirement:** The system shall support regular software updates and bug fixes.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 111, paragraph 1 with score 0.779. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 111, paragraph 1 (art:111:p1), score 0.779
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 1. Without prejudice to the application of Article 5 as referred to in Article 113(3), point (a), AI systems which are components of the large-scale IT systems established by the legal acts listed in Annex X that have been placed on the market or put into service before 2 August 2027 shall be brought into compliance with this Regulation by 31 December 2030. The requirements laid down in this Regulation shall be taken into account in the evaluation of each large-scale IT system established by the legal acts listed in Annex X to be undertaken as provided for in those legal acts and where those legal acts are replaced or amended.
- Article 40, paragraph 3 (art:40:p3), score 0.776
  - Harmonised standards and standardisation deliverables
  - 3. The participants in the standardisation process shall seek to promote investment and innovation in AI, including through increasing legal certainty, as well as the competitiveness and growth of the Union market, to contribute to strengthening global cooperation on standardisation and taking into account existing international standards in the field of AI that are consistent with Union values, fundamental rights and interests, and to enhance multi-stakeholder governance ensuring a balanced representation of interests and the effective participation of all relevant stakeholders in accordance with Articles 5, 6, and 7 of Regulation (EU) No 1025/2012.
- Article 113, paragraph 3 (art:113:p3), score 0.776
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 31, paragraph 11 (art:31:p11), score 0.775
  - Requirements relating to notified bodies
  - 11. Notified bodies shall have sufficient internal competences to be able effectively to evaluate the tasks conducted by external parties on their behalf. The notified body shall have permanent availability of sufficient administrative, technical, legal and scientific personnel who possess experience and knowledge relating to the relevant types of AI systems, data and data computing, and relating to the requirements set out in Section 2.
- Article 8, paragraph 2 (art:8:p2), score 0.775
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.

### REQ-136

**Risk level:** Medium

**Requirement:** The system shall maintain clear documentation for developers and administrators.

**Source:** examples\sample_srs_health_app.pdf, page 6

**Explanation:** Mapped to Article 18, paragraph 3 with score 0.832. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 18, paragraph 3 (art:18:p3), score 0.832
  - Documentation keeping
  - 3. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the technical documentation as part of the documentation kept under the relevant Union financial services law.
- Article 18, paragraph 1 (art:18:p1), score 0.831
  - Documentation keeping
  - 1. The provider shall, for a period ending 10 years after the high-risk AI system has been placed on the market or put into service, keep at the disposal of the national competent authorities: (a) the technical documentation referred to in Article 11; (b) the documentation concerning the quality management system referred to in Article 17; (c) the documentation concerning the changes approved by notified bodies, where applicable; (d) the decisions and other documents issued by the notified bodies, where applicable; (e) the EU declaration of conformity referred to in Article 47.
- Article 11, paragraph 1 (art:11:p1), score 0.818
  - Technical documentation
  - 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of small and microenterprises. Where an SME, including a start-up, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.
- Article 18, paragraph 2 (art:18:p2), score 0.815
  - Documentation keeping
  - 2. Each Member State shall determine conditions under which the documentation referred to in paragraph 1 remains at the disposal of the national competent authorities for the period indicated in that paragraph for the cases when a provider or its authorised representative established on its territory goes bankrupt or ceases its activity prior to the end of that period.
- Article 31, paragraph 7 (art:31:p7), score 0.810
  - Requirements relating to notified bodies
  - 7. Notified bodies shall have documented procedures in place ensuring that their personnel, committees, subsidiaries, subcontractors and any associated body or personnel of external bodies maintain, in accordance with Article 78, the confidentiality of the information which comes into their possession during the performance of conformity assessment activities, except when its disclosure is required by law. The staff of notified bodies shall be bound to observe professional secrecy with regard to all information obtained in carrying out their tasks under this Regulation, except in relation to the notifying authorities of the Member State in which their activities are carried out.

### REQ-137

**Risk level:** Medium

**Requirement:** The system shall allow new health monitoring devices or integrations to be added

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 112, paragraph 10 with score 0.816. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 112, paragraph 10 (art:112:p10), score 0.816
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 72, paragraph 3 (art:72:p3), score 0.813
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 3. The post-market monitoring system shall be based on a post-market monitoring plan. The post-market monitoring plan shall be part of the technical documentation referred to in Annex IV. The Commission shall adopt an implementing act laying down detailed provisions establishing a template for the post-market monitoring plan and the list of elements to be included in the plan by 2 February 2026. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 98(2).
- Article 72, paragraph 1 (art:72:p1), score 0.809
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 1. Providers shall establish and document a post-market monitoring system in a manner that is proportionate to the nature of the AI technologies and the risks of the high-risk AI system.
- Article 72, paragraph 4 (art:72:p4), score 0.802
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 4. For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I, where a post-market monitoring system and plan are already established under that legislation, in order to ensure consistency, avoid duplications and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary elements described in paragraphs 1, 2 and 3 using the template referred in paragraph 3 into systems and plans already existing under that legislation, provided that it achieves an equivalent level of protection. The first subparagraph of this paragraph shall also apply to high-risk AI systems referred to in point 5 of Annex III placed on the market or put into service by financial institutions that are subject to requirements under Union financial services law regarding their internal governance, arrangements or processes. SECTION 2 Sharing of information on serious incidents
- Article 111, paragraph 1 (art:111:p1), score 0.800
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 1. Without prejudice to the application of Article 5 as referred to in Article 113(3), point (a), AI systems which are components of the large-scale IT systems established by the legal acts listed in Annex X that have been placed on the market or put into service before 2 August 2027 shall be brought into compliance with this Regulation by 31 December 2030. The requirements laid down in this Regulation shall be taken into account in the evaluation of each large-scale IT system established by the legal acts listed in Annex X to be undertaken as provided for in those legal acts and where those legal acts are replaced or amended.

### REQ-138

**Risk level:** Medium

**Requirement:** The system shall support testing of individual modules such as reminders, AI

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 9, paragraph 8 with score 0.830. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 9, paragraph 8 (art:9:p8), score 0.830
  - Risk management system
  - 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- Article 113, paragraph 2 (art:113:p2), score 0.828
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 84, paragraph 1 (art:84:p1), score 0.827
  - Union AI testing support structures
  - 1. The Commission shall designate one or more Union AI testing support structures to perform the tasks listed under Article 21(6) of Regulation (EU) 2019/1020 in the area of AI.
- Article 27, paragraph 5 (art:27:p5), score 0.827
  - Fundamental rights impact assessment for high-risk AI systems
  - 5. The AI Office shall develop a template for a questionnaire, including through an automated tool, to facilitate deployers in complying with their obligations under this Article in a simplified manner. SECTION 4 Notifying authorities and notified bodies
- Article 9, paragraph 6 (art:9:p6), score 0.821
  - Risk management system
  - 6. High-risk AI systems shall be tested for the purpose of identifying the most appropriate and targeted risk management measures. Testing shall ensure that high-risk AI systems perform consistently for their intended purpose and that they are in compliance with the requirements set out in this Section.

### REQ-139

**Risk level:** Medium

**Requirement:** The system shall support an increasing number of users without major

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.791. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.791
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 80, paragraph 4 (art:80:p4), score 0.788
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 14, paragraph 5 (art:14:p5), score 0.786
  - Human oversight
  - 5. For high-risk AI systems referred to in point 1(a) of Annex III, the measures referred to in paragraph 3 of this Article shall be such as to ensure that, in addition, no action or decision is taken by the deployer on the basis of the identification resulting from the system unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. The requirement for a separate verification by at least two natural persons shall not apply to high-risk AI systems used for the purposes of law enforcement, migration, border control or asylum, where Union or national law considers the application of this requirement to be disproportionate.
- Article 22, paragraph 1 (art:22:p1), score 0.785
  - Authorised representatives of providers of high-risk AI systems
  - 1. Prior to making their high-risk AI systems available on the Union market, providers established in third countries shall, by written mandate, appoint an authorised representative which is established in the Union.
- Article 80, paragraph 5 (art:80:p5), score 0.784
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 5. The provider shall ensure that all appropriate corrective action is taken in respect of all the AI systems concerned that it has made available on the Union market.

### REQ-140

**Risk level:** Medium

**Requirement:** The system shall support scaling of AI services during peak usage.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 22, paragraph 2 with score 0.810. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 22, paragraph 2 (art:22:p2), score 0.810
  - Authorised representatives of providers of high-risk AI systems
  - 2. The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.
- Article 40, paragraph 2 (art:40:p2), score 0.809
  - Harmonised standards and standardisation deliverables
  - 2. In accordance with Article 10 of Regulation (EU) No 1025/2012, the Commission shall issue, without undue delay, standardisation requests covering all requirements set out in Section 2 of this Chapter and, as applicable, standardisation requests covering obligations set out in Chapter V, Sections 2 and 3, of this Regulation. The standardisation request shall also ask for deliverables on reporting and documentation processes to improve AI systems’ resource performance, such as reducing the high-risk AI system’s consumption of energy and of other resources during its lifecycle, and on the energy-efficient development of general-purpose AI models. When preparing a standardisation request, the Commission shall consult the Board and relevant stakeholders, including the advisory forum. When issuing a standardisation request to European standardisation organisations, the Commission shall specify that standards have to be clear, consistent, including with the standards developed in the various sectors for products covered by the existing Union harmonisation legislation listed in Annex I, and aiming to ensure that high-risk AI systems or general-purpose AI models placed on the market or put into service in the Union meet the relevant requirements or obligations laid down in this Regulation. The Commission shall request the European standardisation organisations to provide evidence of their best efforts to fulfil the objectives referred to in the first and the second subparagraph of this paragraph in accordance with Article 24 of Regulation (EU) No 1025/2012.
- Article 12, paragraph 1 (art:12:p1), score 0.809
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 111, paragraph 1 (art:111:p1), score 0.807
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 1. Without prejudice to the application of Article 5 as referred to in Article 113(3), point (a), AI systems which are components of the large-scale IT systems established by the legal acts listed in Annex X that have been placed on the market or put into service before 2 August 2027 shall be brought into compliance with this Regulation by 31 December 2030. The requirements laid down in this Regulation shall be taken into account in the evaluation of each large-scale IT system established by the legal acts listed in Annex X to be undertaken as provided for in those legal acts and where those legal acts are replaced or amended.
- Article 25, paragraph 4 (art:25:p4), score 0.804
  - Responsibilities along the AI value chain
  - 4. The provider of a high-risk AI system and the third party that supplies an AI system, tools, services, components, or processes that are used or integrated in a high-risk AI system shall, by written agreement, specify the necessary information, capabilities, technical access and other assistance based on the generally acknowledged state of the art, in order to enable the provider of the high-risk AI system to fully comply with the obligations set out in this Regulation. This paragraph shall not apply to third parties making accessible to the public tools, services, processes, or components, other than general-purpose AI models, under a free and open-source licence. The AI Office may develop and recommend voluntary model terms for contracts between providers of high-risk AI systems and third parties that supply tools, services, components or processes that are used for or integrated into high-risk AI systems. When developing those voluntary model terms, the AI Office shall take into account possible contractual requirements applicable in specific sectors or business cases. The voluntary model terms shall be published and be available free of charge in an easily usable electronic format.

### REQ-141

**Risk level:** Medium

**Requirement:** The system shall support large volumes of health data from users and connected

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 10, paragraph 4 with score 0.810. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 4 (art:10:p4), score 0.810
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- Article 10, paragraph 2 (art:10:p2), score 0.810
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 71, paragraph 5 (art:71:p5), score 0.802
  - EU database for high-risk AI systems listed in Annex III
  - 5. The EU database shall contain personal data only in so far as necessary for collecting and processing information in accordance with this Regulation. That information shall include the names and contact details of natural persons who are responsible for registering the system and have the legal authority to represent the provider or the deployer, as applicable. 100/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 10, paragraph 3 (art:10:p3), score 0.802
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 71, paragraph 4 (art:71:p4), score 0.799
  - EU database for high-risk AI systems listed in Annex III
  - 4. With the exception of the section referred to in Article 49(4) and Article 60(4), point (c), the information contained in the EU database registered in accordance with Article 49 shall be accessible and publicly available in a user-friendly manner. The information should be easily navigable and machine-readable. The information registered in accordance with Article 60 shall be accessible only to market surveillance authorities and the Commission, unless the prospective provider or provider has given consent for also making the information accessible the public.

### REQ-142

**Risk level:** Medium

**Requirement:** The system shall allow expansion to additional languages, regions, and healthcare

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 7, paragraph 1 with score 0.805. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 7, paragraph 1 (art:7:p1), score 0.805
  - Amendments to Annex III
  - 1. The Commission is empowered to adopt delegated acts in accordance with Article 97 to amend Annex III by adding or modifying use-cases of high-risk AI systems where both of the following conditions are fulfilled: (a) the AI systems are intended to be used in any of the areas listed in Annex III; (b) the AI systems pose a risk of harm to health and safety, or an adverse impact on fundamental rights, and that risk is equivalent to, or greater than, the risk of harm or of adverse impact posed by the high-risk AI systems already referred to in Annex III. 54/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 112, paragraph 2 (art:112:p2), score 0.801
  - Evaluation and review
  - 2. By 2 August 2028 and every four years thereafter, the Commission shall evaluate and report to the European Parliament and to the Council on the following: (a) the need for amendments extending existing area headings or adding new area headings in Annex III; (b) amendments to the list of AI systems requiring additional transparency measures in Article 50; (c) amendments enhancing the effectiveness of the supervision and governance system.
- Article 7, paragraph 2 (art:7:p2), score 0.800
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 112, paragraph 10 (art:112:p10), score 0.798
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 111, paragraph 1 (art:111:p1), score 0.796
  - AI systems already placed on the market or put into service and general-purpose AI models already placed on the
  - 1. Without prejudice to the application of Article 5 as referred to in Article 113(3), point (a), AI systems which are components of the large-scale IT systems established by the legal acts listed in Annex X that have been placed on the market or put into service before 2 August 2027 shall be brought into compliance with this Regulation by 31 December 2030. The requirements laid down in this Regulation shall be taken into account in the evaluation of each large-scale IT system established by the legal acts listed in Annex X to be undertaken as provided for in those legal acts and where those legal acts are replaced or amended.

### REQ-143

**Risk level:** Medium

**Requirement:** The system shall support future integration with hospitals, pharmacies, and

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 17, paragraph 4 with score 0.785. Detected signals: Safety, robustness, and risk management. Estimated risk level: Medium.

**Risk signals:** Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 17, paragraph 4 (art:17:p4), score 0.785
  - Quality management system
  - 4. For providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law, the obligation to put in place a quality management system, with the exception of paragraph 1, points (g), (h) and (i) of this Article, shall be deemed to be fulfilled by complying with the rules on internal governance arrangements or processes pursuant to the relevant Union financial services law. To that end, any harmonised standards referred to in Article 40 shall be taken into account.
- Article 8, paragraph 2 (art:8:p2), score 0.780
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 113, paragraph 3 (art:113:p3), score 0.776
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.
- Article 62, paragraph 3 (art:62:p3), score 0.773
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 3. The AI Office shall undertake the following actions: (a) provide standardised templates for areas covered by this Regulation, as specified by the Board in its request; (b) develop and maintain a single information platform providing easy to use information in relation to this Regulation for all operators across the Union; 94/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj (c) organise appropriate communication campaigns to raise awareness about the obligations arising from this Regulation; (d) evaluate and promote the convergence of best practices in public procurement procedures in relation to AI systems.
- Article 72, paragraph 4 (art:72:p4), score 0.773
  - Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems
  - 4. For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I, where a post-market monitoring system and plan are already established under that legislation, in order to ensure consistency, avoid duplications and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary elements described in paragraphs 1, 2 and 3 using the template referred in paragraph 3 into systems and plans already existing under that legislation, provided that it achieves an equivalent level of protection. The first subparagraph of this paragraph shall also apply to high-risk AI systems referred to in point 5 of Annex III placed on the market or put into service by financial institutions that are subject to requirements under Union financial services law regarding their internal governance, arrangements or processes. SECTION 2 Sharing of information on serious incidents

### REQ-144

**Risk level:** Medium

**Requirement:** The app shall support integration with common wearable devices and health

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 8, paragraph 2 with score 0.783. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 8, paragraph 2 (art:8:p2), score 0.783
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 7, paragraph 2 (art:7:p2), score 0.778
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 10, paragraph 2 (art:10:p2), score 0.777
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 40, paragraph 3 (art:40:p3), score 0.775
  - Harmonised standards and standardisation deliverables
  - 3. The participants in the standardisation process shall seek to promote investment and innovation in AI, including through increasing legal certainty, as well as the competitiveness and growth of the Union market, to contribute to strengthening global cooperation on standardisation and taking into account existing international standards in the field of AI that are consistent with Union values, fundamental rights and interests, and to enhance multi-stakeholder governance ensuring a balanced representation of interests and the effective participation of all relevant stakeholders in accordance with Articles 5, 6, and 7 of Regulation (EU) No 1025/2012.
- Article 112, paragraph 10 (art:112:p10), score 0.774
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.

### REQ-145

**Risk level:** Medium

**Requirement:** The app shall support standard healthcare data formats where applicable.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 10, paragraph 4 with score 0.797. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 4 (art:10:p4), score 0.797
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- Article 10, paragraph 3 (art:10:p3), score 0.794
  - Data and data governance
  - 3. Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They shall have the appropriate statistical properties, including, where applicable, as regards the persons or groups of persons in relation to whom the high-risk AI system is intended to be used. Those characteristics of the data sets may be met at the level of individual data sets or at the level of a combination thereof.
- Article 10, paragraph 2 (art:10:p2), score 0.792
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 8, paragraph 2 (art:8:p2), score 0.791
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 113, paragraph 3 (art:113:p3), score 0.786
  - Entry into force and application
  - 3. Quality management system 3.1. The application of the provider shall include: (a) the name and address of the provider and, if the application is lodged by an authorised representative, also their name and address; (b) the list of AI systems covered under the same quality management system; (c) the technical documentation for each AI system covered under the same quality management system; (d) the documentation concerning the quality management system which shall cover all the aspects listed under Article 17; (e) a description of the procedures in place to ensure that the quality management system remains adequate and effective; (f) a written declaration that the same application has not been lodged with any other notified body. 3.2. The quality management system shall be assessed by the notified body, which shall determine whether it satisfies the requirements referred to in Article 17. The decision shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the quality management system and the reasoned assessment decision. 3.3. The quality management system as approved shall continue to be implemented and maintained by the provider so that it remains adequate and efficient. 3.4. Any intended change to the approved quality management system or the list of AI systems covered by the latter shall be brought to the attention of the notified body by the provider. The proposed changes shall be examined by the notified body, which shall decide whether the modified quality management system continues to satisfy the requirements referred to in point 3.2 or whether a reassessment is necessary. The notified body shall notify the provider of its decision. The notification shall contain the conclusions of the examination of the changes and the reasoned assessment decision.

### REQ-146

**Risk level:** Medium

**Requirement:** The app shall allow health data export in commonly used formats such as PDF or

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 10, paragraph 4 with score 0.774. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 4 (art:10:p4), score 0.774
  - Data and data governance
  - 4. Data sets shall take into account, to the extent required by the intended purpose, the characteristics or elements that are particular to the specific geographical, contextual, behavioural or functional setting within which the high-risk AI system is intended to be used.
- Article 11, paragraph 1 (art:11:p1), score 0.773
  - Technical documentation
  - 1. The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date. The technical documentation shall be drawn up in such a way as to demonstrate that the high-risk AI system complies with the requirements set out in this Section and to provide national competent authorities and notified bodies with the necessary information in a clear and comprehensive form to assess the compliance of the AI system with those requirements. It shall contain, at a minimum, the elements set out in Annex IV. SMEs, including start-ups, may provide the elements of the technical documentation specified in Annex IV in a simplified manner. To that end, the Commission shall establish a simplified technical documentation form targeted at the needs of small and microenterprises. Where an SME, including a start-up, opts to provide the information required in Annex IV in a simplified manner, it shall use the form referred to in this paragraph. Notified bodies shall accept the form for the purposes of the conformity assessment.
- Article 10, paragraph 2 (art:10:p2), score 0.773
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 59, paragraph 1 (art:59:p1), score 0.773
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 8, paragraph 2 (art:8:p2), score 0.771
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.

### REQ-147

**Risk level:** Medium

**Requirement:** The app shall support integration with telehealth platforms.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 56, paragraph 3 with score 0.765. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 56, paragraph 3 (art:56:p3), score 0.765
  - Codes of practice
  - 3. The AI Office may invite all providers of general-purpose AI models, as well as relevant national competent authorities, to participate in the drawing-up of codes of practice. Civil society organisations, industry, academia and other relevant stakeholders, such as downstream providers and independent experts, may support the process.
- Article 8, paragraph 2 (art:8:p2), score 0.763
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 40, paragraph 3 (art:40:p3), score 0.761
  - Harmonised standards and standardisation deliverables
  - 3. The participants in the standardisation process shall seek to promote investment and innovation in AI, including through increasing legal certainty, as well as the competitiveness and growth of the Union market, to contribute to strengthening global cooperation on standardisation and taking into account existing international standards in the field of AI that are consistent with Union values, fundamental rights and interests, and to enhance multi-stakeholder governance ensuring a balanced representation of interests and the effective participation of all relevant stakeholders in accordance with Articles 5, 6, and 7 of Regulation (EU) No 1025/2012.
- Article 62, paragraph 1 (art:62:p1), score 0.758
  - Measures for providers and deployers, in particular SMEs, including start-ups
  - 1. Member States shall undertake the following actions: (a) provide SMEs, including start-ups, having a registered office or a branch in the Union, with priority access to the AI regulatory sandboxes, to the extent that they fulfil the eligibility conditions and selection criteria; the priority access shall not preclude other SMEs, including start-ups, other than those referred to in this paragraph from access to the AI regulatory sandbox, provided that they also fulfil the eligibility conditions and selection criteria; (b) organise specific awareness raising and training activities on the application of this Regulation tailored to the needs of SMEs including start-ups, deployers and, as appropriate, local public authorities; (c) utilise existing dedicated channels and where appropriate, establish new ones for communication with SMEs including start-ups, deployers, other innovators and, as appropriate, local public authorities to provide advice and respond to queries about the implementation of this Regulation, including as regards participation in AI regulatory sandboxes; (d) facilitate the participation of SMEs and other relevant stakeholders in the standardisation development process.
- Article 25, paragraph 4 (art:25:p4), score 0.756
  - Responsibilities along the AI value chain
  - 4. The provider of a high-risk AI system and the third party that supplies an AI system, tools, services, components, or processes that are used or integrated in a high-risk AI system shall, by written agreement, specify the necessary information, capabilities, technical access and other assistance based on the generally acknowledged state of the art, in order to enable the provider of the high-risk AI system to fully comply with the obligations set out in this Regulation. This paragraph shall not apply to third parties making accessible to the public tools, services, processes, or components, other than general-purpose AI models, under a free and open-source licence. The AI Office may develop and recommend voluntary model terms for contracts between providers of high-risk AI systems and third parties that supply tools, services, components or processes that are used for or integrated into high-risk AI systems. When developing those voluntary model terms, the AI Office shall take into account possible contractual requirements applicable in specific sectors or business cases. The voluntary model terms shall be published and be available free of charge in an easily usable electronic format.

### REQ-148

**Risk level:** Medium

**Requirement:** The app shall support future integration with electronic health record systems,

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 12, paragraph 1 with score 0.764. Detected signals: Logging and traceability. Estimated risk level: Medium.

**Risk signals:** Logging and traceability

**Candidate EU AI Act provisions:**

- Article 12, paragraph 1 (art:12:p1), score 0.764
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 8, paragraph 2 (art:8:p2), score 0.761
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 10, paragraph 2 (art:10:p2), score 0.760
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 59, paragraph 1 (art:59:p1), score 0.758
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 12, paragraph 3 (art:12:p3), score 0.758
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).

### REQ-149

**Risk level:** Medium

**Requirement:** The app shall avoid ageist assumptions in its design and recommendations.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 80, paragraph 4 with score 0.779. Detected signals: Automated decision-making. Estimated risk level: Medium.

**Risk signals:** Automated decision-making

**Candidate EU AI Act provisions:**

- Article 80, paragraph 4 (art:80:p4), score 0.779
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 80, paragraph 5 (art:80:p5), score 0.777
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 5. The provider shall ensure that all appropriate corrective action is taken in respect of all the AI systems concerned that it has made available on the Union market.
- Article 80, paragraph 8 (art:80:p8), score 0.774
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 8. In exercising their power to monitor the application of this Article, and in accordance with Article 11 of Regulation (EU) 2019/1020, market surveillance authorities may perform appropriate checks, taking into account in particular information stored in the EU database referred to in Article 71 of this Regulation.
- Article 9, paragraph 9 (art:9:p9), score 0.771
  - Risk management system
  - 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.
- Article 80, paragraph 3 (art:80:p3), score 0.771
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 3. Where the market surveillance authority considers that the use of the AI system concerned is not restricted to its national territory, it shall inform the Commission and the other Member States without undue delay of the results of the evaluation and of the actions which it has required the provider to take.

### REQ-150

**Risk level:** Medium

**Requirement:** The app shall respect user autonomy and allow older adults to make their own

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.780. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.780
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 21, paragraph 2 (art:21:p2), score 0.773
  - Cooperation with competent authorities
  - 2. Upon a reasoned request by a competent authority, providers shall also give the requesting competent authority, as applicable, access to the automatically generated logs of the high-risk AI system referred to in Article 12(1), to the extent such logs are under their control.
- Article 59, paragraph 1 (art:59:p1), score 0.773
  - Further processing of personal data for developing certain AI systems in the public interest in the AI regulatory
  - 1. In the AI regulatory sandbox, personal data lawfully collected for other purposes may be processed solely for the purpose of developing, training and testing certain AI systems in the sandbox when all of the following conditions are met: (a) AI systems shall be developed for safeguarding substantial public interest by a public authority or another natural or legal person and in one or more of the following areas: (i) public safety and public health, including disease detection, diagnosis prevention, control and treatment and improvement of health care systems; (ii) a high level of protection and improvement of the quality of the environment, protection of biodiversity, protection against pollution, green transition measures, climate change mitigation and adaptation measures; (iii) energy sustainability; (iv) safety and resilience of transport systems and mobility, critical infrastructure and networks; (v) efficiency and quality of public administration and public services; (b) the data processed are necessary for complying with one or more of the requirements referred to in Chapter III, Section 2 where those requirements cannot effectively be fulfilled by processing anonymised, synthetic or other non-personal data; (c) there are effective monitoring mechanisms to identify if any high risks to the rights and freedoms of the data subjects, as referred to in Article 35 of Regulation (EU) 2016/679 and in Article 39 of Regulation (EU) 2018/1725, may arise during the sandbox experimentation, as well as response mechanisms to promptly mitigate those risks and, where necessary, stop the processing; (d) any personal data to be processed in the context of the sandbox are in a functionally separate, isolated and protected data processing environment under the control of the prospective provider and only authorised persons have access to those data; (e) providers can further share the originally collected data only in accordance with Union data protection law; any personal data created in the sandbox cannot be shared outside the sandbox; (f) any processing of personal data in the context of the sandbox neither leads to measures or decisions affecting the data subjects nor does it affect the application of their rights laid down in Union law on the protection of personal data; (g) any personal data processed in the context of the sandbox are protected by means of appropriate technical and organisational measures and deleted once the participation in the sandbox has terminated or the personal data has reached the end of its retention period; (h) the logs of the processing of personal data in the context of the sandbox are kept for the duration of the participation in the sandbox, unless provided otherwise by Union or national law; (i) a complete and detailed description of the process and rationale behind the training, testing and validation of the AI system is kept together with the testing results as part of the technical documentation referred to in Annex IV; (j) a short summary of the AI project developed in the sandbox, its objectives and expected results is published on the website of the competent authorities; this obligation shall not cover sensitive operational data in relation to the activities of law enforcement, border control, immigration or asylum authorities.
- Article 50, paragraph 5 (art:50:p5), score 0.772
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 57, paragraph 7 (art:57:p7), score 0.772
  - AI regulatory sandboxes
  - 7. Competent authorities shall provide providers and prospective providers participating in the AI regulatory sandbox with guidance on regulatory expectations and how to fulfil the requirements and obligations set out in this Regulation. Upon request of the provider or prospective provider of the AI system, the competent authority shall provide a written proof of the activities successfully carried out in the sandbox. The competent authority shall also provide an exit report detailing the activities carried out in the sandbox and the related results and learning outcomes. Providers may use such documentation to demonstrate their compliance with this Regulation through the conformity assessment process or relevant market surveillance activities. In this regard, the exit reports and the written proof provided by the national competent authority shall be taken positively into account by market surveillance authorities and notified bodies, with a view to accelerating conformity assessment procedures to a reasonable extent.

### REQ-151

**Risk level:** Medium

**Requirement:** The app shall clearly distinguish between AI advice and human clinical advice.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 75, paragraph 1 with score 0.798. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 75, paragraph 1 (art:75:p1), score 0.798
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 14, paragraph 1 (art:14:p1), score 0.796
  - Human oversight
  - 1. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use.
- Article 50, paragraph 1 (art:50:p1), score 0.794
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 7, paragraph 2 (art:7:p2), score 0.794
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 113, paragraph 2 (art:113:p2), score 0.793
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.

### REQ-152

**Risk level:** Medium

**Requirement:** The app shall avoid manipulating users into unnecessary engagement.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.777. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.777
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 80, paragraph 4 (art:80:p4), score 0.775
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.
- Article 89, paragraph 2 (art:89:p2), score 0.773
  - Monitoring actions
  - 2. Downstream providers shall have the right to lodge a complaint alleging an infringement of this Regulation. A complaint shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model concerned; (b) a description of the relevant facts, the provisions of this Regulation concerned, and the reason why the downstream provider considers that the provider of the general-purpose AI model concerned infringed this Regulation; (c) any other information that the downstream provider that sent the request considers relevant, including, where appropriate, information gathered on its own initiative.
- Article 46, paragraph 2 (art:46:p2), score 0.772
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.
- Article 80, paragraph 3 (art:80:p3), score 0.771
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 3. Where the market surveillance authority considers that the use of the AI system concerned is not restricted to its national territory, it shall inform the Commission and the other Member States without undue delay of the results of the evaluation and of the actions which it has required the provider to take.

### REQ-153

**Risk level:** Medium

**Requirement:** The app shall be designed to support independence, not replace human care.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 2, paragraph 10 with score 0.766. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 2, paragraph 10 (art:2:p10), score 0.766
  - Scope
  - 10. This Regulation does not apply to obligations of deployers who are natural persons using AI systems in the course of a purely personal non-professional activity.
- Article 80, paragraph 5 (art:80:p5), score 0.756
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 5. The provider shall ensure that all appropriate corrective action is taken in respect of all the AI systems concerned that it has made available on the Union market.
- Article 2, paragraph 11 (art:2:p11), score 0.753
  - Scope
  - 11. This Regulation does not preclude the Union or Member States from maintaining or introducing laws, regulations or administrative provisions which are more favourable to workers in terms of protecting their rights in respect of the use of AI systems by employers, or from encouraging or allowing the application of collective agreements which are more favourable to workers.
- Article 1, paragraph 1 (art:1:p1), score 0.753
  - Subject matter`
  - 1. The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter, including democracy, the rule of law and environmental protection, against the harmful effects of AI systems in the Union and supporting innovation.
- Article 95, paragraph 2 (art:95:p2), score 0.753
  - Codes of conduct for voluntary application of specific requirements
  - 2. The AI Office and the Member States shall facilitate the drawing up of codes of conduct concerning the voluntary application, including by deployers, of specific requirements to all AI systems, on the basis of clear objectives and key performance indicators to measure the achievement of those objectives, including elements such as, but not limited to: (a) applicable elements provided for in Union ethical guidelines for trustworthy AI; (b) assessing and minimising the impact of AI systems on environmental sustainability, including as regards energy-efficient programming and techniques for the efficient design, training and use of AI; (c) promoting AI literacy, in particular that of persons dealing with the development, operation and use of AI; (d) facilitating an inclusive and diverse design of AI systems, including through the establishment of inclusive and diverse development teams and the promotion of stakeholders’ participation in that process; (e) assessing and preventing the negative impact of AI systems on vulnerable persons or groups of vulnerable persons, including as regards accessibility for persons with a disability, as well as on gender equality.

### REQ-154

**Risk level:** Medium

**Requirement:** The app shall provide transparency about how AI decisions are made.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 50, paragraph 2 with score 0.842. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 2 (art:50:p2), score 0.842
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 50, paragraph 5 (art:50:p5), score 0.840
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 50, paragraph 1 (art:50:p1), score 0.840
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 13, paragraph 1 (art:13:p1), score 0.832
  - Transparency and provision of information to deployers
  - 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- Article 50, paragraph 7 (art:50:p7), score 0.829
  - Transparency obligations for providers and deployers of certain AI systems
  - 7. The AI Office shall encourage and facilitate the drawing up of codes of practice at Union level to facilitate the effective implementation of the obligations regarding the detection and labelling of artificially generated or manipulated content. The Commission may adopt implementing acts to approve those codes of practice in accordance with the procedure laid down in Article 56 (6). If it deems the code is not adequate, the Commission may adopt an implementing act specifying common rules for the implementation of those obligations in accordance with the examination procedure laid down in Article 98(2).

### REQ-155

**Risk level:** High

**Requirement:** The app shall include processes for reviewing bias in AI recommendations.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 113, paragraph 2 with score 0.820. Detected signals: Automated decision-making; Data governance and quality. Estimated risk level: High.

**Risk signals:** Automated decision-making, Data governance and quality

**Candidate EU AI Act provisions:**

- Article 113, paragraph 2 (art:113:p2), score 0.820
  - Entry into force and application
  - 2. Overview The approved quality management system for the design, development and testing of AI systems pursuant to Article 17 shall be examined in accordance with point 3 and shall be subject to surveillance as specified in point 5. The technical documentation of the AI system shall be examined in accordance with point 4.
- Article 112, paragraph 10 (art:112:p10), score 0.814
  - Evaluation and review
  - 10. The Commission shall, if necessary, submit appropriate proposals to amend this Regulation, in particular taking into account developments in technology, the effect of AI systems on health and safety, and on fundamental rights, and in light of the state of progress in the information society.
- Article 112, paragraph 11 (art:112:p11), score 0.814
  - Evaluation and review
  - 11. To guide the evaluations and reviews referred to in paragraphs 1 to 7 of this Article, the AI Office shall undertake to develop an objective and participative methodology for the evaluation of risk levels based on the criteria outlined in the relevant Articles and the inclusion of new systems in: (a) the list set out in Annex III, including the extension of existing area headings or the addition of new area headings in that Annex; (b) the list of prohibited practices set out in Article 5; and (c) the list of AI systems requiring additional transparency measures pursuant to Article 50.
- Article 92, paragraph 3 (art:92:p3), score 0.811
  - Power to conduct evaluations
  - 3. For the purposes of paragraph 1, the Commission may request access to the general-purpose AI model concerned through APIs or further appropriate technical means and tools, including source code.
- Article 112, paragraph 5 (art:112:p5), score 0.810
  - Evaluation and review
  - 5. By 2 August 2028, the Commission shall evaluate the functioning of the AI Office, whether the AI Office has been given sufficient powers and competences to fulfil its tasks, and whether it would be relevant and needed for the proper implementation and enforcement of this Regulation to upgrade the AI Office and its enforcement competences and to increase its resources. The Commission shall submit a report on its evaluation to the European Parliament and to the Council.

### REQ-156

**Risk level:** Medium

**Requirement:** The app shall comply with relevant privacy and health data protection laws in the

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 2, paragraph 7 with score 0.827. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 2, paragraph 7 (art:2:p7), score 0.827
  - Scope
  - 7. Union law on the protection of personal data, privacy and the confidentiality of communications applies to personal data processed in connection with the rights and obligations laid down in this Regulation. This Regulation shall not affect Regulation (EU) 2016/679 or (EU) 2018/1725, or Directive 2002/58/EC or (EU) 2016/680, without prejudice to Article 10(5) and Article 59 of this Regulation.
- Article 10, paragraph 5 (art:10:p5), score 0.808
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 8, paragraph 2 (art:8:p2), score 0.806
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 78, paragraph 2 (art:78:p2), score 0.804
  - Confidentiality
  - 2. The authorities involved in the application of this Regulation pursuant to paragraph 1 shall request only data that is strictly necessary for the assessment of the risk posed by AI systems and for the exercise of their powers in accordance with this Regulation and with Regulation (EU) 2019/1020. They shall put in place adequate and effective cybersecurity measures to protect the security and confidentiality of the information and data obtained, and shall delete the data collected as soon as it is no longer needed for the purpose for which it was obtained, in accordance with applicable Union or national law.
- Article 50, paragraph 3 (art:50:p3), score 0.801
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.

### REQ-157

**Risk level:** Medium

**Requirement:** The app shall comply with medical software regulations if its features qualify as

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 8, paragraph 2 with score 0.840. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 8, paragraph 2 (art:8:p2), score 0.840
  - Compliance with the requirements
  - 2. Where a product contains an AI system, to which the requirements of this Regulation as well as requirements of the Union harmonisation legislation listed in Section A of Annex I apply, providers shall be responsible for ensuring that their product is fully compliant with all applicable requirements under applicable Union harmonisation legislation. In ensuring the compliance of high-risk AI systems referred to in paragraph 1 with the requirements set out in this Section, and in order to ensure consistency, avoid duplication and minimise additional burdens, providers shall have a choice of integrating, as appropriate, the necessary testing and reporting processes, information and documentation they provide with regard to their product into documentation and procedures that already exist and are required under the Union harmonisation legislation listed in Section A of Annex I.
- Article 23, paragraph 1 (art:23:p1), score 0.822
  - Obligations of importers
  - 1. Before placing a high-risk AI system on the market, importers shall ensure that the system is in conformity with this Regulation by verifying that: (a) the relevant conformity assessment procedure referred to in Article 43 has been carried out by the provider of the high-risk AI system; (b) the provider has drawn up the technical documentation in accordance with Article 11 and Annex IV; (c) the system bears the required CE marking and is accompanied by the EU declaration of conformity referred to in Article 47 and instructions for use; (d) the provider has appointed an authorised representative in accordance with Article 22(1).
- Article 43, paragraph 3 (art:43:p3), score 0.820
  - Conformity assessment
  - 3. For high-risk AI systems covered by the Union harmonisation legislation listed in Section A of Annex I, the provider shall follow the relevant conformity assessment procedure as required under those legal acts. The requirements set out in Section 2 of this Chapter shall apply to those high-risk AI systems and shall be part of that assessment. Points 4.3., 4.4., 4.5. and the fifth paragraph of point 4.6 of Annex VII shall also apply. For the purposes of that assessment, notified bodies which have been notified under those legal acts shall be entitled to control the conformity of the high-risk AI systems with the requirements set out in Section 2, provided that the compliance of those notified bodies with requirements laid down in Article 31(4), (5), (10) and (11) has been assessed in the context of the notification procedure under those legal acts. Where a legal act listed in Section A of Annex I enables the product manufacturer to opt out from a third-party conformity assessment, provided that that manufacturer has applied all harmonised standards covering all the relevant requirements, that manufacturer may use that option only if it has also applied harmonised standards or, where applicable, common specifications referred to in Article 41, covering all requirements set out in Section 2 of this Chapter.
- Article 29, paragraph 2 (art:29:p2), score 0.820
  - Application of a conformity assessment body for notification
  - 2. The application for notification shall be accompanied by a description of the conformity assessment activities, the conformity assessment module or modules and the types of AI systems for which the conformity assessment body claims to be competent, as well as by an accreditation certificate, where one exists, issued by a national accreditation body attesting that the conformity assessment body fulfils the requirements laid down in Article 31. Any valid document related to existing designations of the applicant notified body under any other Union harmonisation legislation shall be added.
- Article 80, paragraph 4 (art:80:p4), score 0.820
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 4. The provider shall ensure that all necessary action is taken to bring the AI system into compliance with the requirements and obligations laid down in this Regulation. Where the provider of an AI system concerned does not bring the AI system into compliance with those requirements and obligations within the period referred to in paragraph 2 of this Article, the provider shall be subject to fines in accordance with Article 99.

### REQ-158

**Risk level:** High

**Requirement:** The app shall maintain records needed for clinical safety audits.

**Source:** examples\sample_srs_health_app.pdf, page 7

**Explanation:** Mapped to Article 12, paragraph 3 with score 0.815. Detected signals: Logging and traceability; Safety, robustness, and risk management. Estimated risk level: High.

**Risk signals:** Logging and traceability, Safety, robustness, and risk management

**Candidate EU AI Act provisions:**

- Article 12, paragraph 3 (art:12:p3), score 0.815
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 2 (art:12:p2), score 0.814
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 12, paragraph 1 (art:12:p1), score 0.814
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 113, paragraph 5 (art:113:p5), score 0.807
  - Entry into force and application
  - 5. Surveillance of the approved quality management system. 5.1. The purpose of the surveillance carried out by the notified body referred to in Point 3 is to make sure that the provider duly complies with the terms and conditions of the approved quality management system. 5.2. For assessment purposes, the provider shall allow the notified body to access the premises where the design, development, testing of the AI systems is taking place. The provider shall further share with the notified body all necessary information. 5.3. The notified body shall carry out periodic audits to make sure that the provider maintains and applies the quality management system and shall provide the provider with an audit report. In the context of those audits, the notified body may carry out additional tests of the AI systems for which a Union technical documentation assessment certificate was issued. ANNEX VIII Information to be submitted upon the registration of high-risk AI systems in accordance with
- Article 18, paragraph 3 (art:18:p3), score 0.803
  - Documentation keeping
  - 3. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the technical documentation as part of the documentation kept under the relevant Union financial services law.

### REQ-159

**Risk level:** Medium

**Requirement:** The app shall provide consent management features.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 113, paragraph 4 with score 0.794. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 113, paragraph 4 (art:113:p4), score 0.794
  - Entry into force and application
  - 4. Control of the technical documentation. 4.1. In addition to the application referred to in point 3, an application with a notified body of their choice shall be lodged by the provider for the assessment of the technical documentation relating to the AI system which the provider intends to place on the market or put into service and which is covered by the quality management system referred to under point 3. 4.2. The application shall include: (a) the name and address of the provider; (b) a written declaration that the same application has not been lodged with any other notified body; (c) the technical documentation referred to in Annex IV. 134/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj 4.3. The technical documentation shall be examined by the notified body. Where relevant, and limited to what is necessary to fulfil its tasks, the notified body shall be granted full access to the training, validation, and testing data sets used, including, where appropriate and subject to security safeguards, through API or other relevant technical means and tools enabling remote access. 4.4. In examining the technical documentation, the notified body may require that the provider supply further evidence or carry out further tests so as to enable a proper assessment of the conformity of the AI system with the requirements set out in Chapter III, Section 2. Where the notified body is not satisfied with the tests carried out by the provider, the notified body shall itself directly carry out adequate tests, as appropriate. 4.5. Where necessary to assess the conformity of the high-risk AI system with the requirements set out in Chapter III, Section 2, after all other reasonable means to verify conformity have been exhausted and have proven to be insufficient, and upon a reasoned request, the notified body shall also be granted access to the training and trained models of the AI system, including its relevant parameters. Such access shall be subject to existing Union law on the protection of intellectual property and trade secrets. 4.6. The decision of the notified body shall be notified to the provider or its authorised representative. The notification shall contain the conclusions of the assessment of the technical documentation and the reasoned assessment decision. Where the AI system is in conformity with the requirements set out in Chapter III, Section 2, the notified body shall issue a Union technical documentation assessment certificate. The certificate shall indicate the name and address of the provider, the conclusions of the examination, the conditions (if any) for its validity and the data necessary for the identification of the AI system. The certificate and its annexes shall contain all relevant information to allow the conformity of the AI system to be evaluated, and to allow for control of the AI system while in use, where applicable. Where the AI system is not in conformity with the requirements set out in Chapter III, Section 2, the notified body shall refuse to issue a Union technical documentation assessment certificate and shall inform the applicant accordingly, giving detailed reasons for its refusal. Where the AI system does not meet the requirement relating to the data used to train it, re-training of the AI system will be needed prior to the application for a new conformity assessment. In this case, the reasoned assessment decision of the notified body refusing to issue the Union technical documentation assessment certificate shall contain specific considerations on the quality data used to train the AI system, in particular on the reasons for non-compliance. 4.7. Any change to the AI system that could affect the compliance of the AI system with the requirements or its intended purpose shall be assessed by the notified body which issued the Union technical documentation assessment certificate. The provider shall inform such notified body of its intention to introduce any of the abovementioned changes, or if it otherwise becomes aware of the occurrence of such changes. The intended changes shall be assessed by the notified body, which shall decide whether those changes require a new conformity assessment in accordance with Article 43(4) or whether they could be addressed by means of a supplement to the Union technical documentation assessment certificate. In the latter case, the notified body shall assess the changes, notify the provider of its decision and, where the changes are approved, issue to the provider a supplement to the Union technical documentation assessment certificate.
- Article 21, paragraph 2 (art:21:p2), score 0.791
  - Cooperation with competent authorities
  - 2. Upon a reasoned request by a competent authority, providers shall also give the requesting competent authority, as applicable, access to the automatically generated logs of the high-risk AI system referred to in Article 12(1), to the extent such logs are under their control.
- Article 92, paragraph 5 (art:92:p5), score 0.790
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 50, paragraph 3 (art:50:p3), score 0.789
  - Transparency obligations for providers and deployers of certain AI systems
  - 3. Deployers of an emotion recognition system or a biometric categorisation system shall inform the natural persons exposed thereto of the operation of the system, and shall process the personal data in accordance with Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, as applicable. This obligation shall not apply to AI systems used for biometric categorisation and emotion recognition, which are permitted by law to detect, prevent or investigate criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, and in accordance with Union law.
- Article 74, paragraph 12 (art:74:p12), score 0.788
  - Market surveillance and control of AI systems in the Union market
  - 12. Without prejudice to the powers provided for under Regulation (EU) 2019/1020, and where relevant and limited to what is necessary to fulfil their tasks, the market surveillance authorities shall be granted full access by providers to the documentation as well as the training, validation and testing data sets used for the development of high-risk AI systems, including, where appropriate and subject to security safeguards, through application programming interfaces (API) or other relevant technical means and tools enabling remote access.

### REQ-160

**Risk level:** Medium

**Requirement:** The app shall support data retention and deletion policies.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 10, paragraph 5 with score 0.791. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 10, paragraph 5 (art:10:p5), score 0.791
  - Data and data governance
  - 5. To the extent that it is strictly necessary for the purpose of ensuring bias detection and correction in relation to the high-risk AI systems in accordance with paragraph (2), points (f) and (g) of this Article, the providers of such systems may exceptionally process special categories of personal data, subject to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680, all the following conditions must be met in order for such processing to occur: (a) the bias detection and correction cannot be effectively fulfilled by processing other data, including synthetic or anonymised data; (b) the special categories of personal data are subject to technical limitations on the re-use of the personal data, and state-of-the-art security and privacy-preserving measures, including pseudonymisation; (c) the special categories of personal data are subject to measures to ensure that the personal data processed are secured, protected, subject to suitable safeguards, including strict controls and documentation of the access, to avoid misuse and ensure that only authorised persons have access to those personal data with appropriate confidentiality obligations; (d) the special categories of personal data are not to be transmitted, transferred or otherwise accessed by other parties; (e) the special categories of personal data are deleted once the bias has been corrected or the personal data has reached the end of its retention period, whichever comes first; (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special categories of personal data was strictly necessary to detect and correct biases, and why that objective could not be achieved by processing other data.
- Article 12, paragraph 3 (art:12:p3), score 0.783
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 10, paragraph 2 (art:10:p2), score 0.782
  - Data and data governance
  - 2. Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system. Those practices shall concern in particular: (a) the relevant design choices; (b) data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection; (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation; (d) the formulation of assumptions, in particular with respect to the information that the data are supposed to measure and represent; (e) an assessment of the availability, quantity and suitability of the data sets that are needed; (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations; (g) appropriate measures to detect, prevent and mitigate possible biases identified according to point (f); (h) the identification of relevant data gaps or shortcomings that prevent compliance with this Regulation, and how those gaps and shortcomings can be addressed.
- Article 12, paragraph 1 (art:12:p1), score 0.781
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 26, paragraph 6 (art:26:p6), score 0.779
  - Obligations of deployers of high-risk AI systems
  - 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.

### REQ-161

**Risk level:** Medium

**Requirement:** The app shall provide users with clear terms of use and privacy notices.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 2, paragraph 7 with score 0.787. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 2, paragraph 7 (art:2:p7), score 0.787
  - Scope
  - 7. Union law on the protection of personal data, privacy and the confidentiality of communications applies to personal data processed in connection with the rights and obligations laid down in this Regulation. This Regulation shall not affect Regulation (EU) 2016/679 or (EU) 2018/1725, or Directive 2002/58/EC or (EU) 2016/680, without prejudice to Article 10(5) and Article 59 of this Regulation.
- Article 50, paragraph 5 (art:50:p5), score 0.782
  - Transparency obligations for providers and deployers of certain AI systems
  - 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- Article 78, paragraph 2 (art:78:p2), score 0.779
  - Confidentiality
  - 2. The authorities involved in the application of this Regulation pursuant to paragraph 1 shall request only data that is strictly necessary for the assessment of the risk posed by AI systems and for the exercise of their powers in accordance with this Regulation and with Regulation (EU) 2019/1020. They shall put in place adequate and effective cybersecurity measures to protect the security and confidentiality of the information and data obtained, and shall delete the data collected as soon as it is no longer needed for the purpose for which it was obtained, in accordance with applicable Union or national law.
- Article 50, paragraph 2 (art:50:p2), score 0.778
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 50, paragraph 1 (art:50:p1), score 0.776
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

### REQ-162

**Risk level:** Medium

**Requirement:** The system shall maintain regular backups of user data.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 26, paragraph 6 with score 0.803. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 26, paragraph 6 (art:26:p6), score 0.803
  - Obligations of deployers of high-risk AI systems
  - 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
- Article 12, paragraph 3 (art:12:p3), score 0.800
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 19, paragraph 1 (art:19:p1), score 0.796
  - Automatically generated logs
  - 1. Providers of high-risk AI systems shall keep the logs referred to in Article 12(1), automatically generated by their high-risk AI systems, to the extent such logs are under their control. Without prejudice to applicable Union or national law, the logs shall be kept for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in the applicable Union or national law, in particular in Union law on the protection of personal data.
- Article 18, paragraph 3 (art:18:p3), score 0.795
  - Documentation keeping
  - 3. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the technical documentation as part of the documentation kept under the relevant Union financial services law.
- Article 12, paragraph 1 (art:12:p1), score 0.790
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.

### REQ-163

**Risk level:** Medium

**Requirement:** The system shall support disaster recovery procedures.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 12, paragraph 2 with score 0.805. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 12, paragraph 2 (art:12:p2), score 0.805
  - Record-keeping
  - 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- Article 9, paragraph 1 (art:9:p1), score 0.803
  - Risk management system
  - 1. A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems.
- Article 12, paragraph 3 (art:12:p3), score 0.803
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).
- Article 12, paragraph 1 (art:12:p1), score 0.798
  - Record-keeping
  - 1. High-risk AI systems shall technically allow for the automatic recording of events (logs) over the lifetime of the system.
- Article 73, paragraph 6 (art:73:p6), score 0.795
  - Reporting of serious incidents
  - 6. Following the reporting of a serious incident pursuant to paragraph 1, the provider shall, without delay, perform the necessary investigations in relation to the serious incident and the AI system concerned. This shall include a risk assessment of the incident, and corrective action. The provider shall cooperate with the competent authorities, and where relevant with the notified body concerned, during the investigations referred to in the first subparagraph, and shall not perform any investigation which involves altering the AI system concerned in a way which may affect any subsequent evaluation of the causes of the incident, prior to informing the competent authorities of such action.

### REQ-164

**Risk level:** Medium

**Requirement:** The system shall minimise downtime for critical services.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.785. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.785
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 34, paragraph 2 (art:34:p2), score 0.784
  - Operational obligations of notified bodies
  - 2. Notified bodies shall avoid unnecessary burdens for providers when performing their activities, and take due account of the size of the provider, the sector in which it operates, its structure and the degree of complexity of the high-risk AI system concerned, in particular in view of minimising administrative burdens and compliance costs for micro- and small enterprises within the meaning of Recommendation 2003/361/EC. The notified body shall, nevertheless, respect the degree of rigour and the level of protection required for the compliance of the high-risk AI system with the requirements of this Regulation.
- Article 17, paragraph 4 (art:17:p4), score 0.784
  - Quality management system
  - 4. For providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law, the obligation to put in place a quality management system, with the exception of paragraph 1, points (g), (h) and (i) of this Article, shall be deemed to be fulfilled by complying with the rules on internal governance arrangements or processes pursuant to the relevant Union financial services law. To that end, any harmonised standards referred to in Article 40 shall be taken into account.
- Article 81, paragraph 2 (art:81:p2), score 0.783
  - Union safeguard procedure
  - 2. Where the Commission considers the measure taken by the relevant Member State to be justified, all Member States shall ensure that they take appropriate restrictive measures in respect of the AI system concerned, such as requiring the withdrawal of the AI system from their market without undue delay, and shall inform the Commission accordingly. Where the Commission considers the national measure to be unjustified, the Member State concerned shall withdraw the measure and shall inform the Commission accordingly.
- Article 70, paragraph 3 (art:70:p3), score 0.783
  - Designation of national competent authorities and single points of contact
  - 3. Member States shall ensure that their national competent authorities are provided with adequate technical, financial and human resources, and with infrastructure to fulfil their tasks effectively under this Regulation. In particular, the national competent authorities shall have a sufficient number of personnel permanently available whose competences and expertise shall include an in-depth understanding of AI technologies, data and data computing, personal data protection, cybersecurity, fundamental rights, health and safety risks and knowledge of existing standards and legal requirements. Member States shall assess and, if necessary, update competence and resource requirements referred to in this paragraph on an annual basis.

### REQ-165

**Risk level:** Medium

**Requirement:** The system shall notify users of planned maintenance where possible.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 28, paragraph 7 with score 0.839. Detected signals: Transparency and user information. Estimated risk level: Medium.

**Risk signals:** Transparency and user information

**Candidate EU AI Act provisions:**

- Article 28, paragraph 7 (art:28:p7), score 0.839
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
- Article 36, paragraph 6 (art:36:p6), score 0.829
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 31, paragraph 8 (art:31:p8), score 0.827
  - Requirements relating to notified bodies
  - 8. Notified bodies shall have procedures for the performance of activities which take due account of the size of a provider, the sector in which it operates, its structure, and the degree of complexity of the AI system concerned.
- Article 36, paragraph 4 (art:36:p4), score 0.826
  - Changes to notifications
  - 4. Where a notifying authority has sufficient reason to consider that a notified body no longer meets the requirements laid down in Article 31, or that it is failing to fulfil its obligations, the notifying authority shall without delay investigate the matter with the utmost diligence. In that context, it shall inform the notified body concerned about the objections raised and give it the possibility to make its views known. If the notifying authority comes to the conclusion that the notified body no longer meets the requirements laid down in Article 31 or that it is failing to fulfil its obligations, it shall restrict, suspend or withdraw the designation as appropriate, depending on the seriousness of the failure to meet those requirements or fulfil those obligations. It shall immediately inform the Commission and the other Member States accordingly.
- Article 37, paragraph 2 (art:37:p2), score 0.823
  - Challenge to the competence of notified bodies
  - 2. The notifying authority shall provide the Commission, on request, with all relevant information relating to the notification or the maintenance of the competence of the notified body concerned.

### REQ-166

**Risk level:** Medium

**Requirement:** The system shall ensure emergency information remains accessible during service

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 45, paragraph 4 with score 0.823. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 45, paragraph 4 (art:45:p4), score 0.823
  - Information obligations of notified bodies
  - 4. Notified bodies shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 18, paragraph 2 (art:18:p2), score 0.815
  - Documentation keeping
  - 2. Each Member State shall determine conditions under which the documentation referred to in paragraph 1 remains at the disposal of the national competent authorities for the period indicated in that paragraph for the cases when a provider or its authorised representative established on its territory goes bankrupt or ceases its activity prior to the end of that period.
- Article 28, paragraph 6 (art:28:p6), score 0.815
  - Notifying authorities
  - 6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.
- Article 18, paragraph 1 (art:18:p1), score 0.814
  - Documentation keeping
  - 1. The provider shall, for a period ending 10 years after the high-risk AI system has been placed on the market or put into service, keep at the disposal of the national competent authorities: (a) the technical documentation referred to in Article 11; (b) the documentation concerning the quality management system referred to in Article 17; (c) the documentation concerning the changes approved by notified bodies, where applicable; (d) the decisions and other documents issued by the notified bodies, where applicable; (e) the EU declaration of conformity referred to in Article 47.
- Article 12, paragraph 3 (art:12:p3), score 0.811
  - Record-keeping
  - 3. For high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum: (a) recording of the period of each use of the system (start date and time and end date and time of each use); (b) the reference database against which input data has been checked by the system; (c) the input data for which the search has led to a match; (d) the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5).

### REQ-167

**Risk level:** High

**Requirement:** The app shall explain why important alerts or recommendations were generated.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 90, paragraph 3 with score 0.809. Detected signals: Automated decision-making; Transparency and user information. Estimated risk level: High.

**Risk signals:** Automated decision-making, Transparency and user information

**Candidate EU AI Act provisions:**

- Article 90, paragraph 3 (art:90:p3), score 0.809
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 27, paragraph 3 (art:27:p3), score 0.791
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.
- Article 90, paragraph 2 (art:90:p2), score 0.786
  - Alerts of systemic risks by the scientific panel
  - 2. Upon such qualified alert, the Commission, through the AI Office and after having informed the Board, may exercise the powers laid down in this Section for the purpose of assessing the matter. The AI Office shall inform the Board of any measure according to Articles 91 to 94.
- Article 19, paragraph 2 (art:19:p2), score 0.784
  - Automatically generated logs
  - 2. Providers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs automatically generated by their high-risk AI systems as part of the documentation kept under the relevant financial services law.
- Article 73, paragraph 2 (art:73:p2), score 0.784
  - Reporting of serious incidents
  - 2. The report referred to in paragraph 1 shall be made immediately after the provider has established a causal link between the AI system and the serious incident or the reasonable likelihood of such a link, and, in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident. The period for the reporting referred to in the first subparagraph shall take account of the severity of the serious incident.

### REQ-168

**Risk level:** Medium

**Requirement:** The app shall show users when data was last updated.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 36, paragraph 5 with score 0.784. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 36, paragraph 5 (art:36:p5), score 0.784
  - Changes to notifications
  - 5. Where its designation has been suspended, restricted, or fully or partially withdrawn, the notified body shall inform the providers concerned within 10 days.
- Article 36, paragraph 6 (art:36:p6), score 0.779
  - Changes to notifications
  - 6. In the event of the restriction, suspension or withdrawal of a designation, the notifying authority shall take appropriate steps to ensure that the files of the notified body concerned are kept, and to make them available to notifying authorities in other Member States and to market surveillance authorities at their request.
- Article 27, paragraph 3 (art:27:p3), score 0.777
  - Fundamental rights impact assessment for high-risk AI systems
  - 3. Once the assessment referred to in paragraph 1 of this Article has been performed, the deployer shall notify the market surveillance authority of its results, submitting the filled-out template referred to in paragraph 5 of this Article as part of the notification. In the case referred to in Article 46(1), deployers may be exempt from that obligation to notify.
- Article 36, paragraph 8 (art:36:p8), score 0.776
  - Changes to notifications
  - 8. With the exception of certificates unduly issued, and where a designation has been suspended or restricted, the certificates shall remain valid in one of the following circumstances: (a) the notifying authority has confirmed, within one month of the suspension or restriction, that there is no risk to health, safety or fundamental rights in relation to certificates affected by the suspension or restriction, and the notifying authority has outlined a timeline for actions to remedy the suspension or restriction; or (b) the notifying authority has confirmed that no certificates relevant to the suspension will be issued, amended or re-issued during the course of the suspension or restriction, and states whether the notified body has the capability of continuing to monitor and remain responsible for existing certificates issued for the period of the suspension or restriction; in the event that the notifying authority determines that the notified body does not have the capability to support existing certificates issued, the provider of the system covered by the certificate shall confirm in writing to the national competent authorities of the Member State in which it has its registered place of business, within three months of the suspension or restriction, that another qualified notified body is temporarily assuming the functions of the notified body to monitor and remain responsible for the certificates during the period of suspension or restriction. 74/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 28, paragraph 6 (art:28:p6), score 0.773
  - Notifying authorities
  - 6. Notifying authorities shall safeguard the confidentiality of the information that they obtain, in accordance with Article 78.

### REQ-169

**Risk level:** Medium

**Requirement:** The app shall identify whether advice came from AI, a caregiver, or a healthcare

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 50, paragraph 1 with score 0.817. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 1 (art:50:p1), score 0.817
  - Transparency obligations for providers and deployers of certain AI systems
  - 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- Article 92, paragraph 5 (art:92:p5), score 0.814
  - Power to conduct evaluations
  - 5. The providers of the general-purpose AI model concerned or its representative shall supply the information requested. In the case of legal persons, companies or firms, or where the provider has no legal personality, the persons authorised to represent them by law or by their statutes, shall provide the access requested on behalf of the provider of the general-purpose AI model concerned.
- Article 75, paragraph 1 (art:75:p1), score 0.811
  - Mutual assistance, market surveillance and control of general-purpose AI systems
  - 1. Where an AI system is based on a general-purpose AI model, and the model and the system are developed by the same provider, the AI Office shall have powers to monitor and supervise compliance of that AI system with obligations under this Regulation. To carry out its monitoring and supervision tasks, the AI Office shall have all the powers of a market surveillance authority provided for in this Section and Regulation (EU) 2019/1020.
- Article 7, paragraph 2 (art:7:p2), score 0.807
  - Amendments to Annex III
  - 2. When assessing the condition under paragraph 1, point (b), the Commission shall take into account the following criteria: (a) the intended purpose of the AI system; (b) the extent to which an AI system has been used or is likely to be used; (c) the nature and amount of the data processed and used by the AI system, in particular whether special categories of personal data are processed; (d) the extent to which the AI system acts autonomously and the possibility for a human to override a decision or recommendations that may lead to potential harm; (e) the extent to which the use of an AI system has already caused harm to health and safety, has had an adverse impact on fundamental rights or has given rise to significant concerns in relation to the likelihood of such harm or adverse impact, as demonstrated, for example, by reports or documented allegations submitted to national competent authorities or by other reports, as appropriate; (f) the potential extent of such harm or such adverse impact, in particular in terms of its intensity and its ability to affect multiple persons or to disproportionately affect a particular group of persons; (g) the extent to which persons who are potentially harmed or suffer an adverse impact are dependent on the outcome produced with an AI system, in particular because for practical or legal reasons it is not reasonably possible to opt-out from that outcome; (h) the extent to which there is an imbalance of power, or the persons who are potentially harmed or suffer an adverse impact are in a vulnerable position in relation to the deployer of an AI system, in particular due to status, authority, knowledge, economic or social circumstances, or age; (i) the extent to which the outcome produced involving an AI system is easily corrigible or reversible, taking into account the technical solutions available to correct or reverse it, whereby outcomes having an adverse impact on health, safety or fundamental rights, shall not be considered to be easily corrigible or reversible; (j) the magnitude and likelihood of benefit of the deployment of the AI system for individuals, groups, or society at large, including possible improvements in product safety; (k) the extent to which existing Union law provides for: (i) effective measures of redress in relation to the risks posed by an AI system, with the exclusion of claims for damages; (ii) effective measures to prevent or substantially minimise those risks.
- Article 92, paragraph 7 (art:92:p7), score 0.805
  - Power to conduct evaluations
  - 7. Prior to requesting access to the general-purpose AI model concerned, the AI Office may initiate a structured dialogue with the provider of the general-purpose AI model to gather more information on the internal testing of the model, internal safeguards for preventing systemic risks, and other internal procedures and measures the provider has taken to mitigate such risks.

### REQ-170

**Risk level:** Medium

**Requirement:** The app shall allow users to challenge, correct, or dismiss AI-generated

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 50, paragraph 2 with score 0.837. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 50, paragraph 2 (art:50:p2), score 0.837
  - Transparency obligations for providers and deployers of certain AI systems
  - 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- Article 27, paragraph 5 (art:27:p5), score 0.830
  - Fundamental rights impact assessment for high-risk AI systems
  - 5. The AI Office shall develop a template for a questionnaire, including through an automated tool, to facilitate deployers in complying with their obligations under this Article in a simplified manner. SECTION 4 Notifying authorities and notified bodies
- Article 57, paragraph 5 (art:57:p5), score 0.829
  - AI regulatory sandboxes
  - 5. AI regulatory sandboxes established under paragraph 1 shall provide for a controlled environment that fosters innovation and facilitates the development, training, testing and validation of innovative AI systems for a limited time before their being placed on the market or put into service pursuant to a specific sandbox plan agreed between the providers or prospective providers and the competent authority. Such sandboxes may include testing in real world conditions supervised therein.
- Article 50, paragraph 4 (art:50:p4), score 0.827
  - Transparency obligations for providers and deployers of certain AI systems
  - 4. Deployers of an AI system that generates or manipulates image, audio or video content constituting a deep fake, shall disclose that the content has been artificially generated or manipulated. This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offence. Where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work or programme, the transparency obligations set out in this paragraph are limited to disclosure of the existence of such generated or manipulated content in an appropriate manner that does not hamper the display or enjoyment of the work. Deployers of an AI system that generates or manipulates text which is published with the purpose of informing the public on matters of public interest shall disclose that the text has been artificially generated or manipulated. This obligation shall not apply where the use is authorised by law to detect, prevent, investigate or prosecute criminal offences or where the AI-generated content has undergone a process of human review or editorial control and where a natural or legal person holds editorial responsibility for the publication of the content. 82/144 ELI: http://data.europa.eu/eli/reg/2024/1689/oj
- Article 60, paragraph 5 (art:60:p5), score 0.824
  - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes
  - 5. Any subjects of the testing in real world conditions, or their legally designated representative, as appropriate, may, without any resulting detriment and without having to provide any justification, withdraw from the testing at any time by revoking their informed consent and may request the immediate and permanent deletion of their personal data. The withdrawal of the informed consent shall not affect the activities already carried out.

### REQ-171

**Risk level:** Medium

**Requirement:** The app shall avoid creating false reassurance when symptoms may require

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 52, paragraph 1 with score 0.786. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 52, paragraph 1 (art:52:p1), score 0.786
  - Procedure
  - 1. Where a general-purpose AI model meets the condition referred to in Article 51(1), point (a), the relevant provider shall notify the Commission without delay and in any event within two weeks after that requirement is met or it becomes known that it will be met. That notification shall include the information necessary to demonstrate that the relevant requirement has been met. If the Commission becomes aware of a general-purpose AI model presenting systemic risks of which it has not been notified, it may decide to designate it as a model with systemic risk.
- Article 23, paragraph 2 (art:23:p2), score 0.786
  - Obligations of importers
  - 2. Where an importer has sufficient reason to consider that a high-risk AI system is not in conformity with this Regulation, or is falsified, or accompanied by falsified documentation, it shall not place the system on the market until it has been brought into conformity. Where the high-risk AI system presents a risk within the meaning of Article 79(1), the importer shall inform the provider of the system, the authorised representative and the market surveillance authorities to that effect.
- Article 90, paragraph 3 (art:90:p3), score 0.786
  - Alerts of systemic risks by the scientific panel
  - 3. A qualified alert shall be duly reasoned and indicate at least: (a) the point of contact of the provider of the general-purpose AI model with systemic risk concerned; (b) a description of the relevant facts and the reasons for the alert by the scientific panel; (c) any other information that the scientific panel considers to be relevant, including, where appropriate, information gathered on its own initiative.
- Article 6, paragraph 4 (art:6:p4), score 0.786
  - Classification rules for high-risk AI systems
  - 4. A provider who considers that an AI system referred to in Annex III is not high-risk shall document its assessment before that system is placed on the market or put into service. Such provider shall be subject to the registration obligation set out in Article 49(2). Upon request of national competent authorities, the provider shall provide the documentation of the assessment.
- Article 46, paragraph 2 (art:46:p2), score 0.785
  - Derogation from conformity assessment procedure
  - 2. In a duly justified situation of urgency for exceptional reasons of public security or in the case of specific, substantial and imminent threat to the life or physical safety of natural persons, law-enforcement authorities or civil protection authorities may put a specific high-risk AI system into service without the authorisation referred to in paragraph 1, provided that such authorisation is requested during or after the use without undue delay. If the authorisation referred to in paragraph 1 is refused, the use of the high-risk AI system shall be stopped with immediate effect and all the results and outputs of such use shall be immediately discarded.

### REQ-172

**Risk level:** Medium

**Requirement:** The app shall provide clear disclaimers without overwhelming users.

**Source:** examples\sample_srs_health_app.pdf, page 8

**Explanation:** Mapped to Article 28, paragraph 3 with score 0.794. Detected signals: no explicit keyword risk signal. Estimated risk level: Medium.

**Candidate EU AI Act provisions:**

- Article 28, paragraph 3 (art:28:p3), score 0.794
  - Notifying authorities
  - 3. Notifying authorities shall be established, organised and operated in such a way that no conflict of interest arises with conformity assessment bodies, and that the objectivity and impartiality of their activities are safeguarded.
- Article 63, paragraph 1 (art:63:p1), score 0.788
  - Derogations for specific operators
  - 1. Microenterprises within the meaning of Recommendation 2003/361/EC may comply with certain elements of the quality management system required by Article 17 of this Regulation in a simplified manner, provided that they do not have partner enterprises or linked enterprises within the meaning of that Recommendation. For that purpose, the Commission shall develop guidelines on the elements of the quality management system which may be complied with in a simplified manner considering the needs of microenterprises, without affecting the level of protection or the need for compliance with the requirements in respect of high-risk AI systems.
- Article 80, paragraph 8 (art:80:p8), score 0.787
  - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III
  - 8. In exercising their power to monitor the application of this Article, and in accordance with Article 11 of Regulation (EU) 2019/1020, market surveillance authorities may perform appropriate checks, taking into account in particular information stored in the EU database referred to in Article 71 of this Regulation.
- Article 13, paragraph 2 (art:13:p2), score 0.783
  - Transparency and provision of information to deployers
  - 2. High-risk AI systems shall be accompanied by instructions for use in an appropriate digital format or otherwise that include concise, complete, correct and clear information that is relevant, accessible and comprehensible to deployers.
- Article 28, paragraph 7 (art:28:p7), score 0.782
  - Notifying authorities
  - 7. Notifying authorities shall have an adequate number of competent personnel at their disposal for the proper performance of their tasks. Competent personnel shall have the necessary expertise, where applicable, for their function, in fields such as information technologies, AI and law, including the supervision of fundamental rights.
