# Test-negative design: primer

## Concept of Protection

If we are to evaluate how well protection can be estimated, we must first define protection axiomatically.

### General Definition

Protection is the reduction in probability of an adverse outcome due to some intervention.

$$
\text{Protection} = 1 - \frac{P(\text{outcome} | \text{intervention})}{P(\text{outcome}| \mathord{\sim} \text{intervention})}
$$

We interpret protection at the population level, measured via counts of realized outcomes. Both the adverse outcome and the intervention must be specified.

### Specific Components

We are interested in two different interventions:

- Vaccination, administered to individuals
  - Vaccine-based protection is often called "vaccine efficacy" or "VE."
  - Vaccination is binary: individuals are vaccinated or not
- Antibodies, circulating in individuals' blood
  - Antibodies are continuous: titers are non-negative numbers truncated by the bounds of detection.

We are interested in three different adverse outcomes:

- Susceptibility to infection:
  - the replication of a focal pathogen in the respiratory tract
  - probability of infection is denoted $P(S)$
- Progression to severe illness:
  - acute respiratory illness (ARI), given infection with the focal pathogen
  - probability of severe ARI given infection is denoted $P(P | S)$
- Susceptibility to infection AND progression to severe illness:
  - both infection and ARI together, as one event
  - probability of severe infection is denoted $P(PS) = P(P | S) \times P(S)$

Together, these form six combinations, or six possible precise definitions of protection. To start, we consider just one: vaccine-based protection against severe infection.

- We consider vaccination first because binary vaccination is simpler than continuous antibody titers.
- We consider severe infection first because infection and severity cannot be decomposed under some common study designs.

## Test Negative Design (TND)

Our study design of interest is the test-negative design (TND), in which all individual sampled are seeking care due to ARI. They fall into the following four categories of counts:

|                    | Vaccinated | Unvaccinated |
| ------------------ | ---------- | ------------ |
| Focal Pathogen     | $C_{FV}$   | $C_{FU}$     |
| Non-Focal Pathogen | $C_{NV}$   | $C_{NU}$     |

Because infection is never observed in the absence of ARI, TND cannot decompose infection from severity; it can only address severe infection as one event.

## Mathematical Notation and Notes

This is our mathematical language for investigating how well the TND can approximate protection.

### Notation

- $F$ = \[event\] severe illness with the focal pathogen
- $N$ = \[event\] severe illness with non-focal pathogens
- $V$ = \[event\] vaccination against the focal pathogen
- $U$ = \[event\] lack of vaccination against the focal pathogen
- $P$ = \[parameter\] population size
- $v$ = \[parameter\] proportion of the population that is vaccinated
- $\varepsilon$ = \[parameter\] rate of exposure per person per unit time (may depend on F vs. N and/or V vs. U)
- $\lambda$ = \[parameter\] probability of infection given exposure (may depend on F vs. N and/or V vs. U)
- $\pi$ = \[parameter\] probability of ARI given infection (may depend on F vs. N and/or V vs. U)
- $\mu$ = \[parameter\] probability of seeking care given ARI (may depend on V vs. U but not F vs. N)
- $\varphi$ = \[parameter\] probability that a vaccinated person responds to vaccination
- $\theta_\lambda = \frac{\lambda_{\text{FV}}}{\lambda_{\text{FU}}}$ \[parameter\] vaccine reduction in risk of infection with the focal pathogen given exposure
- $\theta_\pi = \frac{\pi_{\text{FV}}}{\pi_{\text{FU}}}$ \[parameter\] vaccine reduction in risk of ARI given infection with the focal pathogen
- $\theta = \theta_\lambda \theta_\pi$: \[parameter\] vaccine reduction in risk of ARI due to the focal pathogen given exposure
- $t$ = time since the disease season began

### Notes

There are several important facts that we must be careful not to overlook.

#### Vaccines Have Multiple Effects

We have declared several parameters related to vaccine action, which allow a spectrum of scenarios:

- If $\theta = 0$ and $\varphi < 1$, we have "all-or-nothing" action: vaccination either completely protects an individual from severe infection, or else it provides no protection at all.
- If $0 < \theta$ and $\varphi = 1$, we have "leaky" action: every vaccinated individual has a positive but reduced probability of severe infection, compared to unvaccinated individuals.

#### Vaccines Correlate with Behavior

Vaccination is not just a cause of immune fortification; it is also a consequence of behavioral choices. For example, we recognize that vaccinated individuals may have a different propensity to seek care in response to ARI compared to unvaccinated individuals ($\mu_V$ vs. $\mu_U$). Spoiler: these behavioral differences can ultimately bias TND-derived estimates of protection. So, to start, we remove them via assumptions:

- Differences in $\lambda$ and $\pi$ with vaccination are entirely immunological, not behavioral.
- The force of exposure $\varepsilon$ does not differ based on vaccination.

#### Observation Occurs Through Time

The counts of people in each quadrant of the TND accumulate through time, during which dynamic processes (e.g. transmission, recovery, etc.) occur. Spoiler: these dynamics are ultimately responsible for biasing TND-derived estimates of protection. So, to start, we remove time dynamics via assumptions:

- No parameters change through time. For example, even the force of exposure $\varepsilon$ is constant.
- Infection provides no protection. Infected individuals are not removed from the susceptible pool.
- All vaccines are administered at $t = 0$ and the effects of vaccination do not wane in time.

## Concept of Protection Revisited

Using our mathematical language, we can write a formula for the precise definition of protection.

