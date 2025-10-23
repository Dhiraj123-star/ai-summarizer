from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

# -----------------------------
# Test 1: Generic Structuring
# -----------------------------
def test_structure_endpoint_valid_input(monkeypatch):
    """Test generic structuring endpoint with mock OpenAI response"""

    # Mock OpenAI client chat completions
    class MockChoice:
        message = type("msg", (), {"content": '{"customer": "John", "order": "books"}'})

    class MockCompletions:
        @staticmethod
        def create(*args, **kwargs):
            return type("obj", (), {"choices": [MockChoice()]})

    monkeypatch.setattr("main.client.chat.completions", MockCompletions)

    response = client.post("/structure/", json={"text": "John ordered some books."})
    assert response.status_code == 200
    data = response.json()
    assert "structured_output" in data
    assert data["structured_output"]["customer"] == "John"

# -----------------------------
# Test 2: Missing Input
# -----------------------------
def test_structure_endpoint_no_input():
    """Test handling of missing text input"""
    response = client.post("/structure/", json={})
    assert response.status_code == 200
    assert response.json()["error"] == "No input text provided."

# -----------------------------
# Test 3: Structured Extraction (Calendar)
# -----------------------------
def test_extract_calendar(monkeypatch):
    """Test structured extraction endpoint for calendar schema"""

    class MockParsed:
        def model_dump(self):
            return {"name": "science fair", "date": "Friday", "participants": ["Alice", "Bob"]}

    class MockResponses:
        @staticmethod
        def parse(*args, **kwargs):
            return type("MockResponse", (), {"output_parsed": MockParsed()})

    monkeypatch.setattr("main.client.responses", MockResponses)

    response = client.post("/extract/", json={
        "schema": "calendar",
        "text": "Alice and Bob are going to a science fair on Friday."
    })

    assert response.status_code == 200
    data = response.json()["structured_output"]
    assert data["name"] == "science fair"
    assert "Alice" in data["participants"]

# -----------------------------
# Test 4: Invalid Schema
# -----------------------------
def test_extract_invalid_schema():
    """Test error response for invalid schema type"""
    response = client.post("/extract/", json={"schema": "invalid", "text": "Some text"})
    assert response.status_code == 200
    assert "Invalid schema type" in response.json()["error"]
