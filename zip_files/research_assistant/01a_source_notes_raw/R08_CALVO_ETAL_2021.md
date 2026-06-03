

# N049_PDF008_P00


It looks like you accidentally pasted your instructions twice instead of including the NotebookLM output you wanted me to convert!

However, since we previously completed all the source extractions for **Luna et al. (2023)** earlier in our conversation, I have proactively converted those findings into your requested Obsidian source note format.

If you meant to paste a completely different source, please just paste it in your next message and I will format it for you!

---

```
---
type: source_note
status: draft_ra
source_id: LUNA_ETAL_2023
filename: LUNA_ETAL_2022_CHILE.pdf
author_year: Luna et al. 2023
clusters: Structural Inequality, Digital Welfare, Topic Modeling, Local Governance, Platformization
priority: High
needs_diegeo_review: no
---

# Luna et al. 2023 — Local Government, Social Media and Management of COVID-19

## Bibliographic identity
*   **Author(s):** Juan Pablo Luna, Daniel Alcatruz, Cristian Pérez Muñoz, Fernando Rosenblatt, Sergio Toro Maureira, and Sebastián Valenzuela.
*   **Year:** 2023.
*   **Title:** Local Government, Social Media and Management of COVID-19: The Case of Chilean Mayoral Communication.
*   **Journal:** *Political Communication*.
*   **DOI:** 10.1080/10584609.2023.2290494.

## What this source studies
*   The study analyzes how local political leaders (mayors) use social media to communicate with constituents during a crisis (the COVID-19 pandemic), following the severe institutional crisis of the October 2019 social uprising.
*   It explicitly tests whether digital communication strategies are primarily driven by political variables (partisanship, electoral incentives) or by structural and socioeconomic factors (poverty, material dependency).

## Method and corpus
*   **Data Collection:** Collected a corpus of 264,387 organic posts scraped via APIs from the personal and institutional Facebook, Instagram, and Twitter accounts of all 52 city mayors in the Santiago Metropolitan Region (March 3, 2020 – June 28, 2021).
*   **Analysis:** Employed Structural Topic Models (STM) to identify latent themes (*k*=25, retaining 7 for final analysis).
*   **Covariates:** Successfully integrated external covariates at the document level, including poverty rate, COVID-19 cases, population size, rural/urban dummy, mayoral incumbency, and political alignment.

## Core claims / findings
*   **The "Structural Override":** Socioeconomic context (specifically poverty levels) heavily dictates a municipality's social media strategy, overriding purely political calculations. Variables like mayoral incumbency or alignment with the national government had no significant effect.
*   **Digital Welfare Dependency ("Street-Level Bureaucracy"):** Because vulnerable populations rely on the local state for survival, strict lockdowns forced poorer municipalities to dramatically increase social media posting to coordinate critical welfare assistance. Wealthier municipalities (relying on private provision) did not alter their posting behavior.
*   **Engagement Dynamics:** Poorer and rural municipalities generated the highest levels of citizen engagement per post, driven by structural dependency on the state rather than local COVID-19 severity.
*   **Platform-Specific Affordances:** Twitter was heavily favored for broadcasting public health and prevention messaging, whereas Facebook acted as the primary infrastructure for organizing social support networks and citizen registries.

## Relevance to Diego paper
*   **Methodological Precedent:** Provides a highly relevant, legitimating peer-reviewed precedent in *Political Communication* for applying STM to a massive corpus of short, Spanish-language social media texts and successfully integrating structural covariates.
*   **Chile / LatAm Context:** Validates the necessity of studying Latin American cases, demonstrating how profound structural inequalities dictate state-citizen digital relationships during crises of representation.
*   **Platformization / Digital Politics:** Counters the universal "technological disruption" narrative by proving that platforms absorb and replicate pre-existing structural power dynamics and act as active infrastructures for state governance, heavily bounded by socioeconomic realities.

## Cluster tags
#structural_inequality #digital_welfare #topic_modeling_STM #chile_politics #platform_infrastructure #political_communication

## Possible citation uses
*   "Use this source as a legitimating methodological precedent to justify the use of Structural Topic Modeling (STM) combined with structural covariates on Spanish-language social media data within *Political Communication*."
*   "Use this source to show that in highly unequal societies, digital communication strategies and platform engagement are driven more by socioeconomic realities and structural state dependency than by pure ideological or partisan alignment."
*   "As Luna et al. (2023) demonstrate, social media platforms do not supplant structural factors in political communication; rather, their usage reflects pre-existing inequalities, functioning as essential digital welfare infrastructure for vulnerable populations during institutional crises."

## Limits / do not infer
*   **Unobserved Mechanisms:** Does not account for the size and professionalization of municipal public relations departments, nor the mitigating influence of traditional broadcast media (local radio/TV).
*   **Geographic Scope:** Strictly restricted to the Santiago Metropolitan Region; it does not capture dynamics in the extreme north or south of Chile.
*   **Paid Ads/Manipulation Focus:** This study has null relevance for analyzing the mechanics, spending, dark posts, or regulatory evasion of paid political advertising. It strictly analyzes organic posts and does not focus on computational propaganda, manipulation, or misinformation risks.

## Open questions for checkpoint
*   Given that this study serves as a *complementary* precedent focusing on local mayors during a health crisis, how should Diego theoretically bridge this to study other political actors (e.g., national candidates or constitutional delegates) while leveraging the same methodological foundation?
```




