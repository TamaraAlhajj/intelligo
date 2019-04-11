# INTELLIGO

## Understanding Complexity

_A web app to aid in understanding of asymptotic complexity theory, for my undergraduate honours project._

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

- Python3.7 for mathematics backend-logic layer
- Django Python Web framework for Model and View
- Bootstrap for frontend (UI layer)
- `graphviz` python library for recussion tree visualization
- `numpy` and `sympy` for computing calculus
- Tested in Brave and Chrome browsers
