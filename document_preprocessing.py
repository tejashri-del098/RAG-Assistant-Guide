# document_preprocessing.py

# Prepare your document chunks
document_chunks = [
    # Company FAQ Document
    "1. What is our company’s mission? Our mission is to provide innovative software solutions to businesses around the world, empowering them to solve complex problems and streamline operations.",
    "2. What services do we offer? We offer a variety of services, including custom software development, cloud-based solutions, and IT consultancy. Our services are tailored to meet the needs of different industries, including healthcare, finance, and education.",
    "3. How can I contact support? You can contact our support team through email at support@company.com or call us at 123-456-7890.",
    "4. What are our working hours? Our office hours are Monday through Friday, from 9:00 AM to 6:00 PM. Our support team is available 24/7 via email.",
    "5. Do we offer any training or tutorials? Yes, we provide online tutorials and training sessions for our software. You can sign up on our website to access these resources.",
    
    # Product Specification Document
    "1. Display: The XYZ Smartwatch features a 1.5-inch OLED display with a resolution of 400 x 400 pixels. It offers vibrant colors and is easily readable in both indoor and outdoor lighting.",
    "2. Battery Life: The smartwatch has a battery life of up to 48 hours on a single charge, depending on usage. It supports fast charging, providing 80% charge in just 30 minutes.",
    "3. Compatibility: The XYZ Smartwatch is compatible with both iOS and Android devices. It connects seamlessly via Bluetooth 5.0.",
    "4. Sensors: The watch includes sensors for heart rate monitoring, sleep tracking, GPS, and activity tracking. It also features a blood oxygen level sensor.",
    "5. Water Resistance: The XYZ Smartwatch has a water resistance rating of 5ATM, making it suitable for swimming and use in wet conditions.",
    
    # Product Feature Document
    "1. Camera: The ABC Smartphone comes with a dual-camera setup: a 12MP primary camera and a 16MP ultra-wide lens. It supports 4K video recording and features advanced AI-based photo enhancements.",
    "2. Processor: Powered by the latest Snapdragon 888 chipset, the ABC Smartphone offers lightning-fast performance and can handle multitasking with ease. It also supports 5G connectivity.",
    "3. Display: The phone features a 6.7-inch AMOLED display with a 120Hz refresh rate. The screen is protected by Corning Gorilla Glass 6, making it more durable.",
    "4. Storage: The smartphone comes with 128GB of internal storage and is expandable via a microSD card, supporting up to 1TB of additional storage.",
    "5. Operating System: The ABC Smartphone runs on Android 12 with a custom user interface, offering smooth navigation and multiple customization options."
]

# Optionally, save these chunks to a file if you want to access them later
with open("document_chunks.txt", "w") as file:
    for chunk in document_chunks:
        file.write(chunk + "\n\n")

print("Documents prepared and saved to 'document_chunks.txt'.")
# document_preprocessing.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize the model for text embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create a function to encode the text chunks into vectors
def encode_text_chunks(chunks):
    return model.encode(chunks)

# Convert the document chunks into vectors
document_vectors = encode_text_chunks(document_chunks)

# Initialize FAISS index (using L2 distance)
dimension = document_vectors.shape[1]  # Embedding dimension (size of the vector)
index = faiss.IndexFlatL2(dimension)

# Add the vectors to the FAISS index
index.add(np.array(document_vectors))

# Save the index (optional, for later use)
faiss.write_index(index, "document_index.faiss")

print("FAISS index created and saved.")

# Function to retrieve top 3 relevant document chunks based on query
def retrieve_relevant_chunks(query, top_k=3):
    # Encode the query into a vector
    query_vector = model.encode([query])
    
    # Search the FAISS index to get the top k results
    distances, indices = index.search(np.array(query_vector), top_k)
    
    # Return the retrieved document chunks
    retrieved_chunks = [document_chunks[i] for i in indices[0]]
    return retrieved_chunks

# Test the retrieval function (optional, you can test with your own queries)
test_query = "What services do we offer?"
retrieved_chunks = retrieve_relevant_chunks(test_query)

print("Retrieved Chunks for query:", test_query)
for chunk in retrieved_chunks:
    print(chunk)



import requests

def get_answer_from_gemini(query, context_chunks, api_key):
    context = "\n".join(context_chunks)
    prompt = f"Answer the following question based on the context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            print("Parsing error:", e)
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
