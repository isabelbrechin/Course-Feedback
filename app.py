import os
import sqlite3
from flask import Flask, render_template, request
import openai

# Set the API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_compassionate_response():
    # Function to generate a compassionate thank you message using GPT-3.5
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            'role': 'system',
            'content': 'You are a helpful assistant.'
        }, {
            'role': 'user',
            'content': 'Generate a compassionate thank you message for a student who has just submitted course feedback.'
        }],
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].message.content.strip()

def generate_feedback_suggestions(feedback):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            'role': 'system',
            'content': 'Your task is to provide constructive suggestions for improving student feedback to a professor about a course.'
        }, {
            'role': 'user',
            'content': feedback
        }],
        temperature=0.5,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    compassionate_response = ""
    suggestions = ""
    feedback_content = ""
    sentiment = ""
    keywords = ""
    summary = ""

    if request.method == "POST":
        feedback_content = request.form.get("feedback", "")
        
        if 'resubmit' in request.form:
            compassionate_response = generate_compassionate_response()
        else:
            suggestions = generate_feedback_suggestions(feedback_content)
            analysis_response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an assistant to a university professor. Analyze this student feedback and provide 'Sentiment:', 'Keywords:', and 'Summary:'."
                    },
                    {"role": "user", "content": feedback_content}
                ],
                temperature=0.5,
                max_tokens=250,
            )

            analysis_content = analysis_response.choices[0].message.content.strip()
            parts = analysis_content.split("\n")

            # Initialize variables to empty strings
            sentiment_parts = ""
            keywords_parts = ""
            summary_parts = ""

            # Check if the expected sections are in the content and extract them
            for part in parts:
                if "Sentiment:" in part:
                    sentiment_parts = part.split("Sentiment: ")[1].strip()
                elif "Keywords:" in part:
                    keywords_parts = part.split("Keywords: ")[1].strip()
                elif "Summary:" in part:
                    summary_parts = part.split("Summary: ")[1].strip()

            sentiment = sentiment_parts if sentiment_parts else ""
            keywords = keywords_parts if keywords_parts else ""
            summary = summary_parts if summary_parts else ""

            conn = get_db_connection()
            conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
            conn.execute("INSERT INTO analysis (sentiment, keywords, summary) VALUES (?, ?, ?)", 
                         (sentiment, keywords, summary))
            conn.commit()
            conn.close()

    return render_template("index.html", compassionate_response=compassionate_response, suggestions=suggestions, feedback_content=feedback_content)

if __name__ == "__main__":
    app.run(debug=True)
