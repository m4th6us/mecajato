# Mecajato

Esse projeto foi desenvolvido para fins acadêmicos, apenas para estudar os conceitos do Django e explorar esse framework, com a ajuda dessa [playlist](https://youtube.com/playlist?list=PL3gEA6Xsr_enTjEeyAyLrqdJmEFM8FvwM&si=V4HLpHVrr18v8ZFh)

# Como rodar o projeto

O projeto possui um **Dockerfile** dentro de **build/dev** que já está configurado com as depedências do projeto.
Para buildar sua imagem e subir a aplicação, temos um **docker-compose.yml** na mesma pasta, o comando necessário para subir a aplicação é esse abaixo:

**build** se a aplicação ainda não estiver rodando

    docker compose build

**up** se a aplicação já teve **build**

    docker compose up

junção dos comandos:

    docker compose up --build

Lembrando que é necessário ter instalador o **Docker** e o **Docker compose** em sua máquina para os comandos funcionarem.