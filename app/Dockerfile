FROM python:3.12.3-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.8.2 \
  DJANGO_DEBUG_MODE=false

RUN apt-get update && apt-get install -y locales dos2unix && rm -rf /var/lib/apt/lists/* \
  && echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen

RUN pip install gunicorn "poetry==$POETRY_VERSION"

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-ansi --no-interaction --only main

COPY ./ ./

# Convert line endings and set permissions
RUN dos2unix ./entrypoint.sh && \
  chmod +x ./entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]