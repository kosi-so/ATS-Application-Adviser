from dotenv import load_dotenv
import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    if response and hasattr(response, 'text'):
        return response.text
    else:
        return "No response from model"

def input_pdf_setup(pdf_file):
    if pdf_file is not None:
        # Convert PDF to image
        images = pdf2image.convert_from_bytes(pdf_file.read())

        # first_page = images[0]
        pdf_parts=[]
        for image in images:
            # Convert to bytes 
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts.append({
                    'mime_type': 'image/jpeg',
                    'data':base64.b64encode(img_byte_arr).decode()  # encode to base64
            })

        return pdf_parts
    else:
         raise FileNotFoundError('No file uploaded')

input_prompt1= """
            As an HR manager, Compare the uploaded resume with the provided job description. 
            Provide feedback on how well the candidate’s experience, skills, and qualifications align with the job requirements. 
            Highlight strengths, weaknesses, and areas for improvement
    """
input_prompt2="""
            As an HR manager, Compare the uploaded resume with the provided job description. 
            Provide feedback on how candidate get improve skills to fit job description
    """

input_prompt3="""
            As a HR manager, Compare the uploaded resume with the provided job description.
            Write a cover letter in 250 words for the applicant based on their resume and the job description
    """

input_prompt4= """
            As an Application Tracking System(ATS), Compare the technical and soft skills in the job description with those listed on the resume. 
            Highlight any major skill gaps or underrepresented skills and give a percentage for how much the resume matches the job description"
            
    """
# Streamlit App
def main():
    st.set_page_config(page_title="Resume Expert")
    st.header("ATS Tracking System")
    input_text =st.text_area("Job Description: ", key='input')
    uploaded_file=st.file_uploader("Upload your Resume(PDF)...", type=['pdf'])

    if uploaded_file is None:
        st.write("Please Upload Resume")
    else:
        st.write("Resume Uploaded Successfully")

    submit1 = st.button("Tell Me About My Resume")

    submit2= st.button("How Can I Improve my Skills")

    submit3= st.button("Write a Cover letter")

    submit4=st.button("Percentage match")


    if submit1:
        pdf_data = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_data, input_prompt1)
        st.subheader("Resume Expert:")
        st.write(response)

    elif submit2:
        pdf_data = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_data, input_prompt2)
        st.subheader("Resume Expert:")
        st.write(response)

    elif submit3:
        pdf_data = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_data, input_prompt3)
        st.subheader("Resume Expert:")
        st.write(response)

    elif submit4:
        pdf_data = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_data, input_prompt4)
        st.subheader("Resume Expert:")
        st.write(response)

    
if __name__=="__main__":
    main()