# N050_PDF008_P01


**1. Bibliographic identity**

- **Author(s):** Ernesto Calvo and Tiago Ventura.
- **Year:** 2021.
- **Title:** Will I Get COVID-19? Partisanship, Social Media Frames, and Perceptions of Health Risk in Brazil.
- **Journal:** _Latin American Politics and Society_.
- **DOI:** 10.1017/lap.2020.30.

**2. Research object**

- The study analyzes how **partisanship and social media frames** (positive/cooperative vs. negative/polarizing messages) affect voters' subjective perceptions of health and job risks during a major crisis (the COVID-19 pandemic). It explores whether citizens internalize elite messages to align their perceived personal risks with the policy preferences of their preferred political parties.

**3. Case and scope**

- **Country/Region:** Brazil.
- **Election/cycle:** The first months of the COVID-19 pandemic. The survey was fielded between March 23 and May 8, 2020.
- **Sample size:** A national online survey of 2,400 respondents, drawn probabilistically by LAPOP via a Netquest panel.

**4. Method**

- **Descriptive Analysis:** Evaluated baseline partisan differences in risk perception (comparing Bolsonaro voters vs. Haddad voters vs. Independents).
- **Difference-in-Differences (Natural Experiment):** Exploited random variation in survey recruitment dates to measure the causal effect of President Jair Bolsonaro's dismissive national television address on March 24, 2020, comparing responses immediately before and after the speech.
- **Survey Experiment:** A preregistered four-arm experimental design. Respondents were randomly exposed to an edited tweet that varied by **author** (Eduardo Bolsonaro [government] vs. Fernando Haddad [opposition]) and **frame** (positive/cooperative vs. negative/polarizing).
- **Mediation Analysis ("Autopsy"):** Evaluated whether the emotional response of "anger" mediated the relationship between the frame and the update in risk perception.

**5. Core claim**

- **Partisanship heavily skews risk perception:** There are massive partisan differences in perceived risk. Bolsonaro supporters reported significantly lower expectations of health and job risks, and much higher approval of the government's crisis response, compared to opposition (Haddad) supporters.
- **Elite cues drive asymmetric risk updates:** Following Bolsonaro's dismissive public speech, opposition voters significantly _increased_ their perception of job and health risks, while government supporters maintained a "business as usual" outlook.
- **Modest/Null effects for social media framing:** The experimental manipulation of social media frames yielded surprisingly weak results. Negative tweets from out-group politicians did not perform exactly as expected. Instead, researchers found a backlash effect: negative, dismissive messages from _in-group_ politicians (like Eduardo Bolsonaro) actually increased job risk perceptions and hurt government support among their _own_ voters and anti-PT independents.
- **Sharing behavior contradicts polarization assumptions:** Despite the focus on negative polarization, respondents across the board (both in-group and out-group) were significantly more likely to "like" and "retweet" _positive, cross-the-aisle_ messages than negative ones.

**6. Relevance to Diego paper**

- **LatAm Context (Brazil):** Serves as an excellent regional precedent demonstrating how populist, hyper-partisan leadership in Latin America interacts with digital communication to shape citizen behavior during severe crises.
- **Limits of Social Media Frames:** It provides a strong foil or cautionary tale regarding the power of brief digital frames. It demonstrates that in a saturated, highly polarized media environment, isolated social media posts (the experimental treatments) have a remarkably modest effect on altering deep-seated cognitive risk perceptions.
- **Partisanship vs. Information:** It aligns with literature showing that platforms and social media messages are heavily filtered through pre-existing partisan identities (or negative partisanship, such as anti-Petismo).

