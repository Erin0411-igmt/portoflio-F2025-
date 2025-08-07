'''
Erin Courtemanche
7/5/2025
Erin's Portfolio Website
Description: This project creates a python-based website that acts a data analytics
and computer information systems portfolio for Erin Courtemanche
'''

#Imports
import streamlit as st
import os
from pathlib import Path
from PIL import Image
import fitz
import base64
import io
from io import BytesIO

#python -m streamlit run "C:\Users\eacou\OneDrive - Bentley University\[1] Portfolio\Portfolio\portfolio(2026).py"

#Website Tab
st.set_page_config(
    page_title="Erin Courtemanche's Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

#Title Formatting
def title_template(text, font_size=75, color= "#333333", center=True):
    align = 'center' if center else 'left'
    st.markdown(f"""
    <h2 style = 'text-align: {align};
        color: {color};
        font-size: {font_size}px;
        margin-botton: 15px;'>
        {text}
        </h2>
        """, unsafe_allow_html=True)

#Navigation Bar Set up
st.sidebar.markdown("""
    <p style="font-size: 18px; font-weight: bold; color: #333333; margin-bottom: 5px;">
        **Erin Courtemanche**
    </p>
""", unsafe_allow_html=True)
st.sidebar.markdown("*Data Analytics & CIS Student*")
st.sidebar.markdown("---")

st.sidebar.markdown("""
    <p style="font-size: 18px; font-weight: bold; color: #333333; margin-bottom: 10px;">
        🧭 Navigate To:
    </p>
""", unsafe_allow_html=True)
page_select = st.sidebar.radio("", ["About Me", "Resume", "Projects", "View Source Code"])

#Navigation Bar Quick Links
st.sidebar.markdown("---")
st.sidebar.markdown("## 🔗 Quick Links")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/erin-courtemanche-4744a72b4/)")
st.sidebar.markdown("[My Data Website](https://erin0411-igmt-nuclear-streamlit-fbbdhv.streamlit.app/)")

base_path = Path(__file__).parent
pdf_path = base_path / "Erin_Courtemanche_Resume(2026).pdf"

with open(pdf_path, "rb") as f:
    st.sidebar.download_button(
        "📥 Download Resume",
        f,
        file_name="Erin_Courtemanche_Resume(2026).pdf",
        mime="application/pdf"
    )

#About Me Page
if page_select == "About Me":
    title_template("About Me")

    st.title("Education")
    st.write("🎓 I'm currently a Junior at Bentley University pursuing double majors in Data Analytics and Computer Information Systems.")
    st.write("🧠 I'm also pursuing double minors in Business Administration and Artificial Intelligence.")
    st.write("✏️ I'm a member of Bentley's Advanced Standing in Business Analytics Program, which is an accelerated Master's degree for business analytics.")

    st.title("Goals")
    st.write("🌱 I strive to always expand my knowledge and skill set by exploring new tools, technologies, and challenges that push me forward.")
    st.write("✨ I aim to work at a company where I'm genuinely excited to show up each day -- a place that values creativity, learning, and collaboration.")
    st.write("🚀 I'm committed to developing myself not just as a professional, but as a person -- improving how I communicate, connect with others, and contribute to a team.")

    st.title("Fun Facts")
    st.write("🥋 I have 3 black belts in Shaolin Kempo and have taught martial arts for 4 years!")
    st.write("🎭 I love live theater, but I didn't become a 'theater kid' until college.")
    st.write("🐶 I have a Shnorkie named Loki; I've attached a photo of him for your viewing pleasure")

    #Loki Picture
    base_path = Path(__file__).parent
    image_path = base_path / "loki.jpg"
    image = Image.open(image_path)

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded = base64.b64encode(buffered.getvalue()).decode()

    #Image Border
    st.markdown(
        f"""
        <div style="border: 4px solid #FF4B4B; border-radius: 12px; padding: 10px; display: inline-block;">
            <img src="data:image/jpeg;base64,{encoded}" width="700" />
            <p style="text-align: center; font-weight: bold; margin-top: 8px;">Loki Courtemanche</p>
        </div>
        """,
        unsafe_allow_html=True
    )

