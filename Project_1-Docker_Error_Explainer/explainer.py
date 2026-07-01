"""
Docker Error Explainer — paste a Docker error, get a human-readable fix.
Run: python3 Project_1-Docker_Error_Explainer/explainer.py
"""

import ollama

SYSTEM_PROMPT = """
eYou are a Docker expert. You can explain things in 1-2 lines max.
You don't overthink, hallucinate or keep reasoning in a loop. 
You Reason and Act according to the user prompt.
When given a Docker error, These are the things that you can do to explain:
1. What went wrong (You tell about errors in plain English)
2. Most likely cause (You tell about the root cause)
3. How to fix it (Give solution with commands)
Keep it short.
"""



while True:
    user_input = input("Paste your Docker error (Enter exit when done):\n\n")

    if user_input == 'exit':
        break

    print("\nThinking...\n")

    response = ollama.chat(
        model="gemma4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
        options={"temperature": 0.5},
    )

    print(response["message"]["content"])
