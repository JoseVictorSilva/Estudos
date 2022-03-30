FROM python:3.9.0-alpine
LABEL maintainer = "José Victor <josevictorcomrc@gmail.com>"
COPY . /var/www
# Diretório funcional
WORKDIR /var/www
# Está rodando comando: 
# apk update: Atualiza o repositório do alpine (só apk se for alpine)
# apk add: instala esses pacotes que precisam ter
# pip instal o que tiver no arquivo requirements
# pyton manage.py migrate: cria o banco
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev && pip install -r requirements.txt && python manage.py migrate
# Quando finalizar o arquivo, o que o workdir deve executar
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
EXPOSE 8000 