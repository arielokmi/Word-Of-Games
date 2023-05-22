FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./app
WORKDIR /app
RUN apt-get update && apt-get install -y \
     curl \
     unzip \
     wget

RUN wget -q https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

ENV FLASK_APP=MainScores.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]

