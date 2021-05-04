# Chatbot Workshop, May 2021

## This repo contains the following:

### Prerequisites

[Please have a look at these](prerequisites.md) and ensure you have the correct software installed on your machine ahead of the workshop.

### Code for the first version of the chatbot

We will be building a chatbot in stages as the workshops progress.  [The code in this repo](flask-bot) relates to the version we will build in the May workshop.

[See the bot in action online](https://wrap-bot.herokuapp.com/), or download the code and run it on your machine.

Tto run the bot on your machine, first ensure you have all the software [prerequisites](prerequisites.md).

You will also need some proficiency with the command line.

To download the files:

* Click the green Code button at the top right.
* Select the Download ZIP option.
* Once the zip file has downloaded, unzip that folder.
* Using the command line, navigate into the folder that the unzip created - you should be able to see all the files.

Now type the following in the command line:

```
$ cd flask-bot
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_ENV=development
$ export FLASK_APP=bot.py
$ flask run --host=0.0.0.0 --extra-files participants.json
```

## What we will cover in this workshop

Here is an overview.  I will provide bespoke learning materials on the day.

### Fundamentals of JavaScript

We will go through some basic principles of the JavaScript programming language.

If you would like to do some learning ahead of the workshop, [freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) has some excellent tutorials.

### Fundamentals of Python

We will go through some basic principles of the JavaScript programming language.

If you would like to do some learning ahead of the workshop, [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/) has some excellent tutorials.

### Building a feminist chatbot using JavaScript and Python

We will look at how to use JavaScript and Python together to build a chatbot application.  The chatbot will take text inputs from the user and respond with information from the database.

We will also look at the type of work we need to do to improve the data to provide a better, more natural experience for the user.
