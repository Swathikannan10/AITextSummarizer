def summarize_text(text):
    return "This is a sample summary generated for demonstration purposes."

if __name__ == "__main__":
    input_text = """
Artificial Intelligence is the ability of machines to perform tasks
that normally require human intelligence. It includes learning,
reasoning, problem-solving, and decision-making abilities.
"""
    summary = summarize_text(input_text)
    print("SUMMARY:\n", summary)