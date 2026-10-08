import requests
import json
from google import genai

# =============================================================
# 1. API KEYS CONFIGURATION (Insert your keys here)
# =============================================================
GEMINI_API_KEY = "AQ.Ab8RN6KswI9XYgbCIwfiPeQ_3QQbI3d2JHN0b7Y7s6EbhXMTYg"
GROQ_API_KEY = "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"
OPENROUTER_API_KEY = "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"
GAPGPT_API_KEY = "sk-v9acBR7jCi4wGoA6x6RbNvW8XAYntvCJDil3mHYNjgmC3szw"
ZAI_API_KEY = "f3e7b97af78d4d6989722748bae3adab.3AusMBrUnVBCVgId"
DEEPSEEK_API_KEY = "sk-078e29c1320b4d23be2e8cb72d167f2b"

# Initialize Google Gemini Client
gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY != "AQ.Ab8RN6KswI9XYgbCIwfiPeQ_3QQbI3d2JHN0b7Y7s6EbhXMTYg" else None

# =============================================================
# 2. AGENTS & ROLES DEFINITION
# =============================================================
BOTS = {
    "Gemini": {
        "role": "Data Analyst & Live Research Agent",
        "system_prompt": "You are Gemini. Your role is to analyze data, perform live context processing, and provide accurate background information."
    },
    "Groq": {
        "role": "High-Speed Logic & Reasoning Agent (Llama 3.3)",
        "system_prompt": "You are the Groq-powered Agent. Your role is fast reasoning, logical review, and instant problem-solving."
    },
    "DeepSeek": {
        "role": "Lead Software Engineer",
        "system_prompt": "You are DeepSeek. Your role is to write clean, efficient, and well-structured code, and resolve technical bugs."
    },
    "OpenRouter": {
        "role": "General AI Advisor",
        "system_prompt": "You are the OpenRouter Agent. Your role is to suggest creative alternatives and technical enhancements."
    },
    "GapGPT": {
        "role": "Localization & Support Agent",
        "system_prompt": "You are GapGPT. Your role is to optimize outputs for local integration and review natural language consistency."
    },
    "Z.ai": {
        "role": "Quality Assurance (QA) & Final Inspector",
        "system_prompt": "You are Z.ai. Your role is to review the collective outputs, test scenarios, and validate the final solution."
    }
}

# =============================================================
# 3. CORE MCP SERVER (Model Context Protocol Hub)
# =============================================================
class MCPServer:
    def __init__(self):
        self.context_history = []

    def log_and_print(self, sender, role, content):
        """Save interaction to shared history and print to terminal"""
        self.context_history.append({"sender": sender, "role": role, "content": content})
        print(f"\n🤖 [{sender} - {role}]:")
        print(f"💬 {content}")
        print("-" * 65)

    def call_bot_api(self, bot_name, prompt):
        """Route requests to corresponding API endpoints safely"""
        try:
            # 1. Google Gemini API
            if bot_name == "Gemini":
                if not gemini_client or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY":
                    return "[Gemini Error]: API Key is not set."
                res = gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                return res.text

            # 2. Groq API
            elif bot_name == "Groq":
                if GROQ_API_KEY == "YOUR_GROQ_API_KEY":
                    return "[Groq Error]: API Key is not set."
                headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
                data = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=15)
                res_data = res.json()
                return res_data['choices'][0]['message']['content'] if 'choices' in res_data else f"[Groq Response Error]: {res_data}"

            # 3. DeepSeek API
            elif bot_name == "DeepSeek":
                if DEEPSEEK_API_KEY == "YOUR_DEEPSEEK_API_KEY":
                    return "[DeepSeek Error]: API Key is not set."
                headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}
                data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=15)
                res_data = res.json()
                return res_data['choices'][0]['message']['content'] if 'choices' in res_data else f"[DeepSeek Response Error]: {res_data}"

            # 4. OpenRouter API
            elif bot_name == "OpenRouter":
                if OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY":
                    return "[OpenRouter Error]: API Key is not set."
                headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
                data = {"model": "google/gemini-2.0-flash-exp:free", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=15)
                res_data = res.json()
                return res_data['choices'][0]['message']['content'] if 'choices' in res_data else f"[OpenRouter Response Error]: {res_data}"

            # 5. GapGPT API
            elif bot_name == "GapGPT":
                if GAPGPT_API_KEY == "YOUR_GAPGPT_API_KEY":
                    return "[GapGPT Error]: API Key is not set."
                headers = {"Authorization": f"Bearer {GAPGPT_API_KEY}", "Content-Type": "application/json"}
                data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.gapgpt.app/v1/chat/completions", headers=headers, json=data, timeout=15)
                res_data = res.json()
                return res_data['choices'][0]['message']['content'] if 'choices' in res_data else f"[GapGPT Response Error]: {res_data}"

            # 6. Z.ai API
            elif bot_name == "Z.ai":
                if ZAI_API_KEY == "YOUR_ZAI_API_KEY":
                    return "[Z.ai Error]: API Key is not set."
                headers = {"Authorization": f"Bearer {ZAI_API_KEY}", "Content-Type": "application/json"}
                data = {"messages": [{"role": "user", "content": prompt}]}
                res = requests.post("https://api.z.ai/v1/chat/completions", headers=headers, json=data, timeout=15)
                res_data = res.json()
                return res_data['choices'][0]['message']['content'] if 'choices' in res_data else f"[Z.ai Response Error]: {res_data}"

        except Exception as e:
            return f"❌ Connection Error for {bot_name}: {str(e)}"

    def start_workflow(self, user_prompt):
        """Execute collaborative teamwork workflow across all agents"""
        print("==========================================================")
        print(f"🚀 NEW MCP WORKFLOW STARTED:\n📌 Project Scope: {user_prompt}")
        print("==========================================================")

        # Log initial user request
        self.log_and_print("User", "Product Owner", user_prompt)

        # Sequential Agent Processing
        for bot_name, bot_info in BOTS.items():
            # Build full contextual prompt (MCP Shared Memory)
            full_context = f"SYSTEM INSTRUCTION: {bot_info['system_prompt']}\n\nMEETING HISTORY:\n"
            for msg in self.context_history:
                full_context += f"- [{msg['sender']}]: {msg['content']}\n"
           
            full_context += f"\nYour turn ({bot_name}). Provide your response based on your assigned role:"

            # Query the corresponding Agent API
            response = self.call_bot_api(bot_name, full_context)
            self.log_and_print(bot_name, bot_info['role'], response)

        print("\n✅ MCP WORKFLOW COMPLETED SUCCESSFULLY!")

# =============================================================
# 4. EXECUTION
# =============================================================
if __name__ == "__main__":
    mcp_hub = MCPServer()
   
    # Define your project objective here
    project_prompt = "Build a random project."
    mcp_hub.start_workflow(project_prompt)