FROM python:3.11
COPY . ./app
WORKDIR /app
RUN pip3 install -r ./requirements.txt
COPY score.txt /Score
ENV FLASK_APP=MainScores.py
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
