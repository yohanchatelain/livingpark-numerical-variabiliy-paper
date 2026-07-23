# Scientific Reports: reviews 2

Deadline: 5th August

Dear Editor and Reviewers,
We sincerely appreciate the time and effort you have dedicated to reviewing our manuscript The practical impact of numerical variability on structural MRI measures of Parkinson’s disease. Your insightful and constructive feedback has been invaluable in improving the quality and clarity of our work. We have carefully considered all of your comments and have made revisions accordingly. Below, we address each of your concerns and suggestions in detail. Our manuscript includes the related edits in track-change mode.
Best regards,

Yohan Chatelain

Editor Comments

---

## Editors

### Comments

"-Please address the final remarks from Reviewer #2.

### Authors responses:

See our responses to Reviewer 2 below.

### Comments

-Where feasible, report exact p-values rather than simply stating p < 0.05 or p > 0.05, as this allows readers to judge the strength of the evidence better.

### Authors responses:

We revised every instance where a specific reported result was expressed only as an inequality, replacing it with the exact statistic and p-value. Instances that state p<0.05 as a threshold definition for a summary figure or table (e.g., "proportion of significant tests, p<0.05, uncorrected," which counts how many of many tests cross a threshold rather than reporting one specific test) are retained as such, since no single exact p-value applies there.
- The permutation tests comparing npvr between PD and HC groups (Results §2.2) now report the exact, per-metric p-value from Supplementary Table S6 instead of a flat p>0.05, and make explicit that the comparison uses a Bonferroni-corrected threshold: 
**Lines 126–131:**
```“In cross-sectional baseline analyses, the average npvr was 0.191 for the PD group and 0.176 for HC. A permutation test found no difference surviving Bonferroni correction across the four metrics (area p=0.734, thickness p=0.033, volume p=0.371, subcortical volume p=0.646; corrected α=0.05/8=0.00625; over the eight metric × analysis tests; Supplementary Table S6).”```
**Lines 134–138:**
```“In contrast, longitudinal analyses exhibited substantially higher variability, with average npvr values of 0.561 for PD and 0.549 for HC; again, no difference survived Bonferroni correction across the four metrics (area p=0.482, thickness p=0.919, volume p=0.370, subcortical volume p=0.489; Supplementary Table S6).”```
- The cohort comparison in Methods (Table 1) now reports exact statistics
**Lines. 318–320:**
```“The PD and HC groups did not differ significantly in age (t=-0.035, p=0.972), education (t=-1.479, p=0.141; two-sample t-tests), or sex distribution (\chi^2=3.108, p=0.078; chi-square test; Table 1).”```
- The sample-size vs. significance-flip-probability analysis (Results §2.3) now reports exact statistics for the overall association and for each test type, together with the exact number of data points each is computed over
**Lines 177–183:**
```“Across all 707 extracted results, flip significance probability was only weakly associated with sample size (Pearson correlation r=-0.118, p=0.002). This overall association was driven by correlation-based tests, for which flip probability decreased significantly with sample size (n=196, r=-0.417, p<10^{-8}), consistent with the theoretical dependence of the sampling variance of the correlation coefficient on n (Table 1); for T- and F-based tests no significant association was found (n=307, r=-0.095, p=0.096 and n=204, r=-0.093, p=0.187, respectively).”```
and, earlier in the same subsection, the total pool behind Figure 4
**Lines 169–170:**
```"...pooled across all statistical tests and the 13 reviewed papers (707 extracted results: 198 reported as significant and 509 as non-significant)."```

### Comments

-The terms numerical variability, numerical uncertainty, and numerical instability are sometimes used interchangeably. It would improve readability to define these terms explicitly and use them consistently throughout the manuscript.
-The terms numerical variability, numerical uncertainty, and numerical instability are sometimes used interchangeably. It would improve readability to define these terms explicitly and use them consistently throughout the manuscript.

### Authors responses:

We agree that the interchangeable use of these terms hurt readability. Rather than formally distinguishing three closely related terms — which we felt risked perpetuating the very ambiguity the reviewer flagged — we resolved the issue by adopting a single, consistent term, numerical variability, throughout the manuscript, and revised every occurrence accordingly (main text, Methods, and Supplementary Information).

Specifically, all previous uses of "numerical uncertainty" and "numerical instability" (and their standalone variants, e.g., "computational uncertainty," "pipeline/inference instability") now read "numerical variability." We chose "variability" rather than "uncertainty" because it is consistent with the metric name used throughout  the Numerical-Population Variability Ratio (NPVR) and with the manuscript title. We deliberately retained a small number of genuinely distinct terms that denote different concepts: "numerical noise" (the machine-level perturbation injected by Monte Carlo Arithmetic), "numerical precision"/"significant digits" (the number of reliable digits), and the broad umbrella "uncertainty" only where numerical variability is described as one component of the total uncertainty in neuroimaging (alongside biological variability and sampling error).

