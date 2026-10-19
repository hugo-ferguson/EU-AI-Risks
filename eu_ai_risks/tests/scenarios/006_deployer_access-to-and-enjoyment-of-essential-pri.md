FR-01 - The system shall allow an authenticated applicant to submit a child benefit application containing household details, including the applicant’s identity, each child’s date of birth and relationship to the applicant, and each adult household member’s details.

FR-02 - The system shall collect and validate income data for all relevant household members, including income source, amount, and assessment period, and shall reject or flag incomplete, inconsistent, or out-of-range values before processing.

FR-03 - The system shall verify submitted identity, income, and family composition information against authorised external records (e.g., tax authority, civil registry, employer records) where available, and shall flag discrepancies for review.

FR-04 - The system shall determine family composition eligibility by applying configurable rules, including child age limits, dependency status, custody or residency arrangements, and the number of eligible children.

FR-05 - The system shall use an AI model, in combination with configurable policy rules, to calculate whether the household meets the income-based eligibility criteria and to compute the benefit amount payable per child and in total, adjusting for income thresholds, tapering, and family size.

FR-06 - The system shall provide an explanation for every eligibility decision and payment calculation, listing the input data, rules, and factors that influenced the outcome, in language understandable to the applicant.

FR-07 - The system shall automatically route applications to a human caseworker for review when the AI’s confidence is below a configurable threshold, when data discrepancies are detected, or when the applicant requests a manual review, and shall allow caseworkers to confirm, amend, or override AI decisions with a recorded justification.

FR-08 - The system shall notify applicants of the decision outcome, the calculated benefit amount, and the right to appeal, and shall allow applicants to submit appeals or updated information that triggers recalculation.

FR-09 - The system shall recalculate eligibility and payment amounts when household circumstances change (e.g., income change, birth of a child, child reaching the age limit) or when policy thresholds are updated by an authorised administrator.

FR-10 - The system shall maintain an immutable audit log of all applications, data inputs, AI outputs, rule versions, human overrides, and decisions, and shall restrict access to personal and financial data to authorised users in compliance with applicable data protection regulations.