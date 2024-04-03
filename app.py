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
    # Access the message content directly
    return response.choices[0].message.content.strip()

def generate_feedback_suggestions(feedback):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            'role': 'system',
            'content': 'Your task is to provide constructive suggestions for improving student feedback.'
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
    analysis_content = ""
    sentiment = ""
    keywords = ""
    summary = ""
    recommended_actions = ""

    if request.method == "POST":
        feedback_content = request.form.get("feedback", "")
        
        if 'resubmit' in request.form:
            compassionate_response = generate_compassionate_response()
        else:
            suggestions = generate_feedback_suggestions(feedback_content)
            
            analysis_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, provide a summary, and include a recommended action for the professor based on the student feedback. Please format your response with 'Sentiment:', followed by 'Keywords:', followed by 'Summary:, followed by 'Recommended Actions:'."},
                {"role": "user", "content": feedback_content}
            ],
            temperature=0.5,
            max_tokens=60,
            )

        analysis_content = analysis_response.choices[0].message.content.strip()

        parts = analysis_content.split("\n")

            # Initialize variables for sentiment, keywords, summary, and recommended_actions
        sentiment_parts = []
        keywords_parts = []
        summary_parts = []
        recommended_actions_parts = []

            # Check that the list has the expected number of parts before accessing
        if len(parts) > 0:
                sentiment_parts = parts[0].split(": ")
                sentiment = sentiment_parts[1].strip() if len(sentiment_parts) > 1 else ""
        if len(parts) > 1:
                keywords_parts = parts[1].split(": ")
                keywords = keywords_parts[1].strip() if len(keywords_parts) > 1 else ""
        if len(parts) > 2:
                summary_parts = parts[2].split(": ")
                summary = summary_parts[1].strip() if len(summary_parts) > 1 else ""
        if len(parts) > 3:
                recommended_actions_parts = parts[3].split(": ")
                recommended_actions = recommended_actions_parts[1].strip() if len(recommended_actions_parts) > 1 else ""
                
   
    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
    conn.execute("INSERT INTO analysis (sentiment, keywords, summary, recommended_actions) VALUES (?, ?, ?, ?)", 
                     (sentiment, keywords, summary, recommended_actions))
    conn.commit()
    conn.close()

    return render_template("index.html", compassionate_response=compassionate_response, suggestions=suggestions, feedback_content=feedback_content)

if __name__ == "__main__":
    app.run(debug=True)
