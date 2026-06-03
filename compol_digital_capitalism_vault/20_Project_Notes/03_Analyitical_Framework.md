# Analytical Foundation




**Working Paper:** *Data-Driven Microtargeting in Political Communication: Evidence from the 2021 Chilean Presidential Election*  
**Document type:** Methodological memo — formal specification  
**Status:** Draft for circulation

---

## Notation Reference

| Symbol | Definition |
|--------|------------|
| $a$ | Individual Facebook ad, $a \in \mathcal{A}$ |
| $A_q$ | Number of ads in analysis subset $q$ |
| $K$ | Number of latent topics |
| $k$ | Topic index, $k \in \{1,\dots,K\}$ |
| $s$ | Demographic segment, $s \in \mathcal{S}$ |
| $g$ | Age group, $g \in \mathcal{G}$ |
| $r$ | Gender category, $r \in \mathcal{R}$ |
| $v$ | Election round, $v \in \{1,2\}$ |
| $c$ | Candidate, $c \in \mathcal{C}$ |
| $P_{a,s}$ | Observed demographic weight of segment $s$ in ad $a$ |
| $t_a$ | MAP topic assignment for ad $a$ |
| $N_k$ | Number of ads in subset $q$ assigned to topic $k$ |
| $\pi_k$ | Empirical topic weight (marginal frequency) |
| $\bar{P}_{s \mid k}$ | Mean demographic weight of segment $s$ conditional on topic $k$ |
| $\bar{P}_s$ | Baseline mean demographic weight of segment $s$ across all ads |

---

# Analytical Foundation

The paper studies whether political campaigns differentiate their message content across demographic segments through paid advertising on Facebook. The analytical task has two components. The first is **unsupervised content classification**: identifying the latent thematic structure of the ad corpus without imposing a priori categories. The second is **segmentation analysis**: measuring whether content, once classified, is directed differentially across demographic groups relative to a neutral baseline. The formal foundation for each component is specified below.

---

## LDA Formalization

### Corpus

Let $\mathcal{A}$ be the full corpus of Facebook ads collected from the Ad Library across all candidates and both election rounds. Each ad $a \in \mathcal{A}$ carries a text body $\mathbf{w}_a$ and a set of covariates: candidate identity $c_a \in \mathcal{C}$, round $v_a \in \{1,2\}$, and a demographic distribution over audience segments $\{P_{a,s}\}_{s \in \mathcal{S}}$.

Analysis is conducted over **analysis subsets** $\mathcal{A}_q \subseteq \mathcal{A}$, defined by restrictions on $(c_a, v_a)$. The set of subsets is:

$$\mathcal{Q} = \{(c, v) : c \in \mathcal{C} \cup \{\text{All}, \text{Left}, \text{Right}\},\; v \in \{1,2\}\} \setminus \emptyset$$

where Left $= \{\text{Boric, MEO, Yasna}\}$ and Right $= \{\text{Kast, Sichel}\}$.

### Preprocessing

Each document $a$ is transformed by a deterministic map $\tau$ that removes punctuation, numbers, symbols, URLs, stop words (Spanish), and candidate names, applies lowercasing, and removes non-ASCII characters. Let $\mathbf{f}_a \in \mathbb{Z}_{\geq 0}^V$ be the term-frequency vector of $\tau(\mathbf{w}_a)$ over vocabulary $\mathcal{V}$, $|\mathcal{V}| = V$. The document-feature matrix for subset $q$ is $\mathbf{F}_q = [\mathbf{f}_a]_{a \in \mathcal{A}_q} \in \mathbb{Z}_{\geq 0}^{A_q \times V}$.

### Generative Model

For each analysis subset $\mathcal{A}_q$, a Latent Dirichlet Allocation model with $K$ topics is specified. Let $\boldsymbol{\alpha} \in \mathbb{R}_{>0}^K$ and $\boldsymbol{\beta} \in \mathbb{R}_{>0}^V$ be symmetric Dirichlet hyperparameters. The generative process is:

**Topic-word distributions.** For each topic $k \in \{1,\dots,K\}$:

$$\boldsymbol{\phi}_k \sim \text{Dirichlet}(\boldsymbol{\beta}), \qquad \boldsymbol{\phi}_k \in \Delta^{V-1}$$

**Document-topic mixtures.** For each document $a \in \mathcal{A}_q$:

$$\boldsymbol{\theta}_a \sim \text{Dirichlet}(\boldsymbol{\alpha}), \qquad \boldsymbol{\theta}_a \in \Delta^{K-1}$$

**Token generation.** For each token position $j \in \{1,\dots,n_a\}$ in document $a$:

