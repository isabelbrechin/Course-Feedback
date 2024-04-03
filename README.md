## Overview
This web application is a generative AI-powered tool designed to enhance the educational experience by providing professors with a sophisticated analysis of student feedback. By using sentiment analysis, keyword extraction, and summarization capabilities of OpenAI's GPT-3.5, this app identifies the core sentiments and topics from student feedback and presents actionable insights to educators.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Innovation and Solution](#innovation-and-solution)
- [Technological Stack](#technological-stack)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Problem Statement
In the traditional educational setting, collecting and analyzing student feedback is often a manual and time-consuming process. Professors find it challenging to derive meaningful conclusions from vast amounts of qualitative data, and as a result, vital insights for improving course delivery are often overlooked.

## Innovation and Solution
The Course-Feedback-Analysis App addresses this problem by automating the collection and analysis of feedback. It applies natural language processing to understand the context and emotions behind student responses, allowing educators to quickly grasp student sentiment and identify areas for improvement.

## Technological Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python), SQLite
- **AI**: OpenAI's GPT-3.5
- **Hosting**: Initially intended for Azure, now hosted on GitHub due to Azure credits limitation.

## Features
- Anonymous feedback submission by students.
- Automated sentiment analysis and keyword extraction using OpenAI's GPT-3.5.
- Summary generation for quick insights into students feedback.
- Generate suggestions for students to improve the quality of their feedback.
- Allow students to resubmit their feedback after reviewing suggestions.
- Responsive web design for accessibility across various devices.
- Compassionate response generation to acknowledge student participation.


## Prerequisites
- Python 3.x
- Pip package manager
- Flask web framework
- SQLite for database management
- OpenAI API key

## Installation
To install this application:

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/isabelbrechin/Course-Feedback

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
To run the application on your desktop server, execute:
    ```
    python -m flask app app run
    ```
Visit `http://127.0.0.1:5000/` in your web browser to view the application.

## License
This project is made available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors
- Isabel Brechin

## Acknowledgments
- Dalhousie University for the imagery and brand.
- Thanks to Dalhousie University for the inspiration behind the project.
- OpenAI for providing the AI technology that powers the feedback analysis.
- Based on code from Colin Conrads REBtrainer and Snaptutor web applications.

## Contact
For support, feedback, or contributions, contact `is417236@dal.ca` or open an issue in this GitHub repository.
