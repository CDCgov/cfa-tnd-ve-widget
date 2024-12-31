# Test-negative design: short primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination. For purposes of a test-negative design (TND) study, we further define VE to be:

- a direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program,
- Protection against symptomatic disease that would lead to a diagnostic test, written $\mathrm{VE}_{SP}$ in [Halloran, Longini, and Struchiner](https://doi.org/10.1007/978-0-387-68636-3),
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
- Each individual has the possibility of becoming exposed $E$, and then has further conditional probabilities of becoming infected $I$, symptomatic $S_I$, and then tested $T_I$
  - Conditional probabilities depend on vaccination status. E.g., the probability that a vaccinated person will receive a test is $P[E|V] \times P[I|E,V] \times P[S_I|I,V] \times P[T_I|S_I,V]$.
  - There is only one opportunity for exposure per individual.
  - The $S \to T$ transition represents a combination of seeking healthcare and then qualifying to receive a test.
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
\mathrm{VE}_{SP} = 1 - \frac{P[S_I | V, E]}{P[S_I | U, E]}
```

#### Measured quantities

The expected values of the numbers of tested individuals, stratified by caused of symptoms (infected $I$ or not $X$) and vaccination status, are:

```math
\begin{align*}
\mathbb{E}[C_{VI}] &= n v \times P[T_I | S_I,V] \times P[S_I|I,V] \times P[I|E,V] \times P[E|V] \\
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

_Proposition_. This estimator is unbiased if:

1. the test has perfect sensitivity and specificity, such that, e.g., $C_{VP} = C_{VI}$,
2. the probability of exposure is identical among the vaccinated and unvaccinated, i.e., $P[E|V] = P[E|U]$,
3. non-infection symptoms arise with equal probability regardless of vaccination status, i.e., $P[S_X|V] = P[S_X|U]$, and
4. people seek testing for symptoms with a single probability, regardless of the cause of the symptoms and vaccination status, i.e., $P[T_I|S_I,V] = P[T_X|S_X,V] = P[T_I|S_I,U] = P[T_X|S_X,U]$.

_Proof_. Under the assumption of perfect performance, the expected value of the estimator is:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}\right] = 1 - \frac{
    P[T_I|S_I,V] \times P[S_I|I,V] \times P[I|E,V] \times P[E|V]
  }{
    P[T_I|S_I,U] \times P[S_I|I,U] \times P[I|E,U] \times P[E|U]
  } \times
  \frac{P[T_X|S_X,U] \times P[S_X|U]}{P[T_X|S_X,V] \times P[S_X|V]}
```

Under the assumption of equal exposure rates, the fourth terms in the numerator in denominator cancel. Under the assumption of equal non-infection symptom probability, sixth terms cancel. Under the assumption of identical testing behavior, the first and fifth terms cancel.

The remaining (second and third) terms collapse to:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}\right]
  = 1 - \frac{P[S_I|E,V]}{P[S_I|E,U]}
```
