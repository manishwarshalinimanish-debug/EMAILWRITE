from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# ---------- Detect Type ----------
def detect_type(topic):
    topic = topic.lower()

    if "leave" in topic:
        return "leave"
    elif "sorry" in topic or "apology" in topic:
        return "apology"
    elif "invite" in topic or "invitation" in topic or "festival" in topic or "function" in topic:
        return "invitation"
    else:
        return "general"


# ---------- Generate Email ----------
def generate_email(topic, email_type, date):

    college = "The Principal, Rathinam College"

    if email_type == "leave":
        body = (
            f"I am writing this letter to formally request leave from college regarding {topic}. "
            "This is due to unavoidable personal circumstances that require my immediate attention. "
            "I assure you that my absence will not affect my academic performance.\n\n"
            "During my leave period, I will complete all pending assignments and stay updated with classwork. "
            "I will take full responsibility for managing my studies properly.\n\n"
            "Kindly consider my request and grant me leave for the required period. "
            "I will be grateful for your understanding and support."
        )

    elif email_type == "apology":
        body = (
            f"I sincerely apologize to the college regarding {topic}. "
            "I deeply regret my mistake and take full responsibility for it.\n\n"
            "I assure you that I will not repeat such mistakes in the future and will improve my behavior.\n\n"
            "Kindly accept my apology and allow me an opportunity to correct myself."
        )

    elif email_type == "invitation":
        body = (
            f"I am pleased to inform the college regarding {topic}. "
            "This event is organized with cultural and academic importance.\n\n"
            "It aims to encourage student participation, teamwork, and talent. "
            "Your presence will make the event more successful.\n\n"
            "We kindly request your support and participation."
        )

    else:
        body = (
            f"I am writing this letter to the college regarding {topic}. "
            "I kindly request your attention and support regarding this matter.\n\n"
            "Thank you for your understanding."
        )

    email = (
        f"Date: {date}\n"
        f"Place: Coimbatore\n\n"
        f"To:\n{college}\n\n"
        f"From:\nManishwar M\nRathinam College\n\n"
        f"Subject: {topic}\n\n"
        f"Respected Sir/Madam,\n\n"
        f"{body}\n\n"
        f"Yours sincerely,\nManishwar M"
    )

    return email


# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    topic = request.form["topic"]
    date = datetime.now().strftime("%d %B %Y")

    email_type = detect_type(topic)
    email = generate_email(topic, email_type, date)

    return email   # ✅ NO <pre>, NO HTML


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
