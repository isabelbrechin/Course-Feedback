import os
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        feedback_content = request.form["feedback"]  # Adjusted to capture feedback content

        # Using 'messages' as per the original file for a chat completion task
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, and provide a summary. Please format your response with 'Sentiment:', followed by 'Keywords:', and end with 'Summary:'. "},
                {"role": "user", "content": feedback_content}
            ]
        )

        # Parsing the structured response from OpenAI
        analysis_result = response.choices[0].message.content
        parts = analysis_result.split("\n")
        sentiment = parts[0].replace("Sentiment: ", "").strip()
        keywords = parts[1].replace("Keywords: ", "").strip()
        summary = parts[2].replace("Summary: ", "").strip()

        # Insert feedback and analysis results into the database
        conn = get_db_connection()
        conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
        conn.execute("INSERT INTO analysis (sentiment, keywords, summary) VALUES (?, ?, ?)", 
                     (sentiment, keywords, summary))
        conn.commit()
        conn.close()

        # Redirect or inform the user that feedback has been submitted
        return redirect(url_for("index", result="Thank you for your feedback!"))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
