# ============================
#   appDesk Backend - Dockerfile
#   Python 3.11 + Django + DRF
# ============================

# --- Base image ---
FROM python:3.11-slim

# --- Environment variables ---
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV APP_HOME=/app

# --- System dependencies ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libmagic1 \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Create app directory ---
WORKDIR $APP_HOME

# --- Copy requirements ---
COPY requirements.txt .

# --- Install Python dependencies ---
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# --- Copy backend source ---
COPY src ./src

# --- Expose Django port ---
EXPOSE 8000

# --- Default command ---
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
