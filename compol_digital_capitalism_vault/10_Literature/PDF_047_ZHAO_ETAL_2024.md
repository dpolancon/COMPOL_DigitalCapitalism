---
type: source_note
status: draft_ra
source_id: PDF_047
filename: ZHAO_ETAL_2024.pdf
author_year: ZHAO 2024
clusters:
- G3_PLATFORMIZATION_DIGITAL_POLITICS
- G2_TOPIC_MODELING_METHOD
priority: Review
needs_diego_review: true
---

Based on the provided text, here is the detailed analysis of the academic source: **"Manufacturing conflict or advocating peace? A study of social bots agenda building in the Twitter discussion of the Russia-Ukraine war" (Zhao et al., 2024)**.

---

### 1. Bibliographic Identity & Content Summary
*   **Bibliographic Identity:**
    *   **Citation:** Zhao, B., Ren, W., Zhu, Y., & Zhang, H. (2024). Manufacturing conflict or advocating peace? A study of social bots agenda building in the Twitter discussion of the Russia-Ukraine war. *Journal of Information Technology & Politics*, 21(2), 176–194. DOI: 10.1080/19331681.2023.2189201.
    *   **Journal:** *Journal of Information Technology & Politics* (Taylor & Francis).
    *   **Publication Date:** Published online March 15, 2023; Vol 21, 2024.
*   **What the Source Studies:**
    *   The role of **social bots** in agenda-building during the **Russia-Ukraine war (2022)**.
    *   It analyzes the relationship between bot-generated content and human accounts regarding war narratives.
    *   It investigates how bots amplify specific topics (countries/regions) and whether they exacerbate conflict or advocate peace.
*   **Method and Corpus:**
    *   **Method:** Time-series analysis and **Structural Topic Model (STM)**.
    *   **Corpus:** 159,048 English tweets, 96,004 unique accounts.
    *   **Timeframe:** February 17, 2022 – March 17, 2022 (First month of war).
    *   **Sampling:** Stratified random sampling (5% of data, hourly strata) for bot detection compatibility.
*   **Core Claims:**
    *   **Two-way Agenda-Setting:** There is bidirectional influence between social bots and human accounts at the aggregate level.
    *   **Regional Differences:** Social bots show different or even opposite agenda-setting effects in national/regional discussions (e.g., amplifying pro-Russian vs. pro-Ukrainian narratives depending on the region).
    *   **Multiplicity of Positions:** Bots occupy multiple positions in conversation, revealing complex manipulators (not a monolithic force).
    *   **Conflict Exacerbation:** The end result may exacerbate the conflict of online public opinion rather than advocating peace.
*   **Relevance to Diego's Paper (Context Assumption):**
    *   *Note: "Diego's paper" is not provided in the context. Assuming Diego's paper concerns digital political campaigns (e.g., Chile 2021):*
    *   **High Relevance:** Provides a methodological benchmark for using STM on political text to detect bot influence.
    *   **Comparative Relevance:** Offers a "counter-factual" comparison for campaign analysis. If Diego studies a democratic election (Chile), this source studies a conflict/war zone. It highlights that bot intervention mechanisms (agitation vs. persuasion) may differ.
    *   **Data Limitation:** The source relies on English-only data, which limits relevance if Diego's paper focuses on Spanish-language discourse (Chile).
*   **Cluster Tags:** `#SocialBots`, `#AgendaSetting`, `#InformationWarfare`, `#RussiaUkraine`, `#StructuralTopicModel`, `#TwitterAnalysis`.
*   **Possible Citation Uses:**
    *   Methodological reference for STM application in political bot detection.
    *   Theoretical reference for "Information Warfare" definitions and bot roles (active vs. passive).
    *   Comparative case study for digital manipulation in high-stakes conflicts.
*   **Limits:**
    *   **Language Bias:** Limited to English tweets (85% of data, but filters out Spanish/other languages).
    *   **Time Scope:** Short duration (1 month), may not capture long-term bot strategy evolution.
    *   **Bot Definition:** Relies on detection algorithms; "bot" definition may vary from academic or platform classifications.
