# Course-Feedback
## Description
This Flask-based web application enables professors to collect and analyze student feedback for their courses. Leveraging the power of OpenAI's GPT-3, the app provides sentiment analysis, keyword extraction, and summary generation to derive meaningful insights from student submissions.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features
- Collect anonymous feedback from students
- Analyze feedback using GPT-3 for sentiment and content
- Generate compassionate responses to acknowledge submissions
- Easy to use with a simple and responsive web interface

## Prerequisites
Before running this application, you'll need the following installed:
- Python 3.x
- Flask
- SQLite3

## Installation
To install this application:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/your-username/your-repo-name.git

    ```
2. Install the necessary Python packages:
    ```
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    ```
    cp .env.example .env
    # Edit .env file to include your OPENAI_API_KEY
    ```

4. Initialize the database with the provided schema:
    ```
    python init_db.py
    ```

## Usage
To run the server, execute:
    ```
    python -m flask app app run
    ```
Visit `http://127.0.0.1:5000/` in your web browser to view the application.

## Contributing
We welcome contributions! Please read through our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to submit pull requests.

## License
This project is made available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors
- Your Name - Initial Work

## Acknowledgments
- Dalhousie University for the imagery and brand inspiration.
- OpenAI for the GPT-3 API used in feedback analysis.

## Contact
For support, feedback, or contributions, contact `your.email@example.com` or open an issue in this GitHub repository.
