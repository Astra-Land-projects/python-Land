#GEMINI_API_KEY=#
#mkdir Astra-AI
#cd Astra-AI

#mkdir templates static

#pip install fastapi uvicorn python-dotenv google-genai#
#requirements.txt
#fastapi
#uvicorn
#python-dotenv
#google-genai#
#python main.py#
import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from google import genai


# ============================================================
# ASTRA AI
# Web AI Assistant
# Version 1.0
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY was not found in .env"
    )


# ============================================================
# Gemini
# ============================================================

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-3.8-flash"


# ============================================================
# App
# ============================================================

app = FastAPI(
    title="ASTRA AI",
    version="1.0.0"
)


# ============================================================
# Static / Templates
# ============================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


# ============================================================
# Logging
# ============================================================

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "ASTRA-AI"
)


# ============================================================
# Request Model
# ============================================================

class ChatRequest(BaseModel):

    message: str


# ============================================================
# Homepage
# ============================================================

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# ============================================================
# AI Endpoint
# ============================================================

@app.post("/api/chat")
async def chat(data: ChatRequest):

    message = data.message.strip()

    if not message:

        return {
            "success": False,
            "error": "Message is empty."
        }


    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": message
                        }
                    ]
                }
            ]
        )

        answer = response.text

        if not answer:

            answer = (
                "متأسفانه پاسخی دریافت نشد."
            )


        return {
            "success": True,
            "response": answer
        }


    except Exception as error:

        logger.exception(
            "Gemini API error"
        )

        return {
            "success": False,
            "error": (
                "خطایی هنگام ارتباط با "
                "هوش مصنوعی رخ داد."
            )
        }


# ============================================================
# Health Check
# ============================================================

@app.get("/api/health")
async def health():

    return {
        "status": "online",
        "service": "ASTRA AI",
        "model": MODEL
    }


# ============================================================
# Run
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
.........
<!DOCTYPE html>

<html lang="fa" dir="rtl">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>ASTRA AI</title>

    <link
        rel="stylesheet"
        href="/static/style.css"
    >

</head>


<body>

<div class="app">

    <!-- Header -->

    <header class="header">

        <div class="brand">

            <div class="logo">
                A
            </div>

            <div>

                <h1>ASTRA AI</h1>

                <span>
                    Intelligent AI Assistant
                </span>

            </div>

        </div>


        <div class="status">

            <span class="status-dot"></span>

            Online

        </div>

    </header>


    <!-- Chat -->

    <main
        id="chat"
        class="chat"
    >

        <div class="welcome">

            <div class="welcome-logo">
                A
            </div>

            <h2>
                Welcome to ASTRA AI
            </h2>

            <p>
                Ask anything. Build anything.
            </p>

        </div>

    </main>


    <!-- Input -->

    <footer class="input-area">

        <div class="input-box">

            <textarea
                id="message"
                rows="1"
                placeholder="پیامت رو برای ASTRA بنویس..."
            ></textarea>

            <button
                id="send"
                aria-label="Send"
            >
                ➤
            </button>

        </div>

        <div class="hint">
            ASTRA AI • Powered by Gemini
        </div>

    </footer>

</div>


<script
    src="/static/script.js"
></script>

</body>

</html>
.........
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background:
        radial-gradient(
            circle at top,
            #17171c,
            #08080a 60%
        );

    color: #ffffff;

    min-height: 100vh;
}


.app {

    width: 100%;
    max-width: 1100px;

    height: 100vh;

    margin: auto;

    display: flex;
    flex-direction: column;
}


/* =========================================================
   Header
   ========================================================= */

.header {

    height: 80px;

    padding: 0 25px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    border-bottom:
        1px solid
        rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);
}


.brand {

    display: flex;

    align-items: center;

    gap: 12px;
}


.logo {

    width: 45px;
    height: 45px;

    border-radius: 14px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 25px;

    font-weight: bold;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #888888
        );

    color: #08080a;
}


.brand h1 {

    font-size: 19px;

    letter-spacing: 1px;
}


.brand span {

    display: block;

    margin-top: 3px;

    font-size: 11px;

    color: #888;
}


.status {

    display: flex;

    align-items: center;

    gap: 7px;

    font-size: 12px;

    color: #aaa;
}


.status-dot {

    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #6cff9b;

    box-shadow:
        0 0 12px
        rgba(108,255,155,.7);
}


/* =========================================================
   Chat
   ========================================================= */

.chat {

    flex: 1;

    overflow-y: auto;

    padding: 35px 20px;
}


.welcome {

    height: 100%;

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;
}


.welcome-logo {

    width: 75px;
    height: 75px;

    border-radius: 25px;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 40px;

    font-weight: bold;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #777
        );

    color: #08080a;

    margin-bottom: 20px;
}


.welcome h2 {

    font-size: 28px;

    margin-bottom: 10px;
}


.welcome p {

    color: #777;

    font-size: 14px;
}


/* =========================================================
   Messages
   ========================================================= */

.message {

    display: flex;

    margin-bottom: 20px;

    animation:
        fadeIn .25s ease;
}


.message.user {

    justify-content: flex-start;
}


.message.ai {

    justify-content: flex-end;
}


