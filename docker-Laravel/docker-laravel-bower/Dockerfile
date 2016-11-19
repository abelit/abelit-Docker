FROM debian:latest

MAINTAINER "Abelit" <ychenid@live.com>

WORKDIR /tmp

RUN sed -i 's/httpredir.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com\/debian-security/g' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y curl git && \
    curl -sL https://deb.nodesource.com/setup | bash -  && \
    apt-get install -y nodejs  && \
    apt-get remove --purge curl -y  && \
    apt-get clean  && \
    npm install -g bower

# For some strange reason Bower doesn't like running
# without a /var/www directory! Even if we're running
# it from a completely different directory! Strange!?
RUN mkdir -p /data/www /var/www && \
    chown www-data:www-data /var/www
VOLUME ["/data"]
WORKDIR /data/www

USER www-data

ENTRYPOINT ["bower"]
CMD ["help"]
