Test Automation Framework — API & UI

Tech stack:
UI: Python + Pytest + Playwright + python-xdist
API Python + Pytest + requests + python-xdist


Step to install and run tests:

1. Install _uv_ [uv installation instruction](https://docs.astral.sh/uv/getting-started/installation/)

for ux/mac run:

```bash
pip install uv
```
2. After installation, open a new terminal window and verify:
```bash
uv --version
```
3. Run sync:

```bash
uv sync
```
uv sync creates a local .venv and installs every dependency pinned in pyproject.toml / uv.lock.

4. Activate the virtual environment so pytest runs directly, without prefixing every command with uv run:

macOS / Linux
```commandline
source .venv/bin/activate
```
Windows (PowerShell):
```commandline
.venv\Scripts\Activate.ps1
```
5. Install playwright browser:
```bash
playwright install
```

6. Running the tests:

All tests:

```bash
pytest -v
```
API tests only:
```bash
pytest -m api -v
```
UI tests only:
```bash
pytest -m ui -v
```
Run in parallel (multiple workers):
```bash
pytest -n auto -v
```