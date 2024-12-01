#!/usr/bin/env python
import sys
from teach.crew import TeachCrew
from datetime import datetime
# import streamlit as st

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
# st.title("CreWAI Output Viewer")
# task_input = st.text_input(inputs)
def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'builtin led turnon and turnoff using accelleration minimum delay 100 milliseconds'
    }

    result = TeachCrew().crew().kickoff(inputs=inputs)
    result.tasks_output[0]


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TeachCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TeachCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TeachCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
