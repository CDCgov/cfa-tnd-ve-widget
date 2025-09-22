# TND does not account for symptoms in general

It is commonly held that TNDs mitigate biases due to differences in testing behavior between the vaccinated and unvaccinated. This cannot be generally true: if symptoms information is not part of the analysis, then for the purposes of analysis, testing behavior and disease progression are perfectly confounded. We cannot distinguish how the vaccine reduces symptoms versus how the vaccinated and unvaccinated seek rates at different rates for different symptoms.

Here we show a general treatment, a specific counterexample, and then follow the derivation that can be erroneously interpreted as proof that TND accounts for testing behavior.

## Defining symptom statuses

Consider a set of disjoint symptom statuses $\{ S_i \}$. This set can be very large: it need not be binary ("symptomatic" vs. not) or even consist of a small number of symptoms like "cough" and "fever" but instead can include a whole universe of types of coughs, fevers, chills, etc. The derivation will hold for any countably infinite set of symptom states, so one can essentially even imagine a smooth continuum of symptom severities.

These statuses are _disjoint_. Every person has is in exactly one symptom state (including a "no symptoms" state). So if you consider only cough and fever, then you need states like "no symptoms," "cough and not fever," "fever and not cough," and "both cough and fever." The symptom states form a partition, so for every event $X$, we have $P[X] = \sum_i P[X, S_i]$.

Although the universe of symptom states can be very large, under certain assumptions made below, two symptom statuses $S_i$ and $S_j$ can be merged into one if:

- they are tested for at the same rate; i.e., $P[T|S_i,V]=P[T|S_j,V]$ and $P[T|S_i,U]=P[T|S_j,U]$ and
- the emerge at the same rate among the infected; i.e., $P[S_i|I,V]=P[S_j|I,V]$ and $P[S_i|I,U]=P[S_j|I,U]$, and
- the emerge at the same rate among the uninfected; i.e., $P[S_i|I',V]=P[S_j|I',V]$ and $P[S_i|I',U]=P[S_j|I',U]$.

## General derivation

These symptoms will determine the probability that a person seeks a test and the probability that, having sought a test, they will receive it (since, in practice, the TND will have some inclusion/exclusion criteria related to symptoms). We do not separately observe test-seeking and test-receiving, so we consider probabilities like $P[T | S_i, V]$ that encapsulate both processes.

Now each vaccinated individual's expected number $x^{T+}_V$ of positive tests is related to their expected number $x^E_V$ of exposures and the probability of a positive test given exposure:

$$
\begin{aligned}
x^{T+}_V &= P[T,I|E,V] \cdot x^E_V \\
&= \sum_i P[T,S_i,I|E,V] \cdot x^E_V \\
&= \sum_i P[T|S_i,I,E,V] \cdot P[S_i,I|E,V] \cdot x^E_V
\end{aligned}
$$

Note that $E \cap I = I$, so that $P[T|S_i,I,E,V] = P[T|S_i,I,V]$. Assume that the probability of testing depends only on symptoms and vaccination (i.e., testing and infection status are conditionally independent given symptoms) so that $P[T|S_i,I,V] = P[T|S_i,V]$. Similarly, $P[S_i,I|E,V] = P[S_i|I,V] P[I|E,V]$. Thus:

$$
x^{T+}_V = \sum_i P[T|S_i,V] \cdot P[S_i|I,V] \cdot P[I|E,V] \cdot x^E_V
$$

We similarly stratify the test-negative rate by symptom statuses:

$$
x^{T-}_V = \sum_i P[T|S_i,V] x^{S_i-}_V
$$

where $x^{S_i-}_V$ is the average number of times a vaccinated individual suffers symptom status $i$ due to test-negative conditions.

Thus, the ORE is:

$$
\frac{\sum_i P[T|S_i,V] P[S_i|I,V]}{\sum_i P[T|S_i,U] P[S_i|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{x^E_V}{x^E_U}
\cdot \frac{\sum_i P[T|S_i,U] x^{S_i-}_U}{\sum_i P[T|S_i,V] x^{S_i-}_V}
$$

The first fraction is relative risk of a seeking and receiving a positive test, given infection, in the vaccinated relative to the unvaccinated. The second fraction is the relative risk of infection given exposure. The third fraction is the relative rate of exposure. The fourth fraction is the relative risk of seeking and receiving a negative test.

This ORE does not reduce, even under some simplifying assumptions. For example, even if:

- both groups have the same average number of exposures $x^E_V = x^E_U$,
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
\cdot \frac{x^E_V}{x^E_U}
\cdot \frac{P[T|S_1,U] x^{S_1-}_U}{P[T|S_1,V] x^{S_1-}_V}
=
\frac{P[S_1|I,V]}{P[S_1|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{x^E_V}{x^E_U}
\cdot \frac{x^{S_1-}_U}{x^{S_1-}_V}
$$

in which case TND can deliver an unbiased estimate for $\mathrm{VE}_{SP}$.

In general, one cannot conclude that there is simply "symptomic" or "not."

### Counterexample

To see why TND cannot generally correct for test-seeking behavior, consider a simple case where there are 3 types of symptoms:

- 0: Neither the vaccinated nor unvaccinated seek a test, so that $P[T|S_0,V]=P[T|S_0,U]=0$
- 1: Everyone seeks a test, with equal probability $P[T|S_1]$.
- 2: The vaccinated seek a test; the unvaccinated do not.

$$
\begin{aligned}
&\quad \frac{P[T|S_1] P[S_1|I] + P[T|S_2,V]P[S_2|I,V]}{P[T|S_1] P[S_1|I,U]}
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{x^E_V}{x^E_U}
\cdot \frac{P[T|S_1] x^{S_1-}_U}{P[T|S_1] x^{S_1-}_V + P[T|S_2,V] x^{S_2-}_V} \\
&= \left(1 + \frac{P[T|S_2,V]P[S_2|I,V]}{P[T|S_1] P[S_1|I,U]} \right)
\cdot \frac{P[I|E,V]}{P[I|E,U]}
\cdot \frac{x^E_V}{x^E_U}
\cdot \left(1 + \frac{P[T|S_2,V] x^{S_2-}_V}{P[T|S_1] x^{S_1-}_U} \right)^{-1} \\
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
