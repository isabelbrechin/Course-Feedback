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

    if request.method == "POST":
        feedback_content = request.form.get("feedback", "")
        
        if 'resubmit' in request.form:
            compassionate_response = generate_compassionate_response()
        else:
            suggestions = generate_feedback_suggestions(feedback_content)
            
            analysis_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant to a university professor. Provide a detailed analysis of student feedback including sentiment, keywords, and a summary. Additionally, suggest specific, actionable recommendations that the professor could take to improve the course based on the feedback. Please format your response with 'Sentiment:', followed by 'Keywords:', followed by 'Summary:, followed by 'Recommended Actions:'." },
                {"role": "user", "content": feedback_content}
            ],
            temperature=0.5,
            max_tokens=250,
            )

        analysis_content = analysis_response.choices[0].message.content.strip()
        parts = analysis_content.split("\n")

        sentiment = ""
        keywords = ""
        summary = ""
        recommended_actions = ""

        try:
            sentiment = parts[0].split("Sentiment: ")[1].strip() if "Sentiment:" in parts[0] else ""
        except IndexError:
                sentiment = ""
            
        try:
            keywords = parts[1].split("Keywords: ")[1].strip() if "Keywords:" in parts[1] else ""
        except IndexError:
                keywords = ""
        try:
            summary = parts[2].split("Summary: ")[1].strip() if "Summary:" in parts[2] else ""
        except IndexError:
                summary = ""
        try:
            recommended_actions = parts[3].split("Recommended Actions: ")[1].strip() if "Recommended Actions:" in parts[3] else ""
        except IndexError:
                recommended_actions = ""

        conn = get_db_connection()
        conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
        conn.execute("INSERT INTO analysis (sentiment, keywords, summary, recommended_actions) VALUES (?, ?, ?, ?)", 
                     (sentiment, keywords, summary, recommended_actions))
        conn.commit()
        conn.close()

    return render_template("index.html", compassionate_response=compassionate_response, suggestions=suggestions, feedback_content=feedback_content)

if __name__ == "__main__":
    app.run(debug=True)
