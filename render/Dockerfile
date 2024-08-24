FROM rust:1.80.0 as builder
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN cargo build --release

FROM debian:bookworm-slim
RUN apt-get update && \
    apt-get install -y openssl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/esp-render /usr/local/bin/esp-render
COPY entrypoint.sh /usr/local/bin/entrypoint.sh 
RUN chmod +x /usr/local/bin/esp-render 
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN mkdir -p /out
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
