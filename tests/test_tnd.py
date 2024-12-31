import tnd


def test_estimator_simple():
    """
    Assume:
      - perfect test performance
      - exposure probability 1.0
    """
    pe = 1.0
    psev = 0.50
    pseu = 0.75
    psx = 0.4
    current = tnd.estimator(
        pev=pe, peu=pe, psev=psev, pseu=pseu, psx=psx, sens=1.0, spec=1.0
    )

    assert current == 1.0 - psev / pseu
