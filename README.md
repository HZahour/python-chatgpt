# ChatGPT for Python
It will run on the docker container and response of your queries using OpenAI API.

Syntax:
docker exec python-chatgpt python main.py How are you?

### Instructions
- Rename the ./app/example.env to .env
- Enter OpenAI API Key in .env file

### Commands
To run the container
- docker compose up -d

To get the ChatGPT message
- docker exec python-chatgpt python main.py How are you?