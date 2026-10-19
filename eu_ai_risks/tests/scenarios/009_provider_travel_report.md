# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- Medium: 3
- Low: 6

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 3 as medium risk and 6 as low risk. The main review focus areas are transparency and accuracy robustness cybersecurity. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 0 high, 3 medium, 6 low.
- Most frequent mapped obligation areas: transparency (7), accuracy robustness cybersecurity (1).
- 1 low-risk requirement appears to describe a control or safeguard, but still needs clarification/evidence review.

**Recommended follow-up actions:**

- Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** low

**Requirement:** The system shall allow the user to select a travel destination (country, city, or region) from a searchable list or by typing a destination name, with auto-suggestions for matching locations.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-01 is a destination search and selection input function with no AI generation, so the Article 50 provisions listed do not create a gap at this requirement level. Any AI-disclosure or AI-generated-content marking obligations belong to the tip-generation and display requirements (FR-04, FR-06), not to destination selection.

---

### FR-02

**Risk level:** low

**Requirement:** The system shall validate the selected destination and prompt the user to correct or reselect it if the destination is not recognized or is ambiguous.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 14 Human oversight (art:14); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-02 is an input-validation control for destination selection and itself supports robustness. The system has no Annex III classification and is not clearly high-risk, so no requirement-level gap is supported by the supplied provisions.

---

### FR-03

**Risk level:** low

**Requirement:** The system shall retrieve relevant, up-to-date safety information for the selected destination from configured data sources, such as government travel advisories, crime statistics, health alerts, and weather or natural hazard reports.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 10 Data and data governance (art:10); Article 4 AI literacy (art:4); Article 95 Codes of conduct for voluntary application of specific requirements (art:95)

**Analysis:** FR-03 is a data retrieval requirement in a non-high-risk system (no Annex III point applies). The high-risk provisions in Articles 10 and 15 do not bind it. The retrieval requirement raises no requirement-level gap under the supplied provisions that apply to it, and FR-06, FR-07 and FR-09 already cover source display, disclaimers and error handling.

---

### FR-04

**Risk level:** medium

**Requirement:** The system shall use an AI model to generate short, clear travel safety tips (e.g., 3 to 7 tips, each no longer than two sentences) based on the retrieved safety information for the selected destination.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 53 Obligations for providers of general-purpose AI models (art:53); Article 25 Responsibilities along the AI value chain (art:25)

**Analysis:** FR-04 generates AI text tips for end users but does not require that the output be marked as AI-generated. The system is not high-risk (no Annex III point applies), so Article 15 does not apply. The Art. 50 transparency gap is limited and only partly covered by FR-07.

**Risks:**

- AI-generated tip text has no requirement for machine-readable marking or detectability as artificially generated, and no user-facing AI disclosure. FR-07's disclaimer says the tips are general guidance but does not say they are AI-generated. [medium] - Article 50(2) (`art:50:p2`)
  - Category: `transparency`
  - Action: Add to FR-04 that generated tips carry machine-readable provenance (e.g., metadata flag or watermark in the API/response payload) marking them as AI-generated. Add a visible 'AI-generated' label in the UI shown at first exposure.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- Users interact directly with an AI generation feature, but nothing requires informing them at or before first exposure that the tips come from an AI system. This may not be obvious to a reasonably well-informed user. [low] - Article 50(1) (`art:50:p1`)
  - Partly addressed by: FR-07 (a disclaimer displayed with the tips, though it does not state that the content is AI-generated)
  - Category: `transparency`
  - Action: Add a clear, accessible AI-use notice at first interaction (Art. 50(5)). Alternatively, document why AI use is obvious from the UI context.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(2)**
  > 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**Recommendations:**

- Mark FR-04 outputs as AI-generated in a machine-readable format and label them in the UI.
- Add an accessible AI-interaction notice shown at first exposure, and extend FR-07's disclaimer to state that the tips are AI-generated.

---

### FR-05

**Risk level:** low

**Requirement:** The system shall categorize each generated tip by topic (e.g., personal safety, health, transportation, scams, local laws and customs, natural hazards) so users can quickly scan the results.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-05 only categorizes generated tips by topic. It is a presentation feature and raises no requirement-level gap under Article 50, which concerns AI-interaction disclosure and machine-readable marking of generated content. The system is not high-risk, and the AI-generated nature of the tips is a system-level concern for FR-04/FR-06/FR-07 rather than for FR-05.

---

### FR-06

**Risk level:** medium

**Requirement:** The system shall display the generated tips to the user in a readable format, along with the destination name, the information sources used, and the date the information was last updated.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 13 Transparency and provision of information to deployers (art:13); Article 53 Obligations for providers of general-purpose AI models (art:53)

**Analysis:** FR-06 displays tips with destination, sources and last-updated date, but does not require that the user is told the text is AI-generated. This is a limited transparency gap for a non-high-risk system with no Annex III classification.

**Risks:**

- The display requirement lists destination, sources and update date but does not state that the tips are AI-generated. The system generates text and interacts directly with users, so an AI-disclosure label at or before first exposure is not specified. FR-07's disclaimer says the tips are general guidance, not that they are AI-generated. [medium] - Article 50(1) (`art:50:p1`)
  - Category: `transparency`
  - Action: Add an AI-generated content label to the tips display, shown clearly at first exposure and meeting accessibility requirements. Also include it in the first-use flow.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- Tips are AI-generated text, but the requirement specifies no machine-readable marking of the output (e.g. metadata or an API flag) to make it detectable as artificially generated. Whether this applies depends on whether the tips are substantially AI-generated text, which they appear to be. [low] - Article 50(2) (`art:50:p2`)
  - Category: `transparency`
  - Action: Embed machine-readable provenance metadata (e.g. an 'ai_generated' field) in the tips output. Document the chosen approach.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(2)**
  > 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

