# comment next line for testing
#FROM nvidia/cuda:12.1.1-runtime-ubuntu20.04
FROM python:3.10.13

WORKDIR /workspace

RUN mkdir -p $WORKDIR/volume
RUN mkdir -p $WORKDIR/volume-test

COPY app.py requirements.txt ./

#RUN --mount=type=cache,target=/root/.cache/pip \
#    pip install -r requirements.txt

RUN  pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python", "app.py"]

# by default out build function will add or replace entrypoint
# even if you set an entrypoint

