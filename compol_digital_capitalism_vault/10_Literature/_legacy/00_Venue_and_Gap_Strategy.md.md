# References Mapping LDA, digital ads, and Latin American campaigns across 16 communication journals

**No paper published in any of the 16 target journals between 2020 and 2025 applies LDA topic modeling to Chilean digital political advertising — the proposed niche is empirically unoccupied.** The closest analogues are an STM analysis of Chilean mayors' organic social-media posts (Aruguete, González-Bustamante et al., _Political Communication_ 2024), a Facebook-clustering study of 80 Chilean congressional campaigns (Toro et al., _JITP_ 2022), and a topic-modeling analysis of Chilean ideology in open-ended survey responses (Argote & Visconti, _LAPS_ 2025). The methodological building blocks all exist in the venue set — multiple journals publish topic-model and STM applications, several publish digital political-advertising work, and several publish Latin American computational political-communication research — but **no published paper combines all three elements (LDA + paid digital ads + Latin America) in this venue ecosystem.** This implies a clear research opening rather than a saturated competitive field. The most receptive venues, in order, are _International Journal of Press/Politics_, _Political Communication_, _Journal of Information Technology & Politics_, and _International Journal of Communication_.

## Section 1. Papers found, grouped by journal (most recent first)

### Tier 1: Political Communication (Routledge/T&F)

The strongest tier-1 venue for this niche — the only one with a Chile-specific computational-text-on-political-communication paper.

**Aruguete, González-Bustamante, Browne et al. (2024).** "Local Government, Social Media and Management of COVID-19: The Case of Chilean Mayoral Communication." _Political Communication_, 41(4). DOI: 10.1080/10584609.2023.2290494. **Method**: Structural Topic Model (STM) with covariates on Facebook/Twitter/Instagram posts. **Focus**: Chilean mayors, 2020–2021 including municipal election. **Findings**: Topical agendas conditioned by partisanship, government alignment, and socioeconomic variables. **Fit**: Closest direct precedent across the entire venue set — Chilean political actors + STM + social media + electoral context. Differs in unit (mayors not presidential candidates) and content type (organic posts not paid ads).

**Klinger, Koc-Michalska & Russmann (2023).** "Are Campaigns Getting Uglier, and Who Is to Blame? Negativity, Dramatization and Populism on Facebook in the 2014 and 2019 EP Election Campaigns." _Political Communication_, 40(3). Mostly manual content analysis with computational tone components. Complementary, not LDA.

**2021 Special Issue (Vol. 38, Nos. 1–2): "Computational Political Communication: Theory, Applications, and Interdisciplinary Challenges"** edited by Theocharis & Jungherr. Foundational pieces include Theocharis & Jungherr (2021) and Nicholls & Culpepper (2021) "Computational Identification of Media Frames" — the latter explicitly compares STM, LDA, doc2vec, and supervised methods on news framing. **This special issue is the strongest editorial signal of receptivity in the entire venue set.**

**Lukito (2020).** "Coordinating a Multi-Platform Disinformation Campaign: IRA Activity on Three U.S. Social Media Platforms, 2015 to 2017." _Political Communication_, 37(2), 238–255. Time-series with computational text features; complementary.

### Tier 1: Journal of Communication (Oxford/ICA)

**Aruguete, Calvo & Ventura (2023).** "Active Users, Selective Frames: Content Sharing and Perceived Polarization in Social Media." _Journal of Communication_, 73(1), 14–24. Computational text analysis of social-media news sharing; Latin American author team. Complementary.

**Yang, Pan, et al. (2023).** Visual misinformation on Facebook. _Journal of Communication_, 73(4). Computer-vision pipeline; ad-adjacent but not LDA.

JoC favors effects/experimental and network-analytic framings over unsupervised topic-modeling of candidate-side messaging. **Zero papers** combine LDA + political ads + LatAm.

### Tier 1: Communication Research (Sage)

**Zero matching papers identified.** Recent themed issues (2024–2025 polarization, deepfakes, machine authorship credibility) skew toward experiments and effects research. The least receptive of the tier-1 communication journals to descriptive LDA work on campaign content.

### Tier 1: Journal of Computer-Mediated Communication (Oxford/ICA)

**Carter et al. (2023).** "A Replication and Extension of the Personal Social Media Ecosystem Framework." _JCMC_, 28(6), zmad036. Combines Semantic Network Analysis and **LDA** — confirms the journal accepts the method, but the application is non-political. **Zero papers** on political advertising or LatAm campaigning in 2020–2025.

