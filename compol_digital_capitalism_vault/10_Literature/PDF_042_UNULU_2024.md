---
type: source_note
status: draft_ra
source_id: PDF_042
filename: UNULU_2024.pdf
author_year: UNULU 2024
clusters:
- G3_PLATFORMIZATION_DIGITAL_POLITICS
- G2_TOPIC_MODELING_METHOD
priority: Medium
needs_diego_review: true
---

### 1. Bibliographic Identity & Overview

*   **Bibliographic Identity:**
    *   **Authors:** Ali Unlu, Sophie Truong, Nitin Sawhney, Tuukka Tammi.
    *   **Title:** Setting the misinformation agenda: Modeling COVID-19 narratives in Twitter.
    *   **Journal:** *New Media & Society*.
    *   **Year/Vol:** 2024, Vol. 27(7).
    *   **Pages:** 3973–3997.
    *   **DOI:** 10.1177/14614448241232079.
*   **What the Source Studies:**
    *   The dynamics of **COVID-19 misinformation spread** on Twitter.
    *   The formation of digital communities and their role in **agenda-setting** during a health crisis.
    *   How specific groups (influential/diverse communities) introduce narratives and how these spread to niche groups.
*   **Method & Corpus:**
    *   **Methods:** Text classification (to identify misinformation), BERTopic (for topic modeling), Social Network Analysis (Community Detection using Leiden Algorithm), Correspondence Analysis (CA).
    *   **Corpus:** 1.6 million Finnish tweets.
    *   **Timeframe:** December 2019 – October 2022.
    *   **Language:** Finnish.
*   **Core Claims:**
    *   Misinformation spreads from "influential, diverse communities" to "niche groups."
    *   This creates an "agenda-setting effect" amplified by platform algorithms optimized for engagement.
    *   Actors in misinformation networks are ambiguous (users, bots, trolls, activists).
    *   Agenda-Setting Theory (AST) can be operationalized at three levels in digital spaces (Coverage, Framing/Attributes, Community Agenda).
*   **Relevance to Diego's Paper (Hypothetical Context):**
    *   **Methodological Transfer:** If Diego's paper analyzes elections or political discourse, this study provides a blueprint for combining **Topic Modeling (BERTopic)** with **Network Analysis** to trace narrative flow.
    *   **Theoretical Extension:** It validates the application of **Agenda-Setting Theory** to digital networks. Diego could adapt the "three levels of AST" to Chilean political actors.
    *   **Contrast:** This study focuses on *health misinformation* in a *stable democracy* (Finland), whereas Diego's likely focuses on *political campaign dynamics* in a *polarized context* (Chile 2021). This contrast highlights the need to adjust "community detection" parameters for higher volatility in political campaigns compared to health crises.
*   **Cluster Tags:**
    *   `#Misinformation`, `#AgendaSetting`, `#BERTopic`, `#Twitter`, `#NetworkAnalysis`, `#Finland`, `#Pandemic`
*   **Possible Citation Uses:**
    *   **Methodology Section:** To justify the use of BERTopic for short political texts.
    *   **Theory Section:** To support the argument that social media communities, not just traditional media, drive agenda setting.
    *   **Discussion Section:** To compare the "niche group" spread mechanism in Finland with "viral" spread in Chilean election contexts.
*   **Limits:**
    *   **Geographic:** Limited to Finland; linguistic isolation makes it hard to generalize to other contexts (e.g., Chile).
    *   **Platform:** Twitter/X bias (bot susceptibility, representativeness).
    *   **Validation:** Specific validation metrics for classification accuracy or topic coherence are not detailed in the provided pages.
*   **Open Questions:**
    *   How does the "ambiguity" of actors (bots vs. humans) impact the validity of "community detection" in other contexts?
    *   Does the "agenda melding" effect observed here hold true for multi-party election systems like Chile's?

---

### 2. Concept Extraction (Digitalization, Actors, Platform, etc.)

*   **Concept of Digitalization/Platformization/Datafication:**
    *   *Not explicitly defined as a standalone theory.* The text treats "the digital age" as a landscape where social media reshapes information dissemination. It acknowledges the "rise of social media platforms" but focuses more on **content dynamics** than the structural "platformization" of society.
*   **Actors:**
    *   Influential opinion leaders (celebrities, politicians, journalists).
    *   Communities (defined by interaction: retweets/mentions).
    *   Bot/Malicious actors (mentioned as ambiguous sources).
    *   Anonymous activists and political groups.
*   **Platform Framing (Channel vs. Infrastructure):**
    *   **Framing:** Primarily treated as a **Channel/Media Outlet** ("decentralized stage," "media outlet").
    *   **Infrastructure:** Acknowledged as having active algorithms ("optimized for engagement") that amplify agenda-setting effects. It oscillates between a passive channel and an active infrastructure influencing reach.
*   **Geographic Scope:**
    *   **Local/National:** Finland.
    *   *Note:* The text explicitly highlights "linguistic singularity" as a way to minimize cross-context influence, making it a **controlled local case**, not a comparative global study.
