#!/bin/bash
echo "Starting Tourism AI Backend..."
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