### Tier 1: Political Analysis (Cambridge)

The methodology-prestige venue — many text-as-data method papers, but no political-advertising or Latin-America applications.

**Kangaslahti, Ebanks, Kossaifi, Liu, Alvarez & Anandkumar (2026).** "Analyzing Political Text at Scale with Online Tensor LDA." _Political Analysis_, 34(1), 53–77. DOI: 10.1017/pan.2025.10024. New scalable Tensor LDA on #MeToo and 2020 election-fraud Twitter. **Direct legitimating precedent for LDA-on-large-Twitter corpora.**

**Wirsching, Rodriguez, Spirling & Stewart (2025).** "Multilanguage Word Embeddings for Social Scientists: Estimation, Inference, and Validation Resources for 157 Languages." _Political Analysis_ Letter, 33(2), 156–163. **Critical infrastructure citation for any Spanish-language text analysis.**

**Licht, H. (2023).** Cross-lingual classification of political texts using multilingual sentence embeddings. _Political Analysis_, _31_(3), 366-379.

**Wang (2024).** "Topic Classification for Political Texts with Pretrained Language Models." _Political Analysis_, 31(4). BERT-based topic classification — competitor framework to LDA.

**Osnabrügge, Ash & Morelli (2021/2023).** "Cross-Domain Topic Classification for Political Texts." _Political Analysis_. Trains on manifestos, applies to social-media campaign content. Direct competitor framing.

**Cocco & Monechi (2022).** "How Populist Are Parties? Measuring Degrees of Populism in Party Manifestos using Supervised Machine Learning." _Political Analysis_, 30(3), 311–327. Supervised alternative.

**Rheault & Cochrane (2020); Rodman (2020); Laurer, van Atteveldt, Casas & Welbers (2024); Stoehr et al. (2023); Watanabe (2025); Rainey (2024); Ornstein (2025); Alvarez & Morrier (2026); Herrmann & Döring (2023).** All methods-focused; together they show PA is methods-friendly but substantively distant from political ads or LatAm cases.

### Tier 1: Public Opinion Quarterly (Oxford)

**Zero matching papers.** POQ remains a survey-methods venue; topic-model use there centers on open-ended survey responses, not campaign content.

### Tier 1: New Media & Society (Sage)

**Larsson (2022).** "Picture-perfect populism: Tracing the rise of European populist parties on Facebook." _New Media & Society_. DOI: 10.1177/14614448221122997. Longitudinal structural content analysis; not topic modeling. Complementary.

**Larsson, Tønnesen, Magin & Skogerbø (2025).** "Calls to (what kind of?) action: A framework for comparing political actors' campaign strategies across social media platforms." _NMS_, 27. DOI: 10.1177/14614448241229156. Manual cross-platform coding; **explicitly contrasts itself with topic modeling, arguing manual coding handles visuals better.** Acts as a published methodological skeptic in the venue.

**Unlu, Truong, Sawhney & Tammi (2025).** "Setting the misinformation agenda: Modeling COVID-19 narratives in Twitter communities." _NMS_. DOI: 10.1177/14614448241232079. Text classification + topic modeling + community detection on Finnish Twitter. Confirms NMS publishes topic modeling, though not on ads.

**Gil de Zúñiga, Koc-Michalska & Römmele (2020).** Special-issue introduction on populism and Twitter. Editorial signal of receptivity.

**Boulianne, Hoffmann & Bossetta (2024).** Cross-platform politics survey. Not topic modeling. **Zero LDA-on-political-ads papers.**

### Tier 1: Information, Communication & Society (Routledge)

**Leerssen, Dobber, Helberger & de Vreese (2023).** "News from the ad archive: how journalists use the Facebook Ad Library to hold online advertising accountable." _Information, Communication & Society_, 26(7), 1381–1400. DOI: 10.1080/1369118X.2021.2009002. Qualitative content analysis + interviews; explicitly engages Facebook Ad Library data. **Strong signal of venue interest in political-ad transparency**, though not a topic-modeling paper.

**Pak (2021).** "Algorithmic inference, political interest, and exposure to news and politics on Facebook." _ICS_, 24(2), 183–200. Computational, not LDA.

**Schmuck & Hameleers (2020).** Cross-national content-analysis of populist Facebook/Twitter posts. _ICS_, 23(10). Manual coding.

