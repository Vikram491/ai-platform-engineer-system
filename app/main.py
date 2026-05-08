from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import time

# -----------------------------------
# Pipeline Imports
# -----------------------------------

from pipeline.intent import extract_intent
from pipeline.design import design_system
from pipeline.schema import generate_schema
from pipeline.refine import refine_output
from pipeline.assumptions import generate_assumptions

# -----------------------------------
# Validator Imports
# -----------------------------------

from validator.validator import validate_all
from validator.repair import repair

# -----------------------------------
# Runtime Imports
# -----------------------------------

from runtime.simulator import simulate_execution
from runtime.confidence import calculate_confidence
from runtime.cost_analysis import analyze_cost_latency


app = FastAPI()

# -----------------------------------
# Enable CORS
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Home Route
# -----------------------------------

@app.get("/")
def home():

    return {
        "message": "AI Platform Engineer System Running"
    }

# -----------------------------------
# Main Generation Pipeline
# -----------------------------------

@app.post("/generate")
def generate(prompt: str):

    start_time = time.time()

    repair_activated = False

    # -----------------------------------
    # Stage 1 — Intent Extraction
    # -----------------------------------

    intent = extract_intent(prompt)

    # -----------------------------------
    # Stage 2 — Assumption Engine
    # -----------------------------------

    assumptions = generate_assumptions(intent)

    # -----------------------------------
    # Stage 3 — System Design
    # -----------------------------------

    design = design_system(intent)

    # -----------------------------------
    # Stage 4 — Schema Generation
    # -----------------------------------

    schema = generate_schema(design)

    # -----------------------------------
    # Stage 5 — Refinement
    # -----------------------------------

    refined = refine_output(schema)

    # -----------------------------------
    # Stage 6 — Validation
    # -----------------------------------

    valid, errors = validate_all(refined)

    # -----------------------------------
    # Stage 7 — Intelligent Repair
    # -----------------------------------

    if not valid:

        repair_activated = True

        refined = repair(refined, errors)

        valid, errors = validate_all(refined)

    # -----------------------------------
    # Stage 8 — Runtime Simulation
    # -----------------------------------

    runtime_report = simulate_execution(refined)

    # -----------------------------------
    # Stage 9 — Latency Analysis
    # -----------------------------------

    latency = time.time() - start_time

    cost_analysis = analyze_cost_latency(latency)

    # -----------------------------------
    # Stage 10 — Confidence Scoring
    # -----------------------------------

    confidence_score = calculate_confidence(
        errors,
        runtime_report,
        assumptions
    )

    # -----------------------------------
    # Final Response
    # -----------------------------------

    return {

        "status": "success" if valid else "failed",

        "intent": intent,

        "assumptions": assumptions,

        "design": design,

        "final_output": refined,

        "validation_errors": errors,

        "runtime_report": runtime_report,

        "confidence_score": confidence_score,

        "repair_activated": repair_activated,

        "cost_analysis": cost_analysis
    }