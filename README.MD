# INTELLIGO

## Complexity Theory Tool 
_A web app to aid in understanding of asymptotic complexity theory, for my undergraduate honours project._
Built with `Django`, `Python`, `Heroku`, \& `Bootstrap`.

### Overview
Web app built for visualizing and learning about discrete maths, which gives thorough solutions to problems using asymptotic notation and graphs.
User may enter an equation for `f(n)`, which will generate the `big-O` & `big-Omega` solutions using the limit as n grows to infty of `f(n)/g(n)`.
Alternatively, user may enter a for divide-and-conquer recurrence, `T(n)`, which will generate the asymptotic analysis using the Master's Method.
To complement the output of the Master's Method, the corresponding recursion tree for `T(n)` is generated dynamically, as a visual learning aid for the user.

## Install Anaconda

To get the Anaconda 2019.03 for installer go to `https://www.anaconda.com/distribution/` and click on the installer for your OS.
Then [follow the instructions](https://docs.anaconda.com/anaconda/install/), for the OS you have chosen.

## Requirements

To install requirements run,

```bash
pip3 install Django anytree
conda install -c anaconda graphviz python-graphviz numpy sympy
```

## Run

Then to launch the site,

`python3 manage.py runserver`

## Development

- Python3 for mathematics backend-logic layer
- Django Python Web framework for Model and View
- Bootstrap for frontend (UI layer)
- `graphviz` python library for recursion tree visualization
- `numpy` and `sympy` for computing calculus
- Tested in Brave and Chrome browsers