**Zero LDA-on-political-ads papers** identified.

### Tier 2: International Journal of Press/Politics (Sage)

The strongest tier-2 venue and arguably the best substantive fit overall.

**Vrielink, Vliegenthart, van Remoortere & Kruikemeier (2025).** "What Matters to Voters? Analyzing the Influence of Targeted Online Ads on Perceived Issue Importance During the United States 2022 Midterm Election and the Dutch General Election 2021." _IJPP_ (online first 2025). DOI: 10.1177/19401612251371514. Multi-level analysis of submitted-screenshot ad data across Facebook/Instagram/YouTube/Google. **Direct substantive competitor** for digital-ad effects in IJPP.

**Pallister & Fitzpatrick (2024).** "The Medium and the Message in Argentina's Presidential Campaigns." _IJPP_. DOI: 10.1177/19401612221149272. Manual content analysis of TV spots and tweets across the 2015 and 2019 Argentine presidential elections. **Closest substantive analogue in the entire 16-journal set** — Latin American presidential campaign messaging across media. The Chilean LDA paper is essentially the methodological upgrade to this conversation.

**Orchard & González-Bustamante (2024).** "Power Hierarchies and Visibility in the News: Exploring Determinants of Politicians' Presence and Prominence in the Chilean Press (1991–2019)." _IJPP_, 29(1), 100–123. DOI: 10.1177/19401612221089482. Quantitative content analysis of Chilean elite press over three decades. **Strongest Chilean precedent in the venue set** — same authors as the _Political Communication_ 2024 piece. Direct citation target.

**Marques (2024).** "Populism and Critical Incidents in Journalism: Has Bolsonaro Disrupted the Mainstream Press in Brazil?" _IJPP_. DOI: 10.1177/19401612231153110. Mixed methods, Brazilian populism. LatAm precedent.

**(2024).** "Does Russian Propaganda Lead or Follow? Topic Coverage, User Engagement, and RT and Sputnik's Agenda Influence on US Media." _IJPP_ (Aug 2024). Topic-coverage computational analysis.

**Maurer, Jost, Schaaf, Sülflow & Kruschinski (2023).** "How Right-Wing Populists Instrumentalize News Media." _IJPP_. Time-series content analysis.

**Dobber, Metoui, Trilling, Helberger & de Vreese (2021).** "Do (Microtargeted) Deepfakes Have Real Effects on Political Attitudes?" _IJPP_, 26(1), 69–91. Experimental; signals IJPP's appetite for digital political ads research.

### Tier 2: Social Media + Society (Sage, OA)

**Lee & Rojas (2025).** "More than Two-Party Divides? Social Media, Ideological Extremity, and Affective Polarization in the Multi-party System." _Social Media + Society_, 11. Colombian survey; LatAm-relevant.

**Heseltine (2024).** "Asymmetric Polarization in Online Media Engagement in the United States Congress." _Social Media + Society_. Engagement metrics + ideology; computational, not LDA.

**Bossetta (2020).** "Scandalous Design: How Social Media Platforms' Responses to Scandal Impacts Campaigns and Elections." _Social Media + Society_, 6(2). DOI: 10.1177/2056305120924777. Engages Facebook Ad Library conceptually.

**Saldaña & Rosenberg (2020)** (cited as adjacent precedent). "Incivility and Media Bias During the Presidential Election in Chile." Chilean digital campaigning precedent in this exact venue, though pre-LDA in method.

**López-Escarcena, Ortega-Gunckel & Gronemeyer (2025).** Connective democracy on X/Twitter and YouTube around the 2020 Chilean plebiscite — direct Chilean digital-politics precedent in this venue.

The 2021 Latin America editorial ("Social Media and Democracy in Latin America," _SM+S_ 7(1)) and the 2025 Sujon-Dyer-Soares editorial both signal continuing receptivity.

### Tier 2: Journal of Information Technology & Politics (Routledge)

The single most precedent-rich venue for this exact niche.

**Cammaerts et al. (2025).** "Facebook election advertising: dangerous for democracy or politics as usual? The case of the 2017 UK general election." _JITP_. DOI: 10.1080/19331681.2025.2487085. **Direct precedent — Facebook political ads, electoral context, in JITP.**

