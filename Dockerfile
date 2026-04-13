FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    REFLEX_USE_NPM=1 \
    REFLEX_HOT_RELOAD_EXCLUDE_PATHS=data

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/data /app/uploaded_files \
    && python -c "from reflex.utils.prerequisites import get_compiled_app; get_compiled_app(check_if_schema_up_to_date=False, dry_run=False, use_rich=False)" \
    && cd .web && npm install tslib --no-save --legacy-peer-deps

EXPOSE 3000 8000

CMD ["python", "-m", "reflex", "run", "--backend-host", "0.0.0.0", "--frontend-port", "3000", "--backend-port", "8000"]
