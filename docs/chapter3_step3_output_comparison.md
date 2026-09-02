# Chapter 3 Step 3 Output Comparison

## Purpose

This document compares the current generated risk report (`risk-assessment-non-agent.md`) against the manual Chapter 3 expected mapping set. The goal is to check whether the system is mapping recruitment-screening requirements to the most useful EU AI Act provisions, especially Annex III employment context and Articles 8-15.

This is not a legal conclusion. It is a validation step for improving the prototype output.

## Overall finding

The current report is useful and often identifies the correct general risk area, but it still needs tuning. The strongest outputs are for data governance, human oversight, transparency, and record-keeping requirements. The weaker outputs are where the system overuses administrative/procedural articles, misses system-level Annex III employment context, or treats safeguards as if they are missing risks.

## Comparison table

| Requirement ID | Requirement focus | Expected mapping | Current system output | Assessment | Notes / suggested fix |
|---|---|---|---|---|---|
| FR-1 | Resume/application ingestion | Art 10 data governance; Art 11 documentation/security context; Annex III employment as system context | Art 10, 9, 13, 27 | Partially correct / overstated | It finds relevant Chapter 3 obligations, but generic ingestion alone should not be treated as a high legal risk unless the requirement mentions data quality, sensitive data, protected data, or automated processing. Consider lowering severity and making Article 27 conditional. |
| FR-2 | Suitability scoring | Annex III employment; Art 10 data governance; Art 13 transparency; Art 14 human oversight; Art 15 accuracy | Art 13, 14, 27 | Partially correct | Good matches for transparency and human oversight. Missing Article 10/data governance and Article 15/accuracy, which are important for scoring based on candidate data. Article 27 may be secondary rather than core requirement-level mapping. |
| FR-3 | Candidate ranking | Annex III employment; Art 13 transparency; Art 14 human oversight; Art 15 accuracy/robustness; Art 6 classification context | Art 50, 14, 27, 72 | Partially correct with noise | Article 14 is useful. Article 50 is less useful than Article 13 for high-risk deployer transparency. Missing Annex III employment context and Article 15. Article 72 should be secondary unless monitoring after deployment is being assessed. |
| FR-4 | Explain factors influencing suitability score | Art 13 transparency; Art 11 documentation where applicable; Annex III employment context | Art 14 only | Weak / missing primary article | The main purpose is explainability/transparency, so Article 13 should be the primary mapping. Article 14 may be a related follow-up, but the current output misses the core transparency obligation. |
| FR-5 | Notify recruiters automated model was used | Art 13 transparency/information to deployers; Article 26 may be secondary | Art 13(3) | Correct | Good match. The report correctly identifies this as a transparency/information issue. Could also label the obligation category as transparency. |
| FR-6 | Human recruiter review/override before removal | Art 14 human oversight; Article 26 deployer responsibility; Annex III employment context | Art 14(4), 14(3) | Mostly correct | Good output. The system correctly maps to human oversight. Suggested refinement: mark this as a safeguard/partial control, not simply a missing risk; remaining risk is whether recruiter training, authority, and oversight process are specified. |
| FR-7 | Log scores, rankings, explanations, overrides, final decisions | Art 12 record-keeping/logging; Art 19 generated logs; Art 11 documentation where traceability evidence is needed | Art 12(3) | Partially correct | Correct category, but Article 12(3) is a very specific logging provision and may not fit general recruitment logging. Article 12(2) is more useful for traceability in this context; Article 19 could also be useful. |
| FR-8 | Retain audit records for screening decisions | Art 12 record-keeping; Art 11 technical documentation; Art 18 documentation retention may be relevant | Art 12(3), 12(2) | Mostly correct with minor noise | Good mapping to Article 12, especially Article 12(2). Article 12(3) may be too specific unless biometrics/search databases are involved. Could add documentation/retention labels. |
| FR-9 | Prevent facial recognition, biometric ID, or emotion recognition | Article 5 prohibited practices/sensitive use safeguards; Annex III biometrics as warning category; safeguard/control label | Art 5(4), 50(3), 5(7) | Partially correct but misframed | It correctly identifies biometric/emotion-recognition relevance, but it treats the requirement like the system uses these technologies. The requirement is actually a safeguard preventing them. Article 5(4)/(7) are likely too specific to law enforcement/public-space biometric contexts. |
| FR-10 | Candidate channel to request review | Art 14 human oversight; Art 13 transparency; Article 26 deployer process may be relevant | Art 14(1), 14(4) | Mostly correct | Good mapping to human oversight. Could be improved by adding transparency/process handling and marking it as a candidate-facing review safeguard rather than only a risk gap. |
| NFR-1 | Validate training/evaluation datasets | Art 10 data governance/data quality; Art 15 if validation affects accuracy/robustness | Art 10(2) | Correct | Good match. Article 10 is the right primary mapping. Could optionally include Article 15 as a secondary link if model quality/performance is discussed. |
| NFR-2 | Measure performance across demographic groups | Art 10 data governance/bias; Art 15 accuracy/robustness; Art 9 risk management | Art 10(2) | Partially correct | Correct primary mapping to Article 10. Missing Article 15 and possibly Article 9, because the requirement is also about performance monitoring and fairness risk. |
| NFR-3 | Do not use protected attributes as ranking inputs | Art 10 data governance/bias control; Article 5 may be relevant if prohibited discrimination/social scoring is implicated; safeguard/control label | Art 5(1) | Partially correct | Article 5 can be relevant, but the main requirement-level issue is data governance and bias control under Article 10. The output should treat this as a safeguard/control, not only a prohibited-practice risk. |
| NFR-4 | Access controls for authorised recruitment staff | Art 15 cybersecurity/access control; Art 10 data governance; possibly confidentiality secondary | Art 74(12), 74(13) | Incorrect / false positive | Current output focuses on market surveillance authority access to documentation/source code, which is not the main issue. This requirement is about internal access control, so Article 15 cybersecurity and Article 10 data governance are more relevant. |
| NFR-5 | Monitoring alerts for accuracy, bias, data quality thresholds | Art 9 risk management; Art 10 data governance; Art 15 accuracy/robustness; Art 72 if deployed monitoring is in scope | Art 72(3) | Partially correct | Article 72 is useful for post-market monitoring, but the output misses the more direct Chapter 3 obligations: Article 9, Article 10, and Article 15. |
| NFR-6 | Rollback if model fails safety, robustness, or fairness checks | Art 15 robustness/fail-safe; Art 9 risk management; Art 72 monitoring; Article 26 if deployer operation is involved; Article 43 secondary only if substantial modification/conformity is in scope | Art 43(4), 15(4) | Partially correct | Article 15 is a strong match. Article 43 may be legally relevant later, but it should not dominate unless conformity assessment or substantial modification is explicitly in scope. Add Article 9 and Article 72 as stronger system operation mappings. |


