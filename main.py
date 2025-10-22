import os
import json
from fastapi import FastAPI, Body
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(
    title="AI Structurizer",
    description=(
        "Generic API to convert unstructured text into structured JSON using OpenAI APIs.\n\n"
        "Endpoints:\n"
        "- `/structure/` → Generic JSON output (any text)\n"
        "- `/extract/` → Structured extraction into defined schema (Calendar or Research Paper)"
    ),
    version="1.0.0"
)

# ----------------------------
# Endpoint 1: Generic Structuring
# ----------------------------
@app.post("/structure/")
async def structured_data(data: dict = Body(...)):
    """
    Accepts raw or unstructured text (from user, API, etc.)
    and returns structured JSON representation.
    """
    text_input = data.get("text", "").strip()

    if not text_input:
        return {"error": "No input text provided."}

    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that converts any given text into a structured JSON object. "
                        "Always return valid JSON. "
                        "Infer meaningful keys and values from the input. "
                        "If data seems incomplete, include null fields."
                    ),
                },
                {"role": "user", "content": text_input},
            ],
            temperature=0,
        )

        # Extract text from response
        message = completion.choices[0].message.content.strip()

        # Try to parse the JSON returned by the model
        try:
            parsed_output = json.loads(message)
        except json.JSONDecodeError:
            parsed_output = {"raw_text_output": message}

        return {"structured_output": parsed_output}

    except Exception as e:
        return {"error": str(e)}


# ----------------------------
# Pydantic Schemas
# ----------------------------
class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


class ResearchPaperExtraction(BaseModel):
    title: str
    authors: list[str]
    abstract: str
    keywords: list[str]


# ----------------------------
# Endpoint 2: Structured Extraction (Responses API)
# ----------------------------
@app.post("/extract/")
async def extract_structured(data: dict = Body(...)):
    """
    Extract structured data (Calendar Event or Research Paper)
    using OpenAI Responses API with schema validation.
    """
    text_input = data.get("text", "").strip()
    schema_type = data.get("schema", "calendar").lower()

    if not text_input:
        return {"error": "No input text provided."}

    try:
        if schema_type == "calendar":
            schema_model = CalendarEvent
            system_prompt = "Extract the event information."
        elif schema_type == "research":
            schema_model = ResearchPaperExtraction
            system_prompt = (
                "You are an expert at structured data extraction. "
                "You will be given unstructured text from a research paper "
                "and should convert it into the given structure."
            )
        else:
            return {"error": "Invalid schema type. Use 'calendar' or 'research'."}

        # Use Responses API for structured output
        response = client.responses.parse(
            model="gpt-4o-2024-08-06",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_input},
            ],
            text_format=schema_model,
        )

        structured_data = response.output_parsed
        return {"structured_output": structured_data.model_dump()}

    except Exception as e:
        return {"error": str(e)}
