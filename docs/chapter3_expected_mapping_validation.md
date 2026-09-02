# Chapter 3 Expected Mapping Set

## Purpose

This validation table is intended to check whether the current risk assessment output is mapping software requirements to the most relevant EU AI Act provisions for a recruitment-screening use case. The focus is on Chapter 3 high-risk AI systems, especially Article 6, Annex III employment classification, and Articles 8-15 obligations.

The goal is not to make final legal conclusions. The goal is to create a small manual expected-mapping set that can be compared against the current pipeline output to identify correct matches, weak matches, false positives, missing obligations, and areas where the retrieval/risk report should be improved.

## Scope used for validation

For the sample AI recruitment system, the whole system should likely be treated as a potential **Annex III employment/recruitment high-risk AI system**, because it supports candidate screening, scoring, ranking, and recruiter decision-making.

Most useful expected provisions/categories:

- **Article 6 + Annex III**: high-risk classification, especially employment/recruitment use.
- **Article 9**: risk management.
- **Article 10**: data and data governance.
- **Article 11**: technical documentation.
- **Article 12**: record-keeping/logging.
- **Article 13**: transparency and information to deployers.
- **Article 14**: human oversight.
- **Article 15**: accuracy, robustness, and cybersecurity.
- **Articles 16-27**: provider/deployer obligations where responsibility needs to be separated.

Lower priority unless directly relevant:

- Notified body/admin provisions.
- Entry into force/application articles.
- General evaluation/review articles.
- Market surveillance/safeguard procedure articles.
- Conformity assessment articles unless the requirement is specifically about conformity/approval.

## Validation table

