import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Khethiwe Ntshangase | Data Analyst",
    layout="wide"
)

# ---------------------------------------------------
# Global Styling
# ---------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #F8F9FC;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 25px;
}
.hero-name {
    font-size: 42px;
    font-weight: 700;
}
.hero-role {
    color: #6C63FF;
    font-size: 22px;
}
.section-title {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 10px;
}
.small-text {
    color: #6B7280;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.markdown("""
<h2 style="color:#6C63FF;">📊 Portfolio</h2>
<p class="small-text">Navigate my journey</p>
""", unsafe_allow_html=True)

st.sidebar.divider()

menu = st.sidebar.radio(
    "Go to:",
    [
        "Profile",
        "About",
        "Education",
        "Work Experience & Projects",
        "Contact"
    ]
)

# ---------------------------------------------------
# PROFILE (HERO SECTION)
# ---------------------------------------------------
if menu == "Profile":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/...",  # keep your base64 image
            use_column_width=True
        )

    with col2:
        st.markdown("""
        <div class="card">
            <div class="hero-name">Khethiwe Ntshangase</div>
            <div class="hero-role">Data Analyst | Mathematical Sciences</div>
            <p class="small-text">
            Mathematics & Physics · Cape Peninsula University of Technology
            </p>
            <p>
            Passionate about data-driven decision-making, credit risk,
            analytics, and transforming raw data into meaningful insights.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧠 Core Skills</h3>
    <ul>
        <li>Statistical Analysis & Modelling</li>
        <li>Data Cleaning & Validation</li>
        <li>Machine Learning & Forecasting</li>
        <li>Data Visualisation & Reporting</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------
elif menu == "About":

    st.markdown('<div class="section-title">👩🏽‍💻 About Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    Mathematical Sciences graduate with a strong foundation in statistics,
    data science, programming, and quantitative analysis.
    <br><br>
    Experienced working with real-world datasets at Statistics South Africa
    and CPUT. Skilled in R, Python, SQL, SAS, and Power BI, with a strong
    interest in credit risk, decision science, and analytics.
    </div>
    """, unsafe_allow_html=True)

    st.image("IMG_5415.JPEG", width=500)

# ---------------------------------------------------
# EDUCATION
# ---------------------------------------------------
elif menu == "Education":

    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Advanced Diploma in Mathematical Sciences (NQF 7)</h3>
    <b>Institution:</b> Cape Peninsula University of Technology<br>
    <b>Status:</b> Completed — December 2025

    <h4>Coursework</h4>
    <ul>
        <li>Mathematical Statistics</li>
        <li>Machine Learning & Data Science</li>
        <li>Econometrics & Financial Mathematics</li>
        <li>Time Series Forecasting</li>
        <li>Numerical Methods & Programming</li>
    </ul>

    <h4>Tools</h4>
    SAS · R · Python · SQL · Power BI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Postgraduate Diploma in Mathematical Science (NQF 8)</h3>
    <b>Status:</b> Currently Pursuing

    <h4>Coursework</h4>
    <ul>
        <li>Bayesian Statistics</li>
        <li>Advanced Programming for Data Science</li>
        <li>Convex Optimisation</li>
        <li>Machine Learning 5A & 5B</li>
        <li>Data Engineering & Visualisation</li>
    </ul>

    <h4>Tools</h4>
    SAS · R · Python · SQL · Power BI · Tableau
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# WORK EXPERIENCE & PROJECTS
# ---------------------------------------------------
elif menu == "Work Experience & Projects":

    st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Data Analyst Intern — Statistics South Africa</h3>
    <b>July 2024 – December 2024</b>
    <ul>
        <li>Cleaned and validated large survey datasets using R</li>
        <li>Performed exploratory and statistical analysis</li>
        <li>Produced analytical tables, charts, and reports</li>
        <li>Worked with SAS, SPSS, Python in a production environment</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">📈 Projects</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Impact of Socio-Economic Factors on Education Outcomes</h3>
    <b>Tools:</b> R<br><br>
    Applied multinomial logistic regression to model education outcomes,
    supported by exploratory analysis and clear reporting.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Student Debt Analytics</h3>
    <b>Tools:</b> R · Power BI<br><br>
    Built regression models and interactive dashboards to analyse
    financial and demographic trends.
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# CONTACT
# ---------------------------------------------------
elif menu == "Contact":

    st.markdown('<div class="section-title">📬 Contact</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="text-align:center;">
    <h3>Let’s Connect</h3>
    <p>Interested in data analytics, risk, or collaboration?</p>
    <h4>📧 khethiwentshangase22@gmail.com</h4>
    </div>
    """, unsafe_allow_html=True)














