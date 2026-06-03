

# N028_PDF005_P00


It appears you forgot to paste the NotebookLM output in your query!

However, since you provided the source document (`ARUGUETE_ETAL_2024.pdf`), I have extracted the core methodological, regional, and theoretical claims directly from the text and formatted them into your requested Obsidian source note structure.

```
---
type: source_note
status: draft_ra
source_id: LUNA_ETAL_2023
filename: ARUGUETE_ETAL_2024.pdf
author_year: Luna et al. 2023
clusters:
  - Topic Modeling (STM)
  - Political Communication
  - Social Media
  - Chile / Latin America
priority:
needs_diegeo_review: yes
---

### Core Claims & Methodological Extraction

**1. Case and Scope**
* **Country/Election studied:** Chile, specifically focusing on local municipal governments during the COVID-19 pandemic and the lead-up to the 2021 municipal elections.
* **Context:** The pandemic occurred immediately after the October 2019 "social uprising," a period of intense crisis where traditional political institutions lost legitimacy, but mayors emerged as the most trusted political figures.

**2. Text Corpus Analyzed**
* **Data:** A total of 264,387 posts across Facebook, Instagram, and Twitter.
* **Actors:** Posts from all 52 city mayors (using both personal and institutional accounts) in the Santiago Metropolitan Region, covering March 3, 2020, to June 28, 2021.

**3. Method: Topic Modeling & Computational Text Analysis**
* **Method Used:** Structural Topic Modeling (STM).
* **Preprocessing:** The authors used the `quanteda` package to remove punctuation, accents, and proper nouns (specifically the names of municipalities and mayors).
* **Validation & Topic Number (K):** They tested 10 models with $k$ varying between 5 and 50. They determined that $k=25$ yielded the best diagnostic measures (balancing semantic coherence and exclusivity). From these 25 topics, they retained 7 highly interpretable topics for their qualitative/quantitative analysis.

**4. Substantive Findings: Structural vs. Political Variables**
* **Socioeconomic factors override political strategy:** The study found that structural/socioeconomic variables (like poverty rates and the urban/rural divide) overwhelmingly determined a municipality's social media strategy, rather than political variables (such as the mayor's partisanship, incumbency status, or alignment with the national government).
* **The "Lockdown" Effect:** During strict COVID-19 lockdowns, poorer municipalities significantly increased their social media posting frequency to manage critical state-provided assistance and social support registries. By contrast, wealthier and rural municipalities did not significantly alter their posting behavior during lockdowns.
* **Engagement:** Poorer and rural municipalities generated higher levels of citizen engagement per post. Interestingly, engagement levels did not depend on the municipality's population size or its local number of COVID-19 cases.
* **Platform usage differences:** Municipalities tended to use Twitter more for COVID-19 prevention messaging, while Facebook was preferred for communicating about social support networks.
```




# N029_PDF005_P01


**1. Bibliographic identity**

- **Author(s):** Juan Pablo Luna, Daniel Alcatruz, Cristian Pérez Muñoz, Fernando Rosenblatt, Sergio Toro Maureira, and Sebastián Valenzuela.
- **Year:** 2023.
- **Title:** Local Government, Social Media and Management of COVID-19: The Case of Chilean Mayoral Communication.
- **Journal:** Political Communication.
- **DOI:** 10.1080/10584609.2023.2290494.

**2. Research object**

- The study examines how local political leaders (mayors) harness social media platforms to communicate with constituents during a crisis, specifically evaluating whether structural (socioeconomic) or political variables primarily drive their communication strategies and content.

**3. Case and scope**

