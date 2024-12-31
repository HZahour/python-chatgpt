FROM python:latest

# Install dependencies
RUN python -m pip install --upgrade pip \
    && pip install openai python-dotenv

WORKDIR /usr/src/app

# command to keep the container running
CMD tail -f /dev/null