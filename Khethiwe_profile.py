import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Data Analyst Profile",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to:",
    ["Data Analyst Profile","About", "Education", "Work Experience & Projects", "Contact"]
)

# ---------------------------------------------------
# Data Analyst Profile Section
# ---------------------------------------------------

if menu == "Data Analyst Profile":

    st.title("Data Analyst Profile")

    col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/...",
        use_column_width=True
    )

with col2:
    st.markdown("""
    <h1 style="margin-bottom:0;">Khethiwe Ntshangase</h1>
    <h4 style="color:#6C63FF; margin-top:5px;">
    Data Analyst | Mathematics & Physics
    </h4>
    <p>
    Cape Peninsula University of Technology
    </p>
    """, unsafe_allow_html=True)



#---------------------------------------------------
# About Section
#--------------------------------------------------

elif menu == "About":
   st.title("About")
   st.write("""Mathematical Sciences graduate with a strong foundation in statistics, data science, programming,
             and quantitative analysis, and hands-on experience working with real-world datasets at Statistics South Africa and CPUT.
             Skilled in data analysis, reporting, R, SQL, SAS, Python, and Power BI, with experience in data validation, trend analysis, 
               and producing analytical reports. Highly interested in credit risk, decision science, and analytics, and eager to apply quantitative skills in a structured risk environment""")

   st.image("IMG_5415.JPEG", width=600)


# ---------------------------------------------------
# Education Section
# ---------------------------------------------------

elif menu == "Education":

    st.title("Education")

    # -----------------------------
    # Advanced Diploma
    # -----------------------------

    st.subheader("Advanced Diploma in Mathematical Sciences (NQF 7)")
    st.write("**Institution:** Cape Peninsula University of Technology")
    st.write("**Status:** Completed — December 2025")

    st.markdown("### Coursework")
    st.markdown("""
    - Mathematical Statistics  
    - Statistics  
    - Machine Learning and Data Science  
    - Econometrics  
    - Financial Mathematics  
    - Finance  
    - Time Series Forecasting  
    - Numerical Methods  
    - Programming  
    """)

    st.markdown("### Tools")
    st.markdown("""
    - SAS  
    - R  
    - Python  
    - SQL  
    - Microsoft Office  
    - Power BI  
    """)

    st.divider()

    # -----------------------------
    # Postgraduate Diploma
    # -----------------------------

    st.subheader("Postgraduate Diploma in Mathematical Science (NQF 8)")
    st.write("**Status:** Currently Pursuing")

    st.markdown("### Coursework")
    st.markdown("""
    - Bayesian Statistics  
    - Advanced Programming for Data Science  
    - Convex Optimisation  
    - Machine Learning 5A & 5B  
    - Data Engineering and Visualization  
    - Mathematical Modelling  
    - Computational Methods  
    - Research Project  
    """)

    st.markdown("### Tools")
    st.markdown("""
    - SAS  
    - R  
    - Python  
    - SQL  
    - Microsoft Office  
    - Power BI  
    - Tableau  
    """)

# ---------------------------------------------------
# Work Experience & Projects Section
# ---------------------------------------------------

elif menu == "Work Experience & Projects":

    st.title("Work Experience & Projects")

    # -----------------------------
    # Work Experience
    # -----------------------------

    st.subheader("Data Analyst Intern")
    st.write("**Organization:** Statistics South Africa (Stats SA)")
    st.write("**Duration:** July 2024 – December 2024")

    st.markdown("""
    **Responsibilities & Achievements:**
    - Cleaned, validated, and prepared large survey datasets using R, ensuring data integrity and accuracy.  
    - Performed statistical summaries and exploratory analysis to identify trends and data quality issues.  
    - Produced tables, charts, and analytical reports for internal stakeholders.  
    - Investigated data inconsistencies, tested statistical assumptions, and verified outputs.  
    - Collaborated with senior statisticians during reporting cycles and data verification processes.  
    - Gained professional exposure to SAS, SPSS, and Python in a production analytics environment.  
    """)

    st.divider()

    # -----------------------------
    # Projects
    # -----------------------------

    st.subheader("Projects")

    st.markdown("### Impact of Socio-Economic Factors on Education Outcomes (R)")
    st.markdown("""
    - Analysed large-scale survey datasets using R for data cleaning, preprocessing, and exploratory analysis.  
    - Applied multinomial logistic regression to model relationships and predict education outcomes.  
    - Summarised findings through clear reporting and data visualisations.  
    """)

    st.markdown("### Data Analytics on Student Debt (R & Power BI)")
    st.markdown("""
    - Processed demographic and financial datasets using R.  
    - Conducted multiple linear regression for predictive analysis.  
    - Designed interactive Power BI dashboards to visualise trends and key insights.  
    """)

# ---------------------------------------------------
# Contact Section
# ---------------------------------------------------

elif menu == "Contact":

    st.title("Contact Information")

    email = "khethiwentshangase22@gmail.com"

    st.write("You can reach me at:")
    st.write(f"📧 {email}")












