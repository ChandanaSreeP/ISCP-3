'''
Create an webservice using chatgpt API.

1) you must be able to have a conversation

2) When you exit the program, it should automatically store the conversation as a json file
'''

import openai
import gradio as gr
import json

openai.api_key = "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"

Chat_History = []

name_of_file="chatBot_History.json"

def make_request(input):
    if input:
        Chat_History.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=Chat_History
        )
        reply = chat.choices[0].message.content
        Chat_History.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

result=gr.Interface(fn=make_request, inputs=inputs, outputs=outputs,title="AI ChatBot")
result.launch(share=True)

with open(name_of_file,"w") as file:
    json.dump(Chat_History,file)