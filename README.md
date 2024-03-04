
This is the server side ( back-end project ) of my personal portfolio build with python [ [Flask](https://flask.palletsprojects.com/en/3.0.x/) ] and some extra tools.

<hr>

#### Install

First you have to install this repo on your local machine with this command :

```bash
git clone https://github.com/touzand/portafolio-serverside.git
```

Next, go inside the folder with using the **cd** command. for example :

```bash
cd C:/<your_user>/desktop/portafolio-serverside/
```

Then you can now create an environment to install all the dependencies inside this folder and don't have nothing installed out of it. you can do it by typing :

**macOS / Linux**
```bash
python3 -m venv .venv
```

**Windows**
```bash
py -3 -m venv .venv
```

and then :


**macOS / Linux**
```bash
. .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```


Now you can start downloading the dependencies of this project by simple typing :

```bash
pip install -r requeriments.py
```

<hr>

And there you have it. now you can init the local server by typing :

```
flask --app __init__ run
```

So the server will be runing on the port [ http://127.0.0.1:5000/ ](http://127.0.0.1:5000). now you can see it working normally on the front-end of my portafolio. if you still dont have it runing or even know how to isntall it. you can go to [portafolio](https://github.com/touzand/portafolio)

> tutorial only for analitic and code reviewers

