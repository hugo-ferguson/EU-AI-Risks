# EU AI Act Risk Assessment

This report identifies compliance risks between software requirements and the EU AI Act. It is an engineering review aid, not legal advice.

## Summary

- High: 9

### Overall analysis

Overall, the assessment reviewed 9 requirements and rated 9 as high risk. The main review focus areas are other, transparency and ai literacy. Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence.

**Review points:**

- 9 requirements reviewed in total.
- Risk distribution: 9 high, 0 medium, 0 low.
- Most frequent mapped obligation areas: other (13), transparency (7), ai literacy (1).

**Recommended follow-up actions:**

- Review and assign owners for high-risk findings before the next project checkpoint.
- Check that the most frequent obligation areas have clear evidence, owners, and documentation links.
- Use the individual requirement findings as the traceable evidence trail for detailed review.

## Requirement Findings

### FR-01

**Risk level:** high

**Requirement:** The system shall store, categorize, and manage a library of audio assets (masked or low-volume voice messages, tones, and embedded suggestion tracks), each linked to specific product categories or campaigns.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 2 Scope (art:2); Article 99 Penalties (art:99); Article 3 Definitions (art:3)

**Analysis:** FR-01 builds the asset library for a system whose purpose is covert subliminal manipulation of shoppers. That is likely a prohibited practice under Article 5(1)(a), and the library holding subliminal suggestion tracks mapped to products is the core enabling component. No design control in this requirement or elsewhere in the SRS mitigates it.

**Risks:**

- The library stores and categorizes masked or low-volume 'embedded suggestion tracks' linked to high-margin products, which directly enables a system deploying subliminal techniques beyond consciousness to distort purchasing decisions, a likely Article 5(1)(a) prohibited practice. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy this asset type. Redefine the library to hold only perceptible, disclosed audio content (announcements, ads, music). Block subliminal or masked content classes at ingestion. Obtain legal review of the intended purpose before further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(g))
- Assets are intended to be hidden from shoppers, so there is no mechanism to inform exposed persons that AI-driven or AI-generated audio is in use, or to mark synthetic audio assets as artificially generated in a machine-readable format. [medium] - Article 50(2) (`art:50:p2`)
  - Category: `transparency`
  - Action: If any assets are AI-generated (e.g. synthetic voice), add machine-readable provenance metadata to each asset. Add in-store disclosure for exposed shoppers at first exposure (Article 50(5)).
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(2)**
  > 2. Providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text content, shall ensure that the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated. Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account the specificities and limitations of various types of content, the costs of implementation and the generally acknowledged state of the art, as may be reflected in relevant technical standards. This obligation shall not apply to the extent the AI systems perform an assistive function for standard editing or do not substantially alter the input data provided by the deployer or the semantics thereof, or where authorised by law to detect, prevent, investigate or prosecute criminal offences.

**Recommendations:**

- Remove subliminal, masked, or below-perception asset types from the library and re-scope the system to transparent, perceptible audio; obtain legal review of Article 5(1)(a) exposure before proceeding.
- Add provenance and AI-generated marking metadata for synthetic audio assets, and a shopper-facing disclosure that audio content is AI-selected or generated.

---

### FR-02

**Risk level:** high

**Requirement:** The system shall let authorized operators import and maintain product catalogs with margin data, stock levels, and store locations, and designate high-margin products as promotion targets.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5)

**Analysis:** FR-02 designates high-margin products as promotion targets, which feeds a system whose stated purpose is covertly manipulating shoppers with subliminal audio. This falls within the Article 5(1)(a) prohibition, so the requirement cannot be remedied by a control and the system as specified cannot be placed on the market.

**Risks:**

