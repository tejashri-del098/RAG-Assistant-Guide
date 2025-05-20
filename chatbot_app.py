# chatbot_app.py

import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
import re  # For calculator expression cleaning

# Load document chunks and FAISS index
with open("document_chunks.txt", "r", encoding="latin-1") as file:
    document_chunks = file.read().split("\n\n")


index = faiss.read_index("document_index.faiss")
model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')


# Function to encode and retrieve relevant chunks
def retrieve_relevant_chunks(query, top_k=3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    return [document_chunks[i] for i in indices[0]]

# Function to get answer from Gemini API
def get_answer_from_gemini(query, context_chunks, api_key):
    context = "\n".join(context_chunks)
    prompt = f"Answer the following question based on the context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"Parsing error: {e}"
    else:
        return f"Error: {response.status_code} - {response.text}"

# 🧮 CALCULATOR: Evaluates safe math expressions
def handle_calculator(query):
    try:
        safe_expr = re.sub(r"[^0-9+\-*/(). ]", "", query)
        result = eval(safe_expr)
        return f"🧮 Result: {result}"
    except:
        return "⚠️ I couldn't calculate that. Please try a valid math expression like 5 + 4 * 2."

# 📖 DICTIONARY: Fetches meaning of a word using Free Dictionary API
def handle_dictionary(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        example = data[0]["meanings"][0]["definitions"][0].get("example", "No example available.")
        return f"📖 Meaning: {meaning}\n📌 Example: {example}"
    else:
        return "❌ Word not found. Please check spelling or try another word."



# Streamlit UI
st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("💬 RAG Chatbot with Gemini + FAISS")
st.markdown("Ask a question about the company, smartwatch, or smartphone documents.")

# 🧠 INTENT DETECTOR: Checks if user wants calculator, dictionary, or RAG
def detect_intent(q):
    if any(op in q for op in ["+", "-", "*", "/", "add", "subtract", "multiply", "divide"]):
        return "calculator"
    elif "define" in q.lower() or "meaning of" in q.lower():
        return "dictionary"
    return "chatbot"


# Input API key securely
api_key = st.text_input("🔑 Enter your Gemini API key", type="password")

# Chat input
query = st.text_input("📝 Ask your question here:")

if query and api_key:
    with st.spinner("Processing..."):
        intent = detect_intent(query)

        if intent == "calculator":
            result = handle_calculator(query)
            st.success(result)

        elif intent == "dictionary":
            word = query.lower().replace("define", "").replace("meaning of", "").strip()
            result = handle_dictionary(word)
            st.info(result)

        else:
            context_chunks = retrieve_relevant_chunks(query)
            st.markdown("### 🔍 Top Relevant Chunks:")
            for chunk in context_chunks:
                st.info(chunk)
            answer = get_answer_from_gemini(query, context_chunks, api_key)
            st.markdown("### 🤖 Answer:")
            st.success(answer)

