import streamlit as st  
import requests  
import json  

# Set up Groq API key  
GROQ_API_KEY = "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"  
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  

# Function to translate using Groq API directly  
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

# Streamlit UI  
st.title("🌍 Multilingual Translator with Groq")  
st.markdown("Translate text from one language to another using the Groq API.")  

# Input fields  
source_lang = st.text_input("Enter the source language")  
target_lang = st.text_input("Enter the target language")  
text = st.text_area("Enter the text to translate")  

if st.button("Translate"):  
    if source_lang and target_lang and text:  
        try:  
            with st.spinner("Translating..."):  
                translated_text = translate_with_groq(text, source_lang, target_lang)  
            st.success("Translation successful!")  
            st.markdown(f"**Translation ({source_lang} → {target_lang}):**")  
            st.write(translated_text)  
        except Exception as e:  
            st.error(f"Error: {e}")  
    else:  
        st.warning("Please fill in all fields.")  

# Run the Streamlit app using:  
# ```  
# streamlit run streamlit_app.py  
# ```  
