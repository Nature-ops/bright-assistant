# Engineering Notebook

## 2026-07-05

Today I learned:

- FastAPI
- GET endpoints
- POST endpoints
- Pydantic Models

Questions I still have:

- Difference between Request and Response models.

Ideas:

- Bright Assistant should remember AWS mistakes.

# Engineering Notebook

## Date

2026-07-05

---

## Topic

FastAPI Basics

---

## Objective

Understand how FastAPI creates web APIs.

---

## What I Learned

- What FastAPI is.
- Difference between GET and POST.
- What Uvicorn does.
- What Pydantic models are.

---

## Challenges

- Typed Python code into PowerShell instead of the editor.
- Learned the difference between the editor and the terminal.

---

## Solution

Python code belongs in `.py` files.

PowerShell is only for commands.

---

## Questions

- How does FastAPI know which endpoint to execute?

---

## Next Topic

API Routers

# Engineering Notebook

---

## Date

2026-07-06

---

## Sprint

BA-002

---

## Topic

Building a Modular FastAPI Backend

---

## Objective

Learn how to organize a FastAPI application using a professional software architecture.

---

## What I Learned

### FastAPI

- FastAPI creates the web application.
- Uvicorn runs the FastAPI server.
- Swagger automatically documents API endpoints.

### API Routers

- API routes should be grouped by feature.
- Each router has one responsibility.
- Routers are connected to the application using `include_router()`.

### Pydantic Models

- Request models validate incoming data.
- Response models define outgoing data.
- FastAPI performs validation automatically.

### Service Layer

- Business logic should not live inside API routes.
- Routes should call services.
- Services perform the actual work.

### Project Organization

Today I learned that organizing code is just as important as writing code.

Keeping related code inside dedicated folders makes the application easier to maintain as it grows.

---

## Challenges

- I accidentally typed Python code into the PowerShell terminal instead of placing it inside a Python file.
- I learned the difference between the terminal and the code editor.
- I initially organized a few folders incorrectly and later corrected the structure.

---

## Solutions

- Python code belongs inside `.py` files.
- The terminal is used to execute commands.
- Every file should have one clear responsibility.

---

## Architecture Decisions

We decided that:

- `main.py` should remain small.
- API routes belong in `app/api`.
- Business logic belongs in `app/services`.
- Models belong in `app/models`.

---

## Questions

- How will multiple routers communicate?
- How will dependency injection work in FastAPI?

---

## Next Goal

Create a configuration layer using `settings.py`.

Then connect Bright Assistant to a real AI model.


## Topic

Configuration Management

### What I Learned

- Applications should not hardcode configuration values.
- Environment variables allow different configurations for development, testing, and production.
- `BaseSettings` loads configuration automatically.
- `.env` stores local configuration.
- `.env.example` documents required configuration without exposing secrets.

### Why It Matters

A professional application should be configurable without changing the source code.

### Challenges

- Learned where `.env` should be stored.
- Learned how FastAPI loads application settings.

### Next Goal

Build a logging system for Bright Assistant.