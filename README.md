
# 🤖 RAG Assistant Chatbot with Gemini + FAISS

A powerful Retrieval-Augmented Generation (RAG) Chatbot built using **Gemini 1.5 API**, **FAISS vector search**, and a **Streamlit web interface**. This intelligent assistant allows users to ask context-based questions over multiple documents like company profiles, smartwatches, and smartphones — delivering accurate, human-like answers using the latest LLM technology.

---

## 🚀 Project Demo

> 🧠 Ask any question like:
> - *"What services do we offer?"*
> - *"What are the features of the smartwatch?"*
> - *"What are the technical specs of the smartphone?"*

> 🎯 And get instant, relevant, AI-generated answers from embedded document knowledge!

---

## 💡 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that enhances the performance of Large Language Models by:
1. **Retrieving** the most relevant context chunks from a local document store using vector similarity (FAISS).
2. **Augmenting** the query with these chunks.
3. **Generating** an answer using an LLM (Gemini in this case).

This ensures:
- **High factual accuracy**
- **Up-to-date information**
- **Explainable, document-grounded responses**

---

## 🛠️ Tech Stack

| Component            | Description                                      |
|----------------------|--------------------------------------------------|
| `Streamlit`          | Clean and responsive web UI                     |
| `Gemini 1.5 API`     | Google’s advanced generative language model     |
| `FAISS`              | Efficient vector similarity search               |
| `SentenceTransformers` | Converts text into semantic embeddings        |
| `Python`             | Core logic and orchestration                    |

---

## 📂 Project Structure

```
RAG-Assistant-Guide/
├── document_preprocessing.py   # Splits documents and creates FAISS index
├── chatbot_app.py              # ✅ Main Streamlit chatbot app
├── main_app.py                 # (Optional) CLI version
├── document_chunks.txt         # Text chunks extracted from docs
├── document_index.faiss        # FAISS vector index
├── requirements.txt            # Python dependencies
└── README.md                   # This file!
```

---

## 🔑 Features

✅ Ask contextual questions based on embedded document knowledge  
✅ Uses RAG pipeline for better accuracy  
✅ Secure Gemini API integration  
✅ Beautiful Streamlit interface  
✅ Highly modular & scalable  

---

## 📦 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/RAG-Assistant-Guide.git
cd RAG-Assistant-Guide
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare Documents
Make sure `document_chunks.txt` and `document_index.faiss` are present. If not, run:
```bash
python document_preprocessing.py
```

### 4. Launch the Chatbot
```bash
streamlit run chatbot_app.py
```

---

## 🔐 Gemini API Setup

> 💡 You need an API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

Paste it into the input field when launching the chatbot.

---

## 📈 Use Cases

- 📄 Internal company knowledgebase assistant  
- 🛒 Product comparison & FAQ bot  
- 🧠 Educational assistant for study material  
- 🧑‍💼 Resume or portfolio Q&A bot  

---

## 🚀 Future Enhancements

- ✅ Document upload feature  
- 💬 Chat history with memory  
- 🔍 Advanced filterable document categories  
- 🧾 PDF, Excel, and Webpage ingestion  

---

## 👨‍💻 Author

**Tejashree Choudhary**  
3rd-year B.Tech AI/ML student at VIT Bhopal  
Passionate about solving real-world problems with AI 🤖

---

## ⭐️ Show Your Support!

If you like this project:
- 🌟 Star the repo
- 🍴 Fork it
- 📢 Share with others
- 💬 Submit feedback or improvements

---

