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
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, and provide a summary."},
                {"role": "user", "content": feedback_content}
            ]
        )

        # Assuming the response is structured as expected, directly extracting it
        analysis_result = response.choices[0].message.content

        conn = get_db_connection()
        # Insert feedback content and analysis result into the database
        conn.execute("INSERT INTO feedback (content) VALUES (?)", (feedback_content,))
        feedback_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.execute("INSERT INTO analysis (feedback_id, result) VALUES (?, ?)", (feedback_id, analysis_result))
        conn.commit()
        conn.close()

        # Thank the student and show a message or redirect
        return redirect(url_for("index", result="Thank you for your feedback!"))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
