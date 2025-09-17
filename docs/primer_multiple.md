# Test-negative design with multiple outcomes

## Vaccine efficacy

Make the same assumptions as in the [short primer](primer_short.md).

## Test-negative design with multiple types of exposure and outcome

In a typical TND, there is one primary covariate of interest (vaccinated or not) and a single dichotomous outcome (test positive or negative). Variations on that main covariate of interest (e.g., vaccinated during some time window) are analyzed by running separate analyses with different values.

Here we generalize to allow for multiple vaccination states (e.g., vaccinated with one or more vaccines, or vaccinated in different time windows) and multiple test outcomes (e.g., each admitted person is subject to a panel of tests that return positive or negative for multiple pathogens.)

Let there be $N$ people in the population who could be admitted into the trail. For each person $i$, we know $A_i$, whether this person is admitted to the trial (e.g., has qualifying symptoms, seeks care, and receives a test). Among those admitted, we have data on vaccination status $X_i$ (multinomial) and the test results $Y_{ip}$ (each dichotomous).

We are interested in, but don't observe, $I_{ip}$ and $E_{ip}$, whether this person was infected with/exposed to pathogen $p$.

People are _a priori_ identical so we drop the index $i$.

We are interested in the quantity

$$
\frac{P[A \cap (I_p = 1) | X=v]}{P[A \cap (I_p=1) | X=v']}
$$

We have, via counts, probabilities like:

$$
\begin{align*}
P[(Y_p=y) \cap A \cap (X=v)]
&= \sum_z P[(Y_p=y) \cap A \cap (I_p=z) \cap (X=v)] \\
&= \sum_z P[Y_p=y | A \cap (I_p=z) \cap X=v] \cdot P[A \cap (I_p=z) \cap (X=v)] \\
&= \sum_z P[Y_p=y | A \cap (I_p=z)] \cdot \sum_e P[A \cap (I_p=z) | (E_p=e) \cap (X=v)] \cdot P[E_p=e|X=v] \cdot P[X=v] \\
\end{align*}
$$

If we furthermore assume perfect test sensitivity, then $Y_p = I_p$:

$$
P[(Y_p=y) \cap A \cap (X=v)] = \sum_e P[A \cap (I_p=y) | (E_p=e) \cap (X=v)] \cdot P[E_p=e|X=v] \cdot P[X=v]
$$

Now note that $E_p=0 \implies I_p=0$:

$$
P[(Y_p=y) \cap A \cap (X=v)] = \left\{ P[A | (E_p=0) \cap (X=v)] \cdot P[E_p=0|X=v] + P[A \cap (I_p=1) | (E_p=1) \cap (X=v)] \cdot P[E_p=1|X=v] \right\} \cdot P[X=v]
$$

## No co-infection, perfect performance

Assume individuals can be uninfected or infected with one pathogen. Assume that the test has perfect sensitivity and specificity so that $\sum_p Y_{ip} \in \{0, 1\}$ for all individuals $i$. In this case, the data in the TND reduce to a table of values $C_{vp}$, the number of people with each vaccination status $v$ who test positive for pathogen $p$.

The expected values of these counts are:

$$
\mathbb{E}[C_{vp}] = \sum_i P[(X_i=v) \cap (A_i = 1) \cap (Y_{ip} = 1)]
$$

For any particular individual $i$:

$$
\begin{align*}
P[(X_i=v) \cap (Y_{ip} = 1)] = P[Y_{ip}=1 | (A_i=1) \cap (X_i=v)] \cdot P[(A_i=1) \cap (X_i=v)]\\
\sum_i P[Y_j | A, E_k] \cdot P[A | E_k] \cdot P[E_k | X_i] \cdot P[X_i]
\end{align*}
$$

where:

- $Y_j$ is the event where a person has test outcome $j$
- $A$ is the event where a person is admitted to the study (i.e., receives a test)
- $E_i$ is the event where a person is "exposed" to "pathogen" $k$ (where "exposed" and "pathogen" are kind of misnomers)

We are interested in estimators of the quantity:

$$
\frac{P[A | X_i]}{P[A | X_{i'}]}
$$

For simplicity, start by assuming perfect sensitivity and specificity. The number of "pathogens" equals the number of outcomes, and

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

```math
\mathbb{E}\left[\hat{\mathrm{VE}}\right] = 1 -
  \frac{P[S_I|E,V] \times P[E|V] \times P[S_X|U]}{P[S_I|E,U] \times P[E|U] \times P[S_X|V]}
```

Under the assumption of equal exposure rates, the two $P[E|\cdot]$ terms cancel. Under the assumption of equal non-infection symptom probability, the two $P[S_X|\cdot]$ terms cancel. Thus:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}\right]
  = 1 - \frac{P[S_I|E,V]}{P[S_I|E,U]}
```