#Resume Page
if page_select == "Resume":
    pdf_path = Path(__file__).parent / "Erin_Courtemanche_Resume(2026).pdf"

    doc = fitz.open(pdf_path)
    page = doc.load_page(0)

    zoom = 2
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    image = Image.open(io.BytesIO(pix.tobytes("png")))

    buffered = BytesIO()
    image.save(buffered, format="PNG")  # Save the image in PNG format
    buffered.seek(0)  # Ensure the pointer is at the start of the image data

    # Create a border around the image
    st.markdown("""
            <div style="border: 5px solid #FF4B4B; padding: 15px; border-radius: 10px; width: 80%; margin: 0 auto;">
                <img src="data:image/png;base64,{}" width="100%" />
            </div>
        """.format(base64.b64encode(buffered.getvalue()).decode()), unsafe_allow_html=True)

#Project Portfolio
if page_select == "Projects":
    title_template("Projects")

    #ST625 Data Project
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.title("🎟️ Theater Ticket Sales Data Project (Sophomore Year)")
    st.write("The following data analysis was conducted using a database containing information from Broadway theaters, including weekly gross ticket sales, show titles, average ticket prices,"
             " and more. The goal of the analysis was to explore the relationship between weekly ticket sales and factors such as the type of show playing, the top ticket price, and"
             " whether the show included a preview performance.")

    startup_path = base_path / "gross_ticket_sales.pdf"
    with open(startup_path, "rb") as f:
        st.download_button(
            label="📥 Download Gross Ticket Sales Project",
            data=f,
            file_name="gross_ticket_sales.pdf",
            mime="application/pdf"
        )

    #Capstone Consulting Project
    st.write("\n")
    st.write("\n")
    st.markdown("---")
    st.write("\n")
    st.write("\n")
    st.title("🤝 Capstone Consulting Project (Sophomore Year)")
    st.write("The following consulting engagement was carried out with the Obsidian Theater Festival, where strategic recommendations were provided across several key areas including funding,"
             " marketing, and collaboration. As part of the project, in-depth market research was conducted to identify audience demographics, current trends, and growth opportunities within the"
             " arts sector. The findings were then synthesized into a comprehensive report, which was presented to company leadership with actionable insights aimed at optimizing the festival's "
             " operations and expanding its reach.")

    startup_path = base_path / "Final Paper.pdf"
    with open(startup_path, "rb") as f:
        st.download_button(
            label="📥 Download Capstone Consulting Project",
            data=f,
            file_name="Final Paper.pdf",
            mime="application/pdf"
        )

    #Nuclear Website
    st.write("\n")
    st.write("\n")
    st.markdown("---")
    st.write("\n")
    st.write("\n")
    st.title("💣 Nuclear Database Website (Sophomore Year)")
    st.write("This website was built using Python and features an interactive database detailing every nuclear explosion that took place between 1945 and 1998. The dataset includes"
             " each explosion's location, purpose, deployment method, yield (in kilotons), and other relevant information. This site is interactive, so feel free to explore the data "
             " and visualizations. ")
    st.markdown("*Note: The site may have to be 'woken up' and may take a few extra seconds to load.*")
    st.markdown(
        '<a href="https://erin0411-igmt-nuclear-streamlit-fbbdhv.streamlit.app/" target="_blank">Visit My Nuclear Dashboard</a>',
        unsafe_allow_html=True)

    # MA214 Data Project
    st.write("\n")
    st.write("\n")
    st.markdown("---")
    st.write("\n")
    st.write("\n")
    st.title("💼 Business Startup Time Data Project (Freshman Year)")
    st.write(
        "The following data analysis was conducted using a World Bank database containing information on business startups from over 188 individuals. The goal of the analysis was to determine"
        " whether there is any correlation between the average time it takes to start a business and other factors in the dataset, such as gender and continent. All necessary testing was performed"
        " using R Script.")

    startup_path = base_path / "business_start_time.pdf"
    with open(startup_path, "rb") as f:
        st.download_button(
            label="📥 Download Business Startup Project",
            data=f,
            file_name="business_start_time.pdf",
            mime="application/pdf"
        )

#View Source Code
if page_select == "View Source Code":
    with open(os.path.abspath(__file__), "r", encoding = "utf-8") as f:
        source_code = f.read()
    st.code(source_code, language = "python")