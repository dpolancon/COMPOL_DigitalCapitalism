
# N013_PDF003_P00

**1. What method is used: LDA, STM, BERTopic, embeddings, dictionary, supervised classifier, manual coding, other?** The study uses **Latent Dirichlet Allocation (LDA)**, an unsupervised machine learning topic modeling method.

**2. What text corpus is analyzed and how large is it?** The corpus consists of **short, open-ended survey responses** from the first wave of an online Netquest panel survey in Chile, where participants were asked what ideas came to their minds when thinking about "the Left" and "the Right". The first wave of the survey includes **3,965 observations**.

**3. What validation strategy is used: coherence, held-out likelihood, human coding, expert rating, robustness, qualitative inspection, other?** The authors rely on **qualitative inspection** based on **interpretability and thematic coherence**. As a robustness check, they initially estimated models with different numbers of topics (k=3 and k=4), but ultimately reduced the model to k=2 after qualitatively observing "considerable overlap" and determining that additional topics were not substantively distinct.

**4. What preprocessing choices are reported?** **No specific preprocessing choices** (such as stopword removal, stemming, or lemmatization) are reported in the provided text.

**5. Does the source discuss short texts, multilingual text, Spanish-language text, or political advertising text?**

- **Short texts:** Yes, the source explicitly notes the "relatively short length of the open-ended responses" in their dataset.
- **Spanish-language text:** The corpus is inherently in Spanish as it surveys the Chilean electorate, though the methodological challenges of analyzing Spanish are not explicitly discussed (the translated output is shown in Table 5).
- **Multilingual/Political advertising text:** No.

**6. What are the method’s limitations according to the source?** The primary limitation noted is the **short length of the open-ended responses**, which constrained the LDA model's ability to "zoom-in" on narrower themes. When attempting to fit more than two topics, the model produced overlapping and indistinguishable categories, forcing the researchers to rely on a highly aggregated two-topic model.

**7. How can Diego cite this source: as method precedent, warning, alternative, or validation standard?** Diego can cite this source as a **method precedent** in two specific ways:

- For applying **LDA to short, open-ended survey responses** to successfully extract ideological labels and affective/moral value judgments from Latin American voters.
- For justifying a **very low topic count (k=2)** when working with short texts, using qualitative interpretability and the avoidance of topic overlap as the primary validation criteria for reducing _k_.


# N014_PDF003_P01

**1. Bibliographic identity**

- **Author(s):** Pablo Argote and Giancarlo Visconti.
- **Year:** 2025.
- **Title:** Causes and Consequences of Ideological Persistence: The Case of Chile.
- **Journal:** Latin American Politics and Society.
- **DOI:** 10.1017/lap.2025.10028.

**2. Research object**

- The study examines ideological persistence as a stabilizing force in electoral behavior, analyzing how ideological identification functions as a social identity that substitutes for weak or delegitimized political parties.

**3. Case and scope**

- **Country/Region:** Chile.
- **Election/cycle:** Examines long-term trends covering the post-authoritarian period (1990s to 2023) and focuses on the enduring effects of the 1988 plebiscite.
- **Sample size:** Analyzes face-to-face cross-sectional survey data from CEP (1994-2023, n=38,388) and a multi-wave Netquest online panel (Wave 1: 3,965 observations; Wave 2: 3,075; Wave 3: 1,065).

**4. Method**

- **Descriptive survey analysis:** Tracking the evolution of party identification, ideological identification, and issue preferences over decades.
- **Conjoint experiment:** Testing whether voters prioritize ideological alignment over specific issue congruence (e.g., immigration) when choosing hypothetical presidential candidates.
- **Topic modeling (LDA):** Unsupervised text analysis of short, open-ended survey responses asking voters what comes to mind when they think of "the Left" and "the Right" (k=2).
- **Regression Discontinuity in Time (RDiT):** Estimating the causal effect of being eligible to vote in the 1988 plebiscite (barely 18 years old) on long-term ideological identification.

**5. Core claim**

- Despite a sharp decline in partisan affiliation in Chile over the past 30 years, ideological self-placement has remained remarkably stable.
- Ideology operates not merely as a bundle of policy preferences, but as a durable _social identity_ characterized by intergenerational transmission, symbolic boundaries, and strong in-group favoritism/out-group animosity.
- Ideological alignment consistently outweighs issue alignment in voting decisions; for instance, a left-wing pro-immigration voter strongly prefers a left-wing anti-immigration candidate over a right-wing pro-immigration candidate.
- High-intensity political events—specifically the 1988 plebiscite that ended the Pinochet dictatorship—acted as critical junctures that solidified long-term ideological attachments, though this effect is slowly weakening with generational replacement.

