# AI-Based Job Application & Career Support System

A full-stack application for AI-powered job applications, resume analysis, ATS scoring, and career recommendations.

## Project Structure

```
ai-job-system/
├── frontend/          # React + TypeScript client
├── backend/           # FastAPI REST API
├── ai-services/       # ML modules (resume parsing, ATS scoring, recommendations)
├── docs/              # Documentation
├── docker/            # Docker configurations
└── .github/           # GitHub workflows and actions
```

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.10+
- Docker (optional)

### Development

1. **Frontend**: `cd frontend && npm install && npm start`
2. **Backend**: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
3. **AI Services**: See `ai-services/` for ML module setup

### Environment Variables

Copy `.env.example` to `.env` and configure your environment.

## License

MIT
