# PyTorch
FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime

# Temporary
ARG GID=3333
ARG UID=$GID

# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
COPY .devcontainer/requirements.txt /app
RUN groupadd --system readers --gid $GID && \
    useradd --system automata --uid $UID --gid $GID && \
    pip install --upgrade pip && \
    pip install --requirement /app/requirements.txt --no-cache-dir

# Specific COPY
COPY src /app/src

# Port
EXPOSE 8050

# Reader
USER automata

# ENTRYPOINT
ENTRYPOINT ["python"]

# CMD
CMD ["src/main.py"]