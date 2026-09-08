---
task_id: 15
date: 2026-09-05
difficulty: Beginner-Intermediate (Micro-Step)
status: Incomplete
---

# Task 15: FastAPI Health Check & Startup Event (Micro-Step)

## Why a Recruiter Cares
In professional production systems, every web service must have a **Health Check endpoint** (usually `GET /` or `GET /health`). Cloud servers, load balancers, and monitoring tools ping this endpoint constantly to verify that the app is alive and the database connection is active. 

## Specifications
Open your existing `task13_api.py` (or a copy) and add these two small, bite-sized features (take 15-20 minutes max):

1. **Root Heartbeat Endpoint (`GET /`)**: 
   * Add a route at the root path that returns a simple JSON status:
     ```json
     {
         "status": "online",
         "service": "Employee Management API",
         "database": "connected"
     }
     ```
2. **Startup Print / Log**: 
   * Add a startup event (`@app.on_event("startup")`) that prints a clear message to your terminal when Uvicorn boots up (e.g., `"🚀 Employee API is live and ready for requests!"`).

## Concepts to Research (Use AI if needed!)
* `@app.get("/")` for the root path.
* `@app.on_event("startup")` for running code when the server starts.

## Self-Verification Checklist
- [ ] **Server Boot Test**: Run `uvicorn task13_api:app --reload`. Does it print your custom startup message in the terminal?
- [ ] **Browser Test**: Open `http://127.0.0.1:8000/`. Does it instantly return the JSON status dictionary?
- [ ] **Swagger Test**: Open `http://127.0.0.1:8000/docs`. Do you see the new root endpoint listed at the very top?

---

Your task note has been saved to **`C:/Users/divya/OneDrive/Documents/vs programs/TASKS/Notes/task15_note.md`**.

This is our new **micro-step** style: fast, focused, low-stress, and easy to code. Take your time, test it out, and let me know when it's working! 🛡️🚀
