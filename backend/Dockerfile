FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application files

COPY main.py .
COPY LinearRegression.pkl .

# Copy dataset

COPY Data ./Data

# Expose FastAPI port

EXPOSE 8000

# Start FastAPI

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
