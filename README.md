# 🧠 AI Ops Agent (MVP)

### Lightweight AI-driven operations intelligence for modern SaaS & e-commerce teams

---

## 🚨 The Problem

Growing engineering teams face **operational issues every day**:

- Sudden error spikes after deployments  
- Increased latency in specific regions  
- Payment or checkout failures  
- Alert fatigue with no clear action items  

Most teams either:
- React manually and late  
- Depend on static alerts with no context  
- Over-invest in heavy enterprise tooling  

👉 **The real gap:**  
Teams don’t lack alerts — they lack **decision intelligence**.

---

## ✅ What This AI Ops Agent Does

This project is a **minimal, focused AI Operations Agent** that:

- Analyzes operational events (errors, latency, deploy signals)
- Reasons like a **senior operations engineer**
- Identifies:
  - What is going wrong
  - Severity level (LOW / MEDIUM / HIGH)
  - Possible root causes
  - Recommended next actions
- Produces **structured, decision-ready output** (logs only)

⚠️ **Important:**  
This MVP intentionally **does not execute automation**.  
It focuses on **accurate reasoning and recommendations first**.

---

## 🧩 Why This Matters

Most automation tools:
- Trigger actions blindly
- Lack system-level context
- Create more noise than clarity

This agent acts as a **thinking layer** between:
> Raw system signals → Human or automated actions

That makes it:
- Safer
- Explainable
- Easier to trust
- Easier to extend

---

## 📌 Example Input

```json
{
  "service": "checkout-service",
  "error_rate": "18%",
  "latency_ms": 2400,
  "region": "ap-south-1",
  "last_deploy": "2 hours ago",
  "symptoms": [
    "payment failures",
    "timeout errors"
  ]
}
```

---

## 📤 Example Output (Simplified)

```
Issue Summary:
Checkout service is experiencing elevated error rates and latency shortly after a recent deployment.

Severity:
HIGH

Possible Root Causes:
- Deployment introduced regression
- Region-specific infrastructure degradation
- Downstream payment gateway instability

Recommended Actions:
- Roll back the last deployment
- Enable detailed error logging
- Check payment gateway health in ap-south-1
- Notify on-call engineer
```

This is the **exact format ops teams need** to act quickly.

---

## 🛠️ What This MVP Is (and Is Not)

### ✅ This MVP IS:
- AI-driven operational analysis
- Decision intelligence
- Lightweight and fast to demo
- Easy to understand for non-AI stakeholders

### ❌ This MVP is NOT:
- A dashboard
- A monitoring replacement
- A Zapier-style workflow tool
- A black-box automation engine

Those come **later**, once reasoning is trusted.

---

## 🧱 Architecture (Intentionally Simple)

- **CrewAI** for agent orchestration  
- **Single agent** with clear responsibility  
- **Log-only output** (no side effects)  
- **Local execution** for fast iteration  

This design keeps:
- Costs low
- Risk low
- Clarity high

---

## 🔄 How This Evolves (Future Phases)

This MVP is designed to grow naturally:

### Phase 2
- API execution (rollback, alerts, tickets)
- Slack / email notifications
- Runbooks as tools

### Phase 3
- Multi-agent collaboration
- Memory & historical context
- Automated remediation (with approval gates)

Clients can adopt **only what they need**.

---

## 👥 Who This Is For

- SaaS founders & CTOs  
- E-commerce ops teams  
- Engineering managers  
- Companies wanting **AI-assisted ops**, not blind automation  

Also suitable as:
- A portfolio project
- A freelance service foundation
- A proof of AI systems thinking

---

## ▶️ How to Run (Developer Friendly)

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python run.py
```

Output is printed directly to the console.

---

## 🧠 Why This Approach Works

Instead of asking:
> “What action should we automate?”

This project asks:
> **“What decision should a senior engineer make here?”**

That shift is what makes AI automation **useful, safe, and scalable**.

---

## 📌 Final Note

This project is intentionally minimal — by design.

It demonstrates:
- Clear problem framing
- AI agent reasoning
- Production-ready thinking
- Real-world applicability

If you’re interested in extending or integrating this into real systems, this MVP is the **right starting point**.
