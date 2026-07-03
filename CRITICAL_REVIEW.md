# Critical review — *The practical impact of numerical variability on structural MRI measures of Parkinson's disease*

Internal critical read of the current revision (branch `claude/paper-review-comments-yb84cg`),
prepared to complement the reviewer responses in `scireports_2026_reviews.md`.
It is deliberately critical: strengths are summarized briefly, and most of the
document lists weaknesses and things a careful reviewer is likely to press on.

## Summary of the paper

The manuscript quantifies numerical variability (floating-point noise emulated
with Monte Carlo Arithmetic, MCA) in FreeSurfer 7.3.1 structural MRI analyses of
Parkinson's disease using PPMI data, and shows it is large enough to flip
statistical conclusions. It introduces the Numerical-Population Variability Ratio
(NPVR = σ_num / σ_pop), propagates it analytically through common estimators to
predict uncertainty in effect sizes and p-values from summary statistics alone,
and applies this to 13 published PD studies to estimate significance-flip
probabilities. A web tool is provided.

## Strengths

- Important, under-appreciated problem, framed with a clear practical message
  (numerical noise does not average out with sample size the way sampling error
  does; longitudinal designs are worse).
- The NPVR + delta-method propagation is a genuinely useful contribution: it
  turns an expensive Monte Carlo measurement into something reviewers can apply
  retrospectively from published summary statistics.
- The empirical MCA experiment, the analytical model, and the numerical
  validation (Supplementary Notes S5–S6) form a coherent three-part argument.
- The revision responded substantively to the reviewers: metric-type breakdown,
  practical-recommendations paragraph, Wilson CIs on Figure 1, corrected Figure 4
  terminology, and global cross-sectional vs longitudinal averages in the abstract.

## Major concerns

1. **Transferability of PPMI-derived σ_num to the 13 external studies.**
   The headline retrospective analysis applies numerical variability measured on
   one cohort (112 PD / 89 HC, PPMI, one scanning context) to 13 heterogeneous
   published studies with different scanners, field strengths, populations, and
   FreeSurfer versions. σ_num is presented as a pipeline property, but it plausibly
   depends on image SNR, resolution, and morphology. The paper should state
   explicitly that the flip-probability estimates for external studies assume the
   PPMI-measured NPVR transfers, and bound how much this assumption could move the
   numbers. This is the single most load-bearing assumption in Section 2.3.

2. **Heterogeneity / selection of the 13 studies (Reviewer 2's point, only
   partly resolved).** The metric-type breakdown added in revision helps, but the
   pool still mixes study designs whose only commonality is FreeSurfer. Selection
   criteria ("based on available summary statistics") invite selection bias — the
   subset of papers that report extractable statistics may not be representative.
   State the inclusion/exclusion procedure and the total number screened.

3. **The Beta-distribution model for p-value fluctuation.** Flip probabilities are
   obtained by modeling each reported p-value as Beta-distributed with the reported
   p as mean and a delta-method σ as SD, then integrating past α. This is a strong
   parametric choice. Near the boundary the delta-method (first-order) approximation
   is least reliable precisely where the CDF is most sensitive. The validation in
   S5/S6 should be described as validating *this* choice, and its failure modes
   (skew, heavy tails, p near 0/1) acknowledged.

4. **The n = 1,340 / 12,000 headline numbers depend on an arbitrary criterion.**
   These sample sizes come from requiring σ_d ≤ 0.01. The threshold 0.01 is not
   motivated; the numbers scale strongly with it. Show sensitivity (e.g. a small
   table or curve of required n vs the σ_d target) so readers see these are
   illustrative, not hard requirements.

5. **Uncorrected thresholds for the instability rates.** The instability
   percentages (27%, 21%, up to 53%) are computed at uncorrected p < 0.05 across
   many regions × tests. Whether the same fragility survives FDR/multiple-comparison
   correction is the question a skeptical reader will ask, since real studies
   correct. Report instability under the corrected regime, or justify uncorrected.

6. **Mechanism is described but not explained.** Why cortical area/volume are more
   fragile than thickness/subcortical volume, and why longitudinal amplifies (the
   "catastrophic cancellation" claim), are asserted rather than demonstrated. The
   paper is honest that mechanism is out of scope, but the cancellation claim in
   particular is testable and currently unsupported by direct evidence.

## Moderate / methodological

- **26 MCA samples.** σ_num (and the variance comparisons via Ansari-Bradley) are
  estimated from 26 repetitions. That is thin for stable variance/tail estimates,
  especially per region. Report uncertainty on σ_num itself, or justify n = 26.
- **Hemispheric asymmetry (Reviewer 2).** The response (sampling effect vs biology)
  is reasonable and CIs were added, but the discussion remains speculative; a
  sentence acknowledging it cannot be resolved here would be more honest than
  implying two clean explanations.
- **Independence assumptions.** NPVR propagation treats numerical error as
  independent of sampling error and across regions; regional measures are
  correlated. Note the implication for any aggregate/family-wise statement.

## Presentation / minor (worth fixing before resubmission)

