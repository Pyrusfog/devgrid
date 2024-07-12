FROM python:3.10

# Verifique a versão do pip
RUN pip --version

WORKDIR /app
# Adicione o script app.py
COPY . /app

# Instale o Flask
RUN pip install Flask
RUN pip install requests
RUN pip install python-dotenv
RUN pip install aiohttp
RUN pip install pytest

CMD ["python", "./app.py"]
