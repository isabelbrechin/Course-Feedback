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

@app.route("/", methods=["GET", "POST"])
def index():
    compassionate_response = ""
    if request.method == "POST":
        feedback_content = request.form.get("feedback", "")

        # Using 'messages' for a chat completion task with OpenAI for analysis
        analysis_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, and provide a summary. Please format your response with 'Sentiment:', followed by 'Keywords:', and end with 'Summary:'."},
                {"role": "user", "content": feedback_content}
            ],
            temperature=0.5,
            max_tokens=60,
        )

        # Access the message content directly
        analysis_result = analysis_response.choices[0].message.content
        parts = analysis_result.split("\n")
        sentiment = parts[0].split(": ")[1] if len(parts) > 0 else ""
        keywords = parts[1].split(": ")[1] if len(parts) > 1 else ""
        summary = parts[2].split(": ")[1] if len(parts) > 2 else ""

        conn = get_db_connection()
        conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
        conn.execute("INSERT INTO analysis (sentiment, keywords, summary) VALUES (?, ?, ?)", 
                     (sentiment, keywords, summary))
        conn.commit()
        conn.close()

        compassionate_response = generate_compassionate_response()

    return render_template("index.html", compassionate_response=compassionate_response)

if __name__ == "__main__":
    app.run(debug=True)
