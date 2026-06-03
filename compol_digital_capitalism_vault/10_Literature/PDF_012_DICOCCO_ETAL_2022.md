---
type: source_note
status: draft_ra
source_id: PDF_012
filename: DICOCCO_ETAL_2022.pdf
author_year: DICOCCO 2022
clusters:
- G2_TOPIC_MODELING_METHOD
- G5_ETHICS_MANIPULATION_RISK
priority: Medium
needs_diego_review: true
---

### 1. Bibliographic Identity & Core Analysis

*   **Bibliographic Identity:**
    *   **Title:** How Populist are Parties? Measuring Degrees of Populism in Party Manifestos Using Supervised Machine Learning
    *   **Authors:** Jessica DiCocco (Sapienza University, Rome) and Bernardo Monechi (Sony Computer Science Laboratories, Paris).
    *   **Journal:** *Political Analysis*, Vol. 30, No. 3, 2022 (pp. 311–327).
    *   **DOI:** 10.1017/pan.2021.29.
*   **What the Source Studies:**
    *   Comparative measurement of populism across parties and countries using automated text analysis.
    *   Development of a continuous populist score using supervised machine learning on party manifestos.
*   **Method:**
    *   Supervised Machine Learning (Random Forest Classifier).
    *   Text-as-data approach (Bag-of-Words features).
*   **Corpus:**
    *   268 electoral manifestos from 99 parties.
    *   6 Western European countries: Italy, France, Spain, Germany, Austria, Netherlands.
    *   Timeframe: 2002–2019.
    *   Unit of analysis: Sentences (243,659 total).
    *   Robustness corpus: 2,151 sentences from Italian leader speeches (2006–2019).
*   **Core Claims:**
    *   Text-as-data allows for scalable, cost-effective, and continuous measurement of populism compared to human coding.
    *   Manifestos are valid proxies for party positions despite being less read than speeches.
    *   Continuous scores reduce arbitrary classification errors inherent in dichotomous measures.
*   **Relevance to Diego's Paper:**
    *   *(Note: Without access to "Diego's paper," relevance is inferred based on topic)*: Likely relevant if Diego's work involves computational political science, measurement of political polarization, or text analysis of electoral data. Provides a methodological benchmark for validating ML-based populism indices.
*   **Cluster Tags:**
    *   #ComputationalPoliticalScience #PopulismMeasurement #MachineLearning #TextAsData #PartyManifestos #RandomForest
*   **Possible Citation Uses:**
    *   Methodological reference for constructing continuous populism indices.
    *   Corpus source for European party manifestos (2002–2019).
    *   Validation example for text-as-data approaches (comparing ML scores to expert surveys).
*   **Limits:**
    *   **Document Specificity:** Results may vary if applied to speeches vs. manifestos (though robustness check attempted this).
    *   **Training Labels:** Relies on existing human-coded classifications (PopuList) for training.
    *   **Language/Linguistic:** Trained per country due to lack of monolingual comprehensive corpus.
*   **Open Questions:**
    *   How well does the model generalize to non-Western contexts?
    *   Does the continuous score capture nuance lost in traditional categorical coding?

### 2. Method & Technical Specifications

*   **Method Type:** Supervised Machine Learning (Random Forest Classifier). *Note: Not LDA/STM/BERTopic; this is a classification/scoring model, not a topic modeling tool.*
*   **Corpus:** National electoral manifestos (2002–2019) from 6 European countries.
*   **Validation Strategy:**
    1.  **Internal:** 70% training, 30% testing split.
    2.  **External:** Correlation with expert survey variables (CHES 2017, POPPA 2018).
    3.  **Robustness:** Comparison against manual coding and alternative text source (Italian leader speeches).
*   **Preprocessing Choices:**
    *   Sentence splitting based on manifesto structure.
    *   Lowercase conversion.
    *   Removal of punctuation, numbers, and stop words.
    *   Stemming.
    *   Conversion to Binary Bag-of-Words (1 if word present, 0 otherwise).
