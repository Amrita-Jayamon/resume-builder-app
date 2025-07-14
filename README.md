# resume-builder-app
# AI-Powered Resume Builder 🧠📄

This is a web-based resume generator built with [Streamlit](https://streamlit.io/) that uses AI to help you write professional, ATS-friendly resumes.

Powered by OpenRouter's free GPT-like models such as Mixtral and LLaMA.

---

## 🔧 Features

- AI-generated resumes with minimal input
- Clean PDF download with one click
- Secure API key handling via Streamlit Secrets
- Deployed publicly on Streamlit Cloud (no setup needed!)

---

## 🚀 Live Demo

👉 [Click here to try it out!](https://your-username.streamlit.app)

---

## 🛠 How to Run It Locally

1. Clone this repo:
    ```bash
    git clone https://github.com/your-username/resume-builder-app.git
    cd resume-builder-app
    ```

2. Create a `.streamlit/secrets.toml` file:
    ```toml
    OPENROUTER_API_KEY = "your-api-key-here"
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 📦 Requirements

- Python 3.9+
- Libraries:
  - streamlit
  - requests
  - fpdf
  - langchain

---

## ✨ Built With

- [Streamlit](https://streamlit.io/)
- [OpenRouter](https://openrouter.ai/)
- [LangChain](https://www.langchain.com/)

---

## 📬 Contact

Made with ❤️ by [Your Name]  
Email: you@example.com
