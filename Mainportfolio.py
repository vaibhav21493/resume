# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from streamlit_option_menu import option_menu

# def main_portfolio():
#     # --- SETTINGS ---
#     st.set_page_config(layout="wide")

#     # Combined CSS
#     st.markdown("""
#     <style>
#     .stApp {
#         background: radial-gradient(circle at top left, #2c3e50, #1a252f, #0a0e12);
#         color: #F0F2F6;
#         font-family: 'Segoe UI', sans-serif;
#     }
#     .card {
#         background-color: rgba(45, 45, 45, 0.9);
#         border: 2px solid #90EE90;
#         border-radius: 15px;
#         padding: 25px;
#         max-width: 800px;
#         margin-bottom: 15px;
#         box-shadow: 0 8px 20px rgba(0,0,0,0.3);
#         transition: transform 0.3s ease, box-shadow 0.3s ease;
#         text-align: left;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 25px rgba(0,0,0,0.5);
#     }
#     .stExpander > button {
#         font-size: 1.2rem;
#         font-weight: bold;
#         color: #90EE90;
#     }
#     .stExpander > button:hover {
#         color: #32CD32;
#     }
#     h1, h2, h3, h4 {
#         color: #90EE90;
#     }
#     a { color: #90EE90; text-decoration: none; }
#     a:hover { color: #32CD32; text-decoration: underline; }
#     </style>
#     """, unsafe_allow_html=True)

#     # Sections
#     def hero_section():
#         col1, col2 = st.columns([1, 3])
#         with col1:
#             st.subheader("Hi there! I'm")
#             st.title("Vaibhav Murotiya 👋")
#             st.markdown("""
#                 **Email:** [vaibhavmurotiya754@gmail.com](mailto:vaibhavmurotiya754@gmail.com)  
#                 **Mobile:** +91-7878554880  
#                 [LinkedIn](https://www.linkedin.com/in/vaibhav-murotiya-293823294/) | 
#                 [GitHub](https://github.com/vaibhav21493/) | 
#                 [LeetCode](https://leetcode.com/u/__vai_21/)
#             """)
#         with col2:
#             st.markdown("""
#                 ### A Passionate Cyber Physical Systems student and aspiring developer.
#                 Dedicated to building innovative solutions in embedded systems, web apps, and automation, 
#                 with strong problem-solving and leadership skills.
#                 ---
#             """)

#     def education_section():
#         st.header("🎓 Education")
#         st.markdown("""
#         <div class="card">
#             <h4>Manipal Institute of Technology (MIT), Udupi, India</h4>
#             <i>Bachelor of Technology – Cyber Physical Systems</i>  
#             <p><strong>CGPA:</strong> 8.13 (2023 – 2027 Expected)</p>
#             <p><strong>Courses:</strong> Analog Electronics, Data Structures, Algorithms, OOP, Communication Networks, 
#             Sensors & Transducers, Probability & Discrete Mathematics, Computer Architecture, Microcontrollers</p>
#         </div>
#         <div class="card">
#             <h4>Adarsh Vidya Mandir, Mt Abu, Rajasthan, India</h4>
#             Class XII – Grade: 91% (2021–2022)  
#             Class X – Grade: 84.4% (2018–2019)
#         </div>
#         """, unsafe_allow_html=True)

#     def skills_section():
#         st.header("🛠 Skills Summary")
#         st.markdown("""
#         <div class="card">
#             <strong>Languages:</strong> C, C++, Python, SQL, Assembly Language  
#             <strong>Tools:</strong> Git, WordPress, Jupyter Notebook, CST, NumPy, Pandas, Matplotlib, VS Code  
#             <strong>Web Development:</strong> HTML5, CSS3, JavaScript, Streamlit, JSON, CSV  
#             <strong>Operating Systems:</strong> Windows  
#             <strong>Soft Skills:</strong> Critical Thinking, Time Management, Adaptability, Unwavering Dedication
#         </div>
#         """, unsafe_allow_html=True)

