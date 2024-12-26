# Test-negative design: primer

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

---

## Concept of Protection

If we are to evaluate how well protection can be estimated, we must first define protection axiomatically.

### General Definition

Protection is the reduction in probability of an adverse outcome due to some intervention.

$$Protection = 1 - \frac{P\left( \text{outcome\ } \right|\ intervention)}{P\left( \text{outcome\ } \right|\ \sim intervention)}$$

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

  - probability of infection is denoted P(S)

- Progression to severe illness:

  - acute respiratory illness (ARI), given infection with the focal pathogen

  - probability of severe ARI given infection is denoted P(P \| S)

- Susceptibility to infection AND progression to severe illness:

  - both infection and ARI together, as one event

  - probability of severe infection is denoted P(PS) = P(P \| S) \* P(S)

Together, these form six combinations, or six possible precise definitions of protection. To start, we consider just one: vaccine-based protection against severe infection.

- We consider vaccination first because binary vaccination is simpler than continuous antibody titers.

- We consider severe infection first because infection and severity cannot be decomposed under some common study designs.

## Test Negative Design (TND)

Our study design of interest is the test-negative design (TND), in which all individual sampled are seeking care due to ARI. They fall into the following four categories of counts:

                       Vaccinated   Unvaccinated

---

Focal Pathogen C~FV~ C~FU~ Non-Focal Pathogen C~NV~ C~NU~

Because infection is never observed in the absence of ARI, TND cannot decompose infection from severity; it can only address severe infection as one event.

## Mathematical Notation and Notes

This is our mathematical language for investigating how well the TND can approximate protection.

### Notation

F = \[event\] severe illness with the focal pathogen

N = \[event\] severe illness with non-focal pathogens

V = \[event\] vaccination against the focal pathogen

U = \[event\] lack of vaccination against the focal pathogen

P = \[parameter\] population size

v = \[parameter\] proportion of the population that is vaccinated

ε = \[parameter\] rate of exposure per person per unit time (may depend on F vs. N and/or V vs. U)

λ = \[parameter\] probability of infection given exposure (may depend on F vs. N and/or V vs. U)

π = \[parameter\] probability of ARI given infection (may depend on F vs. N and/or V vs. U)

µ = \[parameter\] probability of seeking care given ARI (may depend on V vs. U but not F vs. N)

$\varphi$ = \[parameter\] probability that a vaccinated person responds to vaccination

θ~λ~ = $\frac{\lambda_{\text{FV}}}{\lambda_{\text{FU}}}$ \[parameter\] vaccine reduction in risk of infection with the focal pathogen given exposure

θ~π~ = $\frac{\pi_{\text{FV}}}{\pi_{\text{FU}}}$ \[parameter\] vaccine reduction in risk of ARI given infection with the focal pathogen

θ = θ~λ~θ~π~ \[parameter\] vaccine reduction in risk of ARI due to the focal pathogen given exposure

$t$ = time since the disease season began

### Notes

There are several important facts that we must be careful not to overlook.

#### Vaccines Have Multiple Effects

We have declared several parameters related to vaccine action, which allow a spectrum of scenarios:

- If θ = 0 and $\varphi$ \< 1, we have "all-or-nothing" action: vaccination either completely protects an individual from severe infection, or else it provides no protection at all.

- If 0 \< θ and $\varphi$ = 1, we have "leaky" action: every vaccinated individual has a positive but reduced probability of severe infection, compared to unvaccinated individuals.

#### Vaccines Correlate with Behavior

Vaccination is not just a cause of immune fortification; it is also a consequence of behavioral choices. For example, we recognize that vaccinated individuals may have a different propensity to seek care in response to ARI compared to unvaccinated individuals (µ~V~ vs. µ~U~). Spoiler: these behavioral differences can ultimately bias TND-derived estimates of protection. So, to start, we remove them via assumptions:

- Differences in λ and π with vaccination are entirely immunological, not behavioral.

- The force of exposure ε does not differ based on vaccination.

#### Observation Occurs Through Time

The counts of people in each quadrant of the TND accumulate through time, during which dynamic processes (e.g. transmission, recovery, etc.) occur. Spoiler: these dynamics are ultimately responsible for biasing TND-derived estimates of protection. So, to start, we remove time dynamics via assumptions:

