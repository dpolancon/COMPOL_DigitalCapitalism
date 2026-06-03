### Missing Structural Components (In Order)

**Core paper sections:**

1. **Abstract** — summary of findings + contribution claim
2. **Introduction** — research question, motivation, why it matters for strategic communication / political economy
3. **Results section** — organized by your subsetting hierarchy, _with narrative framing_
4. **Robustness & Sensitivity** — K-testing, topic matching thresholds, subsegment stability
5. **Discussion/Implications** — what the microtargeting patterns _mean_ (strategic communication theory, political economy reading)
6. **Conclusion** — synthesis, limitations, future work
7. **References** — full bibliography

**Appendical/supporting material:**

- Extended tables (full REI matrices at joint segment level)
- Topic word lists by K and subset
- Sensitivity tables showing how REI/TTD/TGC change with K
- Code documentation + repo structure
- Data access statement

---

### On the K-Sensitivity Question

You're analytically sound here. Your framework already handles this correctly:

- **REI, TTD, TGC are robust to K**: They're computed _within_ a single model fit. A different K changes which ads cluster together, yes—but the three indices measure _what the model found_, not an absolute truth. The substantive claim is: "within each K, here's what targeting looks like."
- **The probability analysis you mention**: The posterior θ^a,k\hat{\theta}_{a,k} θ^a,k​ (document-topic mixture) and ϕ^k,v\hat{\phi}_{k,v} ϕ^​k,v​ (topic-word distribution) *will* shift with K. Higher K means finer-grained topic separation, so the same ad might be assigned to a narrower topic. This can affect:
    - Which topic an ad's MAP assignment chooses: ta=arg⁡max⁡kθ^a,kt_a = \arg\max_k \hat{\theta}_{a,k} ta​=argmaxk​θ^a,k​
    - The magnitude of the conditional demographic profiles: Pˉs∣k\bar{P}_{s|k} Pˉs∣k​
- **Solution**: Run K ∈ {5, 7, 10, 12} for each subset, report your main results at your chosen K (probably 7–10), and show in Appendix that the REI _rankings_ (which topics are most targeted) are stable across K. TTD and TGC should also be orderly stable—you might find a few topics flip positions, but the typology (high TTD/high TGC, etc.) should hold.

---

### Results Package Architecture

Based on your analytical framework, here's the **minimal reproducible results set**:

```
results/
├── 01_topic_summaries/
│   ├── boric_v1_topics.csv        # Topic Label, N_k, TTD_k, TGC_k, argmax REI
│   ├── boric_v2_topics.csv
│   ├── kast_v1_topics.csv
│   ├── [... all candidate × round combos]
│   └── bloc_summaries.csv         # Left, Right, All aggregates
│
├── 02_rei_matrices/
│   ├── boric_v1_rei_age.csv       # Rows: age groups, Cols: topics ordered by TTD
│   ├── boric_v1_rei_gender.csv
│   ├── [... all combos, both margins]
│   └── [optional] joint_segments/ # 21×K full matrices for appendix
│
├── 03_cross_round_analysis/
│   ├── boric_topic_persistence.csv  # Round 1 topic → Round 2 matches, similarity scores
│   ├── kast_topic_persistence.csv
│   └── persistence_thresholds.md  # τ_high, τ_low, sensitivity checks
│
├── 04_robustness/
│   ├── k_sensitivity/
│   │   ├── boric_v1_K5_vs_K7_vs_K10_rei_ranking.csv
│   │   └── topic_stability_summary.md
│   └── subsegment_stability.csv   # REI across finer breakdowns (e.g., within 18-24)
│
└── 05_metadata/
    ├── lda_hyperparameters.txt    # α, β values per subset, iterations, convergence
    ├── vocabulary_stats.csv        # |V|, word removal rates, preprocessing effects
    └── data_manifest.txt           # Which CSV rows went into which subset
```

---

### Execution Order (Your Critical Path)

#### **Phase 1: Lock the analytical code (parallel with tidying)**

**Repo structure:**

```
thesis-to-paper/
├── data/
│   └── raw/
│       ├── boric.csv, kast.csv, ... [as-is from project]
│
├── code/
│   ├── 01_preprocessing.R          # Deterministic τ map, produce F_q matrices
│   ├── 02_lda_estimation.R         # Collapsed Gibbs, multiple K values
│   ├── 03_index_computation.R      # REI, TTD, TGC, panel construction
│   ├── 04_cross_round_matching.R   # Cosine similarity, topic correspondence
│   ├── 05_results_tables.R         # Export to CSV + formatted tables for paper
│   └── utils/
│       ├── lda_helpers.R           # Preprocessing, sampling, post-hoc labeling
│       └── index_helpers.R         # REI, TTD, TGC vectorized computation
│
├── results/
│   └── [as above]
│
├── paper/
│   ├── 01_abstract.md
│   ├── 02_introduction.md
│   ├── 03_litreview.md
│   ├── 04_framework.md
│   ├── 05_data.md
│   ├── 06_results.md              # [MAIN WORK]
│   ├── 07_robustness.md           # [MAIN WORK]
│   ├── 08_discussion.md
│   ├── 09_conclusion.md
│   └── 10_appendix.md
│
├── README.md                       # Reproducibility statement
└── _setup.R                        # Install packages, set paths
```

**Questions to lock now:**

- What KK K are you committing to for main results? (This determines which model fit feeds into discussion)
- Word removal thresholds (stop word list, min frequency, etc.)?
- Topic labeling: are you doing this with human review, or algorithmic labeling (e.g., top-3 words)?

---

#### **Phase 2: Generate and QA results tables**

Run:

R

```R
source("code/01_preprocessing.R")     # Produce F_q for all subsets
source("code/02_lda_estimation.R")   # Fit models, store all K options
source("code/03_index_computation.R") # Compute REI, TTD, TGC panels
source("code/04_cross_round_matching.R") # Topic correspondence
source("code/05_results_tables.R")   # Export results/
```

**QA checklist:**

- [ ]  Do REI values make sense directionally? (e.g., younger candidates' campaigns reaching younger audiences should show >1 in 18-24 cells)
- [ ]  TTD values in (0,1)? Any close to 0 (broadcast) or 1 (surgical)?
- [ ]  K-sensitivity: do REI _rankings_ within each topic stay consistent?
- [ ]  Topic persistence: do round-1 and round-2 top topics match qualitatively?

---

#### **Phase 3: Write results + discussion**

Once results are locked, the narrative is almost automatic. For each candidate/round/bloc:

**Pattern to write:**

> _"[Candidate] deployed K topics, of which [TTD_top3] showed highest targeting precision. The most targeted topic was [Label], concentrated in [TGC classification] reaching [argmax segment] at [REI magnitude]× baseline. Across candidates on the Left/Right, the pattern suggests [strategic hypothesis]."_

Your indices _enforce_ discipline here—you can't hand-wave.

---

### What Changes with K (Specific Guidance)

**If you move from K=7 to K=10:**

- Some 7-topic ads will "split" into two narrower 10-topics.
- The REI _magnitudes_ might shift (e.g., a 1.8 might become 1.6 + narrower audience).
- **Critical**: The _top 3–4 topics by TTD_ should persist. If they don't, it signals:
    - You're underfitting (K too low) and bundling distinct campaigns, OR
    - You're overfitting (K too high) and fragmenting coherent messaging.
- **Your paper's claim**: "We identify the demographic targeting structure of microtargeting campaigns. Across all K ∈ [5,12], the structural typology (high TTD/high TGC surgical targeting, etc.) holds; detailed results at K=7 in Appendix C."