#     def projects_section():
#         st.header("💻 Projects")
#         projects = [
#             ("Queue Management System", "Python (OOP), Streamlit, MySQL, HTML, CSS", 
#              "Streamlines patient appointments, optimizes doctor availability, and reduces waiting times."),
#             ("Music Journey and Trend Visualization", "Python, NumPy, Pandas, Matplotlib, Streamlit, HTML, CSS",
#              "Visualizes music listening trends with filters for genre, platform, and release year."),
#             ("Affine Cipher Tool", "HTML, CSS, Streamlit, DSA",
#              "Secure message encryption/decryption using Affine Cipher logic."),
#             ("Small Portable Ventilator", "Sensors, Microcontroller, IoT",
#              "Arduino-based ventilator with oxygen monitoring and report generation."),
#             ("Line Following Robot", "8051 Microcontroller",
#              "Embedded system with sensor integration and control logic.")
#         ]
#         for title, tech, desc in projects:
#             with st.expander(f"📝 {title}"):
#                 st.write(f"**Tech Stack:** {tech}")
#                 st.write(desc)

#     def experience_section():
#         st.header("🏢 Experience & Extracurricular")
#         st.markdown("""
#         <div class="card">
#             <h4>Yash Technologies, Indore</h4>
#             <i>June 2, 2025 – August 2, 2025</i>  
#             Completed a 2-month internship focused on Python development and automation.
#         </div>
#         <div class="card">
#             <strong>Human Resource & Management Coordinator</strong> – Placement Team MIT (2024–Present)  
#             <strong>Member</strong> – Volleyball Team MIT (2023–Present)  
#             <strong>NSS Board Member</strong> (2023–2025) – Volunteered in social drives, health camps, rural development, 
#             and literacy programs; attended 3 camps.
#         </div>
#         """, unsafe_allow_html=True)

#     def achievements_section():
#         st.header("🏆 Achievements & Certifications")
#         achievements = [
#             "Published research paper on mm-Wave Antenna – First International Conference on AI, Computational, Communication & Network Society, University of Wollongong, Dubai (June 2025).",
#             "Participated in Smart India Hackathon (SIH).",
#             "Two-time Revels Cup Winner in Volleyball.",
#             "Yoga Instructor & Leader in NSS events.",
#             "Participated in Marathons – 21k, 10k, and 5k runs."
#         ]
#         for ach in achievements:
#             st.markdown(f"<div class='card'>{ach}</div>", unsafe_allow_html=True)

#     def volunteer_section():
#         st.header("🤝 Volunteer Experience")
#         st.markdown("""
#         <div class="card">
#             <strong>Placement Team MIT</strong> – Human Resource & Management Coordinator  
#             <strong>Organizing Committee Member</strong> – Revels (Cultural Fest) & Manipal Marathon
#         </div>
#         """, unsafe_allow_html=True)

#     # --- Navigation Sidebar ---
#     with st.sidebar:
#         selected = option_menu(
#             menu_title=None,
#             options=[
#                 "Home",
#                 "Education",
#                 "Skills Summary",
#                 "Projects",
#                 "Experience & Extracurricular",
#                 "Achievements & Certifications",
#                 "Volunteer Experience"
#             ],
#             icons=['house', 'book', 'wrench', 'code-slash', 'building', 'trophy', 'heart'],
#             menu_icon="cast",
#             default_index=0
#         )

#     # --- Page Switch ---
#     if selected == "Home":
#         hero_section()
#     elif selected == "Education":
#         education_section()
#     elif selected == "Skills Summary":
#         skills_section()
#     elif selected == "Projects":
#         projects_section()
#     elif selected == "Experience & Extracurricular":
#         experience_section()
#     elif selected == "Achievements & Certifications":
#         achievements_section()
#     elif selected == "Volunteer Experience":
#         volunteer_section()
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