- No parameters change through time. For example, even the force of exposure ε is constant.

- Infection provides no protection. Infected individuals are not removed from the susceptible pool.

- All vaccines are administered at $t = 0$ and the effects of vaccination do not wane in time.

## Concept of Protection Revisited

Using our mathematical language, we can write a formula for the precise definition of protection.

$$VE = 1 - \frac{P\left( \text{F\ } \right|\ V)}{P\left( \text{F\ } \right|\ U)} = 1 - \frac{\left( 1 - \varphi \right)\varepsilon_{\text{FV}}\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\varepsilon_{\text{FV}}\lambda_{\text{FV}}\pi_{\text{FV}}}{\varepsilon_{\text{FU}}\lambda_{\text{FU}}\pi_{\text{FU}}} = 1 - \frac{\varepsilon_{\text{FV}}}{\varepsilon_{\text{FU}}}\left( 1 - \ \varphi + \varphi\theta \right) = \ \varphi(1 - \theta)\ $$

Note the importance of assuming that ε does not depend on vaccination.

We will use the axiom $VE = 1 - \frac{P\left( \text{F\ } \right|\ V)}{P\left( F \right|\ U)}$ to pose candidate formulae of TND data to estimate VE.

We will use the equality $\text{VE} = \ \varphi(1 - \theta)$ to verify whether these candidate formulae are correct.

## Estimating Protection from TND

Attempting to pose a formula for a TND estimate of VE reveals common pitfalls and ultimately explains why an odds ratio is required.

### Direct Risk Ratio from Counts Alone Fails

At first, it may appear that the terms of the axiomatic definition of protection are directly available in the TND data. We replace the conditional probabilities using the formula P(AB) = P(A\|B)P(B):

$$VE = 1 - \frac{P\left( \text{F\ } \right|\ V)}{P\left( \text{F\ } \right|\ U)} = 1 - \frac{\frac{P(FV)}{P(V)}}{\frac{P(FU)}{P(U)}}$$

Let C represent the counts in each quadrant of the TND data. It may appear that:

$$VE = \ 1 - \frac{\frac{P(FV)}{P(V)}}{\frac{P(FU)}{P(U)}} = 1 - \ \frac{\frac{C_{\text{FV}}}{(C_{\text{FV}} + \ C_{\text{NV}})}}{\frac{C_{\text{FU}}}{(C_{\text{FU}} + \ C_{\text{NU}})}}$$

However, this is not true, because $C_{\text{FV}} + \ C_{\text{NV}} \propto P\left( \text{V\ and\ ARI\ and\ careseeking} \right) \neq P(V)$. Similarly, $C_{\text{FU}} + \ C_{\text{NU}} \propto P\left( \text{U\ and\ ARI\ and\ careseeking} \right) \neq P(U)$.

### Direct Risk Ratio from Counts and Outside Knowledge Fails

To address this pitfall, one may assume that the vaccination rate v is known from other means outside the TND. In this case:

$$VE = \ 1 - \frac{\frac{P\left( \text{FV} \right)}{P\left( V \right)}}{\frac{P\left( \text{FU} \right)}{P\left( U \right)}} = 1 - \ \frac{\frac{C_{\text{FV}}}{\text{vP}}}{\frac{C_{\text{FU}}}{\left( 1 - v \right)P}}$$

According to the assumptions we've made, the cumulative counts of people in the TND at time $t$ will be:

$C_{\text{FV}} = \varepsilon_{\text{FV}}tvP\lbrack\left( 1 - \varphi \right)\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\lambda_{\text{FV}}\pi_{\text{FV}}\rbrack\mu_{V}$ $C_{\text{FU}} = \varepsilon_{\text{FU}}t\left( 1 - v \right)P\lambda_{\text{FU}}\pi_{\text{FU}}\mu_{U}$

$C_{\text{NV}} = \varepsilon_{\text{NV}}\text{tvP}\lambda_{\text{NV}}\pi_{\text{NV}}\mu_{V}$ $C_{\text{NU}} = \varepsilon_{\text{NU}}t(1 - v)P\lambda_{\text{NU}}\pi_{\text{NU}}\mu_{U}$

