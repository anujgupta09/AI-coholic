# gradio pyMuPDF gemini

# 4 inputs of user 
# Inputs >> text from pdf 1 , text from pdf 2 
# Inputs >> Question of user , system prompt 

# 1 output by model 
# Answer to the question based on the two pdfs and system prompt

#--------------------------------------------------------------------------------------------------------------

import fitz
from google import genai
import os
from  dotenv import load_dotenv
load_dotenv()

# resume = "Anuj_Gupta.pdf"
# jd = "DevOps_Engineer_JD.pdf"
question = "list resume skills that match and skills that dont match with JD (dont miss even 1 single skill here matched and not matched ), overall  resume JD  match in % ,  and Conclude with yes or no for me to apply in this job , all this in less than 100 words "

def process_files(resume, jd):

    resume_pdf = fitz.open(resume)
    resume_text=""
    for page in resume_pdf:
        resume_text += page.get_text()
    
    jd_pdf = fitz.open(jd)
    jd_text=""
    for page in jd_pdf:
        jd_text += page.get_text()

    client = genai.Client(api_key=os.getenv("gemini"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Resume: {resume_text} \n Job Description: {jd_text} \n System_role: Be very accurate and consistent with your answer , not like everytime you are givign different percentage \n Question: {question}"
    )
    return response.text

#-------------------------------------------------------------------------------------------------------------

import gradio

with gradio.Blocks() as JD_2_Resume:
    gradio.Markdown("JD_2_Resume")
    resume = gradio.File(label="Upload your Latest Resume as pdf")
    jd = gradio.File(label="Upload the Job Description as pdf")
    answer = gradio.Text(label="Answer")
    # need button to click after all i/p is taken
    button = gradio.Button("Process")
    button.click(inputs=[resume,jd], outputs=answer, fn=process_files)
JD_2_Resume.launch()

