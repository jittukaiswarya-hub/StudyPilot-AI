

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openrouter/free"


def ask_ai(prompt):
    if not API_KEY:
        return "API key not found. Check your .env file."

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are StudyPilot AI, a friendly tutor. "
                    "Teach college students in simple English, "
                    "step by step, with examples."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60,
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as error:
        details = error.response.text if error.response is not None else str(error)
        return f"AI connection error: {details}"

    except (KeyError, IndexError, ValueError):
        return "The AI returned an unexpected response. Please try again."


def create_study_plan(topic, subject, level):
    return ask_ai(
        f"Create a complete study plan for {topic} in {subject} "
        f"for a {level} student. Include objectives, prerequisites, "
        "ordered concepts, examples, exercises, and revision steps."
    )


def explain_topic(topic, subject, level):
    return ask_ai(
        f"Explain {topic} in {subject} to a {level} student. "
        "Include a definition, step-by-step explanation, real-world "
        "analogy, examples, common mistakes, and summary."
    )


def generate_notes(topic, subject):
    return ask_ai(
        f"Create concise revision notes for {topic} in {subject}. "
        "Include definitions, key points, and examples."
    )


def generate_flashcards(topic, subject):
    return ask_ai(
        f"Create 8 flashcards for {topic} in {subject}. "
        "Format each as Question and Answer."
    )


def generate_quiz(topic, subject):
    return ask_ai(
        f"Create 5 multiple-choice questions about {topic} in "
        f"{subject}. Give four options, the correct answer, "
        "and a short explanation for each question."
    )


def generate_daily_recap(learned_topics, remaining_topics):
    return ask_ai(
        f"Create a daily study recap.\n"
        f"Topics learned: {learned_topics}\n"
        f"Topics remaining: {remaining_topics}\n"
        "Summarize progress and recommend the next steps."
    )
