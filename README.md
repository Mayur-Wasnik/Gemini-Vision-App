# Gemini Image Q&A Application

A Streamlit-based web application that leverages Google's Gemini Vision API to answer questions about uploaded images.

## Features

- **Image Upload**: Upload JPG, JPEG, or PNG images through an intuitive web interface
- **AI-Powered Analysis**: Ask questions about images or get automatic analysis using Gemini 2.5 Flash
- **Real-time Responses**: Get instant responses from Google's Gemini model

## Requirements

- Python 3.8+
- Google API Key (Gemini API access)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download this project

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google API Key:
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

Run the Streamlit application:

```bash
streamlit run vision.py
```

The app will open in your default browser. You can then:

1. Enter a question or prompt (optional)
2. Upload an image
3. Click "Ask the Question" to get a response from Gemini

## Technologies Used

- **Streamlit**: Web application framework
- **Google Gemini API**: Vision and language model
- **Pillow (PIL)**: Image processing
- **python-dotenv**: Environment variable management

## Project Structure

```
.
├── vision.py           # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Notes

- Never commit your `.env` file with API keys to version control
- The `.env` file is excluded in `.gitignore`
- Ensure your Google API key has proper permissions for Gemini Vision API

## License

MIT Licence
