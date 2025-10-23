
# 🧠📊 AI Structurizer

**AI Structurizer** is a lightweight **FastAPI** application that converts **unstructured text** into **structured JSON** using the latest **OpenAI APIs**.  
It supports **generic structuring** and **schema-based extraction** (e.g., calendar events or research papers).

---

## 🚀 Features

✅ Convert any unstructured text into structured JSON (`/structure/`)  
✅ Extract specific structured data using schemas (`/extract/`)  

* Calendar events  
* Research papers  
✅ Built with **FastAPI**, **OpenAI SDK**, and **Pydantic**  
✅ Fully **Dockerized** for easy deployment 🐳  
✅ Includes **automated test suite** with **pytest** 🧪  
✅ Integrated **CI/CD workflow** via **GitHub Actions** for build, test, and deploy  

---

## ⚡ Endpoints

### 1. **Generic Structuring**

**POST** `/structure/`

**Request:**

```json
{
  "text": "John ordered 3 books from Amazon on Friday."
}
````

**Response:**

```json
{
  "structured_output": {
    "customer_name": "John",
    "items": ["books"],
    "quantity": 3,
    "platform": "Amazon",
    "date": "Friday"
  }
}
```

---

### 2. **Structured Extraction**

**POST** `/extract/`

**Request:**

```json
{
  "schema": "calendar",
  "text": "Alice and Bob are going to a science fair on Friday."
}
```

**Response:**

```json
{
  "structured_output": {
    "name": "science fair",
    "date": "Friday",
    "participants": ["Alice", "Bob"]
  }
}
```

---

## 🧪 Run Tests

All test cases are executed using Docker Compose with a mocked OpenAI key.
This ensures CI/CD pipelines can run tests **without real API credentials**.

```bash
docker-compose run tests
```

✅ Example output:

```
tests/test_main.py::test_structure_endpoint_valid_input PASSED
tests/test_main.py::test_structure_endpoint_no_input PASSED
tests/test_main.py::test_extract_calendar PASSED
tests/test_main.py::test_extract_invalid_schema PASSED
```

All tests validate both endpoints and ensure structured data is returned correctly.

---

## 🐳 Run with Docker

Build and run the app locally:

```bash
docker-compose build
docker-compose up
```

Open your browser at 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API interactively.

---

## ⚙️ CI/CD Integration

The repository includes a **GitHub Actions workflow** that:

1. Builds the Docker image (`ai-structurizer`)
2. Runs all test cases inside a Docker container
3. Tags and pushes the image to **Docker Hub** automatically

This ensures every push to `main` is **tested, validated, and deployed** in a reproducible environment.

---

## ⚙️ Requirements

* Python **3.12**
* **OpenAI API Key** (set in `.env` for local development; tests are mocked)
* **Docker** and **Docker Compose**

---

## ✨ Notes

* `/structure/` endpoint handles **any unstructured text**.
* `/extract/` endpoint validates structured output via **Pydantic schemas**.
* Unit tests ensure **consistent behavior** in CI/CD pipelines.
* Ideal for **data extraction**, **AI preprocessing**, and **automation** workflows.

```
