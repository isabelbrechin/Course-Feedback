import os
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_compassionate_response():
    # Function to generate a compassionate thank you message using GPT-3.5
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        prompt="Generate a compassionate thank you message for a student who has just submitted course feedback.",
        temperature=0.7,
        max_tokens=60,
    )
    return response.choices[0].text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    compassionate_response = ""
    if request.method == "POST":
        feedback_content = request.form.get("feedback", "")

        # Using 'messages' for a chat completion task with OpenAI for analysis
        analysis_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=60,
            messages=[
                {"role": "system", "content": "Analyze this student feedback for sentiment, extract keywords, and provide a summary. Please format your response with 'Sentiment:', followed by 'Keywords:', and end with 'Summary:'."},
                {"role": "user", "content": feedback_content}
            ]
        )

        # Correctly parsing the structured response from OpenAI
        # Assuming the response is a single string with new lines separating sentiment, keywords, and summary
        analysis_result = analysis_response.choices[0].message.content  # Accessing the content attribute directly
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

        compassionate_response = generate_compassionate_response()
        # Return template with compassionate response after POST request
        return render_template("index.html", compassionate_response=compassionate_response)
    
    # Redirect or render template without compassionate response for GET request
    return render_template("index.html", compassionate_response=compassionate_response)

if __name__ == "__main__":
    app.run(debug=True)