$$z_{a,j} \mid \boldsymbol{\theta}_a \sim \text{Categorical}(\boldsymbol{\theta}_a)$$

$$w_{a,j} \mid z_{a,j},\, \{\boldsymbol{\phi}_k\} \sim \text{Categorical}(\boldsymbol{\phi}_{z_{a,j}})$$

The joint likelihood over all tokens in $\mathcal{A}_q$ is:

$$p(\mathbf{W}_q \mid \boldsymbol{\alpha}, \boldsymbol{\beta}) = \prod_{a \in \mathcal{A}_q} \int_{\Delta^{K-1}} \left[ \prod_{j=1}^{n_a} \sum_{k=1}^{K} \theta_{a,k}\, \phi_{k,w_{a,j}} \right] p(\boldsymbol{\theta}_a \mid \boldsymbol{\alpha})\, d\boldsymbol{\theta}_a$$

Estimation proceeds by collapsed Gibbs sampling, integrating out $\boldsymbol{\Theta} = \{\boldsymbol{\theta}_a\}$ and $\boldsymbol{\Phi} = \{\boldsymbol{\phi}_k\}$ analytically. The sampler iterates over token-topic assignments $z_{a,j}$, yielding posterior point estimates:

$$\hat{\phi}_{k,v} = \frac{n_{k,v} + \beta}{\sum_{v'} n_{k,v'} + V\beta}, \qquad \hat{\theta}_{a,k} = \frac{n_{a,k} + \alpha}{\sum_{k'} n_{a,k'} + K\alpha}$$

where $n_{k,v}$ is the count of tokens assigned to topic $k$ with word type $v$, and $n_{a,k}$ is the count of tokens in document $a$ assigned to topic $k$.

### MAP Topic Assignment

Each document is assigned its maximum a posteriori topic:

$$t_a = \underset{k \in \{1,\dots,K\}}{\arg\max}\; \hat{\theta}_{a,k}$$

This collapses the soft mixture $\hat{\boldsymbol{\theta}}_a$ to a single discrete label per document, enabling the demographic segmentation analysis in subsequent sections.

### Topic Marginal Distribution

For subset $q$, the empirical topic weight is:

$$N_k = \sum_{a \in \mathcal{A}_q} \mathbf{1}[t_a = k], \qquad \pi_k = \frac{N_k}{A_q} \in [0,1], \qquad \sum_{k=1}^{K} \pi_k = 1$$

### Qualitative Labeling

Topics are labeled post hoc by human inspection of the top-$M$ words ranked by $\hat{\phi}_{k,v}$. Labels are assigned independently for each subset $q$. Because topic indices are exchangeable within each independently estimated model, labels carry no formal correspondence across subsets. Cross-subset comparison of topic content is conducted on the basis of word-distribution similarity, not index identity.

### Non-Identifiability

LDA is subject to two sources of non-identifiability. First, **label switching**: any permutation of topic indices yields an equivalent model, so topic indices are arbitrary. Second, **cross-subset incommensurability**: independently estimated models share no common parameterization. Both are handled by restricting inference to within-subset comparisons and grounding cross-subset claims in qualitative word-level evidence.

---

## Indices Implemented

All three indices are computed within a fixed analysis subset $q$ and with respect to a fixed, single model fit — that is, the same object $\{t_a\}_{a \in \mathcal{A}_q}$ is used for both topic labeling and index computation.

### Baseline Demographic Distribution

For any analysis subset $q$, define the **baseline mean audience weight** in segment $s$ as the average across all ads, irrespective of topic:

$$\bar{P}_s = \frac{1}{A_q} \sum_{a \in \mathcal{A}_q} P_{a,s}$$

This is the demographic profile a segment $s$ would receive if the campaign distributed its ad content without any topic-based differentiation. It serves as the reference distribution for all three indices.

The **conditional mean audience weight** in segment $s$ for topic $k$ is:

$$\bar{P}_{s \mid k} = \frac{1}{N_k} \sum_{a \in \mathcal{A}_q} \mathbf{1}[t_a = k]\cdot P_{a,s}$$

---

### Index 1 — Relative Exposure Index (REI)

$$\boxed{\text{REI}_{s,k} = \frac{\bar{P}_{s \mid k}}{\bar{P}_s}}$$

**Interpretation.** REI measures whether segment $s$ receives topic $k$ at a higher or lower rate than the campaign-wide baseline. A value of 1 indicates no differential targeting: the demographic profile of topic-$k$ ads is identical to that of the full corpus. Values above 1 indicate over-targeting of segment $s$ by topic $k$; values below 1 indicate under-targeting.

