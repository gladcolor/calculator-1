FROM python:3.6

ADD . .

RUN pip install --upgrade pip

CMD ["python", "-m", "unittest", "discover", "-s","Tests"]