| Requirement ID | Requirement text | Expected high-risk domain | Expected obligation category | Expected EU AI Act mapping | Current system output summary | Assessment | Suggested fix |
|---|---|---|---|---|---|---|---|
| FR-1 | The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal. | Employment/recruitment context, but this requirement alone is mainly data ingestion. | Data governance, privacy/security context, possibly technical documentation. | Annex III employment as system-level context; Article 10 if data quality/appropriateness is discussed; Article 11 if documented input/data sources are needed. | Top matches are Article 113 and Article 31, which are entry/application and notified-body style provisions. | Weak match / false positive. | Do not treat generic ingestion as high legal risk by itself. Use system-level Annex III employment context, then map this requirement to data governance only if it involves data quality, relevance, or protected/personal data. Down-rank Article 113 and notified body articles. |
| FR-2 | The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application. | Employment/recruitment high-risk AI. | Data governance, accuracy, transparency, human oversight. | Annex III employment/recruitment; Article 10 data governance; Article 13 transparency; Article 14 human oversight; Article 15 accuracy/robustness. | Current output includes Article 10 as top match, but also Article 113 and Article 112. | Partially correct. | Keep Article 10. Add/boost Annex III employment and Articles 13-15. Down-rank Article 113/112 unless there is a specific admin/evaluation reason. |
| FR-3 | The system shall rank candidates for recruiter review using the generated suitability score. | Employment/recruitment high-risk AI. | High-risk classification, human oversight, transparency, accuracy. | Annex III employment/recruitment; Article 13 transparency; Article 14 human oversight; Article 15 accuracy/robustness; Article 6 classification context. | Current output mostly returns Article 113, Article 112, and Article 7, not the main recruitment/human oversight provisions. | Incorrect / weak match. | Add employment/recruitment trigger detection for words like rank candidates, recruiter review, suitability score. Boost Annex III employment, Article 14, Article 13, Article 15. |
| FR-4 | The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter. | Employment/recruitment high-risk AI. | Transparency/explainability to deployer; possibly documentation. | Article 13 transparency and information to deployers; Article 11 technical documentation where applicable; Annex III employment as context. | Current output returns Article 113, Article 7, and Article 82. | Incorrect / weak match. | Add direct mapping for explain/explanation/understandable language to Article 13. Down-rank Article 113 and Article 82 for requirement-level output. |
| FR-5 | The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model. | Employment/recruitment high-risk AI. | Transparency/information to deployers; possibly deployer obligations. | Article 13 transparency; Article 26 deployer use obligations where relevant; Annex III employment context. | Current output returns Article 28, Article 52, Article 27, Article 31, Article 113. | Mostly incorrect. | Map notification/disclosure to recruiters to Article 13 first. Article 27 may be relevant later for impact assessment, but it should not be the top match for a simple notification requirement. Down-rank Article 28/31/52/113. |
| FR-6 | The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration. | Employment/recruitment high-risk AI. | Human oversight; safeguard/mitigation rather than missing risk. | Article 14 human oversight; Article 26 deployer responsibility where human use is involved; Annex III employment context. | Current output includes Article 14(4), which is useful, but the top match is Article 81 and it also includes Article 14(5), Article 113, Article 79. | Partially correct. | Keep Article 14(4). Down-rank Article 81/79/113. Avoid Article 14(5) unless the requirement involves biometric identification. Mark this as “human oversight addressed/partially addressed”, not simply as a risk gap. |
| FR-7 | The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision. | Employment/recruitment high-risk AI. | Record-keeping/logging; traceability; provider/deployer responsibilities. | Article 12 record-keeping; Article 19 automatically generated logs; Article 11 technical documentation where traceability evidence is needed. | Current output maps to Article 12 and Article 19. | Correct. | This is a good match. Keep as expected behaviour. Could also label obligation category as “record_keeping/logging”. |
| FR-8 | The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved. | Employment/recruitment high-risk AI. | Record-keeping, traceability, technical documentation. | Article 12 record-keeping; Article 11 technical documentation; Article 18 documentation keeping may be relevant for provider-side record retention. | Current output maps to Article 12, but also Article 113 and Article 10. | Mostly correct with noise. | Keep Article 12. Add/boost Article 11/18 if documentation retention is intended. Down-rank Article 113. |
| FR-9 | The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening. | Employment/recruitment context with biometric/emotion-recognition guardrail. | Prohibited/sensitive AI practice avoidance; safeguard. | Article 5 may be relevant for prohibited practices, especially emotion recognition in workplace contexts; Annex III biometrics may be relevant as a warning category; this requirement is a mitigation, not a risk gap. | Current output includes Article 50, Article 5, Article 79, Article 46. | Partially correct. | Keep Article 5 as useful. Consider mapping to biometric/emotion-recognition guardrail. Avoid treating the requirement as if the system uses biometrics; it says it prevents them. Down-rank conformity/admin articles unless needed. |
| FR-10 | The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking. | Employment/recruitment high-risk AI. | Human oversight, transparency, contestability/review, deployer process. | Article 14 human oversight; Article 13 transparency; Article 26 deployer obligations may be relevant; Annex III employment context. | Current output returns Article 92, Article 93, Article 112, Article 91. | Incorrect / weak match. | Map request review / decision influenced by automated ranking to human oversight and transparency. Down-rank Commission/institutional powers and evaluation/review articles. |
| NFR-1 | The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training. | Employment/recruitment high-risk AI. | Data governance, data quality. | Article 10 data and data governance; Article 15 where validation affects accuracy/robustness. | Current output maps strongly to Article 10 and Article 15. | Correct. | Good expected behaviour. Keep Article 10 as primary. |
| NFR-2 | The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available. | Employment/recruitment high-risk AI. | Data governance, bias/fairness evaluation, accuracy. | Article 10 data governance; Article 15 accuracy/robustness; possibly risk management under Article 9. | Current output maps to Article 10, but also Article 112 and Article 92. | Partially correct. | Keep Article 10. Add/boost Article 15 and possibly Article 9. Down-rank Article 112/92 unless evaluating the Act itself or regulator powers. |
| NFR-3 | The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs. | Employment/recruitment high-risk AI. | Data governance, bias/fairness, prohibited/disallowed inputs, safeguard. | Article 10 data governance; Article 5 may be relevant if prohibited discriminatory/social scoring logic is implicated; Annex III employment context. | Current output includes Article 6, Article 5, Article 46, Article 80, Article 7. | Partially correct but missing Article 10. | Add Article 10 as a key expected mapping because the requirement is mainly about input data governance and bias control. Treat this as a safeguard/mitigation, not only a risk. Down-rank Article 46/80/7 unless context supports them. |
| NFR-4 | The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations. | Employment/recruitment high-risk AI. | Security, confidentiality, data governance, access control. | Article 15 cybersecurity may be relevant; Article 10 data governance where data access/management is relevant; Article 78 confidentiality may be secondary but less central to requirements-level mapping. | Current output includes Article 74, Article 75, Article 78, and Article 10. | Weak / partially correct. | Add/boost Article 15 for cybersecurity/access control. Keep Article 10 if candidate data handling is central. Down-rank market surveillance articles 74/75. |
| NFR-5 | The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds. | Employment/recruitment high-risk AI. | Risk management, data governance, accuracy/robustness, post-market monitoring. | Article 9 risk management; Article 10 data governance; Article 15 accuracy/robustness; Article 72 post-market monitoring if deployed system monitoring is in scope. | Current output maps to Article 72, Article 10, and testing provisions. | Partially correct. | Keep Article 72 as useful if deployment monitoring is in scope, but boost Article 9/10/15 because the requirement mentions accuracy, bias, and data quality thresholds. |
| NFR-6 | The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks. | Employment/recruitment high-risk AI. | Robustness, risk management, corrective action, post-market monitoring. | Article 15 accuracy/robustness/cybersecurity; Article 9 risk management; Article 72 post-market monitoring; Article 26 if deployer operation/monitoring is involved. | Current output includes Article 43, Article 15, Article 72, Article 52, Article 26. | Partially correct. | Keep Article 15 and Article 72. Boost Article 9. Down-rank Article 43/52 unless the requirement is specifically about conformity procedure. |

