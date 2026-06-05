from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    topic = request.form["topic"]

    current_date = datetime.now().strftime("%d %B %Y")

    email = f"""
Date: {current_date}
Place: Coimbatore

From:
Manishwar M
Rathinam College

To:
The Principal
Rathinam College
Coimbatore

Subject: Request for {topic}

Respected Sir/Madam,

I hope you are doing well. I am writing this email to request leave regarding {topic}.

I kindly request permission to be absent and assure you that I will complete all pending academic work after returning.

I would be grateful if you could approve my request.

Thank you for your time and consideration.

Yours sincerely,

Manishwar M
II B.Sc CS (AI)
Rathinam College
"""

    return f"<pre>{email}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
