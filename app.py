import streamlit as st

from src.agents import (
    research_agent,
    scoring_agent,
    outreach_agent
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Lead Research Agent",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background-color: #F4FBFC;
    color: #173F45;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}


/* ============================================================
   HERO HEADER
   ============================================================ */

.hero {
    background: linear-gradient(135deg, #087F8C, #0EA5A8);
    padding: 32px 38px;
    border-radius: 20px;
    margin-bottom: 28px;
    color: white;
    box-shadow: 0 10px 30px rgba(8, 127, 140, 0.18);
}

.hero h1 {
    margin: 0;
    color: white;
    font-size: 34px;
    font-weight: 750;
    letter-spacing: -0.5px;
}

.hero p {
    margin: 10px 0 0 0;
    color: white;
    font-size: 16px;
    line-height: 1.6;
    opacity: 0.95;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #D7EEF0;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #087F8C;
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

.stTextInput label,
.stTextArea label {
    color: #24565C !important;
    font-weight: 600 !important;
}


/* ============================================================
   INPUT BOXES
   ============================================================ */

.stTextInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #173F45 !important;
    border: 1px solid #B8DDE0 !important;
    border-radius: 10px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #0EA5A8 !important;
    box-shadow: 0 0 0 3px rgba(14, 165, 168, 0.12) !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #087F8C, #0EA5A8);
    color: white;
    border: none;
    border-radius: 11px;
    padding: 12px 22px;
    font-size: 15px;
    font-weight: 650;
    box-shadow: 0 6px 18px rgba(8, 127, 140, 0.18);
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 9px 24px rgba(8, 127, 140, 0.25);
}


/* ============================================================
   INFO BOX
   ============================================================ */

.info-box {
    background-color: #E8F8F9;
    border-left: 5px solid #0EA5A8;
    padding: 15px 18px;
    border-radius: 10px;
    color: #24565C;
    margin-bottom: 20px;
    line-height: 1.5;
}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {
    color: #087F8C;
    font-size: 22px;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 14px;
}


/* ============================================================
   WHITE CARD
   ============================================================ */

.card {
    background-color: #FFFFFF;
    border: 1px solid #D7EEF0;
    border-radius: 17px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 5px 20px rgba(8, 127, 140, 0.06);
}

.card h3 {
    color: #087F8C;
    margin-top: 0;
    margin-bottom: 12px;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-card {
    background-color: #FFFFFF;
    border: 1px solid #D7EEF0;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    min-height: 150px;
    box-shadow: 0 5px 18px rgba(8, 127, 140, 0.05);
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 8px;
}

.feature-title {
    color: #087F8C;
    font-size: 18px;
    font-weight: 700;
}

.feature-text {
    color: #607E82;
    font-size: 14px;
    margin-top: 6px;
}


/* ============================================================
   RESULT HEADER
   ============================================================ */

.result-banner {
    background: #E8F8F9;
    border: 1px solid #B9E5E7;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 22px;
}

.result-banner h3 {
    color: #087F8C;
    margin: 0;
}

.result-banner p {
    color: #526F73;
    margin: 6px 0 0 0;
}


/* ============================================================
   OUTREACH BOX
   ============================================================ */

.outreach-box {
    background: #FFFFFF;
    border: 1px solid #B9E5E7;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 5px 18px rgba(8, 127, 140, 0.06);
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #789397;
    font-size: 13px;
    padding: 25px;
    margin-top: 25px;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border: none;
    border-top: 1px solid #D7EEF0;
    margin: 28px 0;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
<div class="hero">
<h1>🌊 AI Lead Research & Outreach</h1>
<p>
Research prospects, understand their business,
identify opportunities, and start meaningful
conversations with AI.
</p>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎯 Lead Research")

    st.markdown(
        """
<div class="info-box">
Tell us a little about the company.<br><br>
We'll help you understand the lead
and discover potential opportunities.
</div>
""",
        unsafe_allow_html=True
    )

    company = st.text_input(
        "Company Name",
        placeholder="e.g. Tata Consultancy Services"
    )

    industry = st.text_input(
        "Industry",
        placeholder="e.g. Information Technology"
    )

    website = st.text_input(
        "Website",
        placeholder="e.g. https://www.tcs.com"
    )

    description = st.text_area(
        "Company Description",
        placeholder="Tell us briefly what the company does...",
        height=130
    )

    st.markdown("<br>", unsafe_allow_html=True)

    run = st.button(
        "✨ Understand This Lead",
        use_container_width=True
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

if not run:

    st.markdown(
        """
<div class="section-title">
👋 Welcome
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="card">
<p style="font-size:16px; color:#526F73; margin-bottom:12px;">
Your AI-powered lead assistant helps you research companies,
qualify prospects, understand business opportunities,
and create personalized outreach.
</p>

<p style="color:#526F73; margin-bottom:0;">
Enter a company in the sidebar to get started.
</p>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">🔎</div>
<div class="feature-title">Research</div>
<div class="feature-text">
Understand the company, industry and potential needs.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">🎯</div>
<div class="feature-title">Qualify</div>
<div class="feature-text">
Identify opportunities and evaluate lead potential.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
<div class="feature-card">
<div class="feature-icon">💬</div>
<div class="feature-title">Connect</div>
<div class="feature-text">
Create personalized outreach for meaningful conversations.
</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown(
        """
<div class="footer">
🌊 Research smarter • Connect better
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# AI ANALYSIS
# ============================================================

if run:

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not company or not industry or not description:

        st.warning(
            "Please enter the company name, industry and description."
        )

    else:

        # ----------------------------------------------------
        # RUN AI AGENTS
        # ----------------------------------------------------

        with st.spinner(
            "🔎 Our AI agents are researching the lead..."
        ):

            research = research_agent(
                company,
                industry,
                website,
                description
            )

            score = scoring_agent(
                company,
                industry,
                description
            )

            outreach = outreach_agent(
                company,
                industry,
                "customer acquisition and business automation"
            )


        # ----------------------------------------------------
        # SUCCESS MESSAGE
        # ----------------------------------------------------

        st.success(
            "✨ Lead analysis completed successfully!"
        )


        # ----------------------------------------------------
        # RESULT HEADER
        # ----------------------------------------------------

        st.markdown(
            f"""
<div class="result-banner">
<h3>📋 Lead insights are ready</h3>
<p>
Here's what we found for <b>{company}</b>.
</p>
</div>
""",
            unsafe_allow_html=True
        )


        # ====================================================
        # RESEARCH + SCORE
        # ====================================================

        col1, col2 = st.columns(2)


        # ----------------------------------------------------
        # RESEARCH AGENT
        # ----------------------------------------------------

        with col1:

            st.markdown(
                """
<div class="card">
<h3>🔎 Company Research</h3>
</div>
""",
                unsafe_allow_html=True
            )

            st.write(research)


        # ----------------------------------------------------
        # LEAD SCORE
        # ----------------------------------------------------

        with col2:

            st.markdown(
                """
<div class="card">
<h3>📊 Lead Qualification</h3>
</div>
""",
                unsafe_allow_html=True
            )

            st.write(score)


        # ====================================================
        # OUTREACH
        # ====================================================

        st.markdown("---")

        st.markdown(
            """
<div class="section-title">
💬 Personalized Outreach
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="info-box">
Here's a personalized starting point for your
conversation with this prospect.
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            """
<div class="outreach-box">
""",
            unsafe_allow_html=True
        )

        st.text_area(
            "Generated Message",
            outreach,
            height=250
        )

        st.markdown(
            """
</div>
""",
            unsafe_allow_html=True
        )


        # ====================================================
        # FOOTER
        # ====================================================

        st.markdown(
            """
<div class="footer">
🌊 AI Lead Research & Outreach
<br>
Research smarter • Connect better
</div>
""",
            unsafe_allow_html=True
        )