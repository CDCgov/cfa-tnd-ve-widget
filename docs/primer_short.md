# Test-negative design: short primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination. For purposes of a test-negative design (TND) study, we further define VE to be:

- a direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program,
- protection against symptomatic disease that would lead to a diagnostic test, written $\mathrm{VE}_{SP}$ in [Halloran, Longini, and Struchiner](https://doi.org/10.1007/978-0-387-68636-3),
- conditioned on some probability or amount of exposure to disease, and
- binary, that is, individuals are considered vaccinated or not (e.g., people who were vaccinated shortly before the outcome of interest may be classified as "unvaccinated" in the study, because they are presumed to have not yet been protected).

## Test-negative design

A test-negative design (TND) is a study design that can be used to estimate VE. In a TND:

- The population of interest are those individuals who received a diagnostic test, usually becomes they develop some symptoms, seek a test, and qualify for that test.
- The main covariate of interest is vaccination status.
- The outcome of interest is the test result (positive or negative).

The data available in a TND ultimately reduces to a 2x2 table of counts:

|               | Vaccinated | Unvaccinated |
| ------------- | ---------- | ------------ |
| Test positive | $C_{VP}$   | $C_{UP}$     |
| Test negative | $C_{VN}$   | $C_{UN}$     |

## Mathematical model

### Single-exposure model

- Individuals are vaccinated ($V$) with probability $v$, or unvaccinated ($U$)
  - Here we assume perfect reporting about vaccine status; i.e., there is no one who is actually vaccinated who appears in the "not vaccinated" arm, nor vice versa
- Each individual has the possibility of becoming exposed $E$, and then has further conditional probabilities of becoming symptomatically infected $S_I$, and then tested $T_I$
  - Conditional probabilities depend on vaccination status. E.g., the probability that a vaccinated person will receive a test is $P[E|V] \times P[S_I|E,V] \times P[T_I|S_I,V]$.
  - There is only one opportunity for exposure per individual. Thus, this form of the model does not distinguish between all-or-nothing or leaky vaccine efficacy.
  - The $S \to T$ transitions represent a combination of seeking healthcare and then qualifying to receive a test.
- Every individual also has an independent probability to develop symptoms $S_X$ for reasons unrelated to infection with the pathogen of interest, and then a conditional probability to become tested $T_X$.
  - E.g., the probability that a vaccinated person will seek a test for reasons unrelated to infection is $P[T_X|S_X,V] \times P[S_X|V]$.
- Testing
  - People who receive tests are either positive ($P$) or negative ($N$).
  - The test has sensitivity $p_\mathrm{sens}$ and specificity $p_\mathrm{spec}$, such that, e.g.:
    - $P[P|T_I,V] = p_\mathrm{sens}$
    - $P[N|T_I,V] = 1 - p_\mathrm{sens}$
    - $P[N|T_X,V] = p_\mathrm{spec}$
  - We _a priori_ assume that test performance is unrelated to vaccination status, e.g., $P[P|T_I,V]=P[P|T_I,U]$.

#### Quantity of interest

We are interested in protection against symptomatic disease, conditioned on exposure:

```math
\mathrm{VE}_{SP} = 1 - \frac{P[S_I|E,V]}{P[S_I|E,U]}
```

#### Measured quantities

The expected values of the numbers of tested individuals, stratified by caused of symptoms (infected $I$ or not $X$) and vaccination status, are:

```math
\begin{align*}
\mathbb{E}[C_{VI}] &= n v \times P[T_I | S_I,V] \times P[S_I|E,V] \times P[E|V] \\
\mathbb{E}[C_{VX}] &= n v \times P[T_X|S_X,V] \times P[S_X|V] \\
\end{align*}
```

and similarly for $U$.

The actual values from the TND trial (i.e., counts of positive $P$ and negative $N$ tests) are affected by test performance:

```math
\begin{align*}
\mathbb{E}[C_{VP}] &= p_\mathrm{sens} \mathbb{E}[C_{VI}] + (1 - p_\mathrm{spec}) \mathbb{E}[C_{VX}] \\
\mathbb{E}[C_{VN}] &= (1 - p_\mathrm{sens}) \mathbb{E}[C_{VI}] + p_\mathrm{spec} \mathbb{E}[C_{VX}] \\
\end{align*}
```

and similarly for $U$.

#### Estimator

An estimator of the quantity of interest is:

```math
\hat{\mathrm{VE}} = 1 - \frac{C_{VP} C_{UN}}{C_{UP} C_{VN}}
```

_Proposition 1_. If the conditional probability of testing given symptoms does not depend on the cause of symptoms, but can depend on vaccination status (i.e., vaccinated people seek testing for symptoms with a single probability, regardless of the cause of the symptoms), such that $P[T_I|S_I,V] = P[T_X|S_X,V]$ and $P[T_I|S_I,U] = P[T_X|S_X,U]$, then the conditional probabilities of testing do not affect the estimator.

_Proof_. Write the two resulting probabilities as $P[T|V]$ and $P[T|U]$. Note that $P[T|V]$ appears in both $\mathbb{E}[C_{VI}]$ and $\mathbb{E}[C_{VX}]$ and thus factors out in both $\mathbb{E}[C_{VP}]$ and $\mathbb{E}[C_{VN}]$, and then cancels out in $\hat{\mathrm{VE}}$. The same is true for $P[T|U]$.

_Proposition 2_. This estimator is unbiased if:

1. the conditional probability of testing does not depend on the cause of symptoms,
2. non-infection symptoms arise with equal probability regardless of vaccination status, i.e., $P[S_X|V] = P[S_X|U]$,
3. the test has perfect sensitivity and specificity, such that, e.g., $C_{VP} = C_{VI}$, and
4. the probability of exposure is identical among the vaccinated and unvaccinated, i.e., $P[E|V] = P[E|U]$.

_Proof_. By the previous proposition, the first assumption lets us drop the testing probabilities. Under the assumption of perfect performance, we can replace the test results with actual infection status (e.g., $C_{VP} \to C_{VI}$) so that the expected value of the estimator simplifies to:

$$
\mathbb{E}\left[\hat{\mathrm{VE}}\right] = 1 -
  \frac{P[S_I|E,V] \times P[E|V] \times P[S_X|U]}{P[S_I|E,U] \times P[E|U] \times P[S_X|V]}
$$

Under the assumption of equal exposure rates, the two $P[E|\cdot]$ terms cancel. Under the assumption of equal non-infection symptom probability, the two $P[S_X|\cdot]$ terms cancel. Thus:

$$
\mathbb{E}\left[\hat{\mathrm{VE}}\right]
  = 1 - \frac{P[S_I|E,V]}{P[S_I|E,U]}
$$

## Single-exposure, no-repeat requires rare disease limit to be unbiased

Individuals are either vaccinated $V$ or unvaccinated $V'$. At one moment, all people potentially eligible for inclusion in the TND are exposed $E$ or not $E'$. The exposed can become infected $I$ or not $I'$. All the infected were exposed (i.e., $I \subset E$), and equivalent the unexposed are all uninfected ($E' \subset I'$). Individuals --whether unexposed, exposed and uninfected, or infected-- can become tested $T$, but each individual can be tested only once. Assume perfect test sensitivity.

We consider each counted population in turn. $C_{VI}$ are the individuals who are vaccinated, infected, and tested:

$$
\begin{align*}
C_{VI} &\propto P[T, I, V] \\
&= P[T, I, E, V] + P[T, I, E', V] \\
&= P[T, I, E, V] \quad \text{since } I \subset E\\
&= P[T, I | V, E] P[E | V] P[V]
\end{align*}
$$

The derivation for $C_{V'I}$ is equivalent; just replace $V \to V'$.

The uninfected term is more complicated, since we need to keep the partition into $E$ and $E'$:

$$
\begin{align*}
C_{VI'} &\propto P[T, I', V] \\
&= P[T | I', V] P[I' | V] P[V] \\
&= P[T | I', V] \left( P[I', E | V] + P[I', E' | V] \right) P[V] \\
&= P[T | I', V] \left( P[I' | E, V] P[E | V] + P[E' | V] \right) P[V] \quad \text{since } E' \subset I'\\
\end{align*}
$$

The quantity of interest is:

$$
\begin{align*}
\frac{C_{VI} C_{V'I'}}{C_{V'I} C_{VI'}}
&= \frac{P[T, I | V, E]}{P[T, I | V', E]} \cdot \frac{P[E|V]}{P[E|V']} \cdot \frac{P[T | I', V']}{P[T | I', V]} \cdot \frac{P[I' | E, V'] P[E | V'] + P[E' | V']}{P[I' | E, V] P[E | V] + P[E' | V]} \\
&= \frac{P[T, I | V, E]}{P[T, I | V', E]} \cdot \frac{P[T | I', V']}{P[T | I', V]} \cdot \frac{P[I' | E, V'] + \mathcal{O}[E' | V']}{P[I' | E, V] + \mathcal{O}[E' | V]} \\
\end{align*}
$$

where $\mathcal{O}[\bullet]$ is odds.

The first fraction is the what we want to estimate: the protection due to vaccination against both infection and qualifying for a test, given exposure.

The second fraction represents symptom severity and testing behavior among the uninfected. For an unbiased estimate, the same proportion of uninfected vaccinated and of uninfected unvaccinated must seek a test. If the vaccinated are more likely to seek and receive a test (i.e., $P[T|I',V]>P[T|I',V']$), then the TND underestimates VE.

The last fraction represents the intertwined biases. If vaccination does not protect against infection (i.e., $P[I' | E, V] = P[I' | E, V]$) and the vaccinated and unvaccinated are equally likely to be exposed ($\mathcal{O}[E'|V] = \mathcal{O}[E'|V']$), then TND can be unbiased. If both vaccination protects against infection (i.e., $P[I' | E, V] > P[I' | E, V]$) and also the vaccinated are _less_ likely to be exposed ($\mathcal{O}[E'|V] > \mathcal{O}[E'|V']$) then TND underestimates VE. However, in the case of equal exposure rates ($\mathcal{O}[E'|V] = \mathcal{O}[E'|V']$), and in the limit of rare disease ($\mathcal{O}[E' | V'] \gg P[I' | E, V']$), then this fraction also approaches unity.

## Stratifying by symptoms

Naive derivations of the TND assume that individuals can have symptoms or not, i.e., there is a dichotomous "symptomatic" status. One can then derive statements like: "if non-infection symptoms arise with equal probability regardless of vaccination status, but we allow the vaccinated and unvaccinated can seek tests for symptoms at different rates, then that test-seeking rate need not be equal for an unbiased estimate."

These kinds of arguments confound "symptoms" and test-seeking behavior. Because we never observe what happens when a person with vaccinated-like test-seeking behavior has the kinds of symptoms that arise among the unvaccinated infected, it's unclear what is means to assume a single category of "symptoms."

Instead, allow there to be a set of symptom states $\{ S_i \}$. This set can be very large; it need not just be "cough" or "102 F fever" but could instead include, say, a whole universe of types of coughs.

In practice, receiving a test will be predicated on some set of symptoms, since only people with certain symptoms may be eligible to receive a test or to be included in the study. We need not be concerned with that; we can consider probabilities like $P[T | S_i, V]$ to include both the probability that a vaccinated person with symptoms $S_i$ will seek a test and also that they will qualify to receive a test.

The derivation is similar to the one above, only now we stratify based on exposure and symptoms:

$$
C_{VI} \propto P[T, I, V] = \sum_i P[T, I, S_i, V]
$$

We assert that the probability of testing depends only on symptoms and vaccination, that is, that testing and infection status are conditionally independent given symptoms:

$$
P[T | I, S_i, V] = P[T | S_i, V] \text{ or, equivalent } P[T, I | S_i, V] = P[T | S_i, V] P[I | S_i, V]
$$