**6. Relevance to Diego paper**

- **LDA / Computational Text Analysis:** Highly relevant. Provides a recent methodological precedent for using LDA (k=2) to analyze short, open-ended political survey responses in Spanish from the Chilean electorate, successfully extracting affective and ideological labels.
- **Chilean Case / Latin America:** Highly relevant. Offers an updated analysis of the Chilean party system, electoral behavior, and the enduring legacy of the 1988 plebiscite.
- _Not relevant for:_ Digitalization, platformization, or paid political advertising (the source does not analyze digital media or platforms).

**7. Exact extraction anchors**

- **On ideology vs. issues:** "...ideological voting consistently outweighs issue voting. For example, a left-wing and pro-immigration voter would rather prefer a left-wing and anti-immigration candidate to a rightist pro-immigration, and vice versa".
- **On short text LDA modeling:** "...we began by estimating a model with four topics, given the relatively short length of the open-ended responses in our dataset. However, we subsequently reduced the model to two topics after observing considerable overlap—only two emerged as substantively distinct and interpretable".
- **On social identity:** "...we argue that ideological identification can stabilize electoral behavior, serving as a substitute for weak or delegitimized political parties... ideology in Chile displays features of a social identity, including intergenerational transmission, symbolic boundaries, and in-group affect".

**8. Limitations**

- **Exclusion of Centrists in experiment:** The core conjoint and descriptive analyses focus predominantly on voters who explicitly identify with the left or the right, largely setting aside moderate/centrist voters and those with no ideology, who make up about half of the electorate.
- **Local average treatment effect (LATE):** The RDD findings regarding the 1988 plebiscite estimate a local average treatment effect strictly valid only for units right at the age cutoff, meaning caution is needed when generalizing to individuals further away from that birthdate.

#  N015_PDF003_P04

**Definition of Digitalization/Platformization** The source does not offer a sweeping theoretical definition of platformization, but rather conceptualizes it practically through the specific affordances of **data-driven microtargeting** and Facebook advertising. It defines the platformized digital environment as a "private space" that is inherently "nontransparent," allowing political campaigns to operate free from the public scrutiny and accountability required by traditional broadcast media.

**Mechanisms Named** The text identifies several key mechanisms linking digital platforms to political communication:

- **Microtargeting and Audience Segmentation:** Leveraging data to create "custom audiences" (e.g., by uploading voter email lists) and "lookalike audiences," combined with rapid A/B message testing at scale to refine campaign content.
- **Political "Redlining":** Using platform targeting capabilities to construct narrow, electorally significant sub-publics while strategically excluding citizens deemed to have little electoral value from the national conversation.
- **Mobilization over Persuasion:** Using platform data to aim populist "wedge" issues at existing supporters to increase polarization and turnout, rather than attempting to persuade undecided swing voters.
- **Algorithmic Misdirection:** The process by which platform algorithms act autonomously to misdirect campaign adverts or structurally exclude specific demographic sections of society.

**Passive Channels or Active Infrastructures** The source strongly treats platforms as **active infrastructures**, explicitly arguing that political campaigns do not have absolute control over their reach. It highlights that "Facebook’s algorithms can misdirect adverts to unintended audiences" and that attempts to change algorithmic behavior often fail because the algorithms independently reconstruct attributes (like race) through other variables. Furthermore, the platform's active design shapes political strategy: its "pricing structures make it cheaper to reach likely supporters than undecided swing voters," actively incentivizing polarization and mobilization over persuasion.

**Global, Local, or Comparative Pattern** The core empirical analysis is strictly **local/national**, focusing exclusively on data from the 2017 United Kingdom General Election. However, the authors frame this case within a **global and comparative** context, drawing extensively on literature regarding microtargeting and platform advertising in the United States, Canada, Germany, Spain, Italy, and the Netherlands to establish patterns of campaign behavior.



# N016_PDF003_P02


Based on the provided source, here is the extracted methodological information relevant to topic modeling and computational text analysis:

**1. What method is used: LDA, STM, BERTopic, embeddings, dictionary, supervised classifier, manual coding, other?** The study uses **Latent Dirichlet Allocation (LDA)**, an unsupervised machine learning topic modeling method.

**2. What text corpus is analyzed and how large is it?** The corpus consists of **short, open-ended survey responses** where participants were asked what words or ideas came to mind when thinking about "the Left" and "the Right". The data comes from the first wave of a Netquest online panel survey of the Chilean electorate, which includes **3,965 observations**.

