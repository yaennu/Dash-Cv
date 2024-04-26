# First stage: build
FROM python:3.11.5-slim as builder

# Upgrade pip
RUN pip install --upgrade pip

# Install Poetry
RUN pip install poetry

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copying in our source code
COPY ./app /app

# Second stage: runtime
FROM python:3.11.5-slim

# Upgrade pip
RUN pip install --upgrade pip

# Install Poetry
RUN pip install poetry

# Create a non-root user
RUN useradd --create-home appuser
USER appuser

# Copy from builder
COPY --from=builder /app /app

WORKDIR /app

# Run the application:
CMD ["poetry", "run", "python", "app.py"]