import streamlit as st
from fpdf import FPDF
import requests
from langchain.prompts import PromptTemplate

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="AI Resume Builder", layout="centered")

# ---------------------------
# Prompt Template
# ---------------------------
resume_prompt = PromptTemplate.from_template("""
You are a professional resume writer. Generate a clean, ATS-friendly resume using the information below.

Name: {name}
Contact Information: {contact_info}
Education: {education}
Experience: {experience}
Skills: {skills}
Projects: {projects}
Target Job Description: {job_description}

Use bullet points where needed and keep formatting professional.
Only return the final resume. Do not include notes, suggestions, or formatting advice.
""")

# ---------------------------
# PDF Export Function
# ---------------------------
def save_as_pdf(resume_text, filename="resume.pdf"):
    # Replace unsupported characters with standard ones
    resume_text = resume_text.replace("•", "-")  # bullet point
    resume_text = resume_text.encode("ascii", "ignore").decode()  # strip other Unicode characters

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in resume_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename


# ---------------------------
# Resume Generator (OpenRouter)
# ---------------------------
def generate_resume(prompt_text):
    api_key = st.secrets["OPENROUTER_API_KEY"]  # ⬅️ Load from secrets

    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
        "HTTP-Referer": "https://resume-builder-app-wuvkaly2ubbqydvrjqrcny.streamlit.app/",  # use your real app URL
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "user", "content": prompt_text}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}\n{response.text}"


# ---------------------------
# Streamlit UI
# ---------------------------
st.title("📄 AI-Powered Resume Builder")

with st.form("resume_form"):
    name = st.text_input("Full Name")
    contact_info = st.text_input("Contact Information (email, phone, etc.)")
    education = st.text_area("Education")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    job_description = st.text_area("Job Description You’re Applying For")
    submitted = st.form_submit_button("Generate Resume")

if submitted:
    if not all([name, education, experience, skills, projects, job_description]):
        st.error("Please fill out all fields.")
    else:
        with st.spinner("Crafting your personalized resume..."):

            prompt_text = resume_prompt.format(
                name=name,
                contact_info=contact_info,
                education=education,
                experience=experience,
                skills=skills,
                projects=projects,
                job_description=job_description
            )

            resume_text = generate_resume(prompt_text)

            st.success("Resume generated successfully! 👇")
            st.text_area("📄 Resume Output", resume_text, height=400)

            filename = save_as_pdf(resume_text)
            with open(filename, "rb") as f:
                st.download_button(
                    label="📥 Download Resume as PDF",
                    data=f,
                    file_name="generated_resume.pdf",
                    mime="application/pdf"
                )
