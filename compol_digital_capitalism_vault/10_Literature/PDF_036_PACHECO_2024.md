---
type: source_note
status: draft_ra
source_id: PDF_036
filename: PACHECO_2024.pdf
author_year: PACHECO 2024
clusters:
- G4_CHILE_LATAM_CASE_CONTEXT
- G3_PLATFORMIZATION_DIGITAL_POLITICS
priority: Review
needs_diego_review: true
---

### 1. Bibliographic Identity & Source Analysis

**Bibliographic Identity**
*   **Author:** Diogo Pacheco (University of Exeter, UK)
*   **Title:** Bots, Elections, and Controversies: Twitter Insights from Brazil’s Polarised Elections
*   **Venue:** Proceedings of the ACM Web Conference (WWW'24)
*   **Year:** 2024
*   **DOI:** https://doi.org/10.1145/3589334.3645651
*   **License:** Creative Commons Attribution-International 4.0 License

**Source Study & Corpus**
*   **Country/Election Studied:** **Brazil**. Specifically, the 2018 and 2022 presidential election cycles.
*   **Context Distinctiveness:** Brazil is characterized in the source as a "polarised" context marked by political turmoil (impeachment, coup attempts), conspiracy theories, and high misinformation rates. It notes Brazil has been at the forefront of developing computational methods for detecting propaganda and misinformation in Latin America.
*   **Corpus:** 437 million tweets from 13 million distinct accounts.
    *   **Time Span:** August 30, 2018, to March 14, 2023 (1,657 days).
    *   **Subjects:** 14 presidential candidates (2018) and 13 candidates + 27 political parties (2022).
*   **Methodology:**
    *   **Data Collection:** Twitter Streaming API.
    *   **Analysis Techniques:** Network analysis (connected components/shared handles), temporal analysis, correlation analysis (bot engagement vs. replies), and bot detection using **Botometer Lite**.
    *   **Metrics:** Daily bot score, account creation dates ("birthdays"), tweet types (retweets vs. replies).

**Core Claims**
*   **Bot Engagement:** There is a strong positive correlation ($r = 0.66$) between bot engagement and the volume of replies.
*   **Account Coordination:** A sprawling network of coordinated accounts exists, sharing Twitter handles (screen names), with some accounts utilizing over 100 distinct handles.
*   **Temporal Patterns:** Bot engagement shows a quasi-monotonic escalation with notable surges during the 2020 pandemic and the aftermath of the 2022 election.
*   **Platform Behavior:** The platform functions as an infrastructure for polarization, where bot-like activity intensifies during crises (coups, pandemics) and remains high post-election.

**Relevance to Diego's Paper (Chile Context)**
*   **Comparative Baseline:** Since the user's paper (Diego's) likely focuses on **Chile** (indicated by "Chile 2019 uprising", "Chile 2021"), this source provides a **LatAm comparative benchmark**. It demonstrates that the mechanisms of digital polarization (bots, handle sharing, coordinated inauthentic behavior) are present in neighboring Brazil.
*   **Methodological Transfer:** The source's methodology (Botometer Lite, network analysis of shared handles) offers a technical blueprint for analyzing similar data in Chile.
*   **Thematic Alignment:** Both Brazil and Chile (2021 constitutional process) experienced high polarization and political upheaval, making this source a valid theoretical parallel for platformization dynamics.

**Cluster Tags**
`#LatinAmerica` `#DigitalPolarization` `#BotDetection` `#TwitterAnalysis` `#BrazilPolitics` `#Misinformation` `#NetworkAnalysis` `#ElectionStudies`

**Possible Citation Uses**
*   **Methodological Reference:** "Following Pacheco et al. (2024), we utilized Botometer Lite to assess bot scores..."
*   **Contextual Comparison:** "Similar to the findings in Brazil's polarized 2018-2022 cycle [Pacheco, 2024], Chile's 2021 constitutional debate saw..."
*   **Theoretical Support:** "The platformization of political discourse, where platforms act as active infrastructures for coordination rather than passive channels, is evidenced by Pacheco's (2024) analysis of Brazil."

**Limits**
*   **Bot Detection Accuracy:** Acknowledges Botometer Lite is not infallible (false positives/negatives) and does not provide exact bot counts, only trends.
*   **Account Churn:** The study does not deeply assess the dynamics of accounts exiting the conversation (churn), limiting longitudinal understanding of account lifecycles.
*   **Geographic Scope:** Strictly limited to Brazil; findings may not fully transfer to Chile's specific media landscape (e.g., WhatsApp role mentioned in Brazil, which differs from Chile's ecosystem).

**Open Questions**
*   **Bot Retention:** What happens to bot accounts after they are suspended or cease activity? (Source notes plans for future research on this).
*   **Human vs. Bot Coordination:** The study distinguishes "suspicious users" (bots + humans) but does not fully disentangle human-led coordination from automated bots in specific campaigns.
*   **Platform Response:** How effective are platform interventions (e.g., Twitter/X policies) in mitigating the sustained bot spikes observed post-election?

---

