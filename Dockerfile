FROM python:3.13.2

WORKDIR /hiragana_katakana_learn_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
