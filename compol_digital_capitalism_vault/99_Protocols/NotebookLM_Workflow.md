# NotebookLM Literature Gap-Filling Strategy

## Chilean Digital Political Advertising LDA Paper — Tier-1 Journal Preparation

**Project:** Text-as-data LDA topic modeling of political advertising from Chilean presidential elections (2021, 2025) as a case study of the globalization/digitalization of political communication.

**Objective:** Build a defensible, top-tier reference frame by systematically identifying literature gaps (methodological, theoretical, regional, and empirical) and using NotebookLM to synthesize targeted literature that closes each gap.

---

## Executive Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NOTEBOOKLM LITERATURE STRATEGY                      │
└─────────────────────────────────────────────────────────────────────────────┘

        ┌──────────────────┐
        │  PHASE 1: AUDIT  │
        │  & GAP ID        │
        └────────┬─────────┘
                 │
         ┌───────▼────────┐
         │ Upload all 120 │
         │ references to  │
         │ NotebookLM     │
         └───────┬────────┘
                 │
    ┌────────────┴─────────────────┬──────────────────┐
    │                              │                  │
┌───▼────────┐        ┌────────────▼────┐    ┌───────▼──────┐
│ Gap 1:     │        │ Gap 2: LDA       │    │ Gap 3:       │
│ Political  │        │ Methodological   │    │ Digitalization│
│ Advertising│        │ Innovation       │    │ of Politics  │
│ Theory     │        │ & Validation     │    │ & Latin Amer │
└───┬────────┘        └────────┬────────┘    └───────┬──────┘
    │                          │                      │
    │    ┌──────────────────────┴──────────────────┐  │
    │    │                                         │  │
    │ ┌──▼─────────────┐         ┌────────────────▼──▼────┐
    │ │ Ask NotebookLM │         │  Ask NotebookLM        │
    │ │ to synthesize  │         │  to map & compare      │
    │ │ across refs    │         │  methodological        │
    │ │ on topic       │         │  strengths/limits      │
    │ │                │         │                        │
    │ └──┬─────────────┘         └────────────┬───────────┘
    │    │                                    │
    └────┼────────────────────────────────────┼─────────────┐
         │                                    │             │
    ┌────▼──────────────────────────────────────▼──┐  ┌───▼─────┐
    │         PHASE 2: SYNTHETIC REPORTS          │  │ Gap 4:  │
    │    (3–5 targeted literature synthesises)    │  │ Regional│
    │                                             │  │ & Case  │
    └─────────────────────────────────────────────┘  │ Evidence│
              │                                       └───┬─────┘
              │                                           │
        ┌─────▼──────────────────────────────────────────┘
        │
    ┌───▼──────────────────────────────────────────────────────────┐
    │             PHASE 3: INTEGRATION & SYNTHESIS                 │
    │  (Consistent framing, hierarchical literature structure)     │
    └───┬──────────────────────────────────────────────────────────┘
        │
        │         ┌─────────────────────────────────────────┐
        │         │ OUTPUT: Annotated BibTeX w/ gap labels  │
        │         │ + Synthesis memos for each gap          │
        │         │ + Integration logic map                 │
        └─────────▼─────────────────────────────────────────┘
```

---

## Phase 1: Audit & Gap Identification

### 1.1 Initial Upload & Inventory Prompt

**File naming convention:** `LASTNAME_ETAL_YEAR.md` or `LASTNAME_YEAR.md` for single-author works. Example: `Aruguete_etal_2024.md`, `Toro_etal_2022.md`, `Kangaslahti_etal_2026.md`

**Upload to NotebookLM** all 120 references organized by category:

- `tier1_political_communication/` (Political Communication, New Media & Society, ICS, etc.)
- `tier1_methods/` (Political Analysis, JCMC)
- `tier2_latam/` (Latin American Politics and Society, IJoC, JITP with Chile/LatAm papers)
- `tier2_advertising/` (International Journal of Press/Politics, Social Media + Society)
- `tier2_general/` (remaining tier-2 outputs)

---

### 1.2 First Prompt: Comprehensive Gap Audit

**Prompt to NotebookLM:**

```
Based on the collection of ~120 communication and political science papers 
from 2020–2025 (focusing on Tiers 1–2 venues), execute the following audit:

1. COVERAGE INVENTORY:
   - How many papers explicitly use LDA or topic modeling on political texts?
   - How many study political advertising (paid or organic)?
   - How many focus on Latin America or Chile specifically?
   - How many combine ANY TWO of: (LDA) + (ads) + (Latin America)?
   - How many combine all THREE?

