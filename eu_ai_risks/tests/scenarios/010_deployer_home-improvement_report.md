# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Low: 8

### Overall analysis

Overall, the assessment reviewed 8 requirements and rated 8 as low risk. The main review focus areas are transparency. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 8 requirements reviewed in total.
- Risk distribution: 0 high, 0 medium, 8 low.
- Most frequent mapped obligation areas: transparency (2).
- 2 low-risk requirements appear to describe a control or safeguard, but still needs clarification/evidence review.

**Recommended follow-up actions:**

- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** low

**Requirement:** The system shall present the user with a predefined set of selectable moods (e.g., relaxed, focused, energetic, sleepy, social, romantic).

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95)

**Analysis:** FR-01 only presents a predefined list of moods in the UI. It has no Annex III classification and handles no sensitive data, so no requirement-level gap is supported by the provisions supplied. Art. 50(1) (AI interaction disclosure) is a system-level matter, because the AI model is only introduced in FR-03 and the user is not conversing with an AI.

---

### FR-02

**Risk level:** low

**Requirement:** The system shall allow the user to select exactly one mood at a time as the input for generating a lighting suggestion.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4)

**Analysis:** FR-02 is a single-select mood input control for a low-risk lighting recommender. No supplied provision creates a requirement-level gap: it is not an Annex III use case, and the AI-interaction disclosure and synthetic-content marking obligations are not tied to this input requirement.

---

### FR-03

**Risk level:** low

**Requirement:** The system shall use an AI model to map the selected mood to a recommended indoor lighting colour temperature value expressed in Kelvin (K) within the range 2000K to 6500K.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 15 Accuracy, robustness and cybersecurity (art:15)

**Analysis:** FR-03 maps a mood to a colour temperature using an AI model. The system is not high-risk and has no Annex III classification, so Article 15 and other high-risk obligations do not bind it. The only plausible provision is Article 50(1), and the user-facing AI disclosure is not stated anywhere in the SRS.

**Risks:**

- The system interacts directly with users and produces AI-generated recommendations, but no requirement says users are told the suggestion comes from an AI model. Disclosure may be non-obvious, since the UI shows only a Kelvin value and a label (FR-04). [low] - Article 50(1) (`art:50:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a UI disclosure, available at first interaction, that the lighting recommendation is AI-generated. Make it accessible, per Art. 50(5). Alternatively, document why AI use is obvious to a reasonably well-informed user.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**Recommendations:**

- Add a clear, accessible notice at first interaction that the colour-temperature suggestion is generated by an AI model, or record a justification that this is obvious from the context of use.

---

### FR-04

**Risk level:** low

**Requirement:** The system shall display the recommended colour temperature to the user as both a numeric Kelvin value and a descriptive label (e.g., “Warm White”, “Neutral White”, “Cool White”).

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 13 Transparency and provision of information to deployers (art:13); Article 4 AI literacy (art:4)

**Analysis:** FR-04 only displays the recommended Kelvin value and label. It is a low-stakes lighting recommendation with no Annex III classification, so no high-risk obligations (Art. 13, 9, 4) apply. Art. 50 does not apply either: the output is a numeric value and a label, not synthetic content, and users plainly interact with a lighting app.

---

### FR-05

**Risk level:** low

**Requirement:** The system shall provide a visual preview of the recommended colour temperature on the user interface so the user can see the suggested lighting tone before applying it.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 13 Transparency and provision of information to deployers (art:13); Article 14 Human oversight (art:14); Article 4 AI literacy (art:4)

**Analysis:** FR-05 is a UI preview feature for a non-high-risk lighting recommender (no Annex III match). The supplied provisions that apply to high-risk systems (Arts. 9, 13, 14) do not apply, and the Art. 50 provisions are not triggered by a colour-temperature preview.

---

### FR-06

**Risk level:** low

**Requirement:** The system shall allow the user to accept the suggestion, reject it, or manually adjust the suggested value within the permitted range.

**Articles selected from the index:** Article 14 Human oversight (art:14); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4)

**Analysis:** FR-06 already gives the user accept, reject and adjust control over the suggestion, which is the override capability described in Art. 14(4)(d). The system is not Annex III high-risk, so Art. 14 does not bind it, and no requirement-level compliance gap is identified from the supplied provisions.

---

### FR-07

**Risk level:** low

**Requirement:** The system shall generate a new suggestion each time the user selects a different mood, with the updated recommendation displayed within 2 seconds of selection.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4)

**Analysis:** FR-07 is a UI/latency behaviour for a lighting colour-temperature recommender with no Annex III classification. The supplied provisions do not support a requirement-level compliance gap, since the high-risk obligations in Article 15 do not apply and no transparency trigger is present in this requirement.

---

### FR-08

**Risk level:** low

**Requirement:** The system shall store the user’s accepted or manually adjusted settings for each mood and use this feedback to refine future suggestions for that user.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95); Article 2 Scope (art:2); Article 6 Classification rules for high-risk AI systems (art:6)

**Analysis:** FR-08 stores per-user mood settings and feeds them back into the suggestion model. This is a low-risk lighting recommender with no Annex III use, and the supplied provisions support no requirement-level gap beyond a minor transparency clarification.

**Risks:**

- The system interacts directly with users through an AI-based recommender that adapts to their feedback, and no requirement says users are told the suggestions are AI-generated and personalised from stored feedback. It is arguably obvious to a reasonably informed user, so this is a clarification. [low] - Article 50(1) (`art:50:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add a UI notice, shown no later than first use, that suggestions are AI-generated and adapt to the user's stored accept/adjust feedback. Document the reasoning if the system is deemed obviously AI.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**Recommendations:**

- Add a clear first-interaction notice that suggestions come from an AI model and are personalised from the user's stored feedback, or document why this is obvious in context.

---
