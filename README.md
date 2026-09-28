# 🧠 EchoMind

### An AI that remembers your audience.

> **Brands don't have a memory of their audience. EchoMind gives them one.**

EchoMind is an AI-powered audience intelligence agent that learns from historical social-media interactions and content-performance data, remembers what an audience responds to, and uses that memory to generate more informed content recommendations.

Instead of treating every post as a fresh decision, EchoMind builds persistent memory of **what worked, what the audience cared about, and what the team learned**.

---

## 🚀 Live Demo

**[Launch EchoMind](https://echomind-ai0o.onrender.com)**

**GitHub:** [github.com/saivarun-04/echomind](https://github.com/saivarun-04/echomind)

---

## 👥 Team

| Name | Role |
|---|---|
| **Sai Varun Gotteparthi** | Team Lead (TL) |
| **Karanam Poorna Chandra Rayudu** | Team Member |
| **Ch Likith Gandhi** | Team Member |
| **K Siddish** | Team Member |
| **Nelluri Karthikeya** | Team Member |
| **Abinay Karthik Varma** | Team Member |

---

## 🎯 Problem

Social-media teams continuously collect audience interactions and content-performance data, but that experience is often fragmented across posts, analytics, reports, and individual team members.

As a result:

- Teams repeatedly make similar content decisions.
- Successful audience preferences can be forgotten.
- Lessons from previous posts are difficult to reuse.
- Recommendations can rely on generic engagement patterns instead of the brand's own audience.
- Different platforms and audiences can have different preferences.

### The missing layer is memory.

A social-media agent should not only generate content.

It should **remember the audience it is creating content for.**

---

## 💡 Solution

EchoMind turns historical audience experience into persistent AI memory.

The core learning loop is:

```text
Audience Experience
        ↓
   Hindsight Retain
        ↓
   Hindsight Recall
        ↓
  Hindsight Reflect
        ↓
Audience-Aware Recommendation
        ↓
   New Experience
        ↓
      Memory
```

The recommendation is grounded in remembered audience behavior rather than starting from zero every time.

---

## 🧠 Hindsight Integration

Hindsight is the core memory layer of EchoMind.

### 1. Retain — Learn from experience

When the team provides an audience experience, EchoMind stores it in Hindsight.

Example:

> Our LinkedIn post about practical Python tips received strong engagement. The audience preferred concise, specific code examples over generic motivational content.

### 2. Recall — Retrieve relevant memory

When the team asks what the audience prefers, EchoMind retrieves relevant memories.

Example:

```text
Query:
What type of content did the audience respond positively to?
```

Hindsight can recall information such as:

```text
Audience prefers concise, specific code examples
over generic motivational content.
```

### 3. Reflect — Reason over memory

EchoMind uses Hindsight Reflect to turn remembered experience into an actionable recommendation.

Example:

```text
Create a practical technical post with concise,
specific code examples.

Avoid generic motivational content.
```

This creates the central EchoMind loop:

**Experience → Remember → Recall → Reflect → Improve**

---

## 🗂️ Three Types of Audience Memory

### 📚 Content Memory

What was published and how did it perform?

Examples:

- Post topics
- Content formats
- Engagement patterns
- Platform-specific performance
- Successful content styles

### 👥 Audience Memory

What did people actually respond to?

Examples:

- Frequently requested topics
- Positive reactions
- Common questions
- Complaints
- Audience preferences
- Preferred content formats

### 🧩 Decision Memory

What did the team learn from previous experiences?

Examples:

- Why a particular format worked
- What should be repeated
- What should be avoided
- How future content decisions should change

---

## ✨ Core Features

- 🧠 **Persistent Audience Memory** — Store audience experiences in Hindsight.
- 🔍 **Memory Recall** — Retrieve relevant audience behavior.
- 💭 **Memory-Based Recommendations** — Generate practical recommendations from remembered experience.
- 📈 **Learning From Experience** — Add new experiences so the knowledge base can evolve.
- 🎯 **Audience-Specific Intelligence** — Ground recommendations in a specific audience.
- 🌐 **Web Dashboard** — Add experiences, view memories, and generate recommendations.

---

## 🖥️ Application Workflow

### Step 1 — Teach EchoMind

```text
Our LinkedIn post about practical Python tips
received strong engagement.

The audience preferred concise, specific code
examples over generic motivational content.
```

EchoMind stores the experience in Hindsight.

### Step 2 — View Memory

```text
WHAT HINDSIGHT REMEMBERS

• Audience prefers concise code examples
• Practical technical posts receive strong engagement
• Generic motivational content performs worse
```

### Step 3 — Generate Recommendation

```text
Create a practical technical post with
concise, specific code examples.

Avoid generic motivational content.
```

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │   EchoMind UI    │
                    │  Web Dashboard   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │     Backend      │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  Retain  │   │  Recall  │   │ Reflect  │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                   ┌─────────────────┐
                   │    Hindsight    │
                   │  Memory System  │
                   └─────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **FastAPI** | Backend API |
| **Hindsight** | Persistent memory, recall and reasoning |
| **Hindsight Python SDK** | Hindsight integration |
| **HTML / CSS / JavaScript** | Frontend dashboard |
| **Uvicorn** | ASGI application server |
| **Render** | Cloud deployment |
| **Git / GitHub** | Version control |

---

## 🔌 API Endpoints

### `GET /`

Loads the EchoMind web dashboard.

### `GET /health`

Checks whether the backend is running.

```json
{
  "status": "healthy"
}
```

### `POST /learn`

Stores a new audience experience in Hindsight.

Example:

```json
{
  "content": "Our LinkedIn post about practical Python tips received strong engagement.",
  "context": "LinkedIn content performance"
}
```

### `GET /memory`

Retrieves relevant audience memories.

### `GET /recommendation`

Generates an audience-aware recommendation using Hindsight memory.

Example response:

```json
{
  "platform": "LinkedIn",
  "recommendation": "Post a concise, specific code example...",
  "reasoning": "Hindsight Reflect generated this recommendation using the audience memories stored in Hindsight."
}
```

---

## 📁 Project Structure

```text
echomind/
│
├── app/
│   ├── main.py
│   └── hindsight_service.py
│
├── static/
│   └── index.html
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` contains private credentials and is excluded from Git.

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/saivarun-04/echomind.git
cd echomind
```

### 2. Create a virtual environment

Windows:

```cmd
python -m venv .venv
```

Activate:

```cmd
.venv\Scripts\activate
```

### 3. Install dependencies

```cmd
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
```

Never commit API keys or other secrets to GitHub.

### 5. Run EchoMind

```cmd
python -m uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## ☁️ Deployment

EchoMind is deployed on Render.

### Production URL

**https://echomind-ai0o.onrender.com**

The application runs using:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## 🔐 Security

Sensitive credentials are loaded through environment variables.

The `.env` file is excluded from version control:

```gitignore
.env
__pycache__
```

---

## 🧪 Example Learning Cycle

### Initial Experience

```text
A LinkedIn post about practical Python tips
received strong engagement.
```

### Audience Insight

```text
The audience prefers concise and specific
code examples over generic motivational content.
```

### Recommendation

```text
Create another practical technical post
with concise, specific code examples.
```

### New Experience

The result of the new post can be stored again:

```text
Experience
    ↓
Memory
    ↓
Recommendation
    ↓
New Experience
    ↓
Updated Memory
```

---

## 🌟 Why Memory Matters

A conventional content-generation workflow can look like:

```text
Prompt → Generate
```

EchoMind is designed around:

```text
Experience
    ↓
Remember
    ↓
Recall
    ↓
Reason
    ↓
Recommend
    ↓
Learn Again
```

The value is not only in generating an answer.

It is in making the system capable of using **previous audience experience** when making future decisions.

---

## 📌 Current Scope

EchoMind currently focuses on audience-memory-driven recommendations for social-media content decisions.

The implementation demonstrates:

- Persistent audience memory
- Experience retention
- Relevant memory recall
- Memory-grounded reasoning
- Audience-aware recommendations
- A working web dashboard
- Cloud deployment

---

## 🔮 Future Scope

Potential extensions include:

- Platform-specific audience memory
- Automated analytics ingestion
- Post-performance tracking
- Sentiment-aware memory
- Audience segmentation
- Content experimentation
- Long-term brand knowledge
- Feedback-driven recommendation improvement

---

## 📄 License

This project is intended for educational, experimentation, and hackathon use.

---

## 🙌 Acknowledgements

Built with **Hindsight** to explore how persistent memory can make AI agents more useful over time.

---

# 🧠 EchoMind

### **An AI that remembers your audience.**

**Live Demo:** https://echomind-ai0o.onrender.com  
**Repository:** https://github.com/saivarun-04/echomind
