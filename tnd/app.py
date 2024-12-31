from typing import Optional

import altair as alt
import numpy as np
import polars as pl
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

import tnd


def pct_int(x: Optional[float]) -> Optional[int]:
    """Convert a proportion to an integer percentage"""
    if x is None:
        return None
    else:
        return int(round(x * 100))


def percent_slider(
    generator: DeltaGenerator,
    label: str,
    default: Optional[float] = None,
    min_value: float = 0.0,
    max_value: float = 1.0,
    **kwargs,
):
    """Input and return proportions, but display a slider with percents"""
    value = generator.slider(
        label,
        value=pct_int(default),
        min_value=pct_int(min_value),
        max_value=pct_int(max_value),
        step=1,
        format="%i%%",
        **kwargs,
    )
    return float(value) / 100.0


def make_model_tab(g: DeltaGenerator, n_x: int = 101):
    # default values
    pe = 0.1
    psx = 0.2

    g.header("Input parameters")
    pev = percent_slider(g, "Vaccinated: Probability exposed", default=pe, key="pev")
    peu = percent_slider(g, "Unvaccinated: Probability exposed", default=pe, key="peu")
    pseu = percent_slider(
        g, "Unvaccinated: Probability symptomatic infected given exposed", default=0.25
    )
    psx = percent_slider(
        g, "Probability of non-infection symptoms", min_value=0.01, default=0.2
    )
    sens = percent_slider(g, "Sensitivity", min_value=0.01, default=0.95)
    spec = percent_slider(g, "Specificity", min_value=0.01, default=0.98)

    true_ve = np.linspace(0.0, 1.0, num=n_x)
    psev = (1.0 - true_ve) * pseu

    est_ve = tnd.estimator(
        pev=pev,
        peu=peu,
        psev=psev,
        pseu=pseu,
        psx=psx,
        sens=sens,
        spec=spec,
    )

    data = pl.DataFrame(
        {
            "True VE": true_ve * 100,
            "Estimated VE": est_ve * 100,
        }
    )

    xy_line = (
        alt.Chart(data)
        .mark_line(strokeDash=[8, 8], color="gray")
        .encode(alt.X("True VE"), alt.Y("True VE", title="Estimated VE"))
    )

    ve_line = (
        alt.Chart(data)
        .mark_line()
        .encode(
            alt.X("True VE", scale=alt.Scale(domain=[0, 100])), alt.Y("Estimated VE")
        )
    )

    g.header("Results")
    g.altair_chart(xy_line + ve_line)  # type: ignore


def make_notes_tab(g: DeltaGenerator):
    """Make an explainer tab"""

    g.markdown("""
        # Assumptions in the widget

        - Probability of testing given symptoms is the same for vaccinated and unvaccinated
    """)

    # just read in the primer and stick it here
    with open("docs/primer_short.md", "r") as f:
        primer_content = f.read()

    c = g.container(border=True)
    c.markdown(primer_content)


def app():
    st.title("TND VE estimator widget")
    tabs = st.tabs(["Model", "Notes"])
    make_model_tab(tabs[0])
    make_notes_tab(tabs[1])


if __name__ == "__main__":
    app()
