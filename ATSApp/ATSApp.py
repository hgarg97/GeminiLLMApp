import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import pyperclip

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(jd_input, resume_text, additional_info, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([jd_input, resume_text, additional_info, prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

about_resume_prompt = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume and additional information
   against the job description. Please share your professional evaluation on whether the candidate's profile aligns with the role.
   Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

percent_match_prompt = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume and additional information against the provided job description. give me the percentage of 
match if the resume matches the job description. First the output should come as percentage and then keywords missing and 
last final thoughts.
"""

cover_letter_prompt = """
You are a skilled Technical Human Resource Manager with a deep understanding of data science and computer science, who will be reviewing
the applicant's cover letter.Your task is to leverage the resume and additional information provided against the given job description. 
Also, Your objective is to incorporate relevant keywords from the job descriptionwithin the scope of work the applicant has done
and draft a cover letter in relevant format to enhance the applicant's prospects for the specified job. You can use resume or additional info to gather basic information of the candidate
like Name, Address etc.
"""

mail_to_recruiter_prompt = """
"Leverage the resume and additional information provided against the given job description. 
Incorporate relevant keywords from the job description within the scope of work the applicant has done. 
Draft an email in proper email format to the company's HR Recruiter, who is an expert in technical fields like Data Science 
and Computer Science, to enhance the applicant's prospects for the specified job. 
You can use the resume or additional information to gather basic information of the candidate, such as name and address, if needed."
"""

## streamlit app

# Setting Page Theme

def set_theme(theme):
    if theme != "Light":
        st.markdown(f"## ATS Resume Evaluator - {theme} Theme")
        st.markdown("---")
        st.write(f"Using the {theme} theme...")
        st.markdown("---")
        if theme == "Dark":
            st.markdown("""
                <style>
                    .stApp {
                        color: white;
                        background-color: #1E1E1E;
                    }
                </style>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <style>
                    .stApp {{
                        background-color: {theme.lower()};
                    }}
                </style>
            """, unsafe_allow_html=True)

def layout_buttons():
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        submit1 = st.button("Tell Me About the Resume")

    with col2:
        submit2 = st.button("Percentage Match")

    with col3:
        submit3 = st.button("Write Cover Letter")

    with col4:
        submit4 = st.button("Compose Email to Recruiter")

    return submit1, submit2, submit3, submit4


st.set_page_config(page_title="ATS Resume Evaluator", page_icon=":clipboard:")
set_theme("Light")  # Set default theme

st.title("ATS Resume Evaluator")
st.markdown("---")

# Main content
jd_input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    resume_text=input_pdf_text(uploaded_file)

additional_info = st.text_area("Additional Info:", key="additional_info", value="")

# Buttons layout
submit1, submit2, submit3, submit4 = layout_buttons()

if submit1:
    if uploaded_file is not None:
        response=get_gemini_response(jd_input_text, resume_text, additional_info, about_resume_prompt)
        st.subheader("The Response is")
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")

if submit2:
    if uploaded_file is not None:
        response=get_gemini_response(jd_input_text, resume_text, additional_info, percent_match_prompt)
        st.subheader("The Response is")
        st.subheader(response)
    else:
        st.write("Please uplaod the resume")

if submit3:
    if uploaded_file is not None:
        response = get_gemini_response(jd_input_text, resume_text, additional_info, cover_letter_prompt)
        st.subheader("Cover Letter:")
        st.text_area("Cover Letter Content:", value=response, height=200, key="cover_letter")
        st.button("Copy Cover Letter", on_click=lambda: pyperclip.copy(st.session_state["cover_letter"]))
    else:
        st.write("Please upload the resume")

if submit4:
    if uploaded_file is not None:
        response = get_gemini_response(jd_input_text, resume_text, additional_info, mail_to_recruiter_prompt)
        st.subheader("Email to Recruiter:")
        st.text_area("Email Content:", value=response, height=200, key="email_content")
        st.button("Copy Email Content", on_click=lambda: pyperclip.copy(st.session_state["email_content"]))
    else:
        st.write("Please upload the resume")