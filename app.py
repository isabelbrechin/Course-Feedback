import os
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get(".env"),
    )

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        feedback_content = request.form["feedback"]

    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, and provide a summary. Please format your response with 'Sentiment:', followed by 'Keywords:', and end with 'Summary:'. "},
                {"role": "user", "content": feedback_content}
            ]
        )

    analysis_result = response.choices[0].message.content
    parts = analysis_result.split("\n")
    sentiment = parts[0].replace("Sentiment: ", "").strip()
    keywords = parts[1].replace("Keywords: ", "").strip()
    summary = parts[2].replace("Summary: ", "").strip()

    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
    conn.execute("INSERT INTO analysis (sentiment, keywords, summary) VALUES (?, ?, ?)", 
                     (sentiment, keywords, summary))
    conn.commit()
    conn.close()

    compassionate_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            prompt="Generate a compassionate thank you message for a student who has just submitted feedback.",
            temperature=0.7,
            max_tokens=60,
        ).choices[0].text.strip()
    
    return render_template("index.html", compassionate_response=compassionate_response)  


if __name__ == "__main__":
    app.run(debug=True)
