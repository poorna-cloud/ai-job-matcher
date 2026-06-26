import pdfplumber

SKILLS = [
    "Python", "SQL", "Git", "GitHub", "AWS", "Docker",
    "C", "C++", "Java", "JavaScript", "HTML", "CSS",
    "FastAPI", "Flask", "Django", "REST API", "Linux",
    "MATLAB", "Xilinx Vivado", "Cadence", "Verilog",
    "Embedded C", "Arduino", "Machine Learning",
    "Data Structures", "Algorithms", "NumPy",
    "Pandas", "OpenCV"
]


def extract_text_from_pdf(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def detect_skills(text):
    detected = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            detected.append(skill)

    return detected


def calculate_match_score(resume_skills, job_skills):

    matched = []
    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_skills)) * 100

    return score, matched, missing
def get_keyword_status(resume_skills, job_skills):

    matched = []
    missing = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    return matched, missing