2. METHODOLOGICAL COVERAGE:
   - Which LDA variants are represented? (Vanilla LDA, STM, neural variants, etc.)
   - What alternatives to LDA are documented? (BERT, supervised, dictionary-based?)
   - What are the documented *limitations* of LDA in the corpus?
   - Are there papers explicitly comparing LDA to alternatives for political text?

3. THEORETICAL FRAMEWORKS:
   - How many papers ground political advertising in issue-ownership theory?
   - How many cite agenda-setting, framing, or priming?
   - How many engage with "digitalization of politics" as a theoretical frame?
   - How many theorize Latin American political communication distinctively?
   - Are there papers on populism, polarization, or affective politics via ads?

4. EMPIRICAL SCOPE:
   - Which electoral cycles or countries are studied?
   - Which platforms dominate (Facebook, Twitter, ads, organic)?
   - What sample sizes and temporal ranges are standard?
   - Are there studies of two-round elections or non-presidential cycles?

5. REGIONAL REPRESENTATION:
   - How many papers are LatAm-authored or LatAm-focused?
   - Which LatAm countries appear? (Brazil, Argentina, Chile, Colombia, etc.)
   - Is Chile represented? In what electoral context?
   - Are there comparative LatAm papers?

6. SYNTHESIS OUTPUT:
   Present a gap matrix: rows = [LDA, Political Ads, LatAm, Theory, Empirical Design],
   columns = [Well-filled, Partially filled, Unfilled]. For each unfilled or 
   partially-filled cell, name 2–3 authors who *could* be extended.
```

**Expected output:** A ~1.5–2 page audit identifying:

- ✓ What the corpus already covers well
- ⚠ What is partial or understudied
- ✗ What is completely absent

---

## Phase 2: Gap-Specific Literature Synthesis

### 2.1 Define Your Four Primary Gaps

Based on the literature audit and your project profile, you will likely identify these four gaps:

#### **Gap 1: Political Advertising Theory — Digitally Native**

_What the literature lacks:_ A cohesive framework explaining how **paid digital advertising** (vs. organic posts) functions as a political communication strategy, distinct from traditional media advertising or social media engagement. Most literature conflates organic posts with paid ads.

**Why it matters:** Your paper analyzes paid ads. You need to justify why they merit separate scholarly attention and what theoretical mechanisms they activate.

**Closing strategy:** Synthesize papers on microtargeting, data-driven campaigning, platform affordances, and issue-ownership—but only those that explicitly discuss _advertising_ as a paid, targeted object.

---

#### **Gap 2: LDA Methodological Validation & Interpretation**

_What the literature lacks:_ Published guidance on validating and interpreting LDA results on _Spanish-language political advertising_ specifically. Most LDA validation work covers English news, manifestos, or legislative speech. Few papers validate LDA against human coders on ads. Almost none address Spanish interpretive stability.

**Why it matters:** You need to defend LDA as a credible tool for this corpus and explain how you validate topic interpretability.

**Closing strategy:** Synthesize methodological papers (Political Analysis, methodological reviews) on LDA validation, Bayesian coherence, held-out likelihood, and manual-coder agreement; then synthesize papers on Spanish-language NLP to bridge the gap.

---

#### **Gap 3: Digitalization of Politics as a Global Transformation**

_What the literature lacks:_ A coherent theoretical narrative linking platform-driven digital campaigning in Chile to broader _global_ shifts in political communication. Most Chilean work is case-study bounded; most "globalization" work ignores Latin America.

**Why it matters:** Your paper frames Chilean ads as a case study of global digitalization. You need literature that demonstrates this is a meaningful theoretical move, not just geographically opportunistic.

**Closing strategy:** Synthesize papers on platform globalization, comparative digital politics (with non-Western cases), and Latin American political modernization; then connect them explicitly.

---

#### **Gap 4: The Empirical Distinctiveness of Chilean Presidential Elections**

_What the literature lacks:_ Documentation of what makes the 2021 and/or 2025 Chilean presidential races distinctive as sites of digital campaigning relative to other recent LatAm elections, and relative to the global pattern.

**Why it matters:** Your case is not random. You need to motivate why Chile, why these cycles, why paid ads matter there _in particular._

**Closing strategy:** Synthesize papers on Chilean party system collapse (post-2019), platform regulation, media-digital landscape, and electoral competitiveness. Contrast with Brazil 2018, 2022; Argentina 2019, 2023; Colombia 2022; etc.

---

### 2.2 Gap-Specific Synthesis Prompts

#### **Gap 1: Political Advertising Theory — Paid Digital Native**

**Prompt to NotebookLM:**

```
From the corpus, extract and synthesize papers on PAID DIGITAL POLITICAL 
ADVERTISING (not organic posts, not traditional ads, not news coverage).

SYNTHESIS REQUEST:

1. CORE MECHANISM PAPERS:
   - Which papers theorize microtargeting as a political tool?
   - Which explain data-driven voter targeting?
   - Which discuss advertiser goals, audience segmentation, or persuasion on digital platforms?
   - What *assumptions* about audience responsiveness do they make?

2. DISTINGUISHING PAID FROM ORGANIC:
   - Are there papers that explicitly contrast paid ads to organic posts in terms of 
     reach, targeting, message control, or effects?
   - Do any papers theorize why platforms *enable* advertising as distinct from feed posts?
   - Which papers engage the Facebook Ad Library or Google Ad Transparency work?

3. ISSUE-OWNERSHIP & AGENDA-SETTING IN THE DIGITAL CONTEXT:
   - How do issue-ownership and agenda-setting theories adapt when advertisers 
     (not journalists) control message distribution?
   - Are there papers showing ads successfully shift voter issue salience?
   - Do papers distinguish between ads that *reinforce* existing agendas vs. 
     those that *challenge* them?

4. PLATFORM AFFORDANCES:
   - Which papers analyze how Meta (Facebook/Instagram), Google, or TikTok's 
     targeting affordances reshape political strategy?
   - Do they theorize the shift from broad-reach messaging to microtargeted niches?

5. SYNTHESIS OUTPUT:
   Create a 1-page "Political Advertising in Digital Context: Theoretical Synthesis" 
   memo that defines:
   - Core mechanism (what are paid ads doing theoretically that organic posts are not?)
   - Key theories (issue-ownership? framing? microtargeting-driven polarization?)
   - Gaps (what do we NOT yet understand about paid ads' political effects?)
   - Citeable sentence: "Few studies have directly analyzed [X] in the context of 
     [Y], leaving open whether [Z]."
```

---

#### **Gap 2: LDA Methodological Validation & Interpretation**

**Prompt to NotebookLM:**

```
From the corpus, extract METHODOLOGICAL papers on topic modeling, LDA validation, 
and Spanish-language NLP for political text.

SYNTHESIS REQUEST:

1. LDA VALIDATION STRATEGIES:
   - How do papers validate LDA topic interpretability? 
     (List: held-out likelihood, perplexity, coherence score, manual coder agreement, 
     domain-expert rating, other?)
   - What are the trade-offs between automated metrics and human validation?
   - How many topics are standard for political speech/ads? (Range of K across papers?)

2. SPANISH-LANGUAGE SPECIFICS:
   - Are there papers applying LDA or topic modeling to Spanish political texts?
   - Do they discuss Spanish-specific challenges (diminutives, clitics, morphology)?
   - What preprocessing (stemming, lemmatization) is recommended?
   - Are multilingual embeddings cited as relevant infrastructure?

3. POLITICAL TEXT DISTINCTIVENESS:
   - Do papers acknowledge that political ads are different from news, manifestos, 
     or legislative speech as an LDA target?
   - Are there studies validating LDA on short texts (ads are often brief)?
   - How do papers handle repetition in political messaging?

4. COMPARISON TO ALTERNATIVES:
   - For political texts, how does LDA compare to (a) Structural Topic Models, 
     (b) BERT-based topic classification, (c) supervised classifiers?
   - When is LDA preferable to alternatives? When is it not?
   - Are there papers arguing for LDA's *interpretability* advantage despite 
     lower predictive power?

5. SYNTHESIS OUTPUT:
   Create a 1.5-page "LDA for Spanish-Language Political Advertising: 
   Methodological Foundations" memo that:
   - Justifies LDA as a tool for your corpus (why LDA? why not alternatives?)
   - Outlines a validation strategy (what metrics + manual checks will you use?)
   - Specifies likely K (topic range) based on corpus size and prior work
   - Names 3–5 explicit methodological precedents you will cite
   - Flags any Spanish-language or short-text specific limitations to address
```

---

#### **Gap 3: Digitalization of Politics — Global Frame**

**Prompt to NotebookLM:**

```
From the corpus, extract papers on GLOBAL PATTERNS in digital political 
communication and platform politics, with special attention to NON-WESTERN cases.

SYNTHESIS REQUEST:

1. GLOBALIZATION NARRATIVES:
   - How do papers frame the "digitalization of politics"? 
     (Decentralization? Platformization? Datafication? Other?)
   - Are there papers arguing this is a *global* transformation, not just U.S./EU?
   - Which papers cite non-Western cases (LatAm, Asia, Africa) as evidence?

2. COMPARATIVE DIGITAL POLITICS:
   - Which papers compare digital campaigning across continents or regime types?
   - Do they show platform logic flows are similar, or distinctively shaped by 
     local political systems?
   - Are there papers on Latin American platform politics specifically?
   - How do they theorize LatAm-specific factors (colonial digital economy, 
     regulatory gaps, inequality in digital access)?

3. PLATFORM POWER DYNAMICS:
   - How do papers theorize the role of Meta, Google, TikTok as *political actors* 
     vs. passive channels?
   - Is there literature on platform regulation or resistance in LatAm?
   - Do papers discuss how platforms' global policies (e.g., ad-targeting limits) 
     filter down to LatAm elections?

4. CYCLES & SEQUENCES:
   - Are there papers showing a *global sequence* of digital adoption in elections? 
     (E.g., U.S. 2008 → 2016 → Brazil 2018 → etc.?)
   - Do any map when Chile digitalized relative to neighbors?

5. SYNTHESIS OUTPUT:
   Create a 1-page "Digitalization of Politics: A Global Frame with Latin American 
   Specificity" memo that:
   - Articulates a coherent definition of digitalization (platform-driven? 
     data-centric? fragmented?)
   - Shows Chile 2021/2025 is a meaningful *instance* of a global process, 
     not an outlier
   - Identifies 4–5 key citations showing comparative evidence
   - Flags distinctive LatAm features (regulatory, economic, social) that shape 
     how digitalization manifests there
```

---

#### **Gap 4: Chilean Case — Political & Electoral Distinctiveness**

**Prompt to NotebookLM:**

```
From the corpus, extract papers on CHILEAN POLITICS, elections, and digital 
communication; also extract comparative papers on recent LatAm presidential cycles.

SYNTHESIS REQUEST:

1. CHILEAN POLITICAL CONTEXT (2019–2025):
   - What happened in Chile's 2019 social uprising and how did it reshape politics?
   - How did the party system fracture post-2019? 
   - What role did digital media play in the 2019 uprising and subsequent elections?
   - Who are the key new political actors (Boric, Kast, Sichel, Republicanos)?

2. CHILEAN ELECTIONS 2021 & 2025:
   - What characterized the 2021 presidential election? (Two-round? Party fragmentation?)
   - Is there literature on 2025 yet, or is it only emerging?
   - Were these elections distinctively *digital*? Evidence?
   - How much did candidates spend on ads? Which platforms? Any data?

3. COMPARATIVE LatAm CONTEXT:
   - How do Chilean 2021/2025 compare to Argentina 2019/2023, Brazil 2022, 
     Colombia 2022 in terms of digital campaigning?
   - Is Chile a "late adopter," mainstream, or innovator in LatAm digital politics?
   - What unique affordances or constraints does Chile have? 
     (Internet access? Platform availability? Regulation? Media landscape?)

4. MEDIA & PLATFORM LANDSCAPE:
   - What is Chile's media ownership concentration?
   - What % of voters are on Facebook, Instagram, Twitter/X, TikTok?
   - Has Chile regulated political advertising on platforms? How?
   - Do campaigns have different strategies on different platforms?

5. SYNTHESIS OUTPUT:
   Create a 1.5-page "Why Chile, Why 2021–2025, Why This Matters" memo that:
   - Briefly narrates the Chilean political context (party collapse, key actors)
   - Cites evidence that 2021/2025 were pivotal digital-campaigning moments
   - Shows how Chile compares regionally (similar to X, distinct from Y)
   - Justifies the sample (paid ads on Meta, 2021 1V/2V, 2025 1V if available)
   - Anticipates reader objection: "Why not just study the U.S. or Europe?" 
     (Answer: Chile is a critical case for understanding digital politics 
     beyond the Global North)
```

---

## Phase 3: Integration & Consistency Checking

### 3.1 Synthesis Aggregation Prompt

Once you have the four gap memos, synthesize them into a coherent frame:

**Prompt to NotebookLM:**

```
I have four gap-specific literature syntheses:
1. Political Advertising in Digital Context (Gap 1)
2. LDA Methodological Foundations (Gap 2)
3. Digitalization of Politics: Global Frame (Gap 3)
4. Why Chile Matters (Gap 4)

REQUEST:

1. LOGICAL INTEGRATION:
   - In what order should these gaps be addressed in the paper's introduction 
     and literature review?
   - Are there contradictions between them? (E.g., does Gap 1 assume something 
     Gap 3 questions?)
   - Where do they *reinforce* each other?

2. CITATION COHERENCE:
   - How many *unique* papers are cited across all four syntheses?
   - Are there "hub" papers that bridge multiple gaps? Name them.
   - Are there redundant citations that could be consolidated?
   - Are there gaps within gaps (e.g., "Gap 1 requires Paper X which you haven't cited")?

3. THEORETICAL THROUGH-LINE:
   - What is the *single* most powerful claim that ties all four together?
   - In one sentence, what does the reader understand by the end of the lit review?
   - Example: "We study how global platform architectures enabling microtargeted 
     political advertising reshape electoral competition in Latin America, 
     analyzing Chile's 2021–2025 elections via topic-modeled ad content."

4. OUTPUT:
   - Produce a 2-page "Literature Integration Memo" that outlines:
     * Recommended lit-review structure (intro → theory → method → region → case)
     * Hub citations (papers cited 2+ times across gaps)
     * The single theoretical through-line
     * Remaining weaknesses (e.g., "Literature is still thin on X, but Y 
       provides partial evidence")
```

---

### 3.2 Consistency Check: Evidence Alignment

**Final audit prompt to NotebookLM:**

```
I am writing a paper that:
- Uses LDA topic modeling on paid digital political ads
- Case study: Chilean presidential elections (2021, 2025)
- Frames the contribution as understanding digitalization of politics globally

REQUEST:

1. CLAIM VERIFICATION:
   For each of these claims, what is the strength of evidence in the corpus?
   - Claim A: "Paid digital ads are a distinct object of political communication 
     worthy of study" — EVIDENCE STRENGTH: [Strong/Moderate/Weak]
   - Claim B: "LDA is a validated method for analyzing Spanish-language political 
     advertising" — EVIDENCE STRENGTH: [Strong/Moderate/Weak]
   - Claim C: "Chile's 2021–2025 elections represent a critical case of global 
     digitalization" — EVIDENCE STRENGTH: [Strong/Moderate/Weak]
   - Claim D: "Topic modeling of ads reveals substantively distinct campaign 
     strategies across candidates" — EVIDENCE STRENGTH: [Strong/Moderate/Weak]

2. FOR EACH WEAK/MODERATE CLAIM:
   - What evidence *exists* in the corpus?
   - What would strengthen the evidence? (E.g., "need more LatAm case studies")
   - How should I frame a moderate-evidence claim rhetorically? 
     (E.g., as "emerging evidence" vs. "established finding"?)

3. RED FLAGS:
   - Is there any paper in the corpus that *contradicts* your main claims?
   - If so, how do you respond to that contradiction?

4. OUTPUT:
   Produce a "Claims Audit Table" with columns:
   [Claim | Evidence Strength | Key Supportive Papers | 
   Counterarguments | Rhetorical Framing]
```

---

## Phase 4: NotebookLM Prompts — By Category

### A. Literature Inventory & Mapping

|**Prompt**|**Purpose**|**Output**|
|---|---|---|
|"Map all papers by methodology: which use LDA/topic modeling, which use supervised classifiers, which use dictionaries, which use manual coding? Count each."|Methodology landscape|Table: methodology × count × example papers|
|"List all papers that study political ads specifically (paid or organic). For each, note: (a) platform, (b) country, (c) electoral context, (d) sample size."|Ad literature catalog|Structured list with metadata|
|"Which papers cite other papers in this corpus? Who are the most-cited within-corpus authors?"|Citation structure & influence|Citation network + hub authors|

### B. Theory & Framing

|**Prompt**|**Purpose**|**Output**|
|---|---|---|
|"Extract and compare how papers define 'digitalization of politics.' What are the core mechanisms (platform logic? data-driven targeting? algorithmic curation? other)? What is common vs. contested?"|Conceptual alignment|Definition table with source variation|
|"For political advertising, extract all cited theories: issue-ownership, framing, agenda-setting, microtargeting, polarization, populism, other. Which theories are dominant in recent work (2023–2025)?"|Theoretical landscape|Theory × citation count × recent trend|
|"Papers discussing Latin America: do they treat it as (a) a distinct region with distinctive politics, or (b) a lagging instance of a global North pattern? What evidence supports each view?"|Regional framing|Exemplar quotes + characterization|

### C. Methods & Validation

|**Prompt**|**Purpose**|**Output**|
|---|---|---|
|"For the three papers using LDA on political text (or closest analogues): what K (number of topics) did they choose? How did they validate topic coherence? Did they compare to human coders?"|LDA calibration|Table: Paper × K × coherence metric × validation strategy|
|"Extract all mentions of 'validation,' 'interpretability,' 'validation against human coders,' or 'topic coherence' in method-focused papers. What is the standard practice for LDA in political communication?"|Validation norms|Annotated extraction with frequency|
|"Which papers discuss Spanish-language NLP, multilingual embeddings, or language-specific text preprocessing? List all and note what preprocessing decisions they report."|Spanish-language NLP|Reference list with preprocessing notes|

### D. Evidence & Empirics

|**Prompt**|**Purpose**|**Output**|
|---|---|---|
|"For all papers studying two-round or two-stage elections (like Chile's 2021 1V + 2V), what did they find about campaign messaging _change_ between rounds? Evidence for strategic adaptation?"|Election cycle dynamics|Summary of findings on round effects|
|"Papers on candidate differentiation via messaging: do they find distinct topic distributions across candidates, or do all candidates converge? Cite specific findings."|Candidate strategy divergence|Exemplar findings with citations|
|"Extract all data on political ad spend in recent LatAm elections (Argentina, Brazil, Colombia, Chile). What was the size of digital ad markets? What % of total campaign spend?"|Digital ad market context|Data table: country × year × spend estimate|

### E. Comparative & Regional Analysis

|**Prompt**|**Purpose**|**Output**|
|---|---|---|
|"Compare digital campaigning across Brazil 2022, Argentina 2023, Colombia 2022, Chile 2021, Chile 2025 (if available). What patterns emerge? Which countries adopted digital strategies earliest? Which are most sophisticated?"|LatAm comparative trend|Timeline + characterization of maturity|
|"Papers on platform regulation of political advertising (globally and in LatAm): what constraints do Meta, Google, TikTok impose? How do LatAm countries regulate differently from U.S./EU?"|Platform governance context|Regulation matrix: platform × jurisdiction × constraint|
|"Chilean papers specifically: map them by author, journal, year, and topic. Are there research clusters? Who are the leading Chilean digital-politics researchers? What are their Q1 papers?"|Chilean research ecosystem|Author map + citation patterns + gaps|

---

## Phase 5: Output & Artifact Organization

### 5.1 Deliverables from Each Phase

**After Phase 1 (Audit):**

- Gap Audit Matrix (table identifying well-filled, partial, unfilled cells)
- Inventory spreadsheet (all 120 papers with metadata: year, journal, method, region, theory)

**After Phase 2 (Gap-Specific Synthesis):**

- Four memos (1–1.5 pages each):
    
    1. Political Advertising in Digital Context
    2. LDA Methodological Foundations
    3. Digitalization of Politics: Global Frame
    4. Why Chile Matters
    
    _Each memo includes:_
    - Synthesis narrative (what does the literature say?)
    - Key citations (5–10 essential papers)
    - Gap statement ("Literature does not yet address…")
    - Implication for your paper ("Therefore, this study will…")

**After Phase 3 (Integration):**

- Literature Integration Memo (2 pages)
    - Recommended structure for lit review
    - Hub papers (most valuable for multiple gaps)
    - Theoretical through-line (one sentence)
    - Remaining weaknesses and responses

**After Phase 4 (Claims Audit):**

- Claims Audit Table
    - Each claim with evidence strength
    - Supportive papers and counterarguments
    - Framing guidance (e.g., "emergent evidence" vs. "established")

**Final artifact:**

- **Annotated BibTeX with gap labels** (.bib file where each entry has custom field `gap={Gap1, Gap3}` or similar, indicating which gaps it bridges)
- **Literature review outline** (hierarchical, cross-referenced to gaps and hub papers)

---

### 5.2 NotebookLM Workspace Organization

Structure your NotebookLM workspace as follows:

```
📁 NotebookLM Workspace: Chilean Digital Ads LDA Paper

  📂 SOURCE DOCUMENTS (upload here)
     📂 Tier1_Communication
        ├─ Aruguete_etal_2024.md
        ├─ Kangaslahti_etal_2026.md
        ├─ Unlu_etal_2025.md
        └─ [~30 more]
     
     📂 Tier1_Methods
        ├─ Wirsching_etal_2025.md
        ├─ Wang_2024.md
        └─ [~8 more]
     
     📂 Tier2_LatAm
        ├─ Argote_Visconti_2025.md
        ├─ Mellado_etal_2024.md
        ├─ Aruguete_etal_2024_Mayors.md (Chilean)
        └─ [~25 more]
     
     📂 Tier2_Advertising
        ├─ Vrielink_etal_2025.md
        ├─ Pallister_Fitzpatrick_2024.md
        ├─ Toro_etal_2022.md (Chilean)
        └─ [~20 more]

  📂 NOTEBOOK SESSIONS (your NotebookLM query outputs)
     📂 Phase1_Audit
        ├─ Gap_Audit_Matrix.md
        ├─ Inventory_Spreadsheet.csv
        └─ First_Comprehensive_Audit.md
     
     📂 Phase2_GapSpecific
        ├─ Gap1_Political_Ads_Theory.md
        ├─ Gap2_LDA_Methods.md
        ├─ Gap3_Digitalization_Global.md
        └─ Gap4_Why_Chile.md
     
     📂 Phase3_Integration
        ├─ Literature_Integration_Memo.md
        ├─ Claims_Audit_Table.md
        └─ Remaining_Weaknesses.md

  📂 SYNTHESIS OUTPUTS (what you create from NB outputs)
     ├─ Annotated_Bibliography.bib
     ├─ Lit_Review_Outline.md
     └─ Evidence_Strength_Summary.md
```

---

## Phase 6: Strategic Note-Taking Within NotebookLM

### 6.1 Systematic Query Strategy

**Session 1: Establish Baseline (30–45 min)**

- Upload all sources to one NotebookLM notebook
- Run Gap Audit Comprehensive prompt
- Download output as markdown; save as `Phase1_Audit.md`

**Session 2a–2d: Gap-Specific Synthesis (45 min each, 4 sessions)**

- Create four separate NotebookLM notebooks (or one multi-session)
- For each gap, run the gap-specific synthesis prompt
- Download each as `Gap{N}_Memo.md`
- Annotate with your own reactions in margin (use `<!-- comments -->`)

**Session 3: Integration (60 min)**

- Create a new notebook with the four gap memos as source documents
- Run the integration prompt
- Download as `Literature_Integration_Memo.md`

**Session 4: Consistency Check (30 min)**

- Run the Claims Audit prompt
- Download as `Claims_Audit_Table.md`

---

### 6.2 Annotation & Follow-Up Strategy

For each memo from NotebookLM, immediately:

1. **Tag key citations** with gap labels:
    
    ```
    [Gap 1] Vrielink et al. (2025) on ad targeting effects
    [Gap 1 + Gap 2] Aruguete et al. (2024) on STM validation in political context
    [Gap 3 + Gap 4] Pallister & Fitzpatrick (2024) on LatAm campaign messaging
    ```
    
2. **Flag actionable insights:**
    
    ```
    *** ACTIONABLE: Consider adopting Kangaslahti et al.'s Tensor LDA for 
        scale rather than vanilla LDA ***
    
    ??? UNCLEAR: NotebookLM says LDA is validated for political ads, but 
        cites mostly news/manifestos. Follow up with manual coder check.
    
    ⚠️  COUNTERARGUMENT: Larsson et al. (NMS 2025) argues topic modeling 
        misses visual affordances in social-media ads. Respond in methods section.
    ```
    
3. **Create follow-up prompts:**
    
    ```
    If Gap 2 memo says "No Spanish-language LDA validation exists," 
    → Ask: "What Spanish-language NLP papers *do* exist? Can I infer 
      validation strategy from them?"
    
    If Gap 3 mentions "sparse LatAm in digitalization literature," 
    → Ask: "Which non-Western regions are well-studied? Can I cite 
      Southeast Asia or Sub-Saharan Africa as analogues to LatAm?"
    ```
    

---

## Phase 7: Building the Final Literature Review

### 7.1 Structural Template

Use the integration memo's recommended structure:

```markdown
# Literature Review

## 1. Political Advertising in the Digital Age
[~1.5 pages: define paid digital ads as distinct object, cite Gap 1 papers]

## 2. Topic Modeling as a Methodological Tool
[~1 page: LDA fundamentals, validation, Spanish-language considerations, cite Gap 2]

## 3. Digitalization of Politics: A Global Phenomenon
[~1.5 pages: digitalization as theory, platform politics, non-Western cases, cite Gap 3]

## 4. The Chilean Case: Political Fragmentation & Digital Strategy
[~1 page: Chilean context, 2021/2025 elections, platform landscape, cite Gap 4]

## 5. Research Gap & Contribution
[~0.5 pages: "This study combines LDA + ads + Chile to examine 
how platform-driven political communication reshapes electoral competition 
in post-crisis democracies."]
```

### 7.2 Cross-Gap Citation Strategy

In each section, cite hub papers that bridge gaps:

- **Hub between Gaps 1–2:** Aruguete et al. (2024) — validates STM on Chilean political social media
- **Hub between Gaps 2–3:** Kangaslahti et al. (2026) — scales LDA to large political corpora globally
- **Hub between Gaps 3–4:** Pallister & Fitzpatrick (2024) — LatAm presidential campaign messaging
- **Hub between all:** Orchard & González-Bustamante (2024) — Chilean political elites + computational analysis

---

## Phase 8: Quality Checklist

Before submitting, verify:

### Theoretical Coherence

- [ ] Does Gap 1 (ads theory) logically precede Gap 2 (method)?
- [ ] Does Gap 3 (global frame) justify choosing Chile (Gap 4)?
- [ ] Is there a single unifying claim tying all four?

### Evidence Strength

- [ ] No claim rated "Weak" in the Claims Audit Table is presented as established
- [ ] Moderate claims are framed with hedging language ("emerging evidence," "recent work suggests")
- [ ] Counterarguments are acknowledged, not buried

### Citation Integrity

- [ ] Every factual claim has a source
- [ ] Hub papers are cited in multiple sections (showing their bridging role)
- [ ] No over-reliance on a single author or journal

### Coverage Completeness

- [ ] Are all four gaps visibly addressed in the lit review?
- [ ] Are the Chilean specifics (context, elections, platform landscape) grounded in cited evidence?
- [ ] Is the methodological choice (LDA) defended against alternatives?

### Freshness

- [ ] Are you citing recent work (2024–2026 papers)? Do they appear in your lit review?
- [ ] Are you engaging with emerging debates (e.g., AI-generated ads, platform regulation)?

---

## Quick-Reference: NotebookLM Prompt Templates

### Template A: Coverage Inventory

```
From the 120 papers in [FOLDER], how many papers:
- Use LDA or topic modeling?
- Study political advertising (paid or organic)?
- Focus on Latin America or Chile?
- Combine any two of [LDA + ads + LatAm]?
- Combine all three?

Provide counts, example papers, and gaps.
```

### Template B: Theory Extraction

```
From papers on [TOPIC], extract:
- What theories do they cite? (List all distinct theories)
- Which theories appear in 2+ papers?
- How do they define [KEY CONCEPT, e.g., "digitalization"]?
- Are there definitional disagreements?

Output: Theory inventory table with frequency + definitions.
```

### Template C: Methods Comparison

```
Papers using [METHOD, e.g., LDA] on [DOMAIN, e.g., political ads]:
- Which validation strategies did they use?
- What sample sizes and topic numbers (K)?
- What software (R? Python? Package name)?
- What preprocessing decisions?

Output: Methods table with columns for each decision point.
```

### Template D: Empirical Pattern

```
Papers studying [CONTEXT, e.g., LatAm presidential elections]:
- Which countries and cycles?
- What platforms?
- What sample sizes?
- What were key findings?

Output: Empirical summary table showing coverage & findings.
```

---

## Timeline Estimate

|Phase|Task|Time|Output|
|---|---|---|---|
|1|Gap Audit|1 session (30 min)|Gap Audit Matrix|
|2a|Gap 1 (Ads)|1 session (45 min)|Gap 1 Memo|
|2b|Gap 2 (Method)|1 session (45 min)|Gap 2 Memo|
|2c|Gap 3 (Global)|1 session (45 min)|Gap 3 Memo|
|2d|Gap 4 (Chile)|1 session (45 min)|Gap 4 Memo|
|3|Integration|1 session (60 min)|Integration Memo|
|4|Claims Audit|1 session (30 min)|Claims Table|
|5|Synthesis & Writing|2–3 hours|Final Lit Review|
|**Total**||**~6–7 hours**|**Complete literature foundation**|

---

## Success Criteria

At the end of this process, you should have:

1. ✅ **A defensible literature review** (1500–2000 words) that addresses four concrete gaps
2. ✅ **Annotated bibliography** with gap labels (in BibTeX or Markdown)
3. ✅ **Explicit evidence map** (Claims Audit Table) showing which claims are strongly vs. moderately supported
4. ✅ **Hub papers identified** (5–8 papers that bridge multiple gaps and deserve prominent citation)
5. ✅ **Narrative coherence** (one unifying theoretical claim that ties all four gaps)
6. ✅ **Confidence in submission strategy** (you can explain to reviewers why Political Communication, IJPP, or JITP is the right venue for this work)

---

## Next Steps After NotebookLM

Once you have completed all four gap memos and the integration memo:

1. **Sketch the lit review outline** using the structure template (Phase 7.1)
2. **Write the first draft** of the literature review, using memos as source material
3. **Cite strategically** — use hub papers to connect gaps, not just linearly
4. **Address counterarguments** — flag papers (like Larsson et al. 2025) that complicate your claims
5. **Test the through-line** — can a reader follow a single argument from intro to conclusion?
6. **Submit** to Political Communication, IJPP, or JITP with confidence in your reference foundation

---

## Appendix: Sample NotebookLM Workspace Setup

When you upload your 120 papers, organize them by creating a single master notebook with the folder structure above. Then, for each phase, you can either:

- **Option A:** Create a new NotebookLM notebook for each phase (Audit, Gap1, Gap2, Gap3, Gap4, Integration, Claims)
- **Option B:** Use a single multi-session notebook and label each query clearly (e.g., "PHASE 1: Gap Audit," "PHASE 2a: Gap 1 Synthesis," etc.)

Option A is cleaner for organization; Option B is faster if you want to keep all outputs in one place.

---

_This strategy is designed to be iterative. After each phase, review outputs with your supervisor or a trusted colleague. If a gap remains unfilled, you can run follow-up queries rather than starting over._