Substituting:

$$VE = \ 1 - \frac{\frac{\varepsilon_{\text{FV}}\text{tvP}\left\lbrack \left( 1 - \varphi \right)\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\lambda_{\text{FV}}\pi_{\text{FV}} \right\rbrack\mu_{V}}{\text{vP}}}{\frac{\varepsilon_{\text{FU}}t\left( 1 - v \right)P\lambda_{\text{FU}}\pi_{\text{FU}}\mu_{U}}{\left( 1 - v \right)P}} = 1 - \frac{\mu_{V}}{\mu_{U}}\left( 1 - \ \varphi + \varphi\theta \right)$$

Again, note the importance of assuming that ε does not depend on vaccination. Even so, this estimate of VE reduces to the correct value, $\varphi(1 + \theta)$, if and only if µ~V~ = µ~U~, which is not generally true. In other words, the differential propensity to seek care with vaccination status prevents the direct risk ratio from accurately estimating VE.

### Derivation of the Odds Ratio

We now see that a simple adjustment for the differential propensity to seek care with vaccination status will guarantee that our posed formula reduces to the correct value of VE:

$$VE = 1 - \ \frac{\frac{C_{\text{FV}}}{\text{vP}}}{\frac{C_{\text{FU}}}{\left( 1 - v \right)P}}\frac{\mu_{U}}{\mu_{V}} = 1 - \frac{\mu_{V}}{\mu_{U}}\frac{\mu_{U}}{\mu_{V}}\left( 1 - \ \varphi + \varphi\theta \right) = \varphi(1 - \theta)$$

But how should $\frac{\mu_{U}}{\mu_{V}}$ be estimated from TND data? If we assume that vaccination status does not affect any aspect of the non-focal pathogens (ε~N~, λ~N~, or π~N~), then the only reasons that the number of people seeking care for ARI due to non-focal pathogens would differ by vaccination status are:

- the propensity to seek care differs by vaccination status, and

- different numbers of people are vaccinated vs. unvaccinated.

So we claim $\frac{\mu_{U}}{\mu_{V}}\frac{\left( 1 - v \right)P}{\text{vP}} = \frac{C_{\text{NU}}}{C_{\text{NV}}}$, or equivalently $\frac{\mu_{U}}{\mu_{V}} = \frac{C_{\text{NU}}}{C_{\text{NV}}}\frac{\text{vP}}{\left( 1 - v \right)P}$. Thus, we can say:

$$VE = \ 1 - \ \frac{\frac{C_{\text{FV}}}{\text{vP}}}{\frac{C_{\text{FU}}}{\left( 1 - v \right)P}}\frac{C_{\text{NU}}\text{vP}}{C_{\text{NV}}\left( 1 - v \right)P} = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}}$$

After some convenient canceling, we have an unbiased estimate of VE that only uses TND quadrants! In particular, an outside source of information giving v is unnecessary. Furthermore, note that:

$$VE = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}} = 1 - \frac{P\left( \text{FV} \right)P\left( \text{NU} \right)}{P\left( \text{FU} \right)P\left( \text{NV} \right)} = 1 - \frac{\frac{P\left( \text{FV} \right)}{P\left( \text{FU} \right)}}{\frac{P\left( \text{NV} \right)}{P\left( \text{NU} \right)}} = 1 - \frac{\frac{\frac{P\left( \text{FV} \right)}{P\left( F \right)}}{\frac{P\left( \text{FU} \right)}{P\left( F \right)}}}{\frac{\frac{P\left( \text{NV} \right)}{P\left( N \right)}}{\frac{P\left( \text{NU} \right)}{P\left( N \right)}}} = 1 - \frac{\frac{P(V|F)}{P(U|F)}}{\frac{P(V|N)}{P(U|N)}}$$

The final expression for VE is the odds ratio of vaccination given exposure ("OR"). Thus, it can be helpful to think of the odds ratio used in TND this way: the TND expression for VE uses an odds ratio _not_ because protection itself is an odds ratio (it is not), but because correcting the risk ratio of protection for differential care-seeking behavior happens to result in a formula that is equivalent to an odds ratio.

