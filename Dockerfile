FROM python:3.12.2-slim

# Set the working directory in the container
ARG USER=btc
ARG GROUP=app
ARG PORT=8000

# Create a group and user
RUN groupadd -r ${GROUP} && useradd -m -r -g ${GROUP} ${USER}

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN chown -R ${USER}:${GROUP} /app
USER ${USER}

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN python -m poetry install

# Create the directory
EXPOSE ${PORT}

CMD ["python", "-m", "poetry", "run", "python", "-m", "uvicorn", "btc_app.app:app", "--reload", "--host", "0.0.0.0"]
