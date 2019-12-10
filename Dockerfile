from alpine:latest

RUN apk add --no-cache python3-dev gcc musl-dev  && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN apk add --no-cache postgresql-libs && apk add --no-cache --virtual .build-deps postgresql-dev

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]

ENV PYTHONPATH="$PYTHONPATH:/app"
