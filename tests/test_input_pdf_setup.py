import unittest
from unittest.mock import patch, MagicMock
from src.app import input_pdf_setup


class TestInputPdfSetup(unittest.TestCase):

    @patch('src.app.pdf2image.convert_from_bytes')
    def test_input_pdf_setup_success(self, mock_convert_from_bytes):
        mock_image = MagicMock()
        mock_image.save = MagicMock()
        mock_convert_from_bytes.return_value = [mock_image]

        pdf_file = MagicMock()  # Mock PDF file
        result = input_pdf_setup(pdf_file)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['mime_type'], 'image/jpeg')
        self.assertTrue(mock_image.save.called)

    def test_input_pdf_setup_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            input_pdf_setup(None)