### Comments

-The paragraphs: "We selected T1-weighted MRI data..." & "We processed all images for..." belong to the methods section. Please report only the results in the results section. Please do the same in sections 2.2 & 2.3, removing method-related texts into the section 4.

### Authors responses:

We moved the method-descriptive paragraphs out of Results §2.1–§2.3 and into Methods, replacing them in the Results with brief, results-focused statements that point to the fuller Methods description:

- §2.1: the participant-selection paragraph ("We selected T1-weighted MRI data...") and the image-processing/MCA paragraph ("We processed all images...") both of which duplicated content already present in Methods §4.1 and §4.3:
**Lines 72–74:**
```“Analyses included the 112 PD-non-MCI and 89 HC participants from the PPMI dataset who met inclusion criteria after quality control (Methods, §4.1; Table 2).”```
**Lines 75–90:**
```“We processed all images for both time points using FreeSurfer 7.3.1 instrumented with Monte Carlo Arithmetic (MCA) to introduce machine-level numerical noise and quantify numerical variability across repeated runs, yielding 26 valid perturbed realizations per participant after quality control (Methods, §4.3; Supplementary Table S4). For all analyses, the unperturbed (IEEE-754) result fell within the range of numerically perturbed results, supporting the validity of the perturbation approach (Supplementary Note S4).”```

- §2.2: the sentence narrating how the uncertainty-propagation formulas were derived and validated now points to the existing Methods derivation and Supplementary validation note instead of re-narrating the process
**Lines 116–120:**
```“Propagating this ratio through standard statistical estimators (Methods, §4.3.2) yields closed-form approximations for the numerical variability in common statistics (Table 1), numerically validated in Supplementary Note S5.”```

- §2.3: the rationale for selecting the 13 retrospective studies, and the step-by-step re-derivation of the Beta-distribution significance-flip model (already fully described in Methods), are now (selection pointer; Beta-model pointer):
**Lines 153–155:**
```“...spanning a range of study designs and neuroscientific questions (selection criteria and study characteristics in Methods, §4.5 and Table 3)”```
**Lines 158–163:**
```“For each p-value reported as significant in the original articles, we estimated the probability of a numerically induced significance flip using the Beta-distribution model described in Methods (§4.4), parametrized by the reported p-value (mean) and the propagated numerical variability (standard deviation).”```
The selection rationale and study-by-study detail now live in a new Methods subsection, "Retrospective analysis of published studies" (see Reviewer 2, point 1, below).

### Comments

-For each statistical analysis, explicitly report the number of participants included after quality control and exclusions to improve transparency. "

### Authors responses:

- The main empirical analysis (§2.1–§2.2) now states its N up front (112  PD-non-MCI, 89 HC; see Comment 4 quote above, Lines 72–74) rather than only in  a cross-referenced table.
- The retrospective literature analysis (§2.3) now states the exact number of extracted results behind Figure 4 (707: 198 significant, 509 non-significant; Lines 169–170) and the exact N behind each sample-size correlation (overall 707; correlation-based tests n=196; T/F tests n=307 and n=204; see Comment 2 quote above, Lines 177–183).
- Each of the 13 retrospective studies' own sample size is now reported in the new Methods characterization table (Table 3; Reviewer 2, point 1, below).

### Comments

-Morteza Esmaeili
Editorial Board Member
Scientific Reports

## Reviewer 2

### Authors responses:

We thank the reviewer again for the constructive feedback across both rounds, and for recommending the manuscript for publication. We address the two remaining points below.
The authors addressed some of my concerns. In particular, they now discuss how numerical instability affects different FreeSurfer metrics (thickness, volume) differently, which strengthens the practical value of the manuscript.

### Comments

I still find it unfortunate that the authors did not take the opportunity to describe more qualitatively the body of studies used in their retrospective analysis. Grouping or characterizing these studies (e.g., by study design or neuroscientific question type) would have made the manuscript considerably more informative for the broader neuroimaging community, beyond method engineering.

### Authors responses:

We agree this would make the retrospective analysis considerably more informative. We added a new Methods subsection, "Retrospective analysis of published studies," which states the selection criteria and introduces a new characterization table covering, for each of the 13 studies: design (cross-sectional/longitudinal/both), the study's own sample size, the FreeSurfer-derived metric(s) examined, and its neuroscientific focus (new Methods §4.5, and Table 3 immediately following):
**Lines 513–531:**
```“We compiled a set of previously published studies reporting FreeSurfer-derived structural MRI findings in Parkinson’s disease, to illustrate the impact of numerical variability on reported outcomes across a range of study designs and research questions. Eligible studies had to report, for at least one cortical or subcortical measure, a p-value together with the sample size and statistical test used, so that numerical variability could be estimated from the formulas in Table 1 without requiring access to the original raw data. Thirteen studies met these criteria and were retained [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]. Table 3 summarizes the design, sample size, FreeSurfer-derived metric(s), and neuroscientific focus of each study. The set spans eight purely cross-sectional studies, two purely longitudinal studies, and three studies contributing both cross-sectional and longitudinal analyses, addressing questions of cognitive correlates and impairment (4 studies), psychiatric and behavioral comorbidities (2), motor subtypes (1), disease staging, atrophy, and progression (3), sleep disturbance (1), and methodological replication (2). For each study, we extracted every p-value reported for a FreeSurfer-derived structural measure, together with the corresponding test statistic, sample size, and test type, and propagated numerical variability through the significance-flip model described in Section 4.4.”```

