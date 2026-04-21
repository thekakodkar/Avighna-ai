
# Avighna AI: The Infor ERP LN Sidecar 🚀

**Avighna AI** is an enterprise-grade AI orchestration layer designed to bridge the gap between unstructured industrial data and the structured world of **Infor ERP LN**. 

As a "Privacy Sidecar," it sits alongside your ERP, processing sensitive vendor communications, machine manuals, and shop-floor data locally—ensuring that proprietary manufacturing intelligence never leaves the factory floor while maximizing ROI through autonomous agentic workflows.

---

## 🏗 The Architecture
Avighna AI is built on a **Durable Agentic Stack** (DAS), ensuring that AI processes are not just "chatty," but reliable enough for 24/7 manufacturing operations.

* **Intelligence Layer:** **LangGraph** + **Deep Agents** for autonomous planning and self-correcting logic loops.
* **Validation Layer:** **Pydantic AI** for strict enterprise data contracts (zero-hallucination policy).
* **Knowledge Layer:** **Flowise** + **Qdrant** (Vector DB) for visual RAG management of technical manuals and SOPs.
* **Inference Layer:** **Ollama** running Llama 3.2 locally for data privacy and zero per-token costs.
* **Interface Layer:** **FastAPI** providing a secure REST gateway for Infor ION integration.

---

## 🚀 Key Use Cases

### 1. The Intelligent MRO Auditor (Current MVP)
Automatically reconciles vendor Purchase Order (PO) acknowledgments against Infor LN.
* **Impact:** Identifies price discrepancies and delivery delays in real-time.
* **Value:** Prevents financial leakage and updates "Planned Receipt Dates" autonomously.

### 2. Smart Inventory Optimizer
Queries high-density technical manuals in the Knowledge Layer to suggest alternative part numbers when primary stock is unavailable.
* **Impact:** Reduces production downtime caused by supply chain bottlenecks.

### 3. Production Order Copilot
Transcribes shop-floor voice notes into structured Business Object Documents (BODs) for real-time production progress updates.
* **Impact:** Eliminates manual data entry for operators, ensuring 100% data accuracy.

---

## 🛠 Strategic Implementation Guide

### Prerequisites
* **Docker Desktop:** To run the utility grid (Qdrant, Ollama, Flowise).
* **Python 3.12+:** The core orchestration engine.
* **Ollama:** Pre-loaded with `llama3.2` or `phi-3`.

### Quick Start
1.  **Clone & Navigate:**
    ```bash
    git clone https://github.com/YourUsername/Avighna-ai.git
    cd Avighna-ai
    ```
2.  **Spin up Infrastructure:**
    ```bash
    docker-compose up -d
    ```
3.  **Setup Virtual Environment:**
    ```bash
    python -m venv .venv
    .\venv\Scripts\activate  # Windows (CMD)
    pip install -r requirements.txt
    ```
4.  **Launch the Sidecar:**
    ```bash
    uvicorn app.main:app --reload
    ```
    *Access the API documentation at http://localhost:8000/docs*

---

## 📂 Project Structure
```text
/app
├── main.py              # FastAPI Entry Point & API Routes
├── agents/
│   ├── graph.py         # LangGraph Workflow Orchestration
│   └── deep_harness.py  # Autonomous Agent Logic & Planning
├── schemas/
│   └── state.py         # Pydantic State & Data Guardrails
├── integrations/
│   ├── infor_ion.py     # Infor ERP LN API Bridge
│   └── flowise_client.py # Knowledge Layer Interface
└── core/
    └── config.py        # Enterprise Configuration
```

---

## 📜 Licensing & Terms of Use

### Personal & Educational Use
This software is provided for **personal, non-commercial, and educational use**. You are free to modify and experiment with this skeleton, provided that original credits to the author and this repository are maintained.

### Commercial Use
**STRICTLY PROHIBITED WITHOUT AUTHORIZATION.** Commercial use of Avighna AI, including deployment within a corporate environment, use for-profit services, or integration into commercial products, requires an explicit written license agreement. 

**For commercial licensing, enterprise support, or implementation consulting, please contact the maintainer.**

---

### ⚖️ Disclaimer
*This project is an independent AI solution and is not affiliated with, endorsed by, or sponsored by Infor. "Infor ERP LN" is a trademark of Infor.*