### 2. Contextual Extraction: Country & Chile Comparison

*Note: The following section addresses the specific extraction instructions regarding Chile. As the source text is about Brazil, specific Chilean data points are marked as "Not in Source".*

**Country/Election Studied:**
*   **Country:** Brazil
*   **Election:** 2018 Presidential Election (Bolsonaro victory) and 2022 Presidential Election (Lula victory).
*   **Chile 2019 Uprising / Constitutional Process:** **Not discussed in source.** (Source focuses on Brazil's 2018-2023 cycle).
*   **Party Fragmentation:** Discussed in the context of Brazil (27 federal units, multi-party system).
*   **Candidate References:** Jair Bolsonaro, Lulada Silva, Sergio Moro. (No Chilean candidates referenced).
*   **LatAm Distinctiveness:** The source explicitly positions Brazil as a "frontier" for computational methods for misinformation in Latin America, citing other LatAm studies (WhatsApp groups in Brazil 2018).

**Contrast Case for Chile 2021:**
*   **Source Contrast:** Brazil (2018/2022) serves as a **parallel case** rather than a direct contrast. It highlights that while Chile 2021 focused on constitutional reform, the *underlying digital mechanisms* (bot spikes, polarization) analyzed here in Brazil are structurally similar.
*   **Data Gap:** The source does not contain data for Chile 2021.
*   **Justification Sentence for Chile as Theoretical Case:**
    > "Although this study centers on Brazil, the mechanisms of platformization and bot coordination described provide a transferable theoretical framework for analyzing similar polarized dynamics in Chile's 2021 constitutional process, where digital infrastructure similarly outpaced effective regulatory containment."

---

### 3. Concept of Digitalization & Platform Framing

**Concept of Digitalization:**
*   **Definition:** Digitalization is framed here as **platformization**, where social media platforms (specifically Twitter) are no longer just communication tools but primary mediums for campaigns, debates, and recruitment.
*   **Actors:** Candidates, political parties, bots (automated accounts), and coordinated human actors.
*   **Platform Framing:**
    *   **Infrastructure vs. Channel:** The source treats platforms as **active infrastructures**. The text notes that platforms host "coordinated groups" and that bot activity creates "ferment for misinformation," implying the platform architecture facilitates rather than just transmits content.
    *   **Framing Evidence:** The analysis of "screen name sharing" and "bot scores" suggests the platform's identity layer (handles, profiles) is weaponized, moving beyond a passive channel function.
*   **Geographic Scope:** Primarily **Global** in theoretical discussion (mentions US, Germany, France, Africa, Asia-Pacific, EU), but **Local/Specific** in empirical data (Brazil).
*   **Mechanisms Linking Platforms to Campaign Strategy:**
    *   **Replies vs. Retweets:** Bots prefer **replies** (higher engagement/discourse) over retweets (propaganda), shifting strategy from amplification to debate disruption.
    *   **Volume:** High tweet volume (up to 100,000 tweets from single accounts) and "newborn" account creation spikes are used to flood discourse.
    *   **Timing:** Engagement spikes are synchronized with political events (elections, coups, pandemics).

**Chile 2021 Bridge Sentence:**
> "Consequently, while this study focuses on Brazil, the observation that platforms transition from propaganda channels to active debate infrastructures following an election offers a critical lens for examining the post-2021 digital consolidation of political factions in Chile."

---

### 4. Paper-Specific Questions (G3 & G4)

**[G4_CHILE_LATAM_CASE_CONTEXT]**
*   **Which country/election is studied?** Brazil (2018 and 2022 Presidential Elections).
*   **What makes the context distinctive?** It is characterized by extreme polarization, conspiracy theories, and high bot activity. It is noted as a leader in computational methods for misinformation detection in Latin America.
*   **Does it discuss Chile 2021, post-2019 politics, party fragmentation, LatAm platforms, or regional campaign practices?**
    *   **Chile 2021/Post-2019:** No.
    *   **Party Fragmentation:** Yes (in the Brazilian context).
    *   **LatAm Platforms:** Yes (positions Brazil as a leader in LatAm digital misinformation research).
    *   **Regional Campaign Practices:** Yes (compares to US, Germany, Europe, Africa, Asia-Pacific).

**[G3_PLATFORMIZATION_DIGITAL_POLITICS]**
*   **How does the source define digitalization/platformization?** As the shift where platforms become "primary mediums for campaigns, debates, and recruitment," allowing for "sprawling networks of coordinated accounts."
*   **What mechanisms are named?** Bot engagement, shared screen names (handle coordination), account creation spikes ("birthdays"), and the ratio of replies to retweets.
*   **Does it treat platforms as passive channels or active infrastructures?** **Active infrastructures.** The text describes the platform as an environment where "politicized discourse" evolves and where "bot activity" intensifies during specific political moments, implying the platform's architecture is complicit in the spread.
*   **Is the pattern global, local, or comparative?** **Comparative.** The empirical study is local (Brazil), but the discussion is explicitly comparative (referencing US, Europe, Africa, etc.).