**3. What validation strategy is used: coherence, held-out likelihood, human coding, expert rating, robustness, qualitative inspection, other?** The researchers rely on **qualitative inspection** based on "interpretability and thematic coherence". As a robustness check, they initially estimated models with three and four topics (k=3 and k=4), but ultimately reduced the final model to two topics (k=2) after observing "considerable overlap" and determining that only two topics were substantively distinct and interpretable.

**4. What preprocessing choices are reported?** The source **does not report specific preprocessing choices** (such as stopword removal, lemmatization, or stemming) in the main text.

**5. Does the source discuss short texts, multilingual text, Spanish-language text, or political advertising text?**

- **Short texts:** Yes, the source explicitly acknowledges the "relatively short length of the open-ended responses" in their dataset.
- **Spanish-language text:** While the survey was conducted in Chile and the original text is inherently in Spanish, the methodological challenges of analyzing Spanish are not discussed (the results are presented translated into English).
- **Multilingual / Political advertising text:** No, neither is discussed.

**6. What are the method’s limitations according to the source?** The primary limitation is the **short length of the open-ended responses**, which hindered the LDA model's ability to "zoom-in" on narrower themes. Attempting to fit more topics resulted in overlapping and indistinguishable categories, forcing the researchers to rely on a broad, highly aggregated two-topic model.

**7. How can Diego cite this source: as method precedent, warning, alternative, or validation standard?** Diego can cite this source as a **method precedent** in two specific ways:

- For applying **LDA to short, open-ended political survey responses** to successfully extract ideological labels and affective/moral judgments.
- For justifying a **very low topic count (k=2)** when working with short texts, using qualitative interpretability and the avoidance of topic overlap as the primary validation criteria for reducing _k_.


# N017_PDF003_P07


Based on the provided source, here is the extracted information relevant to using this article as a **Venue Precedent** for your own research submission:

**1. Venue Identity and Scope**

- **Journal:** _Latin American Politics and Society_ (LAPS).
- **Publisher:** Cambridge University Press (on behalf of the University of Miami).
- **Year of Publication:** 2025.
- **Article Type:** Research Article.
- **Thematic Focus:** The journal publishes research on Latin American political development, electoral behavior, party systems, and political identities. This specific article successfully frames a single-country case study (Chile) within broader regional debates about the decline of traditional partisanship and the persistence of ideological identities,.

**2. Methodological Precedent** This article demonstrates that _Latin American Politics and Society_ is highly receptive to **sophisticated, mixed-methods quantitative research**, specifically accepting:

- **Computational Text Analysis:** The venue accepts unsupervised machine learning, specifically Latent Dirichlet Allocation (LDA) topic modeling, to analyze short, open-ended Spanish-language survey responses (e.g., asking voters what comes to mind when thinking about "the Left" and "the Right"),,.
- **Experimental Designs:** The journal accepts original survey data incorporating conjoint experiments to test voter priorities (e.g., ideology vs. issue alignment),.
- **Causal Inference:** The venue is open to quasi-experimental designs, such as Regression Discontinuity in Time (RDiT), to estimate the long-term effects of historical political events,.

**3. Formatting and Open Science Standards**

- **Open Science:** The journal supports and publishes research utilizing open science practices. The authors note that their conjoint experiment was preregistered on the Open Science Framework (OSF), and their data and code are made publicly available on Harvard Dataverse.
- **Supplementary Materials:** The venue allows for extensive use of online supplementary appendices to house robustness checks, conjoint diagnostics, and alternative model specifications (e.g., showing different _k_ topics for LDA), keeping the main text focused on substantive findings,,.

**4. How Diego Can Use This Precedent** If Diego is considering submitting his own work to _Latin American Politics and Society_, he can use Argote & Visconti (2025) to confidently justify:

- Submitting a paper that relies on **topic modeling (LDA)** as a core methodological component for measuring political text or speech in a Latin American context.
- Submitting a **single-country case study** (like Chile) by ensuring the findings are connected to region-wide theoretical concerns (e.g., polarization, platformization, or party system weakness),.



# N018_PDF003_G4


