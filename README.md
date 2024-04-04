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
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Problem Statement
In the traditional educational setting, collecting and analyzing student feedback is often a manual and time-consuming process. Professors find it challenging to derive meaningful conclusions from vast amounts of qualitative data, and as a result, vital insights for improving course delivery are often overlooked.

Additionally, the quality of student feedback varies considerably. Research indicates that consistent quality in student feedback can significantly improve professors' capacity to understand and incorporate student suggestions.


## Innovation and Solution
The Course-Feedback-Analysis App addresses this problem by automating the collection and analysis of feedback. It applies natural language processing to understand the context and emotions behind student responses, allowing educators to quickly grasp student sentiment and identify areas for improvement.

Furthermore, the app encourages students to enhance the quality of their feedback through AI-powered suggestions, fostering an environment of continuous improvement and effective communication between students and their professors.


## Technological Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python), SQLite
- **AI**: OpenAI's GPT-3.5
- **Hosting**: Initially intended for Azure, now hosted on GitHub due to Azure credits limitation.

## Features
- Feedback submission by students.
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

After installing the Course Feedback Analysis app, you can start using it with the following steps:

1. **Starting the Application**:
   To launch the application, navigate to the app's directory in your terminal and run:

    ```
    python -m flask app app run
    ```
This will start the Flask server, and you should see output indicating that the server is running, typically on `http://127.0.0.1:5000/`.

2. **Accessing the Application**:
Open a web browser and visit `http://127.0.0.1:5000/`. This will take you to the homepage of the application.

3. **Submitting Feedback**:
- On the homepage, you'll find a form where students can enter and submit their course feedback.
- After submitting feedback, students will receive suggestions on how they can improve their feedback for more constructive communication.

4. **Reviewing Submissions** (For Professors):
- Currently, to review the analysis of the feedback, professors/administrators need to access the database directly. This process will be updated in future versions for easier access through the application interface.

-Testing the Database: 
    To ensure the database is functioning correctly, navigate back to the appropriate directory in command, and then run python db_test.py

- Accessing the Database:
   The application stores feedback and analysis in an SQLite database named `database.db`. To access this database, navigate to your sqlite3 app and open the database.db file.

- Reviewing Data:
The results of the query will provide you with the feedback ID, sentiment analysis, extracted keywords, and summary. Review these to gain insights into student feedback and determine areas for improvement in the course.

## License
This project is made available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors
- Isabel Brechin

## Acknowledgments
- Dalhousie University for the imagery and brand.
- Thanks to Dalhousie University for the inspiration behind the project.
- OpenAI for providing the AI technology that powers the feedback analysis.
- Based on code from Colin Conrads REBtrainer and Snaptutor web applications.
- ChatGPT assisted with developing the parsing structure of app.py. 

## Contact
For support, feedback, or contributions, contact `is417236@dal.ca` or open an issue in this GitHub repository.
