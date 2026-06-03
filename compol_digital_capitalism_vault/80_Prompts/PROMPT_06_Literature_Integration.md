
# PROMPT: Literature Integration for Conceptual Framework

### SOURCE MATERIAL

- **Location**: `compol_digital_capitalism_vault/10_Literature/papers/` (contains demoted original NotebookLM notes)
- **Task**: Generate two new sets of integrated notes from these source materials

---

### OUTPUT SET 1: CLUSTER NOTES

**Destination**: `compol_digital_capitalism_vault/10_Literature/cluster_notes/`

**Structure**: Create 7 cluster-specific integration notes, one for each cluster code:

1. **NB01_Paid_Digital_Ads.md** (G1_PAID_ADS_OBJECT)
2. **NB02_Topic_Modeling_Methods.md** (G2_TOPIC_MODELING_METHOD)
3. **NB03_Platformization_Digital_Politics.md** (G3_PLATFORMIZATION_DIGITAL_POLITICS)
4. **NB04_Chile_LatAm_Context.md** (G4_CHILE_LATAM_CASE_CONTEXT)
5. **NB05_Ethics_Manipulation_Risk.md** (G5_ETHICS_MANIPULATION_RISK)
6. **NB06_Digital_Capitalism_Platform_Power.md** (G6_DIGITAL_CAPITALISM_PLATFORM_POWER)
7. **NB07_Venue_Positioning_Precedents.md** (G7_VENUE_POSITIONING_PRECEDENT)

**Integration Logic for Each Cluster Note**:

For each cluster, synthesize the paper notes that match the cluster's definition by addressing the cluster-specific questions:

- **G1**: Does the source study paid ads or organic posts? What platform? What targeting mechanism? What does it say about ad visibility, disclosure, persuasion, segmentation, or audience control?
- **G2**: What method is used? What corpus? What validation strategy? Topic number K? What preprocessing choices? Does it discuss short texts, Spanish, interpretability, or alternatives to LDA?
- **G3**: How does the source define digitalization/platformization? What mechanisms are named? Does it treat platforms as passive channels or active infrastructures? Is the pattern global, local, or comparative?
- **G4**: Which country/election is studied? What makes the context distinctive? Does it discuss Chile 2021, post-2019 politics, party fragmentation, LatAm platforms, or regional campaign practices?
- **G5**: What democratic risk is identified? Is the concern manipulation, privacy, polarization, misinformation, opacity, unequal exposure, or persuasion? Does the source distinguish fear from evidence?
- **G6**: What theory of digital capitalism/platform power is offered? Does it explain data extraction, commodification, governance, visibility, control, or political subject formation? How could this deepen the conceptual framework?
- **G7**: What journal published this? Why is it a precedent? Which side of the paper's niche does it cover: method, object, region, or theory? Is it a competitor, complement, or legitimating precedent?

**Format for Each Cluster Note**:

```markdown
# [Cluster Label]

## Cluster Definition
[Definition from table]

## Synthesis of Sources
[Integrated analysis addressing cluster-specific questions, citing specific papers]

## Cross-References to Paper Notes
- [[Paper_Note_1]] - [Relevance to cluster]
- [[Paper_Note_2]] - [Relevance to cluster]
[Continue for all papers in this cluster]

## Gaps and Tensions
[What the cluster literature fails to address or where sources contradict]
```

### OUTPUT SET 2: CONCEPTUAL FRAMEWORK NOTES

**Destination**: `compol_digital_capitalism_vault/10_Literature/conceptual_framework_notes/`

**Purpose**: Build notes that directly serve the publishable conceptual framework, using cluster notes as routers to paper notes, with explicit theoretical positioning.

**Theoretical Positioning**:

- Adopt **Christian Fuchs' perspective on digital capitalism** as the critical lens
- Do NOT remain neutral; position the literature in relation to:
    - Platform capitalism and data commodification
    - Power asymmetries in digital political infrastructure
    - The political economy of microtargeting
    - Class, labor, and exploitation dimensions of platform-mediated campaigning

**Required Conceptual Framework Notes**:

