import google.generativeai as genai

genai.configure(api_key="AIzaSyC8L1t_zZU-fQU3XFsaWGPOX1ZhJokwpz8")

models = genai.list_models()
for m in models:
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
