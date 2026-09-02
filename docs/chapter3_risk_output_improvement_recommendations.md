# Chapter 3 Risk Output Improvement Recommendations

## Purpose

This document summarises the main issues found after comparing the current generated risk report against the manual Chapter 3 expected-mapping set. The aim is to improve the quality of the prototype's risk assessment output so that it maps software requirements to the most relevant EU AI Act provisions, especially for a recruitment-screening use case.

The focus is not to make final legal conclusions. The focus is to make the output more accurate, traceable, and useful as an engineering review aid.

## Top 5 issues found

### 1. System-level Annex III employment context is not being used consistently

The sample SRS is clearly based on an AI recruitment-screening system. Because of this, the generated report should consistently keep Annex III employment/recruitment as the system-level high-risk context, especially for requirements about candidate scoring, ranking, screening, recruiter review, and candidate removal.

At the moment, some requirements are assessed individually without enough system context. This can cause the report to miss the bigger classification issue: the system is likely operating in a high-risk employment/recruitment domain.

### 2. Core Chapter 3 obligations are sometimes missed

The current report often identifies one useful article, but misses other important Articles 8-15 obligations that should usually be considered together.

For example, requirements about suitability scoring and candidate ranking should not only be mapped to transparency or human oversight. They should also consider data governance and accuracy/robustness because the model is using candidate data to generate scores that affect recruitment decisions.

The key obligation categories that should appear more consistently are:

- risk management
- data governance
- transparency
- human oversight
- record-keeping/logging
- accuracy, robustness, and cybersecurity

### 3. Some administrative or later-stage articles are overused

The generated report sometimes includes articles that are legally related but less useful for early requirements-level analysis. These include provisions about market surveillance, conformity assessment, post-market monitoring, or broader regulatory procedures.

These articles should not be removed completely, but they should be down-ranked unless the requirement directly relates to that topic. For example, Article 43 may be relevant if the requirement is about conformity assessment or substantial modification, but it should not dominate a simple rollback or model-control requirement. Similarly, Article 74 is about market surveillance authority access and is not the best match for an internal staff access-control requirement.

### 4. Safeguards are sometimes treated as missing risks

Some requirements already describe controls or mitigations, such as human override, logging, audit records, candidate review channels, and preventing biometric/emotion-recognition use.

The report should not only frame these as missing risks. Instead, it should recognise that the requirement is already trying to address a risk, then identify what details are still missing.

For example:

- A human override requirement should be labelled as a human oversight safeguard, with remaining gaps such as reviewer training, authority, and process documentation.
- A requirement preventing biometric or emotion-recognition use should be labelled as a safeguard, not as evidence that the system actually uses biometrics.

### 5. Some sub-article matches are too specific for the requirement

The report sometimes uses very specific sub-articles where a broader obligation would be more useful. For example, Article 12(3) is specific to certain high-risk biometric identification systems, so it may not be the best primary match for a general recruitment logging requirement unless biometric identification is actually involved.

For general logging and traceability, Article 12(2) is often more useful because it focuses on recording events relevant to risk identification, monitoring, and operation of high-risk AI systems.

## Recommended improvements

### 1. Add Chapter 3 relevance boosting

The retrieval/risk assessment layer should prioritise the most relevant Chapter 3 provisions for requirements-level analysis.

Recommended boosts:

- Article 6 and Annex III for high-risk classification
- Articles 8-15 for core high-risk AI requirements
- Articles 16-27 where provider/deployer responsibility matters
- Article 72 only when post-deployment monitoring is directly relevant
- Article 43 only when conformity assessment or substantial modification is directly relevant

Recommended down-rank unless directly relevant:

- notified body/admin provisions
- market surveillance authority provisions
- general evaluation/review articles
- entry/application articles
- conformity assessment articles when the requirement is not about conformity

### 2. Add recruitment-domain trigger rules

The system should detect when the SRS belongs to an employment/recruitment context. Terms such as the following should trigger Annex III employment/recruitment context:

- candidate
- recruiter
- job requirements
- application
- screening
- ranking
- suitability score
- candidate removal
- review before removal

This context should then be carried through the report so the system does not assess each requirement in isolation.

### 3. Add obligation category labels

Each output should include an obligation category label. This would make the report easier to evaluate and easier for developers to understand.

Suggested labels:

- `high_risk_classification`
- `risk_management`
- `data_governance`
- `transparency`
- `human_oversight`
- `record_keeping`
- `technical_documentation`
- `accuracy_robustness_cybersecurity`
- `provider_obligation`
- `deployer_obligation`
- `post_market_monitoring`
- `safeguard_or_control`

### 4. Add safeguard/control detection

The report should separate actual risk gaps from requirements that already act as safeguards.

Recommended output structure:

```text
Requirement -> EU AI Act provision -> Risk or safeguard -> Remaining gap -> Suggested action
```

This would make the report more balanced. It would avoid overstating risk where the requirement already includes a control, while still identifying details that need to be clarified.

### 5. Add practical engineering actions

The agile guideline research can be used as an optional actionability layer. Once a requirement is mapped to an obligation category, the report could suggest a practical software engineering action.

Examples:

| Obligation category | Suggested engineering action |
|---|---|
| Data governance | Add dataset validation, bias checks, and data origin documentation. |
| Transparency | Add explanation/instruction requirements for recruiters and affected users. |
| Human oversight | Add human review and override criteria to the Definition of Done. |
| Record-keeping | Add logging and audit-trail requirements. |
| Accuracy/robustness | Add performance thresholds and monitoring alerts. |
| Risk management | Add risk review during sprint review or backlog refinement. |

## Recommended next step

The next step is to apply these changes to the retrieval/risk assessment layer, regenerate the risk report, and compare the new output against the manual Chapter 3 validation set.

The main success criteria should be:

1. Fewer irrelevant/admin article matches.
2. More consistent Annex III employment context.
3. Better coverage of Articles 8-15.
4. Clear obligation category labels.
5. Safeguards recognised as controls, not only missing risks.
6. More useful recommendations for software engineers.

## Summary

The current risk report is a useful starting point and already identifies several relevant areas, especially transparency, human oversight, data governance, and record-keeping. However, it needs stronger Chapter 3 prioritisation and clearer output structure to make the results more reliable. The highest-impact improvement would be to add domain triggers, obligation labels, relevance boosting, and safeguard detection before generating the final risk explanation.
