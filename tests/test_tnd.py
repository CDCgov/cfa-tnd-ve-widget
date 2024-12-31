import tnd


class TestEVRREstimator:
    def test_simple(self):
        """
        Assume:
          - perfect test performance
          - exposure probability 1.0
          - same infection->test probability
        """
        eps = 1.0
        lam_v = 0.50
        lam_u = 0.75
        mu_i = 0.4
        mu_x = 0.5
        current = tnd.ev_estimator(
            eps_v=eps,
            eps_u=eps,
            lam_v=lam_v,
            lam_u=lam_u,
            mu_vi=mu_i,
            mu_ui=mu_i,
            mu_vx=mu_x,
            mu_ux=mu_x,
            sens=1.0,
            spec=1.0,
        )

        OR = lam_v / lam_u * (1 - lam_u) / (1 - lam_v)

        assert current == 1.0 - OR
