FROM python:3.12.5-slim-bookworm

COPY src /src
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/src/app.py"]