**7. Exact extraction anchors**

- _On partisan risk assessment:_ "Descriptive results show that progovernment and opposition partisans report very different expectations of health and job risks. Job and health policy have become wedge issues that elicit partisan responses."
- _On the limits of experimental framing:_ "Evidence of framing effects from social media messages in our experiment is modest and mostly null, considering our initial hypothesis about the effect of negative content and cross-the-aisle positive social media messages on risk perceptions."
- _On platform sharing dynamics:_ "Negative social media messages, therefore, both induce identity responses by strong partisans and reduce participation by less committed voters... positive messages were more extensively shared by all voters, in-group and out-group."

**8. Limitations**

- **External Validity of the Experiment:** The researchers used edited/simulated tweets rather than real ones to ensure internal validity and specific wording, which sacrifices some external realism.
- **Null Findings:** Because the social media frames failed to consistently elicit the expected mediating emotion ("anger" specifically directed at out-groups), the authors had to conduct a statistical "autopsy" to explain the null findings, concluding that the treatments likely failed to pierce the noise of a saturated information environment.



# N051_PDF008_P04


Based on the provided source (Calvo and Ventura, 2021) and your previous framework, here is the extracted material regarding the Latin American and regional context:

**1. What specific Latin American country and context is studied?** The study focuses on **Brazil** during the initial months of the COVID-19 pandemic (March to May 2020), capturing the political and digital behavior of citizens right as community spread began in major cities.

**2. What regional political dynamics are highlighted?** The source emphasizes the outsized role of **defiant populist leadership** in the region. It explicitly links Brazil's Jair Bolsonaro and Mexico's Andrés Manuel López Obrador (AMLO) to Donald Trump in the US, highlighting how these populist leaders transformed a public health crisis into a partisan wedge issue. In the Brazilian context, Bolsonaro actively impaired federal agencies, used his bully pulpit and social media to dismiss health risks, and urged citizens to defy stay-at-home orders to prop up the economy.

