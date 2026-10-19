# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 2
- Medium: 8

### Overall analysis

Overall, the assessment reviewed 10 requirements and rated 2 as high risk and 8 as medium risk. The main review focus areas are accuracy robustness cybersecurity, transparency, human oversight, record keeping and data governance. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 10 requirements reviewed in total.
- Risk distribution: 2 high, 8 medium, 0 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (9), transparency (7), human oversight (6), record keeping (4), data governance (3).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** medium

**Requirement:** The system shall allow an authenticated applicant to submit a child benefit application containing household details, including the applicant’s identity, each child’s date of birth and relationship to the applicant, and each adult household member’s details.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14)

**Analysis:** FR-01 is an input-collection requirement. Validation (FR-02), verification (FR-03), audit logging and access control (FR-10) and human review (FR-07) are covered elsewhere. The remaining gap is that nothing states that applicants are told an AI system is used in their application, which matters because this is a high-risk Annex III 5(a) system.

**Risks:**

- The submission flow does not tell applicants that the application will be assessed with a high-risk AI system. FR-08 notifies applicants only after the decision, so they are not informed at the point of data submission. [medium] - Article 26(11) (`art:26:p11`)
  - Partly addressed by: FR-08 (informs the applicant of the decision outcome and the right to appeal after the decision, not that an AI system is used)
  - Category: `transparency`
  - Action: Add an AI-use notice to the application submission step, shown before or at submission and recorded with the application. It should state that an AI model supports eligibility and amount decisions, that human review is available, and how to request it.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The data collected is not tied to the model's input specification or to a check that it is relevant and representative. This includes the household and adult-member fields and the relationship and custody values. Input structure and coverage of household types (for example, shared custody or non-standard households) are not defined. [low] - Article 26(4) (`art:26:p4`)
  - Partly addressed by: FR-02 (validates income inputs for completeness and range, but not household details); FR-03 (verifies identity and family composition against external records)
  - Category: `data_governance`
  - Action: Define the structured input schema, with controlled values for relationship and household types. Document that the fields are relevant to the eligibility purpose. Monitor submitted inputs for coverage across household types.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Obligations of deployers of high-risk AI systems, Article 26(4)**
  > 4. Without prejudice to paragraphs 1 and 2, to the extent the deployer exercises control over the input data, that deployer shall ensure that input data is relevant and sufficiently representative in view of the intended purpose of the high-risk AI system.

**Recommendations:**

- Add an AI-use notice to the application submission step and store a record of it.
- Define a controlled input schema for household details and monitor input coverage across household types.

---

### FR-02

**Risk level:** medium

**Requirement:** The system shall collect and validate income data for all relevant household members, including income source, amount, and assessment period, and shall reject or flag incomplete, inconsistent, or out-of-range values before processing.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 9 Risk management system (art:9)

**Analysis:** FR-02 is an input-validation control that already supports data quality, but it does not state how rejected or flagged records are handled or how validation rules are governed. It also does not say how input data is kept representative and accurate for the eligibility model. The remaining gaps are mostly clarifications, with a possible gap on input integrity.

**Risks:**

- Validation rules (range limits, consistency checks, assessment-period rules) are not specified or documented as data governance practices. Flagging and rejection outcomes are not tied to data-preparation or error-handling procedures, and there is no check for systematic exclusion of household types such as irregular or self-employed income. [medium] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: FR-03 (cross-checks submitted income against authorised external records and flags discrepancies (partial support for error-free, complete data under 10(3)))
  - Category: `data_governance`
  - Action: Define and version-control validation rules (ranges, cross-field consistency, period rules). Document the rejection/flagging procedures and monitor rejection rates by household type to detect bias or unrepresentative data.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The requirement does not define what happens to flagged or inconsistent income data, such as who resolves it, whether processing is blocked, or how users are informed. Erroneous inputs could still reach the model and produce wrong benefit outcomes. [low] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-07 (routes applications with detected data discrepancies to a human caseworker)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: State that flagged records are blocked from automated processing until resolved. Define the resolution workflow and notify the applicant of the specific field to correct.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

**Recommendations:**

- Specify validation rules as versioned, documented data governance artefacts and monitor rejection/flag rates across household groups for bias or unrepresentative data.
- Define in FR-02 that flagged or inconsistent income data blocks automated processing until it is resolved, with the resolution workflow and applicant notification.

---

### FR-03

**Risk level:** medium

