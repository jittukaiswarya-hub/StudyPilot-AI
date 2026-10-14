
import streamlit as st
from study_agent import (
    create_study_plan,
    explain_topic,
    generate_notes,
    generate_flashcards,
    generate_quiz,
    generate_daily_recap,
)

st.set_page_config(
    page_title="StudyPilot AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyPilot AI")
st.write("Your personal AI-powered learning companion.")

with st.sidebar:
    st.header("🎯 Your Learning Profile")
    name = st.text_input("Your name", placeholder="Enter your name")
    subject = st.selectbox(
        "Choose a subject",
        [
            "Python",
            "Java",
            "C Programming",
            "Data Structures",
            "Computer Networks",
        ],
    )
    level = st.selectbox(
        "Your level",
        ["Beginner", "Intermediate", "Advanced"],
    )
    st.caption("Learn • Practice • Revise • Improve")

topic = st.text_input(
    "📖 What topic do you want to learn?",
    placeholder="Example: Python loops, Java OOP, AVL trees",
)

if topic.strip():
    st.subheader(f"Let's learn {topic}!")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🗺️ Study Plan",
            "💡 Explanation",
            "📝 Revision Notes",
            "🃏 Flashcards",
            "🧠 Quiz",
            "📅 Daily Recap",
        ]
    )

    with tab1:
        if st.button("Create my study plan", key="plan"):
            with st.spinner("Creating your personalized study plan..."):
                st.session_state["study_plan"] = create_study_plan(
                    topic, subject, level
                )
        if "study_plan" in st.session_state:
            st.markdown(st.session_state["study_plan"])

    with tab2:
        if st.button("Explain this topic", key="explain"):
            with st.spinner("Your AI tutor is preparing an explanation..."):
                st.session_state["explanation"] = explain_topic(
                    topic, subject, level
                )
        if "explanation" in st.session_state:
            st.markdown(st.session_state["explanation"])

    with tab3:
        if st.button("Generate revision notes", key="notes"):
            with st.spinner("Preparing revision notes..."):
                st.session_state["notes"] = generate_notes(topic, subject)
        if "notes" in st.session_state:
            st.markdown(st.session_state["notes"])

    with tab4:
        if st.button("Create flashcards", key="flashcards"):
            with st.spinner("Creating flashcards..."):
                st.session_state["flashcards"] = generate_flashcards(
                    topic, subject
                )
        if "flashcards" in st.session_state:
            st.markdown(st.session_state["flashcards"])

    with tab5:
        if st.button("Generate quiz", key="quiz"):
            with st.spinner("Writing your quiz questions..."):
                st.session_state["quiz"] = generate_quiz(topic, subject)
        if "quiz" in st.session_state:
            st.markdown(st.session_state["quiz"])

    with tab6:
        st.write("Record what you studied today and what remains.")
        learned = st.text_area(
            "What did you learn?",
            placeholder="Example: Variables and data types",
        )
        remaining = st.text_area(
            "What do you still need to learn?",
            placeholder="Example: Loops and functions",
        )
        if st.button("Create daily recap", key="recap"):
            with st.spinner("Preparing your daily recap..."):
                st.session_state["recap"] = generate_daily_recap(
                    learned or "No topics recorded",
                    remaining or "Not specified",
                )
        if "recap" in st.session_state:
            st.markdown(st.session_state["recap"])

else:
    st.info("👆 Enter a topic above to start learning.")

st.divider()
st.caption("StudyPilot AI | Learn at your own pace 💙")
