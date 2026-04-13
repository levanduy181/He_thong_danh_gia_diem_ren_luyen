FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV REFLEX_USE_NPM=1
ENV REFLEX_HOT_RELOAD_EXCLUDE_PATHS=data
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm && npm install -g npm@10 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
RUN mkdir -p /app/data /app/uploaded_files && chmod +x /app/docker-entrypoint.sh
EXPOSE 3000
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]
