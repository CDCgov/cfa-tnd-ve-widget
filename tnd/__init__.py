import numpy as np


def ev_rr_estimator(
    eps_v: np.ndarray,
    eps_u: np.ndarray,
    lam_v: np.ndarray,
    lam_u: np.ndarray,
    mu_vi: np.ndarray,
    mu_ui: np.ndarray,
    mu_vx: np.ndarray,
    mu_ux: np.ndarray,
    sens: np.ndarray,
    spec: np.ndarray,
) -> np.ndarray:
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
    return 1.0 - (
        eps_v * lam_v * mu_vi * sens + (1.0 - eps_v * lam_v) * mu_vx * (1.0 - spec)
    ) / (eps_u * lam_u * mu_ui * sens + (1.0 - eps_u * lam_u) * mu_ux * (1.0 - spec))
