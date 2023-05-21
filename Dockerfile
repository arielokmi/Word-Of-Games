FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . ./app
WORKDIR /app
ENV FLASK_APP=MainScores.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]

