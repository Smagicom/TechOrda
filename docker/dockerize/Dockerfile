FROM python:3.8
WORKDIR /opt
COPY main.py /opt/
RUN pip3 install fastapi uvicorn
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]