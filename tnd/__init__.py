import numpy as np


def ev_estimator(
    eps_v: float | np.ndarray,
    eps_u: float | np.ndarray,
    lam_v: float | np.ndarray,
    lam_u: float | np.ndarray,
    mu_vi: float | np.ndarray,
    mu_ui: float | np.ndarray,
    mu_vx: float | np.ndarray,
    mu_ux: float | np.ndarray,
    sens: float | np.ndarray,
    spec: float | np.ndarray,
) -> float | np.ndarray:
    """Expected value of risk ratio estimator

    Args:
        eps_v (np.ndarray): exposure probability among the vaccinated
        eps_u (np.ndarray): exposure probability among the unvaccinated
        lam_v (np.ndarray): infection probability among the exposed vaccinated
        lam_u (np.ndarray): infection probability among the exposed unvaccinated
        mu_vi (np.ndarray): receive test probability among the infected vaccinated
        mu_ui (np.ndarray): receive test probability among the infected unvaccinated
        mu_vx (np.ndarray): receive test probability among the uninfected vaccinated
        mu_ux (np.ndarray): receive test probability among the uninfected unvaccinated
        sens (np.ndarray): test sensitivity
        spec (np.ndarray): test specificity

    Returns:
        np.ndarray: expected value
    """
    # expected proportions of true infection status (i=infected or x=not)
    # by vaccination status (v=vaccinated, u=not)
    vi = eps_v * lam_v
    vx = 1.0 - vi
    ui = eps_u * lam_u
    ux = 1.0 - ui

    # proportions of those individuals who are tested (t)
    tvi = vi * mu_vi
    tvx = vx * mu_vx
    tui = ui * mu_ui
    tux = ux * mu_ux

    # expected proportions of test outcomes (p=positive, n=negative)
    pv = tvi * sens + tvx * (1.0 - spec)
    nv = tvi * (1.0 - sens) + tvx * spec
    pu = tui * sens + tux * (1.0 - spec)
    nu = tui * (1.0 - sens) + tux * spec

    return 1.0 - (pv * nu) / (pu * nv)
