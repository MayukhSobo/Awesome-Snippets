import pandas as pd
import numpy as np
import tensorflow as tf
import transformers
import re

class TEmbedding:
    # Refer: https://huggingface.co/transformers/pretrained_models.html
    allowed_models = [
        'bert-base-uncased',
        'bert-large-uncased',
        'bert-base-cased',
        'bert-large-cased',
        'gpt2',
        'gpt2-medium',
        'gpt2-large',  # Use it with caution
        'gpt2-xl',     # Use it with caution
        'roberta-base',
        'roberta-large',
        'distilbert-base-uncased',
        'distilbert-base-cased',
        'albert-base-v2',
        'albert-large-v2',
        'albert-xlarge-v2'
    ]
    def __init__(self, model, backend):
        self.ids = None
        if model not in TEmbedding.allowed_models:
            raise NotImplementedError(f'The given model {model} is not supported!!')
        else:
            if re.match(r'^bert-.*', model):
                from transformers import BertTokenizer, TFBertModel
                self._tokenizer = BertTokenizer.from_pretrained(model)
                self.transformer = TFBertModel.from_pretrained(model)
            elif re.match(r'^gpt2.*', model):
                from transformers import GPT2Tokenizer, TFGPT2Model
                self._tokenizer = GPT2Tokenizer.from_pretrained(model)
                self.transformer = TFGPT2Model.from_pretrained(model)
            elif re.match(r'^distilbert-.*', model):
                from transformers import DistilBertTokenizer, TFDistilBertModel
                self._tokenizer = DistilBertTokenizer.from_pretrained(model)
                self.transformer = TFDistilBertModel.from_pretrained(model)
            elif re.match(r'^roberta-.*', model):
                from transformers import RobertaTokenizer, TFRobertaModel
                self._tokenizer = RobertaTokenizer.from_pretrained(model)
                self.transformer = TFRobertaModel.from_pretrained(model)
            elif re.match(r'^albert-.*', model):
                from transformers import AlbertTokenizer, TFAlbertModel
                self._tokenizer = AlbertTokenizer.from_pretrained(model)
                self.transformer = TFAlbertModel.from_pretrained(model)
        self.backend = backend
        
    def get_embedding(self, text, device):
        if self.backend.lower() == 'tensorflow':
            self.ids = self.tokenizer.encode(text)
            input_ = tf.constant(self.ids)[None, :]
            return self.transformer(input_)
    
    def sent2vec(self, text, criteria='avg', device='cpu'):
        em = self.get_embedding(text, device)[0]
        em = em.numpy()
        n = em.shape[1] - 1
        if criteria.lower() == 'avg':
            # Remove the embedding for the tokens [CLS] [SEP]
            em = em[:, 1:n, :].squeeze(axis=0)
            return np.mean(em, axis=0)
        else:
            raise NotImplementedError(f'Criteria: {criteria} is not implemented!!')
        
    @property
    def tokenizer(self):
        return self._tokenizer
    
    @property
    def token_ids(self):
        return self.ids


if __name__ == '__main__':
    text = "Hello, my dog is so cute!"
    te = TEmbedding(model='distilbert-base-uncased', backend='tensorflow')
    a = te.sent2vec('Hello, my dog is very cute!')
    print(a.shape)