**Requirement:** The system shall verify submitted identity, income, and family composition information against authorised external records (e.g., tax authority, civil registry, employer records) where available, and shall flag discrepancies for review.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-03 verifies submitted data against external records and flags discrepancies, and FR-07 routes discrepancies to a caseworker. Remaining gaps: it does not address the accuracy and integrity of the external-record inputs or how verification errors and unavailable sources are handled.

**Risks:**

- The requirement does not address errors, stale data, mismatches or unavailability in external records. Verification relies on 'where available' with no defined fallback or fail-safe, so wrong or missing external data could lead to wrongly flagged or wrongly approved applications. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-07 (routes applications with detected data discrepancies to a human caseworker)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify behaviour when external sources are unavailable, stale or conflicting (e.g., fail-safe to manual review, no automatic rejection on a failed lookup). Define record-matching rules, data freshness limits and an error-handling path.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not state integrity or authenticity controls for the external record interfaces. Tampered or spoofed responses from tax, civil registry or employer sources could manipulate eligibility inputs. [medium] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require authenticated, encrypted channels to authorised sources, response integrity validation, and input sanitisation. Add anomaly detection on external responses.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not say that discrepancy flags and verification outcomes are presented to caseworkers with enough context (source, mismatch detail, data reliability). Reviewers may not be able to interpret the flags or may over-rely on external records as authoritative. [low] - Article 14(4)(c) (`art:14:p4:c`)
  - Partly addressed by: FR-07 (caseworker review, confirm, amend or override with recorded justification)
  - Category: `human_oversight`
  - Action: State that each flag shows the submitted value, the external value, the source, the retrieval date and the discrepancy type. Allow caseworkers to resolve a discrepancy in favour of the applicant with a recorded reason.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight (closest match: Article 14(4)(c))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Human oversight, Article 14(4)(c)**
  > (c) to correctly interpret the high-risk AI system’s output, taking into account, for example, the interpretation tools and methods available;

**Recommendations:**

- Define fallback, freshness and error-handling rules for unavailable, stale or conflicting external records, with routing to manual review.
- Add authentication, encryption and integrity validation for all external record integrations.
- Specify the discrepancy flag content (submitted vs. external value, source, date) shown to caseworkers so they can interpret it.

---

### FR-04

**Risk level:** medium

**Requirement:** The system shall determine family composition eligibility by applying configurable rules, including child age limits, dependency status, custody or residency arrangements, and the number of eligible children.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 9 Risk management system (art:9); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-04 applies configurable rules to decide family composition eligibility (child age, dependency, custody/residency) but sets no accuracy or rule-testing targets and no controls on rule configuration changes. It also does not consider edge cases affecting children and vulnerable households, so errors could wrongly deny or reduce benefits.

**Risks:**

