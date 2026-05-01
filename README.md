# CG/CI/CD Proof of Concept Pipeline Implementation

## Overview
The developed Proof of Concept (PoC) pipeline extends the traditional CI/CD process by introducing an additional **Continuous Generation (CG)** stage before standard integration and deployment.

In conventional CI/CD workflows, the process begins with manually written source code. In this project, the pipeline begins earlier in the software lifecycle by using project artifacts as the primary input for automated code generation.

---

## Implemented Pipeline Structure

```text
Project Artifact (specification.md)
        ↓
Automatic Code Generation (generate_code.py)
        ↓
Generated Source Code (generated_calculator.py)
        ↓
Automated Testing (pytest)
        ↓
Validation through GitHub Actions
```

### Practical Implementation Details

The developed prototype was implemented as a dedicated GitHub repository designed to simulate an end-to-end CG/CI/CD workflow.

### Repository Components:
- **artifacts/specification.md**  
  Contains the project specification serving as the initial software artifact.

- **generator/generate_code.py**  
  A Python-based generation mechanism that automatically transforms project requirements into executable source code.

- **src/generated_calculator.py**  
  The generated software module produced automatically during pipeline execution.

- **tests/test_generated_app.py**  
  Automated validation suite verifying correctness, functionality, and software reliability.

- **.github/workflows/cg-cicd.yml**  
  GitHub Actions workflow automating the complete CG/CI/CD process.

---

## Pipeline Execution Stages

### 1. Artifact Input Stage
The process begins with project-level software requirements rather than manually written source code.

### 2. Continuous Generation Stage
The generation mechanism interprets project artifacts and automatically creates source code.

### 3. Continuous Integration Stage
Generated code is automatically integrated into the repository workflow.

### 4. Testing and Validation Stage
Automated tests validate generated code quality and correctness.

---

## Technologies Used
- GitHub
- GitHub Actions
- Python
- Pytest
- Markdown-based software specifications

---

## Research Function
This pipeline serves as the primary **research tool** for validating:

- the feasibility of automated code generation from project artifacts,
- integration of generation into CI/CD workflows,
- reduction of manual implementation effort,
- applicability of CG/CI/CD in practical software engineering environments.

---

## Proof of Concept Outcomes
The prototype successfully demonstrates:

- automated transformation of project artifacts into code,
- execution of generation before traditional CI/CD,
- automated validation of generated software,
- feasibility of extending DevOps processes toward earlier project stages.

---

## Pilot Study Relevance
This implementation provides an experimental platform for pilot participants to:

- evaluate generated code,
- measure productivity,
- identify practical limitations,
- validate the proposed research design.

---

## Scientific Contribution
The implemented pipeline confirms the technical possibility of integrating **Continuous Generation** into software delivery processes, establishing a practical basis for future research into:

- model-driven DevOps,
- AI-assisted code generation,
- automated software engineering,
- next-generation CI/CD systems.

---

## Summary
The developed CG/CI/CD Proof of Concept prototype represents a practical validation of the proposed research concept by extending traditional CI/CD with an automated software generation stage.

This implementation supports:
- pilot study execution,
- hypothesis validation,
- practical experimentation,
- and future large-scale research development.
