# Test-negative design: short primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination, that is $\mathrm{VE} = 1 - \mathrm{RR}$ for some risk ratio RR. For purposes of a test-negative design (TND) study, we further define VE to be:

- a direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program,
- protection against both infection and progression to symptoms that would lead to a diagnostic test, written $\mathrm{VE}_{SP}$ in [Halloran, Longini, and Struchiner](https://doi.org/10.1007/978-0-387-68636-3),
- conditioned on (some amount of exposure) to disease, and
- binary, that is, individuals are considered vaccinated or not (e.g., people who were vaccinated shortly before the outcome of interest may be classified as "unvaccinated" in the study, because they are presumed to have not yet been protected).

## TND with independent test-positive and test-negative condition rates

**Proposition: Unbiased TND requires large counts.**

In the simplest derivation, we assume that:

- Test performance is perfect.
- There is some population of $n_V$ vaccinated individuals and $n_U$ unvaccinated individuals that are _a priori_ eligible for inclusion in the TND.
- Testing is a Poisson process. Each vaccinated individual receives tests for the test-positive condition at rate $\lambda^{T+}_V$ and for the test-negative condition at rate $\lambda^{T-}_V$.
- Unvaccinated individuals receive tests at analogous rates $\lambda^{T+}_U$ and $\lambda^{T-}_U$.

Note that this means that we assume there are no "collisions" between test-positive and test-negative conditions. An individual could theoretically test positive and then test negative one millisecond later.

The data available are a 2x2 table of counts of test results:

|               | Vaccinated | Unvaccinated |
| ------------- | ---------- | ------------ |
| Test positive | $X^+_V$    | $X^+_U$      |
| Test negative | $X^-_V$    | $X^-_U$      |

We are interested in the protection provided by the vaccine. In this model, where there are only test-positive and -negative conditions, we are interested in the risk ratio:

$$
\mathrm{RR} = \frac{\lambda^{T+}_V}{\lambda^{T+}_U}
$$

Consider the odds ratio as an estimator for the risk ratio:

$$
\hat{\mathrm{RR}} = \frac{X^+_V X^-_U}{X^-_V X^+_U}
$$

Because the counts of tests from each person is an i.i.d.Poisson distribution, the total counts of tests are themselves Poisson distributed:

$$
X^+_V \sim \mathrm{Poisson}(n_V \lambda^{T+}_V D)
$$

where $D$ is the duration of the trial. These variables are all independent, so

$$
\mathbb{E}\left[\hat{\mathrm{RR}}\right] = \mathbb{E}[X_V^+] \cdot \mathbb{E}\left[ \frac{1}{X_V^-} \right] \cdot \mathbb{E}[X_U^-] \cdot \mathbb{E}\left[ \frac{1}{X_U^+} \right]
$$

If $X \sim \mathrm{Poisson}(\lambda)$, then $\mathbb{E}[X] = \lambda$. It is generally not the case that $\mathbb{E}[1/X] = 1/\lambda$ (consider, e.g., $X=0$), but $\lim_{\lambda \to \infty} E[1/X | X > 0] = 1/\lambda$. Therefore, so long as all rates are nonzero:

$$
\begin{aligned}
\lim_{n_V, n_U \to \infty} \mathbb{E}\left[\hat{\mathrm{RR}}\right]
&= \frac{\mathbb{E}[X_V^+] \mathbb{E}[X_U^-]}{\mathbb{E}[X_V^-] \mathbb{E}[X_U^+]} \\
&= \frac{n_V \lambda^{T+}_V D \cdot n_U \lambda^{T-}_U D}{ n_U \lambda^{T-}_V D \cdot n_V \lambda^{T+}_U D} \\
&= \frac{\lambda^{T+}_V}{\lambda^{T+}_U} \cdot \frac{\lambda^{T-}_U}{\lambda^{T-}_V}
\end{aligned}
$$

Call this the "odds ratio of expectations" (ORE).

<!-- TO DO: Better name? -->

In this model:

$$
\mathrm{ORE} = \mathrm{RR} \cdot \frac{\lambda^{T-}_U}{\lambda^{T-}_V}
$$

Thus, so long as the vaccinated and unvaccinated are tested for test-negative conditions at the same rate, then the TND odds ratio is an unbiased estimator of the relevant VE risk ratio (subject also the requirement that rates be nonzero and in the limit of large populations).

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

## Conditioning on symptoms

**Proposition: TND does not account for testing behavior.**

It is commonly held that TNDs mitigate biases due to differences in testing behavior between the vaccinated and unvaccinated. This cannot be generally true: if symptoms information is not part of the analysis, then for the purposes of analysis, testing behavior and disease progression are perfectly confounded. We cannot distinguish how the vaccine reduces symptoms versus how the vaccinated and unvaccinated seek rates at different rates for different symptoms.

Here we show a general treatment, a specific counterexample, and then follow the derivation that can be erroneously interpreted as proof that TND accounts for testing behavior.

### General derivation

Consider a set of disjoint symptom statuses $\{ S_i \}$. This set can be very large: it need not reference crude categories like "symptomatic" vs. not, or "cough" and "fever," but instead includes a whole universe of types of coughs, fevers, chills, etc.

We emphasize that these statuses are _disjoint_. Every person has is in exactly one symptom state. So if you consider only cough and fever, then you need states like "no symptoms," "cough and not fever," "fever and not cough," and "both cough and fever." The symptom states form a partition, so for every event $X$, we have $P[X] = \sum_i P[X, S_i]$.

These symptoms will determine the probability that a person seeks a test and the probability that, having sought a test, they will receive it (since, in practice, the TND will have some inclusion/exclusion criteria related to symptoms). We do not separately observe test-seeking and test-receiving, so we consider probabilities like $P[T | S_i, V]$ that encapsulate both processes.

Now the positive test rate is:

$$
\begin{aligned}
\lambda^{T+}_V &= P[T,I|E,V] \cdot \lambda^E_V \\
&= \sum_i P[T,S_i,I|E,V] \cdot \lambda^E_V \\
&= \sum_i P[T|S_i,I,E,V] P[S_i,I|E,V] \cdot \lambda^E_V
\end{aligned}
$$

Note that $E \cap I = I$, so that $P[T|S_i,I,E,V] = P[T|S_i,I,V]$. Assume that the probability of testing depends only on symptoms and vaccination (i.e., testing and infection status are conditionally independent given symptoms) so that $P[T|S_i,I,V] = P[T|S_i,V]$. Similarly, $P[S_i,I|E,V] = P[S_i|I,V] P[I|E,V]$. Thus:

$$
\lambda^{T+}_V = \sum_i P[T|S_i,V] \cdot P[S_i|I,V] \cdot P[I|E,V] \cdot \lambda^E_V
$$

We similarly stratify the test-negative rate by symptom statuses:

$$
\lambda^{T-}_V = \sum_i P[T|S_i,V] \lambda^{S_i-}_V
$$

where $\lambda^{S_i-}_V$ is the rate at which symptom status $i$ arises due to test-negative conditions among the vaccinated.

Thus, the ORE is:

$$
\frac{\sum_i P[T|S_i,V] P[S_i|I,V]}{\sum_i P[T|S_i,U] P[S_i|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{\lambda^E_V}{\lambda^E_U}
\cdot \frac{\sum_i P[T|S_i,U] \lambda^{S_i-}_U}{\sum_i P[T|S_i,V] \lambda^{S_i-}_V}
$$

The first fraction is relative risk of a seeking and receiving a positive test, given infection, in the vaccinated relative to the unvaccinated. The second fraction is the relative risk of infection given exposure. The third fraction is the relative rate of exposure. The fourth fraction is the relative risk of seeking and receiving a negative test.

This ORE does not reduce, even under some simplifying assumptions. For example, even if:

- both groups are exposed at the same rate $\lambda^E_V = \lambda^E_U$,
- the probability of testing depends on symptoms and not vaccination status $P[T|S_i,V]=P[T|S_i|U]=P[T|S_i]$, and
- the test-negative conditions arise at the same rate $\lambda_V^{S_i-} = \lambda_U^{S_i-}$,

then the third and fourth fractions cancel, and the ORE reduces to

$$
\frac{\sum_i P[T|S_i] P[S_i|I,V]}{\sum_i P[T|S_i] P[S_i|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
$$

We could further assume that the vaccine has no effect on symptoms, so that $P[S_i|I,V] = P[S_i|I,U]$, in which case the TND estimates $\mathrm{VE}_S$ via the risk ratio $P[I|E,V]/P[I|E,U]$, but this is counterproductive, since we are in fact trying to understand the role of symptoms in testing.

### Dichotomous symptoms

To see where the erroneous conclusion can come from, assume that individuals are symptomatic $S_1$ or not $S_0$, and the asymptomatic do not seek tests so that $P[T|S_0,V]=P[T|S_0,U]=0$. Then the ORE reduces to:

$$
\frac{P[T|S_1,V] P[S_1|I,V]}{P[T|S_1,U] P[S_1|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{\lambda^E_V}{\lambda^E_U}
\cdot \frac{P[T|S_1,U] \lambda^{S_1-}_U}{P[T|S_1,V] \lambda^{S_1-}_V}
=
\frac{P[S_1|I,V]}{P[S_1|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{\lambda^E_V}{\lambda^E_U}
\cdot \frac{\lambda^{S_1-}_U}{\lambda^{S_1-}_V}
$$

in which case TND can deliver an unbiased estimate for $\mathrm{VE}_{SP}$.

In general, one cannot conclude that there is simply "symptomic" or "not."

### Counterexample

To see why TND cannot generally correct for test-seeking behavior, consider a simple case where there are 3 types of symptoms:

- 0: Neither the vaccinated not unvaccinated seek a test, so that $P[T|S_0,V]=P[T|S_0,U]=0$
- 1: Everyone seeks a test, with equal probability $P[T|S_1]$.
- 2: The vaccinated seek a test; the unvaccinated do not.

$$
\begin{aligned}
&\quad \frac{P[T|S_1] P[S_1|I] + P[T|S_2,V]P[S_2|I,V]}{P[T|S_1] P[S_1|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{\lambda^E_V}{\lambda^E_U}
\cdot \frac{P[T|S_1] \lambda^{S_1-}_U}{P[T|S_1] \lambda^{S_1-}_V + P[T|S_2,V] \lambda^{S_2-}_V} \\
&= \left(1 + \frac{P[T|S_2,V]P[S_2|I,V]}{P[T|S_1] P[S_1|I,U]} \right)
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{\lambda^E_V}{\lambda^E_U}
\cdot \left(1 + \frac{P[T|S_2,V] \lambda^{S_2-}_V}{P[T|S_1] \lambda^{S_1-}_U} \right)^{-1} \\
\end{aligned}
$$

To achieve an unbiased estimate, we must assume that $S_2$ is never tested for or never arises, that is, that we return to the single symptom status assumption.

### Logistic regression won't save this?

See logistic regression math below. Controlling for symptoms in the regression is equivalent to assuming that protection from vaccination is the same for each symptom status, that is, that

$$
\frac{P[T,I|V,S_i]}{P[T,I'|V,S_i]} \left( \frac{P[T,I|U,S_i]}{P[T,I'|U,S_i]} \right)^{-1}
$$

is the same for all $i$.

By the conditional independence assumption (testing depends on symptoms, not infection status), this simplifies to

$$
\frac{P[S_i|I,V]}{P[S_i|I',V]} \left( \frac{P[S_i|I,U]}{P[S_i|I',U]} \right)^{-1}
$$

Assume that, among the uninfected, vaccination status does not the probability of symptoms: $P[S_i|I',V]=P[S_i|I',U]$ so that this simplifies to

$$
\frac{P[S_i|I,V]}{P[S_i|I,U]}
$$

In other words, controlling for symptom status rescues from this bias only if vaccination protects against each kind of symptom equally, which is _a priori_ unlikely.

<!-- TO DO: Think about which symptom statuses we can merge together.  -->

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
