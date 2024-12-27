import tnd


class TestEVRREstimator:
    def test_simple(self):
        """
        Assume:
          - perfect test performance
          - same exposure probability
          - same infection->test probability
        """
        eps = 0.2
        mu_i = 0.4
        current = tnd.ev_rr_estimator(
            eps_v=eps,
            eps_u=eps,
            lam_v=0.8,
            lam_u=1.0,
            mu_vi=mu_i,
            mu_ui=mu_i,
            mu_vx=0.5,
            mu_ux=0.5,
            sens=1.0,
            spec=1.0,
        )

        assert current == 1.0 - 0.8 / 1.0