**Domain.** $\text{REI}_{s,k} \in [0, +\infty)$ with natural anchor at 1. The index is scale-free and comparable across candidates, rounds, and topics without normalization.

**Relationship to microtargeting.** REI operationalizes targeting precision at the segment-topic cell level. The hypothesis that a campaign practices demographic microtargeting is equivalent to the claim that the distribution of REI values across cells exhibits systematic dispersion around 1 — that is, that $\text{REI}_{s,k} \neq 1$ for a non-trivial set of $(s,k)$ pairs, and that deviations are coherent with identifiable campaign strategies.

---

### Index 2 — Topic Targeting Divergence (TTD)

$$\boxed{\text{TTD}_k = \text{JSD}\!\left(\bar{\mathbf{P}}_{\cdot \mid k} \;\|\; \bar{\mathbf{P}}_{\cdot}\right)}$$

where $\bar{\mathbf{P}}_{\cdot \mid k} = (\bar{P}_{s \mid k})_{s \in \mathcal{S}}$ and $\bar{\mathbf{P}}_{\cdot} = (\bar{P}_s)_{s \in \mathcal{S}}$ are probability vectors over $\mathcal{S}$, and JSD is the Jensen-Shannon Divergence:

$$\text{JSD}(P \| Q) = \frac{1}{2}\,D_{\text{KL}}(P \| M) + \frac{1}{2}\,D_{\text{KL}}(Q \| M), \qquad M = \frac{P + Q}{2}$$

$$D_{\text{KL}}(P \| M) = \sum_{s \in \mathcal{S}} \bar{P}_{s \mid k} \log_2 \frac{\bar{P}_{s \mid k}}{M_s}$$

**Interpretation.** TTD is a symmetric, smoothed measure of divergence between the demographic profile of topic-$k$ ads and the campaign baseline. It answers the question: *how different, in distributional terms, is the audience that topic $k$ reached from the audience the campaign reached on average?*

**Domain.** $\text{TTD}_k \in [0,1]$ (using $\log_2$). A value of 0 indicates that topic $k$ was distributed to exactly the same demographic mix as all other ads — no targeting differentiation. A value approaching 1 indicates that the demographic profile of topic-$k$ ads is nearly orthogonal to the baseline.

**Role in the analysis.** TTD produces a ranking of topics by targeting precision, identifying which topics in the campaign were genuinely targeted at specific demographic niches versus broadcast indiscriminately. This ranking is the primary headline result of the microtargeting analysis.

---

### Index 3 — Targeting Gini Coefficient (TGC)

$$\boxed{\text{TGC}_k = \frac{\displaystyle\sum_{s \in \mathcal{S}} \sum_{s' \in \mathcal{S}} \left|\bar{P}_{s \mid k} - \bar{P}_{s' \mid k}\right|}{2\cdot|\mathcal{S}|\cdot\displaystyle\sum_{s \in \mathcal{S}} \bar{P}_{s \mid k}}}$$

**Interpretation.** TGC applies the Gini coefficient to the vector of conditional audience weights $(\bar{P}_{s \mid k})_{s \in \mathcal{S}}$. It measures the *concentration* of topic $k$'s demographic reach across segments, independent of which specific segments are reached. A low TGC indicates that a topic's audience is spread broadly and roughly uniformly across all demographic cells. A high TGC indicates concentration in a small number of cells.

**Domain.** $\text{TGC}_k \in [0,1]$, where 0 is perfect equality across segments and 1 is complete concentration in a single segment.

**Joint interpretation with TTD.** TGC and TTD are complementary and non-redundant:

| TTD | TGC | Interpretation |
|-----|-----|----------------|
| High | High | Surgically targeted: distinctive profile, concentrated audience |
| High | Low | Strategically differentiated: distinctive profile, broad reach |
| Low | High | Concentrated but not unusual: narrow audience, close to baseline |
| Low | Low | Broadcast: no meaningful demographic differentiation |

This two-dimensional characterization of each topic constitutes the structural typology of microtargeting strategies observable in the data.

---

## Panel Construction for Segmentation Analysis

### Segment Space

The demographic segment space is $\mathcal{S} = \mathcal{G} \times \mathcal{R}$, where:

$$\mathcal{G} = \{13\text{–}17,\; 18\text{–}24,\; 25\text{–}34,\; 35\text{–}44,\; 45\text{–}54,\; 55\text{–}64,\; 65{+}\}, \quad |\mathcal{G}| = 7$$

$$\mathcal{R} = \{\text{Female},\; \text{Male},\; \text{Unknown}\}, \quad |\mathcal{R}| = 3$$

