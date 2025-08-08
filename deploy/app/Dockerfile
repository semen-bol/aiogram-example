FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt && rm requirements.txt
COPY /bot /app/bot

CMD ["python", "-m", "bot.main"]