## Main issues found from current output

1. **Administrative articles are often ranked too highly.**
   Articles such as 113, 112, 92, 93, 81, 79, 28, and 31 appear in places where the requirement is really about transparency, human oversight, data governance, or record-keeping.

2. **The system needs stronger system-level high-risk context.**
   For this sample SRS, the whole application is an AI recruitment screening system, so Annex III employment/recruitment should be used as context for most requirements.

3. **Semantic similarity alone is not enough.**
   Some legal paragraphs share similar words like “review”, “application”, “decision”, or “assessment”, but they are not the right legal function for requirement-level analysis.

4. **The report should separate risks from safeguards.**
   Some requirements already provide controls, such as human override, logging, audit records, or preventing biometrics. These should be reported as controls or partial mitigations, not only as missing risks.

5. **The report needs obligation labels.**
   Each result should be labelled with a category such as data governance, transparency, human oversight, record-keeping, risk management, or accuracy/robustness/cybersecurity.

## Suggested implementation improvements

### 1. Add Chapter 3 relevance boosting

Prioritise:

- Article 6 and Annex III for high-risk classification.
- Articles 8-15 for the main high-risk AI requirements.
- Articles 16-27 for provider/deployer responsibilities.
- Article 72/73 only when monitoring or incident reporting is involved.
- Article 49 only when registration is specifically relevant.

Down-rank unless directly relevant:

- Article 113 entry/application.
- Article 112 evaluation/review of the regulation.
- Article 92/93 Commission/authority powers.
- Article 81/79 safeguard/market procedure.
- Article 28-39 notified body provisions.
- Article 43 conformity assessment, unless conformity is specifically mentioned.

### 2. Add domain trigger rules

For this SRS, terms like “candidate”, “recruiter”, “job requirements”, “application”, “screening”, “ranking”, and “suitability score” should trigger the employment/recruitment high-risk context.

### 3. Add obligation category labels

Suggested labels:

- `high_risk_classification`
- `data_governance`
- `transparency`
- `human_oversight`
- `record_keeping`
- `technical_documentation`
- `risk_management`
- `accuracy_robustness_cybersecurity`
- `provider_obligation`
- `deployer_obligation`
- `post_market_monitoring`
- `safeguard_or_control`

### 4. Mark safeguards differently from risk gaps

Example:

- FR-6 should not simply be “human oversight risk”. It should be “human oversight is addressed, but reviewer authority/training/logging may need to be specified.”
- FR-9 should not be treated as use of biometrics. It is a safeguard preventing biometric/emotion-recognition use.

### 5. Add a “Suggested engineering action” field

Using the agile guideline paper idea, each mapped risk could include a practical software engineering action.

Examples:

| Obligation category | Suggested engineering action |
|---|---|
| Data governance | Add dataset validation and bias-check acceptance criteria. |
| Transparency | Add explanation/instruction requirements for recruiters and affected users. |
| Human oversight | Add human review/override criteria to the Definition of Done. |
| Record-keeping | Add logging and audit-trail requirements. |
| Accuracy/robustness | Add threshold-based testing and monitoring alerts. |
| Risk management | Add risk review during sprint review/backlog refinement. |

## Recommended next step

Use this validation table as a small manual gold-standard set. Run the current pipeline against the sample SRS, compare the generated report to the expected mapping column, and record each output as correct, partially correct, weak, missing, or false positive. This gives the team a concrete way to evaluate and improve the risk assessment pipeline before final demonstration.
