FROM python:3-slim

WORKDIR /app/
COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-root \
    && poetry cache clear --all .
COPY /app ./
EXPOSE 8047
CMD ["python", "app.py"]
