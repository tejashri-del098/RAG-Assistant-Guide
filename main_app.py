import os
from document_preprocessing import retrieve_relevant_chunks, get_answer_from_gemini

# 🔐 Your API Key (use environment variable in production)
API_KEY = "AIzaSyAkJNX3Wa6e3Aw24wHHC2rdWM8mathzQ6o"  # Replace with actual key

def main():
    print("Welcome to your RAG Assistant! Ask your question below.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # Step 1: Get top 3 relevant chunks
        chunks = retrieve_relevant_chunks(query)

        # Step 2: Get Gemini's answer
        answer = get_answer_from_gemini(query, chunks, API_KEY)

        # Step 3: Show the answer
        print("\n🤖 Gemini Answer:")
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()
