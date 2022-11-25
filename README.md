# Numerical Analysis

## JABA proyect

### How to install

1. Install [python](https://www.python.org/downloads/)
2. Clone the proyect

```git
git clone https://github.com/bened18/numerical-analysis.git
```

3. Create a virtual environment for the project

```console
python -m venv venvName
```

4. Activate the virtual environment

- Go to the environment path
- Scripts
- Open console here

```console
activate
```

5. Install the dependencies

- With the venv activated
- Go to the project path
- Use pip

```console
pip install -r requirements.txt
```

6. Configure the settings.py

- Go to app_core_numericalanalysis
- Edit the settings.py
- BASE_URL can be: BASE_URL = "http://localhost" or BASE_URL = "https://domain.com"
- ALLOWED_HOSTS can be: ALLOWED_HOSTS = ["localhost", "*", "domain.com"]
- Can add another config of database consult [django documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#databases)

7. Make the migrations

```console
python manage.py migrate
```

8. Run the proyect

```console
python manage.py runserver
```

- If you want to deploy the local server in another port or url

```console
python manage.py runserver localhost:8000
```

```console
python manage.py runserver 192.168.x.x:8000
```

### User manual
- [See](https://www.youtube.com/watch?v=QOztrMcN2Q8&ab_channel=Benjamindelatorre)

### Members
* Andrés Guerra Montoya
* Benjamin Eduardo de la Torre Rojas
* Antonio Carmona Gaviria
* Juan Esteban Cardona Ospina

### Technologies
- [Python](https://www.python.org/about/gettingstarted/)
- [Django](https://www.djangoproject.com/)
- [mpmath](https://mpmath.org/)
- [numpy](https://numpy.org/)
- [scitools3](https://pypi.org/project/scitools3/)
- [sympy](https://www.sympy.org/en/)
- [tabulate](https://pypi.org/project/tabulate/)

### Host
- [PythonAnywhere](https://www.pythonanywhere.com/)

### Example of the project
- [website](https://bened18.pythonanywhere.com/)