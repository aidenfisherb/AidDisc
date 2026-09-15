from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>Hello</h1>
    <button onclick="ping()">Ping</button>
    <p id="out"></p>
    <script>
      async function ping() {
        const r = await fetch('/api/ping');
        document.getElementById('out').textContent = (await r.json()).msg;
      }
    </script>
    """

@app.get("/api/ping")
def ping():
    return {"msg": "pong from the API"}
