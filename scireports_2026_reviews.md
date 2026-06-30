Deadline: 9th July

Dear Reviewer,
We sincerely appreciate the time and effort you have dedicated to reviewing our manuscript The practical impact of numerical variability on structural MRI measures of Parkinson's disease. Your insightful and constructive feedback has been invaluable in improving the quality and clarity of our work. We have carefully considered all of your comments and have made revisions accordingly. Below, we address each of your concerns and suggestions in detail.
Best regards,

Yohan Chatelain


Reviewer 1
The Practical Impact of numerical variability on structural MRI measures of Parkinson's disease
The authors studied the impact of numerical variability coming from different computational environments on volumetric measurements of Parkinson's disease subjects obtained using Freesurfer, which is a common tool in neuroimaging studies for MRI volumetry. They used publicly available MRI data (PPMI). Their methods included injecting numerical noise at the order of machine precision into floating-point operations during processing. Authors stated that in many brain regions, the numerical variability reaches 1/3 of population variability, thereby affecting statistical group conclusions and clinical associations. They observed that numerical noise can alter downstream statistical inference in structural MRI analyses of Parkinson's. This effect is previously underappreciated by researchers. Authors state that in order to suppress this numerical uncertainty effect, the number of participants in a given study should considerably increase (1340 in cross-sectional, 12000 in longitudinal studies).
The authors further estimated this effect in 13 previously published Parkinson's studies.
The authors could better describe how this numerical effect is changing the key findings of these 13 papers. Figure 4 and the related discussion can be expanded. In its current form, Figure 4 is not very informative. The S6 section in the supplemental materials can also be expanded accordingly.

Authors responses:

We thank the reviewer for this suggestion. We made the following changes to address this point:

1. **Figure 4 simplified**: We simplified the Figure 4, pooling results across statistical test types so that the key message (flip probability as a function of distance to the significance threshold) is conveyed more directly. The previous, more detailed version of the figure, which separates results by statistical test type, has been moved to Supplementary Note S6, where it is now discussed in greater depth as described above.

2. **Figure 4 caption revised**: We rewrote the caption of Figure 4 to precisely define what is shown: each point represents a result (significant or non-significant) from the 13 reviewed studies; the y-axis is the probability of numerically-induced significance flip; and the terms "false positive risk" (reported significant result at risk of flipping to non-significant) and "false negative risk" (reported non-significant result at risk of flipping to significant) are now explicitly defined inline.

3. **Discussion of Figure 4 expanded**: We added sentences to the paragraph accompanying Figure 4 (Results section) explicitly noting that the breakdown by statistical test type is provided in Supplementary Note S6, and that the same pattern — high flip risk near the significance boundary — holds consistently across test types (T-values, F-values, and correlation coefficients), regardless of the statistic used.

4. **Supplementary Note S6 expanded**: We added a new paragraph to S6 that discusses the per-test-type breakdown shown in the figure in that section (Figure S6, previously labeled as `figure-distance-paper`). This paragraph explicitly interprets the distribution of flip probabilities across T-tests, ANCOVA (F-values), and partial correlations, noting that partial correlations tend to exhibit slightly higher flip probabilities consistent with their larger numerical variability as quantified by NPVR.

Reviewer 2
In this Brain-MRI method paper, the authors are working on two fronts: 1. they create a sophisticated numerical perturbation framework, and derive mathematical measure to retro-analyse existing studies. 2. they show the limit of Freesurfer numerical precision on the PPMI (Parkinson) dataset, thus the title.
Even in this age of stochastic algorithm, this is a worthy message to convey.
Pro:
- the authors show that this numerical error is different than a regular measurement error (that everyone is familar with) in that it does not necessarily cancel with a bigger dataset. This is one key take-home message. They also show that longitudinal analysis (at least as conducted in the literature) are even more prone to such errors.
- They run a Freesurfer analysis of the PPMI dataset under a range of numerical perturbation using an LD_PRELOAD trick, and shows the distribution of conclusions.
- They derive mathematical formulas for common statistics, and applies their sophisticated framework on a set of existing studies, using a model-based distribution of p-values, to conclude on the stability of the "significant" finding.
Con:
While I think the paper succeeds in convincing the reader that numerical variability is a real and potentially important source of uncertainty; it is much less successful at translating that observation into practical actions for neuroimaging researchers.
- The authors pool various unrelated studies whose only common point is that they used FreeSurfer, regardless on the type of study. The reader who cares about the reliability of previous studies conclusions would likely wants to know what kind of studies are dubious and what kind of findings are less affected. I believe the promise in the manuscript title, ie. of explaining how variability affects Parkinson disease results, should be honored.

Authors responses:

We agree that a breakdown by finding type adds important clarity. Our results show marked differences in numerical instability across MRI metric types (Supplementary Table S5): cortical area exhibits the highest instability in longitudinal settings (up to 53% of regions affected under ANCOVA), followed by cortical volume (up to 53% under partial correlation), subcortical volume (up to 36%), and cortical thickness (up to 28%). We now report these metric-specific instability rates in the Results section and refer readers to Supplementary Table S5 for the complete breakdown by metric type and statistical test. We additionally note, in the Discussion, that these metric-specific differences should inform the interpretation of neuroimaging findings and motivate targeted investigation of numerical stability for the most sensitive metrics. Understanding the precise mechanisms underlying these differences is an important avenue for future work, but is beyond the scope of the present study, which focuses on quantifying and communicating the impact of numerical variability.

