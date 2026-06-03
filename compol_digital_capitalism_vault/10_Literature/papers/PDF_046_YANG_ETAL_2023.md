---
type: source_note
status: draft_ra
source_id: PDF_046
filename: YANG_ETAL_2023.pdf
author_year: YANG 2023
clusters:
- G3_PLATFORMIZATION_DIGITAL_POLITICS
- G5_ETHICS_MANIPULATION_RISK
priority: Medium
needs_diego_review: true
---

### 1. Bibliographic Identity and Core Analysis
*   **Bibliographic Identity:** Yang, Y., Davis, T., & Hindman, M. (2021). *Visual Misinformation on Facebook*. (Context: 2020 US Election cycle).
*   **What the source studies:** The prevalence, types, and partisan asymmetry of visual misinformation (images/memes/screenshots) on Facebook during the three months preceding the 2020 US general election.
*   **Method and Corpus:**
    *   **Corpus:** 13,284,364 image posts shared across 14,532 US public pages and 11,454 US public groups. Estimated to cover 94% of US politics image post interactions.
    *   **Methodology:** Manual labeling + Google AutoML for page/group identification. AWS Rekognition for identifying top political figures. Perceptual hashing for identifying widely shared images. Random sampling (1,000 posts) and targeted labeling (top 300 shared images).
*   **Core Claims:**
    *   Visual misinformation is highly prevalent (22.6% of random political image posts; 30-40% of right-leaning posts).
    *   **Partisan Asymmetry:** Right-leaning images are 5 to 8 times more likely to be misleading than left-leaning images.
    *   **Engagement:** Misinformation does not correlate significantly with engagement volume when group membership size is controlled.
    *   **Content:** Includes dehumanization, calls for violence, and sexism (specifically targeting female politicians like Kamala Harris).
*   **Relevance to Diego's paper:** (Assuming a Digital Politics/Platformization thesis) This source provides empirical, large-scale evidence for the "infrastructural" role of platforms in spreading visual falsehoods, countering the "marketplace of ideas" narrative. It supports arguments regarding partisan asymmetry in digital campaigning.
*   **Cluster Tags:** #VisualMisinformation, #PartisanAsymmetry, #FacebookInfrastructure, #DemocracyRisk, #EmpiricalDigitalPolitics.
*   **Possible Citation Uses:** Evidence of the scale of visual disinformation; Methodological precedent for analyzing image-based politics at scale; Counter-evidence to studies claiming misinformation has declined.
*   **Limits:** US-specific (2020 election focus); Public pages/groups only (excludes private messaging/DMs); Reliance on AWS Rekognition accuracy (though validated); Definition of misinformation relies on manual labeling of samples.
*   **Open Questions:** Impact of countermeasures on visual misinformation; Long-term effects of visual dehumanization on democratic trust; Cross-platform generalizability (e.g., TikTok, X).

### 2. Concept of Digitalization and Platform Strategy
*   **Concept of Digitalization/Platformization:** The source frames Facebook not merely as a communication channel but as an **infrastructure** where political communication is heavily concentrated on public pages and groups (millions of followers). It highlights the shift from text/URLs to image-based datafication of political content.
*   **Actors:** Public Pages, Public Groups, State-sponsored entities (context: Russian IRA), Political Candidates/Figures, Algorithmic systems (AWS Rekognition/Hashing).
*   **Platform Framing (Channel vs. Infrastructure):** **Infrastructure.** The authors treat Facebook pages/groups as the primary containers for political discourse, noting that these entities hold reach far exceeding individual users (5,000 friends limit).
*   **Geographic Scope:** USA (United States).
*   **Mechanisms Linking Platforms to Campaign Strategy:**
    *   **Persuasion:** Visual content is inherently more persuasive than text/links.
    *   **Visibility:** Public pages/groups allow for mass distribution without peer limits.
    *   **Asymmetry:** The platform architecture facilitates the spread of right-leaning imagery more effectively than left-leaning imagery (observed via data).
*   **Chile 2021 Bridge Sentence:** "While this analysis focuses on the US 2020 election, the infrastructural role of visual misinformation on public pages suggests a parallel vulnerability in the Chile 2021 digital ecosystem, where similar partisan asymmetries may be amplified through comparable platform dynamics."
*   **G3_PLATFORMIZATION_DIGITAL_POLITICS Answers:**
    *   **Definition:** Digitalization is the prevalence of image-based political communication; Platformization is the concentration of this communication within public page structures.
    *   **Mechanisms:** Visual persuasiveness, sharing bias, group membership dynamics.
    *   **Platform Framing:** Active Infrastructure (Pages/Groups hold reach).
    *   **Scope:** Local (US), Comparative (Left vs. Right).

### 3. Risks, Ethics, and Evidence
*   **Risks Named:** Misinformation, Polarization (implied by asymmetry), Dehumanization (Democrats as "cockroaches"), Sexism (misogyny against female politicians), Calls for Political Violence.
*   **Empirical Evidence vs. Speculation:** **Empirical Evidence.** Based on 13M+ posts and manual labeling. The authors explicitly contrast this with speculation regarding URL-based fake news.
*   **Microtargeting (Inherent Harm/Over-feared):** The paper does *not* focus on microtargeting (private ads). It argues that **public** visual misinformation is the larger problem, suggesting fears about private targeting may underestimate the scale of public visual falsehoods.
*   **Platform/Campaign/Regulator Roles:**
    *   **Platform:** Provides the infrastructure (Facebook) that enables mass reach.
    *   **Campaigns:** Right-wing public pages/groups are the primary drivers of the misinformation ("tsunami of falsehoods").
    *   **Regulator:** Not discussed in terms of policy, but implied need for intervention ("difficult to imagine any additional analysis that could alter our core findings").
*   **Counterargument:** Previous studies claimed misinformation consumption is "negligible" (based on URL/link sharing). This source counters that image sharing is the dominant vector for falsehoods.
*   **Ethics/Evidence Debate Framing Sentence:** "The very pervasiveness of visual misinformation on Facebook makes its impacts difficult to measure, but they are likely to be highly corrosive to democratic self-government, challenging the glib responses about the virtues of the 'marketplace of ideas.'"

### 4. Paper-Specific Questions Answered
*   **[G3_PLATFORMIZATION_DIGITAL_POLITICS]**
    *   **Definition:** Defined by the dominance of image-based content over text/URLs on public pages.
    *   **Mechanisms:** Visual persuasion, high sharing rates, and asymmetric partisan targeting in public groups.
    *   **Framing:** **Active Infrastructure.** Facebook is treated as a venue where political actors (pages) build audiences, not just a passive pipe.
    *   **Scope:** Comparative (Right vs. Left), but geographically local (US).
*   **[G5_ETHICS_MANIPULATION_RISK]**
    *   **Democratic Risk:** Misinformation, Dehumanization, and Polarization. The risk is that falsehoods are "highly corrosive to democratic self-government."
    *   **Manipulation vs. Evidence:** The concern is **Manipulation/Persuasion** via images. The source distinguishes fear from evidence by providing large-scale data proving the prevalence (20%+) and asymmetry, contradicting the "negligible" narrative.
    *   **Distinction:** The authors argue the "marketplace of ideas" is a myth in the face of this volume, implying the risk is systemic, not just individual user error.