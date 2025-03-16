import streamlit as st  
import requests  
import json  


GROQ_API_KEY = "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"  
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  


st.markdown("""  
    <style>  
        body {  
            background-color: #f4f4f9;  
            font-family: 'Arial', sans-serif;  
        }  
        .title {  
            color: #4CAF50;  
            text-align: center;  
            font-size: 36px;  
            font-weight: bold;  
            margin-bottom: 10px;  
        }  
        .subtitle {  
            color: #555;  
            text-align: center;  
            font-size: 18px;  
            margin-bottom: 30px;  
        }  
        .stTextInput>div>div>input {  
            border: 2px solid #4CAF50 !important;  
            border-radius: 10px;  
            padding: 10px;  
            font-size: 16px;  
            color: #333;  
            background-color: #fafafa;  
        }  
        .stTextArea>div>textarea {  
            border: 2px solid #4CAF50 !important;  
            border-radius: 10px;  
            padding: 10px;  
            font-size: 16px;  
            color: #333;  
            background-color: #fafafa;  
        }  
        .stButton>button {  
            background-color: #4CAF50 !important;  
            color: white !important;  
            font-size: 18px;  
            border-radius: 10px;  
            padding: 10px 20px;  
            border: none;  
            cursor: pointer;  
            transition: background-color 0.3s ease;  
        }  
        .stButton>button:hover {  
            background-color: #45a049 !important;  
        }  
        .result-box {  
            border: 2px solid #4CAF50;  
            padding: 15px;  
            border-radius: 10px;  
            background-color: #f0fff0;  
            color: #333;  
            font-size: 16px;  
            margin-top: 20px;  
            overflow-wrap: break-word;  
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);  
        }  
    </style>  
""", unsafe_allow_html=True)  


def translate_with_groq(text, source_lang, target_lang):  
    headers = {  
        "Authorization": f"Bearer {GROQ_API_KEY}",  
        "Content-Type": "application/json"  
    }  

    data = {  
        "model": "llama-3.3-70b-versatile",  
        "messages": [  
            {"role": "system", "content": "You are a helpful language translation assistant."},  
            {"role": "user", "content": f"Translate the following text from {source_lang} to {target_lang}:\n\n{text}"}  
        ],  
        "temperature": 0.7  
    }  

    response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(data))  

    if response.status_code == 200:  
        result = response.json()  
        translated_text = result['choices'][0]['message']['content']  
        return translated_text  
    else:  
        raise Exception(f"Groq API Error: {response.status_code}, {response.text}")  


st.markdown("<div class='title'>🌍 Multilingual Translator</div>", unsafe_allow_html=True)  
st.markdown("<div class='subtitle'>🗣️ Break language barriers – Communicate effortlessly across the globe!</div>", unsafe_allow_html=True)  


source_lang = st.text_input("Enter the source language")  
target_lang = st.text_input("Enter the target language")  
text = st.text_area("Enter the text to translate")  


if st.button("Translate"):  
    if source_lang and target_lang and text:  
        try:  
            with st.spinner("Translating..."):  
                translated_text = translate_with_groq(text, source_lang, target_lang)  
            st.success("✅ Translation successful!")  

          
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)  
            st.markdown(f"**Translation ({source_lang} → {target_lang}):**")  
            st.write(translated_text)  
            st.markdown("</div>", unsafe_allow_html=True)  

        except Exception as e:  
            st.error(f"❌ Error: {e}")  
    else:  
        st.warning("⚠️ Please fill in all fields.")  