- No accuracy or correctness criteria or pre-defined test metrics are specified for the family-composition rule logic (age limits, dependency, custody/residency, child count), so rule errors affecting eligibility cannot be measured or declared. [medium] - Article 15(1) (`art:15:p1`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics and acceptance thresholds for rule outcomes (e.g. test suites of edge cases per rule type), run them before release and after each rule change, and declare the metrics in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Rules are 'configurable' with no stated protection against unauthorised or erroneous changes, or validation of configurations, so altered rules could change eligibility outcomes undetected. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-10 (records rule versions in the audit log, supporting detection of configuration changes (not prevention or validation))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Require role-based access, four-eyes approval, schema/consistency validation, versioning and rollback for rule configuration changes, and test against regression cases before activation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Complex custody, shared residency and dependency situations may be handled inconsistently or discriminate against particular family types and vulnerable households, and the requirement does not address how such cases are identified, tested or handled. [medium] - Article 9(9) (`art:9:p9`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-07 (routes data discrepancies and low-confidence cases to human review (not rule-specific edge cases))
  - Category: `risk_management`
  - Action: Document foreseeable risks for rule edge cases (shared custody, foster/kinship care, cross-border residency) and their impact on children; add test scenarios for these cases and a default route to caseworker review for ambiguous situations.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Risk management system, Article 9(9)**
  > 9. When implementing the risk management system as provided for in paragraphs 1 to 7, providers shall give consideration to whether in view of its intended purpose the high-risk AI system is likely to have an adverse impact on persons under the age of 18 and, as appropriate, other vulnerable groups.

**Recommendations:**

- Define and declare accuracy metrics and acceptance thresholds for the family composition rules, with edge-case regression tests.
- Add access control, validation, approval and rollback for rule configuration changes.
- Add a risk analysis and tests for complex custody/residency/dependency cases, with automatic caseworker referral for ambiguous situations.

---

### FR-05

**Risk level:** high

**Requirement:** The system shall use an AI model, in combination with configurable policy rules, to calculate whether the household meets the income-based eligibility criteria and to compute the benefit amount payable per child and in total, adjusting for income thresholds, tapering, and family size.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 9 Risk management system (art:9)

**Analysis:** FR-05 computes eligibility and benefit amounts with an AI model plus policy rules, but it declares no accuracy metrics or thresholds, no robustness or feedback-loop controls, and no data governance or bias controls for the model. Without these, benefit amounts could be wrong or biased and the system could not show Article 15 and 10 conformity.

**Risks:**

- No accuracy level or metrics are specified for the AI eligibility and benefit-amount calculation, such as error tolerance versus the deterministic policy rules, or acceptance thresholds. The levels therefore cannot be declared in the instructions for use or tested against predefined metrics. [high] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define accuracy metrics for eligibility classification and amount error (e.g. misclassification rate, maximum absolute and relative amount deviation versus the reference rule calculation). Set acceptance thresholds, test against them before release, and declare them in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- The requirement does not define how the AI model and policy rules are combined or how conflicts between them are resolved, nor fail-safe behaviour for model errors or faults. Calculation errors could silently affect payments. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-07 (fallback to human review when AI confidence is low or data discrepancies are detected (partial robustness measure)); FR-02 (rejects or flags inconsistent input values before processing (resilience to input errors))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Specify rule-versus-model precedence, deterministic cross-checks of the computed amount against the policy formula, and a fail-safe that routes to manual calculation on faults or inconsistent outputs. If the model keeps learning, add feedback-loop safeguards.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- No data governance is specified for the data used to train, validate and test the eligibility and amount model, including representativeness and bias examination across household types, family sizes and income groups. This risks discriminatory or erroneous outcomes for benefit recipients. [medium] - Article 10(2)(f) (`art:10:p2:f`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `data_governance`
  - Action: Document the training, validation and test data, including origin and representativeness. Run bias tests by household composition and income band, define mitigation measures and acceptance criteria, and record them in the technical documentation.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- The model's computation of eligibility and amounts is not required to be interpretable by caseworkers, for example through the factors that drove the model output versus the rule output. This limits their ability to interpret and verify results. [low] - Article 13(1) (`art:13:p1`)
  - Partly addressed by: FR-06 (explanation of input data, rules and factors behind each decision and calculation (partly supports interpretation of output))
  - Category: `transparency`
  - Action: Require the calculation to expose per-factor contributions and a rule-versus-model breakdown to caseworkers. Document the model's limitations and its interpretation tools in the instructions for use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Data and data governance, Article 10(2)(f)**
  > (f) examination in view of possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law, especially where data outputs influence inputs for future operations;
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- Define and declare accuracy metrics and acceptance thresholds for eligibility and benefit amount outputs, and test against them before release.
- Specify rule-versus-model precedence, deterministic cross-checks and a fail-safe fallback for calculation faults.
- Establish documented data governance and bias testing, with mitigation, for the model's training, validation and test data.
- Expose per-factor contributions and a rule-versus-model breakdown to caseworkers, and document model limitations in the instructions for use.

---

### FR-06

**Risk level:** medium

**Requirement:** The system shall provide an explanation for every eligibility decision and payment calculation, listing the input data, rules, and factors that influenced the outcome, in language understandable to the applicant.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 13 Transparency and provision of information to deployers (art:13); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 14 Human oversight (art:14); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-06 largely implements the applicant-facing explanation (Art. 86), but it does not state that the explanation covers the AI system's role in the decision, and it does not require the system to give caseworkers interpretable output (Art. 13/14). Without these, affected persons may get explanations that omit AI involvement, and caseworkers may not be able to interpret the AI output.

**Risks:**

- The explanation must list inputs, rules and factors, but it need not state the role of the AI model versus the policy rules and caseworker, which Art. 86(1) requires. This may leave applicants without a clear account of how the AI contributed or whether a human reviewed or overrode the outcome. [medium] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-08 (notifies the applicant of the outcome, the amount and the right to appeal (the decision itself, not the AI's role))
  - Category: `transparency`
  - Action: Require each explanation to state whether the AI model was used, how it influenced the result alongside the rules, and whether a caseworker confirmed, amended or overrode it (using the FR-07 record). Also state the main elements of the decision in plain language.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- The requirement targets applicants only. It does not require the system to give deployer staff and caseworkers output-interpretation information, such as factor attribution and confidence, so they can interpret and appropriately use the AI output. [medium] - Article 13(1) (`art:13:p1`)
  - Partly addressed by: FR-07 (routes low-confidence cases to caseworkers for confirmation or override, but does not make the AI output interpretable)
  - Category: `transparency`
  - Action: Add a caseworker-facing explanation view showing per-decision feature or rule contributions, model confidence and known limitations. Document these explanation capabilities in the instructions for use (Art. 13(3)(b)(iv)).
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 13 Transparency and provision of information to deployers
- The requirement does not specify that factor-level explanations must be faithful to the AI model's actual computation, nor does it set accessibility or format criteria. This leaves it unclear whether the explanations are accurate and meaningful for applicants. [low] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-10 (logs inputs, AI outputs and rule versions that explanations can be derived from)
  - Category: `transparency`
  - Action: Define acceptance criteria: the explanation must be generated from the logged decision inputs and rule versions (FR-10), tested for fidelity and comprehensibility with users, and available in accessible formats and the applicant's language.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making

**Cited provisions:**

- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Transparency and provision of information to deployers, Article 13(1)**
  > 1. High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system’s output and use it appropriately. An appropriate type and degree of transparency shall be ensured with a view to achieving compliance with the relevant obligations of the provider and deployer set out in Section 3.

**Recommendations:**

- State the AI model's role and any human review or override in every explanation.
- Provide caseworkers with interpretable per-decision output (factor contributions, confidence, limitations) and document it in the instructions for use.
- Define fidelity, comprehensibility and accessibility acceptance criteria, and generate explanations from the logged inputs and rule versions.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall automatically route applications to a human caseworker for review when the AI’s confidence is below a configurable threshold, when data discrepancies are detected, or when the applicant requests a manual review, and shall allow caseworkers to confirm, amend, or override AI decisions with a recorded justification.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12); Article 86 Right to explanation of individual decision-making (art:86); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-07 provides routing to caseworkers and confirm/amend/override with justification, which is a solid oversight control. Remaining gaps: the requirement does not address automation-bias awareness, reviewer competence/authority, or a stop/suspend capability. Art. 14(5) does not apply because it is scoped to Annex III 1(a), not 5(a).

**Risks:**

- No measures make reviewers aware of automation bias or help them interpret AI output (e.g. confidence display, factors) at the review step; routing is only triggered by low confidence, so high-confidence decisions may be auto-accepted without any oversight. [medium] - Article 14(4)(b) (`art:14:p4:b`)
  - Partly addressed by: FR-06 (explanation of input data, rules and factors influencing the outcome, supporting output interpretation (14(4)(c)))
  - Category: `human_oversight`
  - Action: Show caseworkers the confidence score, key factors and known model limitations in the review UI; add automation-bias guidance and periodic sampled review of high-confidence auto-decisions.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- No ability to halt or suspend AI-driven decisioning (stop button or equivalent safe-state procedure) is specified; oversight is limited to case-by-case override. [medium] - Article 14(4)(e) (`art:14:p4:e`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `human_oversight`
  - Action: Add an authorised-operator control to suspend automated eligibility decisions and route all cases to manual review in a safe state.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement does not state that reviewers must have the competence, training and authority to override, nor how the confidence threshold and discrepancy triggers are governed and validated as commensurate with risk. [low] - Article 26(2) (`art:26:p2`)
  - Category: `human_oversight`
  - Action: Define reviewer role permissions, training prerequisites and change control for the threshold configuration; document threshold rationale and review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems

**Cited provisions:**

- **Human oversight, Article 14(4)(b)**
  > (b) to remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (automation bias), in particular for high-risk AI systems used to provide information or recommendations for decisions to be taken by natural persons;
- **Human oversight, Article 14(4)(e)**
  > (e) to intervene in the operation of the high-risk AI system or interrupt the system through a ‘stop’ button or a similar procedure that allows the system to come to a halt in a safe state.
- **Obligations of deployers of high-risk AI systems, Article 26(2)**
  > 2. Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support.

**Recommendations:**

- Surface confidence, key factors and limitations to caseworkers, add automation-bias safeguards and sampling of high-confidence decisions.
- Add a suspend/stop capability for automated decisions that falls back to manual review.
- Specify reviewer role authority and training prerequisites, and govern and document the threshold configuration.

---

### FR-08

**Risk level:** high

**Requirement:** The system shall notify applicants of the decision outcome, the calculated benefit amount, and the right to appeal, and shall allow applicants to submit appeals or updated information that triggers recalculation.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 86 Right to explanation of individual decision-making (art:86); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 13 Transparency and provision of information to deployers (art:13); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 14 Human oversight (art:14)

**Analysis:** FR-08 notifies applicants of outcome, amount and appeal right, and supports appeals with recalculation. It does not state that applicants are told an AI system is used in the decision, and it gives no human review for appeals, which weakens deployer transparency toward affected persons.

**Risks:**

- The notification covers outcome, amount and appeal right but does not inform applicants that they are subject to a high-risk AI system used in making or assisting the decision. [high] - Article 26(11) (`art:26:p11`)
  - Category: `transparency`
  - Action: Add to the decision notification a clear statement that an AI system was used to assess eligibility and calculate the benefit, plus its role in the decision.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- The notification does not include or link to the explanation of the AI system's role and the main elements of the decision. FR-06 produces explanations, but FR-08 does not require delivering them with the decision or on request, so the Article 86 right is not clearly met when an applicant appeals. [medium] - Article 86(1) (`art:86:p1`)
  - Partly addressed by: FR-06 (explanation of input data, rules and factors influencing the eligibility and payment outcome, in language understandable to the applicant)
  - Category: `transparency`
  - Action: Require the decision notice to include the FR-06 explanation, covering the AI's role and main decision factors, or a link to it, and make it available in the appeal flow.
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Remedies > Article 86 Right to explanation of individual decision-making
- Appeals and updated information trigger recalculation, but the requirement does not guarantee that a competent human can review, disregard or override the AI output on appeal. FR-07 routes manual review requests to caseworkers, but FR-08 does not link appeals to that route. [low] - Article 14(4)(d) (`art:14:p4:d`)
  - Partly addressed by: FR-07 (routing on applicant request for manual review and caseworker ability to confirm, amend or override AI decisions with recorded justification)
  - Category: `human_oversight`
  - Action: State that every appeal is routed to a human caseworker through the FR-07 workflow, which can override the recalculated AI result, and that the notification says so.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(11)**
  > 11. Without prejudice to Article 50 of this Regulation, deployers of high-risk AI systems referred to in Annex III that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system. For high-risk AI systems used for law enforcement purposes Article 13 of Directive (EU) 2016/680 shall apply.
- **Right to explanation of individual decision-making, Article 86(1)**
  > 1. Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof, and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken.
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;

**Recommendations:**

- Add an explicit AI-use disclosure to the decision notification.
- Include the FR-06 explanation, covering the AI's role and main decision elements, in the notice and the appeal flow.
- Link appeals explicitly to FR-07 human caseworker review with override authority.

---

### FR-09

**Risk level:** medium

**Requirement:** The system shall recalculate eligibility and payment amounts when household circumstances change (e.g., income change, birth of a child, child reaching the age limit) or when policy thresholds are updated by an authorised administrator.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12); Article 9 Risk management system (art:9)

**Analysis:** FR-09 triggers automatic recalculation of eligibility and payment amounts, which can reduce or revoke benefits, but it specifies no accuracy or consistency checks, no human review of recalculated outcomes, and no change control over threshold updates. Erroneous or unauthorised changes could affect many households without detection.

**Risks:**

- Recalculation triggered by administrator threshold updates has no stated validation, testing against predefined metrics, or approval/versioning before it applies to existing cases, so a faulty or tampered threshold could silently alter many benefits. [medium] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-10 (records rule versions, so threshold changes are traceable)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add pre-deployment testing of threshold/rule changes against defined metrics, a staged rollout with dry-run impact preview, dual approval, and rollback for administrator updates.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Recalculations that reduce or revoke payments are not stated to go through caseworker review (FR-07 triggers cover only low confidence, discrepancies, or applicant request), so automated adverse changes could take effect without effective oversight or override. [medium] - Article 14(4)(d) (`art:14:p4:d`)
  - Partly addressed by: FR-07 (caseworker confirm/amend/override of AI decisions, but only for low confidence, discrepancy or requested-review triggers)
  - Category: `human_oversight`
  - Action: Route recalculations that reduce, suspend or revoke benefits (or exceed a change magnitude) to caseworker confirmation before they are applied, with the ability to override.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 14 Human oversight
- The requirement does not state that a recalculation is logged with its trigger (circumstance change vs. threshold update), prior and new values, or the affected cases, which limits traceability of automated benefit changes. [low] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-10 (immutable audit log of AI outputs, rule versions and decisions)
  - Category: `record_keeping`
  - Action: Specify that each recalculation event logs the trigger, initiator (system or administrator), previous and new eligibility/amount, and rule version used.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping (closest match: Article 12(2)(a))

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.
- **Human oversight, Article 14(4)(d)**
  > (d) to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output of the high-risk AI system;
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).

**Recommendations:**

- Add validation, impact preview, dual approval and rollback for threshold updates before they trigger bulk recalculation.
- Require caseworker confirmation for recalculations that reduce or revoke benefits.
- Log trigger, initiator, before/after values and rule version for every recalculation event.

---

### FR-10

**Risk level:** medium

**Requirement:** The system shall maintain an immutable audit log of all applications, data inputs, AI outputs, rule versions, human overrides, and decisions, and shall restrict access to personal and financial data to authorised users in compliance with applicable data protection regulations.

**Classified as:** Annex III point 5(a) (annex:III:5:a): (a) AI systems intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services;

**Articles selected from the index:** Article 12 Record-keeping (art:12); Article 19 Automatically generated logs (art:19); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10)

**Analysis:** FR-10 provides an immutable log of applications, inputs, outputs, rule versions, overrides and decisions with access control, which covers most of Art. 12 traceability. It leaves open the retention period, the identity of the reviewing persons, the model version and the usage periods, and it does not say that logs are meant to support risk identification and monitoring.

**Risks:**

- No log retention period is specified. Art. 19 and 26(6) require at least six months, or longer as the purpose and data protection law require. An immutable log combined with personal data also needs a defined retention and erasure policy. [medium] - Article 26(6) (`art:26:p6`)
  - Category: `record_keeping`
  - Action: Specify a log retention period of at least six months, aligned with national law and GDPR, with documented retention and deletion rules that remain compatible with immutability, for example by using pseudonymised references.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 26 Obligations of deployers of high-risk AI systems
- Logged events are not tied to the purposes in Art. 12(2): identifying risk situations or substantial modifications, supporting post-market monitoring, and supporting deployer monitoring. The AI model version and confidence are not logged, only rule versions. Without them, drift or malfunction cannot be traced to a specific model. [medium] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-07 (records human overrides with a justification, and routes low-confidence cases, which gives some traceability of AI-output reliability)
  - Category: `record_keeping`
  - Action: Extend the log schema to record the model version, confidence score, threshold applied, routing outcome, and system errors or anomalies. State that the logs feed post-market monitoring and deployer monitoring.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- The log does not explicitly capture the identity of the caseworkers who review or override AI outputs, nor the start and end time of each use. The requirement lists human overrides but not reviewer identification or usage periods. [low] - Article 12(2) (`art:12:p2`)
  - Partly addressed by: FR-07 (recorded justification for caseworker confirm, amend or override actions)
  - Category: `record_keeping`
  - Action: Record the authenticated reviewer ID, timestamps, and the session or use period for each review, override and decision event.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 12 Record-keeping
- Access restriction is stated only as 'authorised users'. It does not define roles, authentication, or protection of the log against tampering, so the log's confidentiality and integrity are not demonstrably secured. [low] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define role-based access, strong authentication, access logging, and cryptographic integrity protection (for example hash chaining or WORM storage) for the audit log.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Obligations of deployers of high-risk AI systems, Article 26(6)**
  > 6. Deployers of high-risk AI systems shall keep the logs automatically generated by that high-risk AI system to the extent such logs are under their control, for a period appropriate to the intended purpose of the high-risk AI system, of at least six months, unless provided otherwise in applicable Union or national law, in particular in Union law on the protection of personal data. Deployers that are financial institutions subject to requirements regarding their internal governance, arrangements or processes under Union financial services law shall maintain the logs as part of the documentation kept pursuant to the relevant Union financial service law.
- **Record-keeping, Article 12(2)**
  > 2. In order to ensure a level of traceability of the functioning of a high-risk AI system that is appropriate to the intended purpose of the system, logging capabilities shall enable the recording of events relevant for: (a) identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification; (b) facilitating the post-market monitoring referred to in Article 72; and (c) monitoring the operation of high-risk AI systems referred to in Article 26(5).
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Define a log retention period of at least six months, with retention and deletion rules that fit immutability and GDPR.
- Log the model version, confidence and anomalies, and state that the logs feed risk identification and post-market monitoring.
- Record the reviewer identity and the usage period for every review, override and decision.
- Specify role-based access, authentication and cryptographic tamper protection for the audit log.

---