- Product targeting data (margin, stock, promotion targets) is the input that directs subliminal, below-perception audio at shoppers to distort purchasing decisions, which is a prohibited practice under Article 5(1)(a). [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy promotion-target designation for subliminal delivery. Remove the subliminal capability (FR-01, FR-03, FR-06, FR-08) and redesign the system so any promotion is overt and perceivable. Have legal review the redesigned purpose.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- Margin-based targeting could direct manipulation at shoppers in vulnerable situations, for example economically constrained shoppers, with nothing to exclude or limit such effects (Article 5(1)(b)). [medium] - Article 5(1)(b) (`art:5:p1:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: If any promotion function is retained after redesign, document an assessment of vulnerability exploitation. Add constraints that prevent targeting by inferred vulnerability, and exclude the manipulative techniques entirely.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Prohibited AI practices, Article 5(1)(b)**
  > (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;

**Recommendations:**

- Stop and redesign: remove subliminal and manipulative delivery so that promotion-target designation does not feed a prohibited practice.
- Before any retained promotion feature, assess vulnerability exploitation risk and add safeguards against targeting by inferred vulnerability.

---

### FR-03

**Risk level:** high

**Requirement:** The system shall embed target messages into background audio (e.g., in-store music) at levels below conscious perception, by masking, layering, or frequency manipulation.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 99 Penalties (art:99); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 2 Scope (art:2)

**Analysis:** FR-03 specifies embedding messages below conscious perception to covertly influence purchasing, which is a subliminal technique aimed at materially distorting shopper behaviour. This falls under the Article 5(1)(a) prohibition, and no control in the SRS can cure it. Transparency measures cannot cure it either, because the design aim is to avoid awareness.

**Risks:**

- The requirement mandates subliminal techniques (masking, layering, frequency manipulation below conscious perception) intended to distort shoppers' purchasing decisions without their awareness, which matches the prohibited practice in Article 5(1)(a). Harm may be argued as financial rather than 'significant', but the covert design and the sales-optimisation loop (FR-07, FR-08) make the effect on informed decision-making hard to defend. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not implement as specified. Remove the below-perception embedding requirement and redesign the feature as overt, perceptible in-store audio. Escalate the product concept to legal/compliance review before further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(a))
- Shoppers are exposed to AI-manipulated audio content with no disclosure. The covert design conflicts with the requirement to inform people at the latest at first exposure, and the SRS has no notice mechanism. [medium] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: If any audio feature remains after redesign, add clear, accessible in-store notices that AI-generated or AI-optimised audio is in use, and make the content perceptible.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.

**Recommendations:**

- Remove or redesign the subliminal embedding so it is no longer covert. Treat Article 5(1)(a) as a blocking issue and obtain legal review before proceeding.
- If any AI-driven audio remains, provide clear in-store disclosure at first exposure and make the content perceptible.

---

### FR-04

**Risk level:** high

**Requirement:** The system shall deliver audio through store speaker infrastructure, with independent control of content, volume, and timing for each store zone or aisle.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 99 Penalties (art:99); Article 2 Scope (art:2)

**Analysis:** FR-04 provides the delivery channel for subliminal, covertly manipulative audio, which is the practice prohibited by Art. 5(1)(a). Per-zone control of content, volume, and timing makes targeted deployment operational, and nothing in the requirement or the SRS limits or discloses it.

**Risks:**

- FR-04 delivers subliminal audio (FR-03 sub-perceptual masking, FR-01 embedded suggestion tracks) to shoppers through zone-level speaker control. This is a technique beyond a person's consciousness that is intended to distort purchasing decisions without the shopper's awareness, and it is likely to fall under the Art. 5(1)(a) prohibition. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy this delivery capability for subliminal or sub-perceptual content. Restrict FR-04 to transparent, perceptible audio (ordinary music or announcements). Add a design gate that blocks playback of any asset flagged as masked, below-threshold, or embedded-suggestion. Escalate the intended purpose to legal review before further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Independent per-zone control of content, volume, and timing lets the system target specific shoppers and groups, including vulnerable ones, and adjust delivery so that the effect on behaviour is maximised. No safeguard against exploiting vulnerabilities such as age or economic situation is specified. [medium] - Article 5(1)(b) (`art:5:p1:b`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Add constraints that prevent zone targeting aimed at vulnerable groups (e.g. zones frequented by children or the elderly). Include a documented assessment of vulnerability exploitation, and enforce limits on volume and timing in the control logic.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Shoppers are exposed to audio that is generated or selected by an AI system, with no disclosure that AI is involved or that the audio has been manipulated. The playback channel in FR-04 has no notice mechanism, such as signage or an announcement, delivered at or before first exposure. [medium] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: If any form of the system is retained, add a requirement for clear in-store disclosure of AI-driven audio at store entry and in each zone. Make the disclosure accessible, and make sure it does not depend on the delivered audio itself.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Prohibited AI practices, Article 5(1)(b)**
  > (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.

**Recommendations:**

- Remove or block subliminal content delivery in FR-04 and re-scope the system to transparent, perceptible audio only.
- Add safeguards against targeting vulnerable groups and document the vulnerability-exploitation assessment.
- Add a requirement for clear, accessible in-store disclosure of AI-driven audio at or before first exposure.

---

### FR-05

**Risk level:** high

**Requirement:** The system shall use in-store sensors (e.g., occupancy counters, footfall sensors, point-of-sale feeds) to estimate shopper presence, density, and dwell time in each zone.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 2 Scope (art:2); Article 4 AI literacy (art:4); Article 3 Definitions (art:3)

**Analysis:** FR-05 supplies zone-level presence, density and dwell-time inputs that drive targeting of a covert subliminal audio manipulation system (FR-03, FR-06, FR-08), which Article 5(1)(a) prohibits. The sensing is aggregate and not itself prohibited, but as specified it enables a prohibited practice and has no transparency to shoppers.

**Risks:**

- FR-05 sensing feeds FR-06 traffic-conditioned scheduling and FR-08 adaptive optimisation, so the system can deliver subliminal messages to shoppers in specific zones at moments of peak density or dwell. This operationalises a prohibited subliminal technique that can materially distort purchasing decisions, and no requirement excludes this use. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not use FR-05 outputs to trigger or tune subliminal delivery. Remove the subliminal capability (FR-03) or redesign the system so it does not deploy techniques beyond a person's consciousness. Add an explicit prohibition and technical guard against feeding sensor data into manipulative-content selection.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Shoppers sensed and exposed to the AI-driven audio are never told that an AI system is operating on them or that the audio content is artificially manipulated. FR-05 specifies no notice or signage at the point of sensing or first exposure. [medium] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add clear in-store notices at entrances and zones stating that sensors and an AI system are used to estimate presence and dwell time and to select audio. Disclose any audio content that is generated or manipulated, and make the notices accessible.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.

**Recommendations:**

- Block use of FR-05 sensor outputs for targeting subliminal or manipulative audio, and remove or redesign the subliminal functionality so the system does not fall under the Article 5(1)(a) prohibition.
- Provide clear, accessible shopper-facing disclosure of the sensing and AI-driven audio at store entry and in each zone, no later than first exposure.

---

### FR-06

**Risk level:** high

**Requirement:** The system shall let operators schedule campaigns by time, day, zone, and shopper traffic conditions, and shall automatically select the audio asset that matches the targeted product and context.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 99 Penalties (art:99); Article 26 Obligations of deployers of high-risk AI systems (art:26)

**Analysis:** FR-06 automates scheduling and selection of subliminal audio assets by product, context and live shopper traffic. It operationalises a practice that Article 5(1)(a) prohibits, and no transparency or safeguard exists to mitigate this. The requirement cannot be made compliant by adding controls.

**Risks:**

- Automatic context-aware selection and scheduling of subliminal messages (FR-01/FR-03) for high-margin products deploys subliminal techniques beyond shoppers' consciousness. This materially distorts purchasing decisions and is a prohibited practice under Article 5(1)(a). [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy this function for subliminal assets. Remove subliminal or masked content from the asset library and from the selection logic, and restrict scheduling to perceptible, disclosed audio. Run a prohibited-practice screening before any further design work.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- Targeting by shopper traffic and context lets the system time messages for moments of reduced decision-making ability, such as high density or long dwell. This could exploit vulnerable groups, and the requirement has no exclusion or safeguard for them. [medium] - Article 5(1)(b) (`art:5:p1:b`)
  - Category: `other`
  - Action: Define and document targeting constraints that exclude exploitative timing and contexts. Add a review gate that checks whether campaign rules could exploit vulnerabilities linked to age, disability or economic situation.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- Shoppers are never told that an AI system selects and plays audio aimed at them. Nothing in FR-06 or the related requirements provides disclosure at or before first exposure. [medium] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add in-store notices that are clear and accessible and shown before or at first exposure, stating that AI-driven audio is in use. Only perceptible, disclosed content should be played. Notices alone do not cure the Article 5 prohibition.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems
- Operators who configure campaigns are not required to have any AI literacy or training on the manipulation risks and legal limits of the scheduling and selection function. [low] - Article 4(1) (`art:4:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `ai_literacy`
  - Action: Provide operator training and onboarding that covers prohibited practices, and require acknowledgement before access to campaign scheduling is granted.
  - Trace:
    - selected from the Act's index: ch:I GENERAL PROVISIONS > Article 4 AI literacy

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Prohibited AI practices, Article 5(1)(b)**
  > (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.
- **AI literacy, Article 4(1)**
  > Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used.

**Recommendations:**

- Remove subliminal capability from scheduling and selection. Treat the system's purpose as a prohibited practice under Article 5(1)(a) and redesign or halt it.
- Add targeting guardrails and a vulnerability-exploitation review to campaign scheduling rules.
- Add clear, accessible shopper disclosure of AI-driven audio at store entry and in zones.
- Add operator AI-literacy training covering Article 5 limits, required before access is granted.

---

### FR-07

**Risk level:** high

**Requirement:** The system shall correlate audio playback events with sales data to report conversion uplift, margin impact, and per-campaign performance.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 12 Record-keeping (art:12); Article 4 AI literacy (art:4)

**Analysis:** FR-07 measures conversion uplift and margin impact for a system whose purpose is covertly steering shoppers with subliminal audio. This is a prohibited practice under Art. 5(1)(a), and the requirement supplies the effectiveness feedback that optimizes the manipulation. No requirement-level fix can make it compliant.

**Risks:**

- FR-07 reports conversion uplift and margin impact per campaign. This measures and supports optimizing subliminal messaging meant to distort purchasing behaviour below conscious awareness, which falls under the Art. 5(1)(a) prohibition (use of subliminal techniques causing decisions shoppers would not otherwise take). FR-08 feeds this output back into message selection. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy FR-07 as part of this system. Remove the subliminal-messaging purpose (FR-03, FR-01, FR-08) or redesign the system so it uses only perceptible, disclosed audio. Escalate to legal/compliance for a prohibited-practice determination before further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(e))
- Shoppers are never told they are exposed to AI-selected and AI-optimized audio influence. The measurement in FR-07 assumes covert exposure, and nothing discloses it at or before first exposure. [high] - Article 50(5) (`art:50:p5`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: If a non-prohibited, perceptible variant is pursued, add clear in-store disclosure of AI-driven audio personalization at or before first exposure. Restrict FR-07 analytics to consented or aggregated data.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(5)**
  > 5. The information referred to in paragraphs 1 to 4 shall be provided to the natural persons concerned in a clear and distinguishable manner at the latest at the time of the first interaction or exposure. The information shall conform to the applicable accessibility requirements.

**Recommendations:**

- Treat FR-07 and the subliminal-influence function as an Art. 5(1)(a) prohibited practice. Do not release it, and remove or redesign the subliminal features before any further development.
- If a lawful, perceptible variant is pursued, add clear disclosure of AI-driven audio to shoppers at or before first exposure, and limit FR-07 analytics to aggregated or consented data.

---

### FR-08

**Risk level:** high

**Requirement:** The system shall adjust message selection, timing, and frequency based on measured effectiveness and shall support A/B testing of audio variants.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 50 Transparency obligations for providers and deployers of certain AI systems (art:50); Article 4 AI literacy (art:4); Article 99 Penalties (art:99); Article 2 Scope (art:2)

**Analysis:** FR-08 adds an optimisation loop that tunes and A/B tests subliminal audio against measured effectiveness, which strengthens the system's ability to materially distort shopper behaviour. This falls within the Article 5(1)(a) prohibition, and no requirement-level control can cure it. Article 50 transparency is also absent.

**Risks:**

- Adaptive selection, timing and frequency, plus A/B testing of subliminal audio variants against sales effectiveness, optimises the system to distort shopper behaviour beyond conscious awareness. This is a prohibited practice under Article 5(1)(a), and the A/B testing would expose real shoppers to it. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy this optimisation for subliminal or covert audio. Remove the subliminal capability (FR-01, FR-03) and limit adaptation to perceptible, disclosed content, with legal review before any release.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Adapting and A/B testing covert audio targeted at high-margin products may exploit shoppers' vulnerabilities, such as economic situation or age, because the optimisation does not exclude susceptible groups. This risks falling within Article 5(1)(b). [medium] - Article 5(1)(b) (`art:5:p1:b`)
  - Category: `other`
  - Action: Prohibit optimisation that targets or learns from vulnerable-group signals. Document a vulnerability and harm assessment, and set guardrails on the frequency and intensity the optimiser may reach.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))
- Shoppers exposed to adaptive and A/B-tested audio are never informed that an AI system is influencing them. Nothing discloses the AI interaction or the AI-generated or manipulated audio at first exposure. [high] - Article 50(1) (`art:50:p1`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `transparency`
  - Action: Add clear in-store notice at entry that AI-driven audio is in use. Mark any synthetic audio in a machine-readable format and exclude non-disclosed variants from experiments.
  - Trace:
    - selected from the Act's index: ch:IV TRANSPARENCY OBLIGATIONS FOR PROVIDERS AND DEPLOYERS OF CERTAIN AI SYSTEMS > Article 50 Transparency obligations for providers and deployers of certain AI systems

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;
- **Prohibited AI practices, Article 5(1)(b)**
  > (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a natural person or a specific group of persons due to their age, disability or a specific social or economic situation, with the objective, or the effect, of materially distorting the behaviour of that person or a person belonging to that group in a manner that causes or is reasonably likely to cause that person or another person significant harm;
- **Transparency obligations for providers and deployers of certain AI systems, Article 50(1)**
  > 1. Providers shall ensure that AI systems intended to interact directly with natural persons are designed and developed in such a way that the natural persons concerned are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect, taking into account the circumstances and the context of use. This obligation shall not apply to AI systems authorised by law to detect, prevent, investigate or prosecute criminal offences, subject to appropriate safeguards for the rights and freedoms of third parties, unless those systems are available for the public to report a criminal offence.

**Recommendations:**

- Remove the adaptive optimisation and A/B testing of subliminal audio. Redesign the system around perceptible, non-manipulative content, after legal review under Article 5(1)(a).
- Add guardrails that block optimisation exploiting vulnerable groups, and document a harm assessment.
- Disclose AI-driven audio to shoppers at first exposure and mark synthetic audio machine-readably.

---

### FR-09

**Risk level:** high

**Requirement:** The system shall provide a secure operator dashboard with role-based access, remote multi-store management, audit logging of all playback and configuration changes, and system health monitoring.

**Articles selected from the index:** Article 5 Prohibited AI practices (art:5); Article 12 Record-keeping (art:12); Article 15 Accuracy, robustness and cybersecurity (art:15); Article 26 Obligations of deployers of high-risk AI systems (art:26); Article 19 Automatically generated logs (art:19)

**Analysis:** FR-09 is an operator dashboard with audit logging and access control for a system whose purpose, subliminal manipulation of shoppers, falls under the Article 5(1)(a) prohibition. Dashboard controls cannot cure this, and the requirement makes the prohibited practice easier to operate across multiple stores.

**Risks:**

- The dashboard provides remote multi-store management and operation of a system that deploys subliminal, below-conscious-perception audio to distort shoppers' purchasing decisions, which is a prohibited practice. The management and audit controls support the use of the prohibited system and do not mitigate it. [high] - Article 5(1)(a) (`art:5:p1:a`)
  - SRS-wide gap: no single requirement owns this obligation.
  - Category: `other`
  - Action: Do not build or deploy this dashboard for the subliminal-messaging purpose. Escalate to legal and compliance, and redefine the system scope to remove subliminal or manipulative techniques (FR-01, FR-03, FR-06, FR-08) before any further development.
  - Trace:
    - selected from the Act's index: ch:II PROHIBITED AI PRACTICES > Article 5 Prohibited AI practices (closest match: Article 5(1)(h))

**Cited provisions:**

- **Prohibited AI practices, Article 5(1)(a)**
  > (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person’s consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm;

**Recommendations:**

- Stop development and deployment of the subliminal audio system, and have legal counsel review it against Article 5(1)(a). Only a redesign that removes covert, below-perception influence, with transparent and non-manipulative audio, could make FR-09's dashboard acceptable.

---
