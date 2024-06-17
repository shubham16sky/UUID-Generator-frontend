FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -c "import streamlit; print(streamlit.__version__)"

COPY . .

EXPOSE 8081

CMD ["python3", "-m", "streamlit", "run", "app/app.py", "--server.port", "8081"]
