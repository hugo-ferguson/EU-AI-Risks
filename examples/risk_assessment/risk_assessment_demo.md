# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 1

### Overall analysis

Overall, the assessment reviewed 1 requirements and rated 1 as high risk. The main review focus areas are accuracy robustness cybersecurity, data governance, human oversight, risk management and transparency. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 1 requirements reviewed in total.
- Risk distribution: 1 high, 0 medium, 0 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (1), data governance (1), human oversight (1), risk management (1), transparency (1).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-1

**Risk level:** high

**Requirement:** . The system can rank job candidates’ applicability based on their job application

**Classified as:** Annex III point 4(a) (annex:III:4:a): (a) AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9)

**Analysis:** FR-1 specifies candidate ranking with no accuracy metrics, bias examination, oversight or transparency to deployers. Without these, rankings could discriminate or be over-relied on in recruitment decisions, and the system could not pass conformity assessment as specified.

**Risks:**

- The ranking function states no accuracy level or metrics, so ranking quality cannot be tested or declared in the instructions for use. [high] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define ranking accuracy and robustness metrics (e.g., rank correlation against expert ratings, per-group performance) with target thresholds, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Ranking candidates from application data without any bias examination or mitigation risks discriminatory outcomes against protected groups. [high] - Article 10(2)(f) (`art:10:p2:f`)
  - Category: `data_governance`
  - Action: Add requirements for bias examination of the training, validation and testing data and of ranking outputs, for bias detection and mitigation, and for excluding protected attributes and their proxies.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- FR-1 gives recruiters no means to interpret, override or disregard rankings, which invites automation bias in candidate selection. [high] - Article 14(4)(d) (`art:14:p4:d`)
  - Category: `human_oversight`
  - Action: Specify that rankings are advisory. Provide an interface where reviewers can see ranking factors, override or reverse rankings, and stop use of the system. Include automation-bias warnings.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The ranking output has no specified explanation or interpretability, so deployers cannot interpret it and use it appropriately. [medium] - Article 13(1) (`art:13:p1`)
  - Category: `transparency`
  - Action: Require that each ranking carries the key contributing criteria and a score. Document the ranking logic, limitations and intended use in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- No risk management process covers the fundamental-rights risks of ranking applicants, such as discrimination and unfair exclusion. [medium] - Article 9(2)(a) (`art:9:p2:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `risk_management`
  - Action: Establish a documented risk management process covering ranking risks, with pre-defined test metrics and thresholds, residual-risk acceptance and post-deployment review.
  - Trace:
    - referenced by Article 13(3) (Article 9(2))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.
- **Risk management system, Article 9(2)(a)**
  > (a) the identification and analysis of the known and the reasonably foreseeable risks that the high-risk AI system can pose to health, safety or fundamental rights when the high-risk AI system is used in accordance with its intended purpose;

**Recommendations:**

- Define and declare ranking accuracy metrics and thresholds, and robustness targets.
- Add bias examination, detection and mitigation requirements for the data and the ranking outputs.
- Make rankings advisory, with reviewer override, interpretation support and stop capability.
- Provide per-candidate ranking explanations and document the ranking logic in the instructions for use.
- Establish a lifecycle risk management process for the ranking function.

---
