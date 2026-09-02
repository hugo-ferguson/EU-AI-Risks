export const sampleReport = {
  "summary": {
    "high": 0,
    "medium": 11,
    "low": 5
  },
  "findings": [
    {
      "id": "FR-1",
      "level": "medium",
      "requirement": "The system shall ingest candidate resumes, cover letters, and application form responses submitted through the recruitment portal.",
      "analysis": "Requirement FR-1 does not specify data processing and storage practices, leaving a gap in data_governance with Article 10(2).",
      "risks": [
        {
          "description": "Does not specify data processing and storage practices [medium] \u2014 Article 10(2)",
          "category": "data_governance",
          "action": "Define data processing and storage practices for resume, cover letter, and application form responses."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Define data processing and storage practices for resume, cover letter, and application form responses.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define data processing and storage practices"
      ]
    },
    {
      "id": "FR-2",
      "level": "medium",
      "requirement": "The system shall generate a suitability score for each candidate based on job requirements, experience, education, and skills extracted from the application.",
      "analysis": "The requirement FR-2 may not meet data quality criteria, creating a data governance compliance gap with art:10(3) and (4).",
      "risks": [
        {
          "description": "Does not specify data quality properties for training, validation and testing datasets [medium] \u2014 Article 10(3)",
          "category": "data_governance",
          "action": "Define and document data quality properties for training, validation and testing datasets."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Define and document data quality properties for training, validation and testing datasets.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define and document data quality properties for training, validation and testing datasets"
      ]
    },
    {
      "id": "FR-3",
      "level": "medium",
      "requirement": "The system shall rank candidates for recruiter review using the generated suitability score.",
      "analysis": "The requirement lacks clarity on data governance and transparency for human oversight, and does not specify the statistical properties of the suitability score data, creating a missing compliance gap with Article 10 and 13.",
      "risks": [
        {
          "description": "Does not specify data governance practices for suitability score data [medium] \u2014 Article 10(3)",
          "category": "data_governance",
          "action": "Implement data quality checks and validation procedures for suitability score data."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Implement data quality checks and validation procedures for suitability score data.",
          "category": "",
          "action": ""
        },
        {
          "description": "Lacks transparency in human oversight for recruiter review, creating a gap with Article 13(1) [medium] \u2014 Article 13(1)",
          "category": "transparency",
          "action": "Provide clear instructions for use and transparency requirements for human oversight in recruiter review."
        },
        {
          "description": "Category: `transparency`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Provide clear instructions for use and transparency requirements for human oversight in recruiter review.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Implement data quality checks and validation procedures for suitability score data.",
        "Provide clear instructions for use and transparency requirements for human oversight in recruiter review."
      ]
    },
    {
      "id": "FR-4",
      "level": "low",
      "requirement": "The system shall explain the main factors that influenced each candidate suitability score in language understandable to a recruiter.",
      "analysis": "The requirement FR-4 is partially addressed by provisions in art:13 and art:50, but the main factor explanation is not specified, creating a missing compliance gap with art:13(1).",
      "risks": [
        {
          "description": "Does not specify main factor explanation for scores [low] \u2014 art:13(1)",
          "category": "transparency",
          "action": "Clarify the explanation for scores in the requirement or technical documentation."
        },
        {
          "description": "Category: `transparency`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Clarify the explanation for scores in the requirement or technical documentation.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Clarify the explanation for scores in the requirement or technical documentation"
      ]
    },
    {
      "id": "FR-5",
      "level": "medium",
      "requirement": "The system shall notify recruiters when a candidate ranking was generated by an automated decision-support model.",
      "analysis": "The requirement does not specify how the transparency of the automated decision-support model used in candidate ranking is ensured, creating a missing gap in transparency, and does not explicitly address the data quality of the candidate data used for ranking, which could lead to biased outcomes.",
      "risks": [
        {
          "description": "The requirement does not specify how the transparency of the automated decision-support model used in candidate ranking is ensured [medium] \u2014 Article 13(1)",
          "category": "transparency",
          "action": "Specify the methodology for model interpretability and explainability."
        },
        {
          "description": "Category: `transparency`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Specify the methodology for model interpretability and explainability.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Specify the methodology for model interpretability and explainability, and ensure data quality of candidate data."
      ]
    },
    {
      "id": "FR-6",
      "level": "medium",
      "requirement": "The system shall allow a human recruiter to review, override, or reject any automated ranking before a candidate is removed from consideration.",
      "analysis": "Requirement FR-6 does not specify competency requirements for human reviewers, and monitoring expectations, creating a remaining gap with Article 14(4).",
      "risks": [
        {
          "description": "Does not specify competency requirements for human reviewers [medium] \u2014 Article 14(4)",
          "category": "human_oversight",
          "action": "Add reviewer competency, escalation, and monitoring requirements"
        },
        {
          "description": "Category: `human_oversight`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Add reviewer competency, escalation, and monitoring requirements",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define reviewer competency, escalation, and monitoring requirements"
      ]
    },
    {
      "id": "FR-7",
      "level": "low",
      "requirement": "The system shall log every model-generated score, ranking, explanation, recruiter override, and final screening decision.",
      "analysis": "The requirement already describes a control/safeguard. A low remaining clarification risk is retained for manual review.",
      "risks": [
        {
          "description": "Does not specify information on recruiter override, final screening decision, and model-generated scores in logging capabilities [low] \u2014 Article 12(3)",
          "category": "record_keeping",
          "action": "Add information on recruiter override, final screening decision, and model-generated scores to the logging capabilities."
        },
        {
          "description": "Category: `record_keeping`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Add information on recruiter override, final screening decision, and model-generated scores to the logging capabilities.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Add information on recruiter override, final screening decision, and model-generated scores to the logging capabilities."
      ]
    },
    {
      "id": "FR-8",
      "level": "low",
      "requirement": "The system shall retain audit records for each screening decision so that reviewers can trace the input data, model version, and human actions involved.",
      "analysis": "The requirement already describes a control/safeguard. A low remaining clarification risk is retained for manual review.",
      "risks": [
        {
          "description": "Does not specify the storage duration for the audit records [low] \u2014 art:19(2)",
          "category": "record_keeping",
          "action": "Define the storage duration for the audit records"
        },
        {
          "description": "Category: `record_keeping`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Define the storage duration for the audit records",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define the storage duration for the audit records"
      ]
    },
    {
      "id": "FR-9",
      "level": "low",
      "requirement": "The system shall prevent the use of facial recognition, biometric identification, or emotion recognition during candidate screening.",
      "analysis": "No requirement-level risk was retained because the requirement is framed as an existing safeguard/control that prevents a sensitive or prohibited feature. Manual review may still confirm how the control is implemented.",
      "risks": [],
      "recommendations": []
    },
    {
      "id": "FR-10",
      "level": "medium",
      "requirement": "The system shall provide candidates with a channel to request review of a decision that was influenced by automated ranking.",
      "analysis": "The requirement FR-10 lacks clarity on the review process criteria and does not ensure competency requirements for human reviewers, creating a missing gap with Article 14(4).",
      "risks": [
        {
          "description": "Does not specify criteria for review of automated decision-making by human reviewers [medium] \u2014 Article 14(4)",
          "category": "human_oversight",
          "action": "Define clear review criteria and competency requirements for human reviewers."
        },
        {
          "description": "Category: `human_oversight`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Define clear review criteria and competency requirements for human reviewers.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define clear review criteria, competency requirements and monitoring expectations for human reviewers"
      ]
    },
    {
      "id": "NFR-1",
      "level": "low",
      "requirement": "The system must validate training and evaluation datasets for missing values, duplicate records, and inconsistent labels before model training.",
      "analysis": "Requirement NFR-1 does not explicitly require validation of dataset quality for missing values, duplicate records, or inconsistent labels, which is covered by art:10(3) and art:10(4).",
      "risks": [
        {
          "description": "Does not specify requirements for dataset quality validation [low] \u2014 Article 10(3)",
          "category": "data_governance",
          "action": "Implement data quality validation for missing values, duplicate records, and inconsistent labels."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Implement data quality validation for missing values, duplicate records, and inconsistent labels.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Implement data quality validation for missing values, duplicate records, and inconsistent labels."
      ]
    },
    {
      "id": "NFR-2",
      "level": "medium",
      "requirement": "The system must measure model performance separately across demographic groups where lawful demographic evaluation data is available.",
      "analysis": "Requirement NFR-2 lacks demographic data validation, missing a critical safeguard to ensure fairness and unbiased model performance across demographic groups.",
      "risks": [
        {
          "description": "Does not specify demographic data validation [medium] \u2014 Article 10(4)",
          "category": "data_governance",
          "action": "Include data validation to account for characteristics or elements that are particular to specific geographical, contextual, behavioural or functional settings within which the high-risk AI system is intended to be used."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Include data validation to account for characteristics or elements that are particular to specific geographical, contextual, behavioural or functional settings within which the high-risk AI system is intended to be used.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Include demographic data validation to address potential bias in model performance across demographic groups"
      ]
    },
    {
      "id": "NFR-3",
      "level": "medium",
      "requirement": "The system must not use protected attributes such as race, religion, disability, or political opinion as ranking inputs.",
      "analysis": "Requirement does not specify how protected attributes will be handled, raising concerns under art:10(2) about data governance and management practices.",
      "risks": [
        {
          "description": "Does not specify handling of protected attributes [medium] \u2014 Article 10(2)",
          "category": "data_governance",
          "action": "Specify data handling and protection mechanisms in the requirement."
        },
        {
          "description": "Category: `data_governance`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Specify data handling and protection mechanisms in the requirement.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Specify data handling and protection mechanisms for protected attributes"
      ]
    },
    {
      "id": "NFR-4",
      "level": "medium",
      "requirement": "The system must maintain access controls so that only authorised recruitment staff can view candidate data and model explanations.",
      "analysis": "Requirement NFR-4 does not explicitly address cybersecurity measures for the recruitment system, leaving a gap in the protection of authorized recruitment staff from unauthorized access to candidate data and model explanations, which relates to Article 15(1) and 15(4) of the AI Act.",
      "risks": [
        {
          "description": "Does not specify technical cybersecurity measures to prevent unauthorized access to candidate data and model explanations [medium] \u2014 Article 15(1)",
          "category": "accuracy_robustness_cybersecurity",
          "action": "Implement a multi-layered security framework, including encryption, secure data storage, and access controls."
        },
        {
          "description": "Category: `accuracy_robustness_cybersecurity`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Implement a multi-layered security framework, including encryption, secure data storage, and access controls.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Implement a multi-layered security framework, including encryption, secure data storage, and access controls."
      ]
    },
    {
      "id": "NFR-5",
      "level": "medium",
      "requirement": "The system must produce monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds.",
      "analysis": "The requirement on monitoring alerts when model accuracy, bias metrics, or data quality checks fall outside configured thresholds does not address the need for an analysis of interaction between the AI system and other systems, creating a remaining gap with art:72, paragraph 2.",
      "risks": [
        {
          "description": "Does not address interaction analysis with other systems [medium] \u2014 art:72",
          "category": "post_market_monitoring",
          "action": "Implement an interaction analysis module to monitor and report on interactions between the AI system and other systems."
        },
        {
          "description": "Category: `post_market_monitoring`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Implement an interaction analysis module to monitor and report on interactions between the AI system and other systems.",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Implement interaction analysis module",
        "Analyze interactions between AI system and other systems"
      ]
    },
    {
      "id": "NFR-6",
      "level": "medium",
      "requirement": "The system should support rollback to a previously approved model version if a deployed model fails safety, robustness, or fairness checks.",
      "analysis": "The system lacks specific requirements for model version rollback and post-deployment monitoring, creating a gap with art:15(4) and art:72(2).",
      "risks": [
        {
          "description": "Does not specify rollback procedures for model version failures [medium] \u2014 Article 15(4)",
          "category": "accuracy_robustness_cybersecurity",
          "action": "Implement model version rollback procedures"
        },
        {
          "description": "Category: `accuracy_robustness_cybersecurity`",
          "category": "",
          "action": ""
        },
        {
          "description": "Suggested engineering action: Implement model version rollback procedures",
          "category": "",
          "action": ""
        }
      ],
      "recommendations": [
        "Define model version rollback procedures",
        "Establish post-deployment monitoring plans"
      ]
    }
  ]
};
