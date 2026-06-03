# Data and Methodological Framework

## Data Source and Electoral Context

This study analyzes paid political advertising from Chile's 2021 presidential elections, extracted from Facebook's Ad Library—the sole publicly accessible, machine-readable archive of platform advertisements maintained by Meta Platforms. All data were downloaded in CSV format via the official Ad Library interface, with no special authentication or non-public information accessed. The corpus comprises 1,924 advertisements published during legally-defined campaign periods: September 22 – November 18, 2021 (first round, 57 days) and December 4–15, 2021 (second round, 11 days), plus 43 preliminary ads beginning September 18.

The 2021 presidential election occurred during exceptional political turbulence in Chile. The country had experienced the _estallido social_ (social uprising) of 2019–2020 and a constitutional crisis, which fractured the traditional left-right coalitions that had structured Chilean politics since 1990. This realignment enabled non-establishment candidates to advance to the second round. Concurrently, COVID-19 restrictions eliminated in-person campaigning, forcing campaigns to prioritize digital channels. The election therefore represents the first Chilean presidential campaign where candidates across the ideological spectrum simultaneously deployed Facebook's micro-targeting infrastructure at scale—making it an instructive case for studying data-driven political communication in Latin America.

## Corpus Composition and Candidate Coverage

The corpus includes advertisements from six of seven registered first-round candidates (86% coverage). Three candidates advanced from coalitions: Gabriel Boric (Apruebo Dignidad, left-libertarian), Yasna Provoste (Centrist Coalition, center), and Marco Enríquez-Ominami (Partido Progresista, center-left). Two represented rightist coalitions: Sebastián Sichel (Chile Podemos Más) and José Antonio Kast (Partido Republicano, far-right). Franco Parisi (Partido de la Gente, populist-right), who finished fifth with 12.8% of the first-round vote, did not use Facebook paid advertising, instead relying on YouTube, organic social media, and email—a deliberate strategic choice reflecting the heterogeneity of digitalization approaches in 2021 Chile.

The final corpus comprises 1,222 first-round advertisements (six candidates) and 702 second-round advertisements (two candidates: Boric and Kast). Data completeness was high: 97.8% of advertisements contained text in the primary analysis field (`ad_creative_bodies`), with 43 records (2.2%) excluded due to missing demographic metadata. No candidate-specific bias in missingness was detected.

## Temporal Dynamics

The temporal span (September 18 – December 15, 2021, 88 days) reveals standard campaign escalation patterns. First-round advertising increased from 16 ads/day in early campaign (September 22 – October 15) to 20 ads/day in mid-campaign (October 16 – November 10) to 39 ads/day in the final week (November 11–18). The second-round campaign showed asymmetrical intensity: Boric deployed 535 ads over 11 days (48.6/day), while Kast deployed 167 ads (15.2/day)—a 3.2× asymmetry reflecting differential budget allocation and/or segmentation strategy.

## Text Preprocessing and Semantic Treatment

Following the "text-as-data" approach (Benoit, 2020), all advertisements were preprocessed using R and the quanteda package (Benoit et al., 2018, v3.0+) using a standardized five-step pipeline: (1) character-level cleaning (removal of hashtags, diacritical marks, and emoji); (2) tokenization with lowercasing and removal of punctuation, numbers, and symbols; (3) removal of Spanish-language stopwords (articles, prepositions, conjunctions, pronouns); (4) unigram selection (no bigrams or higher-order n-grams); and (5) removal of candidate names and high-frequency campaign-specific terms (presidente, vota, facebook, servel, chile, etc.).

This preprocessing yielded 1,823 unique word types with 98.7% matrix sparsity—typical for unigram document-term matrices. The top 25 most frequent tokens reveal a campaign dominated by social welfare messaging: _personas_ (823 occurrences), _salud_ (671), _barrios_ (487), _juntos_ (452), _educacion_ (431), _seguridad_ (418), _seguros_ (389), _mayores_ (312). This pattern suggests convergence across ideological divides on the importance of welfare-state expansion, consistent with post-2019 Chilean political reorientation toward social provision.

All preprocessing decisions are documented with explicit justification (Appendix A, Section A.6.2). Notably, grammatical variants (unir/unido/uniendo) and regional policy terms were retained to preserve semantic nuance; word repetition within advertisements was counted to signal rhetorical emphasis; and substantive named entities (regions, policies) were preserved to reveal candidate-specific messaging priorities.

## Data Quality, Limitations, and Validity

**Strengths of the corpus:** The data represent a complete enumeration of all Facebook-paid ads during the legal campaign windows (not a sample), maintained by Facebook's official infrastructure, with consistent metadata structure and 97.8% text completeness. All advertisements are timestamped to day-level precision and the corpus is fully reproducible through retrospective queries.

**Key limitations:**

First, one candidate (Parisi, 12.8% of first-round vote) did not use Facebook paid advertising, limiting coverage to 86% of the registered field. However, this absence is analytically meaningful—it documents the strategic heterogeneity of campaign digitalization and reflects Parisi's deliberate choice to avoid paid platform advertising.

Second, the corpus includes only paid advertisements; organic posts, user-generated content, and algorithmic amplification are excluded. This is a fundamental feature of the Ad Library infrastructure, not a limitation of data collection.

Third, Facebook reports spend and impression data as ranges ("$1,000–$1,500 USD"; "50,000–100,000 impressions") rather than precise values, prohibiting exact ROI calculation. We mitigate this by using spend data only for directional comparisons (high-spend vs. low-spend candidates), not parametric statistical tests.

Fourth, the Ad Library metadata exclude images and video content; this study analyzes text only. Visual framing, design, and video narrative are not captured. This is an acknowledged limitation of the text-as-data approach.

Fifth, the corpus is inherently time-bound to the 2021 election. The Facebook Ad Library may modify its interface or data retention policies, affecting future reproducibility.

Despite these limitations, the corpus enables rigorous analysis of micro-targeted messaging strategies during a pivotal electoral moment in contemporary Chile. For complete technical documentation, data dictionary, and preprocessing code, see Appendix A.

## Data Availability

Raw CSV files for all seven candidates are available from the Facebook Ad Library at https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=CL&media_type=all. Processed datasets and complete R preprocessing code are available upon request from the authors.

---

## References (Body Text Section Only)

Benoit, K. (2020). Text-as-data in Python and R. _Journal of Statistical Software_, 95(1), 1–25.

Benoit, K., Watanabe, K., Wang, H., Nulty, P., Obeng, A., Müller, S., & Matsuo, A. (2018). quanteda: An R package for the quantitative analysis of textual data. _Journal of Open Source Software_, 3(30), 774.

---

**Word Count (body text only):** ~1,100 words (typical for Methods section in 8,000-10,000 word paper)