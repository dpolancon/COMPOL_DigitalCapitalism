---
type: source_note
status: draft_ra
source_id: PDF_039
filename: SCHMOKEL_ETAL_2022.pdf
author_year: SCHMOKEL 2022
clusters:
- G3_PLATFORMIZATION_DIGITAL_POLITICS
- G5_ETHICS_MANIPULATION_RISK
priority: Medium
needs_diego_review: true
---

### 1. Bibliographic Identity & Source Analysis

**Bibliographic Identity:**
*   **Title:** FBAdLibrarian and Pykognition: open science tools for the collection and emotion detection of images in Facebook political ads with computer vision
*   **Authors:** Rasmus Schmøkel & Michael Bossetta
*   **Journal:** Journal of Information Technology & Politics
*   **Year/Vol:** 2022, Vol. 19, No. 1
*   **DOI:** 10.1080/19331681.2021.1928579
*   **License:** Open Access (Creative Commons Attribution-NonCommercial)

**What the Source Studies:**
The source studies the **methodological workflow** for collecting and analyzing visual content (images and videos) in political advertisements on Facebook using Computer Vision (CV). It focuses on the technical implementation of tools to access the Facebook Ad Library API and detect facial emotions.

**Method and Corpus:**
*   **Method:** Computer Vision techniques (K-means clustering, Convolutional Neural Networks/VGG19), Python scripting (FBAdLibrarian, Pykognition), AWS Rekognition API (emotion detection), and API scraping.
*   **Corpus:** Paid political ads on Facebook/Instagram/Messenger during the **2020 US Presidential Primary Elections**.
    *   **Candidates:** 8 candidates (Donald Trump + 7 Democratic challengers).
    *   **Volume:** 221,136 ads collected (filtered to ~90,432 images after deduplication).
    *   **Timeframe:** Focused on the month before Super Tuesday (March 2020), though API data extended back to October 2019.

**Core Claims:**
1.  **Rarity of Unique Imagery:** Unique images of candidates represent less than 0.1% of overall ads; most are duplicates with text overlays.
2.  **Emotional Tone:** Candidates predominantly display **Happiness** and **Calm**.
3.  **Attack Ads:** Candidates rarely attack opponents in image-based ads from official pages. When they do, opponents are portrayed using negative emotions (Anger, Sadness, Fear).
4.  **Methodological Utility:** Open-source tools (FBAdLibrarian/Pykognition) are necessary because the Ad Library API lacks systematic visual export features.

**Relevance to Diego's Paper:**
*   *Note: Specifics of "Diego's paper" are unknown.*
*   **Potential Context:** Relevant if Diego's paper investigates **methodological transparency**, **affective computing in politics**, **US election studies**, or the **limitations of platform APIs**. It offers a technical methodology that could be replicated or compared against other digital methods papers.
*   **Methodological Alignment:** If Diego's paper critiques the "black box" of platforms, this source provides a counter-example of opening that box via open science tools.

**Cluster Tags:**
`#DigitalMethods` `#ComputerVision` `#PoliticalCampaigning` `#AffectiveIntelligence` `#OpenScience` `#FacebookAdLibrary` `#USPolitics` `#Methodology`

**Possible Citation Uses:**
*   Methodological tutorial for scraping social media ad images.
*   Empirical evidence for the emotional tone of political ads (Happiness/Calm vs. Anger).
*   Critique of platform transparency (limitations of Ad Library).
*   Example of using AWS Rekognition in political science.

**Limits:**
*   **Platform Constraints:** Relies on the Facebook Ad Library API, which has verification hurdles and limited visual export features.
*   **Deduplication:** Pixel-based deduplication can miss slight variations (text/location) requiring manual filtering.
*   **Scientific Validity:** Explicitly notes "weak scientific evidence" that external facial expressions accurately reflect internal emotional states (citing Barrett et al., 2019).
*   **Scope:** Focused on official campaign pages, excluding organic posts or third-party ads.

**Open Questions:**
*   How do these findings hold up in other electoral contexts (non-US, different parties)?
*   Does the "industry-grade" algorithm bias emotion detection in political contexts?
*   What is the impact of these ad images on actual voter behavior vs. just strategic messaging?

---

### 2. Concept Extraction & Specific Analysis

