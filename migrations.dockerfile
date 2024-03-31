FROM python:3.12.1-alpine3.19

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

CMD ["alembic", "upgrade", "head"]