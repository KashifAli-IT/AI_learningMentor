---

# AI Mentor App

**Learn by thinking. Not memorizing.**

The AI Mentor App is a fast, interactive web application powered by **Gradio** and **Groq's LLaMA 3.1 (8B)** model. It acts as an intelligent coding and concept mentor that focuses on guiding you through problem-solving rather than just handing you the answers.

## Features

The application adapts to your specific learning needs using a customizable prompt builder. You can adjust both the **Mode** and the **Level** to tailor the mentor's responses.

**Supported Modes:**

* **📘 Learn Concept:** Simple explanations, key takeaways, real-world usage, and small examples.
* **🧠 Practice Problems:** Generates 5 problems (easy to hard) with real-world context (no answers provided so you can actually practice!).
* **🏗 Best Practices:** Explains decomposition, modularity, design patterns, and common mistakes.
* **🔍 Deep Dive:** Step-by-step advanced insights and edge cases.
* **✅ Evaluate Answer:** Critiques your provided answer for correctness, missing parts, and potential improvements.

**Difficulty Levels:**

* Beginner
* Intermediate
* Advanced

## 🛠 Prerequisites

Before running the app, ensure you have Python installed along with the required libraries.

Install the dependencies using pip:

```bash
pip install gradio groq

```

## 🔑 Environment Setup

This app uses the Groq API to run the LLM. You must have a valid Groq API key set as an environment variable, otherwise, the application will throw an error upon startup.

**On Linux/macOS:**

```bash
export GROQ_API_KEY="your_api_key_here"

```

**On Windows (Command Prompt):**

```cmd
set GROQ_API_KEY=your_api_key_here

```

**On Windows (PowerShell):**

```powershell
$env:GROQ_API_KEY="your_api_key_here"

```

## 🚀 How to Run

Once your dependencies are installed and your API key is set, simply execute the Python script:

```bash
python app.py

```

*(Replace `app.py` with whatever you named your Python file).*

Gradio will generate a local web server (usually running on `http://127.0.0.1:7860`). Open that URL in your web browser to start chatting with your AI Mentor.

## 🧠 Under the Hood

* **UI Framework:** Gradio (`gr.Blocks`, `gr.Chatbot`)
* **LLM Provider:** Groq
* **Model Used:** `llama-3.1-8b-instant`
* **Generation Parameters:** Temperature is set to `0.7` for a balance of creativity and accuracy, with a `900` max token limit per response.
