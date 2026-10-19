# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Medium: 1
- Low: 8

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 1 as medium risk and 8 as low risk. The main review focus areas are accuracy robustness cybersecurity, data governance, ai literacy, post market monitoring and quality management. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 0 high, 1 medium, 8 low.
- Most frequent mapped obligation areas: accuracy robustness cybersecurity (4), data governance (2), ai literacy (1), post market monitoring (1), quality management (1).
- 2 low-risk requirements appear to describe a control or safeguard, but still needs clarification/evidence review.

**Recommended follow-up actions:**

- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** low

**Requirement:** The system shall ingest historical and real-time station data, including bike availability, dock availability, and trip start/end events, from the bike-sharing operator’s data feeds at a configurable interval of no more than 5 minutes.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 4 AI literacy (art:4); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 95 Codes of conduct for voluntary application of specific requirements (art:95)

**Analysis:** FR-01 is a data ingestion requirement for a bike-demand forecasting system with no Annex III classification. The high-risk provisions in Articles 10 and 15 are not shown to apply, and the remaining provisions do not fit this requirement. No requirement-level compliance gap is identified.

---

### FR-02

**Risk level:** low

**Requirement:** The system shall collect and integrate external contextual data that influences demand, including weather conditions and forecasts, time of day, day of week, public holidays, and scheduled local events.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 2 Scope (art:2); Article 6 Classification rules for high-risk AI systems (art:6); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 95 Codes of conduct for voluntary application of specific requirements (art:95)

**Analysis:** FR-02 ingests external contextual data (weather, calendar, events) for a bike-demand forecasting system with no Annex III classification, so it is likely not high-risk and Article 10 and 15 obligations do not bind it. No requirement-level compliance gap is supported by the supplied provisions.

---

### FR-03

**Risk level:** low

**Requirement:** The system shall validate and preprocess incoming data by detecting missing, duplicate, or anomalous records and applying defined cleaning or imputation rules before the data is used for prediction.

**Articles selected from the index:** Article 10 Data and data governance (art:10); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 9 Risk management system (art:9)

**Analysis:** FR-03 already provides a data validation and cleaning control for incoming data. The system has no Annex III classification, so the high-risk obligations in Articles 9, 10 and 15 are only a weak fit. Only low-severity wording and documentation gaps remain, and they matter only if the system is treated as high-risk.

**Risks:**

- The cleaning and imputation rules are not required to be documented, with their assumptions, rationale, and effect on data quality. They also have no stated acceptance criteria. This is the data-preparation documentation Article 10(2)(c) and (d) expects, and Article 10(3) expects data that is free of errors and complete. [low] - Article 10(2)(c) (`art:10:p2:c`)
  - Category: `data_governance`
  - Action: Document the cleaning and imputation rules, their assumptions, and anomaly thresholds. Log the count of records flagged, dropped, or imputed per run, and define acceptable data-quality limits, such as a maximum imputation rate beyond which predictions are suppressed or flagged.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance (closest match: Article 10(2)(c))
- The requirement does not say how anomalous or manipulated inputs are handled beyond cleaning. It does not specify whether bad feeds trigger a fallback or fail-safe, or whether an anomaly can be an injected or poisoned input. Article 15(4) and (5) call for resilience to input errors and faults and for protection against manipulation. [low] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-06 (flags stations or time periods where accuracy falls below a threshold, which partly supports consistent performance monitoring (Art. 15(1)))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define behaviour when data quality is too poor, such as suppressing forecasts, falling back to the last good model or a baseline, and alerting operators. Treat anomaly detection as an integrity control against corrupted or manipulated feeds.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

**Recommendations:**

- Document the cleaning and imputation rules, log per-run data-quality statistics, and set acceptance thresholds for data quality.
- Specify fail-safe behaviour for severely degraded or suspicious input data, and treat anomaly detection as an input-integrity control.

---

### FR-04

**Risk level:** low

**Requirement:** The system shall generate short-term demand predictions for each station, forecasting the expected number of bike pickups and returns for upcoming horizons (e.g., the next 15, 30, and 60 minutes).

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 6 Classification rules for high-risk AI systems (art:6); Article 95 Codes of conduct for voluntary application of specific requirements (art:95)

**Analysis:** FR-04 is a demand-forecasting function for bike-sharing rebalancing. No Annex III point applies, so it is not high-risk and the Article 15 high-risk obligations do not bind it. No Article 50 transparency trigger applies either, because it is not a chatbot and generates no synthetic content. No requirement-level compliance gap is identified.

---

### FR-05

**Risk level:** medium

**Requirement:** The system shall train, retrain, and update its prediction models automatically on a configurable schedule using the latest historical data, and shall maintain versioned models so that a previous version can be restored if needed.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 17 Quality management system (art:17); Article 9 Risk management system (art:9); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72)

