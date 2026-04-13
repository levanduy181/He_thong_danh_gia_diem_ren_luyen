#!/bin/sh
set -eu

cd /app
mkdir -p /app/data /app/uploaded_files

if [ ! -f /app/.web/package.json ]; then
  python -m reflex run --backend-host 0.0.0.0 --frontend-port 3000 --backend-port 8000 > /tmp/reflex-bootstrap.log 2>&1 &
  REFLEX_PID=$!

  for _ in $(seq 1 90); do
    if [ -f /app/.web/package.json ]; then
      break
    fi
    if ! kill -0 "$REFLEX_PID" 2>/dev/null; then
      break
    fi
    sleep 2
  done

  if kill -0 "$REFLEX_PID" 2>/dev/null; then
    kill "$REFLEX_PID" 2>/dev/null || true
    wait "$REFLEX_PID" 2>/dev/null || true
  fi

  if [ ! -f /app/.web/package.json ]; then
    echo "Khong the khoi tao frontend Reflex trong container." >&2
    if [ -f /tmp/reflex-bootstrap.log ]; then
      cat /tmp/reflex-bootstrap.log >&2
    fi
    exit 1
  fi
fi

if [ ! -d /app/.web/node_modules/tslib ]; then
  cd /app/.web
  npm install tslib --no-save --legacy-peer-deps
  cd /app
fi

exec python -m reflex run --backend-host 0.0.0.0 --frontend-port 3000 --backend-port 8000