## When TND Fails

Note how many assumptions were required to make the formula VE = 1 -- OR true. These assumptions about the force of infection and time dynamics are likely false. Relaxing these assumptions will bias the estimator of VE. Now we explore how relaxing specific assumptions causes specific biases in 1 -- OR.

### Force of Exposure Differs by Vaccination Status

We relax the assumption that vaccination does not correlate with force of exposure, so that in general $\varepsilon_{\text{FV}} \neq \varepsilon_{\text{FU}}$ and $\varepsilon_{\text{NV}} \neq \varepsilon_{\text{NU}}$. Many factors can influence this in different directions; for example, perhaps:

- People who choose to get vaccinated also choose to avoid contacts more frequently

- People who choose to get vaccinated live in more densely populated contact-rich areas

Note that we continue to assume that any particular force of exposure ε is constant, and that natural infection provides no protection against natural infection. Under these assumptions:

$$VE = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}} = \ 1 - \frac{\left( \varepsilon_{\text{FV}}\text{tvP}\left\lbrack \left( 1 - \varphi \right)\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\lambda_{\text{FV}}\pi_{\text{FV}} \right\rbrack\mu_{V} \right)\left( \varepsilon_{\text{NU}}t\left( 1 - v \right)P\lambda_{\text{NU}}\pi_{\text{NU}}\mu_{U} \right)}{\left( \varepsilon_{\text{FU}}t\left( 1 - v \right)P\lambda_{\text{FU}}\pi_{\text{FU}}\mu_{U} \right)\left( \varepsilon_{\text{NV}}\text{tvP}\lambda_{\text{NV}}\pi_{\text{NV}}\mu_{V} \right)}$$

$$= \ 1 - \frac{\left( \varepsilon_{\text{FV}}\left\lbrack \left( 1 - \varphi \right)\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\lambda_{\text{FV}}\pi_{\text{FV}} \right\rbrack \right)\left( \varepsilon_{\text{NU}}\lambda_{\text{NU}}\pi_{\text{NU}} \right)}{\left( \varepsilon_{\text{FU}}\lambda_{\text{FU}}\pi_{\text{FU}} \right)\left( \varepsilon_{\text{NV}}\lambda_{\text{NV}}\pi_{\text{NV}} \right)}\text{\ \ \ \ }$$

By continuing to assume that λ and π are purely immunological, such that λ~N~ and π~N~ are unimpacted by vaccination (i.e., $\lambda_{\text{NV}} = \lambda_{\text{NU}}$ and $\pi_{\text{NV}} = \pi_{\text{NU}}$):

$$= \ 1 - \frac{\varepsilon_{\text{FV}}\varepsilon_{\text{NU}}}{\varepsilon_{\text{FU}}\varepsilon_{\text{NV}}}\left( 1 - \ \varphi + \varphi\theta \right)\text{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }$$

The term $\frac{\varepsilon_{\text{FV}}\varepsilon_{\text{NU}}}{\varepsilon_{\text{FU}}\varepsilon_{\text{NV}}}$ no longer reduces to 1 by assumption, so the TND VE estimate of 1 -- OR no longer _necessarily_ reduces to the correct value of $\varphi(1 + \theta)$. However, $\frac{\varepsilon_{\text{FV}}\varepsilon_{\text{NU}}}{\varepsilon_{\text{FU}}\varepsilon_{\text{NV}}}$ _can_ still reduce to 1, resulting in an unbiased estimate of VE. All that is required is a weaker assumption that vaccination correlates with force of exposure identically for different pathogens, such that $\varepsilon_{\text{FV}} \neq \varepsilon_{\text{FU}}$ and $\varepsilon_{\text{NV}} \neq \varepsilon_{\text{NU}}$ but $\frac{\varepsilon_{\text{FV}}}{\varepsilon_{\text{FU}}} = \frac{\varepsilon_{\text{NV}}}{\varepsilon_{\text{NU}}}$.

If this weaker assumption is true, 1 -- OR is still an unbiased estimate of VE; otherwise, 1 -- OR is biased in a way that depends on the values of ε~FV~, ε~FU~, ε~NV~, and ε~NU~.

