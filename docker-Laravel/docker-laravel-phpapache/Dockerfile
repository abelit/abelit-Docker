FROM php:5.6.25-apache

MAINTAINER "Abelit" <ychenid@live.com>
RUN sed -i 's/httpredir.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com\/debian-security/g' /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y \
    php5-gd \
    php5-mysqlnd \
    php5-mcrypt && \
    apt-get clean
RUN docker-php-ext-install pdo pdo_mysql
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load
RUN sed -i 's/\/var\/www\/html/\/data\/www\/public/g' /etc/apache2/sites-enabled/000-default.conf && \
    sed -i 's/<Directory \/var\/www\/>/<Directory \/data\/www\/>/g' /etc/apache2/apache2.conf && \
    sed -i '166s/None/All/' /etc/apache2/apache2.conf
RUN mkdir -p /data/www && \
    chown -R www-data:www-data /data/www
VOLUME ["/data"]
WORKDIR /data/www
