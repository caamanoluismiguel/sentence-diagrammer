from flask import Flask, request, jsonify, send_from_directory
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__, static_folder="static")

@app.route('/parse', methods=['POST'])
def parse_sentence():
    data = request.get_json()
    sentence = data.get("sentence", "")
    doc = nlp(sentence)
    tokens = []
    for token in doc:
        tokens.append({
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "head": token.head.text
        })
    return jsonify(tokens)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