## Main issues identified

### 1. System-level Annex III employment context is missing

For this sample SRS, the overall system is a recruitment-screening tool. The report should consistently keep Annex III employment/recruitment as system-level context, especially for requirements about candidate scoring, ranking, screening, and recruiter decision-making.

### 2. Some core Articles 8-15 are missed

The system often finds one useful article but misses another core obligation. For example, scoring and ranking requirements should usually consider data governance, transparency, human oversight, and accuracy together, not only one article.

### 3. Some administrative or later-stage articles are overused

The current output sometimes uses provisions that are more relevant to regulators, market surveillance, conformity assessment, or post-market procedure. These may be legally related, but they are not always useful for early requirement-level analysis.

Examples to down-rank unless directly relevant:
- Article 43 conformity assessment
- Article 72 post-market monitoring, unless deployment monitoring is in scope
- Article 74 market surveillance authority access
- Article 27 fundamental rights impact assessment, unless deployer context is clearly in scope
- Article 50, where Article 13 is the more direct Chapter 3 transparency article

### 4. Safeguards should be labelled differently from gaps

Some requirements already introduce controls, such as human override, logging, audit records, and preventing biometric/emotion-recognition use. The report should not always treat these as missing-risk gaps. It should identify them as safeguards or partial mitigations, then explain what details are still missing.

### 5. Some sub-articles are too specific

The report sometimes uses Article 12(3), which is specific to certain Annex III biometric identification systems. For a recruitment-screening system, Article 12(2) is generally more useful for logging/traceability unless biometrics are actually involved.

## Suggested implementation improvements

### Add obligation category labels

Each finding should include a label such as:

- `high_risk_classification`
- `data_governance`
- `transparency`
- `human_oversight`
- `record_keeping`
- `technical_documentation`
- `risk_management`
- `accuracy_robustness_cybersecurity`
- `post_market_monitoring`
- `safeguard_or_control`

### Add Chapter 3 relevance boosting

Prioritise:

- Article 6 and Annex III for high-risk classification
- Articles 8-15 for the core high-risk requirements
- Articles 16-27 for provider/deployer obligations where responsibility matters

Down-rank unless directly relevant:

- notified body/admin provisions
- market surveillance authority provisions
- conformity assessment articles
- general evaluation/review articles
- entry/application articles

### Add recruitment-domain trigger rules

Terms such as candidate, recruiter, job requirements, application, screening, ranking, suitability score, and candidate removal should trigger the employment/recruitment high-risk context.

### Add safeguard detection

If a requirement says it provides a control, the report should mark it as a safeguard and then identify remaining gaps. For example:

- FR-6 should be: human oversight is addressed, but reviewer training/authority/process may need to be specified.
- FR-9 should be: biometric/emotion-recognition use is prohibited by the requirement, so this is a safeguard, not evidence that the system uses biometrics.

## Recommended next step

Use this comparison to tune the retrieval/risk assessment layer, then re-run the report and record whether the mappings improve. The most useful improvement would be adding Chapter 3 obligation labels and relevance boosting before the LLM produces the final risk explanation.
