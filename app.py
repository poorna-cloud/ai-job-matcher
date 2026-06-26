import streamlit as st
from ai import (
    ai_resume_review,
    rewrite_resume,
    generate_cover_letter,
    generate_interview_questions,
    generate_learning_roadmap
)
from utils import (
    extract_text_from_pdf,
    detect_skills,
    calculate_match_score
)

from charts import (
    show_pie_chart,
    show_bar_chart
)

from ai import (
    ai_resume_review,
    rewrite_resume,
    generate_cover_letter
)

from ui import (
    load_css,
    hero_section,
    sidebar,
    footer
)


st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

load_css()

hero_section()

sidebar()


st.markdown("## 📄 Upload Resume")

resume = st.file_uploader(
    "",
    type=["pdf"]
)

st.markdown("## 💼 Job Description")

job_description = st.text_area(
    "",
    height=220,
    placeholder="Paste Job Description Here..."
)
if resume:

    resume_text = extract_text_from_pdf(resume)

    resume_skills = detect_skills(resume_text)

    job_skills = detect_skills(job_description)

    match_score, matched_skills, missing_skills = calculate_match_score(
        resume_skills,
        job_skills
    )

    st.success("✅ Resume uploaded successfully!")
    st.markdown("## 📊 Resume Dashboard")

    col1, col2, col3,col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 5px 15px rgba(0,0,0,.08);
        text-align:center;
        ">
        <h4 style="color:#2563eb;">🎯 Match Score</h4>
        <h1 style="color:#16a34a;">{match_score:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 5px 15px rgba(0,0,0,.08);
        text-align:center;
        ">
        <h4 style="color:#2563eb;">✅ Matched Skills</h4>
        <h1 style="color:#16a34a;">{len(matched_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 5px 15px rgba(0,0,0,.08);
        text-align:center;
        ">
        <h4 style="color:#2563eb;">❌ Missing Skills</h4>
        <h1 style="color:#dc2626;">{len(missing_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)
    with col4:

        st.markdown(f"""
        <div style="
        background:white;
        padding:25px;
        border-radius:18px;
        box-shadow:0px 5px 15px rgba(0,0,0,.08);
        text-align:center;
        ">
        <h4 style="color:#2563eb;">📄 Resume Skills</h4>
        <h1 style="color:#0f766e;">{len(resume_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)
    st.write(f"### 🎯 ATS Match Score: {match_score:.0f}%")
    st.progress(match_score / 100)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Resume Skills")

        if resume_skills:

            for skill in resume_skills:

                st.markdown(
                    f"""
                    <span style="
                    display:inline-block;
                    background:#dbeafe;
                    color:#1d4ed8;
                    padding:8px 15px;
                    margin:5px;
                    border-radius:20px;
                    font-weight:bold;
                    border:1px solid #93c5fd;
                    ">
                    {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.warning("No skills detected.")
            
    with col2:

        st.subheader("💼 Job Requirements")

        if job_skills:

            for skill in job_skills:

                st.markdown(
                    f"""
                    <span style="
                    display:inline-block;
                    background:#fef3c7;
                    color:#92400e;
                    padding:8px 15px;
                    margin:5px;
                    border-radius:20px;
                    font-weight:bold;
                    border:1px solid #fbbf24;
                    ">
                    {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.warning("No job skills found.")
        st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:

                st.markdown(
                    f"""
                    <span style="
                    display:inline-block;
                    background:#dcfce7;
                    color:#166534;
                    padding:8px 15px;
                    margin:5px;
                    border-radius:20px;
                    font-weight:bold;
                    border:1px solid #22c55e;
                    ">
                    ✅ {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.info("No matched skills.")


    with col4:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.markdown(
                    f"""
                    <span style="
                    display:inline-block;
                    background:#fee2e2;
                    color:#991b1b;
                    padding:8px 15px;
                    margin:5px;
                    border-radius:20px;
                    font-weight:bold;
                    border:1px solid #ef4444;
                    ">
                    ❌ {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.success("No missing skills.")
    st.divider()

    st.subheader("💡 Suggestions")

    if missing_skills:

        for skill in missing_skills:
            st.write(f"👉 Learn **{skill}**")

    else:
        st.success("Excellent! Your resume matches the job description.")
    st.divider()

    show_pie_chart(matched_skills, missing_skills)

    show_bar_chart(resume_skills, job_skills)
    st.divider()
    
    # -------------------- AI Resume Review --------------------

with st.container(border=True):

    st.subheader("🤖 AI Resume Review")
    st.caption("Analyze your resume using Gemini AI.")

    if st.button("Analyze Resume with AI", key="review"):

        with st.spinner("Analyzing Resume..."):

            result = ai_resume_review(
                resume_text,
                job_description
            )

        st.markdown(result)

        st.download_button(
            "📥 Download AI Review",
            result,
            file_name="AI_Resume_Review.txt"
        )

st.divider()

# -------------------- Resume Rewriter --------------------

with st.container(border=True):

    st.subheader("✨ AI Resume Rewriter")
    st.caption("Rewrite your resume according to the job description.")

    if st.button("Rewrite Resume", key="rewrite"):

        with st.spinner("Rewriting Resume..."):

            rewritten_resume = rewrite_resume(
                resume_text,
                job_description
            )

        st.markdown(rewritten_resume)

        st.download_button(
            "📥 Download Rewritten Resume",
            rewritten_resume,
            file_name="Rewritten_Resume.md"
        )

st.divider()

# -------------------- Cover Letter --------------------

with st.container(border=True):

    st.subheader("💌 AI Cover Letter")
    st.caption("Generate a professional cover letter instantly.")

    if st.button("Generate Cover Letter", key="cover"):

        with st.spinner("Generating Cover Letter..."):

            cover_letter = generate_cover_letter(
                resume_text,
                job_description
            )

        st.markdown(cover_letter)

        st.download_button(
            "📥 Download Cover Letter",
            cover_letter,
            file_name="Cover_Letter.md"
        )

st.divider()

# -------------------- Interview Questions --------------------

with st.container(border=True):

    st.subheader("🎤 AI Interview Questions")
    st.caption("Practice interview questions generated from your resume.")

    if st.button("Generate Interview Questions", key="interview"):

        with st.spinner("Generating Interview Questions..."):

            questions = generate_interview_questions(
                resume_text,
                job_description
            )

        st.markdown(questions)

        st.download_button(
            "📥 Download Interview Questions",
            questions,
            file_name="Interview_Questions.md"
        )

st.divider()

# -------------------- Learning Roadmap --------------------

with st.container(border=True):

    st.subheader("📚 AI Learning Roadmap")
    st.caption("Get a personalized roadmap based on your missing skills.")

    if st.button("Generate Learning Roadmap", key="roadmap"):

        with st.spinner("Creating Learning Roadmap..."):

            roadmap = generate_learning_roadmap(
                missing_skills
            )

        st.markdown(roadmap)

        st.download_button(
            "📥 Download Learning Roadmap",
            roadmap,
            file_name="Learning_Roadmap.md"
        )

st.divider()

# -------------------- ATS Keyword Analysis --------------------

st.subheader("🎯 ATS Keyword Analysis")

for skill in job_skills:

    if skill in resume_skills:
        st.success(f"✅ {skill}")
    else:
        st.error(f"❌ {skill}")

footer()