*   **Open Questions:**
    *   How do bot strategies change after the initial "false popularity" strategy (e.g., do they pivot to real-time misinformation)?
    *   How does the correlation between bot sentiment and human sentiment differ in non-war contexts (e.g., elections)?

---

### 2. Concept Extraction
*   **Concept of Digitalization/Platformization/Datafication:**
    *   **Digitalization:** Treated as the medium of "Information Warfare." The war is described as a "network battlefield" parallel to the physical one.
    *   **Platformization:** Not explicitly defined as a structural shift (e.g., van Dijck), but described as an "ecology where humans and machines coexist."
    *   **Datafication:** Implied through "big data analysis" and "algorithms" that drive "false popularity."
*   **Actors:**
    *   **Social Bots:** Automated accounts mimicking human behavior (communicative actors).
    *   **Human Accounts:** Ordinary citizens, verified accounts.
    *   **State Actors:** Russia, Ukraine, NATO, EU, US, UK, China, India (implied manipulators behind bots).
    *   **Manipulators:** Described as complex ("multiple positions"), potentially state-sponsored (e.g., Internet Research Agency).
*   **Platform Framing (Channel vs. Infrastructure):**
    *   **Framing:** **Active Infrastructure / Battlefield.**
    *   **Evidence:** The authors describe Twitter as a "network battlefield" and note that algorithms drive "false popularity" and "big data analysis." The platform is not just a passive channel but an active environment where bots leverage algorithmic visibility to shape news agendas.
*   **Geographic Scope:**
    *   **Primary:** Global (Twitter discussion).
    *   **Secondary:** Regional/National (Analysis of tweets mentioning different countries/regions: Russia, Ukraine, China, NATO, EU, etc.).
*   **Mechanisms Linking Platforms to Campaign Strategy:**
    *   **Selective Amplification:** Bots amplify specific issues to gain citizen support.
    *   **Disinformation/False Climate:** Spreading disinformation to create a false perception of reality.
    *   **Echo Chambers:** Leveraging internet to shape information environments (e.g., "pro-Russian bots showed more effective communication").
*   **Chile 2021 Bridge Sentence:**
    *   **Status:** **NOT PRESENT.**
    *   **Explanation:** The provided text is exclusively about the Russia-Ukraine war (2022). There is no reference to Chile, the 2021 Chilean protests, or specific Chilean political campaigns. You cannot extract a bridge sentence connecting this source to Chile 2021 from this text alone.

---

### 3. Methodology Extraction
*   **Method Type:** **Structural Topic Model (STM)** combined with **Time-Series Analysis**.
*   **Corpus:** 159,048 English tweets (96,004 unique accounts).
*   **Validation Strategy:**
    *   **Stratified Random Sampling:** Used hourly strata to randomly select 5% of tweets for compatibility with social bot detection.
    *   **Comparative Validation:** The study implicitly validates topic relevance by comparing bot-generated topics against human-generated topics.
    *   **Bot Detection:** Relies on external detection rules (implied by "rules for social bots detection and analysis"), though specific detection tools are not named in the excerpt provided.
*   **Preprocessing Choices:**
    *   **Language:** Filtered for **English tweets only** (Rationale: English is most common on Twitter, dominates global issue discussions in this context, and makes up 85% of data).
    *   **Retweets/Quotes:** Filtered out; kept only **original tweets**.
    *   **Time Window:** Fixed window (Feb 17 – Mar 17, 2022).
*   **Spanish/Short-Text/Political-Ad Text Handling:**
    *   **Spanish Handling:** **Not handled.** The text explicitly states the exclusion of non-English tweets to ensure compatibility and data dominance.
    *   **Short-Text Handling:** Implicitly handled by STM (which is capable of short text), but the specific tokenization or stop-word removal strategies for Twitter (short text) are not detailed in this excerpt (standard NLP preprocessing is assumed).