**Recommendations:**

- Add a visible 'AI-generated' label to the tips display, shown no later than first exposure and accessible.
- Add a machine-readable AI-generated marker to the tips output and document it.

---

### FR-07

**Risk level:** medium

**Requirement:** The system shall include a disclaimer with the tips stating that they are general guidance and not a substitute for official government travel advisories.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 13 Transparency and provision of information to deployers (art:13); Article 4 AI literacy (art:4)

**Analysis:** FR-07 adds a disclaimer that the tips are general guidance, which supports user transparency. It does not state that the tips are AI-generated, and Art. 50 may require that disclosure. The system is not Annex III high-risk, so Art. 13, 9 and 4 do not apply to this requirement.

**Risks:**

- The disclaimer says only 'general guidance'. It does not tell users the tips are AI-generated, and no requirement in the SRS marks the text output as AI-generated. Art. 50(2) applies to AI-generated text, with possible exemptions to be assessed. Art. 50(5) requires the information to be clear and given at the first exposure. [medium] - Article 50(2) (`art:50:p2`)
  - Category: `transparency`
  - Action: Extend the FR-07 disclaimer to state that the tips are AI-generated. Show it at first exposure in an accessible, distinguishable way. Add machine-readable marking of the generated text, or document why the Art. 50(2) exemptions apply.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(2)**
  > 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

**Recommendations:**

- Reword FR-07 to include an explicit AI-generated content notice, shown at first exposure and meeting accessibility requirements. Add machine-readable marking of the output, or document the Art. 50(2) exemption analysis.

---

### FR-08

**Risk level:** low

**Requirement:** The system shall allow the user to change the selected destination at any time and shall regenerate the tips for the new destination without requiring the user to restart the application.

**Articles selected from the index:** Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50)

**Analysis:** FR-08 regenerates AI-generated tips on destination change but does not specify that each regeneration is disclosed as AI-generated. FR-07 and FR-06 provide a disclaimer and sources, but neither explicitly marks the content as AI-generated, and this gap persists across regenerations.

**Risks:**

- Regenerated tips for a new destination have no stated requirement to be marked as AI-generated (machine-readable marking or visible disclosure), so the AI-generated label could be lost after a destination change. [low] - Article 50(2) (`art:50:p2`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Partly addressed by: FR-07 (a disclaimer shown with the tips saying they are general guidance, which gives users context but does not mark the text as AI-generated)
  - Category: `transparency`
  - Action: State in FR-08 that every regeneration carries the same AI-generated marking (machine-readable metadata plus a visible label) as the first generation, and test that the marking is present after each destination change.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- The user is not told at or before first exposure that the tips are AI-generated, and FR-08 does not ensure this information is shown again after each regeneration in a clear and distinguishable manner. [low] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add an AI-use notice shown with the first tips and retained in the UI when tips are regenerated. Make sure it meets accessibility requirements.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Transparency obligations for providers and deployers of certain AI systems, Article 50(2)**
  > 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.

**Recommendations:**

- Require FR-08 regeneration to apply the same AI-generated marking as initial generation, in machine-readable and visible form.
- Add a clear, accessible AI-use notice at first exposure and keep it displayed after each destination change.

---

### FR-09

**Risk level:** low

**Requirement:** The system shall handle errors, such as unavailable data sources or AI generation failures, by displaying a clear message to the user and offering to retry or showing the most recent cached tips where available.

**Articles selected from the index:** Article 15 Accuracy, robustness and cybersecurity (art:15); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 13 Transparency and provision of information to deployers (art:13)

**Analysis:** FR-09 already provides user-facing error messages, retry and cached-tip fallback, which supports resilience. The system is not Annex III high-risk, so Article 15 and 13 high-risk obligations do not strictly apply. One minor gap remains: cached tips may be shown without clear staleness indication, which is a transparency/accuracy concern for safety guidance.

**Risks:**

- Cached tips shown as a fallback may be outdated safety information, and FR-09 does not require that the user is told they are cached and when they were last refreshed; FR-06 covers the last-updated date only for normal display. [low] - Article 15(4) (`art:15:p4`)
  - Partly addressed by: FR-06 (display of the date the information was last updated)
  - Category: `accuracy_robustness_cybersecurity`
  - Action: Amend FR-09 so cached fallback tips are labelled as cached, show the retrieval date, and are suppressed once older than a defined maximum age. Note that Article 15 applies strictly only if the system is classified high-risk; treat it as good practice otherwise.
  - Trace:
    - selected from the Act's index: ch:III HIGH-RISK AI SYSTEMS / Requirements for high-risk AI systems > Article 15 Accuracy, robustness and cybersecurity

**Cited provisions:**

- **Accuracy, robustness and cybersecurity, Article 15(4)**
  > 4. High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard. The robustness of high-risk AI systems may be achieved through technical redundancy solutions, which may include backup or fail-safe plans. High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

**Recommendations:**

- Label cached tips as cached with their retrieval date, and set a maximum cache age beyond which they are not shown.

---
