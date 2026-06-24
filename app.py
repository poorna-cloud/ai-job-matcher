import streamlit as st
import pdfplumber

st.title("AI Job Matcher")

st.write("Upload your resume and compare it with a job description.")

resume = st.file_uploader("Upload Your Resume", type=["pdf"])

job_description = st.text_area("Paste Job Description Here")

if resume:

    st.success("Resume uploaded successfully!")

    text = ""

    with pdfplumber.open(resume) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text

    skills = [
        "Python",
        "SQL",
        "Git",
        "AWS",
        "Docker",
        "C",
        "MATLAB",
        "Xilinx Vivado",
        "Cadence"
    ]

    # Resume Skills
    detected_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            detected_skills.append(skill)

    st.subheader("Detected Resume Skills")

    for skill in detected_skills:
        st.write("✅", skill)

    # Job Description Skills
    job_skills = []

    for skill in skills:
        if skill.lower() in job_description.lower():
            job_skills.append(skill)

    st.subheader("Job Skills")

    for skill in job_skills:
        st.write("📌", skill)
    matched_skills = []

    for skill in job_skills:
        if skill in detected_skills:
            matched_skills.append(skill)

    if len(job_skills) > 0:
        match_score = (len(matched_skills) / len(job_skills)) * 100
    else:
        match_score = 0

    st.subheader("Match Score")

    st.write(f"{match_score:.0f}%")
    missing_skills = []

    for skill in job_skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.write("❌", skill)
    st.subheader("Matched Skills")

    for skill in matched_skills:
        st.write("✅", skill)

    st.subheader("Suggestions")

    for skill in missing_skills:
        st.write(f"💡 Learn {skill} fundamentals")