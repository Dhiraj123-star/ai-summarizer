
# AI Structurizer 🧠📊

**AI Structurizer** is a simple **FastAPI** project that converts unstructured text into structured JSON.  
It can handle **generic text** or extract **specific structured data** like calendar events or research papers using **OpenAI API**.

---

## 🚀 Features

- Convert any unstructured text into JSON (`/structure/`)  
- Extract structured data with defined schema (`/extract/`)  
  - Calendar events  
  - Research papers  
- Built with **FastAPI**, **OpenAI SDK**, and **Pydantic**  
- Fully **Dockerized** for easy deployment 🐳  

---

## ⚡ Endpoints

1. **Generic Structuring**
   - **POST** `/structure/`
   - Request body:
     ```json
     {
       "text": "John ordered 3 books from Amazon on Friday."
     }
     ```
   - Response:
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

2. **Structured Extraction**
   - **POST** `/extract/`
   - Request body:
     ```json
     {
       "schema": "calendar",
       "text": "Alice and Bob are going to a science fair on Friday."
     }
     ```
   - Response:
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

## 🐳 Run with Docker

```bash
docker-compose build
docker-compose up
````

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

---

## ⚙️ Requirements

* Python 3.12
* OpenAI API key (set in `.env`)
* Docker & Docker Compose

---

## ✨ Notes

* Supports both generic text and schema-based structured extraction.
* Designed for local development and easy deployment.


