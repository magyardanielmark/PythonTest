FROM python:3.9.19-alpine3.19

WORKDIR /app

COPY app.py requirements.txt start.sh /app/

RUN chmod +x start.sh

RUN pip3 install -r requirements.txt

EXPOSE 80

RUN apk add nginx

COPY nginx.conf /etc/nginx/nginx.conf

CMD ["/app/start.sh"]