1. **CF01_Microtargeting_As_Digital_Capitalism.md**
    - Integrate: G1 (paid ads object) + G6 (digital capitalism/platform power)
    - Position: How microtargeting practices instantiate platform capitalism logic
    - Router function: Link to specific papers in NB01 and NB06
2. **CF02_Methodological_Approach_Topic_Modeling.md**
    - Integrate: G2 (topic modeling methods) + G7 (venue precedents)
    - Position: Why LDA/text-as-data is appropriate for exposing platform power dynamics
    - Router function: Link to NB02 and NB07
3. **CF03_Platformization_Of_Politics.md**
    - Integrate: G3 (platformization) + G4 (Chile/LatAm context)
    - Position: How platformization operates differently in Global South crisis contexts
    - Router function: Link to NB03 and NB04
4. **CF04_Democratic_Risk_Vs_Evidence.md**
    - Integrate: G5 (ethics/manipulation) + G4 (Chile context)
    - Position: Distinguish dystopian fears from empirically-documented harms through a political economy lens
    - Router function: Link to NB05 and NB04
5. **CF05_Chile_2021_As_Constitutive_Context.md**
    - Integrate: G4 (Chile/LatAm) + G3 (platformization) + G6 (platform power)
    - Position: Why 2021 Chile (post-estallido, pandemic, bloc dislocation) is theoretically generative, not just another case
    - Router function: Link to NB04, NB03, NB06
6. **CF06_Integrated_Analytical_Framework.md**
    - Integrate: ALL clusters (G1-G7)
    - Position: The complete theoretical framework connecting platform capitalism → political crisis → microtargeting strategies → democratic implications
    - Router function: Comprehensive index linking to all cluster notes and key paper notes

**Format for Each Conceptual Framework Note**:


```markdown
# [Conceptual Framework Element]

## Theoretical Position (Fuchs/Digital Capitalism Lens)
[Explicit positioning statement - not neutral]

## Literature Integration
[Synthesis drawing from specific cluster notes]

## Empirical Implications for Chile 2021
[How this framework element guides analysis of the case]

## Cross-References to Cluster Notes
- [[NB0X_Cluster_Name]] - [Specific relevance]

## Cross-References to Paper Notes
- [[Paper_Note_X]] - [Specific insight]
- [[Paper_Note_Y]] - [Specific insight]

## Unresolved Questions
[What this framework element still needs to address]
```


### EXECUTION CONSTRAINTS

1. **Preserve Original Notes**: Do not modify notes in `papers/` folder; only read and reference them
2. **Maintain WikiLinks**: Use `[[NoteName]]` syntax for all cross-references to enable Obsidian/Roam-style navigation
3. **Cite Specific Papers**: When synthesizing, explicitly name papers (e.g., "Borgesius et al. (2018) argues...") rather than vague "the literature says"
4. **Position, Don't Describe**: In conceptual framework notes, take a stance. Example: "Fuchs' framework reveals that X is not merely a technical issue but a manifestation of platform capital's extraction logic"
5. **Bridge to Empirical Analysis**: Each conceptual framework note should clearly indicate how it informs the analysis of Chile 2021 Facebook ads


### DELIVERABLE STRUCTURE


```
compol_digital_capitalism_vault/10_Literature/
├── _legacy/
│   └── [legacy notes stored here - no changes]
├── papers/
│   └── [original notes demoted here - no changes]
├── cluster_notes/
│   ├── NB01_Paid_Digital_Ads.md
│   ├── NB02_Topic_Modeling_Methods.md
│   ├── NB03_Platformization_Digital_Politics.md
│   ├── NB04_Chile_LatAm_Context.md
│   ├── NB05_Ethics_Manipulation_Risk.md
│   ├── NB06_Digital_Capitalism_Platform_Power.md
│   └── NB07_Venue_Positioning_Precedents.md
└── conceptual_framework_notes/
    ├── CF01_Microtargeting_As_Digital_Capitalism.md
    ├── CF02_Methodological_Approach_Topic_Modeling.md
    ├── CF03_Platformization_Of_Politics.md
    ├── CF04_Democratic_Risk_Vs_Evidence.md
    ├── CF05_Chile_2021_As_Constitutive_Context.md
    └── CF06_Integrated_Analytical_Framework.md
```


