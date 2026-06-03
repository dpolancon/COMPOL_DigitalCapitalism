
# N036_PDF006_P00


**1. What is the source’s main theoretical object: platform capitalism, digital labor, data extraction, digital governance, algorithmic control, cybernetics, posthumanism, Marx, political subjectivity, other?** The source does not explicitly draw on critical theory, Marxism, or cybernetics; rather, its main theoretical object is **digital governance and political communication** mediated by structural inequality. It investigates how the use of social media as an interface between the state and citizens is dictated by the material and socioeconomic contexts of the population, rather than the autonomous logic of the technology itself.

**2. What mechanism links digital technology to power?** The mechanism linking digital technology to power in this text is the role of platforms as **digital extensions of "street-level bureaucracy"**. In highly unequal societies, affluent groups rely on private provisions, while vulnerable populations are heavily dependent on the local state for survival. When crises (like lockdowns) close physical access, social media becomes the primary, indispensable lifeline to power and welfare. Technology here does not "disrupt" power; instead, platforms replicate and absorb the pre-existing structural power dynamics of state dependency.

**3. Does the source help theorize political advertising as a platform-mediated infrastructure of visibility/control?** While the source does not discuss paid political advertising, it absolutely helps theorize platforms as **infrastructures of visibility and control**. It demonstrates how platforms cease to be mere communication tools and instead become the mandatory, material infrastructure through which the state governs, targets populations, and distributes resources. It proves that digital visibility strategies are not universal but are sharply segmented by class: governments use these platforms specifically to manage and control information for the poor who have no alternative channels.

**4. What concepts are portable to Diego’s conceptual framework without overloading the paper?**

- **The "Structural Override":** The concept that material and socioeconomic conditions (like poverty and geographic divides) heavily dictate digital communication strategies, overriding pure political or partisan calculations.
- **Platforms as State Infrastructure:** The idea that social media acts as an essential, rapid-response infrastructure for welfare distribution and state communication in the Global South, especially when physical institutions fail or are shut down.
- **The Myth of Uniform Technological Disruption:** The argument that social media does not constitute a universal "technological disruption" of political logic, but rather adapts to the varying structural functions that different governments perform based on their territory's wealth.

**5. What should NOT be imported because it is too broad or unrelated?** Do not import the specific empirical details regarding COVID-19 pandemic management (such as the "Plan Paso a Paso" lockdown phases, critical-care bed availability, or the vaccination calendar). Additionally, the deep focus on mayoral administrative duties and incumbency rates is likely too specific to local governance to map neatly onto a broader theory of digital capitalism or national digital campaigns.

**6. Provide 3 concise conceptual building blocks that could be used in a literature/theory note.**

- **Material Limits of Digital Disruption:** The impact of social media in political communication is heavily bounded by the socioeconomic realities of the territory; digital tools reflect pre-existing structural inequalities rather than universally disrupting how politics is done.
- **Platforms as Welfare Intermediaries:** In unequal Latin American societies, social media platforms function as critical civic infrastructures, acting as the primary point of contact for vulnerable populations who rely entirely on the local state for resources and information.
- **Structural Over Political Logics:** The volume, content, and engagement of digital political communication are driven more significantly by the structural needs of the populace (e.g., poverty levels) than by the partisan affiliation, ideology, or strategic electoral positioning of the political actor.

Saved responses are vi


# N037_PDF006_P01

**1. Bibliographic identity**

- **Author(s):** Juan Pablo Luna, Daniel Alcatruz, Cristian Pérez Muñoz, Fernando Rosenblatt, Sergio Toro Maureira, and Sebastián Valenzuela.
- **Year:** 2023.
- **Title:** Local Government, Social Media and Management of COVID-19: The Case of Chilean Mayoral Communication.
- **Journal:** Political Communication.
- **DOI:** 10.1080/10584609.2023.2290494.

**2. Research object**

- The study analyzes how local political leaders (mayors) use social media to communicate with their constituents, explicitly testing whether this communication is driven by political variables (partisanship, electoral incentives) or by structural and socioeconomic factors.

**3. Case and scope**

