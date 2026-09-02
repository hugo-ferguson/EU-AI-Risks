# EU AI Risk Mapper Frontend

Sleek proof-of-concept frontend for the EU AI Act risk assessment pipeline.

## What it does

- Uploads a requirements document (`.json`, `.txt`, `.md`, `.pdf`, or `.docx`).
- Sends the document to the Python API for risk assessment.
- Displays requirement-level EU AI Act risk findings.
- Shows risk level, obligation category, analysis, and suggested engineering actions.
- Supports filtering by risk level and obligation category.
- Includes demo mode using the current v5 report output.
- Always shows High, Medium, and Low summary cards, even when a risk count is zero.
- Uses a compliance/checklist-style brand mark instead of the earlier star icon.

## Run locally

Start the Python API from the project root:

```bash
uvicorn eu_ai_risks.api:app --reload --host 0.0.0.0 --port 8000
```

Then create `frontend/.env`:

```bash
VITE_API_URL=http://localhost:8000
```

Start the frontend:

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5174/
```

## Demo flow

1. Upload a requirements document in the left panel.
2. Click **Run assessment**.
3. The frontend sends the file to `POST /api/assess-risks`.
4. The Python API extracts requirements and runs the existing semantic-profile risk assessment pipeline.
5. The dashboard displays the generated risk findings.

The frontend is intentionally lightweight and aimed at the FYP proof-of-concept demo, not production use.