We also added a summary of this characterization to the Discussion, directly addressing the point that fragility is not confined to one kind of finding
**Lines 222–227:**
```“These thirteen studies spanned a range of designs (eight cross-sectional, two longitudinal, and three combining both) and neuroscientific questions, including cognitive correlates and impairment, psychiatric and behavioral comorbidities, motor subtypes, disease staging and progression, and sleep disturbance (Methods §4.5; Table 3), indicating that numerically induced fragility is not confined to a narrow category of neuroimaging findings but is broadly distributed across the PD structural-MRI literature.”```

### Comments

Nonetheless, the main message is clear, and, I believe, suitable for publication in Scientific Reports.

Of note, regarding SI : in its current form it is difficult to navigate and largely consists of numerical tables with non-existent context and explanation, nor always linked to the main text either, so I could not perform a detailed review of it.

### Authors responses:


We agree, and substantially reworked the Supplementary Information (SI) to make it navigable and self-contained. Concretely:
1. **Table of contents.** We added a clickable table of contents at the top of the Supplementary Information, giving an at-a-glance, hyperlinked index of the six supplementary sections (S1–S6).
2. **Reader's roadmap.** Immediately below the "Supplementary Information" heading we added an orienting overview that states, in one line per section, what each supplementary section contains and which main-text claim or Methods subsection it supports directly addressing both the "difficult to navigate" and "not always linked to the main text" concerns 
**Lines 662–679:**
```“This Supplementary Information provides the derivations, additional analyses, and validation experiments supporting the main text. It is organised as follows: • Section S1 derives the partial derivatives of common sample statistics that underlie the closed-form variability-propagation formulas of Table 1 (Methods, “Relationship between NPVR and downstream statistical test variability”). • Section S2 quantifies cross-sectional numerical variability of FreeSurfer measures (significant digits and spatial-overlap Dice coefficients), with region-by-region precision tables supporting the low-precision claim in Results, Section 2.1. • Section S3 reports the region-level significance-flip frequencies, the HC-vs-PD permutation test, and the per-region Ansari-Bradley comparisons showing that longitudinal processing amplifies variance (Results, Sections 2.1–2.3). • Section S4 shows the distributions of test-statistic coefficients across MCA repetitions, including the unperturbed (IEEE-754) reference used to check the validity of the perturbation approach (Results, Section 2.1). • Section S5 numerically validates the variability-propagation formulas of Table 1 against sampled MCA estimates. • Section S6 numerically validates the Beta-distribution significance-flip model used in the retrospective analysis (Results, Section 2.3).”```
3. **Guidance for the dense tables.** For the large per-region tables the reviewer most likely had in mind the significant-digit / standard-deviation tables (Section S2) and the two 68-region Ansari-Bradley tables (Section S3) we added explicit interpretive text. The Section S2 tables already carried a lead-in clarifying the column abbreviations and how to read the significant-digit values; we expanded the Ansari-Bradley captions (Supplementary Tables S7 and S8) so each table is now interpretable on its own, e.g. 
**Table S7:**
```“Longitudinal versus cross-sectional variance of test statistics in subcortical regions ... W = Ansari-Bradley statistic, p = FDR-adjusted p-value; an asterisk (* p_{\text{FDR}} < 0.05) marks regions where the test statistic is significantly more variable longitudinally than cross-sectionally, i.e. where longitudinal processing inflates numerical variance.”```
We also corrected a caption error in which the subcortical Ansari-Bradley table was mislabelled as reporting "cortical" regions.
4. **Explicit main-text links.** In addition to the roadmap, each supplementary section now opens by naming the specific main-text result or Methods subsection it supports (e.g., the partial-derivative proofs of Section S1 are tied to the propagation formulas of Table 1; Lines 681–682 for S1 and Lines 789–790 for S4). We also linked the Section S3 Ansari-Bradley analysis from the main text (Results §2.1; Lines 101–103):
**Lines 100-103:**
```“Test statistics (r-values and F-values) also exhibited substantial variability across repetitions (see Supplementary Note S4). The greater variance of longitudinal compared with cross-sectional analyses was confirmed statistically by a one-sided Ansari-Bradley test contrasting the two (Supplementary Note S3).”```


We reviewed the remainder of the SI and confirmed that the other tables and figures are accompanied by prose describing what they show and how to interpret them.




