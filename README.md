# NLP Emotion Detection Web App

This is a simple web application that detects emotions in text using OpenAI's GPT-4o-mini model. The app is built with Flask for the backend and HTML/CSS/JavaScript for the frontend. It allows users to input text, analyzes the sentiment, and returns the likelihood of each emotion as a percentage.

### Table of Contents

- Installation
- Usage
- Project Structure
- API Endpoints
- Customization
- Contributing
- License


### Installation

**Prerequisites**

* Python 3.7 or higher
* pip (Python package installer)
* Git

**Steps**

1. Clone the repository:
```
git clone https://github.com/nickklos10/NLP-emotion-detecion.git
cd NLP-emotion-detecion

```

2. Create a virtual environment (optional but recommended):
```

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3. Export your API key as an environment variable:

For macOS:
```
export OPENAI_API_KEY='your-api-key-here'

```

For Windows:
```
set OPENAI_API_KEY=your-api-key-here

```

4. Run the Flask application:
```
python server.py

```

### Usage

* Enter the text you want to analyze in the input field.
* Click the "Run Sentiment Analysis" button.
* The app will display the likelihood of each emotion (anger, disgust, fear, joy, sadness) and highlight the dominant emotion.


### API Endpoints

* GET /: Renders the main HTML page for the application.
* POST /emotionDetector: Accepts text input and returns the likelihood of each emotion and the dominant emotion in a human-readable format.


### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements, bug fixes, or new features.


### License

This project is licensed under the MIT License. See the LICENSE file for details.
