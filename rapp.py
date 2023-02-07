import streamlit as st
import openpyxl
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu


st.set_page_config(page_title = "Aakarshan Dutta Resume", page_icon = ":email:", layout = "wide")


@st.cache()   #Image Cache Setup
def load_image(filename):
    l_img = Image.open(filename)
    return (l_img)

@st.cache(allow_output_mutation=True)   #Dataframe cache setup
def load_data(filename):
    xl_df = pd.read_excel(filename)
    return xl_df

#----USE LOCAL CSS-------
#Style.css file download: https://github.com/Sven-Bo/personal-website-streamlit/blob/master/style/style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Style/Style.css")

c1, c2 = st.columns((1,3))
with c2:
    st.title("AAKARSHAN DUTTA")

#-----Social Links---
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/aakarshan-dutta-1b3a30133/",
    "GitHub": "https://github.com/Akkudutta?tab=repositories",
}
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#----Navigation Menu----
with st.sidebar:
    selected =  option_menu(
    menu_title = "MY RESUME",
    options = ["Introduction","Educational Qualifications", "Work Experience", "Achievements", "Core Skills", "Projects", "Personal Details", "References"],
    menu_icon = "graph-up-arrow"
    )

#---Professional Summary---
if selected == "Introduction":
    l_col, r_col = st.columns((1,2))
    with l_col:
        l_img = load_image("Images/dp.jpg")
        st.image(l_img)
    with r_col:
        st.subheader("PROFESSIONAL SUMARY")
        st.write("##")
        st.write("""
    Dynamic and motivated professional with a proven record of generating
and building relationships, managing projects from concept to completion,
and coaching individuals to success. Skilled in building cross-functional
teams, demonstrating exceptional communication skills, and making
critical decisions during challenges. Looking forward to secure a
challenging position in a reputable organization to expand my learnings,
knowledge, and skills
""")
    st.write("---")

#----Education----
if selected == "Educational Qualifications":
    st.header("EDUCATIONAL QUALIFICATIONS")
    st.write("##")
    xl_df = load_data("EQ.xlsx")
    xl_df['Grade/CGPA'] = xl_df['Grade/CGPA'].astype(str)   
    st.dataframe(xl_df)
    st.write("---")

#----Experience----
if selected == "Work Experience":
    st.header("WORK EXPERIENCE")
    st.write("##")
    st.subheader("Assistant Business Manager:Operations - Highway Amenities Developers Private Limited")
    st.write("""
**Duration:-** 04/2022 - Current \n
**Location:-** Bangalore
**Job Role:**
* Generated daily operational and sales reports for corrective action or continuous improvement.
* Empowered staff members to contribute to continuous improvement, quality and growth of company.
""")
    st.write("##")
    st.subheader("Hospitality Supervisor - IRCTC")
    st.write("""
**Duration:-** 07/2019 - 07/2021 \n
**Location:-** Bangalore
* Maintained impeccable food hygiene standards for optimised customer comfort and ongoing safety compliance.
* Ensured COVID protocols were consistently adhered to, minimising risk to hospitality staff and passengers.
""")
    st.write("##")
    st.subheader("Front Office Associate - Hard Rock Hotel Goa")
    st.write("""
**Duration:-** 04/2018 - 07/2019 \n
**Location:-** Goa
* Used excellent time management and organisation skills to effectively prioritise administrative duties.
* Demonstrated outstanding communication and relationship-building skills, effectively enhancing customer experiences.
""")
    st.write("##")
    st.subheader("Housekeeping Assistant - Tridet Chennai")
    st.write("""
**Duration:-** 07/2015 - 02/2018 \n
**Location:-** Chennai 
* Completed all tasks as requested by management within set timeframes and to high-quality standards.
""")
    st.write("---")

#---Achievements---
if selected == "Achievements":
    st.header("ACHIEVEMENTS")
    st.write("##")
    st.write("""
* Created Webapp using Python
* Received multiple medals and awards in extra curricular activities like singing, dance, sports, martial arts and studies.
* Awarded as Employee of the Month at Trident Chennai
* Successfully organized Musical and Sports Events as Event Director
* Trained multiple people in the fields of music, sports, hospitality, and event management
* Accomplished music composer and director
""")
    st.write("---")

#---Skillset---
if selected == "Core Skills":
    st.header("CORE SKILLS")
    st.write("##")
    st.write("""
* Quick learner
* Good communication skills
* Operations management
* Leadership and team building
* Data review and analysis
* IT Skills like Python, C++, R, SQL, Tableau, OPERA, Triton, SAP, Logic Pro X, Pro Tools, MS Excel, MS Word, MS PowerPoint
* Analytical skills like ML, Big Data, Deep Learning
* Music Production/Audio Engineer
""")
    st.write("---")

#---Projects---
if selected == "Projects":
    st.header("PROJECTS")
    st.write("##")
    st.write("""
**Title:** Windmill Power prediction \n
**Problem Statement:** To identify key features that impact the windmill's power generation and prediction of power generated by windmill based on historical data \n
**Skills Used:** Data Collection, Exploratory data Analysis(EDA), Feature Selection, Model Selection/Evaluation, R, Python 
""")
    st.write("##")
    st.write("""
**Title:** Digital Resume \n
**Problem Statement:** To build a digital Resume WebApp in Python using Streamlit \n
**Skills Used:** Python, Streamlit 
""")
    st.write("##")
    st.write("""
**Title:** Dominant Color DS \n
**Problem Statement:** To find the most dominant colors in an image \n
**Skills Used:** Pyhton, KNN, KMeans Clustering \n
""")
    st.write("---")

#---Personal Details---
if selected == "Personal Details":
    st.header("PERSONAL DETAILS")
    st.write("""
**Name:** AAKARSHAN DUTTA \n
**Father's Name:** Rabindra Nath Dutta \n
**Address:** House No 42/880, Devnandan Nagar Phase -1, Seepat Road, Sarkanda, Bilaspur, Chhattisgarh - 495006 \n
**Contact No:** 9789863162, 9039769126 \n
**email id:** akku.dutta@gmail.com \n
**Languages Known:** Hindi, English & Bangla
""")
    st.write("---")

#----References---
if selected == "References":
    st.header("REFERENCES")
    st.write("""
* Mr. Jitendra Das, Lecturer, I.H.M. Chennai
* Mr. Tanuj Arora, Hotel Manager, Hard Rock Hotel Goa
* Mr. Sivakumar D., Area Officer IRCTC Bangalore Division
* Prof Gaurav Garg, Program Director, IIML
""")
    st.write("---")