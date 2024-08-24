FROM python:3.12-alpine

# Install system dependencies required for Pillow:
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers
RUN mkdir -p /app
RUN mkdir -p /out
COPY . /app
WORKDIR /app
RUN chmod +x /app/entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/app/entrypoint.sh"]
