Djanog のマルチテナントサンプルです.

## usage

```console
# .env の作成
cp sample.env .env

# docker コンテナ起動
docker-compose up -d

# docker コンテナに入る
docker exec -it multi-tenant-django bash

# コンテナ内 で runserver
[root@724ec4f18373 django]# python manage.py runserver
```