$$
\begin{align*}
\mathrm{VE} &= 1 - \frac{P(F|V)}{P(F|U)} \\
&= 1 - \frac{( 1 - \varphi)\varepsilon_{FV}\lambda_{FU}\pi_{FU} + \varphi\varepsilon_{FV}\lambda_{FV}\pi_{FV}}{\varepsilon_{FU}\lambda_{FU}\pi_{FU}} \\
&= 1 - \frac{\varepsilon_{FV}}{\varepsilon_{FU}}\left( 1 - \varphi + \varphi\theta \right) \\
&= \varphi(1 - \theta)
\end{align*}
$$

Note the importance of assuming that $\varepsilon$ does not depend on vaccination.

We will use the axiom $\mathrm{VE} = 1 - \frac{P(F|V)}{P(F|U)}$ to pose candidate formulae of TND data to estimate VE.

We will use the equality $\mathrm{VE} = \varphi(1 - \theta)$ to verify whether these candidate formulae are correct.

## Estimating Protection from TND

Attempting to pose a formula for a TND estimate of VE reveals common pitfalls and ultimately explains why an odds ratio is required.

### Direct Risk Ratio from Counts Alone Fails

At first, it may appear that the terms of the axiomatic definition of protection are directly available in the TND data. We replace the conditional probabilities using the formula P(AB) = P(A\|B)P(B):

$$
\mathrm{VE} = 1 - \frac{P(F|V)}{P(F|U)} = 1 - \frac{\frac{P(FV)}{P(V)}}{\frac{P(FU)}{P(U)}}
$$

Let C represent the counts in each quadrant of the TND data. It may appear that:

$$
\mathrm{VE} = 1 - \frac{\frac{P(FV)}{P(V)}}{\frac{P(FU)}{P(U)}} = 1 - \frac{\frac{C_{FV}}{(C_{FV} + C_{NV})}}{\frac{C_{FU}}{(C_{FU} + C_{NU})}}
$$

However, this is not true, because $C_{FV} + C_{NV} \propto P(V \text{ and ARI and care-seeking}) \neq P(V)$. Similarly, $C_{FU} + C_{NU} \propto P(U \text{ and ARI and care-seeking}) \neq P(U)$.

### Direct Risk Ratio from Counts and Outside Knowledge Fails

To address this pitfall, one may assume that the vaccination rate v is known from other means outside the TND. In this case:

$$
\mathrm{VE} = 1 - \frac{\frac{P(FV)}{P\left( V \right)}}{\frac{P(FU)}{P\left( U \right)}} = 1 - \frac{\frac{C_{FV}}{vP}}{\frac{C_{FU}}{\left( 1 - v \right)P}}
$$

According to the assumptions we've made, the cumulative counts of people in the TND at time $t$ will be:

$$
\begin{align*}
C_{FV} &= \varepsilon_{FV}tvP\lbrack\left( 1 - \varphi \right)\lambda_{FU}\pi_{FU} + \varphi\lambda_{FV}\pi_{FV}\rbrack\mu_{V} \\
C_{FU} &= \varepsilon_{FU}t\left( 1 - v \right)P\lambda_{FU}\pi_{FU}\mu_{U} \\
C_{NV} &= \varepsilon_{NV}tvP\lambda_{NV}\pi_{NV}\mu_{V} \\
C_{NU} &= \varepsilon_{NU}t(1 - v)P\lambda_{NU}\pi_{NU}\mu_{U}
\end{align*}
$$

Substituting:

$$
\mathrm{VE} = 1 - \frac{\frac{\varepsilon_{FV}tvP\left\lbrack \left( 1 - \varphi \right)\lambda_{FU}\pi_{FU} + \varphi\lambda_{FV}\pi_{FV} \right\rbrack\mu_{V}}{vP}}{\frac{\varepsilon_{FU}t\left( 1 - v \right)P\lambda_{FU}\pi_{FU}\mu_{U}}{\left( 1 - v \right)P}} = 1 - \frac{\mu_{V}}{\mu_{U}}\left( 1 - \varphi + \varphi\theta \right)
$$

Again, note the importance of assuming that $\varepsilon$ does not depend on vaccination. Even so, this estimate of VE reduces to the correct value, $\varphi(1 + \theta)$, if and only if $\mu_V$ = $\mu_U$, which is not generally true. In other words, the differential propensity to seek care with vaccination status prevents the direct risk ratio from accurately estimating VE.

### Derivation of the Odds Ratio

We now see that a simple adjustment for the differential propensity to seek care with vaccination status will guarantee that our posed formula reduces to the correct value of VE:

$$
\mathrm{VE} = 1 - \frac{\frac{C_{FV}}{vP}}{\frac{C_{FU}}{\left( 1 - v \right)P}}\frac{\mu_{U}}{\mu_{V}} = 1 - \frac{\mu_{V}}{\mu_{U}}\frac{\mu_{U}}{\mu_{V}}\left( 1 - \varphi + \varphi\theta \right) = \varphi(1 - \theta)
$$

But how should $\frac{\mu_{U}}{\mu_{V}}$ be estimated from TND data? If we assume that vaccination status does not affect any aspect of the non-focal pathogens ($\varepsilon_N$, $\lambda_N$, or $\pi_N$), then the only reasons that the number of people seeking care for ARI due to non-focal pathogens would differ by vaccination status are:

- the propensity to seek care differs by vaccination status, and

