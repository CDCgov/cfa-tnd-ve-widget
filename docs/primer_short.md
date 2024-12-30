# Test-negative design: short primer

## Vaccine efficacy

VE is the fractional reduction in the probability of an adverse outcome due to vaccination. For purposes of a test-negative design (TND) study, we further define VE to be:

- A direct effect, that is, the counterfactual reduction in risk that would occur if a single individual were vaccinated or not, and not the population-level effect of reducing transmission via a vaccination program
- VE against infection, written $\mathrm{VE}_S$ in HLS
- Binary: Individuals are considered vaccinated or not (e.g., people who were vaccinated shortly before the outcome of interest may be classified as "unvaccinated" in the study, because they are presumed to have not yet been protected)
- Conditioned on some probability or amount of exposure to disease

Thus:

$$
\mathrm{VE} = 1 - \frac{P[\text{infected} | \text{vaccinated}]}{P[\text{infected} | \text{unvaccinated}]}
$$

## Test-negative design

A test-negative design (TND) is a study design that can be used to estimate VE. In a TND:

- The population of interest are those individuals who received a diagnostic test, usually becomes they develop some symptoms, seek a test, and qualify for that test.
- The main covariate of interest is vaccination status.
- The outcome of interest is the test result (positive or negative).

The data available in a TND ultimately reduces to a 2x2 table of counts:

|               | Vaccinated | Unvaccinated |
| ------------- | ---------- | ------------ |
| Test positive | $C_{PV}$   | $C_{PU}$     |
| Test negative | $C_{NV}$   | $C_{NU}$     |

## Mathematical model

### Single-exposure model

- Individuals are vaccinated $V$ with probability $v$, or unvaccinated $U$
  - Here we assume perfect reporting about vaccine status; i.e., there is no one who is actually vaccinated who appears in the "not vaccinated" arm, nor vice versa
- Individuals are exposed with probability $P[E|V]$ and $P[E|U]$
  - There is only one opportunity for exposure per individuals; individuals are either exposed or not
- Exposed individuals are infected ($I$) with probability $P[I|E,V]$ or $P[I|E,U]$
- Infected individuals seek and receive a test ($S$) with probability $P[S|I,V]$ or $P[S|I,U]$
  - Note that this probability represents a combination of developing symptoms, seeking healthcare, and actually receiving a test
- Uninfected individuals ($X$) also seek and receive tests, with unconditional probability $P[S|X,V]$ or $P[S|X,U]$
- People who receive tests are either positive ($P$) or negative ($N$)
- The test has sensitivity $p_\mathrm{sens}$ and specificity $p_\mathrm{spec}$
  - E.g., $P[P|S,V] = p_\mathrm{sens}$

#### Quantity of interest

We are interested in protection against symptomatic disease, conditioned on exposure:

```math
\mathrm{VE}_{SP} = 1 - \frac{P[S | V, E]}{P[S | U, E]}
```

#### Measured quantities

The expected values of the numbers of infected and uninfected, stratified by vaccination status, are:

```math
\begin{align*}
\mathbb{E}[C_{VI}] &= n v \times P[E|V] \times P[I|E,V] \times P[S|I,V] \\
\mathbb{E}[C_{VX}] &= n v \times P[S|X,V] \\
\mathbb{E}[C_{UI}] &= n (1-v) \times P[E|U] \times P[I|E,U] \times P[S|I,U] \\
\mathbb{E}[C_{UX}] &= n (1-v) \times P[S|X,U] \\
\end{align*}
```

The actual values from the TND trial are affected by test performance:

```math
\begin{align*}
\mathbb{E}[C_{VP}] &= p_\mathrm{sens} \mathbb{E}[C_{VI}] + (1 - p_\mathrm{spec}) \mathbb{E}[C_{VX}] \\
\mathbb{E}[C_{VN}] &= (1 - p_\mathrm{sens}) \mathbb{E}[C_{VI}] + p_\mathrm{spec} \mathbb{E}[C_{VX}] \\
\mathbb{E}[C_{UP}] &= p_\mathrm{sens} \mathbb{E}[C_{UI}] + (1 - p_\mathrm{spec}) \mathbb{E}[C_{UX}] \\
\mathbb{E}[C_{UN}] &= (1 - p_\mathrm{sens}) \mathbb{E}[C_{UI}] + p_\mathrm{spec} \mathbb{E}[C_{UX}] \\
\end{align*}
```

#### Odds ratio estimator

An estimator of the desired quantity is:

```math
\hat{\mathrm{VE}}_\mathrm{OR} = 1 - \frac{C_{VP} C_{UN}}{C_{UP} C_{VN}}
```

When there is perfect test performance, the TND counts reduce to the actual disease status counts, e.g., $C_{VP} = C_{VI}$. In this case, the expected value of the estimator is:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right] = 1 - \frac{P[E|V] \times P[I|E,V] \times P[S|I,V] \times P[S|X,U]}{P[E|U] \times P[I|E,U] \times P[S|I,U] \times P[S|X,V]}
```

If we further assume that:

1. the probability of exposure is identical among the vaccinated and unvaccinated, i.e., $P[E|V] = P[E|U]$, and
2. vaccination does not affect progression to testing among the uninfected, i.e., $P[S|X,U]=P[S|X,V]$

then:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right]
  = 1 - \frac{P[S|E,V]}{P[S|E,U]}
```

which is an unbiased estimator of $\mathrm{VE}_{SP}$.
