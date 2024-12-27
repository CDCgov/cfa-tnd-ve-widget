def ev_rr_estimator(eps_v, eps_u, lam_v, lam_u, mu_vi, mu_ui, mu_vx, mu_ux, sens, spec):
    """Expected value of risk ratio estimator

    Args:
        eps_v (_type_): _description_
        eps_u (_type_): _description_
        lam_v (_type_): _description_
        lam_u (_type_): _description_
        mu_vi (_type_): _description_
        mu_ui (_type_): _description_
        mu_vx (_type_): _description_
        mu_ux (_type_): _description_
        sens (_type_): _description_
        spec (_type_): _description_

    Returns:
        _type_: _description_
    """
    return 1.0 - (
        eps_v * lam_v * mu_vi * sens + (1.0 - eps_v * lam_v) * mu_vx * (1.0 - spec)
    ) / (eps_u * lam_u * mu_ui * sens + (1.0 - eps_u * lam_u) * mu_ux * (1.0 - spec))