- different numbers of people are vaccinated vs. unvaccinated.

So we claim $\frac{\mu_{U}}{\mu_{V}}\frac{\left( 1 - v \right)P}{vP} = \frac{C_{NU}}{C_{NV}}$, or equivalently $\frac{\mu_{U}}{\mu_{V}} = \frac{C_{NU}}{C_{NV}}\frac{vP}{\left( 1 - v \right)P}$. Thus, we can say:

$$
\mathrm{VE} = 1 - \frac{\frac{C_{FV}}{vP}}{\frac{C_{FU}}{\left( 1 - v \right)P}}\frac{C_{NU}vP}{C_{NV}\left( 1 - v \right)P} = 1 - \frac{C_{FV}C_{NU}}{C_{FU}C_{NV}}
$$

After some convenient canceling, we have an unbiased estimate of VE that only uses TND quadrants! In particular, an outside source of information giving v is unnecessary. Furthermore, note that:

$$
\mathrm{VE} = 1 - \frac{C_{FV}C_{NU}}{C_{FU}C_{NV}} = 1 - \frac{P(FV)P(NU)}{P(FU)P(NV)} = 1 - \frac{\frac{P(FV)}{P(FU)}}{\frac{P(NV)}{P(NU)}} = 1 - \frac{\frac{\frac{P(FV)}{P(F)}}{\frac{P(FU)}{P(F)}}}{\frac{\frac{P(NV)}{P(N)}}{\frac{P(NU)}{P(N)}}} = 1 - \frac{\frac{P(V|F)}{P(U|F)}}{\frac{P(V|N)}{P(U|N)}}
$$

The final expression for VE is the odds ratio of vaccination given exposure ("OR"). Thus, it can be helpful to think of the odds ratio used in TND this way: the TND expression for VE uses an odds ratio _not_ because protection itself is an odds ratio (it is not), but because correcting the risk ratio of protection for differential care-seeking behavior happens to result in a formula that is equivalent to an odds ratio.

## When TND Fails

Note how many assumptions were required to make the formula $\mathrm{VE} = 1 - \mathrm{OR}$ true. These assumptions about the force of infection and time dynamics are likely false. Relaxing these assumptions will bias the estimator of VE. Now we explore how relaxing specific assumptions causes specific biases in $1 - \mathrm{OR}$. These are only some examples.

### Force of Exposure Differs by Vaccination Status

We relax the assumption that vaccination does not correlate with force of exposure, so that in general $\varepsilon_{FV} \neq \varepsilon_{FU}$ and $\varepsilon_{NV} \neq \varepsilon_{NU}$. Many factors can influence this in different directions; for example, perhaps:

- People who choose to get vaccinated also choose to avoid contacts more frequently
- People who choose to get vaccinated live in more densely populated contact-rich areas

Note that we continue to assume that any particular force of exposure $\varepsilon$ is constant, and that natural infection provides no protection against natural infection. Under these assumptions:

$$
\begin{align*}
\mathrm{VE} &= 1 - \frac{C_{FV}C_{NU}}{C_{FU}C_{NV}} \\
&= 1 - \frac{\left( \varepsilon_{FV}tvP\left\lbrack \left( 1 - \varphi \right)\lambda_{FU}\pi_{FU} + \varphi\lambda_{FV}\pi_{FV} \right\rbrack\mu_{V} \right)\left( \varepsilon_{NU}t\left( 1 - v \right)P\lambda_{NU}\pi_{NU}\mu_{U} \right)}{\left( \varepsilon_{FU}t\left( 1 - v \right)P\lambda_{FU}\pi_{FU}\mu_{U} \right)\left( \varepsilon_{NV}tvP\lambda_{NV}\pi_{NV}\mu_{V} \right)} \\
&= 1 - \frac{\left( \varepsilon_{FV}\left\lbrack \left( 1 - \varphi \right)\lambda_{FU}\pi_{FU} + \varphi\lambda_{FV}\pi_{FV} \right\rbrack \right)\left( \varepsilon_{NU}\lambda_{NU}\pi_{NU} \right)}{\left( \varepsilon_{FU}\lambda_{FU}\pi_{FU} \right)\left( \varepsilon_{NV}\lambda_{NV}\pi_{NV} \right)}
\end{align*}
$$

By continuing to assume that $\lambda$ and $\pi$ are purely immunological, such that $\lambda_N$ and $\pi_N$ are unimpacted by vaccination (i.e., $\lambda_{NV} = \lambda_{NU}$ and $\pi_{NV} = \pi_{NU}$):

$$= 1 - \frac{\varepsilon_{FV}\varepsilon_{NU}}{\varepsilon_{FU}\varepsilon_{NV}}\left( 1 - \varphi + \varphi\theta \right)$$

The term $\frac{\varepsilon_{FV}\varepsilon_{NU}}{\varepsilon_{FU}\varepsilon_{NV}}$ no longer reduces to 1 by assumption, so the TND VE estimate of $1 - \mathrm{OR}$ no longer _necessarily_ reduces to the correct value of $\varphi(1 + \theta)$. However, $\frac{\varepsilon_{FV}\varepsilon_{NU}}{\varepsilon_{FU}\varepsilon_{NV}}$ _can_ still reduce to 1, resulting in an unbiased estimate of VE. All that is required is a weaker assumption that vaccination correlates with force of exposure identically for different pathogens, such that $\varepsilon_{FV} \neq \varepsilon_{FU}$ and $\varepsilon_{NV} \neq \varepsilon_{NU}$ but $\frac{\varepsilon_{FV}}{\varepsilon_{FU}} = \frac{\varepsilon_{NV}}{\varepsilon_{NU}}$.