**3. How does partisanship operate in this LatAm case?** The study highlights a distinct paradox in Latin American political behavior: while Brazil’s party system is historically described as "weakly institutionalized" and candidate-centered, the current electorate is driven by intense **negative partisanship**. Specifically, political behavior and risk perception in Brazil are heavily anchored by _anti-Petismo_ (animus against the Workers' Party, or PT). The authors find that these strong partisan and anti-partisan identities successfully overrode objective scientific facts, dictating whether citizens felt personally at risk of losing their jobs or contracting the virus.

**4. Does the case contrast with or mirror the Global North?** Unlike Luna et al. (2023), which emphasizes how structural inequality in Chile overrides Global North assumptions about digital politics, this study emphasizes **direct parallels** between Brazil and the US. The authors note that in both countries, areas with high support for their respective right-wing populist leaders (Bolsonaro and Trump) exhibited steeper epidemiological curves because partisans actively followed elite cues to minimize the risks of the virus.

**5. What is the digital/social media environment like in this context?** The Brazilian digital ecosystem is depicted as a highly polarized and saturated information environment. The study found a massive discrepancy between the power of the presidential bully pulpit and everyday social media posts. While Bolsonaro's dismissive national television address immediately triggered opposition voters to heighten their perception of risk, the experimental social media frames (edited tweets) had surprisingly modest or null effects. This suggests that in hyper-polarized Latin American contexts, brief, isolated digital messages struggle to pierce through the existing partisan noise.

**6. How does this fit into Diego's conceptual framework alongside the Chilean case?** Diego can use this source as a vital regional complement to his Chilean literature (like Luna et al., 2023) to build a comprehensive picture of Latin American digital politics:

- **The Local vs. National split:** While Luna et al. demonstrate that _structural inequality and welfare dependency_ dictate digital communication at the _local/mayoral_ level in Chile, Calvo and Ventura demonstrate that _populist rhetoric and negative partisanship_ drive digital communication at the _national/presidential_ level in Brazil.
- **Use as a citation:** "Use this source to demonstrate that digital political communication in Latin America is heavily mediated by negative partisanship and populist elite cues, which can completely override objective assessments of risk during national crises."



# N052_PDF008_P03


Here is the extracted material regarding the digitalization and platformization of politics based on the Calvo and Ventura (2021) study:

**1. What is the source’s concept of digitalization/platformization?** The source conceptualizes the digital landscape as a **highly polarized and saturated information environment** where social media messages act as framing devices. However, it pushes back against the idea that these digital frames are inherently persuasive on their own; instead, digital communication is heavily subordinated to strong offline political identities, particularly negative mass partisanship.

**2. Which actors matter: campaigns, platforms, voters, journalists, regulators, parties, movements?** The primary actors are:

- **High-level Political Elites:** Specifically populist national leaders (like Jair Bolsonaro) and prominent opposition figures (like Fernando Haddad) who generate digital cues.
- **Voters/Citizens:** Categorized by their strong partisan, anti-partisan (anti-PT), or independent identities, who filter and share these elite messages.

**3. Does the source treat platforms as neutral channels or active infrastructures?** The source treats platforms largely as **saturated communication channels** rather than active structural infrastructures. It models social media as a space for elite framing and "cascading activation"—where the visibility of a message depends entirely on peers willingly sharing it in their networks. However, the study concludes that platforms are so flooded with partisan noise that brief, isolated digital interventions (like an experimental tweet) struggle to break through and alter voters' fundamental risk perceptions.

**4. Is the argument global/comparative, national, or regional?** The empirical scope is strictly **national**, focusing on Brazil during the early months of the COVID-19 pandemic. However, the authors draw **comparative parallels** to other nations led by defiant populist leaders, specifically Donald Trump in the United States and Andrés Manuel López Obrador in Mexico.

**5. What mechanisms link digital platforms to campaign/communication strategy?**

- **Cascading Activation & Cross-Aisle Sharing:** The visibility of digital frames relies on users sharing content. Counterintuitively, the study found that despite intense negative polarization, users were significantly more likely to "like" and "retweet" **positive, cooperative messages** from both in-group and out-group politicians than negative, polarizing ones.
- **Affective Mediation (Anger):** A key mechanism linking digital messages to cognitive updates is emotion. The study proves that when a social media message successfully triggers **anger**, it significantly increases the user's perception of personal health risk.
- **In-Group Backlash:** When a digital strategy relies on negative, dismissive frames that minimize a crisis, it can trigger a backlash if deployed by the ruling party. Negative messages from the Bolsonaro camp actually increased job risk perceptions and decreased government support among his _own_ base and anti-PT independents.
- **Partisan Override in Saturated Environments:** The primary mechanism driving digital interpretation is cognitive dissonance and partisanship. Because the digital environment is saturated, isolated digital frames have "modest and mostly null" effects; voters instead rely heavily on sweeping cues from their preferred political leaders (like national television addresses) to update their beliefs.

**6. What sentence could Diego cite to connect his case to a broader transformation of political communication?** To argue that the impact of digital political communication in Latin America is heavily bounded by the pre-existing partisan and emotional environment, Diego could cite:

> "**While digital platforms facilitate the rapid spread of elite political frames, Calvo and Ventura (2021) demonstrate that in hyper-polarized Latin American contexts, isolated social media interventions struggle to cut through the saturated information environment, as users' reactions are ultimately dictated by intense negative partisanship and affective emotional responses.**"





# N053_PDF008_P05


**1. What democratic risks are identified?**

- **Elite-Driven Partisan Polarization:** The primary democratic (and public health) risk identified is that populist elites can successfully transform objective scientific reality into a polarized wedge issue. The study shows that leaders like Jair Bolsonaro use their massive platforms (such as national television addresses) to dismiss crises, which directly causes their partisan supporters to minimize personal risk and ignore critical public health measures like social distancing. This elite-driven polarization actively facilitates the spread of the disease in progovernment localities.
- **Saturated, Hyper-Partisan Information Environments:** The study highlights the risk of a political environment so saturated by negative partisanship (such as _anti-Petismo_) that voters filter crisis information entirely through their political identities rather than objective facts, altering their perceived vulnerability to health and job threats based on who is in power.

**2. Is the concern manipulation, privacy, polarization, misinformation, opacity, unequal exposure, or persuasion?** The core concern is **polarization** and **elite persuasion/cues**. The source does not focus on computational manipulation, algorithmic opacity, privacy breaches, or covert disinformation campaigns (like bots or dark ads). Instead, it tests how overt, organic social media frames (positive vs. negative messages) and high-level political rhetoric persuade citizens to update their cognitive assessments of risk.

**3. Does the source distinguish fear from evidence?** Yes, the source heavily distinguishes the theoretical fear of digital manipulation from the empirical reality of how users actually behave online. It does so in two main ways:

- **The Limits of Digital Framing vs. The Power of the Bully Pulpit:** There is a common assumption that negative, polarizing social media posts easily manipulate users into changing their worldviews. However, the study’s **empirical evidence** showed that the effects of isolated social media frames were actually "modest and mostly null". In a hyper-polarized, saturated environment, brief digital tweets failed to consistently alter risk perceptions or elicit the targeted anger. By contrast, major offline elite cues—specifically Bolsonaro's national TV address—produced robust, causal shifts in how voters assessed their risks.
- **Contradicting the Fear of Negative Sharing:** The authors tested the fear that users naturally gravitate toward and amplify toxic, negative content. Their **empirical evidence** contradicted this: respondents from all political camps (both in-group and out-group) were significantly more likely to "like" and "retweet" **positive, cooperative messages** than negative ones. Furthermore, when in-group politicians (like the Bolsonaro camp) used negative, dismissive frames, it often backfired, increasing job risk perceptions and hurting government support among their own base rather than energizing them.




# N054_PDF008_G04


Based on the provided source and our previous extractions, here is the Latin American and case context for Calvo and Ventura (2021):

**1. Which country/election is studied?** The study focuses on **Brazil** during the initial months of the COVID-19 pandemic, with survey data collected between March 23 and May 8, 2020.

**2. What makes the context distinctive?** The Brazilian context is defined by two major factors:

- **Defiant Populist Leadership:** The political environment was dominated by a populist leader, President Jair Bolsonaro, who actively used his platform (both social media and national television) to dismiss the severity of the pandemic, challenge scientific recommendations, and encourage citizens to defy stay-at-home orders. This leadership successfully transformed a public health crisis into a deep partisan wedge issue.
- **Negative Mass Partisanship:** Despite a historically weak party system, political behavior during this crisis was heavily anchored by negative partisanship, specifically _anti-Petismo_ (animus against the Workers' Party, or PT). This intense partisan identity successfully overrode objective scientific facts, dictating whether citizens felt personally at risk of losing their jobs or contracting the virus.

**3. Does it discuss Chile 2021 or post-2019 politics?** **No.** The source strictly analyzes Brazil. However, as noted in our earlier conversation, Diego can use this study as a vital regional complement to his Chilean literature (like Luna et al., 2023). While the Chilean case highlights how _structural inequality_ drives local digital politics, this Brazilian case demonstrates how _negative partisanship and populist rhetoric_ drive national digital politics in Latin America.

**4. Does it discuss party fragmentation?** **Yes.** The study highlights Brazil's party fragmentation, describing its party system as "weakly institutionalized" with a "large number of parties" and candidate-centered incentives. Because most Brazilian parties have failed to build strong labels, traditional partisanship is often a weak predictor of voter behavior; instead, political affinity is better captured by vote intention or intense pro/anti-Workers' Party sentiments.

**5. Does it discuss LatAm platforms or regional campaign practices?**

- **Regional Practices:** The study explicitly links Brazil's dynamics to broader regional and hemispheric trends, comparing Bolsonaro’s dismissive pandemic response to that of Andrés Manuel López Obrador (AMLO) in Mexico and Donald Trump in the United States.
- **LatAm Platforms:** Regarding digital platforms, the study demonstrates that the Brazilian digital ecosystem is so saturated and hyper-polarized that brief, isolated digital campaign interventions (such as the experimental positive or negative tweets tested in the study) have "modest and mostly null" effects on fundamentally altering voters' perceptions. Ultimately, sweeping elite cues (like national TV addresses) and pre-existing partisan identities heavily override isolated social media framing in this environment.



# N055_PDF008_G03


Based on the source provided (Calvo and Ventura, 2021), here is how the study addresses the digitalization and platformization of politics:

**1. How does the source define digitalization/platformization?** The source conceptualizes the digital landscape as a **highly polarized and saturated information environment** utilized primarily for elite framing. Rather than viewing social media as an inherently persuasive technological disruption, the authors define it through the lens of "cascading activation"—a system where the visibility and reach of political messages depend entirely on users' willingness to share them within their networks. Ultimately, the study suggests that the digital environment is so saturated with noise that isolated digital interventions struggle to alter deeply rooted political beliefs.

**2. What mechanisms are named?** The source identifies several specific mechanisms that link digital platform use to political behavior and risk perception:

- **Affective Mediation (Anger):** Emotion is a critical mechanism. The study demonstrates that when a digital message successfully triggers the emotion of "anger," it significantly increases a user’s subjective perception of personal health risk (_anger  risk_).
- **Cascading Activation & Cross-Aisle Sharing:** The spread of digital frames relies on peer-to-peer activation. Counterintuitively, the study found a mechanism of positive reinforcement: despite intense polarization, users across all partisan lines were significantly more likely to "like" and "retweet" **positive, cooperative messages** rather than negative, polarizing ones.
- **Cognitive Dissonance and Partisan Filtering:** Digital frames are heavily filtered through negative mass partisanship (such as _anti-Petismo_ in Brazil). Exposure to negative, dissonant messages from out-groups heightens partisan identity responses, causing voters to align further with their in-group.
- **In-Group Backlash:** When political elites use negative digital frames to minimize a crisis, it can trigger a backlash mechanism. Negative tweets from the Bolsonaro camp actually increased job risk perceptions and decreased government support among his _own_ base and anti-PT independents.

**3. Does it treat platforms as passive channels or active infrastructures?** The source treats platforms largely as **passive, saturated communication channels** rather than active structural infrastructures. In this model, platforms are essentially noisy conduits for elite framing. The authors found that isolated digital frames (experimental tweets) had "modest and mostly null" effects on fundamentally altering voters' perceptions. The study contrasts the weak persuasive power of these digital channels against the massive, causal impact of traditional mass media (specifically, President Bolsonaro's national television address), which successfully shifted risk perceptions.

**4. Is the pattern global, local, or comparative?** The empirical scope is strictly **national**, focusing on the digital and political behavior of voters in Brazil during the initial months of the COVID-19 pandemic. However, the authors frame their findings as part of a **comparative pattern**, drawing direct parallels between Brazil and other nations led by defiant populist leaders who used their platforms to transform a public health crisis into a partisan wedge issue—specifically citing Donald Trump in the United States and Andrés Manuel López Obrador (AMLO) in Mexico.



# N056_PDF008_G05

**1. What democratic risks are identified?**

- **Elite-Driven Partisan Polarization:** The primary democratic (and public health) risk identified is that populist elites can successfully transform objective scientific reality into a polarized wedge issue. The study demonstrates that leaders like Jair Bolsonaro use their massive platforms, such as national television addresses, to dismiss crises. This directly causes their partisan supporters to minimize personal risk and ignore critical public health measures like social distancing, which actively facilitates the spread of the disease in progovernment localities.
- **Hyper-Partisan Information Environments:** The study highlights the risk of an environment so saturated by negative partisanship (such as _anti-Petismo_ in Brazil) that voters filter crisis information entirely through their political identities. This deep polarization alters voters' perceived vulnerability to personal health and job threats based strictly on who is in power.

**2. Is the concern manipulation, privacy, polarization, misinformation, opacity, unequal exposure, or persuasion?** The core concern is **polarization** and **elite persuasion/cues**. The source does not focus on algorithmic opacity, privacy breaches, unequal exposure to state resources, or covert manipulation via bots and dark ads. Instead, it tests how overt social media frames (positive vs. negative messages) and high-level political rhetoric persuade citizens to update their cognitive assessments of risk and align with the policy preferences of their preferred parties.

**3. Does the source distinguish fear from evidence?** Yes, the source heavily distinguishes the theoretical fear of digital manipulation from the empirical evidence of how users actually behave online:

- **The Limits of Digital Framing vs. The Power of the Bully Pulpit:** There is a common theoretical fear that negative, polarizing social media posts easily manipulate users into changing their worldviews. However, the study’s **empirical evidence** showed that the effects of isolated social media frames were actually "modest and mostly null". In a hyper-polarized environment, brief digital tweets failed to consistently alter risk perceptions or reliably elicit targeted anger. By contrast, major offline elite cues—specifically Bolsonaro's national TV address—produced robust, causal shifts in how voters assessed their risks.
- **Contradicting the Fear of Negative Sharing:** The authors tested the fear that users naturally gravitate toward and amplify toxic, negative content. Their **empirical evidence** contradicted this: respondents from all political camps (both in-group and out-group) were significantly more likely to "like" and "retweet" **positive, cross-the-aisle messages** than negative ones.
- **The Backlash Effect:** Furthermore, the evidence showed that when in-group politicians (like the Bolsonaro camp) used negative, dismissive frames, it actually backfired, increasing job risk perceptions and hurting government support among their own base rather than energizing them.
















