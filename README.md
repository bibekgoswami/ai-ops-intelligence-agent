# 🚀 AI Ops Intelligence Agent

An **AI-powered Operations Intelligence Agent** designed to assist engineering and SRE teams in **analyzing production incidents**, assessing impact, and generating **actionable remediation guidance** using LLMs.

This project focuses on **practical Ops intelligence**, not generic chatbots.

---

## 🧠 What This Agent Does

Given a production incident or operational event, the agent:

- ✅ Diagnoses the issue using structured reasoning  
- ✅ Assesses **severity and blast radius**
- ✅ Generates **root cause hypotheses** (not guesses)
- ✅ Suggests **actionable remediation steps**
- ✅ Responds in a format suitable for real Ops workflows  

Built for environments where **partial signals, noisy alerts, and time pressure** are the norm.

---

## 🏗️ Architecture Overview

**Core components:**

- **Ops Intelligence Agent**  
  Encapsulates senior-level operational reasoning and decision-making logic.

- **Task Orchestration (CrewAI)**  
  Coordinates analysis steps in a deterministic, inspectable flow.

- **Structured Inputs**  
  Incident context is provided as structured input, mimicking real-world alert payloads.

- **LLM-backed Reasoning**  
  Uses LLMs for synthesis, prioritization, and hypothesis generation — not blind automation.

---

## 🧩 Project Structure

```
ai-ops-intelligence-agent/
├── agent/          # Ops agent definition & prompt logic
├── task/           # Incident analysis tasks
├── inputs/         # Sample incident payloads
├── crew.py         # Agent-task orchestration
├── run.py          # Execution entry point
└── README.md
```

---

## ▶️ Running the Agent

### 1. Setup environment
```bash
pip install -r requirements.txt
```

### 2. Configure API access
```bash
export OPENAI_API_KEY="your_api_key"
```

### 3. Run the agent
```bash
python run.py
```

---

## 🎯 Use Cases

- Production incident triage  
- On-call decision support  
- SRE & Platform Engineering workflows  
- Ops-focused AI experimentation  
- Agentic system design reference  

---

## 🚧 Current Status

This is an **early-stage but functional MVP**, focused on:
- Correct reasoning
- Clear outputs
- Ops relevance

---

## 👨‍💻 Author

**Bibek Jyoti Goswami**  
Backend Tech Lead | Distributed Systems | Agentic AI for Ops & Reliability  

🔗 LinkedIn: https://www.linkedin.com/in/bibek-jyoti-goswami-a16aa585/

---

## 📌 Why This Project Exists

Most AI agents optimize for demos.  
This one optimizes for **operational thinking**.
