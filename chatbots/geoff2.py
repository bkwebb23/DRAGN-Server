from chatbots.Chatbot import Chatbot
from transformers import pipeline
import json
import os

class geoff2(Chatbot):
    def __init__(self):
        print(os.listdir())
        self.generator = pipeline('text-generation',model='./chatbots/gpt2-untemplated-quests', tokenizer='gpt2',config={'max_length':30})
        self.response = None
    def send_message(self):
        print('Sending message...')
        return {"text": self.generate(self.response)}
    def recv_message(self, message):
        self.response = message
        return super().recv_message(message)
    def generate(self, input):
        return self.generator(input)[0]['generated_text']
