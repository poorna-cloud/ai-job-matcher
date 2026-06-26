import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ai_resume_review(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze this resume based on the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Give:

1. ATS Score out of 100

2. Summary

3. Strengths

4. Weaknesses

5. Missing Skills

6. Resume Improvements

7. Final Verdict
"""

    response = model.generate_content(prompt)

    return response.text


def rewrite_resume(resume_text, job_description):

    prompt = f"""
You are an expert resume writer.

Rewrite the following resume according to the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Rules:

- Rewrite Career Objective.
- Improve Technical Skills section.
- Rewrite Projects professionally.
- Add ATS keywords naturally.
- Do not invent new skills or experience.

Return the rewritten resume in Markdown.
"""

    response = model.generate_content(prompt)

    return response.text


def generate_cover_letter(resume_text, job_description):

    prompt = f"""
Generate a professional cover letter.

Resume:
{resume_text}

Job Description:
{job_description}

Rules:

- One page
- Professional tone
- Mention relevant skills
- Mention relevant projects
- End professionally

Do not invent information.
"""

    response = model.generate_content(prompt)

    return response.text
def generate_learning_roadmap(missing_skills):

    prompt = f"""
You are an experienced software mentor.

The candidate is missing these skills:

{', '.join(missing_skills)}

Create a learning roadmap.

Format:

# 30-Day Learning Roadmap

Week 1:
...

Week 2:
...

Week 3:
...

Week 4:
...

Mention:
- Best learning order
- Practice ideas
- Mini project ideas

Keep it beginner friendly.
"""

    response = model.generate_content(prompt)

    return response.text
def generate_interview_questions(resume_text, job_description):

    prompt = f"""
You are an experienced technical interviewer.

Based on the resume and job description, generate:

1. 5 Technical Interview Questions
2. 5 Project-based Questions
3. 5 HR Questions
4. Expected answers (2-3 lines each)

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = model.generate_content(prompt)

    return response.text