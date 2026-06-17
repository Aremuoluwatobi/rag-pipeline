from model import client
from retrieval import retrieve_data
from fastapi import HTTPException


def ai_response(question):

    chunk_retrieval = retrieve_data(
        question=question
    )
    retrieval = "\n".join(
        f"Source: {metadata['source']}\n{chunk}"
        for chunk, metadata in chunk_retrieval
    )

    prompt = f"""
You are a helpful assistant.

Use ONLY the retrieved context.

Rules:
- Do not hallucinate.
- If the retrieved context contains enough information to answer the question, answer confidently using only the context.
- If the retrieved context does not contain enough information, say: "I am not exposed to such information."
- Match the level of detail requested by the user.
- If the user asks for a summary, keep it short.
- If the user asks for a detailed or extensive explanation, provide a detailed answer using all relevant information from the context.
- If the user does not specify a length, provide a concise answer.

Context:
{retrieval}

Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"LLM Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate response. Please try again."
        )