*   **Spanish/Short-text/Political-Ad Handling:**
    *   **Spanish:** Included as one of the 6 languages (corpora 2004–2019). Trained separately per country.
    *   **Short-text:** Explicitly excluded tweets/posts (argued to be post-2004/2006 diffusion).
    *   **Political Ads:** Not analyzed; manifestos are the primary focus.
*   **Method Limitations:**
    *   Resource-intensive human annotation required for training labels (PopuList).
    *   Limited to contemporary classifications and specific Western contexts.
*   **How to Cite:**
    *   DiCocco, J., & Monechi, B. (2022). How Populist are Parties? Measuring Degrees of Populism in Party Manifestos Using Supervised Machine Learning. *Political Analysis*, 30(3), 311–327. https://doi.org/10.1017/pan.2021.29

### 3. Risks & Ethics (Based on Provided Text)

*   **Risks Named:**
    *   **Measurement Risk:** "Risk of arbitrary classifications" (dichotomous vs. continuous).
    *   **Data Risk:** "Document specificity" (manifestos may show lower levels of rhetoric than speeches/magazines).
    *   **Time Risk:** "Rapid changes and transformations" of party landscapes may outpace human coding.
*   **Empirical Evidence vs. Speculation:**
    *   The paper provides empirical evidence (correlations with CHES/POPPA) to support its claims. It frames the methodological approach as evidence-based rather than speculative.
*   **Microtargeting/Harm Discussion:**
    *   **Not Discussed:** This source does *not* discuss microtargeting, privacy, or algorithmic manipulation risks. It focuses on the *measurement* of populism, not the *political campaign strategy* or *algorithmic dissemination*.
    *   **Platform/Campaign/Regulator Roles:** Not addressed.
*   **Counterargument:**
    *   Standard argument against manifestos: They are rarely read.
    *   Paper's Counterargument: They are official documents, summarize party stances, and are comparable across cases.
*   **Ethics/Evidence Debate Framing:**
    *   "Automated methods allow for faster processing and more accurate predictions, reducing the limitations inherent in human-coding techniques, provided that the model is validated against established expert surveys."

### 4. Paper-Specific Questions

**[G2_TOPIC_MODELING_METHOD]**
*   **What method is used?** Supervised Machine Learning (Random Forest Classifier).
*   **What corpus?** 243,659 sentences from 268 party manifestos (99 parties) across 6 Western European countries (2002–2019).
*   **What validation strategy?** Split sample validation (70% train/30% test) and external validation against expert survey variables (CHES, POPPA). Robustness check using Italian leader speeches.
*   **Topic number K if any?** No. The model outputs a **continuous score** (0 to 1) representing probability of populist rhetoric, rather than discrete topics.
*   **What preprocessing choices?** Lowercase, remove punctuation/numbers/stop words, stemming, Binary Bag-of-Words features.
*   **Does it discuss short texts, Spanish, interpretability, or alternatives to LDA?** Discusses Spanish (included). Explicitly excludes short texts (tweets). Discusses alternatives to LDA by favoring supervised classification for accuracy over topic modeling for this specific goal.

**[G5_ETHICS_MANIPULATION_RISK]**
*   **What democratic risk is identified?** The paper identifies risks primarily related to **measurement validity and arbitrariness** (e.g., "risk of arbitrary classifications"), not direct manipulation or polarization. It notes the risk that manifestos might show lower rhetoric than other texts.
*   **Is the concern manipulation, privacy, polarization, misinformation, opacity, unequal exposure, or persuasion?** No. The concerns are methodological (measurement validity, document specificity, scalability).
*   **Does the source distinguish fear from evidence?** Yes. The authors distinguish between the theoretical definition of populism (Manichean struggle) and the empirical evidence of the method's ability to measure it (via correlation with expert surveys). They argue for evidence-based measurement over resource-intensive coding.