**(2024).** "Resisting right-wing populism in power: a comparative analysis of the Facebook activities of social movements in Italy and the UK." _JITP_, 21(3). DOI: 10.1080/19331681.2023.2262973. **Mixed-method with two-step quantitative text analysis based on Topic Model and Dictionary Method.** Direct LDA-class precedent.

**(2023/2024).** "Manufacturing conflict or advocating peace? A study of social bots agenda building in the Twitter discussion of the Russia-Ukraine war." _JITP_, 21(2). Time-series + **STM** on Twitter.

**Toro et al. (2022).** "Much Ado About Facebook? Evidence from 80 Congressional Campaigns in Chile." _JITP_, 19(2). DOI: 10.1080/19331681.2021.1936334. **The single most direct precedent in the entire venue set — Chile + Facebook + congressional campaign messaging + clustering.** Different election (legislative vs. presidential) and different method (clustering vs. LDA).

**Crockett et al. (2021).** "FBAdLibrarian and Pykognition: open science tools for the collection and emotion detection of images in Facebook political ads with computer vision." _JITP_, 18. DOI: 10.1080/19331681.2021.1928579. Confirms Facebook Ad Library tooling pipeline at JITP.

**(2024).** "Blending positivity energy and fun: dominant discourse patterns of popular short videos in China's mobile media communication." _JITP_. **Topic modeling + social network analysis** on Chinese platforms.

### Tier 2: International Journal of Communication (USC Annenberg)

The largest reservoir of LatAm-focused political-communication research, though most uses content analysis rather than LDA.

**Mellado, Lagos et al. (2024).** "Between Hagiography and Self-Trolling: Multimodal Analysis of Memes for Boric in the 2021 Chilean Presidential Election." _International Journal of Communication_, 18, 4935–4961. **Direct competitor in venue and case** (IJoC + Chilean 2021 presidential election + digital campaign content) — but uses qualitative multimodal analysis. **The user's LDA paper would be the methodological pair to it.**

**Cazzamatta, Santos & Albuquerque (2024).** "Unveiling Disinformation: Mapping Attacks on Brazil's Electoral System." _IJoC_, 18, 3551–3575. Quantitative content analysis with reported "Top Five Topics" (possible undocumented topic-modeling component).

**Chagas (2022).** "WhatsApp and Digital Astroturfing: A Social Network Analysis of Brazilian Political Discussion Groups of Bolsonaro's Supporters." _IJoC_, 16, 2431–2455. SNA on 760,000 messages from the 2018 Brazilian election.

**Santini, Ruediger et al. (2021).** Bots and computational propaganda in Brazil's 2018 election. _IJoC_, 15, 1220–1243.

**Dourado, Piaia, Chagas et al. (2022).** Brazilian disinformation typology on WhatsApp/Facebook. _IJoC_, 16.

**Ituassu et al. (2023).** "Postmodern Without Modernization: Historicizing Digital Campaigns in Brazil 2010–2020." _IJoC_, 17, 3133–3153.

A 2023 _IJoC_ piece (vol. 17, 6718–6740) uses STM on YouTube right-wing influencers — non-LatAm but confirms STM acceptance.

### Tier 2: Latin American Politics and Society (Cambridge)

**Argote & Visconti (2025).** "Causes and Consequences of Ideological Persistence: The Case of Chile." _Latin American Politics and Society_, 67(4), 80–103. **Topic modeling on open-ended Chilean survey responses about "the Left" and "the Right."** **The single explicit topic-modeling-on-Chilean-political-text precedent in the entire 16-journal set.** Not on advertising, but the venue's most important signal of receptivity to the method on Chilean material.

**Olivella, Loubaton et al.** "Tweeting Antagonism: (De)Polarizing Rhetoric and Tone in Colombia's 2022 Presidential Campaign." _LAPS_. Tweet-level rhetoric/tone analysis (likely supervised classifier/dictionary). **Direct LatAm digital-campaign computational precedent.**

**Aruguete, Calvo, Cantú et al. (2021/22).** "Will I Get COVID-19? Partisanship, Social Media Frames, and Perceptions of Health Risk in Brazil." _LAPS_. Social-media frame experiment.

### Tier 2: Journal of Politics in Latin America (Sage)

**Zero text-as-data papers on political advertising or digital campaigning identified.** Multiple Chile-focused articles (De la Cerda 2022; Cox, González & Le Foulon 2024; Munita-Morgan, Navia & Bo Guzmán 2025; Cella & Castro Cornejo 2026) all use survey or roll-call data.

