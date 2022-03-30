# Não precisa de extensão, se tiver só 1 arquivo docker, usar o nome de dockerfile
# De nginx instalar a versão 1.19 alpine
FROM nginx:1.19-alpine
# Autor
LABEL maintainer = "José Victor <josevictorcomrc@gmail.com>"
# Copia de um lugar pro outro, poderia selecionar só um arquivo colocando index.html ao invés de '.'
COPY . /usr/share/nginx/html
# Expõe a porta 80
EXPOSE 80

# docker build -f .\Dockerfile -t josevictornasilva/servidor_web:v1 . -> builda
# -f -> Informa um nome do dockerfile
# -t -> Cria uma tag pra imagem
# josevictornogueira/servidor_web -> meu nome no docker/nome da imagem
# :v1 -> Tag
# . -> Onde está o arquivo, no caso, está no mesmo diretório 
# docker login --username:
# docker image push josevictorna/servidor_web:v1