### Natural Infection Protects against Re-Infection

We assume that infection with the focal pathogen provides complete protection, rather than no protection at all. Importantly, this change does not extend to non-focal pathogens. Even if one non-focal pathogen stimulates complete protection, there are many other non-focal pathogens that can still infect. Thus, we retain the assumption that natural infection provides no protection for non-focal pathogens.

As a result, the number of people susceptible to non-focal pathogens remains constant at P over time, whereas the number of people susceptible to the focal pathogen decays as $e^{- \varepsilon_{F}\lambda_{F}t}$. Accordingly, the cumulative counts of people observed in the TND with the focal pathogen at time $t$ will be:

$C_{\text{FV}} = vP\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FU}}t})\pi_{\text{FU}} + \ \varphi(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t})\pi_{\text{FV}}\rbrack\mu_{V}$

$$C_{\text{FU}} = \left( 1 - v \right)P(1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t})\pi_{\text{FU}}\mu_{U}$$

Now the 1 -- OR estimate of VE becomes:

$$VE = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}} = \ 1 - \frac{vP\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FU}}t})\pi_{\text{FU}} + \ \varphi(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t})\pi_{\text{FV}}\rbrack\mu_{V})\left( \varepsilon_{\text{NU}}t\left( 1 - v \right)P\lambda_{\text{NU}}\pi_{\text{NU}}\mu_{U} \right)}{\left( \left( 1 - v \right)P(1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t})\pi_{\text{FU}}\mu_{U} \right)\left( \varepsilon_{\text{NV}}\text{tvP}\lambda_{\text{NV}}\pi_{\text{NV}}\mu_{V} \right)}$$

$$= \ 1 - \frac{\lbrack\left( 1 - \varphi \right)(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FU}}t})\pi_{\text{FU}} + \ \varphi(1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t})\pi_{\text{FV}}\rbrack)\left( \varepsilon_{\text{NU}}\lambda_{\text{NU}}\pi_{\text{NU}} \right)}{\left( (1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t})\pi_{\text{FU}} \right)\left( \varepsilon_{\text{NV}}\lambda_{\text{NV}}\pi_{\text{NV}} \right)}$$

As above, we will continue to assume that $\lambda_{\text{NV}} = \lambda_{\text{NU}}$ and $\pi_{\text{NV}} = \pi_{\text{NU}}$. And we will reimpose the assumption that $\varepsilon_{\text{FV}} = \varepsilon_{\text{FU}}$ and $\varepsilon_{\text{NV}} = \varepsilon_{\text{NU}}$, to better isolate the consequences of natural protection:

$$= 1 - \left( 1 - \varphi \right) - \varphi\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}}\frac{\pi_{\text{FV}}}{\pi_{\text{FU}}} = \varphi\left( 1 - \theta_{\pi}\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} \right)\text{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }$$

Because the term $\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}}$ is not necessarily equal to θ~λ~, the TND VE estimate of 1 -- OR no longer necessarily reduces to the correct value of $\varphi(1 - \theta)$. In fact, 1 -- OR only reduces to the correct value of $\varphi(1 + \theta)$ under one of the following conditions:

- $\lambda_{\text{FV}} = \lambda_{\text{FU}}$, that is, vaccination does not affect the probability of infection given exposure to the focal pathogen. In this case, $VE = \ \varphi\left( 1 - \theta_{\pi} \right) = \varphi\left( 1 - \theta \right)$ because $\theta = \theta_{\lambda}\theta_{\pi} = 1*\theta_{\pi} = \theta_{\pi}$. Note that vaccination may still affect the probability of ARI given infection, π. Thus, 1 -- OR can be unbiased under "leaky" vaccination, so long as vaccination reduces the probability of ARI, not infection itself.

- $\lambda_{\text{FV}} = 0$, that is, vaccination provides perfect protection against infection given exposure to the focal pathogen. In this case, $VE = \ \varphi = \varphi\left( 1 - \theta \right)$ because $\theta = \theta_{\lambda}\theta_{\pi} = 0*\theta_{\pi} = 0$. Note that vaccination may still affect the probability of ARI given infection, π, although this is meaningless because successfully vaccinated people never get infected. As such, this condition is equivalent to all-or-nothing vaccination, in which $\varphi$ ≤ 1 and θ = 0.

