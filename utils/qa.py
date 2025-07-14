# -*- coding: utf-8 -*-

# utils/qa.py

from transformers import pipeline

# Load question-answering pipeline once
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_questions(transcript, questions):
    """
    Given a transcript and a list of questions, return a dictionary of answers.
    """
    answers = {}
    context = transcript

    for question in questions:
        if question.strip() == "":
            continue
        result = qa_pipeline(question=question, context=context)
        answers[question] = result["answer"]

    return answers
