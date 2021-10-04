FROM python:3.9.5-buster

EXPOSE 8080

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8


RUN pip3 install Flask gunicorn numpy nltk spacy bs4 regex anonymization

RUN python -m spacy download fr_core_news_sm

COPY src/* /app/src/
COPY server.py /app/server.py

WORKDIR /app

ENV PYTHONHASHSEED=42

CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "1", "--timeout", "300", "--access-logfile",  "-", "server:app"]

