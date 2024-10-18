import unittest
from unittest.mock import patch, MagicMock
from src.app import get_gemini_response

class TestGeminiResponse(unittest.TestCase):
    
    @patch('src.app.genai.GenerativeModel')  # Mocking the GenerativeModel
    def test_get_gemini_response_success(self, mock_generative_model):
        mock_model_instance = mock_generative_model.return_value
        mock_model_instance.generate_content.return_value = MagicMock(text="This is a test response")

        input_text = "Sample Job Description"
        pdf_content = [{"mime_type": "image/jpeg", "data": "sample_base64_encoded_data"}]
        prompt = "Sample Prompt"

        response = get_gemini_response(input_text, pdf_content, prompt)

        self.assertEqual(response, "This is a test response")
        mock_model_instance.generate_content.assert_called_once_with([input_text, pdf_content[0], prompt])

    @patch('src.app.genai.GenerativeModel')  # Mocking the GenerativeModel
    def test_get_gemini_response_no_text(self, mock_generative_model):
        mock_model_instance = mock_generative_model.return_value
        mock_model_instance.generate_content.return_value = None  # No 'text' attribute

        input_text = "Sample Job Description"
        pdf_content = [{"mime_type": "image/jpeg", "data": "sample_base64_encoded_data"}]
        prompt = "Sample Prompt"

        response = get_gemini_response(input_text, pdf_content, prompt)

        # Now it should return 'No response from model' since there's no 'text' attribute
        self.assertEqual(response, "No response from model")
