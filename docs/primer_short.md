# Test-negative design: "short" primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination, that is $\mathrm{VE} = 1 - \mathrm{RR}$ for some risk ratio RR. For purposes of a test-negative design (TND) study, we further define VE to be:

- a direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program,
- protection against both infection and progression to symptoms that would lead to a diagnostic test, written $\mathrm{VE}_{SP}$ in [Halloran, Longini, and Struchiner](https://doi.org/10.1007/978-0-387-68636-3),
- conditioned on (some amount of exposure) to disease, and
- binary, that is, individuals are considered vaccinated or not (e.g., people who were vaccinated shortly before the outcome of interest may be classified as "unvaccinated" in the study, because they are presumed to have not yet been protected).

## TND with independent test-positive and test-negative condition rates

**Proposition: Unbiased TND requires large counts.**

In the mathematically simplest derivation, we assume that:

- There is some population of $n_V$ vaccinated individuals and $n_U$ unvaccinated individuals that are _a priori_ eligible for inclusion in the TND.
- Receiving tests for test-positive and test-negative conditions are each inhomogeneous Poisson processes. Thus, for each individual, the number of positive tests for each vaccinated individual is Poisson-distributed with mean $x^{T+}_V$. Similarly define $x^{T-}_V$, $x^{T+}_U$, and $x^{T-}_U$.
- Test performance is perfect.

Note that this means that we assume there are no "collisions" between test-positive and test-negative conditions. An individual could theoretically test positive and then test negative one millisecond later.

The data available are a 2x2 table of counts of test results:

|               | Vaccinated | Unvaccinated |
| ------------- | ---------- | ------------ |
| Test positive | $Y^+_V$    | $Y^+_U$      |
| Test negative | $Y^-_V$    | $Y^-_U$      |

We are interested in the protection provided by the vaccine. In this model, where there are only test-positive and -negative conditions, we are interested in the risk ratio:

$$
\mathrm{RR} = \frac{x^{T+}_V}{x^{T+}_U}
$$

Consider the odds ratio as an estimator for the risk ratio:

$$
\hat{\mathrm{RR}} = \frac{Y^+_V Y^-_U}{Y^-_V Y^+_U}
$$

Because the counts of tests from each person is an i.i.d. Poisson distribution, the total counts of tests are themselves Poisson distributed:

$$
Y^+_V \sim \mathrm{Poisson}(n_V x^{T+}_V)
$$

and similarly for $Y^-_V$, $Y^+_U$, and $Y^-_U$.

These variables are all independent, so

$$
\mathbb{E}\left[\hat{\mathrm{RR}}\right] = \mathbb{E}[Y_V^+] \cdot \mathbb{E}\left[ \frac{1}{Y_V^-} \right] \cdot \mathbb{E}[Y_U^-] \cdot \mathbb{E}\left[ \frac{1}{Y_U^+} \right]
$$

If $Y \sim \mathrm{Poisson}(\lambda)$, then $\mathbb{E}[Y] = \lambda$. It is generally not the case that $\mathbb{E}[1/Y] = 1/\lambda$ (consider, e.g., $Y=0$), however, $\lim_{\lambda \to \infty} E[1/Y | Y > 0] = 1/\lambda$. Therefore, so long as all rates are nonzero:

$$
\begin{aligned}
\lim_{n_V, n_U \to \infty} \mathbb{E}\left[\hat{\mathrm{RR}}\right]
&= \frac{\mathbb{E}[Y_V^+] \mathbb{E}[Y_U^-]}{\mathbb{E}[Y_V^-] \mathbb{E}[Y_U^+]} \\
&= \frac{n_V x^{T+}_V \cdot n_U x^{T-}_U}{n_V x^{T-}_V \cdot n_U x^{T+}_U} \\
&= \frac{x^{T+}_V}{x^{T+}_U} \cdot \left( \frac{x^{T-}_V}{x^{T-}_U} \right)^{-1}
\end{aligned}
$$

Call this the "odds ratio of expectations" (ORE).

<!-- TO DO: Better name? -->

In this model:

$$
\mathrm{ORE} = \mathrm{RR} \cdot \left( \frac{x^{T-}_V}{x^{T-}_U} \right)^{-1}
$$

Thus, so long as:

1. the vaccinated and unvaccinated seek and receive the same average number of negative tests per capita,
2. $x^{T-}_V > 0$ and $x^{T-}_U > 0$, and
3. the population is very large,

then the TND odds ratio approaches an unbiased estimator of the relevant VE risk ratio.

## Conditioning on exposure

**Proposition: TND gives an unbiased estimate of VE given exposure, so long as exposure rates are identical.**

Replace the test-positive exposure rate $\lambda^{T+}_V$ with the exposure rate $\lambda^E_V$, the probability of infection given exposure $P[I|E,V]$ and the probability of testing given infection:

$$
\lambda^{T+}_V = \lambda_V^E \cdot P[T,I|E,V]
$$

(To check this result, treat exposure and testing as one-time possibilities, replacing $\lambda_V^E \to P[E|V]$ and $\lambda_V^{T+} \to P[T,I|V]$.)

In this case, the ORE is:

$$
\frac{P[T,I|E,V]}{P[T,I|E,U]} \cdot \frac{\lambda^E_V}{\lambda^E_U} \cdot \frac{\lambda^{T-}_U}{\lambda^{T-}_V}
$$

Thus, if the vaccinated and unvaccinated have equal exposure rates, then the TND odds ratio will be an unbiased estimate of protection from vaccine _conditioned on exposure_ (subject again to the other assumptions above). If the vaccinated are exposed at a higher rate, then TND will underestimate VE.

## Rare disease assumption

**Proposition: TND requires a rare disease assumption, but not because of its odds ratio.**

Because the TND uses an odds ratio to estimate a risk ratio, it is commonly believed that TND requires the rare disease assumption, since the TND is a kind of case-control study.

It is in general not true that interpreting case-control studies requires a rare disease assumption. Only certain case-control designs (the "cumulative" or "epidemic" design) need this assumption. The TND is not one of them.

Confusingly, however, the TND does require a rare disease assumption, but not because of the odds ratio, but because of sort of immortal time bias. After a person is infected, they cannot test negative for some time, even if the reason they pursued testing was because of a test-negative condition. Therefore, vaccination, by reducing the probability of infection, actually increases the probability of the test-negative condition, creating a second-order bias.

To demonstrate this bias, consider a simplified situation, in which everyone in the trial has the single opportunity to be exposed. The exposed then have a probability of being infected. After this, everyone has a probability of being tested. In this case, the ORE is:

$$
\frac{P[T,I|V] P[T,I'|U]}{P[T,I'|V] P[T,I|U]}
$$

where $I'$ means uninfected, and we are estimating the risk ratio:

$$
\frac{P[T,I|E,V]}{P[T,I|E,U]}
$$

The test positive terms are:

$$
\begin{aligned}
P[T,I|V] &= P[T,I,E|V] \quad \text{since } I \subset E\\
&= P[T,I|E,V] P[E|V]
\end{aligned}
$$

The test negative terms are more complicated, since we need to partition the uninfected into the exposed but infected versus the unexposed $I' = (I' \cap E) \cup E'$:

