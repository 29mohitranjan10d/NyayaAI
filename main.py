from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_engine import analyze_case
from risk_engine import calculate_risk
from referral_engine import get_lawyers
from fastapi import UploadFile, File
from pypdf import PdfReader
import io
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CaseInput(BaseModel):
    text: str
    city: str

@app.post("/analyze")
def analyze(data: CaseInput):

    result = analyze_case(data.text)

    risk_score, category = calculate_risk(result, data.text)

    lawyers = get_lawyers(data.city, category)

    return {
        "analysis": result,
        "risk_score": risk_score,
        "category": category,
        "lawyers": lawyers
    }
@app.post("/analyze-file")
async def analyze_file(file: UploadFile = File(...), city: str = "Delhi"):

    contents = await file.read()

    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(contents))
        for page in reader.pages:
            text += page.extract_text() or ""

    else:
        return {"error": "Only PDF files supported for now."}

    result = analyze_case(text)
    risk_score, category = calculate_risk(result, text)
    lawyers = get_lawyers(city, category)

    return {
        "analysis": result,
        "risk_score": risk_score,
        "category": category,
        "lawyers": lawyers
    }
