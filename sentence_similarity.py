from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from sklearn.metrics.pairwise import cosine_similarity
from flask_ngrok import run_with_ngrok


parser = reqparse.RequestParser()

app = Flask(__name__)
api = Api(app)
run_with_ngrok(app)

@app.route('/')
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def compare_sentences(sentence1, sentence2):
    
    sentences = [sentence1, sentence2]
 
    # Load model from HuggingFace Hub
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
    model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
   
    # Tokenize sentences
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
   
    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)
    
    # Perform pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    
    # Normalize embeddings
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
    # Let's calculate cosine similarity for sentence 0:
    # convert from PyTorch tensor to numpy array
    mean_pooled = sentence_embeddings.detach().numpy()
    # calculate
    similarity = cosine_similarity(
        [mean_pooled[0]],
        mean_pooled[1:]
    )
    return similarity[0].tolist()

class SimilarityEstimationEndpoint(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        try:
            sentence1 = json_data['sentence1']
            sentence2 = json_data['sentence2']
        except KeyError:
            return jsonify({'error': 'Please make sure both sentences are included in the request'})

        similarity_score = compare_sentences(sentence1, sentence2)
        result = {'similarity_score': similarity_score}
        #sentences = [sentence1, sentence2]
        return result
        #return sentences


@app.errorhandler(404)
def page_not_found(err):
    return "page not found"


@app.errorhandler(500)
def raise_error(error):
    return error

api.add_resource(SimilarityEstimationEndpoint, '/similarity_score')

if __name__ == '__main__':
    app.run()
