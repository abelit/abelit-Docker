# docker-laravel

## Usage
1. 使用docker-compose启动相关容器，"-d"表示在后台运行
> docker-compose up -d

2. 运行容器composer创建laravel项目
> docker-compose run --rm composer create-project laravel/laravel /data/www --prefer-dist

3. 运行容器artisan来使用artisan相关命令
> docker-compose run --rm artisan {command}