- **Caption error, Supplementary Table S7** (`tab:stats-coef-var-subcortical`,
  `appendix.tex`): caption reads "Variance variability in **cortical** regions"
  but the table lists **subcortical** structures (L-Thalamus, L-Caudate, …).
  Should read "subcortical". Also "Variance variability" is redundant — prefer
  "Variance of test statistics" or "Variability of test statistics".
- **Supplementary numbering shares the "S" prefix across separate figure and
  table counters**, so both a "Figure S6" and a "Table S6" exist. This was the
  underlying source of the reviewer's "S8 before S7" confusion. The float-ordering
  inversion has been fixed in this revision, but consider always writing
  "Fig. S#/Table S#" (never bare "S#") or switching to a single combined
  supplementary counter to remove the ambiguity entirely.
- **Abstract vs Discussion headline numbers.** Abstract says numerical variation
  "reached nearly one-third of the population variability"; Discussion now says
  "18% … cross-sectional and 55% … longitudinal on average, with up to 80%".
  Harmonize so the abstract's one-third and the discussion's averages tell one story.
- **Hyphenation:** abstract uses "cross sectional" (unhyphenated) while the body
  uses "cross-sectional". Make consistent.
- **Figure 4 bin sizes remain non-uniform** (0.005 for false-positive risk, 0.05
  for false-negative risk). This is defensible (denser sampling near threshold),
  but a half-sentence in the caption justifying the asymmetry would preempt the
  reviewer question that was raised.
- **"Test statistics" vs "statistical test values":** now consistent in the main
  text; check the appendix uses the same term throughout.

## Mathematical review (derivations)

Every derivation was checked step by step against the supporting proofs. The
mathematics is sound; there are no algebraic errors in the propagation results.

Verified correct:

- **Delta-method core** (`methods.tex`, `eq:var-ds`): Var_num[ds] ≈ σ_num²‖∇f‖²
  under the stated independent, homoscedastic Gaussian noise model.
- **Cohen's *d***: Σ(∂d/∂xᵢ)² = (1/s_p²)(1/n₁ + 1/n₂ + d²/df); the cross term
  vanishes because Σ_{i∈G_g}(xᵢ − x̄_g) = 0, and (n₁−1)s₁² + (n₂−1)s₂² = df·s_p².
  Balanced large-n limit σ_d ≈ 2ν/√n.
- **Two-sample *t***: Var[t] = ν²(1 + d²/(df·ω_n)); the df·ω_n limits (→4 balanced,
  →∞ unbalanced) are correct; σ_p = 2f_t(|t₀|)ν.
- **ANCOVA (df₁=1)**: F = t² ⇒ σ_F = 2√F·ν and σ_p = 2√F₀·f_F(F₀)·ν.
- **Partial correlation**: ∂R/∂b re-derived independently, equal to the paper's
  (1−c²)(ab−c)/D³; the gradient sum collapses via the correlation identities
  (Σαᵢ² = (n−1)(1−a²), Σβᵢ² = (n−1)(1−b²), Σαᵢβᵢ = (n−1)(c−ab)) and the symmetric
  identity (1−a²)(1−b²)−(c−ab)² = (1−b²)(1−c²)−(a−bc)² to
  Σ(∂R/∂xᵢ)² = (1−R²)/((n−1)s_x²(1−b²)). The lower bound (b²∈[0,1]) and the
  propagated σ_p bound follow correctly.
- **Supplementary Note S1** proofs (mean, variance, std, pooled std, covariance,
  Pearson derivative, correlation identities): all correct.
- **Table 1** reproduces every derived σ and σ_p expression.
- **Beta parameterization** (`eq:beta-params`): standard method-of-moments (valid
  while σ_p² < μ_p(1−μ_p)); the flip-probability integrals P[FN]=∫₀^α, P[FP]=∫_α^1
  are consistent with the figure shading and the main-text FP/FN-risk convention.

One fix applied (terminology, not math): the two flip-probability bullets
(`methods.tex`) labeled the flip regions FN/FP (consistent with the paper's
false-positive/false-negative-**risk** convention) but tagged them "Type I-like"
/"Type II-like", which is the opposite pairing in standard usage (false positive ≡
Type I, false negative ≡ Type II) and reads as self-contradictory — the same
vocabulary problem Reviewer 2 raised for Figure 4. The two parenthetical
"(instability leading to Type X-like errors)" clauses were removed; the general
statement that the model links to classical Type I/II error rates is retained.

Minor (not errors), optional: subject count is written `n` in the σ definitions
and the estimator sums but `N` in the noise-model paragraph — harmonize; the
squared Cohen's-*d* derivative uses "±" for a cross term whose sign is group-
dependent but which vanishes on summation; and the Beta model's validity
condition (σ_p² < μ_p(1−μ_p)) could be stated.

## Bottom line

The core contribution (NPVR and its retrospective applicability) is solid and the
revision addressed the reviewers' substantive asks. The main residual risk is
Section 2.3: the external-study flip probabilities rest on transferring
PPMI-measured numerical variability to heterogeneous cohorts and on a parametric
p-value model, and the headline sample-size numbers depend on an unstated
criterion. Framing these three as explicitly stated assumptions/limitations —
rather than leaving them implicit — would materially strengthen the paper and is
likely what a second-round reviewer will focus on.
