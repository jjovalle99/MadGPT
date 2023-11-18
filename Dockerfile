FROM python:3.10.13-slim

RUN useradd -m user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR $HOME/app
COPY --chown=user ./ ./

RUN pip install poetry==1.6.1 --no-cache-dir && \
touch README.md && \
poetry install --only main \
--no-interaction \
--no-ansi \
--no-cache

EXPOSE 7860

ENTRYPOINT ["poetry", "run", "chainlit", "run", "-w", "--host", "0.0.0.0", "--port", "7860", "app.py"]