FROM python:alpine
RUN pip install redis
RUN pip install requests
COPY broker.py /
CMD ["python", "broker.py"]