**Analysis:** FR-05 automates retraining and versioned rollback, but it has no validation gate before a retrained model is promoted and no integrity control against poisoned or biased training data. The system has no Annex III classification, so the high-risk provisions apply only if it is deemed high-risk, and the gaps are modest.

**Risks:**

- Automatic scheduled retraining can promote a new model to production with no pre-deployment test against defined metrics or thresholds. FR-06 evaluates accuracy only after deployment, so a degraded model could go live and trigger rollback only after the fact. [medium] - Article 9(8) (`art:9:p8`)
  - Partly addressed by: FR-06 (error metrics and a configurable accuracy threshold (post-deployment evaluation only))
  - Category: `risk_management`
  - Action: Add an automated validation gate to the retraining pipeline. Test the candidate model on a holdout set against predefined metrics and thresholds, and promote it only if it meets or beats the current version. Otherwise keep the current version and alert operators.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 9 Risk management system
- The 'latest historical data' used for retraining has no stated provenance, quality or representativeness checks, or data-governance records for each training run. FR-03 cleans incoming data for prediction but does not cover training-set governance. Retraining on the system's own outputs is also not addressed. [medium] - Article 10(2)(c) (`art:10:p2:c`)
  - Partly addressed by: FR-03 (cleaning and imputation of missing, duplicate and anomalous records (10(2)(c)))
  - Category: `data_governance`
  - Action: For each training run, record the dataset version, time window, source and cleaning steps. Check representativeness (seasonality, stations, events) and drift before training.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 10 Data and data governance