### Tier 2: Journal of Elections, Public Opinion & Parties (Routledge)

**Greene & McMillan (2020).** "The independence echo: the rise of the constitutional question in Scottish election manifestos and voter behaviour." _JEPOP_, 30(3), 317–338. Quantitative manifesto coding via the Regional Manifestos Project — topic-coded data, not LDA. The author's editorial role under Greene may modestly raise receptivity to computational party communication, but **zero LDA-on-digital-campaigning papers** were identified.

### Tier 2: Latin American Research Review (Cambridge)

**Zero matching papers.** A 2025 issue piece on Bukele's Twitter/X campaign in El Salvador uses qualitative discourse analysis. LARR remains predominantly area-studies and qualitative for political-communication topics.

## Section 2. Summary table

|Journal|Relevant text-as-data papers (2020–25)|Most recent year|Any Chilean/LatAm case?|
|---|---|---|---|
|**Political Communication** (T1)|~6 (incl. 2021 special issue)|2024|**Yes** — Chile (mayors, STM, 2024)|
|**Journal of Communication** (T1)|2–3|2023|Argentine authorship (Aruguete/Calvo)|
|**Communication Research** (T1)|0|—|No|
|**JCMC** (T1)|1 (LDA, non-political)|2023|No|
|**Political Analysis** (T1)|~15 methodological|2026|No|
|**Public Opinion Quarterly** (T1)|0|—|No|
|**New Media & Society** (T1)|3–4|2025|No (Finnish, European)|
|**Information, Communication & Society** (T1)|2–4|2023|No|
|**International Journal of Press/Politics** (T2)|≥8|2025|**Yes** — Chile (Orchard 2024); Argentina (Pallister 2024); Brazil (Marques 2024)|
|**Social Media + Society** (T2)|5–6|2025|**Yes** — Colombia (Lee & Rojas 2025); Chilean editorials|
|**Journal of Information Technology & Politics** (T2)|6–7|2025|**Yes** — Chile (Toro 2022)|
|**Journal of Politics in Latin America** (T2)|0|—|No (no computational text)|
|**Latin American Politics and Society** (T2)|≥3|2025|**Yes** — Chile (Argote & Visconti 2025); Colombia 2022; Brazil|
|**Latin American Research Review** (T2)|0|—|No|
|**International Journal of Communication** (T2)|≥6|2024|**Yes** — Chile (Mellado 2024); multiple Brazil pieces|
|**Journal of Elections, Public Opinion & Parties** (T2)|~1|2020|No|

## Section 3. Gap analysis

**Gap (a): LDA + political advertising specifically.** **Zero direct precedents in any of the 16 journals.** The closest hits are STM on organic Facebook posts (Aruguete et al. 2024 Chile; the JITP STM-on-Russia-Ukraine piece), the JITP topic-model-plus-dictionary paper on social-movement Facebook activity, the Cazzamatta et al. (IJoC 2024) "Top Five Topics" disinformation piece, and Stier et al.'s 2018 LDA on German candidate Facebook/Twitter (just outside the date window in _Political Communication_). Paid political ads from Meta or Google ad libraries have been studied qualitatively (Leerssen et al. 2023, ICS) and via tooling/computer vision (Crockett et al. 2021, JITP), but **no published paper in this venue set runs LDA on a political ad-archive corpus.** This is a clean, defensible gap.

**Gap (b): LDA + Latin American elections.** **One precedent (Argote & Visconti 2025, _LAPS_) — and it analyzes survey responses, not campaign content.** Latin American digital politics has been studied in these journals via SNA (Chagas 2022 IJoC), bot detection (Santini et al. 2021 IJoC), supervised content classification (Olivella et al. _LAPS_), manual coding (Pallister & Fitzpatrick 2024 IJPP; Mellado et al. 2024 IJoC), and STM applied to Chilean mayors (Aruguete et al. 2024 _Political Communication_). **LDA on Latin American political ads or candidate digital campaigning is not yet published in this venue ecosystem.**

**Gap (c): LDA + digital campaigning generally.** **Partially filled, but mostly outside the political-ad subdomain.** Stier et al. (2018, _Political Communication_) is the canonical antecedent on candidate Facebook/Twitter. Kangaslahti et al. (2026, _Political Analysis_) legitimates LDA for large-scale political Twitter. The JITP topic-model-plus-dictionary piece (2024) and JITP STM piece on Russia-Ukraine Twitter (2024) demonstrate ongoing acceptance. The Unlu et al. (2025) _NMS_ topic-modeling piece confirms cross-venue method acceptance. Yet these all study organic content, not paid advertising. **The combination of (LDA) × (paid digital campaign ads) × (any region) remains thinly published in the 16-journal set.**

