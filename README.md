Test Automation Framework — API & UI

Tech stack:
- UI: Python + Pytest + Playwright + python-xdist
- API Python + Pytest + requests + python-xdist


Steps to install dependency and run tests:
- Installed Python 3.11+

1. Install _uv_ [uv installation instruction](https://docs.astral.sh/uv/getting-started/installation/)

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
 to run ui tests without headless mode open tests/conftest.py and set headless=True to headless=False

Run in parallel (multiple workers):
```bash
pytest -n auto -v
```

7. Test strategy:

API (tests/api/test_user.py)

Tests are grouped to demonstrate four aspects of API testing:

- Correct expected response — full CRUD coverage: login, /user/me, get single/all users, create, full update (PUT), partial update (PATCH), delete — each validated against a Pydantic schema, not just the status code.
- Data types & constraints — response bodies are parsed via model_validate() against strict schemas (extra="forbid", Strict* types), so an unexpected field or a wrong type fails the test with a precise message.
- Error handling — nonexistent user ID (404) across get/update/delete, plus invalid input handling (wrong login credentials, malformed request body).
- Boundary / edge cases — delayed responses (dummyjson's ?delay= parameter) with a timeout check, and an empty response body scenario.

dummyjson.com is a mock API — write operations (create/update/delete) don't persist between requests. Tests validate the shape and correctness of each individual response, not data persistence across calls.

UI (tests/ui/test_smoke_ui.py)

Covers the core shopping flow on [shop.unitree.com]():

- Login — authenticates with a real test account, verifies the account page.
- Add to cart — adds a product, verifies the cart page and subtotal.
- Quantity change — increases item quantity in the cart and verifies the subtotal recalculates correctly (this is the "waiting for a key calculation" scenario called out in the assignment).
- Remove from cart — removes an item and verifies the empty-cart state.
- Checkout — proceeds from cart to Shopify's checkout page and verifies the total price and the redirect URL.