Outside of these conditions, the value of the term $\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}}$ varies in time, so it cannot equal the constant value θ~λ~. At best, this term can equal θ~λ~ at exactly one time point, meaning 1 -- OR will be unbiased at only one time point. We can show that this time point is $t = 0$ using L'Hôpitál's Rule:

$$\lim_{t \rightarrow 0}\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} = \lim_{t \rightarrow 0}\frac{\varepsilon_{\text{FV}}\lambda_{\text{FV}}e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{\varepsilon_{\text{FU}}\lambda_{\text{FU}}e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} = \frac{\varepsilon_{\text{FV}}\lambda_{\text{FV}}}{\varepsilon_{\text{FU}}\lambda_{\text{FU}}} = \frac{\lambda_{\text{FV}}}{\lambda_{\text{FU}}} = \theta_{\lambda}$$

Again, note the importance of reinstating the assumption that $\varepsilon_{\text{FV}} = \varepsilon_{\text{FU}}$. Also, note that as $t \rightarrow 0$ from the right, $\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} \rightarrow \theta_{\lambda}$ from above. Thus, for times beyond $t = 0$, 1 -- OR yields $VE < \ \varphi\left( 1 - \theta \right)$.

In sum, if vaccination reduces but does not eliminate the probability of infection given exposure to the focal pathogen, then 1 -- OR will underestimate the true value of VE for times beyond the very beginning of the season. In loose terms, protection against the focal pathogen derived from natural infections causes the susceptible population to dwindle. This dwindling through time occurs disproportionately in the unvaccinated, who are more likely to experience natural infections. The same process does not occur for non-focal pathogens, for which natural infections do not provide protection. Thus, the term C~FU~ in $VE = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}}$ shrinks disproportionately as time passes, causing the estimate of VE to also shrink.

### Different Force of Exposure and Natural Protection

If both assumptions discussed above are broken at once, such that the force of exposure differs by vaccination status and the focal pathogen provides natural protection, then 1 -- OR gives:

$$VE = 1 - \frac{C_{\text{FV}}C_{\text{NU}}}{C_{\text{FU}}C_{\text{NV}}} = \ 1 - \frac{\varepsilon_{\text{NU}}}{\varepsilon_{\text{NV}}}\left\lbrack \left( 1 - \varphi \right)\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FU}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} + \varphi\theta_{\pi}\frac{1 - e^{- \varepsilon_{\text{FV}}\lambda_{\text{FV}}t}}{1 - e^{- \varepsilon_{\text{FU}}\lambda_{\text{FU}}t}} \right\rbrack \neq \varphi\left( 1 - \theta \right)$$

In this case, the bias in the TND estimate of VE depends on the relative force of exposure between vaccinated and unvaccinated people, for all pathogens. Unlike in Section 6.1, assuming that vaccination correlates with force of exposure identically for different pathogens ($\frac{\varepsilon_{\text{FV}}}{\varepsilon_{\text{FU}}} = \frac{\varepsilon_{\text{NV}}}{\varepsilon_{\text{NU}}}$) no longer corrects this.

Two further observations about these assumptions are also warranted:

- The disparity in force of exposure by vaccination status is what biases 1 -- OR. Different forces of exposure between the focal and non-focal pathogens (i.e. $\varepsilon_{F} \neq \varepsilon_{N}$), even if these forces are dynamic in time (i.e. $\varepsilon_{F}\left( t \right) \neq \varepsilon_{N}(t)$), do not contribute to the bias.

- The disparity in natural protection between the focal and non-focal pathogens need not be so exaggerated (i.e. complete vs. non-existent, respectively). Any disparity in natural protection will bias 1 -- OR for the same reasons described in Section 6.2, albeit perhaps to a lesser extent.

### Behavioral Correlations between Vaccination and Susceptibility/Severity

