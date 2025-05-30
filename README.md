## AI-File-Classifier
Objective:

  Build a multi-agent AI system that accepts input in PDF, JSON, or Email (text) format, classifies the format and intent, and routes it to the appropriate agent. The system must maintain shared context (e.g., sender, topic, last extracted fields) to enable chaining and traceability.

## Project Structure
```text
multi_agent_system/
│
├── README.md
├── .gitignore
│
├── backend/
│   ├── app.py                     # Main FastAPI/Flask app
│   ├── requirements.txt
│
│   ├── agents/                    # All agent logic here
│   │   ├── __init__.py
│   │   ├── classifier_agent.py    # Format + intent classification
│   │   ├── email_agent.py         # Handles email parsing
│   │   ├── json_agent.py          # Handles JSON extraction
│   │   └── pdf_agent.py           # Handles PDF parsing/extraction
│
│   ├── memory/                    # Shared memory module
│   │   ├── __init__.py
│   │   ├── memory.py              # Unified interface for Redis/SQLite
│   │   └── context_store.db       # Used if SQLite is chosen
│
│   ├── utils/                     # Helper functions & classifiers
│   │   ├── __init__.py
│   │   ├── format_detector.py     # Detects PDF / JSON / Email
│   │   ├── intent_classifier.py   # Detects RFQ, Complaint, etc.
│   │   └── pdf_parser.py          # Raw PDF text extractor (e.g. pdfplumber)
│
│   ├── data/                      # I/O samples & logs
│   │   ├── input/
│   │   │   ├── sample_email.txt
│   │   │   ├── sample_json.json
│   │   │   └── sample_pdf.pdf
│   │   └── output/
│   │       ├── extracted/
│   │       │   ├── processed_email.json
│   │       │   ├── processed_json.json
│   │       │   └── processed_pdf.json
│   │       └── logs/
│   │           └── system_log.txt
│
│   └── tests/                     # Unit tests for each component
│       ├── test_classifier.py
│       ├── test_email_agent.py
│       ├── test_json_agent.py
│       ├── test_pdf_agent.py
│       └── test_memory.py
│
├── frontend/                      # React (Vite) frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── api/                   # Axios or fetch clients
│   │   │   └── agentApi.js
│   │   ├── components/
│   │   │   ├── UploadForm.jsx     # Upload PDF, JSON, Email
│   │   │   ├── ResultView.jsx     # Displays agent output
│   │   │   └── MemoryLog.jsx      # Shows conversation context
│   │   └── styles/
│   │       └── app.css
│   ├── package.json
│   └── vite.config.js
```
