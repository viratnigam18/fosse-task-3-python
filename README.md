# FOSSEE Task 3 — Python

## Overview
This repository contains my submission for **FOSSEE Python Screening Task 3: Evaluating Open Source Models for Student Competence Analysis**.  

The task required preparing a research plan, answering reasoning questions, and evaluating open-source AI models for their suitability in analyzing student competence.

---

## Reasoning Answers

**1. What makes a model suitable for high-level competence analysis?**  
It should be able to *explain* code (not just generate it), handle long contexts, and be robust to buggy inputs. Interpretability and instruction-following behavior are key.

**2. How would you test whether a model generates meaningful prompts?**  
I would use a set of student codes and measure whether the model’s prompts reveal conceptual gaps (human-graded), and verify the prompts guide students without giving final solutions.

**3. Trade-offs between accuracy, interpretability, and cost?**  
Larger models often yield better accuracy but are costlier and harder to run locally. Smaller models are cheaper and faster but may hallucinate or give shallow explanations. A middle-ground is to use specialized models (like StarCoder) or distilled versions.

**4. Why choose the model you evaluated and what are its strengths/limitations?**  
Example: *StarCoder2* — strength: trained specifically on code, large context windows, good for code explanation and debugging hints. Limitation: resource-heavy for larger sizes, and still requires human verification for subtle bugs.

---

## Models Considered
- **StarCoder2** (BigCode project, Hugging Face) — specialized for multi-language code tasks.  
- **Code Llama** (Meta) — LLaMA-based family fine-tuned for coding.  
- **Falcon-40B-Instruct** (TII, Apache 2.0) — strong general-purpose LLM, can serve as a baseline.  

---