def main_portfolio():
    # --- SETTINGS ---
    st.set_page_config(layout="wide")

    # Combined CSS
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #2c3e50, #1a252f, #0a0e12);
        color: #F0F2F6;
        font-family: 'Segoe UI', sans-serif;
    }
    .card {
        background-color: rgba(45, 45, 45, 0.9);
        border: 2px solid #90EE90;
        border-radius: 15px;
        padding: 25px;
        max-width: 800px;
        margin-bottom: 15px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: left;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.5);
    }
    .stExpander > button {
        font-size: 1.2rem;
        font-weight: bold;
        color: #90EE90;
    }
    .stExpander > button:hover {
        color: #32CD32;
    }
    h1, h2, h3, h4 {
        color: #90EE90;
    }
    a { color: #90EE90; text-decoration: none; }
    a:hover { color: #32CD32; text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

    # Sections
    def hero_section():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.subheader("Hi there! I'm")
            st.title("Vaibhav Murotiya 👋")
            st.markdown("""
                **Email:** [vaibhavmurotiya754@gmail.com](mailto:vaibhavmurotiya754@gmail.com)  
                **Mobile:** +91-7878554880  
                [LinkedIn](https://www.linkedin.com/in/vaibhav-murotiya-293823294/) | 
                [GitHub](https://github.com/vaibhav21493/) | 
                [LeetCode](https://leetcode.com/u/__vai_21/)
            """)
        with col2:
            st.markdown("""
                ### A Passionate Cyber Physical Systems student and aspiring developer.
                Dedicated to building innovative solutions in embedded systems, web apps, and automation, 
                with strong problem-solving and leadership skills.
                ---
            """)

    def education_section():
        st.header("🎓 Education")
        st.markdown("""
        <div class="card">
            <h4>Manipal Institute of Technology (MIT), Udupi, India</h4>
            <i>Bachelor of Technology – Cyber Physical Systems</i>  
            <p><strong>CGPA:</strong> 8.13 (2023 – 2027 Expected)</p>
            <p><strong>Courses:</strong> Analog Electronics, Data Structures, Algorithms, OOP, Communication Networks, 
            Sensors & Transducers, Probability & Discrete Mathematics, Computer Architecture, Microcontrollers</p>
        </div>
        <div class="card">
            <h4>Adarsh Vidya Mandir, Mt Abu, Rajasthan, India</h4>
            Class XII – Grade: 91% (2021–2022)  
            Class X – Grade: 84.4% (2018–2019)
        </div>
        """, unsafe_allow_html=True)

    def skills_section():
        st.header("🛠 Skills Summary")

        # Skills data with proficiency levels
        skills = {
            "Languages": [
                ("Python", 90),
                ("C++", 85),
                ("C", 80),
                ("SQL", 80),
                ("Assembly Language", 70)
            ],
            "Tools": [
                ("Git", 85),
                ("WordPress", 80),
                ("Jupyter Notebook", 85),
                ("CST", 75),
                ("VS Code", 90)
            ],
            "Web Development": [
                ("HTML5", 85),
                ("CSS3", 80),
                ("JavaScript", 70),
                ("Streamlit", 85),
                ("JSON / CSV", 90)
            ],
            "Soft Skills": [
                ("Critical Thinking", 90),
                ("Time Management", 85),
                ("Adaptability", 90),
                ("Dedication", 95)
            ]
        }

        # Display skills with progress bars
        for category, items in skills.items():
            st.subheader(f"📌 {category}")
            for skill, level in items:
                st.markdown(f"**{skill}**")
                st.progress(level / 100)

        # Radar chart for overview
        radar_data = {
            'Skill': ['Python', 'C++', 'SQL', 'Web Dev', 'Embedded', 'Data Analysis'],
            'Proficiency': [4.5, 4.0, 4.0, 3.5, 4.0, 4.5],
        }
        df_radar = pd.DataFrame(radar_data)
        fig = px.line_polar(
            df_radar,
            r='Proficiency',
            theta='Skill',
            line_close=True,
            title="Skillset Overview",
            color_discrete_sequence=px.colors.sequential.Electric
        )
        fig.update_traces(fill='toself')
        st.plotly_chart(fig, use_container_width=True)

    def projects_section():
        st.header("💻 Projects")
        projects = [
            ("Queue Management System", "Python (OOP), Streamlit, MySQL, HTML, CSS", 
             "Streamlines patient appointments, optimizes doctor availability, and reduces waiting times."),
            ("Music Journey and Trend Visualization", "Python, NumPy, Pandas, Matplotlib, Streamlit, HTML, CSS",
             "Visualizes music listening trends with filters for genre, platform, and release year."),
            ("Affine Cipher Tool", "HTML, CSS, Streamlit, DSA",
             "Secure message encryption/decryption using Affine Cipher logic."),
            ("Small Portable Ventilator", "Sensors, Microcontroller, IoT",
             "Arduino-based ventilator with oxygen monitoring and report generation."),
            ("Line Following Robot", "8051 Microcontroller",
             "Embedded system with sensor integration and control logic.")
        ]
        for title, tech, desc in projects:
            with st.expander(f"📝 {title}"):
                st.write(f"**Tech Stack:** {tech}")
                st.write(desc)

    def experience_section():
        st.header("🏢 Experience & Extracurricular")
        st.markdown("""
        <div class="card">
            <h4>Yash Technologies, Indore</h4>
            <i>June 2, 2025 – August 2, 2025</i>  
            Completed a 2-month internship focused on Python development and automation.
        </div>
        <div class="card">
            <strong>Human Resource & Management Coordinator</strong> – Placement Team MIT (2024–Present)  
            <strong>Member</strong> – Volleyball Team MIT (2023–Present)  
            <strong>NSS Board Member</strong> (2023–2025) – Volunteered in social drives, health camps, rural development, 
            and literacy programs; attended 3 camps.
        </div>
        """, unsafe_allow_html=True)

    def achievements_section():
        st.header("🏆 Achievements & Certifications")
        achievements = [
            "Published research paper on mm-Wave Antenna – First International Conference on AI, Computational, Communication & Network Society, University of Wollongong, Dubai (June 2025).",
            "Participated in Smart India Hackathon (SIH).",
            "Two-time Revels Cup Winner in Volleyball.",
            "Yoga Instructor & Leader in NSS events.",
            "Participated in Marathons – 21k, 10k, and 5k runs."
        ]
        for ach in achievements:
            st.markdown(f"<div class='card'>{ach}</div>", unsafe_allow_html=True)

    def volunteer_section():
        st.header("🤝 Volunteer Experience")
        st.markdown("""
        <div class="card">
            <strong>Placement Team MIT</strong> – Human Resource & Management Coordinator  
            <strong>Organizing Committee Member</strong> – Revels (Cultural Fest) & Manipal Marathon
        </div>
        """, unsafe_allow_html=True)

    # --- Navigation Sidebar ---
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=[
                "Home",
                "Education",
                "Skills Summary",
                "Projects",
                "Experience & Extracurricular",
                "Achievements & Certifications",
                "Volunteer Experience"
            ],
            icons=['house', 'book', 'wrench', 'code-slash', 'building', 'trophy', 'heart'],
            menu_icon="cast",
            default_index=0
        )

    # --- Page Switch ---
    if selected == "Home":
        hero_section()
    elif selected == "Education":
        education_section()
    elif selected == "Skills Summary":
        skills_section()
    elif selected == "Projects":
        projects_section()
    elif selected == "Experience & Extracurricular":
        experience_section()
    elif selected == "Achievements & Certifications":
        achievements_section()
    elif selected == "Volunteer Experience":
        volunteer_section()
