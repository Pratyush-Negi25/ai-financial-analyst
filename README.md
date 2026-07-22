# AI Financial Analyst
### Intelligent Financial Report Analysis using Retrieval-Augmented Generation (RAG), FastAPI, React, FAISS, and Google Gemini

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![Vite](https://img.shields.io/badge/Vite-Build_Tool-646CFF?logo=vite)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Repository Description

AI Financial Analyst is a Retrieval-Augmented Generation (RAG) based web application that enables users to upload financial reports in PDF format and interact with them through natural language using Google Gemini. The application performs semantic search using Sentence Transformers and FAISS to provide context-aware financial insights rather than relying solely on keyword matching.

---

# Table of Contents

- Project Overview
- Problem Statement
- Proposed Solution
- Key Features
- Demo Workflow
- System Architecture
- Technology Stack
- Repository Structure
- Backend Architecture
- Frontend Architecture
- API Documentation
- AI Pipeline
- Backend Workflow
- Frontend Workflow
- Installation
- Official Resources
- Environment Variables
- Usage
- Screenshots
- Troubleshooting
- Phase-wise Development
- Engineering Decisions
- Performance Considerations
- Security Considerations
- Future Enhancements
- Roadmap
- Resume Highlights
- Contributing
- License
- Acknowledgements

---

# Project Overview

## Introduction

Organizations publish annual reports, financial statements, quarterly filings, and investor presentations containing hundreds of pages of valuable financial information.

Extracting meaningful insights from these reports manually is:

- Time-consuming
- Error-prone
- Difficult for non-financial users
- Inefficient for repeated queries

This project introduces an AI-powered Financial Analyst that enables users to upload financial reports and ask questions in natural language.

Instead of manually reading an entire document, users receive context-aware answers generated using Retrieval-Augmented Generation (RAG).

---

## Objectives

The primary objectives of this project are:

- Automate financial document understanding
- Improve accessibility of financial reports
- Demonstrate a production-style Retrieval-Augmented Generation pipeline
- Combine semantic search with Large Language Models
- Provide an intuitive web interface for interacting with financial documents

---

## Target Users

This application is useful for:

- Students
- Researchers
- Financial Analysts
- Investors
- Business Professionals
- Data Scientists
- AI Enthusiasts

---

# Problem Statement

Financial reports are lengthy and highly technical.

A typical annual report may contain:

- Income Statements
- Cash Flow Statements
- Balance Sheets
- Notes to Accounts
- Risk Factors
- Corporate Governance
- Management Discussion
- Future Outlook

Finding answers such as

> "What was Amazon's operating income in 2024?"

often requires manually searching hundreds of pages.

Traditional keyword search suffers from several limitations:

- Cannot understand context
- Misses semantically related information
- Returns irrelevant results
- Cannot summarize information
- Does not answer questions conversationally

As document sizes increase, manual analysis becomes increasingly inefficient.

---

# Proposed Solution

The AI Financial Analyst addresses these challenges by combining semantic retrieval with Google's Gemini Large Language Model.

The application follows a Retrieval-Augmented Generation (RAG) architecture.

Instead of asking Gemini directly, the workflow is:

1. Upload PDF
2. Extract text
3. Split document into semantic chunks
4. Generate embeddings
5. Store vectors inside FAISS
6. Retrieve the most relevant chunks
7. Provide retrieved context to Gemini
8. Generate a grounded response

This significantly improves:

- Accuracy
- Context awareness
- Response relevance
- Hallucination reduction
- Financial document understanding

---

# Key Features

## Backend Features

### Document Processing

- PDF Upload API
- PDF validation
- Text extraction using PyMuPDF
- Automatic document preprocessing
- Intelligent text chunking
- Embedding generation
- Vector storage using FAISS
- Metadata persistence
- Semantic similarity search

---

### AI Features

- Google Gemini integration
- Context-aware prompting
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Natural language question answering
- Financial report understanding

---

### API Features

- RESTful FastAPI architecture
- JSON responses
- Environment-based configuration
- Modular services
- Configurable Gemini model
- Error handling
- Logging support
- Health endpoint

---

## Frontend Features

### Modern Interface

- React + Vite frontend
- Responsive layout
- Glassmorphism UI
- Modern typography
- Interactive cards
- Professional color palette

---

### Upload Module

- PDF upload interface
- Upload status
- File validation
- Progress feedback

---

### AI Chat Module

- Natural language question input
- AI response card
- Loading indicators
- Error messages
- Clean conversation layout

---

### User Experience

- Responsive design
- Minimalistic interface
- Accessible typography
- Smooth transitions
- Clear workflow
- Beginner-friendly interaction

---

# Demo Workflow

```
User

    │

    ▼

Upload Financial Report (PDF)

    │

    ▼

FastAPI Upload Endpoint

    │

    ▼

Extract PDF Text

    │

    ▼

Chunk Document

    │

    ▼

Generate Embeddings

    │

    ▼

Store in FAISS

    │

──────────────────────────────

User asks a question

    │

    ▼

Semantic Retrieval

    │

    ▼

Top Relevant Chunks

    │

    ▼

Prompt Construction

    │

    ▼

Google Gemini

    │

    ▼

Context-Aware Answer

    │

    ▼

Displayed in React UI
```

---

# High-Level System Architecture

```
                +--------------------+
                |     React UI       |
                +---------+----------+
                          |
                    Axios HTTP
                          |
                +---------v----------+
                |      FastAPI       |
                +---------+----------+
                          |
        +-----------------+-----------------+
        |                                   |
        ▼                                   ▼
 PDF Processing                    Chat Endpoint
        |                                   |
        ▼                                   ▼
 Text Extraction                 Semantic Retrieval
        |                                   |
        ▼                                   ▼
 Intelligent Chunking            Relevant Chunks
        |                                   |
        ▼                                   ▼
 Sentence Embeddings            Prompt Construction
        |                                   |
        ▼                                   ▼
       FAISS  ----------------------> Google Gemini
                          |
                          ▼
                  Generated Response
                          |
                          ▼
                     React Frontend
```

---

# Technology Stack

| Category | Technologies |
|------------|-----------------------------|
| Frontend | React, Vite, CSS3 |
| Backend | FastAPI, Uvicorn |
| AI Model | Google Gemini |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| PDF Processing | PyMuPDF |
| HTTP Client | Axios |
| Configuration | python-dotenv |
| Language | Python, JavaScript |
| Styling | CSS (Glassmorphism UI) |
| Version Control | Git, GitHub |
| Development Tools | VS Code, Postman |

---

# Why Retrieval-Augmented Generation (RAG)?

Large Language Models possess impressive reasoning capabilities but lack direct access to uploaded documents.

Without retrieval, the model cannot reliably answer questions about user-specific financial reports.

RAG solves this by retrieving the most relevant document fragments before generating an answer.

Advantages include:

- Reduced hallucinations
- Document-grounded responses
- Improved factual accuracy
- Better scalability
- Context-aware answers
- Efficient semantic search

This architecture combines the strengths of vector databases with modern Large Language Models to create an intelligent financial document assistant.

---

# Repository Structure

The project follows a modular architecture that separates backend services, frontend components, configuration, and AI-specific functionality. This organization improves maintainability, scalability, and readability.

```
ai-financial-analyst/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── services/
│   │   │   ├── pdf_service.py
│   │   │   ├── chunker.py
│   │   │   ├── embedder.py
│   │   │   ├── retriever.py
│   │   │   ├── vector_store.py
│   │   │   ├── pipeline.py
│   │   │   ├── chatbot.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── logging.py
│   │   │
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── uploads/
│   ├── faiss_index/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Upload.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── Message.jsx
│   │   │   └── Loading.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── styles/
│   │   │   └── global.css
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Backend Architecture

The backend is built using **FastAPI**, chosen for its high performance, asynchronous support, automatic API documentation, and developer-friendly architecture.

The backend is organized into independent modules, where each component has a clearly defined responsibility.

---

## API Layer

The API layer acts as the communication interface between the frontend and backend.

Responsibilities include:

- Receiving HTTP requests
- Validating user input
- Calling appropriate services
- Returning JSON responses
- Handling exceptions

This separation keeps routing logic lightweight while business logic remains inside dedicated service modules.

---

## Service Layer

The service layer contains the application's core functionality.

### PDF Service

Responsible for:

- Accepting uploaded PDF files
- Saving uploaded documents
- Reading PDF content
- Extracting raw text using PyMuPDF

---

### Chunking Service

Transforms extracted text into manageable semantic chunks.

Responsibilities:

- Split long documents
- Preserve semantic meaning
- Maintain chunk consistency
- Prepare data for embedding generation

Proper chunking significantly improves retrieval accuracy.

---

### Embedding Service

Converts text chunks into dense vector embeddings using Sentence Transformers.

Responsibilities:

- Load embedding model
- Encode chunks
- Generate numerical vector representations
- Pass embeddings to the vector store

---

### Vector Store

Responsible for semantic indexing.

Responsibilities:

- Create FAISS index
- Store embeddings
- Persist metadata
- Load index on startup
- Perform similarity search

---

### Retriever

Retrieves the most relevant document chunks.

Workflow:

Question

↓

Question embedding

↓

FAISS similarity search

↓

Top matching chunks

↓

Return context

---

### Chatbot Service

Handles interaction with Google Gemini.

Responsibilities:

- Prompt construction
- Context injection
- Gemini API communication
- Response generation
- Error handling

---

### Pipeline

Coordinates all services.

Instead of tightly coupling components, the pipeline orchestrates the complete RAG workflow.

Responsibilities:

- PDF processing
- Embedding generation
- Index creation
- Retrieval
- AI response generation

---

# Frontend Architecture

The frontend is developed using **React** with **Vite** for fast development and optimized builds.

A component-based architecture improves maintainability and encourages code reuse.

---

## Header Component

Displays:

- Project title
- Short description
- Application branding

---

## Upload Component

Responsible for:

- PDF selection
- Upload button
- Upload status
- API communication
- Error handling

Workflow

User selects PDF

↓

Upload API

↓

Backend processing

↓

Status update

---

## Chat Component

Handles:

- User question input
- API requests
- Loading state
- Displaying AI responses

Workflow

Question

↓

POST /chat

↓

Backend

↓

Gemini

↓

Answer

↓

Render Response

---

## API Service

A dedicated API layer abstracts HTTP requests.

Responsibilities:

- Upload requests
- Chat requests
- Centralized backend URL
- Error propagation

Benefits:

- Cleaner components
- Easier maintenance
- Reusable request logic

---

## Styling

The application uses a centralized stylesheet implementing a clean glassmorphism-inspired design.

Features include:

- Responsive layout
- Gradient background
- Glass cards
- Modern typography
- Interactive buttons
- Styled response cards
- Upload status indicators

---

# REST API Documentation

## Root Endpoint

| Property | Value |
|------------|------------------|
| Endpoint | `/` |
| Method | GET |
| Purpose | API welcome message |

---

## Health Check

| Property | Value |
|------------|------------------|
| Endpoint | `/health` |
| Method | GET |
| Purpose | Verify backend availability |

Useful for deployment verification and monitoring.

---

## Upload Endpoint

| Property | Value |
|------------|------------------|
| Endpoint | `/upload` |
| Method | POST |
| Input | PDF File |
| Output | Success message + chunk count |

### Responsibilities

- Validate uploaded file
- Extract PDF text
- Chunk document
- Generate embeddings
- Build FAISS index
- Persist metadata

---

### Example Request

```
POST /upload

multipart/form-data

file=document.pdf
```

---

### Example Response

```json
{
    "message": "Upload successful",
    "chunks": 409
}
```

---

## Chat Endpoint

| Property | Value |
|------------|------------------|
| Endpoint | `/chat` |
| Method | POST |
| Input | Question |
| Output | AI Response |

---

### Example Request

```json
{
    "question":"What was Amazon's operating income?"
}
```

---

### Example Response

```json
{
    "answer":"Amazon reported an operating income of ..."
}
```

---

# API Request Lifecycle

```
React

     │

Axios POST

     │

FastAPI Route

     │

Validation

     │

Retriever

     │

Embedding Search

     │

Top Chunks

     │

Prompt Builder

     │

Google Gemini

     │

Generated Answer

     │

JSON Response

     │

React Rendering
```

---

# AI Pipeline

The application follows a Retrieval-Augmented Generation workflow.

```
PDF Upload

↓

Text Extraction

↓

Cleaning

↓

Chunking

↓

Sentence Embeddings

↓

FAISS Index

↓

Store Metadata

↓

User Question

↓

Question Embedding

↓

Semantic Search

↓

Relevant Chunks

↓

Prompt Construction

↓

Google Gemini

↓

Final Answer
```

---

## Stage 1 — PDF Processing

Uploaded financial reports are extracted into raw text using PyMuPDF.

---

## Stage 2 — Intelligent Chunking

Large documents are divided into semantically meaningful chunks.

Benefits include:

- Better retrieval accuracy
- Faster search
- Improved context management

---

## Stage 3 — Embedding Generation

Each chunk is transformed into a high-dimensional vector representation.

Semantic meaning is preserved, allowing concept-based retrieval rather than keyword matching.

---

## Stage 4 — Vector Storage

Embeddings are indexed using FAISS.

This enables extremely fast nearest-neighbor searches.

---

## Stage 5 — Semantic Retrieval

When the user submits a question:

1. Generate embedding
2. Search FAISS
3. Retrieve most relevant chunks

---

## Stage 6 — Prompt Construction

Retrieved document context is combined with the user's question before being sent to Gemini.

This ensures responses remain grounded in the uploaded financial report.

---

## Stage 7 — Response Generation

Google Gemini generates a context-aware answer using only the retrieved financial information.

This reduces hallucinations while improving answer quality.

---

# Backend Request Workflow

```
Application Starts

↓

Load Configuration

↓

Initialize Services

↓

Load Embedding Model

↓

Initialize FAISS

↓

Start FastAPI

↓

Receive Request

↓

Process Business Logic

↓

Return JSON Response
```

---

# Frontend Workflow

```
User Opens Application

↓

Upload PDF

↓

Backend Processes Document

↓

Success Status

↓

User Types Question

↓

POST /chat

↓

AI Processing

↓

Receive Response

↓

Display Answer
```

---

# Design Principles

The project follows several software engineering best practices:

- Modular architecture
- Separation of concerns
- Service-oriented backend
- Component-based frontend
- Reusable API layer
- Environment-based configuration
- Clean code organization
- Maintainable folder structure
- Scalable project layout
- Clear responsibility boundaries

# Installation Guide

This section provides detailed instructions for setting up the project on your local machine.

---

# System Requirements

| Requirement | Recommended Version |
|--------------|---------------------|
| Operating System | Windows 10/11, macOS, Linux |
| Python | 3.11 or newer |
| Node.js | Latest LTS |
| npm | Latest |
| RAM | Minimum 8 GB (16 GB Recommended) |
| Internet | Required for Gemini API |
| Browser | Google Chrome or Microsoft Edge |

---

# Official Resources & Downloads

Download all dependencies from their official websites.

## Python

Official Website

https://www.python.org/

Download

https://www.python.org/downloads/

Recommended Version

Python 3.11+

During installation, enable:

✔ Add Python to PATH

---

## Node.js

Official Website

https://nodejs.org/

Download

https://nodejs.org/en/download

Recommended Version

Latest LTS Release

Node.js automatically installs:

- npm

---

## Git

Official Website

https://git-scm.com/

Download

https://git-scm.com/downloads

Git is required for:

- Cloning repositories
- Version control
- Collaboration

---

## GitHub

Official Website

https://github.com/

Create an account if you don't already have one.

GitHub is used for:

- Hosting repositories
- Version control
- Collaboration
- Issue tracking

---

## Visual Studio Code

Official Website

https://code.visualstudio.com/

Download

https://code.visualstudio.com/download

Recommended Extensions

- Python
- Pylance
- ESLint
- Prettier
- GitLens
- GitHub Copilot (Optional)

---

## Google AI Studio

Official Website

https://aistudio.google.com/

Used for generating your Gemini API Key.

Steps

1. Sign in with your Google account.

2. Navigate to

Get API Key

3. Create a new API Key.

4. Copy the generated key.

5. Add it inside your `.env` file.

Example

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Gemini API Documentation

https://ai.google.dev/

Useful for understanding:

- Available models
- Pricing
- Free tier
- Rate limits
- SDKs

---

## FastAPI Documentation

https://fastapi.tiangolo.com/

---

## React Documentation

https://react.dev/

---

## Vite Documentation

https://vitejs.dev/

---

## FAISS

GitHub Repository

https://github.com/facebookresearch/faiss

Documentation

https://faiss.ai/

Purpose

High-performance vector similarity search.

---

## Sentence Transformers

https://www.sbert.net/

Purpose

Generate semantic embeddings from text.

---

## PyMuPDF

https://pymupdf.readthedocs.io/

Purpose

Extract text from uploaded PDF documents.

---

## python-dotenv

https://pypi.org/project/python-dotenv/

Used for managing environment variables.

---

## Axios

https://axios-http.com/

Used by the React frontend to communicate with the FastAPI backend.

---

## REST API Testing

Swagger UI

Automatically available after running FastAPI.

Example

```
http://127.0.0.1:8008/docs
```

Postman

https://www.postman.com/

Useful for testing API endpoints manually.

---

# Clone the Repository

```bash
git clone https://github.com/Pratyush-Negi25/ai-financial-analyst.git
```

Navigate into the project

```bash
cd ai-financial-analyst
```

---

# Backend Setup

Navigate into the backend folder.

```bash
cd backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

---

### macOS/Linux

```bash
python3 -m venv env
```

Activate

```bash
source env/bin/activate
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named

```
.env
```

Example

```env
GEMINI_API_KEY=your_api_key_here

GEMINI_MODEL=gemini-2.5-flash

CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

> **Note:** Use the Gemini model configured in your project. Update the model name if you choose a different supported version.

---

## Run Backend

```bash
uvicorn app.main:app --reload --port 8008
```

Backend will be available at

```
http://127.0.0.1:8008
```

Swagger Documentation

```
http://127.0.0.1:8008/docs
```

---

# Frontend Setup

Open a new terminal.

Navigate to the frontend folder.

```bash
cd frontend
```

---

Install dependencies.

```bash
npm install
```

---

Run the React application.

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

(or the port displayed by Vite if different.)

---

# Quick Start (5 Minutes)

```text
Clone Repository

↓

Create Virtual Environment

↓

Activate Virtual Environment

↓

Install Python Packages

↓

Create .env

↓

Add Gemini API Key

↓

Run FastAPI

↓

Install React Packages

↓

Run Vite

↓

Open Browser

↓

Upload PDF

↓

Ask Questions
```

---

# Configuration Reference

| Variable | Required | Description |
|------------|----------|-------------|
| GEMINI_API_KEY | Yes | Google Gemini API Key |
| GEMINI_MODEL | Yes | Gemini model used for response generation |
| CORS_ORIGINS | Yes | Allowed frontend origins |

---

# Dependency Explanation

| Dependency | Purpose | Used In |
|------------|----------|----------|
| FastAPI | REST API framework | Backend |
| Uvicorn | ASGI server | Backend |
| PyMuPDF | PDF text extraction | Backend |
| Sentence Transformers | Embedding generation | Backend |
| FAISS | Vector similarity search | Backend |
| Google Gemini | AI response generation | Backend |
| python-dotenv | Environment variable loading | Backend |
| NumPy | Numerical operations | Backend |
| Axios | HTTP requests | Frontend |
| React | UI library | Frontend |
| Vite | Frontend tooling | Frontend |

---

# Usage Guide

## Step 1 — Start Backend

Ensure the FastAPI server is running.

---

## Step 2 — Start Frontend

Launch the React application using Vite.

---

## Step 3 — Upload Financial Report

Click **Upload PDF** and select a financial report.

The backend will:

- Validate the file
- Extract text
- Chunk the document
- Generate embeddings
- Build the FAISS index

---

## Step 4 — Ask Questions

Example questions:

- What was Amazon's total revenue?
- What are the major business segments?
- How much operating income was reported?
- What risks did the company identify?
- Summarize the management discussion.

---

## Step 5 — Receive AI Response

The system retrieves the most relevant document chunks and generates a context-aware answer using Google Gemini.

---

# Screenshots

Replace the following placeholders with screenshots from your project.

```text
assets/

homepage.png

upload-page.png

upload-success.png

chat-interface.png

ai-response.png

swagger-api.png

architecture-diagram.png
```

Example

```markdown
![Home Page](assets/homepage.png)

![Upload](assets/upload-page.png)

![AI Response](assets/ai-response.png)
```

---

# Troubleshooting Guide

## Python Not Recognized

**Cause**

Python is not added to PATH.

**Solution**

Reinstall Python and enable **Add Python to PATH** during installation.

---

## Node Not Recognized

Install Node.js LTS and restart your terminal.

---

## Missing `.env`

Create the `.env` file inside the backend directory and add the required variables.

---

## Invalid Gemini API Key

Verify that:

- The API key is active.
- It is copied correctly.
- Billing or quota limits (if applicable) are not exceeded.
- The selected Gemini model is available for your account.

---

## Frontend Cannot Connect

Check:

- Backend is running.
- Backend port matches the frontend configuration.
- `CORS_ORIGINS` includes the frontend URL.

---

## Port Already in Use

Either stop the conflicting process or run the application on a different port.

---

## FAISS Installation Errors

Use the version compatible with your operating system and Python version.

---

## ModuleNotFoundError

Run:

```bash
pip install -r requirements.txt
```

inside the activated virtual environment.

---

## Upload Fails

Verify:

- File is a valid PDF.
- Backend server is running.
- Network connection is active.
- The upload directory has write permissions.

# Phase-wise Development Summary

The project was developed incrementally, with each phase building upon the previous one. This modular approach ensured that every component was tested independently before integrating it into the overall system.

---

## Phase 1 — Project Planning

### Objective

Define the project scope, identify the problem statement, and choose an appropriate architecture for building an AI-powered financial document assistant.

### Tasks Completed

- Requirement analysis
- Technology selection
- RAG workflow planning
- Folder structure design

### Outcome

A clear roadmap for implementing the backend, frontend, and AI pipeline.

---

## Phase 2 — Backend Setup

### Objective

Develop the REST API backend using FastAPI.

### Tasks Completed

- FastAPI project initialization
- Route configuration
- Configuration management
- Logging setup
- Environment variable support

### Outcome

A modular backend ready for AI service integration.

---

## Phase 3 — PDF Processing

### Objective

Enable document upload and text extraction.

### Tasks Completed

- PDF upload endpoint
- File validation
- PDF parsing using PyMuPDF
- Text extraction

### Outcome

Uploaded financial reports could now be converted into machine-readable text.

---

## Phase 4 — Intelligent Chunking

### Objective

Split extracted documents into meaningful semantic chunks.

### Tasks Completed

- Chunking service
- Chunk size optimization
- Metadata generation

### Outcome

Improved semantic retrieval and context preservation.

---

## Phase 5 — Embedding Generation

### Objective

Convert text chunks into numerical vector representations.

### Tasks Completed

- Sentence Transformer integration
- Embedding generation
- Batch processing

### Outcome

Documents became searchable using semantic similarity.

---

## Phase 6 — Vector Database

### Objective

Implement efficient semantic search.

### Tasks Completed

- FAISS integration
- Index creation
- Metadata storage
- Similarity search

### Outcome

Fast retrieval of relevant financial information.

---

## Phase 7 — Google Gemini Integration

### Objective

Generate intelligent responses grounded in retrieved context.

### Tasks Completed

- Gemini API integration
- Prompt construction
- Context injection
- Response handling

### Outcome

Accurate, document-aware financial question answering.

---

## Phase 8 — REST API Development

### Objective

Expose backend functionality through clean API endpoints.

### Tasks Completed

- Upload endpoint
- Chat endpoint
- Health endpoint
- Root endpoint

### Outcome

Backend services became accessible to external clients.

---

## Phase 9 — React Frontend

### Objective

Develop an intuitive web interface.

### Tasks Completed

- React setup using Vite
- Component architecture
- Routing preparation
- State management using React Hooks

### Outcome

Interactive user interface connected to the backend.

---

## Phase 10 — Upload Integration

### Objective

Connect the frontend upload component with the backend API.

### Tasks Completed

- Axios integration
- Upload status updates
- Error handling
- File validation

### Outcome

Users could upload financial reports directly from the web interface.

---

## Phase 11 — AI Chat Integration

### Objective

Allow users to ask natural language questions.

### Tasks Completed

- Chat interface
- API communication
- AI response rendering
- Loading indicators

### Outcome

Complete end-to-end RAG workflow.

---

## Phase 12 — User Interface Polish

### Objective

Improve usability and visual design.

### Tasks Completed

- Glassmorphism UI
- Modern typography
- Responsive layout
- Styled response cards
- Interactive buttons
- Upload status improvements

### Outcome

A cleaner and more professional user experience.

---

## Phase 13 — Testing

### Objective

Verify application stability.

### Tasks Completed

- Upload testing
- API validation
- Chat testing
- Error handling verification
- Frontend/backend integration

### Outcome

Stable end-to-end application.

---

## Phase 14 — Documentation

### Objective

Document the project for future users and contributors.

### Tasks Completed

- README
- Architecture explanation
- Installation guide
- API documentation
- Workflow diagrams

### Outcome

Complete project documentation.

---

# Engineering Decisions

## Why FastAPI?

FastAPI was selected due to its:

- High performance
- Automatic Swagger documentation
- Type hint support
- Asynchronous capabilities
- Clean architecture

---

## Why React?

React enables reusable UI components, efficient state management, and a scalable frontend architecture suitable for modern web applications.

---

## Why Vite?

Vite offers:

- Instant development server startup
- Fast Hot Module Replacement (HMR)
- Optimized production builds
- Minimal configuration

---

## Why FAISS?

FAISS was chosen because it provides:

- Extremely fast vector similarity search
- Efficient indexing
- Scalability for large embedding collections
- Industry-standard semantic retrieval

---

## Why Sentence Transformers?

Sentence Transformers generate high-quality semantic embeddings that preserve contextual meaning, making retrieval significantly more accurate than keyword-based search.

---

## Why Retrieval-Augmented Generation (RAG)?

Instead of relying solely on the language model's pre-trained knowledge, RAG grounds responses using retrieved document context.

Benefits include:

- Improved factual accuracy
- Reduced hallucinations
- Better document understanding
- Reliable financial question answering

---

## Why Google Gemini?

Google Gemini provides:

- Strong reasoning capabilities
- High-quality natural language generation
- Efficient API integration
- Support for contextual prompts

---

# Additional Improvements Implemented

Throughout development, several improvements were introduced to enhance code quality and maintainability.

These include:

- Modular backend architecture
- Dedicated service layer
- Centralized configuration management
- Environment variable support
- Reusable API service in React
- Component-based frontend
- Responsive UI
- Glassmorphism-inspired design
- Improved upload feedback
- Styled AI response cards
- Error handling
- Logging support
- Separation of concerns
- Scalable folder structure

---

# Security Considerations

Current security measures include:

- Environment variables for API keys
- `.gitignore` to prevent secret leakage
- CORS configuration
- Input validation
- File type validation
- Exception handling

Future improvements may include:

- User authentication
- Role-based access control
- Rate limiting
- HTTPS deployment
- Secure cloud storage

---

# Performance Considerations

Performance optimizations implemented include:

- FAISS for efficient vector search
- Semantic chunking
- Modular services
- Lightweight React frontend
- Vite development server
- Cached vector index
- Efficient PDF processing

Potential future optimizations:

- Streaming AI responses
- Incremental indexing
- Embedding caching
- Background document processing

---

# Current Limitations

The current implementation has the following limitations:

- Single document workflow
- No persistent chat history
- No OCR support
- No authentication
- No user accounts
- No cloud deployment
- No citation highlighting
- No streaming responses
- Limited by Gemini context window

These limitations provide opportunities for future enhancement.

---

# Future Enhancements

Potential improvements include:

- Multi-document support
- Chat history
- Authentication and authorization
- Citation highlighting
- Source references
- OCR support
- Financial ratio analysis
- Interactive charts
- Data visualization dashboards
- Conversation memory
- Streaming AI responses
- Docker deployment
- Kubernetes support
- Cloud deployment (AWS/GCP/Azure)
- PostgreSQL integration
- Admin dashboard
- Dark mode
- Drag-and-drop uploads
- Export chat as PDF
- Markdown rendering
- Multi-user support

---

# Project Roadmap

| Version | Features | Status |
|----------|----------|--------|
| v1.0 | PDF Upload, RAG Pipeline, Gemini Integration, React UI | Completed |
| v1.1 | Multi-document Retrieval | Planned |
| v1.2 | Authentication & Chat History | Planned |
| v1.3 | OCR Support & Citation Highlighting | Planned |
| v2.0 | Cloud Deployment & Multi-user Platform | Future |

---

# Key Technical Skills Demonstrated

This project demonstrates practical experience in:

- FastAPI REST API Development
- React Frontend Development
- Retrieval-Augmented Generation (RAG)
- Google Gemini Integration
- Vector Databases (FAISS)
- Semantic Search
- Sentence Transformers
- PDF Processing
- Prompt Engineering
- API Integration
- Environment Configuration
- Modern UI Design
- Component-based Architecture
- Modular Backend Design
- End-to-End AI Application Development

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

Please ensure that all code follows the existing project structure and coding style.

---

# License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project while retaining the original license.

---

# Acknowledgements

This project was made possible through the use of several outstanding open-source technologies and services:

- FastAPI
- React
- Vite
- Google Gemini
- Sentence Transformers
- FAISS
- PyMuPDF
- Axios
- Python Community
- Open Source Community

Special thanks to the maintainers and contributors of these projects.

---

# Author

**Pratyush Negi**

B.Tech Computer Science & Engineering  
Faculty of Technology, University of Delhi

- GitHub: https://github.com/Pratyush-Negi25
- LinkedIn: https://www.linkedin.com/in/25pratyushnegi
- Email: pratyushnegi@ce.du.ac.in

---

# Repository Topics

Suggested GitHub Topics:

```
ai
artificial-intelligence
rag
retrieval-augmented-generation
fastapi
react
vite
google-gemini
faiss
sentence-transformers
pdf
financial-analysis
machine-learning
nlp
semantic-search
```

---

# Repository Description

**AI-powered financial report analysis using FastAPI, React, FAISS, and Google Gemini with Retrieval-Augmented Generation (RAG) for intelligent document question answering.**

---

## Final Notes

This project demonstrates the complete lifecycle of building an AI-powered web application—from document ingestion and semantic retrieval to modern frontend development and LLM integration. It highlights practical software engineering principles, modular architecture, and the application of Retrieval-Augmented Generation (RAG) to solve real-world document analysis challenges.