*   **Mechanisms Linking Platforms to Campaign Strategy:**
    *   **Agenda Melding:** Sustaining group consensus through sharing similar content.
    *   **Influencer Diffusion:** High-profile figures facilitate diffusion of media agendas.
    *   **Algorithmic Amplification:** Engagement optimization drives the spread of misinformation agendas.
*   **Chile 2021 Bridge Sentence:**
    *   *Status:* **Not present in the provided text.**
    *   *Note:* The provided pages (1-5) focus exclusively on Finland and COVID-19. There is no mention of Chile, 2021, or elections.
    *   *Suggestion for Bridge:* You must create this bridge yourself. Example: *"While Unlu et al. (2024) map agenda-setting in Finnish health crises, a similar network topology likely underpins the political polarization observed in Chile's 2021 presidential campaign (Diego, 2024), suggesting..."*

---

### 3. Method Extraction (Technical Details)

*   **Method Type:**
    *   **Topic Modeling:** **BERTopic** (specifically mentioned).
    *   **Community Detection:** **Leiden Algorithm** (within Social Network Analysis).
    *   **Statistical Analysis:** **Correspondence Analysis (CA)**.
    *   **Classification:** **Text Classification** (specific library not named, but `academictwitteR` mentioned for extraction).
*   **Corpus:**
    *   1.6 million tweets.
    *   Query words related to "COVID-19 and vaccinations."
    *   Timeframe: Dec 1, 2019 – Oct 24, 2022.
*   **Validation Strategy:**
    *   *Snippet Status:* **Not detailed.** The text claims "text classification... identifies misinformation" but does not provide F1 scores, precision/recall, or topic coherence scores in this section.
*   **Preprocessing Choices:**
    *   Extraction tool: **R package `academictwitteR`**.
    *   Language Handling: **Finnish** (requires specific tokenizer).
    *   Short-text handling: BERTopic is noted to handle "short text," but specific tokenization/stopword removal details are not in the snippet.
*   **Spanish/Short-text/Political-ad Handling:**
    *   **Spanish:** **No.** This study is Finnish.
    *   **Short-text:** The study *does* analyze short tweets, but the specific preprocessing (e.g., handling hashtags, emojis, or casing) is not detailed in this snippet.
    *   **Political-ad:** Not applicable (Health crisis focus).
*   **Method Limitations:**
    *   **Twitter Bias:** Acknowledged representativeness issues and bot susceptibility.
    *   **Interpretability:** Topic modeling (BERTopic) requires interpretation of "topics" which can be subjective.
    *   **Ambiguity:** Difficulty distinguishing between bots and human users in network analysis.
*   **How to Cite (Method):**
    *   *Example:* "Following Unlu et al. (2024), we employed BERTopic to model the semantic structure of short-form political text..."

---

### 4. Paper-Specific Questions ([G3] & [G2])

#### [G3_PLATFORMIZATION_DIGITAL_POLITICS]
*   **How does the source define digitalization/platformization?**
    *   It does not explicitly define "platformization." It defines the landscape as "ubiquity and pervasiveness of social media platforms" reshaping information dissemination from a traditional media monopoly to a "decentralized stage."
*   **What mechanisms are named?**
    *   Agenda melding (sustaining group consensus).
    *   Diffusion through influential opinion leaders.
    *   Algorithmic optimization for engagement (amplifying agenda-setting).
    *   Community detection based on retweet and mention networks.
*   **Does it treat platforms as passive channels or active infrastructures?**
    *   **Active Infrastructure.** It notes that "social media algorithms optimized for engagement" amplify the agenda-setting effect, moving beyond the platform as a mere carrier of content.
*   **Is the pattern global, local, or comparative?**
    *   **Local/National.** The study is explicitly situated in Finland ("unique context of Finland," "linguistically distinct environment"). It is not presented as a global comparative study.

#### [G2_TOPIC_MODELING_METHOD]
*   **What method is used?**
    *   **BERTopic** (for topics), **Leiden Algorithm** (for communities), **Correspondence Analysis** (for mapping topics to communities).
*   **What corpus?**
    *   1.6 million Finnish tweets (Dec 2019–Oct 2022).
*   **What validation strategy?**
    *   *Not detailed in provided pages.* (Usually requires checking topic coherence scores or classification accuracy metrics).
*   **Topic number K if any?**
    *   *Not detailed in provided pages.*
*   **What preprocessing choices?**
    *   Used `academictwitteR` for extraction. Language is Finnish.
*   **Does it discuss short texts, Spanish, interpretability, or alternatives to LDA?**
    *   **Short texts:** Yes, BERTopic is chosen (implied suitability for short text compared to LDA).
    *   **Spanish:** No (Study is Finnish).
    *   **Interpretability:** Yes, via Correspondence Analysis to link topics to communities.
    *   **Alternatives to LDA:** Yes, explicitly uses **BERTopic** instead of traditional Latent Dirichlet Allocation.
*   **Does it discuss how to cite?**
    *   Yes, the paper lists authors and DOI, but does not provide a specific "Method Citation" guide, though standard academic citation of the authors is implied.