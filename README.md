# MedBot - PDF-based Question Answering System

MedBot is a simple conversational chatbot designed to answer user queries based on the contents of uploaded PDF or text files. The bot uses natural language processing (NLP) techniques and pre-trained transformer models to understand user questions and provide contextually relevant answers from the documents.

## Features:
- **PDF and TXT File Upload**: Upload health-related documents (PDF or text) for processing.
- **Question Answering**: After uploading the document, users can ask questions, and the bot will provide answers based on the document content.
- **Shortened Answers**: The bot returns concise, shortened versions of the most relevant sections from the document.
- **Model**: Uses the BGE-M3 model from Sentence-Transformers for embedding-based semantic search and question answering.
- **Real-time Querying**: Users can submit queries and get instant responses.

## How It Works:
1. **PDF/Text Upload**: Users upload a PDF or text document containing health-related information.
2. **Text Extraction**: The bot extracts text from the uploaded document and splits it into sections (paragraphs).
3. **Embedding Calculation**: The document text is encoded into embeddings using the BGE-M3 model.
4. **Question Handling**: Users input questions, and the bot matches them with the most relevant sections of the document using cosine similarity between the question's and document embeddings.
5. **Response**: The bot returns a short, relevant response based on the document sections.

## Technologies Used:
- **Flask**: A lightweight web framework for building the application.
- **Transformers**: For handling tokenization and question answering with pre-trained models.
- **Sentence-Transformers**: Used for generating document and query embeddings.
- **PyPDF2**: To extract text from PDF documents.
- **Torch**: For tensor manipulation and similarity calculation.

## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/ali713111/med_bot_Q&A.git
