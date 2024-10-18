import unittest
from unittest.mock import patch, MagicMock
from src import app  # Importing the whole app to access main()

class TestStreamlitApp(unittest.TestCase):

    @patch('src.app.st.file_uploader')
    @patch('src.app.st.text_area')
    @patch('src.app.st.button')
    @patch('src.app.st.write')
    @patch('src.app.get_gemini_response')
    @patch('src.app.input_pdf_setup')
    def test_main_with_uploaded_file(self, mock_input_pdf_setup, mock_get_gemini_response, mock_write, mock_button, mock_text_area, mock_file_uploader):
        # Mocking Streamlit inputs and outputs
        mock_file_uploader.return_value = MagicMock()  # Simulating an uploaded file
        mock_text_area.return_value = "Job Description"
        mock_button.side_effect = [True, False, False, False]  # Only submit1 button is clicked
        mock_input_pdf_setup.return_value = [{"mime_type": "image/jpeg", "data": "sample_data"}]
        mock_get_gemini_response.return_value = "Sample Response"

        app.main()  # Run the main app function

        # Assert file uploader was called
        mock_file_uploader.assert_called_once_with("Upload your Resume(PDF)...", type=['pdf'])

        # Assert get_gemini_response was called with correct parameters
        mock_get_gemini_response.assert_called_once_with("Job Description", [{"mime_type": "image/jpeg", "data": "sample_data"}], app.input_prompt1)

        # Assert the write function was called to display the result
        mock_write.assert_called_with("Sample Response")