.bubble {

    max-width: 75%;

    padding: 14px 17px;

    border-radius: 18px;

    line-height: 1.8;

    font-size: 14px;

    white-space: pre-wrap;
}


.user .bubble {

    background: #202025;

    border-bottom-right-radius: 5px;
}


.ai .bubble {

    background: #111114;

    border:
        1px solid
        rgba(255,255,255,.08);

    border-bottom-left-radius: 5px;
}


/* =========================================================
   Input
   ========================================================= */

.input-area {

    padding: 15px 20px 20px;
}


.input-box {

    display: flex;

    align-items: flex-end;

    gap: 10px;

    padding: 10px;

    background: #111114;

    border:
        1px solid
        rgba(255,255,255,.08);

    border-radius: 18px;
}


textarea {

    flex: 1;

    resize: none;

    border: none;

    outline: none;

    background: transparent;

    color: white;

    font-size: 14px;

    padding: 9px;

    max-height: 150px;
}


textarea::placeholder {

    color: #666;
}


button {

    width: 42px;
    height: 42px;

    border: none;

    border-radius: 13px;

    cursor: pointer;

    background: white;

    color: black;

    font-size: 18px;

    transition:
        transform .2s,
        opacity .2s;
}


button:hover {

    transform: scale(1.05);
}


button:disabled {

    opacity: .4;

    cursor: not-allowed;
}


.hint {

    text-align: center;

    color: #555;

    font-size: 10px;

    margin-top: 8px;
}


/* =========================================================
   Loading
   ========================================================= */

.loading {

    display: flex;

    align-items: center;

    gap: 5px;
}


.loading span {

    width: 6px;
    height: 6px;

    border-radius: 50%;

    background: #aaa;

    animation:
        bounce 1s infinite;
}


.loading span:nth-child(2) {

    animation-delay: .15s;
}


.loading span:nth-child(3) {

    animation-delay: .3s;
}


@keyframes bounce {

    0%, 100% {
        transform: translateY(0);
        opacity: .4;
    }

    50% {
        transform: translateY(-5px);
        opacity: 1;
    }
}


@keyframes fadeIn {

    from {

        opacity: 0;

        transform:
            translateY(8px);
    }

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}


/* =========================================================
   Mobile
   ========================================================= */

@media (max-width: 600px) {

    .header {

        padding: 0 15px;
    }

    .chat {

        padding: 25px 12px;
    }

    .bubble {

        max-width: 88%;
    }

    .welcome h2 {

        font-size: 22px;
    }

}
.........
const chat = document.getElementById("chat");

const input = document.getElementById("message");

const sendButton = document.getElementById("send");


let loading = false;


/* ============================================================
   Add Message
   ============================================================ */

function addMessage(
    text,
    type
) {

    const welcome =
        document.querySelector(".welcome");

    if (welcome) {
        welcome.remove();
    }


    const message =
        document.createElement("div");

    message.className =
        `message ${type}`;


    const bubble =
        document.createElement("div");

    bubble.className =
        "bubble";

    bubble.textContent =
        text;


    message.appendChild(
        bubble
    );

    chat.appendChild(
        message
    );


    scrollToBottom();

    return message;
}


/* ============================================================
   Loading
   ============================================================ */

function addLoading() {

    const message =
        document.createElement("div");

    message.className =
        "message ai";

    message.id =
        "loading-message";


    const bubble =
        document.createElement("div");

    bubble.className =
        "bubble loading";


    for (let i = 0; i < 3; i++) {

        const dot =
            document.createElement("span");

        bubble.appendChild(dot);
    }


    message.appendChild(
        bubble
    );

    chat.appendChild(
        message
    );


    scrollToBottom();
}


function removeLoading() {

    const loading =
        document.getElementById(
            "loading-message"
        );

    if (loading) {
        loading.remove();
    }
}


/* ============================================================
   Scroll
   ============================================================ */

function scrollToBottom() {

    chat.scrollTop =
        chat.scrollHeight;
}


/* ============================================================
   Send
============================================================ */

async function sendMessage() {

    if (loading) {
        return;
    }


    const message =
        input.value.trim();


    if (!message) {
        return;
    }


    addMessage(
        message,
        "user"
    );


    input.value = "";

    input.style.height =
        "auto";


    loading = true;

    sendButton.disabled =
        true;


    addLoading();


    try {

        const response =
            await fetch(
                "/api/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message
                    })
                }
            );


        const data =
            await response.json();


        removeLoading();


        if (data.success) {

            addMessage(
                data.response,
                "ai"
            );

        } else {

            addMessage(
                "❌ " +
                (
                    data.error ||
                    "خطایی رخ داد."
                ),
                "ai"
            );
        }


    } catch (error) {

        removeLoading();


        addMessage(
            "❌ ارتباط با سرور برقرار نشد.",
            "ai"
        );

    }


    loading = false;

    sendButton.disabled =
        false;

    input.focus();
}


/* ============================================================
   Button
   ============================================================ */

sendButton.addEventListener(
    "click",
    sendMessage
);


/* ============================================================
   Enter
   ============================================================ */

input.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();
        }

    }
);


/* ============================================================
   Auto Resize
   ============================================================ */

input.addEventListener(
    "input",
    function() {

        this.style.height =
            "auto";

        this.style.height =
            Math.min(
                this.scrollHeight,
                150
            ) + "px";
    }
);