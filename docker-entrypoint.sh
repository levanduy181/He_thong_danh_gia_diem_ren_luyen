#!/bin/sh
set -eu

cd /app
mkdir -p /app/data /app/uploaded_files

MARKER_FILE=/app/.web/reflex.install_frontend_packages.cached

if [ -d /app/.web ] && [ ! -f "$MARKER_FILE" ]; then
  rm -rf /app/.web
fi

if [ ! -f "$MARKER_FILE" ]; then
  setsid sh -c "python main.py" > /tmp/reflex-bootstrap.log 2>&1 &
  REFLEX_PID=$!

  for _ in $(seq 1 90); do
    if [ -f "$MARKER_FILE" ]; then
      break
    fi
    if ! kill -0 "$REFLEX_PID" 2>/dev/null; then
      break
    fi
    sleep 2
  done

  if kill -0 "$REFLEX_PID" 2>/dev/null; then
    kill -TERM -"$REFLEX_PID" 2>/dev/null || kill "$REFLEX_PID" 2>/dev/null || true
    wait "$REFLEX_PID" 2>/dev/null || true
    sleep 2
  fi

  if [ ! -f "$MARKER_FILE" ]; then
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

exec python main.py
