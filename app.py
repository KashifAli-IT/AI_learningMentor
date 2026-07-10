# ============================================================
# AI Mentor App (Hugging Face Ready)
# ============================================================

import os
import gradio as gr
from groq import Groq

# ============================================================
# LOAD API KEY FROM ENV
# ============================================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in environment variables")

client = Groq(api_key=GROQ_API_KEY)


# ============================================================
# CORE LLM FUNCTION
# ============================================================
def call_llm(prompt, model="llama-3.1-8b-instant"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an AI Mentor.
                    Focus on problem-solving, not just explaining.
                    Style:
                    - Clean formatting (headings, bullets)
                    - Short, clear responses
                    - Encourage thinking
                    """
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=900
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ============================================================
# PROMPT BUILDER
# ============================================================
def build_prompt(user_input, mode, level):

    base = f"""
    User Input: {user_input}
    Level: {level}
    Mode: {mode}
    """

    if mode == "📘 Learn Concept":
        return base + """
        Provide:
        - Simple explanation
        - Key concepts (bullets)
        - Real-world usage
        - Small example
        """

    elif mode == "🧠 Practice Problems":
        return base + """
        Generate:
        - 5 problems (easy → medium → hard)
        - Real-world context
        - Do NOT include answers
        """

    elif mode == "✅ Evaluate Answer":
        return base + """
        Evaluate:
        - Correctness
        - Missing parts
        - Improvements
        - Ideal answer
        """

    elif mode == "🏗 Best Practices":
        return base + """
        Explain:
        - Decomposition
        - Modularity
        - Patterns
        - Common mistakes
        """

    elif mode == "🔍 Deep Dive":
        return base + """
        Provide:
        - Step-by-step explanation
        - Advanced insights
        - Edge cases
        """

    return base


# ============================================================
# CHAT FUNCTION
# ============================================================
def mentor_chat(user_input, mode, level, history):

    if not user_input.strip():
        return history, ""

    prompt = build_prompt(user_input, mode, level)
    response = call_llm(prompt)

    # history.append((f"{mode} → {user_input}", response))
    history.append({"role": "user", "content": f"{mode} → {user_input}"})
    history.append({"role": "assistant", "content": response})

    return history, ""


# ============================================================
# UI
# ============================================================
with gr.Blocks() as app:

    gr.Markdown("# 🚀 AI Mentor")
    gr.Markdown("Learn by thinking. Not memorizing.")

    # chatbot = gr.Chatbot(height=450)
    chatbot = gr.Chatbot(height=450)

    user_input = gr.Textbox(
        placeholder="Enter topic, question, or problem...",
        label="Your Input"
    )

    with gr.Row():
        mode = gr.Radio(
            [
                "📘 Learn Concept",
                "🧠 Practice Problems",
                "🏗 Best Practices",
                "🔍 Deep Dive",
                "✅ Evaluate Answer"
            ],
            value="📘 Learn Concept",
            label="Mode"
        )

        level = gr.Dropdown(
            ["beginner", "intermediate", "advanced"],
            value="beginner",
            label="Level"
        )

    send_btn = gr.Button("Ask Mentor")

    state = gr.State([])

    send_btn.click(
        mentor_chat,
        inputs=[user_input, mode, level, state],
        outputs=[chatbot, user_input]
    )

# ============================================================
# LAUNCH
# ============================================================
app.launch()
