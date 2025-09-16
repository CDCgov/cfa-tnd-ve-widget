# Test-negative design: short primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination, that is $\mathrm{VE} = 1 - \mathrm{RR}$ for some risk ratio RR. For purposes of a test-negative design (TND) study, we further define VE to be:

- a direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program,
- protection against both infection and progression to symptoms that would lead to a diagnostic test, written $\mathrm{VE}_{SP}$ in [Halloran, Longini, and Struchiner](https://doi.org/10.1007/978-0-387-68636-3),
- conditioned on (some amount of exposure) to disease, and
- binary, that is, individuals are considered vaccinated or not (e.g., people who were vaccinated shortly before the outcome of interest may be classified as "unvaccinated" in the study, because they are presumed to have not yet been protected).

## TND with independent test-positive and test-negative condition rates

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
&= \mathrm{RR} \cdot \frac{\lambda^{T-}_U}{\lambda^{T-}_V}
\end{aligned}
$$

Thus, so long as the vaccinated and unvaccinated are tested for test-negative conditions at the same rate, then the TND odds ratio is an unbiased estimator of the relevant VE risk ratio (subject also the requirement that rates be nonzero and in the limit of large populations).

where $T_I$ is the event that a person is tested, in the presence of infection, and the test was "for" the infection (i.e., it wasn't the person's second, non-infection test).

**TO DO: Rewrite VE=1-RR, and then talk about the OR as an estimator of the OR, in the limit of N->infty.**

We consider the estimator:

$$
\hat{\mathrm{VE}}_{SP} \equiv 1 - \frac{C_{IV} C_{I'V'}}{C_{IV'} C_{I'V}}
$$

In the limit of a large study, this ratio of counts approaches the ratios of its expected values:

$$
\lim_{N \to \infty} \left(1 - \mathbb{E}\left[\hat{\mathrm{VE}}_{SP}\right]\right) = \frac{\mathbb{E}[C_{IV}] \mathbb{E}[C_{I'V'}]}{\mathbb{E}[C_{IV'}] \mathbb{E}[C_{I'V}]}
$$

Consider each of the $\mathbb{E}[C_\bullet]$ terms in turn:

$$
\begin{gathered}
\mathbb{E}[C_{IV}] \propto P[T_I, V] = P[T_I | E, V] P[E|V] P[V] \\
\mathbb{E}[C_{I'V}] \propto P[T_{I'}, V] = P[T_{I'} | V] P[V]
\end{gathered}
$$

where $T_{I'}$ represents the non-infection test.

The derivations for the $V'$ are equivalent, replacing $V \to V'$. Thus, the quantity of interest is:

$$
\frac{\mathbb{E}[C_{IV}] \mathbb{E}[C_{I'V'}]}{\mathbb{E}[C_{IV'}] \mathbb{E}[C_{I'V}]}
= \frac{P[T_I | E, V]}{P[T_I | E, V']}
\cdot \frac{P[E|V]}{P[E|V']}
\cdot \frac{P[T_{I'}|V']}{P[T_{I'}|V]}
$$

- The first ratio is the risk reducation from $\mathrm{VE}_{SP}$, conditioned on exposure.
- The second ratio shows that, if the vaccinated are exposed at a greater rate, then TND can underestimate VE.
- The third ratio shows that, if the vaccinated are more likely to be tested for non-infection causes, then TND can overestimate VE.

If we assume equal exposure and equal non-infection testing rates, then TND will be unbiased.

## Single-exposure, no-repeat requires rare disease limit to be unbiased

The assumption about the two, unrelated tests was awkward. The assumption that the second test would always be negative was even worse. Instead, assume that each individual is one of unexposed, exposed and uninfected, or infected, and can become tested $T$, but each individual can be tested only once. Assume perfect test sensitivity.

Now we define the relevant risk ratio as:

$$
\frac{P[T, I | E, V]}{P[T, I | E, V']}
$$

Thus:

$$
\begin{aligned}
\mathbb{E}[C_{VI}] &\propto P[T, I, V] \\
&= P[T, I, E, V] \quad \text{since } I \subset E\\
&= P[T, I | V, E] P[E | V] P[V]
\end{aligned}
$$

The uninfected term is more complicated, since we need to partition the uninfected into the exposed but infected versus the unexposed $I' = (I' \cap E) \cup E'$:

$$
\begin{aligned}
C_{VI'} &\propto P[T, I', V] \\
&= P[T | I', V] P[I' | V] P[V] \\
&= P[T | I', V] \left( P[I', E | V] + P[E' | V] \right) P[V] \\
&= P[T | I', V] \left( P[I' | E, V] P[E | V] + P[E' | V] \right) P[V] \\
\end{aligned}
$$

The quantity of interest is:

$$
\begin{aligned}
\frac{\mathbb{E}[C_{IV}] \mathbb{E}[C_{I'V'}]}{\mathbb{E}[C_{IV'}] \mathbb{E}[C_{I'V}]}
&= \frac{P[T, I | V, E]}{P[T, I | V', E]} \cdot \frac{P[E|V]}{P[E|V']} \cdot \frac{P[T | I', V']}{P[T | I', V]} \cdot \frac{P[I' | E, V'] P[E | V'] + P[E' | V']}{P[I' | E, V] P[E | V] + P[E' | V]} \\
&= \frac{P[T, I | V, E]}{P[T, I | V', E]} \cdot \frac{P[T | I', V']}{P[T | I', V]} \cdot \frac{P[I' | E, V'] + \mathcal{O}[E' | V']}{P[I' | E, V] + \mathcal{O}[E' | V]} \\
\end{aligned}
$$

where $\mathcal{O}[\bullet]$ is odds.

The first fraction is the desired risk ratio.

The second fraction represents testing rates among the uninfected. For an unbiased estimate, the same proportion of uninfected vaccinated and of uninfected unvaccinated must be tested. If the vaccinated are more likely to be tested (i.e., $P[T|I',V]>P[T|I',V']$), for example, because they are more likely to seek and receive a test, then the TND underestimates VE.

The last fraction represents two intertwined biases. If vaccination does not protect against infection (i.e., $P[I' | E, V] = P[I' | E, V]$) _and_ the vaccinated and unvaccinated are equally likely to be exposed ($\mathcal{O}[E'|V] = \mathcal{O}[E'|V']$), then TND can be unbiased. If both vaccination protects against infection (i.e., $P[I' | E, V] > P[I' | E, V]$) and also the vaccinated are _less_ likely to be exposed ($\mathcal{O}[E'|V] > \mathcal{O}[E'|V']$) then TND underestimates VE.

However, in the case of equal exposure rates ($\mathcal{O}[E'|V] = \mathcal{O}[E'|V']$), and in the limit of rare disease ($\mathcal{O}[E' | V'] \gg P[I' | E, V']$), then the third fraction also approaches unity. This approaches the situation above, where receiving a non-infection test is essentially independent of receiving a for-infection test.

## Stratifying by symptoms

Naive derivations of the TND assume that individuals can have symptoms or not, i.e., there is a dichotomous "symptomatic" status. One can then derive statements like: "if non-infection symptoms arise with equal probability regardless of vaccination status, but we allow the vaccinated and unvaccinated can seek tests for symptoms at different rates, then that test-seeking rate need not be equal for an unbiased estimate."

These kinds of arguments confound "symptoms" and test-seeking behavior. Because we never observe what happens when a person with vaccinated-like test-seeking behavior has the kinds of symptoms that arise among the unvaccinated infected, it's unclear what is means to assume a single category of "symptoms."

Instead, allow there to be a set of disjoint symptom states $\{ S_i \}$. This set can be very large; it need not just be "cough" or "102 degree fever" but could instead include, say, a whole universe of types of coughs.

In practice, receiving a test will be predicated on some set of symptoms, since only people with certain symptoms may be eligible to receive a test or to be included in the study. We need not be concerned with that; we can consider probabilities like $P[T | S_i, V]$ to include both the probability that a vaccinated person with symptoms $S_i$ will seek a test and also that they will qualify to receive a test.

Now the risk ratio of interest is:

$$
\frac{P[S | E, V]}{P[S | E, V']} = \frac{\sum_i P[S_i | E, V]}{\sum_i P[S_i | E, V']}
$$

where $S = \bigcup_i S_i$ is the event that a person has any symptoms.

The derivation is similar to the one above, but more involved because we stratify based on exposure and symptoms:

$$
\begin{aligned}
\mathbb{E}[C_{VI}] &\propto P[T, I, V] \\
&= \sum_i P[T, I, S_i, V] \\
&= \sum_i P[T | I, S_i, V] P[I, S_i, V]
\end{aligned}
$$

We now make two assertion about conditional independence. First, the probability of testing depends only on symptoms and vaccination (i.e., testing and infection status are conditionally independent given symptoms):

$$
P[T | I, S_i, V] = P[T | S_i, V]
$$

Second, that symptoms depend on infection status and not exposure (i.e., symptoms and infection are conditionally independent given exposure):

$$
P[S_i | I, E, V] = P[S_i | I, V] \implies P[S_i, I | E, V] = P[S_i | E, V] P[I | E, V]
$$

Thus:

$$
\begin{aligned}
\mathbb{E}[C_{VI}] &\propto \sum_i P[T | I, S_i, V] P[I, S_i, V] \\
&= \sum_i P[T | S_i, V] P[I, S_i, E, V] \\
&= \sum_i P[T | S_i, V] P[I, S_i | E, V] P[E, V] \\
&= \sum_i P[T | S_i, V] P[I | E, V] P[S_i | E, V] P[E|V] P[V] \\
\end{aligned}
$$

The first probability represents testing behavior conditioned on symptoms. The second is about infection rates (and how the vaccine protects against infection). The third is the term of interest for the VE risk ratio. The last two terms are typical.

For the uninfected, we need to partition into exposed and unexposed, but we don't need to do the convoluted work to get $P[S_i | E, V]$:

$$
\begin{aligned}
\mathbb{E}[C_{VI'}] &\propto P[T, I', V] \\
&= \sum_i P[T, I', S_i, V] \\
&= \sum_i P[T | S_i, V] P[I', S_i, V] \\
&= \sum_i P[T | S_i, V] P[S_i | I', V] P[I', V] \\
&= \sum_i P[T | S_i, V] P[S_i | I', V] \left( P[I', E, V] + P[I', E', V] \right) \\
&= \sum_i P[T | S_i, V] P[S_i | I', V] \left( P[I'|E, V]P[E|V] + P[E'|V] \right) P[V] \\
\end{aligned}
$$

Some tedious algebra shows that the odds ratio is:

$$
\frac{\sum_i P[T|S_i,V] P[S_i|E,V]}{\sum_i P[T|S_i,V'] P[S_i|E,V']}
\cdot \frac{P[I|E,V]}{P[I|E,V']}
\cdot \frac{\sum_i P[T_i|S_i,V'] P[S_i|I',V']}{\sum_i P[T_i|S_i,V] P[S_i|I',V]}
\cdot
\frac{P[I'|E,V'] + \mathcal{O}[E'|V']}{P[I'|E,V] + \mathcal{O}[E'|V]}
$$

**TO DO: Retry, but avoiding the collision problem; i.e., allow each person to be tested twice. But this doesn't look promising.**

With the two independent test assumption, we get something like:

$$
\frac{\sum_i P[T^+|S^+_i,V] P[S^+_i|V]}{\sum_i P[T^+|S^+_i,V'] P[S^+_i|V']}
\cdot \frac{\sum_i P[T^-|S^-_i,V'] P[S^-_i|V']}{\sum_i P[T^-|S^-_i,V] P[S^-_i|V]}
$$

Even if we assume that vaccination doesn't affect test-negative symptoms $P[S_i^-|V] = P[S_i^-|V'] = P[S_i^-]$, and that the testing rate does not depend on origin $P[T^+|S_i^+,V] = P[T^-|S_i^-,V] = P[T|S_i,V]$ and similarly for $V'$, then we have:

$$
\frac{\sum_i P[T|S_i,V] P[S^+_i|V]}{\sum_i P[T|S_i,V'] P[S^+_i|V']}
\cdot \frac{\sum_i P[T|S_i,V'] P[S_i^-]}{\sum_i P[T|S_i,V] P[S^-_i]}
$$

which does not, in general, simplify to anything.

**TO DO: Show how removing test-negative assumption gets to cross-vaccine protection.**

Simplify to four symptom types:

1. those that no one tests for,
2. those that only the vaccinated test for,
3. those that only the unvaccinated test for, and
4. those that everyone tests for.

Then we get:

$$
\frac{P[S_1^+|V] + P[S_3^+|V]}{P[S_2^+|V'] + P[S_3^+|V']} \cdot \frac{P[S_2^-] + P[S_3^-]}{P[S_1^-] + P[S_3^-]}
$$

In general, this doesn't work.