- The authors do not cleanly separates the metrics of different nature (thickness, area, volume), even though those are intuitively expected to behave quite differently. Would the authors comment on that ?

Authors responses:

We agree this distinction is important and have now addressed it explicitly. Supplementary Table S5 provides a complete breakdown of instability rates (proportion of regions with significance flipping) by metric type (cortical area, cortical thickness, cortical volume, subcortical volume) and analysis type (ANCOVA and partial correlation), for both baseline and longitudinal settings. The results show that cortical area and cortical volume are substantially more numerically unstable in longitudinal analyses than cortical thickness and subcortical volume. We have added a dedicated paragraph in the Discussion summarizing these metric-specific findings and their implications. We also added a brief comparison of instability rates across metric types in the Results section, with a reference to Table S5.

- There are no further conclusion, no actionable methodological advices for the reader. Should we stop trusting FreeSurfer ? change the way to conduct statistical analyses ? or proceed to report results differently ? 

Authors responses:

We agree that actionable guidance is essential and thank the reviewer for raising this. We have added a dedicated "Practical recommendations" paragraph at the end of the Discussion with six concrete guidelines for neuroimaging researchers:

1. Move beyond binary p < 0.05 reporting toward effect sizes and confidence intervals, and report both significant and non-significant results (Amrhein et al., 2019).
2. Validate results across multiple neuroimaging pipelines rather than relying on a single tool, as numerical sensitivity varies across software.
3. Consider multiverse analyses that systematically explore the space of analytical decisions (Botvinik-Nezer et al., 2020; Lefort-Besnard et al., 2025; Kruper et al., 2021).
4. Systematically assess numerical stability using the NPVR framework or the provided web tool, particularly for longitudinal analyses where numerical amplification is pronounced.
5. For new pipeline development, prioritize numerical robustness, especially for longitudinal applications.
6. Develop a gallery comparing numerical variability and population variability across neuroimaging tools and pipelines, modeled on existing galleries of effect sizes such as BrainEffeX (Shearer et al., 2025), so that researchers can situate the numerical variability of a given tool relative to the population variability typically observed for the same measure, and compare this relationship across tools.

I believe the manuscript would benefit from clearer guidance regarding the practical implications of these findings.
Furthremore, there are some specific points that could be addressed or commented on:
- Loosy and inconsistent vocabulary should be improved: Caption of Figure 4 is misleading, as e.g. "False positives" actually refers to results reported as True positive if my understanding is correct. This doesn't help that the y-label is merely "Probability". The text mentions "Each point corresponds to a significant result reported in the literature", where non-significant results are necessarily plotted too, etc. IMHO, more effort on the figure and terminology would convey the result in a more precise and accurate way, with less reader effort.
- 
Authors responses:

We thank the reviewer for catching these inconsistencies and agree that the previous figure and text lacked precision. We have made the following corrections:

1. **Figure 4 caption**: Completely rewritten to (a) state that each point represents "a result (significant or non-significant) reported in the literature"; (b) define the y-axis as the "probability of significance flip"; (c) define "false positive risk" as the probability that a reported significant result flips to non-significant, and "false negative risk" as the probability that a reported non-significant result flips to significant. These definitions are now also consistent with the in-text description.

2. **Surrounding text**: The phrase "Each point corresponds to a significant result reported in the literature" has been corrected to "Each point corresponds to a result (significant or non-significant) reported in the literature."

3. **Supplementary Note S6 figure caption**: The same terminology corrections have been applied to the corresponding figure in S6 (figure-distance-paper), which additionally provides the per-test-type breakdown. 

- Fig 1. why are there such heavy left-right differences in some nucleus ? I would intuitively expect numerical precision to disrupt bilateral measures equally by default. Is it random chance or instability of the whole analysis ? If so, i believe CI-bars are necessary. If this is due to the nature of the studies themselves, this would require clarification, especially since the nature of the studies are always vague in the manuscript. At present, the reader cannot tell whether they reflect differences in numerical stability, differences in the underlying statistical analyses, or simply Monte Carlo sampling variability. 
The observed hemispheric differences deserve some discussion. 

Authors responses:

The left-right differences visible in Figure 1 are not caused by asymmetric numerical noise. By construction, Monte Carlo Arithmetic injects perturbations symmetrically and independently in all floating-point operations, regardless of hemisphere, so differential numerical instability between hemispheres is not expected. We see two possible explanations for the observed asymmetries. First, a statistical sampling effect: by chance, the underlying p-values for left and right regions may fall at different distances from the significance threshold, which directly governs the flip probability, so a result closer to the threshold will exhibit a higher flip probability regardless of hemisphere. Second, a genuine biological left-right difference in the underlying measure; confirming this would require dedicated analyses in a larger cohort and is beyond the scope of the present study.

Regarding confidence interval bars: these have been added to Figure 1 in the current revision (Wilson score intervals at 95% confidence level, visible for all bars), so readers can now directly assess whether apparent left-right differences exceed sampling uncertainty.

I think all that could be fixed in a minor revision, and would drastically increase the value for readers