## Section 4. Competitive-landscape assessment

**The proposed paper's combination of LDA + Chilean presidential digital ads sits in a clearly unfilled niche, not a saturated one.** The strongest evidence: a comprehensive author-reading scholar like Bastián González-Bustamante — who has published the closest analogue in _Political Communication_ (Chilean mayors, STM, 2024) and the most-cited Chilean media-quantification piece in _IJPP_ (2024) — has not published an LDA-on-Chilean-political-ads paper. The same is true of Mellado, Saldaña, Scherman, Valenzuela, Halpern, Aruguete, and Calvo, whose Chilean and Latin American digital-politics output appears across these venues using non-LDA methods (manual coding, SNA, frame experiments, supervised classifiers, dictionaries).

**Differentiation strategy.** The proposed paper should foreground three distinguishing claims:

1. **Object distinctiveness** — paid digital ads from platform-mandated archives (Meta Ad Library, Google Ad Transparency) are a different empirical object from organic candidate posts (which Aruguete et al. 2024 and Toro et al. 2022 covered) and from news-media coverage (Orchard & González-Bustamante 2024). Position the contribution against Vrielink et al.'s 2025 _IJPP_ targeted-ad-effects paper, which uses ad data but not topic modeling.
    
2. **Methodological calibration to Spanish-language Chilean political vocabulary** — cite Wirsching, Rodriguez, Spirling & Stewart's 2025 multilingual embedding infrastructure and Vallejo Vera/Timoneda's cross-lingual classification work in _Political Analysis_ as scaffolding, then justify LDA's interpretive transparency over BERTopic and supervised classifiers in a single-country, low-annotated-resource setting. This addresses the methodological-skeptic posture published in _NMS_ (Larsson et al. 2025) preemptively.
    
3. **Theoretical anchoring** — bind the descriptive topic findings to a substantive theoretical claim (issue ownership, populist communication, microtargeting, second-order elections) so the paper does not read as a purely descriptive computational exercise. _Journal of Communication_ and _New Media & Society_ effectively require this.
    

**Recommended venue ladder, by descending fit:**

The strongest first submission target is _**International Journal of Press/Politics**_, where Pallister & Fitzpatrick (2024) on Argentine campaigns and Orchard & González-Bustamante (2024) on Chilean media visibility form a built-in citation context, Vrielink et al. (2025) provides a digital-ads anchor, and Dobber et al. (2021) signals platform-ads receptivity. The second target is _**Political Communication**_, anchored to Aruguete et al. (2024) and the 2021 special issue legacy — but there the paper must offer stronger theoretical and effects-oriented framing. The third target is _**Journal of Information Technology & Politics**_, where Toro et al. (2022) and the existing topic-modeling and Facebook-Ad-Library precedents make this the most methodologically natural home, though prestige is lower. _**International Journal of Communication**_ is a strong open-access fallback with a built-in audience for the case (Mellado et al. 2024) and should be considered if a faster turnaround matters. _**Latin American Politics and Society**_ is viable if reframed around partisanship, polarization, or ideological persistence using Argote & Visconti (2025) as the methodological precedent. _Communication Research_, _Public Opinion Quarterly_, _Latin American Research Review_, _Journal of Politics in Latin America_, and _JEPOP_ should be deprioritized — none has published a comparable text-as-data digital-campaign study in the 2020–2025 window.

## Conclusion

The data tell a consistent story: **the methodological tools, the empirical case, and the regional interest each have published precedents in this venue ecosystem — but no one has yet brought all three together.** That is rare in 2025 for a niche this active, and it likely reflects the recency of usable Latin American political ad-archive data combined with the persistent methodological preference of LatAm-focused communication research for content analysis and SNA. The opening is real and time-sensitive; the most defensible framing positions the paper as the methodological complement to qualitative and content-analytic Chilean digital-politics work (Mellado et al. 2024; Pallister & Fitzpatrick 2024) and the substantive Latin American extension of established LDA/STM political-text scholarship (Stier et al. 2018; Aruguete et al. 2024; Kangaslahti et al. 2026). _International Journal of Press/Politics_ is the recommended primary target.