giving $|\mathcal{S}| = 21$ joint cells. Marginal analyses over $\mathcal{G}$ and $\mathcal{R}$ are obtained by summing $P_{a,s}$ over the complementary dimension prior to index computation:

$$P_{a,g} = \sum_{r \in \mathcal{R}} P_{a,(g,r)}, \qquad P_{a,r} = \sum_{g \in \mathcal{G}} P_{a,(g,r)}$$

Results are reported separately for the age margin ($|\mathcal{G}| = 7$ rows) and the gender margin ($|\mathcal{R}| = 3$ rows). The full joint analysis over $\mathcal{S}$ is available but withheld from the main tables given cell sparsity at the joint level for individual-candidate subsets.

### REI Panel

For each analysis subset $q$, the REI panel is the matrix:

$$\mathbf{REI}_q \in \mathbb{R}_{>0}^{(|\mathcal{G}| + |\mathcal{R}|) \times K}$$

with entry $(s,k)$ equal to $\text{REI}_{s,k}$. Rows are ordered by age group (ascending) followed by gender categories. Columns are ordered by $\text{TTD}_k$ descending, so the most targeted topics appear leftmost.

Entries above 1 indicate over-representation of segment $s$ in topic $k$ relative to the campaign baseline; entries below 1 indicate under-representation. Values are reported to two decimal places. A column of all-ones would indicate a topic with no demographic differentiation.

### Topic Summary Panel

For each subset $q$, the topic summary panel is a $K \times 5$ table:

$$\mathbf{T}_q = \left[k,\; \text{Label}_k,\; N_k,\; \text{TTD}_k,\; \text{TGC}_k,\; \underset{s}{\arg\max}\;\text{REI}_{s,k},\; \max_s\,\text{REI}_{s,k} \right]_{k=1}^{K}$$

Rows are sorted by $\text{TTD}_k$ descending. This panel is the primary result table for the microtargeting section.

**Columns:**

- $N_k$: raw count of ads assigned to topic $k$, providing scale context
- $\text{TTD}_k$: targeting precision relative to baseline (main ranking criterion)
- $\text{TGC}_k$: audience concentration (structural typology dimension)
- $\arg\max_s \,\text{REI}_{s,k}$: the segment most over-targeted by topic $k$
- $\max_s \,\text{REI}_{s,k}$: magnitude of peak over-targeting

### Cross-Round Panel (Topic Birth and Death)

For candidates present in both rounds ($c \in \{\text{Boric, Kast}\}$), a cross-round comparison panel is constructed. Because round-1 and round-2 models are estimated independently, topic indices are not directly comparable. Correspondence between topics across rounds is established by computing pairwise cosine similarity between estimated word distributions:

$$\text{sim}(k_1, k_2) = \frac{\hat{\boldsymbol{\phi}}_{k_1}^{(v=1)} \cdot \hat{\boldsymbol{\phi}}_{k_2}^{(v=2)}}{\|\hat{\boldsymbol{\phi}}_{k_1}^{(v=1)}\|\;\|\hat{\boldsymbol{\phi}}_{k_2}^{(v=2)}\|}$$

for all pairs $(k_1, k_2) \in \{1,\dots,K\}^2$. The resulting $K \times K$ similarity matrix $\mathbf{C}$ supports three formal claims:

- **Topic persistence:** $\text{sim}(k_1, k_2) > \tau_{\text{high}}$ — a round-1 topic survives into round 2
- **Topic birth:** no $k_1$ such that $\text{sim}(k_1, k_2) > \tau_{\text{low}}$ — topic $k_2$ has no round-1 analog
- **Topic death:** no $k_2$ such that $\text{sim}(k_1, k_2) > \tau_{\text{low}}$ — topic $k_1$ has no round-2 analog

Thresholds $\tau_{\text{high}}$ and $\tau_{\text{low}}$ are reported explicitly and sensitivity-checked. This replaces the qualitative comparison currently in the thesis with a formal, replicable criterion.

The cross-round REI comparison for persistent topics answers whether not only the content but also the *targeting strategy* of a topic changed between rounds — a second-order result with direct implications for the strategic communication literature.

### Subsetting Hierarchy

All panels nest within the following hierarchy:

```
Round (v=1, v=2)
  └── Political bloc (All, Left, Right)
        └── Candidate (Boric, Kast, MEO, Sichel, Yasna)
              └── Segment dimension (Age margin, Gender margin)
                    └── Topic k (ordered by TTD_k)
```

This hierarchy defines the natural ordering of results sections in the working paper. Bloc-level and candidate-level models are estimated independently; results at one level do not aggregate mechanically to the level above.