Even when $1 - OR = \ \varphi\left( 1 - \theta \right) = \ \varphi\left( 1 - \frac{\lambda_{\text{FV}}}{\lambda_{\text{FU}}}\frac{\pi_{\text{FV}}}{\pi_{\text{FU}}} \right)$, bias may be lurking in the interpretation. VE is typically interpreted as purely a result of vaccine-stimulated immune defense. But perhaps $\lambda_{\text{FV}} \neq \lambda_{\text{FU}}$ and/or $\pi_{\text{FV}} \neq \pi_{\text{FU}}$ for reasons unrelated to immunological action. For example:

- Individuals at high risk of infection given exposure (e.g. elderly, some immunocompromised) may be more likely to get vaccinated than the general public. In this case, the realized value of $\theta_{\lambda} = \frac{\lambda_{\text{FV}}}{\lambda_{\text{FU}}}$ is closer to 1 than it would be if it only captured immunological phenomena.

- Individuals who get vaccinated may be more likely to use at-home treatments for mild illness which help prevent progression to ARI. In this case, the realized value of $\theta_{\pi} = \frac{\pi_{\text{FV}}}{\pi_{\text{FU}}}$ is closer to 0 than it would be if it only captured immunological phenomena.

These examples show that a purely immunological interpretation of VE could under- or overestimate the impact of vaccination, depending on which conditions and behaviors correlate with vaccination.

### Probability of Being Tested Differs by Disease and Vaccination Status

To this point, we have tacitly assumed that everyone with ARI who seeks care is tested for the causal pathogen. But in practice, ARI symptoms may manifest differently based on the causal pathogen and/or vaccination status, leading to different probabilities of a clinician deciding to administer a test. If we reimpose all previous assumptions but introduce ζ as the probability of being tested, we have:

$$VE = \ 1 - \frac{\left( \varepsilon_{\text{FV}}\text{tvP}\left\lbrack \left( 1 - \varphi \right)\lambda_{\text{FU}}\pi_{\text{FU}} + \ \varphi\lambda_{\text{FV}}\pi_{\text{FV}} \right\rbrack\mu_{V}\zeta_{\text{FV}} \right)\left( \varepsilon_{\text{NU}}t\left( 1 - v \right)P\lambda_{\text{NU}}\pi_{\text{NU}}\mu_{U}\zeta_{\text{NU}} \right)}{\left( \varepsilon_{\text{FU}}t\left( 1 - v \right)P\lambda_{\text{FU}}\pi_{\text{FU}}\mu_{U}\zeta_{\text{FU}} \right)\left( \varepsilon_{\text{NV}}\text{tvP}\lambda_{\text{NV}}\pi_{\text{NV}}\mu_{V}\zeta_{\text{NV}} \right)} = \ 1 - \frac{\zeta_{\text{FV}}\zeta_{\text{NU}}}{\zeta_{\text{FU}}\zeta_{\text{NV}}}\left( 1 - \ \varphi + \varphi\theta \right)$$

Thus, unless the effect of vaccination on the probability of being tested is identical for both the focal and non-focal pathogens, $\frac{\zeta_{\text{FV}}}{\zeta_{\text{FU}}} = \frac{\zeta_{\text{NV}}}{\zeta_{\text{NU}}}$, then testing probability also contributes to bias in 1 -- OR.

## Conclusions

1 -- OR from a TND study is an unbiased estimator of VE only under a restrictive and unrealistic set of assumptions. Violating these assumptions introduces biases which can be understood in isolation, but which may interact with one another in complicated ways. Nonetheless, some themes emerge:

- The transmission and/or disease caused by the focal vs. non-focal pathogens need not be identical, but they must respond to vaccination identically (except for λ and π), to avoid bias.

- Dynamics cause bias not because the rates of observing TND quadrants changes through time, but because the _relative_ rates of observing vaccinated vs. unvaccinated TND quadrants change through time.

Using these conclusions and the mathematical language developed above, the biasing effect of other factors not discussed here (e.g. vaccine waning through time) on VE should be more easily investigated.

## Protection from Antibodies

\[Upcoming material\] Investigate how the math changes when vaccination (a binary event) is replaced with antibody titer (a continuous measure).

## Statistical Estimation

\[Upcoming material\] Investigate how logistic regression is able to estimate the terms needed to calculate protection and its uncertainty, along with the conditions under which logistic regression fails.
