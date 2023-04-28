# KenzieBUSTER

<h4>NOTE:</h4>

Through this repository, I present the final result of the project that I developed for KenzieAcademy.

As I developed my work from a fork of a private repository, I am unable to make public the entirety of my development process and code changes leading up to the final result. If you are interested in reviewing the complete development process of this project in the repository where I originally developed this work, please do not hesitate to contact me. It would be my pleasure to present it to you. For now, I am providing a general overview of the project's objectives, requirements, and stages, as well as the final version of the work that I completed.
#

<h4>MAIN OBJECTIVES</h4>

Develop an application to manage users, movies, and purchases, including authentication and route permissions for different types of users.
Have the application approved in all the previously prepared tests provided in the application's base repository.

*Note: The mentioned tests are included in this repository, and they come along with this final version of the project, so they can be downloaded and run locally. I provide instructions on how to run the tests locally at the end of this document.

<h4>MAJOR TECHNOLOGIES USED</h4>
Python, Django Rest Framework, JWT Authentication, SQLite3, Git.

<h4>INITIAL CHALLENGES</h4>
Setting up the project's structure, customizing the user model based on AbstractUser, registering models in Django Admin, creating conventional serializers, creating custom validation, overriding serializer methods, protecting routes with JWT authentication and custom Django Rest Framework permissions, creating a custom pivot table, creating choice fields for model attributes, implementing pagination with APIView.

<h4>METHODOLOGY</h4>
Use Django as the main framework to develop the application. Configuration of the structure, customization of the models, implementation of serializers, custom validation, route protection, pivot table, choice fields, and pagination. Use of Django Rest Framework tools and JWT authentication to protect routes and manage user permissions.


<h4>COMPLETE DEVELOPMENT REQUIREMENTS LIST</h4>

<h4>TASK 1:</h4>

Model User inheriting from AbstractUser with correct fields and rules.

Registration Serializer:
- Correct input and output fields
- Overridden .create method implemented correctly
- Correct unique message for email and username

POST /api/users/ creating non-employee
Creates non-employee with false superuser and returns status code 201.

POST /api/users/ with incorrect body returns required message.
All required fields correctly returned with status code 400.

POST /api/users/ with duplicated email/username returns correct message.
- Correct duplicated user message
- Correct duplicated email message


<h4>TASK 2:</h4>

Movie Model with correct fields and relationship with User.

Movie Serializer:
- Correct input and output fields
- Correct extra field added_by
- Overridden .create method implemented correctly

Login at /api/users/login/ returning valid JWT
Returns both access_token and refresh_token

Login at /api/users/login/ with username/password
Django's default message with status code 401

Login at /api/users/login/ missing fields
Correctly returned all required fields with status code 400

POST at /api/movies/ with employee token
Route protected for employee use only

POST at /api/movies/ with non-employee token
It should not be possible to create movies with a non-employee token

POST at /api/movies/ without token
It should not be possible to create movies without authentication

POST at /api/movies/ with correct token but wrong fields
Correct message about required fields returned.

GET at /api/movies/
Movies correctly returned without needing a token.

DELETE at /api/movies/:id/ with employee token
Movie deleted and correct message and status code returned

DELETE at /api/movies/:id/ with non-employee token
It should not be possible to delete a movie without being an employee.

DELETE at /api/movies/:id/ without token
It should not be possible to access the route without being authenticated.

GET at /api/movies/:id/ free for access.
Route open for access


<h4>TASK 3:</h4>

Customized MovieOrder pivot Model with correct attributes.

MovieOrder Serializer:
- Correct input and output fields
- Correct extra field buyed_by
- Overridden .create method implemented correctly

POST at /api/movies/:id/orders/ with employee token
Route protected for employee use only

POST at /api/movies/:id/orders/ with non-employee token
It should be possible to buy movies with a non-employee token

POST at /api/movies/:id/orders/ without token
It should not be possible to buy movies without authentication

POST at /api/movies/:id/orders/ with correct token but wrong fields
Correct message about required fields returned


<h4>TASK 4:</h4>

User Serializer with .update method
- Overridden .update method implemented correctly

GET at /api/users/:id/ without token
Access should not be allowed without authentication

GET at /api/users/:id/ with employee token
Employee should be able to access any profile information

GET at /api/users/:id/ with non-employee token
Non-employee should only be able to access their own profile information

PATCH at /api/users/:id/ without token
Access should not be allowed without authentication

PATCH at /api/users/:id/ with employee token
Employee should be able to update any profile information

PATCH at /api/users/:id/ with non-employee token
Non-employee should only be able to update their own profile information

GET at /api/movies/ with pagination
Pagination with 2 items per page

Best practices:
- Correct syntax
- gitignore
- requirements.txt
- Each task must have a commit following the commit standardization request (task x: completed).



<!-- 



# M5 - Kenzie Buster

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate

# git bash:
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

5. Vá até o arquivo `pytest.ini` e modifique o nome do projeto `my_project_name.settings` para o nome do **seu_projeto**.settings (onde se encontra o settings.py)

4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```



## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes da Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes da Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes da Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```


-->