**1. Country/election studied:** The source studies **Chile**, focusing on long-term electoral behavior from the post-authoritarian transition to the present (1990s–2023),. It places specific emphasis on the enduring legacy of the **1988 plebiscite** (which ended Augusto Pinochet's dictatorship) and also collects experimental data during the **2021 presidential election cycle**,,.

**2. What makes the context distinctive?** Chile's context is distinctive because it presents a paradox: **a weak and fragmented party system combined with remarkably stable electoral competition**,. Over the past three decades, traditional partisan affiliation has collapsed—dropping from over 70% in 1994 to just 36% in 2023. However, ideological self-placement on the left-right scale has remained incredibly stable,. The authors argue that this stability occurs because **ideology acts as a substitute for weak political parties**, functioning not merely as a set of policy preferences, but as a deeply rooted "social identity",.

**3. Discussion of specific themes:**

- **Chile 2021:** Yes. The source discusses the 2021 presidential election, highlighting the rise of new challengers from outside the traditional center-left and center-right coalitions: Gabriel Boric on the left (who won the presidency) and José Antonio Kast of the far-right _Partido Republicano_,. The primary survey panel data used in the study was also collected in November and December 2021.
- **Post-2019 politics:** Yes. The source explicitly analyzes the impact of the **2019 Social Outburst**, noting it as a moment of acute political crisis and anti-establishment discontent where the percentage of citizens identifying with "no ideology" temporarily peaked,. It also notes that both the 2019 protests and the subsequent 2022 Constitutional Plebiscite have heightened polarization and led to a re-politicization of Chilean voters.
- **Party fragmentation:** Yes, this is a core theme. The study extensively documents party system erosion, noting that Chilean parties have lost their societal roots, suffer from low popular support, and fail to represent voters' interests,. It also covers the recent realignment where new political actors have emerged, though it notes these actors still fit neatly within the traditional left-right spectrum,.
- **LatAm platforms or regional campaign practices:** **No.** The source does not discuss digital platforms, social media, or campaign practices. It does, however, discuss the broader Latin American political context, noting that Chile's pattern of declining partisanship alongside enduring left-right ideological structures is mirrored in other countries like Brazil, Argentina, Ecuador, and Colombia.



# N019_PDF003_G2


Based on the provided source, here is the methodological information regarding the topic modeling approach:

- **Method used:** The study uses **Latent Dirichlet Allocation (LDA)**, an unsupervised machine learning topic modeling method.
- **Corpus:** The text corpus consists of **short, open-ended survey responses** from the first wave of a Netquest online panel survey conducted in Chile in 2021, containing 3,965 observations. The prompt asked respondents what ideas came to their minds when thinking about "the Left" and "the Right".
- **Validation strategy:** The authors relied on qualitative inspection based on **"interpretability and thematic coherence"**. To validate their chosen model, they examined the most frequent words in each topic and checked for overlapping content, ultimately reducing the number of topics to ensure they remained substantively distinct.
- **Topic number K:** The final model uses **k=2** (labeled "Ideological labels" and "Value judgment"). The authors initially estimated models with three and four topics (k=3 and k=4) as a robustness check, but discarded them after observing "considerable overlap".
- **Preprocessing choices:** The provided text **does not report** any specific preprocessing steps (such as stopword removal, stemming, or lemmatization).
- **Short texts:** **Yes**, the authors explicitly acknowledge the "relatively short length of the open-ended responses" in their dataset. This shortness is the primary reason they could not extract a higher number of distinct topics without them overlapping.
- **Spanish language:** The corpus is inherently in Spanish, as it is based on a survey of the Chilean electorate. However, the text **does not discuss** any methodological challenges specific to processing Spanish, and the topic modeling results are presented translated into English (e.g., "thieves," "chaos," "rights").
- **Interpretability:** **Yes**, "interpretability" is explicitly stated as a core criterion used by the researchers to inspect the results and select the final number of topics.
- **Alternatives to LDA:** **No**, the source does not discuss or compare LDA to alternative computational text analysis methods (like STM, BERTopic, or embeddings).


# N020_PDF003_G7


Based on the provided source, here is the venue positioning and precedent information for this article:

- **Journal:** The article was published in _**Latin American Politics and Society**_ in 2025.
- **Why is it a precedent?** It serves as a strong precedent because it demonstrates that this specific journal is highly receptive to sophisticated, mixed-methods quantitative research. Specifically, it shows the venue will publish studies utilizing computational text analysis (like Latent Dirichlet Allocation or LDA) on short, open-ended Spanish-language survey responses. It also demonstrates the venue's openness to experimental survey designs (conjoint experiments) and single-country case studies that are effectively linked to broader regional debates.
- **Niche coverage:** This paper covers the **Method** and **Region** sides of your niche. Methodologically, it applies LDA topic modeling. Regionally, it focuses extensively on the Chilean case while connecting it to the broader Latin American context of declining partisanship. It also touches on **Theory** (electoral behavior and social identity). However, it does _not_ cover the **Object** of your research, as it makes no mention of digital politics, platformization, or paid political advertising.
- **Type of precedent:** It acts as a **legitimating precedent**. Because it does not study digital platforms or paid ads, it is not a direct competitor. Instead, it legitimates your methodological approach (using topic modeling for short Spanish texts) and your regional focus (studying Chile to understand broader democratic trends) for submission to this specific journal.




