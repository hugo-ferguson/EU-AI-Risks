# Rubric for judging compliance risks

You judge one compliance risk at a time. Each risk was produced for one requirement of a software
requirements specification (SRS) and cites one provision of the EU AI Act (Regulation (EU)
2024/1689) as its legal basis. You are given:

- the full SRS, so you know what the system as a whole does and what the other requirements
  already provide;
- the requirement the risk was raised for;
- the risk: the gap it claims, the provision it cites, and the words it quotes from that
  provision;
- the text of the cited provision as it appears in the Act, or a note that it does not exist.

Score the risk on the three criteria below, each from 0 to 10, using the anchors. Judge only from
the text you are given and the meaning of the Act. Judge each criterion separately: a risk can
describe a real gap but cite the wrong provision, or cite the right provision for a gap that does
not exist. Do not reward length, confident wording, or severity. You do not know which system
produced the risk, and it does not matter.

## 1. Gap validity (RQ1: is the risk correct?)

Does the gap the risk describes really exist? A gap exists when the requirement, read with the
rest of the SRS, does not provide what the risk says is missing, and providing it would require
changing or adding to the SRS. A gap that belongs to the SRS as a whole (no single requirement
provides it) still counts.

| Score | Meaning |
|---|---|
| 10 | The gap clearly exists. Nothing in the requirement or the rest of the SRS provides it. |
| 7-9 | The gap exists, but part of it is already provided by this or another requirement, or the risk slightly overstates it. |
| 4-6 | Debatable. The gap depends on one reading of the requirement, or the requirement mostly provides it and only clarification or evidence is missing. |
| 1-3 | Mostly wrong. The requirement or another requirement already provides what the risk says is missing, or the risk misreads what the requirement does. |
| 0 | The risk contradicts the SRS (it calls something missing that is explicitly stated), or describes a system or function the SRS does not describe. |

## 2. Provision support (RQ2: is the risk supported by the Act?)

Does the cited provision impose the obligation that the risk says is missing, on this kind of
system and on the party the SRS concerns? Read the provision's text, not its title or topic.
A provision that defines a term, sets out scope, gives powers to the Commission or authorities,
or places a duty on a different party does not support a risk about what the system must do.

| Score | Meaning |
|---|---|
| 10 | The provision's text directly imposes exactly the obligation the risk says is missing, and it applies to this system. |
| 7-9 | The provision imposes the obligation, but the risk stretches it slightly, or another paragraph or point states it more exactly. |
| 4-6 | The provision concerns the same obligation but supports only part of the gap, or the obligation is implied rather than stated. |
| 1-3 | The provision shares the topic but does not impose this obligation (for example a definition, a scope rule, a cross-reference, or another party's duty), or it does not apply to this kind of system. |
| 0 | The provision is unrelated to the gap, does not exist, or no provision is cited. |

## 3. Citation precision (RQ3: can the risk be traced to the text of the Act?)

Could a reviewer go from the risk straight to the words of the Act that create the obligation?
Consider whether the citation points to the most specific paragraph or lettered point that
contains the obligation, and whether the quoted words are the operative words of that provision.

| Score | Meaning |
|---|---|
| 10 | The citation is the exact paragraph or point that contains the obligation, and the quote is its operative words. |
| 7-9 | The right paragraph, but a lettered point within it would be more exact, or the quote includes words that are not about the obligation. |
| 4-6 | The right article, but a different paragraph of it contains the obligation, or the quote comes from elsewhere in the provision. |
| 1-3 | The citation only refers to the obligation (for example a provision that cross-references it) or is a whole article with no way to find the words. |
| 0 | There is no traceable link: the provision does not exist, is not cited, or has nothing to do with the gap. |

## Response

Respond with only a JSON object of three integers from 0 to 10, and nothing else:

{"gap_validity": 0, "provision_support": 0, "citation_precision": 0}
