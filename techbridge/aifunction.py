import google.generativeai as genai
from datetime import datetime
import os
from .local_settings import API_KEY

# Cấu hình API với khóa API của bạn
genai.configure(api_key=API_KEY)

# Tạo một đối tượng model từ Gemini
model = genai.GenerativeModel('gemini-1.5-flash')


def word_explanation(paragraph,language):
    PROMPT = f"""
    Please detect IT professional vocabulary from the follwing conversation and write the explanations of the each vocabs. 
    Do not include words that can be considered It professional vocabs but are used within non It professional people. 
    Only detect vocabs higher than IT Skills Standard level 3.
    Don't say anything about hwy you chose that words and what words you chose.
    Write the reply in {language} language
    "{paragraph}"
    """
    
    # Gọi API để tóm tắt văn bản
    response = model.generate_content(PROMPT)
    
    # Trả về kết quả tóm tắt
    return response.text.strip()
