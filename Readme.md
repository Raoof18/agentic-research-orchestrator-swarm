# Agentic Research Orchestrator Swarm

A modular, asynchronous multi-agent system designed to perform automated research and executive summarization using **Llama 3.1** via the Groq API.

## Overview
This system orchestrates a "swarm" of specialized AI agents:
*   **Researchers (Alice & Bob):** Perform parallel, deep-dive research on specific topics.
*   **Manager (James):** Synthesizes raw research data into a polished, professional Markdown report.

##  Architecture
The project is built with a focus on clean code and production-ready patterns:
*   **Asynchronous Orchestration:** Powered by `asyncio` for non-blocking API calls.
*   **Data Validation:** Uses `Pydantic` models to ensure structured data integrity between agents.
*   **Modular Design:** Separated into `models`, `agents`, and `utils` for high maintainability.
*   **Performance Monitoring:** Includes a custom Python decorator to log agent execution time.

##  Tech Stack
*   **Language:** Python 3.11+
*   **AI Engine:** Groq SDK (Llama 3.1)
*   **Data Models:** Pydantic v2
*   **Environment:** Python-dotenv for secure API key management

##  Installation & Usage
1. Clone the repo:
   ```bash
   git clone [https://github.com/Raoof18/agentic-research-orchestrator-swarm.git](https://github.com/Raoof18/agentic-research-orchestrator-swarm.git)