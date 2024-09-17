#!/usr/bin/env python
# coding: utf-8

"""Hello, thank you for checking out this code!
This code is designed to help you find answers quickly and easily by pulling information directly from multiple websites.
Instead of manually visiting each site and copying content, this tool automatically gathers the data from URLs you provide and processes it to generate relevant answers.
Whether you need information from a specific source or want to compare answers from several sites, this tool simplifies the process and saves you time.
You can also use it with text files for more flexibility!"""





# Install required libraries (uncomment the lines below if needed)
# !pip install streamlit
# !pip install langchain
# !pip install openai
# !pip install faiss-cpu
# !pip install unstructured
# !pip install langchain-community
# !pip install python-dotenv

import os
import streamlit as st
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Loading API key from the .env file
#Make Sure you have your API key on .env folder and make sure to provide the proper file path
dotenv_path = ".env"
load_dotenv(dotenv_path=dotenv_path)
open_ai_api_key = os.getenv("OPENAI_API_KEY")

# Validating if it can access API key
if not open_ai_api_key:
    st.error("The OpenAI API key couldn't be found. Please set it in the .env file.")
else:
    os.environ["OPENAI_API_KEY"] = open_ai_api_key  # Ensure the API key is available globally

# Using Streamlit for UI
st.title("Finding the Right Answer ASAP Guide")
st.sidebar.title("Please Provide the URLs")

no_of_url = st.sidebar.number_input(f"Enter the number of URLs", min_value=1, step=1, value=1, format="%d")

list_of_urls = []
for i in range(no_of_url):
    url = st.sidebar.text_input(f"URL {i + 1}", key=f"url_{i}")
    list_of_urls.append(url)

#Processing Button
users_clicked_on_process = st.sidebar.button("Process URLs")

#Saving on vector database(Providing file path)
file_path = "faiss_store"


main_placeholder = st.empty()

#Initiaition LLM Models
llm = OpenAI(temperature=0.9, max_tokens=500)

#Running the URL Loader, Embedding and Indexing if the process button clicked
if users_clicked_on_process:
    if not any(list_of_urls):
        st.error("Please enter at least 1 URL.")
    else:
        # Scraping texts from the URLS
        loader = UnstructuredURLLoader(urls=list_of_urls)
        main_placeholder.text("Loading data from URLs...⏳")
        data = loader.load()

        # Spliting text based on the differnet characters
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Splitting data...⏳")
        docs = text_splitter.split_documents(data)

        # Embeddings using OpenAI
        embeddings = OpenAIEmbeddings()
        main_placeholder.text("Building embedding vectors...⏳")
        vectorstore_open_ai = FAISS.from_documents(docs, embeddings)

        # Storing Embedded Vectorized file on fiass vector database
        vectorstore_open_ai.save_local(file_path)
        main_placeholder.success("Embedding vectors built and saved! ✅")

# Retrieving the Queries based on the data we have using llm
query = main_placeholder.text_input("Enter your question:")
if query:
    if os.path.exists(file_path):
        main_placeholder.text("Loading the FAISS index...⏳")
        vectorstore = FAISS.load_local(file_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

        # Executing the query (You )
        result = chain({"question": query}, return_only_outputs=True)
        #result ( you can print this if you want to see several answer that was generated and also see the final answer)

        # Displaying the final answer
        st.header("Answer")
        st.write(result["answer"])

        # Displaying the source on whose basis the answer is provided
        sources = result.get("sources", "")
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")

            unique_sources = set(sources.split("\n"))
            for source in unique_sources:
                st.write(sources)
        else:
            st.warning("No sources found.")