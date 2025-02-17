from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from sentence_transformers import SentenceTransformer, util
import PyPDF2
import torch
import os

app = Flask(__name__)

# Load models
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
embedding_model = SentenceTransformer("BAAI/bge-m3")

def extract_text_from_file(file_path):
    """Extract text from a PDF or TXT file."""
    text = ""
    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        raise ValueError("Unsupported file format. Please provide a PDF or TXT file.")
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    """Handle PDF upload and process the content."""
    if 'pdf_file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['pdf_file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        # Save the uploaded PDF file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Extract text and precompute embeddings
        pdf_text = extract_text_from_file(file_path)
        pdf_content = pdf_text.split("\n\n")
        context_embeddings = embedding_model.encode(pdf_content, convert_to_tensor=True)
        
        # Store embeddings in a session or a cache for querying
        return jsonify({"message": "PDF uploaded and processed successfully!"}), 200

@app.route('/ask_question', methods=['POST'])
def ask_question():
    """Handle question queries."""
    question = request.json.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    # Retrieve the context embeddings and PDF content from session or cache
    context_embeddings = ...  # Retrieve stored embeddings from the session/cache
    
    question_embedding = embedding_model.encode(question, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(question_embedding, context_embeddings)[0]
    best_match_idx = torch.argmax(scores).item()
    best_response = pdf_content[best_match_idx]
    
    # Provide a short response
    shortened_response = ". ".join(best_response.split(". ")[:3]) + "."
    
    return jsonify({"response": shortened_response}), 200

if __name__ == '__main__':
    app.run(debug=True)
