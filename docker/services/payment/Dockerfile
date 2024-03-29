# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.12.1
FROM python:${PYTHON_VERSION}-alpine as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Required for the djnago-configuration library
ENV DJANGO_SETTINGS_MODULE "src.settings"

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    django

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Creating folder for gunicorn logs.
RUN mkdir /var/log/gunicorn

# Granting log permissions to non-privileged user.
RUN chown -R django:django /var/log/gunicorn

# Switch to the non-privileged user to run the application.
USER django

# Copy the source code into the container.
COPY --chown=django:django . .

# Expose the port that the application listens on.
EXPOSE 8002

# Run the application.
CMD ["gunicorn", "-c", "/app/gunicorn.conf.py", "src.wsgi"]
