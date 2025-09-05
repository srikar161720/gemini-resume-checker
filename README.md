> DevNetwork [API + Cloud + Data] Hackathon 2025\
> Team: <a href="https://www.linkedin.com/in/srikar-pottabathula/" target="_blank">Srikar Pottabathula</a>
# 👔 Resume Matcher

An AI-powered agent that analyzes your resume against a job description to provide a detailed match report, helping you tailor your application and land more interviews.

This application uses Google's Gemini 2.5 Flash model via LangChain to act as an expert career coach. It parses your resume, compares it to a job's requirements, and generates a report with a match score, keyword analysis, and actionable suggestions for improvement.

---

## ✨ Features

* **PDF & TXT Parsing:** Upload your resume in either `.pdf` or `.txt` format.
* **AI-Powered Analysis:** Leverages the power of Google's Gemini model for nuanced understanding of your skills and experience.
* **Detailed Match Report:** Get a comprehensive analysis including:
    * A percentage match score.
    * Matched and missing keywords.
    * Actionable advice to improve your resume.
* **Interactive Web UI:** A clean and simple user interface built with Streamlit.

---

## 🛠️ Tech Stack

* **Backend:** Python
* **AI Framework:** LangChain
* **LLM:** Google Gemini 2.5 Flash
* **Frontend:** Streamlit
* **Document Parsing:** PyMuPDF (`fitz`)

---

## ⚙️ Setup and Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* Python 3.9 or higher
* Git

### Step 1: Clone the Repository

First, clone the project repository to your local machine.

```bash
git clone [https://github.com/your-username/gemini-resume-matcher.git](https://github.com/your-username/gemini-resume-matcher.git)
cd gemini-resume-matcher
```

### Step 2: Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

* **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### Step 3: Install Dependencies

Install all the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Your API Key

This project requires an API key from Google AI Studio to use the Gemini model.

1.  **Obtain your API key:** Visit [Google AI Studio](https://aistudio.google.com/) and create your free API key.
2.  **Create a `.env` file:** In the root directory of the project, create a new file named `.env`.
3.  **Add your key:** Inside the `.env` file, add your API key in the following format:

    ```
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
    ```

    *The `.gitignore` file is already configured to prevent this file from being committed to your repository.*

If you would like to change/modify the model being used in the backend, see [Using a Different LLM](#using-a-different-llm).

### Step 5: Run the Application

You are now ready to run the Streamlit application!

```bash
streamlit run app.py
```

A new tab should open in your browser at `http://localhost:8501` with the running application.

---

## 🔧 Customization

This project is built with customization in mind, thanks to LangChain's modularity.

### Using a Different LLM

If you want to use a different Large Language Model (e.g., from OpenAI, Anthropic, or Hugging Face), you can easily swap it out.

1.  Install the required library (e.g., `pip install langchain-openai`).
2.  In `app.py`, find this line:
    ```python
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    ```
3.  Replace it with your chosen LLM. For example, to use OpenAI's GPT-4:
    ```python
    # from langchain_openai import ChatOpenAI
    # llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    ```

### Modifying the AI's Behavior

The behavior, personality, and output format of the AI agent are controlled by the prompt template. You can modify it to suit your needs by editing the `prompt_template_string` variable in `app.py`.