If this weaker assumption is true, $1 - \mathrm{OR}$ is still an unbiased estimate of VE; otherwise, $1 - \mathrm{OR}$ is biased in a way that depends on the values of $\varepsilon_{FV}$, $\varepsilon_{FU}$, $\varepsilon_{NV}$, and $\varepsilon_{NU}$.

### Natural Infection Protects against Re-Infection

We assume that infection with the focal pathogen provides complete protection, rather than no protection at all. Importantly, this change does not extend to non-focal pathogens. Even if one non-focal pathogen stimulates complete protection, there are many other non-focal pathogens that can still infect. Thus, we retain the assumption that natural infection provides no protection for non-focal pathogens.

As a result, the number of people susceptible to non-focal pathogens remains constant at P over time, whereas the number of people susceptible to the focal pathogen decays as $e^{- \varepsilon_{F}\lambda_{F}t}$. Accordingly, the cumulative counts of people observed in the TND with the focal pathogen at time $t$ will be:

$C_{FV} = vP\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{FV}\lambda_{FU}t})\pi_{FU} + \varphi(1 - e^{- \varepsilon_{FV}\lambda_{FV}t})\pi_{FV}\rbrack\mu_{V}$

$C_{FU} = \left( 1 - v \right)P(1 - e^{- \varepsilon_{FU}\lambda_{FU}t})\pi_{FU}\mu_{U}$

Now the $1 - \mathrm{OR}$ estimate of VE becomes:

$$
\begin{align*}
\mathrm{VE} &= 1 - \frac{C_{FV}C_{NU}}{C_{FU}C_{NV}} \\
&= 1 - \frac{vP\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{FV}\lambda_{FU}t})\pi_{FU} + \varphi(1 - e^{- \varepsilon_{FV}\lambda_{FV}t})\pi_{FV}\rbrack\mu_{V})\left( \varepsilon_{NU}t\left( 1 - v \right)P\lambda_{NU}\pi_{NU}\mu_{U} \right)}{\left( \left( 1 - v \right)P(1 - e^{- \varepsilon_{FU}\lambda_{FU}t})\pi_{FU}\mu_{U} \right)\left( \varepsilon_{NV}tvP\lambda_{NV}\pi_{NV}\mu_{V} \right)} \\
&= 1 - \frac{\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{FV}\lambda_{FU}t})\pi_{FU} + \varphi(1 - e^{- \varepsilon_{FV}\lambda_{FV}t})\pi_{FV}\rbrack)\left( \varepsilon_{NU}\lambda_{NU}\pi_{NU} \right)}{\left( (1 - e^{- \varepsilon_{FU}\lambda_{FU}t})\pi_{FU} \right)\left( \varepsilon_{NV}\lambda_{NV}\pi_{NV} \right)}
\end{align*}
$$

As above, we will continue to assume that $\lambda_{NV} = \lambda_{NU}$ and $\pi_{NV} = \pi_{NU}$. And we will reimpose the assumption that $\varepsilon_{FV} = \varepsilon_{FU}$ and $\varepsilon_{NV} = \varepsilon_{NU}$, to better isolate the consequences of natural protection:

$$= 1 - \left( 1 - \varphi \right) - \varphi\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}}\frac{\pi_{FV}}{\pi_{FU}} = \varphi\left( 1 - \theta_{\pi}\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}} \right)$$

Because the term $\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}}$ is not necessarily equal to θ\_$\lambda$, the TND VE estimate of $1 - \mathrm{OR}$ no longer necessarily reduces to the correct value of $\varphi(1 - \theta)$. In fact, $1 - \mathrm{OR}$ only reduces to the correct value of $\varphi(1 + \theta)$ under one of the following conditions:

- $\lambda_{FV} = \lambda_{FU}$, that is, vaccination does not affect the probability of infection given exposure to the focal pathogen. In this case, $\mathrm{VE} = \varphi\left( 1 - \theta_{\pi} \right) = \varphi\left( 1 - \theta \right)$ because $\theta = \theta_{\lambda}\theta_{\pi} = 1*\theta_{\pi} = \theta_{\pi}$. Note that vaccination may still affect the probability of ARI given infection, $\pi$. Thus, $1 - \mathrm{OR}$ can be unbiased under "leaky" vaccination, so long as vaccination reduces the probability of ARI, not infection itself.

- $\lambda_{FV} = 0$, that is, vaccination provides perfect protection against infection given exposure to the focal pathogen. In this case, $\mathrm{VE} = \varphi = \varphi\left( 1 - \theta \right)$ because $\theta = \theta_{\lambda}\theta_{\pi} = 0*\theta_{\pi} = 0$. Note that vaccination may still affect the probability of ARI given infection, $\pi$, although this is meaningless because successfully vaccinated people never get infected. As such, this condition is equivalent to all-or-nothing vaccination, in which $\varphi$ ≤ 1 and θ = 0.

Outside of these conditions, the value of the term $\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}}$ varies in time, so it cannot equal the constant value θ*$\lambda$. At best, this term can equal θ*$\lambda$ at exactly one time point, meaning $1 - \mathrm{OR}$ will be unbiased at only one time point. We can show that this time point is $t = 0$ using L'Hôpitál's Rule:

$$\lim_{t \rightarrow 0}\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}} = \lim_{t \rightarrow 0}\frac{\varepsilon_{FV}\lambda_{FV}e^{- \varepsilon_{FV}\lambda_{FV}t}}{\varepsilon_{FU}\lambda_{FU}e^{- \varepsilon_{FU}\lambda_{FU}t}} = \frac{\varepsilon_{FV}\lambda_{FV}}{\varepsilon_{FU}\lambda_{FU}} = \frac{\lambda_{FV}}{\lambda_{FU}} = \theta_{\lambda}$$

Again, note the importance of reinstating the assumption that $\varepsilon_{FV} = \varepsilon_{FU}$. Also, note that as $t \rightarrow 0$ from the right, $\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}} \rightarrow \theta_{\lambda}$ from above. Thus, for times beyond $t = 0$, $1 - \mathrm{OR}$ yields $\mathrm{VE} < \varphi\left( 1 - \theta \right)$.

In sum, if vaccination reduces but does not eliminate the probability of infection given exposure to the focal pathogen, then $1 - \mathrm{OR}$ will underestimate the true value of VE for times beyond the very beginning of the season. In loose terms, protection against the focal pathogen derived from natural infections causes the susceptible population to dwindle. This dwindling through time occurs disproportionately in the unvaccinated, who are more likely to experience natural infections. The same process does not occur for non-focal pathogens, for which natural infections do not provide protection. Thus, the term $C_{FU}$ in $\mathrm{VE} = 1 - \frac{C_{FV} C_{NU}}{C_{FU}C_{NV}}$ shrinks disproportionately as time passes, causing the estimate of VE to also shrink.

### Different Force of Exposure and Natural Protection

If both assumptions discussed above are broken at once, such that the force of exposure differs by vaccination status and the focal pathogen provides natural protection, then $1 - \mathrm{OR}$ gives:

$$
\begin{align*}
\mathrm{VE} &= 1 - \frac{C_{FV}C_{NU}}{C_{FU}C_{NV}} \\
&= 1 - \frac{\varepsilon_{NU}}{\varepsilon_{NV}} \left[ (1 - \varphi)\frac{1 - e^{- \varepsilon_{FV}\lambda_{FU}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}} + \varphi\theta_{\pi}\frac{1 - e^{- \varepsilon_{FV}\lambda_{FV}t}}{1 - e^{- \varepsilon_{FU}\lambda_{FU}t}} \right] \\
&\neq \varphi (1 - \theta)
\end{align*}
$$

In this case, the bias in the TND estimate of VE depends on the relative force of exposure between vaccinated and unvaccinated people, for all pathogens. Unlike in Section 6.1, assuming that vaccination correlates with force of exposure identically for different pathogens ($\frac{\varepsilon_{FV}}{\varepsilon_{FU}} = \frac{\varepsilon_{NV}}{\varepsilon_{NU}}$) no longer corrects this.

Two further observations about these assumptions are also warranted:

- The disparity in force of exposure by vaccination status is what biases $1 - \mathrm{OR}$. Different forces of exposure between the focal and non-focal pathogens (i.e. $\varepsilon_{F} \neq \varepsilon_{N}$), even if these forces are dynamic in time (i.e. $\varepsilon_{F}\left( t \right) \neq \varepsilon_{N}(t)$ ), do not contribute to the bias.

- The disparity in natural protection between the focal and non-focal pathogens need not be so exaggerated (i.e. complete vs. non-existent, respectively). Any disparity in natural protection will bias $1 - \mathrm{OR}$ for the same reasons described in Section 6.2, albeit perhaps to a lesser extent.

### Behavioral Correlations between Vaccination and Susceptibility/Severity

Even when $1 - \mathrm{OR} = \varphi\left( 1 - \theta \right) = \varphi\left( 1 - \frac{\lambda_{FV}}{\lambda_{FU}}\frac{\pi_{FV}}{\pi_{FU}} \right)$, bias may be lurking in the interpretation. VE is typically interpreted as purely a result of vaccine-stimulated immune defense. But perhaps $\lambda_{FV} \neq \lambda_{FU}$ and/or $\pi_{FV} \neq \pi_{FU}$ for reasons unrelated to immunological action. For example:

- Individuals at high risk of infection given exposure (e.g. elderly, some immunocompromised) may be more likely to get vaccinated than the general public. In this case, the realized value of $\theta_{\lambda} = \frac{\lambda_{FV}}{\lambda_{FU}}$ is closer to 1 than it would be if it only captured immunological phenomena.

- Individuals who get vaccinated may be more likely to use at-home treatments for mild illness which help prevent progression to ARI. In this case, the realized value of $\theta_{\pi} = \frac{\pi_{FV}}{\pi_{FU}}$ is closer to 0 than it would be if it only captured immunological phenomena.

These examples show that a purely immunological interpretation of VE could under- or overestimate the impact of vaccination, depending on which conditions and behaviors correlate with vaccination.

### Probability of Being Tested Differs by Disease and Vaccination Status

To this point, we have tacitly assumed that everyone with ARI who seeks care is tested for the causal pathogen. But in practice, ARI symptoms may manifest differently based on the causal pathogen and/or vaccination status, leading to different probabilities of a clinician deciding to administer a test. If we reimpose all previous assumptions but introduce ζ as the probability of being tested, we have:

$$
\begin{align*}
\mathrm{VE} &= 1 - \frac{\left( \varepsilon_{FV}tvP\left\lbrack \left( 1 - \varphi \right)\lambda_{FU}\pi_{FU} + \varphi\lambda_{FV}\pi_{FV} \right\rbrack\mu_{V}\zeta_{FV} \right)\left( \varepsilon_{NU}t\left( 1 - v \right)P\lambda_{NU}\pi_{NU}\mu_{U}\zeta_{NU} \right)}{\left( \varepsilon_{FU}t\left( 1 - v \right)P\lambda_{FU}\pi_{FU}\mu_{U}\zeta_{FU} \right)\left( \varepsilon_{NV}tvP\lambda_{NV}\pi_{NV}\mu_{V}\zeta_{NV} \right)} \\
&= 1 - \frac{\zeta_{FV}\zeta_{NU}}{\zeta_{FU}\zeta_{NV}}\left( 1 - \varphi + \varphi\theta \right)
\end{align*}
$$

Thus, unless the effect of vaccination on the probability of being tested is identical for both the focal and non-focal pathogens, $\frac{\zeta_{FV}}{\zeta_{FU}} = \frac{\zeta_{NV}}{\zeta_{NU}}$, then testing probability also contributes to bias in $1 - \mathrm{OR}$.

## Conclusions

$1 - \mathrm{OR}$ from a TND study is an unbiased estimator of VE only under a restrictive and unrealistic set of assumptions. Violating these assumptions introduces biases which can be understood in isolation, but which may interact with one another in complicated ways. Nonetheless, some themes emerge:

- The transmission and/or disease caused by the focal vs. non-focal pathogens need not be identical, but they must respond to vaccination identically (except for $\lambda$ and $\pi$), to avoid bias.
- Dynamics cause bias not because the rates of observing TND quadrants change through time, but because the _relative_ rates of observing vaccinated vs. unvaccinated TND quadrants change through time.

Using these conclusions and the mathematical language developed above, the biasing effect of other factors not discussed here (e.g. vaccine waning through time, imperfect specificity and sensitivity of the diagnostic test, etc.) on VE should be more easily investigated.

## Protection from Antibodies

We now switch the intervention responsible for protection from binary vaccination to continous antibody titer. Rather than a single number, protection is now a function of antibody titer. However, for any mathematical demonstration, it suffices to consider just a single arbitrary titer.

Importantly, we are concerned with antibody titer _at the time of exposure_, regardless of when exposure occurs. As a result, we discard several complicating factors from the vaccination case (e.g. distinguishing natural infection- vs. vaccine-stimulated protection, leaky vs. all-or-nothing protection, etc.). This actually makes antibody-mediated protection an easier problem than vaccine-stimulated protection!

### Notation

Only slight changes to our mathematical language are required:

- $F$ = \[event\] severe illness with the focal pathogen
- $N$ = \[event\] severe illness with non-focal pathogens
- $X$ = \[event\] an individual's antibody titer at a time of exposure
- $D$ = \[function\] probability density of an individual having titer x at time t
- $\varepsilon$ = \[parameter\] rate of exposure per person per unit time (may depend on F vs. N and/or X)
- $\lambda$ = \[parameter\] probability of infection given exposure (may depend on F vs. N and/or X)
- $\pi$ = \[parameter\] probability of ARI given infection (may depend on F vs. N and/or X)
- $\mu$ = \[parameter\] probability of seeking care given ARI (may depend on X but not F vs. N)
- $\theta_\lambda = \frac{\lambda_{F,X=x}}{\lambda_{F,X=0}}$ \[parameter\] reduction in risk of infection with the focal pathogen given exposure due to antibody titer x
- $\theta_\pi = \frac{\pi_{F,X=x}}{\pi_{\text{F,X=0}}$ \[parameter\] vaccine reduction in risk of ARI given infection with the focal pathogen due to antibody titer x
- $\theta = \theta_\lambda \theta_\pi$: \[parameter\] vaccine reduction in risk of ARI due to the focal pathogen given exposure
- $t$ = time since the disease season began

### TND Data

For any particular antibody titer $X=x$, a subset of the data collected from the TND design will look like:

|                    |  Vaccinated   |  Unvaccinated   |
| ------------------ | ------------- | --------------- |
| Focal Pathogen     | $C_{F,X=x}$   | $C_{F,X=0}$     |
| Non-Focal Pathogen | $C_{N,X=x}$   | $C_{N,X=0}$     |

### Assumptions

Some assumptions from the vaccine case are no longer relevant, e.g. leaky vs. all-or-nothing protection. However, other assumptions still apply.

#### Titers Correlate with Behavior

Antibody titer is not only the cause immunological action inside an individual, but titer is also the effect of behavioral choices. For example, many individuals with high titers might have gotten those titers from vaccination, reflecting their behavioral propensity to interact with the healthcare system. Just as for vaccination, behavioral differences can bias TND-derived estimates of protection. So we remove them via assumptions:

- Differences in $\lambda$ and $\pi$ with titer are entirely immunological, not behavioral.
- The force of exposure $\varepsilon$ does not vary with titer.

#### Observation Occurs through Time

Just as for vaccination, the counts of people in each quadrant of the TND accumulate through time, during which dynamic processes occur. These dynamic processes can ultimately bias the TND-derived estimate of protection. So we remove these dynamics via assumption:

- No parameters change through time. For example, force of exposure $\varepsilon$ is constant.
- All people included in the TND were sampled over a very short period of time $\Delta t$.

Notice we need not consider when vaccines were administered, how they wane, or whether natural infection confers protection. This is because we only care about titer at the time of exposure, not how that titer came to be.

### Protection Defined

Rather than a single number, protection is now a function of antibody titer $P(X=x)$, whose value at is one minus the risk ratio of infection for antibody titer $X=x$ vs. $X=0$.

$$
\begin{align*}
\mathrm{P(X=x)} &= 1 - \frac{P(F|X=x)}{P(F|X=0)} \\
&= 1 - \frac{\varepsilon_{F,X=x}\lambda_{F,X=x}\pi_{F,X=x}}{\varepsilon_{F,X=0}\lambda_{F,X=0}\pi_{F,X=0}} \\
&= 1 - \frac{\varepsilon_{F,X=x}}{\varepsilon_{F,X=0}}\theta \\
&= 1 - \theta
\end{align*}
$$

Notice the importance of assuming that $\varepsilon$ does not depend on antibody titer.

We will use the equality $P(X=x) = 1 - \theta$ to verify whether candidate formulae for protection are correct.

### Verification of the Odds Ratio

According to the assumptions we've made, the counts of people in the TND at time $t$ will be:

$$
\begin{align*}
C_{F,X=x} &= \varepsilon_{F,X=x}\Delta t D(x)\lambda_{F,X=x}\pi_{F,X=x}\mu_{X=x} \\
C_{F,X=0} &= \varepsilon_{F,X=0}\Delta t D(0)\lambda_{F,X=0}\pi_{F,X=0}\mu_{X=0} \\
C_{N,X=x} &= \varepsilon_{N,X=x}\Delta t D(x)\lambda_{N,X=x}\pi_{N,X=x}\mu_{X=x} \\
C_{N,X=0} &= \varepsilon_{N,X=0}\Delta t D(0)\lambda_{N,X=0}\pi_{N,X=0}\mu_{X=0} \\
\end{align*}
$$

Similar to the vaccine case, we now postulate that one minus the odds ratio of $X=x$ given exposure is an unbiased estimator of the protection conferred by antibody titer $X=x$.

$$
\begin{align*}
\mathrm{Protection(X=x)} &= 1 - \frac{C_{F,X=x}C_{N,X=0}}{C_{F,X=0}C_{N,X=x}} \\
&= 1 - \frac{\varepsilon_{F,X=x}\Delta t D(x)\lambda_{F,X=x}\pi_{F,X=x}\mu_{X=x}\varepsilon_{N,X=0}\Delta t D(0)\lambda_{N,X=0}\pi_{N,X=0}\mu_{X=0}}{\varepsilon_{F,X=0}\Delta t D(0)\lambda_{F,X=0}\pi_{F,X=0}\mu_{X=0}\varepsilon_{N,X=x}\Delta t D(x)\lambda_{N,X=x}\pi_{N,X=x}\mu_{X=x}} \\
&= 1 - \frac{\varepsilon_{F,X=x}\lambda_{F,X=x}\pi_{F,X=x}\varepsilon_{N,X=0}\lambda_{N,X=0}\pi_{N,X=0}}{\varepsilon_{F,X=0}\lambda_{F,X=0}\pi_{F,X=0}\varepsilon_{N,X=x}\lambda_{N,X=x}\pi_{N,X=x}} \\
&= 1 - \frac{\varepsilon_{F,X=x}\lambda_{F,X=x}\pi_{F,X=x}\varepsilon_{N,X=0}\lambda_{N,X=0}\pi_{N,X=0}}{\varepsilon_{F,X=0}\lambda_{F,X=0}\pi_{F,X=0}\varepsilon_{N,X=x}\lambda_{N,X=x}\pi_{N,X=x}} \\
\end{align*}
$$

By natural cancellation, we see that differential care seeking given ARI by antibody titer ($\mu$) is inconsequential. So is the distribution of antibody titers $D$.

By assuming that exposure, susceptibility, and severity of non-focal causes of ARI do not depend on antibody titer (i.e. $\varepsilon_{N,X=x}) = \varepsilon_{N,X=0}$, $\lambda_{N,X=x}) = \lambda_{N,X=0}$, and $\pi_{N,X=x}) = \pi_{N,X=0}$), we further cancel to obtain:

$$
\begin{align*}
\mathrm{Protection(X=x)} &= 1 - \frac{\varepsilon_{F,X=x}\lambda_{F,X=x}\pi_{F,X=x}}{\varepsilon_{F,X=0}\lambda_{F,X=0}\pi_{F,X=0}} \\
\end{align*}
$$

And finally, by assuming that exposure to the focal pathogen does not depend on antibody titer (i.e. $\varepsilon_{F,X=x} = \varepsilon_{F,X=0}$), we cancel again to obtain:

$$
\begin{align*}
\mathrm{Protection(X=x)} &= 1 - \frac{\lambda_{F,X=x}\pi_{F,X=x}}{\lambda_{F,X=0}\pi_{F,X=0}} \\
&= 1 - \theta_{\lambda}\theta_{\pi} \\
\end{align*}
$$

Thus, under the above assumptions, one minus the odds ratio of $X=x$ given exposure is an unbiased estimator of the protection conferred by antibody titer $X=x$.

### When TND Fails for Antibody Titer

As with vaccination, many assumptions were required to make $1 - OR$ an unbiased estimator of $P(X=x)$. Now we will explore how relaxing some of these assumptions lead to bias.

#### Force of Exposure Differs by Antibody Titer

It is possible that force of exposure to pathogens (either focal or non-focal) may be correlated with antibody titer, perhaps due to population-level behavioral phenomena. In this case, some cancellations in the above derivation fail, and we obtain

$$
\begin{align*}
\mathrm{Protection(X=x)} &= 1 - \frac{\varepsilon_{F,X=x}\lambda_{F,X=x}\pi_{F,X=x}\varepsilon_{N,X=0}}{\varepsilon_{F,X=0}\lambda_{F,X=0}\pi_{F,X=0}\varepsilon_{N,X=x}} \\
&= 1 - \frac{\varepsilon_{F,X=x}\varepsilon_{N,X=0}}{\varepsilon_{F,X=0}\varepsilon_{N,X=x}}\theta \\
\end{align*}
$$

As was the case for vaccination, the term $\frac{\varepsilon_{F,X=x}\varepsilon_{N,X=0}}{\varepsilon_{F,X=0}\varepsilon_{N,X=x}}$ no longer reduces to 1 by assumption, so the estimator $1 - OR$ no longer _necessarily_ reduces to the correct value of $1 - \theta$. However, if antibody titer $X=x$ correlates with force of exposure identically for both pathogens, such that $\varepsilon_{F,X=x} \neq \varepsilon_{F,X=0}$ and such that $\varepsilon_{N,X=x} \neq \varepsilon_{N,X=0}$ but $\frac{\varepsilon_{F,X=x}}{\varepsilon_{F,X=0}} = \frac{\varepsilon_{N,X=x}}{\varepsilon_{N,X=0}}$, then $1 - OR$ is still an unbiased estimator of $P(X=x)$. Otherwise, $1 - OR$ is biased in a way that depends on the individual values of the $\varepsilon$ parameters.

#### TND Data Are Collected over a Time Period

In the vaccination case, time dynamics cause bias when the relative rates of observing vaccinated vs. unvaccinated quadrants of the TND change. A key example was the case where natural infection protects against reinfection. Because unvaccinated people are more likely to be naturally infected, their rate of observation declines faster through time than the rate of observation for vaccinated people. This leads to underestimates of vaccine efficacy (with a few exceptional edge cases depending on vaccine mechanism of action). This particular example was easy to derive mathematically, and it illustrated the broader point that a changing _relative_ rate of observation of vaccinated vs. unvaccinated people through time causes bias in the TND estimator.

Similarly, time dynamics can cause biases in the TND estimator of protection afforded by antibodies. Thus, relaxing the assumption that all people in the study are sampled in a short time window $\Delta t$ can cause bias. Although a specific example is harder to pinpoint, general reasoning will suffice. According to transmission dynamics, the force of exposure can vary through time, and differently for the focal vs. non-focal pathogen. Moreover, the distribution of antibody titers in the population $D$ also changes through time, as individuals experience boosting and waning.

Thus, we have $\varepsilon (t)$ and $D(x, t)$. Suppose that individuals are observed over the time window from $t_1$ to $t_2$. Even if we continue to invoke other simplifying assumptions above, the expanded time window of collection means that:

$$
\begin{align*}
\mathrm{Protection(X=x)} &= 1 - \frac{C_{F,X=x}C_{N,X=0}}{C_{F,X=0}C_{N,X=x}} \\
&= 1 - \frac{\int_{t1}^{t2}\varepsilon_{F,X=x}(t)D(x,t) \,dt\ \lambda_{F,X=x}\pi_{F,X=x}\mu_{X=x}\int_{t1}^{t2}\varepsilon_{N,X=0}(t)D(0,t) \,dt\ \lambda_{N,X=0}\pi_{N,X=0}\mu_{X=0}}{\int_{t1}^{t2}\varepsilon_{F,X=0}(t)D(0,t) \,dt\ \lambda_{F,X=0}\pi_{F,X=0}\mu_{X=0}\int_{t1}^{t2}\varepsilon_{N,X=x}(t)D(x,t) \,dt\ \lambda_{N,X=x}\pi_{N,X=x}\mu_{X=x}} \\
&= 1 - \frac{\int_{t1}^{t2}\varepsilon_{F,X=x}(t)D(x,t) \,dt\ \int_{t1}^{t2}\varepsilon_{N,X=0}(t)D(0,t) \,dt\ }{\int_{t1}^{t2}\varepsilon_{F,X=0}(t)D(0,t) \,dt\ \int_{t1}^{t2}\varepsilon_{N,X=x}(t)D(x,t) \,dt\ }\theta \\
\end{align*}
$$

Clearly this does not reduce to the correct value of $1 - \theta$ in general. Although this could reduce to $1 - \theta$ if the time-dynamic force of exposure is always equivalent between the focal and non-focal pathogens (i.e. $\varepsilon_{F}(t) = \varepsilon_{N}(t), \forall t \in [t_1, t_2]$), this was not one of the original assumptions and seems highly unlikely.

#### Other Biasing Conditions

We could continue to consider other biasing conditions: when the force of exposure differs by antibody titer _and_ TND data are collected over a time periood, when the diagnostic test for the focal pathogen has imperfect specificity and/or sensitivity, etc. But there is no way to be exhaustive. The above should suffice to show that estimating protection afforded by a continuous antibody titer via the TND design is largely similar to, but at times simpler than, the analogous problem of vaccine efficacy.

## Statistical Estimation

\[Upcoming material\] Investigate how logistic regression is able to estimate the terms needed to calculate protection and its uncertainty, along with the conditions under which logistic regression fails.
