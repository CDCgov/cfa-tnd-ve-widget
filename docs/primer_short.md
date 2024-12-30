# Test-negative design: short primer

## Draft outline

- What is VE
  - Known biases with any VE estimator
- What is a TND study
- There are 16 kinds of people:
  - Vaccinated vs. not
  - Infected with the pathogen of interest vs. not
  - Seek a test vs. not
  - Test positive vs. not
- TND has access only to people who seek a test
- "Actual" VE is: [insert risk ratio math]
- TND estimator of VE is: [insert odds ratio math]
- Note that TND estimator is unbiased only when: [assumptions]
- Bias of TND estimator scales this way with underlying parameters: [discuss]

"HLS" refers to Halloran, Longini, and Struchiner _Design and Analysis of Vaccine Studies_.

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

- The population of interest are those individuals who received a diagnostic test
- The main covariate of interest is vaccination status
- The outcome of interest is the test result (positive or negative)

The data available in a TND ultimately reduces to a 2x2 table of counts:

|               | Vaccinated | Unvaccinated |
| ------------- | ---------- | ------------ |
| Test positive | $C_{PV}$   | $C_{PU}$     |
| Test negative | $C_{NV}$   | $C_{NU}$     |

## Mathematical model

### Single-exposure model

- Individuals are vaccinated with probability $v$
  - Here we assume perfect reporting about vaccine status; i.e., there is no one who is actually vaccinated who appears in the "not vaccinated" arm, nor vice versa
- Individuals are exposed with probability $\varepsilon_V$ or $\varepsilon_U$
  - There is only one opportunity for exposure per individuals; individuals are either exposed or not
- Exposed individuals are infected ($I$) with probability $\lambda_V$ or $\lambda_U$
- Infected individuals seek and receive a test with probability $\mu_{VI}$ or $\mu_{UI}$
  - Note that this probability represents a combination of developing symptoms, seeking healthcare, and receiving a test given that healthcare was sought
- Uninfected individuals ($X$) also seek and receive tests with unconditional probability $\mu_{VX}$ or $\mu_{UX}$
- People who receive tests are either positive ($P$) or negative ($N$)
- The test has imperfect sensitivity $p_\mathrm{sens}$ and specificity $p_\mathrm{spec}$

#### Quantities of interest

We are interested in VE against infection conditioned on exposure:

$$
1 - \frac{\lambda_V}{\lambda_U}
$$

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
\hat{\mathrm{VE}}_\mathrm{OR} = 1 - \frac{C_{PV} C_{NU}}{C_{PU} C_{NV}}
```

The expected value of this estimator is:

```math
\begin{align*}
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right]
  &= 1 -
    \frac{n v \left[\varepsilon_V \lambda_V \mu_{VI} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{VX} (1 - p_\mathrm{spec}) \right]}{n (1-v) \left[\varepsilon_U \lambda_U \mu_{UI} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{UX} (1 - p_\mathrm{spec}) \right]}
    \times \frac{n (1-v) \left[\varepsilon_U \lambda_U \mu_{UI} (1 - p_\mathrm{sens}) + (1 - \varepsilon_U \lambda_U) \mu_{UX} p_\mathrm{spec} \right]}{n v \left[\varepsilon_V \lambda_V \mu_{VI} (1 - p_\mathrm{sens}) + (1 - \varepsilon_V \lambda_V) \mu_{VX} p_\mathrm{spec} \right]} \\
  &= 1 -
    \frac{
      \left[\varepsilon_V \lambda_V \mu_{VI} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{VX} (1 - p_\mathrm{spec}) \right] \times
      \left[\varepsilon_U \lambda_U \mu_{UI} (1 - p_\mathrm{sens}) + (1 - \varepsilon_U \lambda_U) \mu_{UX} p_\mathrm{spec} \right]
      }{
        \left[\varepsilon_U \lambda_U \mu_{UI} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{UX} (1 - p_\mathrm{spec}) \right] \times
        \left[\varepsilon_V \lambda_V \mu_{VI} (1 - p_\mathrm{sens}) + (1 - \varepsilon_V \lambda_V) \mu_{VX} p_\mathrm{spec} \right]
      }
\end{align*}
```

Assuming perfect test sensitivity and specificity:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right] = 1 -
  \frac{
    \varepsilon_V \lambda_V (1 - \varepsilon_U \lambda_U) \mu_{VI} \mu_{UX}
    }{
      \varepsilon_U \lambda_U (1 - \varepsilon_V \lambda_V) \mu_{VX} \mu_{UI}
    }
```

Furthermore assume equivalent post-infection behavior among the vaccinated and unvaccinated. Specificially, the infected are equally likely to progress to symptoms and seek care, regardless of vaccination status, such that $\mu_{VI} = \mu_{UI}$, and similarly for the uninfected, such that $\mu_{VX} = \mu_{UX}$. Then:

```math
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right] = 1 -
  \frac{\varepsilon_V \lambda_V (1 - \varepsilon_U \lambda_U)}{\varepsilon_U \lambda_U (1 - \varepsilon_V \lambda_V)}
```

If everyone is exposed $\varepsilon_V = \varepsilon_U = 1$, then:

$$
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right] = 1 - \frac{\lambda_V (1 - \lambda_U)}{\lambda_U (1 - \lambda_V)}
$$

which is an unbiased estimate of the odds ratio of protection.
