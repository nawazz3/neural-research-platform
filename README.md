# Neural Research Platform

Enterprise-Grade Multi-Agent AI Research System
---
Demo:https://drive.google.com/file/d/1tolKMXMF8oDuw50_gmhsIGR4UPNdCEJq/view?usp=drive_link

## Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [Architecture](#-architecture)
* [Technology Stack](#-technology-stack)
* [Getting Started](#-getting-started)
* [Project Structure](#-project-structure)
* [Configuration](#-configuration)
* [Export Options](#-export-options)
* [API Reference](#-api-reference)
* [Monitoring & Metrics](#-monitoring--metrics)
* [Contributing](#-contributing)
* [Acknowledgements](#-acknowledgements)

---

# Overview

**Neural Research Platform** is an enterprise AI system that orchestrates a team of specialized AI agents to conduct deep research, extract structured insights, produce professional-grade reports, and validate output quality — autonomously.

Built for researchers, analysts, consultants, and enterprise teams, the platform provides a polished **Streamlit** interface on top of a robust multi-agent backend powered by **CrewAI** and ultra-fast LLM inference.

> **One topic in → Four specialized agents → One validated, exportable report**

The system ensures:
* Structured research workflows
* Source-backed intelligence
* Quality assurance validation
* Multi-format export readiness
* Full research traceability

---

# Features

## AI Agent Team

| Agent                  | Role               | Responsibility                                       | Output                 |
| ---------------------- | ------------------ | ---------------------------------------------------- | ---------------------- |
| 🔬 Research Specialist | Data Acquisition   | Web search, source gathering, raw data collection    | `research_findings.md` |
| 📊 Data Analyst        | Insight Extraction | Pattern detection, synthesis, statistical validation | `analysis_report.md`   |
| ✍️ Content Writer      | Report Authoring   | Structured professional writing                      | `final_report.md`      |
| ✅ QA Reviewer          | Quality Assurance  | Accuracy checks, clarity scoring, validation         | `critique_report.md`   |

---

## Platform Capabilities

* Multi-format export — **PDF, Word, JSON, Markdown**
* Real-time progress tracking with confidence scoring
* Per-agent health monitoring dashboard
* System Control panel (depth, sources, validation)
* Session history & full audit trail
* Enterprise Mode toggle
* Role-based access (Admin, Analyst, Viewer)

---

# Architecture

## Agent Pipeline

```
User Input (Topic)
        │
        ▼
Research Specialist  ──► Serper Web Search API
        │
        ▼
Data Analyst         ──► Groq LLM Inference
        │
        ▼
Content Writer       ──► Groq LLM Inference
        │
        ▼
QA Reviewer          ──► Groq LLM Inference
        │
        ▼
Final Consolidated Report (PDF · DOCX · JSON · Markdown)
```

Each agent operates independently but passes structured output downstream to ensure consistency and traceability.

---

# Technology Stack

| Layer               | Technology   |
| ------------------- | ------------ |
| Frontend            | Streamlit    |
| Agent Orchestration | CrewAI       |
| LLM Inference       | Groq         |
| Web Search          | Serper       |
| PDF Generation      | ReportLab    |
| Word Generation     | python-docx  |
| Environment         | Python 3.10+ |

---

# Getting Started

## Prerequisites

* Python 3.10+
* Groq API Key
* Serper API Key

---

## 1️⃣ Clone the Repository

```bash
git clone  https://github.com/nawazz3/neural-research-platform.git
cd neural-research-platform
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

⚠️**Never commit your `.env` file.** It is excluded via `.gitignore`.⚠️
---

## 5️⃣ Launch the Application

```bash
streamlit run app.py
```

Application will run at:

```
http://localhost:8501
```

---
# 📁 Project Structure

```
neural-research-platform/
│
├── app.py
├── crew.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── research_findings.md
    ├── analysis_report.md
    ├── final_report.md
    ├── critique_report.md
    └── final_consolidated_report.md
```

Each research run generates structured, auditable artifacts.

---

# ⚙️ Configuration

The **System Control Panel** enables pipeline customization.

## Research Settings

| Parameter         | Options                     | Default  | Description               |
| ----------------- | --------------------------- | -------- | ------------------------- |
| Research Depth    | Standard / Deep / Executive | Standard | Controls breadth & depth  |
| Number of Sources | 3–20                        | 5        | Max sources used          |
| Validation Layer  | Enabled / Disabled          | Enabled  | Activates QA agent        |
| Enterprise Mode   | On / Off                    | Off      | Unlocks advanced features |

---

## Role-Based Access

| Role    | Permissions                            |
| ------- | -------------------------------------- |
| Admin   | Full access, system control, analytics |
| Analyst | Research, export, history              |
| Viewer  | Read-only report access                |

---

##  Advanced Features

* Risk Scoring Engine (0–100 sensitivity control)
* Citation Panel (APA, MLA, Chicago, Harvard)
* Enterprise feature toggles
* Adjustable QA strictness

---

# 📥 Export Options

| Format          | Description                | Best For                 |
| --------------- | -------------------------- | ------------------------ |
| 📄 PDF          | Print-ready via ReportLab  | Archival & presentations |
| 📝 Word (.docx) | Editable via python-docx   | Collaboration            |
| 📦 JSON         | Structured data + metadata | API / Automation         |
| 📃 Markdown     | Portable plain-text        | GitHub / Documentation   |

Exports are available immediately after completion.

---

# 🔑 API Reference

## Required Services

| Service | Purpose              | Free Tier           |
| ------- | -------------------- | ------------------- |
| Groq    | LLM inference engine | ✅ Available         |
| Serper  | Google Search API    | ✅ 2,500 calls/month |

---

## Environment Variables

```env
GROQ_API_KEY=gsk_...
SERPER_API_KEY=...
```

---

# 📊 Monitoring & Metrics

The Dashboard provides real-time performance visibility.

## 📈 Session Metrics

* Total Sessions
* Success Count
* Success Rate
* Average Execution Time


This enables enterprise-grade observability and reliability.

---

# Contributing

We welcome contributions.

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Commit Using Conventional Commits

```bash
git commit -m "feat: add feature description"
```

### 3. Push and Open PR

```bash
git push origin feature/your-feature-name
```

Please ensure:

* No regression in existing functionality
* Clean, readable commits
* Documentation updates where applicable

For major changes, open an issue first.

---


#  Acknowledgements

* CrewAI — Multi-agent orchestration
* Streamlit — Web interface
* Groq — Ultra-low latency inference
* Serper — Real-time search
* ReportLab — PDF generation
* python-docx — Word document creation


