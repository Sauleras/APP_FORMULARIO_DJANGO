# APP_FORMULARIO_DJANGO
Formulario simples feito com Html, Bootstrap e Django. O intuito deste projeto é estudar e treinar sobre criação de formularios e o metodo CRUD, utilizando o banco de dados PostgresSQL.

<strong>Tela Inicial</strong>
![image](https://user-images.githubusercontent.com/91494533/180869731-8f97fce4-ac61-46cc-b6d4-e082c377b5b3.png)

<strong>Tela de cadastro de usuario</strong>
![image](https://user-images.githubusercontent.com/91494533/180869815-b8f605cc-b5e3-4118-88d1-9b23f71330a2.png)

<strong>Tela de login do usuario</strong>
![image](https://user-images.githubusercontent.com/91494533/180869860-67ad81a5-1429-437c-b8e2-21de6978cfa7.png)

<strong>Tela inicial apos o login</strong>
![image](https://user-images.githubusercontent.com/91494533/180869958-17c7d90a-44c5-42d8-9510-6ca51d187c98.png)

<strong>Tela de cadastro de produto</strong>
![image](https://user-images.githubusercontent.com/91494533/180870044-29df8e87-05d3-43cb-a924-4c8ceb50afd2.png)

<strong>Tela de edição de produto</strong>
![image](https://user-images.githubusercontent.com/91494533/180870149-02974c88-d278-4672-8013-ac02839161aa.png)

<strong>Tela de exclusão de produto</strong>
![image](https://user-images.githubusercontent.com/91494533/180870201-4c5a7bf9-90bd-4340-9478-a7db10b1d5bf.png)


# Pre-Requisitos
Instalar o Python na sua maquina -> https://www.python.org/downloads/

# Criando o ambiente virtual
<strong>Apos a instalação do python abra o terminal na pasta do projeto e crie um ambiente virtual</strong>

![image](https://user-images.githubusercontent.com/91494533/180862194-f2c69639-3a45-4163-a2b2-9655c9f30a94.png)

<strong>Em seguida o ative</strong>

![image](https://user-images.githubusercontent.com/91494533/180862493-51acc222-2028-4269-b56c-ec43feb53d36.png)

<strong>Caso funcione o nome do ambiente virtual vai aparecer ao lado esquerdo do diretorio</strong>

![image](https://user-images.githubusercontent.com/91494533/180862759-d0b58cc2-e1ae-41c8-be3f-c40fc67d9cc6.png)

# Instalação e Como Rodar o Projeto
<strong>É necessário instalar todos os pacotes do arquivo "requirements.txt", para isso utilize o comando "pip install -r requirements.txt"</strong>

![image](https://user-images.githubusercontent.com/91494533/180864494-9d485381-0647-4a11-ab2d-4979b7ca7bb8.png)

<strong>Feita a instalação é necessário configurar o seu banco de dados</strong>

Abra a pasta "form_django" do projeto, depois abra o arquivo "settings.py" e procure por "DATABASES"

Caso não deseje utilizar o Postgres, você pode descomentar a opção de sqlite que é o banco de dados padrão que já vem no pacote do Django.

![image](https://user-images.githubusercontent.com/91494533/180867607-5b4e9d8e-e85e-48a1-bc62-ffba1a85a918.png)

Utilize o comando "python manage.py makemigrations" e logo em seguida o comando "python manage.py migrate" para que seja salvo as configurações de tabelas do banco de dados.

![image](https://user-images.githubusercontent.com/91494533/180868634-97b696b6-34a0-4f92-af59-0458a3679961.png)

![image](https://user-images.githubusercontent.com/91494533/180868680-930e003d-e637-433b-b5f0-2b639f1a2ebe.png)

<strong>A sua aplicação deve estar toda configurada, agora utilize o comando "python manage.py runserver" para rodar a aplicação no host local.</strong>

![image](https://user-images.githubusercontent.com/91494533/180869060-28ac44b0-19f4-466e-a269-8d19756b9cbd.png)

![image](https://user-images.githubusercontent.com/91494533/180869484-f170976e-5f6f-46d6-8eb7-4cea10962c46.png)
