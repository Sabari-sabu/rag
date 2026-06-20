import os
from openai import OpenAI
from config import Config
from dotenv import load_dotenv

load_dotenv()

# OpenRouter uses the OpenAI-compatible API format
client = OpenAI(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Model available on the current OpenRouter account
OPENROUTER_MODEL = "anthropic/claude-3-haiku"

def get_embedding(text):
    """Get embedding for text using keyword extraction."""
    # Simple keyword extraction for chunk matching
    return text.lower().split()[:50]

def find_relevant_chunks(query, chunks, top_k=3):
    """Find most relevant chunks for a query using keyword similarity."""
    query_words = set(query.lower().split())

    scored_chunks = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        # Simple similarity: intersection of words
        similarity = len(query_words & chunk_words) / (len(query_words | chunk_words) + 1)
        scored_chunks.append((chunk, similarity))

    # Sort by similarity and return top_k
    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    return [chunk for chunk, _ in scored_chunks[:top_k]]

def answer_question(query, context_chunks):
    """Generate answer using Claude via OpenRouter with context."""
    context = "\n---\n".join(context_chunks)

    system_prompt = (
        "You are a helpful assistant that answers questions based on provided document context. "
        "If the answer is not in the context, say 'I cannot find this information in the provided documents.' "
        "Be concise and accurate."
    )

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": (
                    f"Context from documents:\n{context}\n\n"
                    f"Question: {query}\n\n"
                    "Please answer based on the context provided."
                ),
            },
        ],
    )

    return response.choices[0].message.content or "No response generated"