- **Country/Region:** Chile, specifically focusing on the 52 communes of the Santiago Metropolitan Region (which comprises 42% of the country's population).
- **Election/cycle:** The study spans from March 3, 2020 (the first COVID-19 case in Chile) to June 28, 2021 (the municipal elections). This period immediately followed the October 2019 "social uprising," a time of intense institutional legitimacy crisis.
- **Sample size:** A total corpus of 264,387 posts scraped from the personal and institutional Facebook, Instagram, and Twitter accounts of all 52 mayors.

**4. Method**

- **Data Collection:** Collected social media posts using the CrowdTangle API (for Facebook and Instagram) and the Twitter API.
- **Engagement Index:** Created a custom index to measure citizen interaction by dividing the raw count of reactions by the total number of posts, scaled by 100.
- **Topic Modeling (STM):** Employed Structural Topic Models (STM) to identify latent themes in the text. They included external covariates at the document level: poverty rate, number of COVID-19 cases, population size, rural/urban dummy, mayoral incumbency, and political alignment with the national government.
- **Preprocessing and Validation:** Used the `quanteda` R package to remove punctuation, accents, and proper nouns (names of municipalities and mayors). Tested models with _k_ ranging from 5 to 50 topics, ultimately selecting _k_=25 based on semantic coherence and exclusivity, and retaining 7 highly interpretable topics for the main analysis.

**5. Core claim**

- **Structural factors override political incentives:** A municipality's socioeconomic context (specifically poverty levels) heavily dictates its social media strategy, whereas political variables (mayoral incumbency or alignment with the national government) have no significant effect on the content or frequency of posts.
- **The lockdown discontinuity:** Because poor households rely on the local state for survival (acting as "street-level bureaucrats" for welfare), strict lockdowns forced poorer municipalities to drastically increase their social media posting to coordinate critical assistance. Wealthier municipalities, which rely on private provision, did not significantly alter their posting behavior during lockdowns.
- **Engagement dynamics:** The highest levels of citizen engagement per post occurred in poorer and rural municipalities, rather than being driven by the severity of the local COVID-19 outbreak or population size.
- **Platform differences:** Mayors preferred Twitter for broadcasting COVID-19 prevention messaging, while Facebook was utilized more heavily for organizing social support networks.

**6. Relevance to Diego paper**

- **Methodological Precedent:** Provides a highly relevant, peer-reviewed precedent for applying Structural Topic Modeling (STM) to a massive corpus of short, Spanish-language social media texts. It specifically demonstrates how to integrate structural covariates (like poverty and rural/urban divides) into topic modeling.
- **Chile / LatAm Context:** Offers crucial context on the 2019-2021 Chilean political cycle, emphasizing how deep structural inequality dictates state-citizen digital relationships, especially when traditional national institutions lose legitimacy.
- **Platformization / Digital Politics:** Counters the pure "technological disruption" narrative by demonstrating that platforms absorb and replicate pre-existing structural power dynamics; digital communication strategies are not uniform but are sharply segmented by class and state capacity.

**7. Exact extraction anchors**

- **On structural vs. political variables:** "We found that mayors’ social media communication strategies depend on the functions that different municipalities perform in the territory, and that socioeconomic variables differentiate these activities."
- **On social media substituting physical welfare state presence:** "...in poor municipalities, lockdowns implied that some critical services and government programs, which are targeted at poor families, were not offered, or had to be restructured. Thus, social media provided a direct and fast means of communication for contacting the targeted population."
- **On the lack of political effects:** "The political variables—incumbency and political alignment with the national government—do not affect the prevalence of any topic."

**8. Limitations**

- **Unobserved Mechanisms:** The authors concede they could not explicitly measure several confounding variables, such as the size and professionalization of municipal public relations departments (which are likely larger in wealthy urban districts), or the mitigating influence of traditional broadcast media like local radio and television.
- **Geographic Scope:** The study is restricted to the Santiago Metropolitan Region; thus, it does not capture the unique dynamics of municipalities in the extreme north or south of the country



# N038_PDF006_P02


**1. Does the source study paid political advertising?** **No.** The source does not investigate paid political advertising, dark posts, or algorithmic ad targeting. It strictly analyzes a corpus of 264,387 **organic social media posts** published on the personal and institutional accounts of 52 city mayors in the Santiago Metropolitan Region.

**2. Which platforms are analyzed?** The study analyzes organic posts across **Facebook, Instagram, and Twitter**.

**3. What are the key findings regarding platforms and targeting?** While the study does not examine paid financial targeting, it highlights organic "targeting" strategies shaped by platform affordances and structural needs:

- **Platform affordances:** Mayors favored **Twitter** for broadcasting public health information and COVID-19 prevention messaging, whereas **Facebook** was used more frequently for communicating about social support networks.
- **Structural targeting:** The study finds that the "targeting" of specific messages was driven by socioeconomic factors rather than political alignment. For instance, during lockdowns, mayors of poorer municipalities specifically targeted their populations with information regarding registries and the administration of support networks, because these vulnerable populations rely heavily on the local state for welfare and survival. Conversely, wealthier municipalities, which rely more on private self-provision, did not need to target their populations with this level of digital welfare assistance.

**4. How does this connect to Diego's research object?** This source has **null relevance for analyzing the mechanics, spending, or regulatory evasion of paid political ads**.

However, if Diego's conceptual framework involves comparing paid digital strategies to organic ones in Latin America, this paper provides a strong theoretical baseline. It demonstrates that in highly unequal societies, organic digital communication is not a uniform "technological disruption" driven by electoral or partisan strategy; instead, it is heavily constrained and driven by pre-existing structural inequalities and the material needs of the population.

Saved responses are view only

NotebookLM can be inaccurate; please double check its responses.



# N039_PDF006_P03


Based on the provided source (Luna et al. 2023), here is the extracted material regarding the digitalization and platformization of politics:

**1. What is the source’s concept of digitalization/platformization?** The source pushes back against the idea that social media constitutes a universal "technological disruption" that fundamentally changes how politics is done. Instead, it conceptualizes digital platforms as communication tools whose usage and impact are heavily bounded by pre-existing material and socioeconomic realities. In unequal societies, platformization replicates offline structural dynamics; digital communication becomes a lifeline for vulnerable populations but remains a secondary channel for affluent groups who do not depend on the state.

**2. Which actors matter: campaigns, platforms, voters, journalists, regulators, parties, movements?** The primary actors in this study are:

- **Local Authorities (Mayors):** Who act as the "street-level bureaucrats" managing crisis communication and welfare distribution.
- **Citizens/Constituencies:** Specifically differentiated by socioeconomic class and their level of material dependence on the local state.
- **Platforms:** Facebook, Twitter, and Instagram are the primary conduits for this communication.
- **The National Government:** Which sets the overarching pandemic policies (lockdowns, vaccinations) that local actors must navigate and communicate.

**3. Does the source treat platforms as neutral channels or active infrastructures?** The source treats platforms as **vital, active infrastructures for state governance and welfare**, rather than just neutral communication channels. During the COVID-19 lockdowns, platforms essentially replaced physical municipal buildings as the primary infrastructure through which the state could target vulnerable populations and administer social support networks. Furthermore, the study notes specific platform affordances: municipal authorities treated Twitter as the optimal infrastructure for broadcasting public health and prevention messaging, while Facebook was utilized as the primary infrastructure for coordinating social support and citizen registries.

**4. Is the argument global/comparative, national, or regional?** The empirical scope is strictly **national and local**, focusing on the 52 municipalities of the Santiago Metropolitan Region in Chile. However, the theoretical argument is framed to apply to **unequal and developing societies**, specifically within Latin America, where profound structural inequalities dictate the relationship between citizens and the state.

**5. What mechanisms link digital platforms to campaign/communication strategy?**

- **The "Structural Override":** The core mechanism is that socioeconomic variables dictate a political actor's digital strategy far more than political calculations (like partisanship, electoral goals, or government alignment).
- **Digital Welfare Dependency:** In poor municipalities, strict lockdowns severed physical access to essential government programs. The mechanism driving digital communication was survival: mayors were forced to dramatically increase their use of platforms to digitally administer welfare and support registries for dependent populations. Wealthy municipalities did not experience this shift because their residents rely on private self-provision.

**6. What sentence could Diego cite to connect Chile 2021 to a broader transformation of political communication?** To argue that the digitalization of politics in Latin America is fundamentally constrained by structural inequality rather than pure electoral strategy or universal technological disruption, Diego could cite:

"The findings suggest that social media platforms, at least in the Chilean political context, do not supplant the influence of structural factors in determining how political leaders communicate and connect with their constituencies. Their use does not constitute a technological disruption in how politics is done in the country".

Alternatively, regarding how platforms function as a substitute for physical welfare state access:

"...in poor municipalities, lockdowns implied that some critical services and government programs, which are targeted at poor families, were not offered, or had to be restructured. Thus, social media provided a direct and fast means of communication for contacting the targeted population".



# N040_PDF006_P05

Based on the provided source, the study does **not** focus on the typical ethical risks of computational propaganda, such as **manipulation, misinformation, opacity, privacy, or polarization**. Instead, the primary democratic concern identified aligns with **unequal exposure** and the reproduction of **structural inequality** in digital state-citizen relationships.

**1. What democratic risks are identified?**

- **Unequal Exposure and Structural Dependency:** The core democratic concern is that in highly unequal societies, digital communication is not a uniformly empowering or equalizing tool; rather, it reflects and replicates deep structural inequalities. Vulnerable populations are structurally dependent on their local municipalities for basic welfare and survival. During the strict COVID-19 lockdowns, these poorer citizens were forced to rely heavily on platforms like Facebook and Twitter as an indispensable lifeline to access critical state services, whereas wealthier citizens relied on private self-provision and did not face this vulnerability.
- **Limits of Technological Democratization:** The authors offer a "nuanced, if pessimistic, account of the political effects of technologies". They warn against the assumption that social media universally democratizes or disrupts politics, emphasizing instead that platforms merely absorb the offline socioeconomic divisions and differing levels of state capacity across different territories.

**2. Does the source distinguish fear from evidence?** Because the paper does not study malicious manipulation or fake news, it does not contrast theoretical "fear" against evidence in the context of disinformation. However, it does rely on robust **empirical evidence**—analyzing a corpus of 264,387 social media posts using Structural Topic Modeling (STM)—to test broad assumptions about how politicians use social media.

The evidence demonstrates that structural, socioeconomic, and welfare realities—rather than pure political strategizing, partisan alignment, or electoral calculations—primarily drove the differences in how mayors communicated digitally with their constituents.


# N042_PDF006_G03

Here is how the source conceptualizes digitalization and platformization:

**1. Definition of Digitalization/Platformization** The source pushes back against the idea that social media constitutes a universal "technological disruption" that fundamentally changes how politics operates. Instead, it conceptualizes digital platformization as a process that **reflects and replicates pre-existing offline structural and socioeconomic inequalities**. Rather than offering novel communicational strategies that disrupt the political landscape, platforms are viewed primarily as tools used to perform the exact same administrative and welfare tasks that are traditionally carried out offline.

**2. Mechanisms Named** The source identifies several specific mechanisms linking platforms to political communication strategies:

- **The "Structural Override":** The primary mechanism driving digital strategy is the socioeconomic reality of the population. A municipality's poverty level and material needs dictate its digital communication strategy far more than political variables such as mayoral partisanship, incumbency, or alignment with the national government.
- **Digital Welfare Dependency ("Street-Level Bureaucracy"):** Because vulnerable populations in highly unequal societies rely heavily on the local state for survival, municipalities act as "street-level bureaucrats". When physical access was cut off during lockdowns, mayors in poorer areas were forced to dramatically increase their social media use to manage critical welfare registries and targeted social programs. Wealthier populations, who rely on private self-provision, did not trigger this mechanism.
- **Platform-Specific Affordances:** The study notes that distinct platforms serve different administrative functions. Mayors utilized Twitter more frequently to broadcast COVID-19 prevention measures and public health alerts, whereas Facebook was the preferred mechanism for coordinating social support and citizen registries.

**3. Passive Channels or Active Infrastructures?** The source treats platforms as **active, vital state infrastructures** rather than merely passive communication channels. During the strict COVID-19 lockdowns, social media essentially replaced physical municipal buildings, acting as the primary, indispensable infrastructure through which the state could locate vulnerable populations, distribute resources, and administer social support networks.

**4. Global, Local, or Comparative Pattern?** The empirical scope of the study is strictly **local and national**, focusing specifically on the 52 communes of the Santiago Metropolitan Region in Chile. However, the authors frame their findings as a **comparative pattern**, arguing that these dynamics apply broadly to highly unequal, developing societies (especially in Latin America) where deep structural divides heavily condition the relationship between citizens and the state.




# N043_PDF006_G05


The primary democratic concern identified in this source is **unequal exposure** and the reproduction of **structural inequality**. The authors do not focus on typical digital risks such as manipulation, privacy, polarization, misinformation, opacity, or persuasion.

**1. What democratic risk is identified?**

- **Unequal Exposure and Structural Dependency:** The core democratic concern is that in highly unequal societies, digital communication is not a uniformly empowering or equalizing tool; rather, it reflects and replicates deep offline structural inequalities. Vulnerable populations are structurally dependent on their local municipalities—which act as "street-level bureaucrats"—for basic welfare and survival.
- **The Limits of Democratization:** The study warns against the assumption that social media universally democratizes or disrupts politics. Because poor households rely on the local state for survival, strict COVID-19 lockdowns forced poorer citizens to rely heavily on platforms as an indispensable lifeline to access critical state services, whereas wealthier citizens, who rely on private self-provision, did not face this same digital vulnerability.

**2. Does the source distinguish fear from evidence?** Because the paper does not study malicious manipulation or fake news, it does not explicitly contrast theoretical "fear" against evidence in the context of disinformation. However, it grounds its claims in robust **empirical evidence** to counter broad theoretical assumptions about how politicians use social media.

Instead of assuming that politicians uniformly use digital platforms for novel, manipulative electoral strategies, the authors provide a "nuanced, if pessimistic, account of the political effects of technologies". They test their hypotheses using empirical data—analyzing a corpus of 264,387 social media posts using Structural Topic Modeling (STM)—to prove that structural, socioeconomic, and welfare realities override pure political strategizing, partisan alignment, or electoral calculations in driving digital communication strategies.
