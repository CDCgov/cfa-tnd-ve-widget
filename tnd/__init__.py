import numpy as np


def estimator(
    pev: float | np.ndarray,
    peu: float | np.ndarray,
    psev: float | np.ndarray,
    pseu: float | np.ndarray,
    psx: float | np.ndarray,
    sens: float | np.ndarray,
    spec: float | np.ndarray,
) -> float | np.ndarray:
    """Expected value of risk ratio estimator

    Assume that conditional probability of testing does not depend on the cause of symptoms.

    Args:
        pev (np.ndarray): probability of exposure among the vaccinated
        peu (np.ndarray): probability of exposure among the unvaccinated
        psev (np.ndarray): probability of symptomatic infection given exposure among the vaccinated
        pseu (np.ndarray): probability of symptomatic infection given exposure among the unvaccinated
        psx (np.ndarray): probability of symptoms without exposure
        sens (np.ndarray): test sensitivity
        spec (np.ndarray): test specificity

    Returns:
        np.ndarray: expected value
    """
    # counts of those individuals who are:
    # - vaccinated (v) or unvaccinated (u)
    # - infected (i) or not (x)
    # excluding factors of:
    # - population size
    # - v or (1-v)
    # - conditional testing probabilities
    vi = psev * pev
    vx = psx
    ui = pseu * peu
    ux = psx

    # test outcomes (p=positive, n=negative)
    pv = sens * vi + (1.0 - spec) * vx
    nv = (1.0 - sens) * vi + spec * vx
    pu = sens * ui + (1.0 - spec) * ux
    nu = (1.0 - sens) * ui + spec * ux

    return 1.0 - (pv * nu) / (pu * nv)
