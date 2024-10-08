FROM python:3.10.13

WORKDIR /workspace

RUN mkdir -p $WORKDIR/volume
RUN mkdir -p $WORKDIR/volume-test

COPY app.py requirements.txt ./

RUN  pip install -r requirements.txt

CMD ["python", "app.py"]
