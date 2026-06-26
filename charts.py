import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st


def show_pie_chart(matched_skills, missing_skills):

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Matched Skills", "Missing Skills"],
                values=[len(matched_skills), len(missing_skills)],
                hole=0.5,
                marker=dict(
                    colors=["#22c55e", "#ef4444"]
                )
            )
        ]
    )

    fig.update_layout(
    title="Skills Distribution",
    title_x=0.5,
    height=420,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(size=16),
    legend=dict(
        orientation="h",
        y=-0.15,
        x=0.3
    )
)

def show_bar_chart(resume_skills, job_skills):

    data = pd.DataFrame({
        "Category": ["Resume Skills", "Job Skills"],
        "Count": [len(resume_skills), len(job_skills)]
    })

    fig = px.bar(
        data,
        x="Category",
        y="Count",
        color="Category",
        text="Count"
    )

    fig.update_layout(
    title="Skills Distribution",
    title_x=0.5,
    height=420,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(size=16),
    legend=dict(
        orientation="h",
        y=-0.15,
        x=0.3
    )
    )
    
    st.plotly_chart(fig, use_container_width=True)