- **Country/Region:** Chile (specifically the Santiago Metropolitan Region, representing 42% of the country's population).
- **Election/cycle:** The study covers the period from March 3, 2020 (the first COVID-19 case in Chile) to June 28, 2021 (the municipal elections). This period is heavily contextualized by the aftermath of the October 2019 "social uprising".
- **Sample size:** 264,387 total posts across Facebook, Instagram, and Twitter from the personal and institutional accounts of all 52 city mayors in the region.

**4. Method**

- **Data Collection:** Used the CrowdTangle API for Facebook and Instagram, and the Twitter API. They also computed a custom "Engagement Index" adjusting raw reactions by total posts and population size.
- **Topic Modeling (STM):** Used Structural Topic Models (STM), which allows for the inclusion of external covariates to assess topic prevalence. The tested covariates included poverty rates, COVID-19 case numbers, population size, rural/urban classification, mayoral incumbency, and political alignment with the national government.
- **Preprocessing and Validation:** Used the `quanteda` R package to remove punctuation, accents, and proper nouns (mayor and municipality names). They tested models with _k_ ranging from 5 to 50 topics, ultimately selecting _k_=25 based on semantic coherence and exclusivity diagnostics, and retained 7 interpretable topics for the final analysis.

**5. Core claim**

- **Structural factors override political incentives:** A municipality's socioeconomic context (specifically poverty levels and the urban/rural divide) overwhelmingly dictates its social media communication strategy, rather than political variables like mayoral partisanship, incumbency, or alignment with the national government.
- **The lockdown discontinuity:** Mayors of poorer communities made much more extensive use of social media during lockdown periods than wealthier municipalities. Because poor households rely heavily on municipal services for survival, lockdowns forced mayors to use social media as a direct, fast substitute for coordinating targeted state assistance.
- **Engagement dynamics:** Higher user engagement on social media was driven by poorer and rural municipalities, rather than being determined by the severity of the local COVID-19 outbreak or the population size.
- **Platform differences:** Mayors tended to use Twitter more frequently for COVID-19 prevention messaging, while Facebook was preferred for communicating about social support networks.

**6. Relevance to Diego paper**

- **Topic Modeling (STM):** Highly relevant. Provides a direct methodological precedent for applying Structural Topic Modeling (STM) to a large corpus of Spanish-language political social media posts (Facebook, Twitter, Instagram), demonstrating how to incorporate socioeconomic and political covariates into the analysis of digital text.
- **Chile / LatAm Context:** Highly relevant. Provides vital context on the immediate aftermath of the 2019 _estallido social_ (social uprising), emphasizing a period where national institutions lost almost all legitimacy and citizens relied heavily on local mayors.
- **Platformization / Digitalization:** Relevant. The paper argues against the idea of a universal "technological disruption" in political communication, demonstrating instead that social media usage strongly maps onto pre-existing structural inequalities and state capacity issues in the Global South.

**7. Exact extraction anchors**

- **On structural vs. political variables:** "...we found that mayors’ social media communication strategies depend on the functions that different municipalities perform in the territory, and that socioeconomic variables differentiate these activities."
- **On social media substituting physical welfare state presence:** "...in poor municipalities, lockdowns implied that some critical services and government programs, which are targeted at poor families, were not offered, or had to be restructured. Thus, social media provided a direct and fast means of communication for contacting the targeted population."
- **On the lack of political effects:** "The political variables—incumbency and political alignment with the national government—do not affect the prevalence of any topic."

**8. Limitations**

- **Unobserved Mechanisms:** The authors acknowledge that they could not explicitly measure certain confounding mechanisms, such as the size and professionalization of public relations departments in wealthier urban municipalities versus poorer rural ones, or the mitigating influence of traditional broadcast media.
- **Geographic Scope:** The data is restricted to the Santiago Metropolitan Region, meaning it does not capture the dynamics of municipalities in the extreme north or south of the country.




# N030_PDF005_P04


Based on the provided source, here is the extracted material specifically relevant to the political and social context of **Chile and Latin America**:

**1. The 2019 Social Uprising and Crisis of Representation**

- **The "Estallido Social":** In October 2019, Chile experienced a massive civic uprising that—unlike previous single-issue protests—targeted the entire political, economic, and social establishment.
- **Collapse of Institutional Legitimacy:** As a result of this unrest and a long-building perception of abuse by the wealthy, traditional political institutions (including both the government and opposition parties) saw their legitimacy plummet to the lowest levels in Chile's recorded history. Citizens became deeply detached from the political system that had governed the country since the 1990 democratic transition.

**2. The Rise of Mayors as Legitimate Actors**

- **Trust in Local Government:** In the midst of this generalized crisis of national representation and severe public distrust, local city mayors broke the trend and emerged as the most trusted political figures in the country.
- **Mediators of the Crisis:** During the worst of the social uprising, mayors were highly visible and at the forefront of institutional efforts to reinstate political order, even coming together to propose structural and constitutional reforms to navigate the country out of the crisis.

**3. Deep Inequality and Dependence on the Local State**

- **Highly Visible Inequality:** Despite being viewed as a successful case of democratic transition and economic growth, Chile remains one of the most unequal countries in Latin America. This inequality is starkly visible at the municipal level, where there are drastic differences in state capacity, infrastructure, and household wealth.
- **Municipalities as Welfare Providers:** In unequal Latin American societies, structural conditions dictate how citizens relate to the state. While wealthier populations can rely on private provision for their needs, vulnerable populations depend heavily on the local municipality. Municipalities act as the "street-level bureaucrats" for the central government, making them the primary—and sometimes only—access point for critical welfare programs and social assistance for the poor.

**4. Chile's Evolving Media Landscape**

- **Shift from TV to Social Media:** The Chilean media context has transformed dramatically over the last decade. Internet penetration is extremely high (92%), and social media and messaging applications have overtaken traditional outlets as the primary source of news and public affairs information.
- **Decline of Traditional Media:** While reliance on platforms like Facebook, Instagram, and Twitter has surged, news consumption through traditional media has continuously declined—even during the height of the pandemic—with television news viewership dropping from 80% to 65% between 2017 and 2022.



# N031_PDF005_P02

**1. What method is used: LDA, STM, BERTopic, embeddings, dictionary, supervised classifier, manual coding, other?** The study uses **Structural Topic Models (STM)**, an unsupervised machine learning topic modeling algorithm that allows for the inclusion of external covariates to assess topic prevalence across documents,.

**2. What text corpus is analyzed and how large is it?** The corpus consists of **264,387 social media posts** (from Facebook, Instagram, and Twitter). These posts come from both the personal and institutional accounts of all 52 city mayors in the Santiago Metropolitan Region of Chile, collected during the COVID-19 pandemic between March 3, 2020, and June 28, 2021.

**3. What validation strategy is used: coherence, held-out likelihood, human coding, expert rating, robustness, qualitative inspection, other?** The researchers used a combination of quantitative diagnostics and qualitative inspection. They estimated 10 different models with the number of topics (_k_) ranging from 5 to 50. To select the best model, they evaluated four diagnostic measures: **semantic coherence, exclusivity, held-out likelihood, and residuals**,. They determined that the model with _k_=25 yielded the best balance of semantic coherence and exclusivity. From those 25 topics, they relied on qualitative inspection to retain 7 topics that were "readily interpretable, relevant, and clear" for their final substantive analysis.

**4. What preprocessing choices are reported?** The authors utilized the `quanteda` R package for text preprocessing. The explicitly reported preprocessing steps include the **removal of punctuation, accents, and proper nouns** (specifically the names of mayors and municipalities).

**5. Does the source discuss short texts, multilingual text, Spanish-language text, or political advertising text?**

- **Short texts:** The text analyzes social media posts, which are inherently short, but it does not discuss specific methodological or algorithmic challenges related to analyzing short texts,.
- **Spanish-language text:** The corpus is in Spanish, as evidenced by the topic keywords presented (e.g., "medidas", "cuarentena", "fiscalización", "información"),, but the authors do not highlight any specific methodological challenges associated with processing Spanish.
- **Multilingual / Political advertising text:** No, neither is discussed. The data consists of organic political crisis communication.

**6. What are the method’s limitations according to the source?** Regarding the topic model specifically, the authors note the standard trade-off that increasing the number of extracted topics makes the model "more detailed but less accurate or interpretable". More broadly, the authors acknowledge the study is limited by **unobserved mechanisms** (they could not measure the size and professionalization of municipal public relations departments, nor the influence of traditional broadcast media like TV and radio) and a **limited geographic scope**, as it only focuses on the Santiago Metropolitan Region.

**7. How can Diego cite this source: as method precedent, warning, alternative, or validation standard?** Diego can cite this source as a strong **method precedent** in two key ways:

- For applying **Structural Topic Modeling (STM) to a large corpus of Spanish-language social media posts** to demonstrate how to incorporate **external covariates** (such as poverty rates, urban/rural divides, and political alignment) to estimate how structural versus political factors drive topic prevalence,,.
- For justifying a **two-step topic selection (_k_) validation process**: first using quantitative diagnostic tests (semantic coherence, exclusivity, residuals, and held-out likelihood) to find an optimal mathematical fit (_k_=25), and then utilizing qualitative interpretability to isolate a smaller subset of topics (7) for the final analysis,,.


# N032_PDF005_P07


Here is the venue positioning and precedent information extracted from the provided source:

**1. Venue Identity and Scope**

- **Journal:** _Political Communication_,.
- **Year of Publication:** 2023.
- **Article Type:** Research Article.
- **Thematic Focus:** The journal publishes research on how political actors utilize media and technology to connect with constituents. This specific article expands the journal's traditional focus (which often centers on national elections in developed democracies) by examining local government (mayoral) communication during a crisis in a developing democracy,,.

**2. Methodological Precedent** This article demonstrates that _Political Communication_ is highly receptive to **sophisticated computational text analysis** applied to massive, non-English datasets. Specifically, it establishes a precedent for:

- Accepting **Structural Topic Modeling (STM)** to analyze large corpora (in this case, 264,387 posts),,.
- Accepting research based on **API-scraped platform data**, specifically utilizing the CrowdTangle API (for Facebook and Instagram) and the Twitter API,.
- Publishing studies that incorporate **external covariates** (such as poverty rates, urban/rural divides, and political alignment) directly into the text analysis to measure what drives topic prevalence,.

**3. Niche Coverage: Method, Object, Region, and Theory**

- **Method:** Strong coverage. It extensively models Spanish-language social media text using STM and quantitative engagement metrics,,.
- **Object:** Strong coverage. It directly analyzes political actors' multi-platform social media strategies, explicitly comparing the use of Facebook, Twitter, and Instagram,,.
- **Region:** Strong coverage. It focuses entirely on a Latin American case study (Chile), specifically validating the region's high inequality and structural features as critical variables for understanding political communication,,.
- **Theory:** Covers the intersection of digital communication and institutional legitimacy, particularly how social media functions in unequal societies where traditional political institutions face severe crises of representation,,.

**4. Type of Precedent and How Diego Can Use It** This article serves as both a **legitimating** and a **complementary precedent**.

- It is **legitimating** because it proves that _Political Communication_ will publish research relying on STM to analyze Spanish-language social media platforms in Chile,,. Diego can cite it to justify that studying Latin American cases is not just a geographical curiosity, but essential for understanding how structural inequalities heavily dictate digital political behavior,.
- It is **complementary** because it focuses on _local_ governments (mayors) during a public health crisis (COVID-19),,. It leaves room for Diego to study other political actors (like national candidates, parties, or movements) or other contexts (like electoral campaigns or the constitutional process) while building on their methodological foundation.



# # N033_PDF005_G04


**1. Which country/election is studied?** The source studies **Chile**, focusing specifically on the Santiago Metropolitan Region. It examines the period from March 2020 (the outbreak of the COVID-19 pandemic) to the **municipal elections in mid-2021**.

**2. What makes the context distinctive?** The context is distinctive because the pandemic lockdowns immediately followed the massive **October 2019 social uprising (_estallido social_)**, which caused a historic collapse in the legitimacy of national political institutions. In this environment of deep national distrust, local **mayors emerged as the most trusted political figures** in the country.

Additionally, Chile's high levels of structural inequality make the context unique. While wealthier citizens can rely on private resources, the poor are highly dependent on their local municipalities, which act as "street-level bureaucrats" providing critical welfare and social assistance.

**3. Does it discuss Chile 2021?** Yes. The study explicitly analyzes mayoral communication strategies in the lead-up to the **2021 municipal elections**.

**4. Does it discuss post-2019 politics?** Yes, extensively. The aftermath of the **2019 social uprising** is the defining political backdrop of the study, framing a period where citizens were deeply detached from the political system and national authorities.

**5. Does it discuss party fragmentation?** It does not explicitly use the term "party fragmentation," but it heavily discusses the underlying **crisis of representation**, noting that political institutions, including government and opposition parties, had reached their lowest levels of legitimacy in recorded history. It also tests whether mayoral partisanship and alignment with the national government influenced their communication, finding that these political variables had no significant effect.

**6. Does it discuss LatAm platforms or regional campaign practices?**

- **Platforms:** Yes. The source details Chile's evolving media landscape, noting 92% internet penetration and a sharp decline in traditional television news. It highlights **Facebook as the dominant platform** for news (used by 53% of online users), followed by Instagram and Twitter.
- **Regional Practices:** Yes. The study argues that in unequal Latin American societies, **structural and socioeconomic factors drive digital communication strategies far more than political calculations**. Because poorer households rely on the state for survival, mayors in vulnerable municipalities were forced to significantly increase their social media use during lockdowns to coordinate welfare assistance. Wealthier municipalities, whose residents rely on self-provision, did not alter their posting behavior during the crisis.



# N034_PDF005_G02


**Method used:** The study uses **Structural Topic Models (STM)**, an unsupervised machine learning topic modeling method that allows researchers to include external covariates (like poverty rates or political alignment) to assess topic prevalence.

**Corpus:** The text corpus consists of **264,387 social media posts** from Facebook, Instagram, and Twitter. The texts are from the personal and institutional accounts of all 52 city mayors in the Santiago Metropolitan Region of Chile, collected between March 3, 2020, and June 28, 2021.

**Validation strategy:** The authors used a mixed validation approach relying on both quantitative diagnostics and qualitative inspection. They evaluated different models based on four diagnostic measures: **semantic coherence, exclusivity, held-out likelihood, and residuals**. After finding the optimal mathematical fit, they used qualitative evaluation to retain a subset of topics that were "readily interpretable, relevant, and clear" for their substantive analysis.

**Topic number K:** The researchers tested 10 different models with _k_ (number of topics) ranging from 5 to 50. They determined that **k=25** yielded the best combination of semantic coherence and exclusivity. From these 25 topics, they selected a final subset of **7 topics** to analyze.

**Preprocessing choices:** Using the `quanteda` R package, the authors preprocessed the text by **removing punctuation, accents, and proper nouns** (specifically removing the names of municipalities and mayors).

**Short texts:** The text corpus consists of social media posts, which are inherently short, but the source does not explicitly discuss specific methodological considerations or challenges related to analyzing short texts.

**Spanish:** The corpus is in Spanish, which is evident from the translated top words provided in the results (e.g., "medidas", "cuarentena", "mascarilla"). However, the paper does not discuss any methodological challenges or preprocessing steps unique to the Spanish language.

**Interpretability:** **Yes**, interpretability is explicitly addressed. The authors note the methodological trade-off that extracting a higher number of topics can make the results "more detailed but less accurate or interpretable". They also state that "interpretable" was one of the core qualitative criteria for selecting their final 7 topics.

**Alternatives to LDA:** The source does not explicitly mention Latent Dirichlet Allocation (LDA) or alternatives like BERTopic or embeddings. When describing their chosen method, they simply state that STM, "unlike other models," does not consider word order but detects topics based on word correlations.




# N035_PDF005_G07


Based on the provided source, here is the venue positioning and precedent information for this article:

- **Journal:** The article was published in _**Political Communication**_ in 2023.
- **Why is it a precedent?** It establishes a strong precedent that this journal is highly receptive to **computational text analysis applied to massive, non-English datasets**,. Specifically, it demonstrates that the venue accepts research utilizing Structural Topic Modeling (STM) and data scraped directly from platform APIs (like CrowdTangle for Facebook/Instagram, and the Twitter API),. Furthermore, it shows the journal's openness to expanding beyond national elections in the Global North by publishing studies on local governments in developing democracies,.
- **Niche coverage:**
    - **Method:** Strong coverage. It applies STM to a large corpus of Spanish-language social media posts and demonstrates how to successfully incorporate structural covariates into the text analysis,,.
    - **Object:** Strong coverage. It directly investigates political actors' multi-platform social media strategies, explicitly comparing the use of Facebook, Twitter, and Instagram,.
    - **Region:** Strong coverage. It focuses entirely on a Latin American case study (Chile), validating the region's high inequality and structural features as critical variables for understanding political communication,.
    - **Theory:** Strong coverage. It engages with theories of how structural conditions heavily dictate digital political behavior, especially in societies experiencing severe crises of institutional legitimacy,,.
- **Type of precedent:** This article serves as both a **legitimating** and a **complementary** precedent.
    - It is **legitimating** because it proves that _Political Communication_ will publish research that relies on STM to analyze Spanish-language social media platforms,. It justifies that studying Latin American cases is not just a geographic novelty, but essential for understanding how structural inequalities override political variables.
    - It is a **complement** because it narrowly focuses on _local_ governments (mayors) during a specific public health crisis (the COVID-19 pandemic and lockdowns),. This leaves substantial room for Diego to study other political actors (like national candidates, parties, or movements) or different contexts (like electoral campaigns or digital advertising) while utilizing this paper as a methodological anchor.


