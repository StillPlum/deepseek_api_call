# DeepSeek Chat Demo

Polished Flask + HTML demo for interacting with the DeepSeek Chat Completions API. The web UI delivers a futuristic dark theme, supports drag-and-drop uploads for files and images, and forwards extracted text together with the conversation history.

## Features
- Single-page chat interface with typing indicator, progress bar, and removable file chips.
- Either chat directly or upload multiple documents plus an optional note for contextual analysis.
- Best-effort text extraction for TXT/Markdown/PDF/Word/Excel; images are summarised with a placeholder line.
- Minimal prompt-generator and task-executor helpers that show how to chain DeepSeek requests.

## Quick Start
1. **Install dependencies** (Python 3.10+ recommended)

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure credentials**

   Copy `.env.example` to `.env` and fill in your DeepSeek API key.

   ```
   DS_API_KEY=your_key
   DS_API_URL=https://api.deepseek.com/v1/chat/completions
   DS_MODEL=deepseek-chat
   PORT=7860
   ```

   `client.py` defaults to the OpenAI-compatible DeepSeek endpoint above. Point it to your proxy if required.

3. **Run the app**

   ```bash
   python server.py
   ```

   Visit `http://127.0.0.1:7860/` in your browser.

## Project Structure
- `server.py` - Flask server with chat/upload/history endpoints and file parsing helpers.
- `client.py` - thin DeepSeek API wrapper.
- `chat.html` - standalone futuristic chat UI.
- `prompt_generator.py`, `task_executor.py`, `main.py` - simple prompt-to-execution demo scripts.
- `uploads/` - directory where uploads are stored (auto-created).

## API Surface
- `POST /chat` - JSON `{ "message": "..." }` for plain chat.
- `POST /upload` - multipart form with `files` (one or more) and optional `message`.
- `POST /clear` - clears the conversation state.
- `GET /history?n=50` - returns recent messages.

## File Parsing Notes
- TXT / Markdown: direct read with UTF-8 fallback.
- PDF: `pypdf` extracts up to roughly 20 pages.
- DOCX: `python-docx` collects paragraph text.
- XLSX: `openpyxl` reads up to five sheets, first 100 rows each.
- Images: no OCR yet; a placeholder line is added to the prompt context.

Parsing failures are captured in the generated summary but do not crash the request flow.

## Deployment Tips
- Disable `debug=True` in production and serve behind a proper WSGI stack or reverse proxy.
- Adjust upload size limits to suit your environment (default 25 MB).
- Keep `.env` and real API keys out of version control.

---

Made for DeepSeek integrations - have fun building!
