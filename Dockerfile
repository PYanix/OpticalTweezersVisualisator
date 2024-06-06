# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m uvicorn main:app --reload"]
CMD [ "python3", "-m streamlit run app.py"]
