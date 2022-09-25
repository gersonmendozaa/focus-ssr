FROM python:3.8-slim-buster

RUN adduser --system worker
USER worker
WORKDIR /home/worker/app

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY --chown=worker:worker . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]