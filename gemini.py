import os
import google.generativeai as genai

genai.configure(api_key = 'AIzaSyDGXS9dQQ9CW0S7SKus5aWzRKCfHCDxdJg')

from IPython.display import Markdown

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("List 5 planets each with an interesting fact")

Markdown(response.text)

print(response.text)