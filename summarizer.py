import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    prompt = "Summarize the following text in simple and clear language suitable for students:\n" + text
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    
    return response.output_text

if __name__ == "__main__":
    input_text = """
Artificial Intelligence is the ability of machines to perform tasks
that normally require human intelligence. It includes learning,
reasoning, problem-solving, and decision-making abilities.
"""
    summary = summarize_text(input_text)
    print("SUMMARY:\n", summary)