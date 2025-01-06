import pytest
import streamlit.testing.v1

import tnd


@pytest.mark.filterwarnings(
    r"ignore:\s+Deprecated since `altair=5.5.0`. Use altair.theme instead."
)
def test_app_simple():
    """
    End to end app test

    Ignore altair deprecation warning
    """
    at = streamlit.testing.v1.AppTest.from_file("tnd/app.py")
    at.run()
    assert not at.exception


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
