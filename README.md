
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

---

## ⚡ Endpoints

### 1. **Generic Structuring**

**POST** `/structure/`

**Request:**

```json
{
  "text": "John ordered 3 books from Amazon on Friday."
}
```

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

You can run all test cases (for both endpoints) using Docker Compose:

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

All tests ensure both endpoints work correctly and return valid structured data.

---

## 🐳 Run with Docker

To build and run the app locally:

```bash
docker-compose build
docker-compose up
```

Then open your browser at 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API interactively.

---

## ⚙️ Requirements

* Python **3.12**
* **OpenAI API Key** (set in `.env`)
* **Docker** and **Docker Compose**

---

## ✨ Notes

* Generic `/structure/` endpoint works for **any unstructured input**.
* `/extract/` endpoint validates output using **Pydantic schemas** for precision.
* Includes **unit tests** to ensure consistent behavior.
* Ideal for **data extraction**, **AI preprocessing**, and **automation** workflows.

---

