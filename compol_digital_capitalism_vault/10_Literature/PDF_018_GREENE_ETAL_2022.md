---
type: source_note
status: draft_ra
source_id: PDF_018
filename: GREENE_ETAL_2022.pdf
author_year: GREENE 2022
clusters:
- G2_TOPIC_MODELING_METHOD
- G7_VENUE_POSITIONING_PRECEDENT
priority: Low
needs_diego_review: true
---

### Bibliographic Identity
*   **Title:** The Independence Echo: The Rise of the Constitutional Question in Scottish Election Manifestos and Voter Behaviour
*   **Authors:** Zachary Greene (University of Strathclyde), Fraser McMillan (University of Glasgow)
*   **Journal:** *Journal of Elections, Public Opinion, and Parties*
*   **Year:** 2020
*   **Status:** Forthcoming (at time of source text)
*   **Core Subject:** The relationship between party manifesto content and voter opinion shifts regarding Scottish independence.
*   **Abstract Summary:** Investigates an elite-driven perspective where increased salience of independence in voter opinion is an echo of elite and partisan attention. Uses unsupervised content analysis of manifestos and structural topic models to predict changes in voter support from the British Election Study (BES).

### Methodology & Corpus
*   **Method Type:** Structural Topic Model (STM) / Unsupervised Content Analysis.
*   **Corpus:** 25 party election manifestos (Scottish parties, late 1990s to 2016).
*   **Validation Strategy:** Pairing topic model estimates with British Election Study (BES) survey data (2007, 2011, 2016) to predict change in voter support for independence.
*   **Preprocessing Choices:** Unsupervised learning approach; text treated as manifestos (16,382 sentences total).
*   **Short-text Handling:** Not applicable (uses long-form manifestos).
*   **Spanish Handling:** Not applicable (English/Scottish political text).
*   **Method Limitations:** Specificity to Scottish context; K (number of topics) not specified in provided text; generalizability of STM to political text remains a claim rather than a tested alternative in this specific instance.

### Relevance to Diego's Paper
*   **Analogue/Precedent:** Serves as a strong methodological precedent for using STM on election manifestos to track issue salience.
*   **Methodological Parallel:** Shares the use of topic modeling to quantify political text and link it to survey data.
*   **Theoretical Context:** Provides a theoretical framework (elite-driven issue entrepreneurship) that complements or contrasts with voter-centric models often found in similar literature.

### Bibliographic Extraction Details

**Method & Corpus:**
*   **Method:** Structural Topic Model (STM).
*   **Corpus:** 25 Scottish election manifestos (16,382 sentences); British Election Study (BES) survey data.
*   **Validation:** Predictive modeling linking manifesto topic estimates to BES voter support changes.
*   **K (Topics):** Not explicitly specified in the provided text.
*   **Preprocessing:** Unsupervised content analysis.
*   **Short-text/Spanish Handling:** N/A (Long-form English texts).
*   **Citation:** Greene, Z., & McMillan, F. (2020). The Independence Echo: The Rise of the Constitutional Question in Scottish Election Manifestos and Voter Behaviour. *Journal of Elections, Public Opinion, and Parties*.

**Journal & Positioning:**
*   **Journal:** *Journal of Elections, Public Opinion, and Parties*.
*   **Year:** 2020.
*   **Article Type:** Empirical Research Article.
*   **Niche Coverage:** 
    *   **Method:** Topic Modeling (STM).
    *   **Object:** Election Manifestos.
    *   **Region:** Scotland/UK.
    *   **Theory:** Issue Competition / Elite-Driven Responsiveness.
*   **Relationship to Diego's Paper:** **Precedent/Analogue.** It validates the application of unsupervised topic models to manifesto text and links them to voter behavior, likely serving as a similar reference point for Diego's work depending on whether Diego focuses on method or case.
*   **Gap Remaining:** The authors explicitly note that "cross-national studies of issue competition will enable more conclusive theory testing."
*   **One-Sentence Citation Use:** "Greene and McMillan (2020) employ a structural topic model on Scottish manifestos to demonstrate how elite-driven issue entrepreneurship shapes voter salience, offering a methodological template for linking text mining to survey data."

### Bibliographic Identity, Method, and Claims
*   **Identity:** Greene & McMillan (2020). *Journal of Elections, Public Opinion, and Parties*.
*   **Studies:** The causal link between party manifesto emphasis on independence and shifts in Scottish voter opinion.
*   **Method:** Unsupervised content analysis (STM) on manifestos + Regression/Structural modeling on BES survey data.
*   **Corpus:** 25 Scottish party manifestos; BES waves (2007, 2011, 2016).
*   **Core Claims:** 1) Independence salience is an echo of elite attention (SNP). 2) Increased elite attention leads voters to form stronger views. 3) Topic models can distinguish post-devolution politics.
*   **Relevance to Diego's Paper:** Likely serves as a methodological benchmark for STM on political text or a theoretical counterpoint to voter-centric theories.
*   **Cluster Tags:** `#TopicModeling`, `#STM`, `#ElectionManifestos`, `#ScottishIndependence`, `#IssueSalience`, `#VoterBehavior`.
*   **Possible Citation Uses:** Methodological example for STM on political text; Theoretical support for elite-driven agenda setting.
*   **Limits:** Case-specific (Scotland); Forthcoming status (potential citation uncertainty); K-value not reported.
*   **Open Questions:** How generalizable are STM findings to other political systems or short-text campaigns?

### Specific Question Answers

**[G2_TOPIC_MODELING_METHOD]**
*   **Method:** Structural Topic Model (STM).
*   **Corpus:** 25 Scottish party election manifestos (16,382 sentences).
*   **Validation Strategy:** Using topic model estimates to predict changes in voter support for independence derived from the British Election Study (BES).
*   **Topic Number (K):** Not explicitly stated in the provided text.
*   **Preprocessing:** Unsupervised content analysis (standard topic modeling pipeline implied).
*   **Short Text/Spanish Handling:** Not applicable (Uses long-form English manifestos).
*   **Interpretability/Alternatives:** The authors claim STM distinguishes distinct language and framing pathways; they discuss using unsupervised learning specifically to overcome limitations of hand-coding.

**[G7_VENUE_POSITIONING_PRECEDENT]**
*   **Journal:** *Journal of Elections, Public Opinion, and Parties*.
*   **Why Precedent:** It establishes STM as a viable tool for analyzing manifesto evolution and linking it to voter behavior in a sub-national context.
*   **Niche Coverage:** Method (Topic Model), Object (Manifestos), Region (Scotland), Theory (Issue Salience/Competition).
*   **Relationship:** **Analogue/Precedent.** It directly addresses the application of topic modeling to political text similar to Diego's paper.
*   **Gap Remaining:** Lack of cross-national testing; the need to apply these methods beyond the Scottish case.
*   **One-Sentence Citation Use:** "Greene and McMillan (2020) demonstrate how structural topic models can track elite-driven issue salience in election manifestos, linking textual content to voter behavior changes."