# Test-negative design: short primer

## Draft outline

- What is VE
  - Known biases with any VE estimator
- What is a TND study
- There are 8 kinds of people:
  - Vaccinated vs. not
  - Infected with the focal pathogen vs. not
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

- There is only one opportunity for exposure per individuals; individuals are either exposed or not
- Individuals are vaccinated with probability $v$
- Individuals are exposed with probability $\varepsilon_V$ or $\varepsilon_U$
- Exposed individuals are infected ($I$) with probability $\lambda_V$ or $\lambda_U$
- Infected individuals seek and receive a test with probability $\mu_{V|I}$ or $\mu_{U|I}$
  - Note that this probability represents a combination of developing symptoms, seeking healthcare, and receiving a test given that healthcare was sought
  - $1-\mu_V/\mu_U$ is an example of VE against progression conditional on an earlier outcome, written $\mathrm{VE}_P$ in HLS
- Uninfected individuals ($X$) also seek and receive tests with probability $\mu_{V|X}$ or $\mu_{U|X}$
- People who receive tests are either positive ($P$) or negative ($N$)
- The test has imperfect sensitivity $p_\mathrm{sens}$ and specificity $p_\mathrm{spec}$

#### Quantities of interest

We are interested in VE against infection conditioned on exposure:

$$
1 - \frac{\lambda_V}{\lambda_U}
$$

In a population of size $n$, the TND supplies counts whose expected values are:

$$
\begin{align*}
\mathbb{E}[C_{PV}] &= n v \left[\varepsilon_V \lambda_V \mu_{V|I} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{V|X} (1 - p_\mathrm{spec}) \right] \\
\mathbb{E}[C_{NV}] &= n v \left[\varepsilon_V \lambda_V \mu_{V|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_V \lambda_V) \mu_{V|X} p_\mathrm{spec} \right] \\
\mathbb{E}[C_{PU}] &= n (1-v) \left[\varepsilon_U \lambda_U \mu_{U|I} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{U|X} (1 - p_\mathrm{spec}) \right] \\
\mathbb{E}[C_{NU}] &= n (1-v) \left[\varepsilon_U \lambda_U \mu_{U|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_U \lambda_U) \mu_{U|X} p_\mathrm{spec} \right] \\
\end{align*}
$$

#### Risk ratio estimator

One estimator is:

$$
\hat{\mathrm{VE}}_\mathrm{RR} \equiv 1 - \frac{C_{PV} / (C_{PV} + C_{NV})}{C_{PU} / (C_{PU} + C_{NU})}
$$

The expected value of this estimator is:

$$
\begin{align*}
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{RR}\right] &= 1 - \frac{nv \left[\varepsilon_V \lambda_V \mu_{V|I} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{V|X} (1 - p_\mathrm{spec}) \right]}{n (1-v) \left[\varepsilon_U \lambda_U \mu_{U|I} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{U|X} (1 - p_\mathrm{spec}) \right]} \frac{n(1-v)}{nv} \\
&= 1 - \frac{\left[\varepsilon_V \lambda_V \mu_{V|I} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{V|X} (1 - p_\mathrm{spec}) \right]}{\left[\varepsilon_U \lambda_U \mu_{U|I} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{U|X} (1 - p_\mathrm{spec}) \right]}
\end{align*}
$$

This estimator is unbiased if:

- Exposure probabilities are identical (e.g., vaccination status is uncorrelated with contact networks): $\varepsilon_V = \varepsilon_U$
- Probability of receiving a test given infection is identical (i.e., vaccination does not protect against progression to symptomatic disease _and_ vaccination status is uncorrelated with healthcare seeking or probability of receiving a test given healthcare seeking)
- The test has perfect sensitivity and specificity

#### Odds ratio estimator

Another estimator is:

$$
\hat{\mathrm{VE}}_\mathrm{OR} = 1 - \frac{C_{PV} C_{NU}}{C_{PU} C_{NV}}
$$

The expected value of this estimator is:

$$
\begin{align*}
\mathbb{E}\left[\hat{\mathrm{VE}}_\mathrm{OR}\right]
  &= 1 -
    \frac{n v \left[\varepsilon_V \lambda_V \mu_{V|I} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{V|X} (1 - p_\mathrm{spec}) \right]}{n (1-v) \left[\varepsilon_U \lambda_U \mu_{U|I} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{U|X} (1 - p_\mathrm{spec}) \right]}
    \times \frac{n (1-v) \left[\varepsilon_U \lambda_U \mu_{U|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_U \lambda_U) \mu_{U|X} p_\mathrm{spec} \right]}{n v \left[\varepsilon_V \lambda_V \mu_{V|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_V \lambda_V) \mu_{V|X} p_\mathrm{spec} \right]} \\
  &= 1 -
    \frac{
      \left[\varepsilon_V \lambda_V \mu_{V|I} p_\mathrm{sens} + (1 - \varepsilon_V \lambda_V) \mu_{V|X} (1 - p_\mathrm{spec}) \right] \times
      \left[\varepsilon_U \lambda_U \mu_{U|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_U \lambda_U) \mu_{U|X} p_\mathrm{spec} \right]
      }{
        \left[\varepsilon_U \lambda_U \mu_{U|I} p_\mathrm{sens} + (1 - \varepsilon_U \lambda_U) \mu_{U|X} (1 - p_\mathrm{spec}) \right] \times
        \left[\varepsilon_V \lambda_V \mu_{V|I} (1 - p_\mathrm{sens}) + (1 - \varepsilon_V \lambda_V) \mu_{V|X} p_\mathrm{spec} \right]
      }
\end{align*}
$$

If we assume:

- Equal exposure probabilities: $\varepsilon_V = \varepsilon_U$
- Perfect sensitivity and specificity

Then this reduces to:

$$
1 - \frac{\lambda_V (1 - \lambda_U)}{\lambda_U (1 - \lambda_V)}
$$

In other words, at the cost of estimating VE in terms of an odds ratio rather than a risk ratio, we remove the need to make assumptions about probabilities $\mu$. This removes assumptions about (1) the vaccine preventing progression from infection to symptoms that would drive healthcare seeking and (2) healthcare seeking given the development of symptoms.