$$
\begin{aligned}
P[T,I'|V] &= P[T|I',V] P[I'|V] \\
&= P[T|I',V] \cdot \Big( P[I',E|V] + P[E'|V] \Big) \\
&= P[T|I',V] \cdot \Big( P[I'|E,V] P[E|V] + P[E'|V] \Big) \\
\end{aligned}
$$

The ORE is:

$$
\begin{aligned}
&\quad \frac{P[T, I | V, E]}{P[T, I | U, E]} \cdot \frac{P[E|V]}{P[E|U]} \cdot \frac{P[T | I', U]}{P[T | I', V]} \cdot \frac{P[I' | E, U] P[E | U] + P[E' | U]}{P[I' | E, V] P[E | V] + P[E' | V]} \\
&= \frac{P[T, I | V, E]}{P[T, I | U, E]} \cdot \frac{P[T | I', U]}{P[T | I', V]} \cdot \frac{P[I' | E, U] + \mathcal{O}[E' | U]}{P[I' | E, V] + \mathcal{O}[E' | V]} \\
\end{aligned}
$$

where $\mathcal{O}[\bullet]$ is odds.

The first fraction is the desired risk ratio. The second fraction represents test-negative rates. The last fraction shows that TND can be unbiased in two cases. Both require that the vaccinated and unvaccinated are equally likely to be exposed ($\mathcal{O}[E'|V] = \mathcal{O}[E'|V']$). First, if exposure is rare ($\mathcal{O}[E' | V'] \gg 1$), then the third fraction approaches unity. Second, and less plausible, if vaccination does not protect against infection (i.e., $P[I' | E, V] = P[I' | E, V]$), then the vaccinated are not at greater risk for the test-negative condition anyway.

## Logistic regression

### Simple case

In the simplest case, a logistic regression for TND has one predictor (vaccinated or not) and one outcome (positive or negative test result). It estimates the risk ratio of a positive test, given that a test occurred:

$$
\frac{P[I|T,V]}{P[I'|T,V]} = \exp\{\boldsymbol{\beta}_V \cdot \mathbf{X}\}
$$

where $\boldsymbol{\beta}_V = [1, 1]$, $X_0$ relates to the risk of a positive test in the absence of vaccination, and $X_0$ relates to the change in risk of a positive test due to vaccination. Similarly:

$$
\frac{P[I|T,U]}{P[I'|T,U]} = \exp\{\boldsymbol{\beta}_U \cdot \mathbf{X}\}
$$

where $\boldsymbol{\beta}_V = [1, 0]$.

Note that $P[I|T,V]/P[I'|T,V] = P[T,I|V]/P[T,I'|V]$, so we can relate the probability of a positive test conditioned on there being a test to the probability of a positive test not conditioned on testing. Thus:

$$
\begin{aligned}
\mathrm{ORE} &=
\frac{P[T,I|V]}{P[T|I',V]} \frac{P[T,I'|U]}{P[T|I|U]} \\
&= \frac{P[I|T,V]}{P[I'|T,V]} \left( \frac{P[I|T,U]}{P[I'|T,U]} \right)^{-1} \\
&= \exp\{ (\boldsymbol{\beta}_V - \boldsymbol{\beta}_U) \cdot \mathbf{X} \} \\
&= \exp\{ X_1 \}
\end{aligned}
$$

In other words, an exponentiated coefficient from the regression is the ORE, which predicts the VE risk ratio of interest.

### Multiple predictors

If there are multiple subpopulations $B_i$ that each have different risks of a positive test in the absence of vaccination and also have different vaccination rates. Then the traditional ORE has terms like:

$$
\frac{P[T,I|V]}{P[T,I'|V]} = \frac{\sum_i P[T,I|V,B_i] P[V|B_i] P[B_i]}{\sum_i P[T,I'|V,B_i] P[V|B_i] P[B_i]}
$$

which are not useful to us.

Instead, we assume that vaccination has the same relative effect in each population, so that

$$
\frac{P[T,I|V,B_i]}{P[T,I'|V,B_i]} \left( \frac{P[T,I|U,B_i]}{P[T,I'|U,B_i]} \right)^{-1}
$$

is the same for all $i$.

Then logistic regression with multiple predictors again delivers the quantity of interest.

### Example: Correlated vaccinations

When measuring VE for one vaccine (e.g., COVID-19) using a TND, if vaccination status for another vaccine (e.g., flu) is not stratified for in the analysis (i.e., as a predictor in the logistic regression), then the VE estimate will be biased downward.

As a concrete example, assume:

- 25% of people take both vaccine 1 and vaccine 2, and the remaining 75% of people take neither.
- 25% of pathogen 1-like symptoms are in fact caused by pathogen 2 and that vaccine 2 prevents pathogen 2 symptoms with 50% VE.
- In the absence of vaccine 2, the unvaccinated and those vaccinated with vaccine 1 would have the same test-negative rate.
- The true VE for vaccine 1 is 25% (i.e., its risk ratio is $\tfrac{3}{4}$).

We naively use TND to estimate VE for vaccine 1, without accounting for vaccine 2. Among those vaccinated with vaccine 1, vaccine 2 reduces the test-negative rate by $\tfrac{1}{4}\cdot\tfrac{1}{2} = \tfrac{1}{8} = 12.5\%$. This increases the ORE by $1 - \tfrac{1}{1/8} = \tfrac{8}{7}$, from $\tfrac{3}{4}$ to $\tfrac{6}{7}$. Then the estimate VE is $1-\tfrac{6}{7} \approx 14\%$, which is a substantial underestimate.