- Automated retraining on live data feeds has no stated protection against data or model poisoning, and no access control on the pipeline or model store. Rollback exists, but it does not detect or prevent manipulated training data. [medium] - Article 15(5) (`art:15:p5`)
  - Partly addressed by: FR-03 (detection of anomalous records in incoming data (partial input integrity))
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Add anomaly checks on training data, restrict and audit write access to the training pipeline and model registry, and sign model artifacts. Define rollback triggers that fire when performance degrades.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Model versions and retraining events are not tied to documented change management or to the technical documentation. Versioning is stated, but there are no records of what changed, when, or why. [low] - Article 17(1)(a) (`art:17:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `quality_management`
  - Action: Keep a model registry that records each version's training data, metrics, approver and rollback reason. Define which retraining changes count as significant modifications that need review.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Obligations of providers and deployers of high-risk AI systems and other parties > Article 17 Quality management system (closest match: Article 17(1)(f))

**Cited provisions:**

- **Risk management system, Article 9(8)**
  > 8. The testing of high-risk AI systems shall be performed, as appropriate, at any time throughout the development process, and, in any event, prior to their being placed on the market or put into service. Testing shall be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose of the high-risk AI system.
- **Data and data governance, Article 10(2)(c)**
  > (c) relevant data-preparation processing operations, such as annotation, labelling, cleaning, updating, enrichment and aggregation;
- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.
- **Quality management system, Article 17(1)(a)**
  > (a) a strategy for regulatory compliance, including compliance with conformity assessment procedures and procedures for the management of modifications to the high-risk AI system;

**Recommendations:**

- Add a pre-promotion validation gate with predefined metrics and thresholds, and keep the current version if the candidate fails.
- Log dataset provenance, time window and quality checks per training run, and check for drift and representativeness.
- Protect the training pipeline and model registry with access control, data anomaly checks and signed artifacts, and define rollback triggers.
- Maintain a model registry with change records, and define which retraining changes are significant modifications.

---

### FR-06

**Risk level:** low

**Requirement:** The system shall evaluate prediction accuracy by comparing forecasts against actual observed demand, compute error metrics (e.g., MAE, RMSE), and flag stations or time periods where accuracy falls below a configurable threshold.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems (art:72); Article 9 Risk management system (art:9); Article 17 Quality management system (art:17)

**Analysis:** FR-06 already implements accuracy evaluation (MAE/RMSE) with configurable threshold flagging. The system has no Annex III classification, so Article 15 and the high-risk obligations only apply by assumption. The remaining gaps are minor: the declared accuracy levels and the action taken on flagged degradation are not specified.

**Risks:**

- FR-06 computes metrics and flags below-threshold performance, but the threshold is only 'configurable'. No pre-defined acceptance levels are specified and no link exists to declaring accuracy levels and metrics in instructions of use. [low] - Article 15(3) (`art:15:p3`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define default accuracy thresholds per horizon (15/30/60 min) and document the metrics (MAE, RMSE) and expected levels in the instructions of use.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity
- Flagged accuracy degradation is not tied to any follow-up (retraining, rollback, or feeding post-market monitoring), so continuous performance across the lifecycle is only partly ensured. [low] - Article 72(2) (`art:72:p2`)
  - Partly addressed by: FR-05 (model retraining and version restore, which can serve as a response to degraded performance)
  - Category: `post_market_monitoring`
  - Action: Persist accuracy results over time and define a documented response to threshold breaches (e.g., trigger retraining via FR-05 or rollback to a prior model version).
  - Trace:
    - selected from the Act's index: ch:IX POST-MARKET MONITORING, INFORMATION SHARING AND MARKET SURVEILLANCE / Post-market monitoring > Article 72 Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(3)**
  > 3. The levels of accuracy and the relevant accuracy metrics of high-risk AI systems shall be declared in the accompanying instructions of use.
- **Post-market monitoring by providers and post-market monitoring plan for high-risk AI systems, Article 72(2)**
  > 2. The post-market monitoring system shall actively and systematically collect, document and analyse relevant data which may be provided by deployers or which may be collected through other sources on the performance of high-risk AI systems throughout their lifetime, and which allow the provider to evaluate the continuous compliance of AI systems with the requirements set out in Chapter III, Section 2. Where relevant, post-market monitoring shall include an analysis of the interaction with other AI systems. This obligation shall not cover sensitive operational data of deployers which are law-enforcement authorities.

**Recommendations:**

- Specify default accuracy thresholds per forecast horizon and document the metrics and levels in the instructions of use.
- Store accuracy metric history and define a documented response to threshold breaches, linking to FR-05 retraining or rollback.

---

### FR-07

**Risk level:** low

**Requirement:** The system shall generate alerts when a station is predicted to run out of bikes or docks within a forecast horizon, and shall deliver these alerts to operators via the dashboard and configurable notification channels.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 6 Classification rules for high-risk AI systems (art:6); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-07 generates shortage alerts for bike-sharing operators. The system is not Annex III and not high-risk, and it does not interact with natural persons in a way that triggers Art. 50 or generate synthetic content. No requirement-level gap is supported by the supplied provisions.

---

### FR-08

**Risk level:** low

**Requirement:** The system shall provide an operator dashboard displaying current station status, demand forecasts, and predicted shortages or surpluses on a map and in tabular form, with filtering by station, area, and time horizon.

**Articles selected from the index:** Article 4 AI literacy (art:4); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14)

**Analysis:** FR-08 is an operator dashboard for a bike-sharing demand forecasting system with no Annex III classification, so the high-risk provisions (Arts. 9, 13, 14) do not clearly apply. Only a light AI literacy point for dashboard users remains.

**Risks:**

- Operators who read forecasts and shortage predictions on the dashboard may lack the skills to interpret forecast uncertainty and accuracy limits; the dashboard does not state that interpretation guidance or training is provided (Article 4 applies to all AI systems). [low] - Article 4(1) (`art:4:p1`)
  - Category: `ai_literacy`
  - Action: Show forecast confidence and accuracy indicators (e.g. from FR-06) in the dashboard, add in-app help on interpreting predictions, and document operator onboarding on the system's limitations.
  - Trace:
    - selected from the Act's index: ch:I GENERAL PROVISIONS > Article 4 AI literacy

**Cited provisions:**

- **AI literacy, Article 4(1)**
  > Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used.

**Recommendations:**

- Add confidence and accuracy indicators and brief interpretation guidance to the dashboard, and document operator AI literacy onboarding.

---

### FR-09

**Risk level:** low

**Requirement:** The system shall expose forecasts through a secured API so that other systems, such as rebalancing/dispatch tools and rider-facing applications, can retrieve station-level predictions programmatically.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 13 Transparency and provision of information to deployers (art:13); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 25 Responsibilities along the AI value chain (art:25); Article 6 Classification rules for high-risk AI systems (art:6)

**Analysis:** FR-09 exposes forecasts through a 'secured' API but does not specify authentication, authorization, integrity or abuse controls. The system has no Annex III classification, so high-risk obligations are unlikely to bind. If it were treated as high-risk, unauthorized manipulation of outputs consumed by dispatch tools would be a gap, but it is a low-severity wording issue.

**Risks:**

- 'Secured API' is unspecified (no authentication, authorization, rate limiting, or output-integrity requirements). If the system were deemed high-risk, resilience against unauthorized parties altering outputs or performance would not be demonstrable. [low] - Article 15(5) (`art:15:p5`)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Define API security controls: client authentication (OAuth2/mTLS), per-consumer authorization scopes, rate limiting, TLS, signed or integrity-protected responses, and access/audit logging. Document the threat model for downstream consumers.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(5)**
  > 5. High-risk AI systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities. The technical solutions aiming to ensure the cybersecurity of high-risk AI systems shall be appropriate to the relevant circumstances and the risks. The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

**Recommendations:**

- Replace 'secured API' with testable security criteria (authN/authZ, rate limits, TLS, response integrity, logging) and record the Article 6 non-high-risk assessment for this system.

---
