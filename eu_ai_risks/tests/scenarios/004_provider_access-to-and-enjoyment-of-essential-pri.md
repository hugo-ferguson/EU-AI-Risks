FR-01 - The system shall collect and ingest applicant data from authorized sources, including application forms, credit bureau records, bank transaction histories, income and employment verification, and existing debt obligations.

FR-02 - The system shall validate, clean, and standardize all ingested applicant data, flagging missing, inconsistent, or anomalous values for correction or manual review before scoring.

FR-03 - The system shall use a trained AI model to calculate a numeric credit score for each applicant, along with a risk category (e.g., low, medium, high), based on the processed applicant data.

FR-04 - The system shall provide an explanation for each credit score, identifying the key factors and their relative influence on the result, in a form understandable to loan officers and applicants.

FR-05 - The system shall generate a creditworthiness recommendation (approve, decline, or refer for manual review) by comparing the credit score and risk category against configurable lending policy thresholds.

FR-06 - The system shall allow authorized loan officers to review, override, or escalate AI-generated recommendations, requiring a documented justification for every override.

FR-07 - The system shall monitor the model for bias and fairness by evaluating outcomes across protected demographic groups, excluding protected attributes (e.g., race, gender, religion) as scoring inputs, and alerting administrators when disparities exceed defined limits.

FR-08 - The system shall maintain an immutable audit log of all inputs, model versions, scores, explanations, recommendations, and human overrides to support regulatory compliance and dispute resolution.

FR-09 - The system shall enable applicants to access the data used in their assessment, request corrections, and contest decisions, and shall generate adverse action notices stating the principal reasons for any declined application.

FR-10 - The system shall track model performance over time (e.g., accuracy, drift, default prediction rates) and support controlled retraining, versioning, and rollback of models by authorized administrators.