**Concept of Digitalization/Platformization/Datafication:**
*   **Status:** The text **does not explicitly define** "digitalization," "platformization," or "datafication" as theoretical constructs.
*   **Context:** It operates within a context of **datafication** (making ads visible via the API) and **platformization** (platforms embedding images into ads and controlling access via API).
*   **Platform Framing:** The platform (Facebook) is framed primarily as a **Channel** for persuasion (embedding images in ads) and a **Data Stream** for researchers (via API). It is treated as a semi-opaque infrastructure where transparency is limited (citing Leerssen et al., 2018).
*   **Actors:** Campaigns (strategic messaging), Platform (Facebook/Rekognition API), Researchers (Schmøkel & Bossetta), and Voters (implied recipients of emotional messaging).

**Geographic Scope:**
*   **Local/Specific:** United States (2020 Presidential Primaries).
*   **Bridge Sentence for Chile 2021:** *Not available.* **The source text contains no information regarding Chile 2021.** It focuses exclusively on the 2020 US Primary Elections.

**Mechanisms Linking Platforms to Campaign Strategy:**
*   **Affective Intelligence Theory (AIT):** The platform used to deliver emotional configurations designed to mobilize (Disposition system: Happy/Sad/Anger) or demobilize information-seeking (Surveillance system: Fear/Calm/Surprised).
*   **Visual Persuasion:** Leveraging non-verbal cues (facial expressions) which humans prioritize in information processing.

**Risks Named (Manipulation/Privacy/Polarization):**
*   **Primary Focus:** The paper does not focus on risks like manipulation, privacy, or polarization. It focuses on *measuring* content.
*   **Acknowledged Risks/Limitations:**
    *   **Opacity:** The Ad Library lacks detail on targeting practices (citing Bossetta, 2020).
    *   **Verification:** Issues with defining a "political" ad.
    *   **Emotion Accuracy:** Weak evidence that facial expressions reveal internal states (potential for misinterpretation/misuse).
    *   **Demobilization:** AIT suggests the "Surveillance system" (Fear/Calm) may demobilize participation.

**Empirical Evidence vs. Speculation:**
*   **Evidence:** Empirical data from 221k ads shows candidates display happiness/calm; attacks are rare.
*   **Speculation/Weak Evidence:** The interpretation of these emotions as internal states is labeled as having "weak scientific evidence." The link between displayed emotion and actual voter behavior is theoretical (AIT).

**Microtargeting & Harm:**
*   **Inherent Harm:** Not discussed. The paper treats the tools as neutral "open science" instruments.
*   **Over-feared:** Implied that the Ad Library lacks transparency on targeting ("scholars have noted shortcomings... regarding targeting practices"), but the paper itself does not argue microtargeting is inherently harmful, only that it remains opaque.

**Platform/Campaign/Regulator Roles:**
*   **Campaign:** Strategic use of emotional display for persuasion/fundraising.
*   **Platform:** Provides transparency via Ad Library but controls access via API verification; acts as an opaque infrastructure for targeting.
*   **Regulator:** Not discussed.
*   **Ethics/Evidence Debate Framing Sentence:** "It should be noted that scientific evidence is weak that internal emotional states can be detected from facial expressions... However, we consider these labels valuable for classifying external facial configurations, especially for public actors who engage in strategic messaging."

---

### 3. Paper-Specific Questions (G3 & G5)

**[G3_PLATFORMIZATION_DIGITAL_POLITICS]**
*   **Definition of Digitalization/Platformization:** **Not explicitly defined.** The text treats digital political communication as the existing context ("political campaigns increasingly incorporate social media") and focuses on the *tools* to analyze it rather than the *theory* of platformization.
*   **Mechanisms Named:** Computer Vision, API scraping, K-means clustering, Affective Intelligence Theory (Disposition vs. Surveillance systems).
*   **Passive Channels vs. Active Infrastructures:** The platform is treated as a **Channel** for ads, but an **Active Infrastructure** regarding data governance (API access, verification, cost per image). The authors argue for "open science" to bypass platform opacity.
*   **Scope:** **Local/Case Study.** Focused on the 2020 US Primary Elections (specifically Democrats vs. Trump).

**[G5_ETHICS_MANIPULATION_RISK]**
*   **Democratic Risk Identified:** **Affective Mobilization/Demobilization.** Based on AIT, risks include demobilization via anxiety (Fear/Calm) or reification of partisan preferences via enthusiasm (Happy/Sad). Secondary risk is **Opacity** regarding targeting.
*   **Specific Concern:** **Manipulation** (via emotional configurations), **Opacity** (targeting data not visible to researchers), and **Scientific Validity** (risk of misinterpreting facial expressions).
*   **Fear vs. Evidence:** The authors explicitly **distinguish** between the fear of emotional manipulation (industry technology) and the **evidence** available (weak scientific support for internal state detection, but strong empirical data on *displayed* emotions). They argue that while scientific evidence for internal state detection is weak, the *external* classification is valuable for strategic analysis.