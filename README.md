# ATS Application Adviser
ATS Resume Expert is a web-based application that helps users analyze their resumes against job descriptions using Google's Generative AI (Gemini). The app provides feedback on how well the resume aligns with the job description, generates suggestions for skill improvement, writes cover letters, and calculates a percentage match based on technical and soft skills.

The app is built with Streamlit and allows users to upload their resume (in PDF format) and compare it to a given job description.

## Features 
- Resume Feedback: Provides insights on how well the resume matches the job description, highlighting strengths, weaknesses, and areas for improvement.
- Skill Improvement Suggestions: Recommends ways to improve skills based on job requirements.
- Cover Letter Generator: Automatically generates a cover letter tailored to the job description and resume.
- Percentage Match: Calculates how much the resume matches the job description in terms of skills and qualifications.

## Technology Stack
- Python 3.x
- Streamlit: Web framework for interactive UI.
- Google Generative AI (Gemini): Used to analyze the resume against the job description.
- pdf2image: Converts PDF resumes into images for processing.
- Pillow (PIL): For handling image manipulation.
- unittest and mock: For unit testing the application.
- dotenv: For securely handling API keys and environment variables.

## Prerequisites 
Before setting up the project, ensure you have the following installed:
- Python 3.x
- A Google Cloud account with access to the Google Generative AI (Gemini) API
- API key for Google Generative AI

## Installation
1. Clone the Repository
   `git clone https://github.com/your-username/ats-resume-expert.git
   cd ats-resume-expert`
3. Create and Activate Virtual Environment
   `conda create venv`
   `conda activate venv/`
3. Install dependencies
   `pip install requirements.txt`
4. Setup .env file
   Create .env file in root directory with your Google API Key
   `GOOGLE_API_KEY=your_google_api_key`
5. Run the Application
   To start application locally, run the following command
   `streamlit run app.py`

## How to Use Application
1. **Input Job Description**: Type the job description into the text area provided
2. **Upload Resume**: Upload your resume in PDF format.
3. **Select an Action**: Select one of the following actions
   - Tell Me About My Resume: Provides feedback on how well your resume aligns with the job description.
   - How Can I Improve My Skills: Suggests ways to enhance your skills based on job requirements.
   - Write a Cover Letter: Generates a cover letter tailored to your resume and job description.
   - Percentage Match: Calculates a percentage match between your resume and the job description.
  
## Contribution 
Contributions are welcome! If you want to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Create a Pull request

## Acknowledgments
- Google Generative AI API: Thanks to Google for providing the tools to analyze resumes with AI.
- Streamlit: A great framework for building interactive web applications in Python.
- [Krish Naik] (https://github.com/krishnaik06)