*   **Method Limitations:**
    *   **English Bias:** Excluding Spanish/other languages limits generalizability for global South contexts (e.g., Latin America).
    *   **STM Assumptions:** Assumes topics are additive and interpretable; may struggle with nuanced sarcasm or coded language common in bot networks.
    *   **Bot Detection:** Relies on algorithmic detection which can have false positives/negatives.
*   **How to Cite:**
    *   (Zhao, Ren, Zhu, & Zhang, 2024).
    *   Zhao, B., Ren, W., Zhu, Y., & Zhang, H. (2024). Manufacturing conflict or advocating peace? A study of social bots agenda building in the Twitter discussion of the Russia-Ukraine war. *Journal of Information Technology & Politics*, *21*(2), 176–194. https://doi.org/10.1080/19331681.2023.2189201

---

### 4. Paper-Specific Questions to Answer

#### [G3_PLATFORMIZATION_DIGITAL_POLITICS]
*   **Definition of Digitalization/Platformization:**
    *   The source does not provide a formal theoretical definition of "platformization." It defines the context as a **"network battlefield"** and an **"ecology where humans and machines coexist."** It frames digitalization as the operational environment for **"information warfare"** where algorithms create "false popularity."
*   **Mechanisms Named:**
    *   Selective amplification of issues.
    *   Spreading disinformation.
    *   Creating a false climate.
    *   Leveraging algorithmic visibility (big data analysis) to frame issues.
    *   Echo chambers.
*   **Platform Framing (Channel vs. Infrastructure):**
    *   **Infrastructure/Active Agent.** The authors treat Twitter not as a neutral channel but as an active infrastructure where algorithms and bots interact to shape public opinion. The "network battlefield" metaphor supports the infrastructure view.
*   **Scope:**
    *   **Global/Comparative.** The scope is the global Twitter discussion of the war, but it analyzes **regional/national** differences (e.g., how bots amplify different countries). It is **not** a comparative study between two countries' domestic politics, but a comparative analysis of bot impact *within* a global conversation across regions.

#### [G2_TOPIC_MODELING_METHOD]
*   **Method Used:** **Structural Topic Model (STM)**.
*   **Corpus:** 159,048 English tweets (96,004 unique accounts), Feb 17–Mar 17, 2022.
*   **Validation Strategy:** Stratified random sampling (5% hourly strata) for bot detection; Comparative analysis of bot vs. human topic salience.
*   **Topic Number (K):** Not explicitly stated in the provided text (K is typically a parameter set by the researcher, but the abstract does not list the specific K value used).
*   **Preprocessing Choices:**
    *   Language: English only (excluded non-English).
    *   Data Type: Original tweets only (filtered retweets, quotes, replies).
    *   Sampling: Stratified random sampling to ensure compatibility with bot detection.
*   **Spanish/Short-Text Handling:**
    *   **Spanish:** Explicitly excluded (English tweets selected).
    *   **Short Text:** The study acknowledges the nature of Twitter data but does not detail specific techniques (e.g., LIWC, word embeddings) beyond the standard application of STM.
*   **Interpretability/Alternatives:**
    *   STM is noted for better interpretability than standard LDA regarding covariates (which this study uses, likely time and topic).
    *   Alternatives mentioned in literature review include standard topic modeling (LDA) and sentiment analysis.
*   **Method Limitations:**
    *   English-only bias.
    *   STM assumes linear topic distribution which may not capture complex bot coordination.
*   **How to Cite:** (Zhao et al., 2024).

---

### Summary Note on "Chile 2021"
The provided source text is **not applicable** for extracting information regarding the **Chile 2021** protest movement or election. The text is exclusively focused on the Russia-Ukraine war (2022) on Twitter. If you are writing a paper on Chile 2021, this source can only be used as a **methodological reference** (how to study bots) or a **comparative case** (digital conflict vs. domestic protest), but it cannot provide a "bridge sentence" connecting the two events.