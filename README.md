# wlke

wlke (cloud = wolke in german) is a Python Django created Cloud solution for self-hosting. In this Project we want to improof our python - django skills.

## tools

This project is written in Python 3 and HTML. The frameworks that are used are Django for Python and the backend and Bootstrap4 for the frontend.

## try this project

To test this project, simpy clone it an navigate into the wlke folder. If you are there, you can launch the development-server with `python manage.py runserver` on Windows or with `python3 manage.py runserver` on Linux or MacOS.

## use our build virtualenviroment

#### Attention: to make this work, we recommend on Windows to use Git Bash as terminal!!

1. open the terminal in the directory, where also the `README.md` ist stored (main directory)
2. on Windows type `python -m venv env` in the terminal | on MacOS/Linux type in your terminal `python3 -venv env`
3. on Windows (Git Bash) and MacOS type in your terminal `source env/Scripts/activate`
4. then enter the command `pip installl -r wlke/requirements.txt`
5. Now you can select in the open folder in VS Code the virtual-enviroment `env` as python-interpreter

# How to contribute

You can support and contribute us by making pull requests and open issues that we can now how we can improve our webapp. 

## security

This project is actually in the development stage. This means, that it isn't suitable for production. But if you use it now in production, we don't guarantee for the security and the whole functionallity of the project and we don't give you any liability.

## production use

To use this in production, we highly recommend to use Docker. To build a image, you can find a `Dockerfile` in the `wlke` folder; simpy navigate with your terminal in this folder and build with `docker build .` your image for docker.

#### Attention: you have to install docker on your machine to make this work! Also we recommend to turn debug of at `settings.py` before use this for productio!
