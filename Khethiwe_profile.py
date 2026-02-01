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
            "data:data:image/jpeg;base64,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",  # keep your base64 image
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
    Mathematical Sciences graduate with a strong foundation in statistics, data science, programming, and quantitative analysis, 
    and hands-on experience working with real-world datasets at Statistics South Africa and CPUT. Skilled in data analysis, reporting, 
    R, SQL, SAS, Python, and Power BI, with experience in data validation, trend analysis, and producing analytical reports.
    Highly interested in credit risk, decision science, and analytics, and eager to apply quantitative skills in a structured risk environment
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
    <li> Analysed large-scale survey datasets using R for data cleaning, preprocessing, and exploratory analysis.
    <li> Applied multinomial logistic regression to model relationships and predict education outcomes.
    <li> Summarised findings through clear reporting and data visualisations..
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Student Debt Analytics</h3>
    <b>Tools:</b> R · Power BI<br><br>
    <li> Built regression models and interactive dashboards to analyse
    <li> financial and demographic trends.
    <li> Processed demographic and financial datasets using R.
    <li> Conducted multiple linear regression for predictive analysis. 
    <li> Designed interactive Power BI dashboards to visualise trends and key insights.
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

















