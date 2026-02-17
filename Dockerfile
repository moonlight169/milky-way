FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# พอร์ต 8080 คือพอร์ตมาตรฐานของ Google Cloud Run
CMD python train.py && uvicorn main:app --host 0.0.0.0 --port 8080