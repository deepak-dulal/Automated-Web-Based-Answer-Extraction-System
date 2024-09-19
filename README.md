# Automated Web-Based Answer Extraction System

This project is designed to find accurate answers to user-provided questions by scraping and processing data from a list of URLs. The tool uses OpenAI for natural language processing and FAISS for efficient vector search. It also provides the source URLs of the answers for transparency. The tool is built with Streamlit, offering an easy-to-use web interface for users to input URLs, submit queries, and get answers quickly.

## Features
- **Multiple Source Input**: You can input multiple URLs (up to 10 is preferred) from which the tool will scrape and analyze the content to find the best answer to your query.
- **Natural Language Processing**: Utilizes OpenAI’s API for advanced text comprehension and question answering.
- **Efficient Search with FAISS**: Stores and retrieves vectorized content using FAISS (Facebook AI Similarity Search), allowing for fast and efficient querying.
- **Streamlit User Interface**: A simple and interactive UI to make the process of entering URLs and queries easy.
- **Source Transparency**: Provides the sources of the information returned, ensuring that users can verify the origin of the answers.

## Libraries Used

To run this project, you need to install several Python libraries. Below is the list of required libraries:

- **Streamlit**: To build the web-based UI.
- **LangChain**: For building chains and connecting various AI modules.
- **OpenAI**: To utilize OpenAI’s language model for generating answers.
- **FAISS (faiss-cpu)**: For storing and retrieving vectorized data efficiently.
- **Unstructured**: To scrape and parse data from the provided URLs.
- **Python-Dotenv**: To manage environment variables, including your API key.

## Installation

Make sure you have Python installed on your system. If not, download and install Python from [here](https://www.python.org/downloads/).

### Step-by-Step Guide

1. **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```

2. **Create a Virtual Environment** (Optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/MacOS
    .\\env\\Scripts\\activate  # For Windows
    ```

3. **Install the Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

    If you haven't created a `requirements.txt` file yet, here’s a list of the packages you need to install individually:

    ```bash
    pip install streamlit
    pip install langchain
    pip install openai
    pip install faiss-cpu
    pip install unstructured
    pip install langchain-community
    pip install python-dotenv
    ```

4. **Set Up Your OpenAI API Key**:
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key in the `.env` file like this:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Running the Application

Once you have everything set up, follow these steps to run the project:

1. **Run Streamlit**:
    ```bash
    streamlit run app.py
    ```

2. **Provide URLs**: Input the number of URLs you want to scrape. Enter the URLs one by one in the text boxes that appear.

3. **Ask a Question**: After processing the URLs, input your question in the text box, and the system will provide an answer based on the content scraped from the URLs.

4. **View the Sources**: Along with the answer, you can see the URLs from which the tool pulled the relevant information, allowing you to verify the sources.

## Usage Example

1. Input URLs of various articles or web pages.
2. Ask a question like: "What are the benefits of AI in Transportation system?"
3. The tool will retrieve relevant information from the URLs, process it using OpenAI’s model, and return the most accurate answer along with the URLs of the sources.

## Applications

This tool can be applied in various fields, including but not limited to:

- **On-Page SEO**: Analyze competitor websites to generate optimized content for better search engine ranking.
- **Research Assistance**: Gather information from multiple sources on a topic for research purposes.
- **Knowledge Aggregation**: Summarize and compare content from various online sources to get comprehensive insights.

## Future Improvements

1. **Integration with More Data Sources**: Expand the tool to scrape data from PDF files, blogs, and other structured documents.
2. **Enhanced AI Models**: Incorporate other AI models or fine-tuned versions of OpenAI for better domain-specific answers.
3. **Cloud Storage for FAISS Index**: Move the FAISS index to a cloud-based solution for scalability.

## Contributing

Feel free to submit pull requests or report issues! Any contribution is welcome.
