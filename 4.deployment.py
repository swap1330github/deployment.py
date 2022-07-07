#!/usr/bin/env python
# coding: utf-8

# In[70]:


# -*- coding: utf-8 -*-

#packages for run,deploy.
import pandas as pd
import numpy as np
import pipeline
import joblib
import streamlit as st

df2 = pd.read_csv("FinalTextBlobSentiment.csv")

def main():
    st.title("Sentiment Analyzer App")
    menu = ["Home","Monitor","About"]
    choice = st.sidebar.selectbox("menu",menu)
  
    
    if choice =="Home":
        st.subheader("Home-Sentiment In Text")
        
        with st.form(key='Sentiment_clf_form'):
            raw_text = st.text_area("Enter the Review")
            submit_text = st.form_submit_button(label='Submit')   
            
    if submit_text:
        col1,col2 = st.beta_columns(2)
        
        with col1:
            st.success("Original Text")
            st.write(raw_text)
            
            st.success("Sentiment")
            st.write(Sentiment_TextBlob)
            
        with col2:
            st.success("Textblob_Polarity")
            st.write(Polarity_TextBlob)
            
            Sentiment= df2.predict([var])
            print(Sentiment)

        if (Sentiment[0] == 0):
            return 'The review is Negative'
        else:
            return 'The review is Positive'
  
            
   


# In[ ]:




