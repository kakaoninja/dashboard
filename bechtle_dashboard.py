import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import base64

hole_radius = 0.7


with open("assets/BechtlePro.woff2", "rb") as f:
    font_data = base64.b64encode(f.read()).decode()

# Page config
st.set_page_config(
    page_title="Bechtle & Cybersecurity Dashboard",
    # layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
    }
    h1 {
        color: #1f77b4;
        padding-bottom: 20px;
    }
    h2 {
        color: #2c3e50;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    
    @font-face {
        font-family: 'MyCustomFont';
        src: url('assets/BechtlePro.woff2') format('woff2');
        font-weight: 200;
        font-style: normal;
    }
    
    html, body, [class*="css"] {
        font-family: 'MyCustomFont', sans-serif;
        font-weight: 200 !important;
    }
    
    h1, h2, h3, h4, h5, h6, p, div, span {
        font-family: 'MyCustomFont', sans-serif !important;
        font-weight: 200 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title

st.image("logo_bechtle.svg", width=200)
st.markdown("---")

# BECHTLE FINANCIAL DATA
st.header("Financial Data (compared to FY 2023)")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Revenue", "€6.31B", "-1.8%")
    st.metric("Business Volume", "€8B", "+2%")

with col2:
    st.metric("EBIT", "€345M", "-8%")
    st.metric("EBIT Margin", "5.5%", "-0.3%")

with col3:
    st.metric("Employees", "15,801", "+642")
    st.metric("Acquisitions", "6", "-1")

with col4:
    st.metric("IT System Revenue", "€5.0B", "79% of total")
    st.metric("Total Acquisitions", "24", "€247M")

st.markdown("---")

# CYBERSECURITY DATA
st.header("Global Cybersecurity Attacks (2024)")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Daily Global Attacks",
        "2,200+",
        "Every 39 seconds",
        delta_color="inverse",
    )

with col2:
    st.metric(
        "Annual Attacks/Org",
        "4 avg.",
        "+25%",
        delta_color="inverse",
    )

with col3:
    st.metric(
        "2024 Cybercrime Cost",
        "€9.5T",
        "Global estimate",
        delta_color="inverse",
    )

with col4:
    st.metric(
        "Avg Data Breach Cost",
        "€4.88M",
        "+10%",
        delta_color="inverse",
    )

# Most targeted sectors
st.subheader("Cyberattacks per organisation per week (2024)")
col1, col2 = st.columns(2)

with col1:
    # Sector attacks
    sectors_data = {
        "Sector": ["Research", "Military", "Healthcare"],
        "Weekly Attacks per Org": [3828, 2553, 2434],
    }
    fig_sector = go.Figure(
        data=[
            go.Pie(
                labels=sectors_data["Sector"],
                values=sectors_data["Weekly Attacks per Org"],
                hole=hole_radius,
                # marker_colors=["#23A96A", "#075033", "#85FE67", "#2FFB95"],
                marker_colors=[
                    "#FF9C5B",
                    "#23A96A",
                    "#27C9D1",
                    "#346CEF",
                    "#AADE0C",
                ],
            )
        ]
    )
    fig_sector.update_layout(
        title="Cyber Attacks per Sector",
        height=400,
        margin=dict(
            r=100,
            # r=20,
            # t=40,
            # b=20,
        ),
    )
    st.plotly_chart(fig_sector, use_container_width=True, width="stretch")
with col2:
    #     # Regional attacks
    regional_data = {
        "Region": ["Ukraine", "United States", "Poland", "Israel", "India"],
        "Weekly Attacks": [
            2000,
            1300,
            1000,
            900,
            750,
        ],  # Approximate based on data
    }
    fig_regional = go.Figure(
        data=[
            go.Pie(
                labels=regional_data["Region"],
                values=regional_data["Weekly Attacks"],
                hole=hole_radius,
                # marker_colors=[
                #     "#27C9D1",
                #     "#346CEF",
                #     "#A774D8",
                #     "#AADE0C",
                #     "#D9486C",
                #     "#FF9C5C",
                # ],
                marker_colors=[
                    "#FF9C5B",
                    "#23A96A",
                    "#27C9D1",
                    "#346CEF",
                    "#AADE0C",
                ],
            )
        ]
    )
    fig_regional.update_layout(
        title="Cyber Attacks per Region",
        height=400,
        margin=dict(
            r=100,
            # r=20,
            # t=40,
            # b=20,
        ),
    )
    st.plotly_chart(fig_regional, use_container_width=True, width="stretch")

# Ransomware statistics
st.subheader("Ransomware Attacks on Organisations")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("France", "74%", "Highest Rate globally", delta_color="inverse")

with col2:
    st.metric(
        "South Africa, Italy, Austria",
        "69%",
        "High vulnerability",
        delta_color="inverse",
    )

with col3:
    st.metric("United States", "59%", "Global average", delta_color="off")

st.markdown("---")
# SUSTAINABILITY DATA
st.header("Sustainability")

col1, col2 = st.columns(2)

with col1:
    st.metric("Scope 1 & 2 Reduction Target (by 2030)", "54.4%")
    st.caption("From 2019 baseline")
    st.metric("Scope 3 Reduction Target (by 2030)", "55%")
    st.caption("Per €1,000 value")

with col2:
    st.metric("Net Zero Target Year", "2050")
    st.caption("SBTi commitment")
    st.metric("EV Charging Stations", "794 bays")
    st.caption("As of Dec 2024")

# sustainability chart

emissions_data = {
    "Year": ["2020", "2021", "2022", "2023", "2024"],
    "Scope 1": [14500, 15060, 18241, 17892, 17500],
    "Scope 2": [7000, 6607, 4563, 4949, 4800],
    "Scope 3": [2020000, 2075731, 2212495, 1987159, 2067700],
    "Total": [2041500, 2097398, 2235336, 2010000, 2090000],
}

df = pd.DataFrame(emissions_data)

# Create stacked horizontal bar chart
fig_stacked = go.Figure()

fig_stacked.add_trace(
    go.Bar(
        y=df["Year"],
        x=df["Scope 1"],
        name="Scope 1 Emissions",
        orientation="h",
        marker_color="#346CEF",
        marker=dict(
            opacity=[
                0.6,
                0.6,
                0.6,
                0.6,
                1,
            ],
        ),
        # hovertemplate="<b>Scope 1</b><br>%{x:,.0f} t CO₂e<extra></extra>",
    )
)

fig_stacked.add_trace(
    go.Bar(
        y=df["Year"],
        x=df["Scope 2"],
        name="Scope 2 Emissions",
        orientation="h",
        marker_color="#D9486C",
        marker=dict(
            opacity=[
                0.6,
                0.6,
                0.6,
                0.6,
                1,
            ],
        ),
        # hovertemplate="<b>Scope 2</b><br>%{x:,.0f} t CO₂e<extra></extra>",
    )
)


fig_stacked.add_trace(
    go.Bar(
        y=df["Year"],
        x=df["Scope 3"],
        name="Scope 3 Emissions",
        orientation="h",
        marker_color="#23A96A",
        marker=dict(
            opacity=[
                0.6,
                0.6,
                0.6,
                0.6,
                1,
            ],
        ),
        hovertemplate="<b>Scope 3</b><br>%{x:,.0f} t CO₂e<extra></extra>",
        text=df["Scope 3"],
        texttemplate="%{text:,.0f}",  # ADD THIS - formats with commas
        textposition="inside",
        textfont=dict(color="white", size=14),
    )
)

fig_stacked.update_layout(
    title="CO2 Emissions by Scope (tonnes CO₂e)",
    # xaxis_title="",
    # yaxis_title="",
    height=400,
    barmode="stack",
    # yaxis=dict(autorange="reversed"),
    xaxis=dict(tickformat=","),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=-0.022,
        traceorder="normal",
        # xref="paper",
    ),
)
max_x = df["Total"].max()

for i, year in enumerate(df["Year"]):
    fig_stacked.add_annotation(
        x=max_x,  # Fixed position instead of df["Total"][i]
        y=year,
        text=f"{df['Total'][i]:,.0f}",
        showarrow=False,
        xanchor="left",
        xshift=10,
        font=dict(size=14, color="black"),
    )

fig_stacked.add_annotation(
    x=max_x,
    y=-0.13,
    text="<b>Total</b>",
    showarrow=False,
    xanchor="left",
    xshift=10,
    yref="paper",  # ADD THIS - uses paper coordinates (0=bottom, 1=top)
    font=dict(size=14, color="black", weight="bold"),
)

st.plotly_chart(fig_stacked, use_container_width=True)


# st.info(
#     "**Scope 3** emissions represent the largest portion, accounting for over 98% of total emissions."
# )


# Footer
# st.markdown("---")
# st.markdown("---")

# st.markdown(
#     "**Data Sources:** Bechtle AG Annual Reports, Check Point Research, IBM Security, Various Cybersecurity Reports"
# )
# st.markdown("**Last Updated:** November 2024")
