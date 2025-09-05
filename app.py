# app.py

import os
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from utils import get_file_text

# Load environment variables from .env file
load_dotenv()

# --- GOOGLE GEMINI SETUP ---
# Configure the Google Generative AI with the API key
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except (AttributeError, TypeError):
    st.error("🚨 GOOGLE_API_KEY not found. Please set it in your .env file or as a Streamlit secret.")
    st.stop()

# --- LANGCHAIN SETUP ---
# This is the master prompt that guides the AI's analysis.
prompt_template_string = """
You are an expert ATS (Applicant Tracking System) and a highly experienced senior career coach.
Your goal is to provide a detailed, constructive analysis of a resume against a job description.

Analyze the following resume and job description. Provide your analysis in the structured Markdown format specified below.

**Resume Text:**
{resume_text}

**Job Description:**
{job_description}

---

**Required Output Format (Strictly follow this Markdown structure):**

## Match Score: [Provide a percentage]%

## Analysis:
[Provide a 2-3 sentence expert summary of the candidate's fit for the role, highlighting key strengths and weaknesses.]

## Matched Keywords & Strengths:
- [List the key skills and experiences from the resume that align perfectly with the job description.]
- [Another matched keyword or strength.]
- [...]

## Missing Keywords & Gaps:
- [List the crucial keywords and qualifications from the job description that are missing or not emphasized in the resume.]
- [Another missing keyword or gap.]
- [...]

## Actionable Suggestions:
1. **[Suggestion 1]:** [Provide a specific, actionable recommendation. For example: "Incorporate the keyword 'Agile Methodologies' into your project descriptions to better align with the job's requirements."]
2. **[Suggestion 2]:** [Another specific recommendation.]
3. **[Suggestion 3]:** [...]
"""

prompt_template = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template=prompt_template_string
)

# Instantiate the Gemini 1.5 Pro model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

# --- LANGCHAIN CHAIN ---
# The chain connects the prompt, the LLM, and an output parser.
# StrOutputParser ensures the output is a clean string.
chain = prompt_template | llm | StrOutputParser()

# --- STREAMLIT UI ---
st.set_page_config(page_title="Gemini Resume Matcher", page_icon=":male-technologist:")

st.title("👔 Gemini Resume Matcher")
st.markdown("""
Welcome! This tool helps you optimize your resume for a specific job by analyzing it against the job description. 
Simply upload your resume, paste the job description, and let the AI provide you with a detailed analysis and match report.
""")

st.divider()

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.header("Your Resume")
    resume_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"], label_visibility="collapsed")

with col2:
    st.header("Job Description")
    job_description = st.text_area("Paste the job description here", height=300, label_visibility="collapsed")

# Submit button centered
submit_button = st.button("Analyze My Application", type="primary", use_container_width=True)


# --- LOGIC TO RUN ON SUBMIT ---
# This part is currently empty and will be filled in the next task.
if submit_button:
    st.info("The 'Analyze' button was clicked! The logic to process the inputs will be added in the final step.")
    # The integration logic will go here.