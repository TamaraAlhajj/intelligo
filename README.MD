# INTELLIGO

## Understanding Complexity

_A web app to aid in understanding of asymptotic complexity theory, for my undergraduate honours project._

## Install Anaconda 

From the working directory of this project run,

`bash Anaconda3-2019.x-Linux-x86[_64].sh`

When installing anaconda scroll to the bottom of the license terms and enter `yes` to agree.

Then accept the default install location by clicking Enter.

Once the installer prompts to prepend the Anaconda install location to PATH .bashrc, enter `yes`

When the installation completes type `source ~/.bashrc`, and verify by typeing `anaconda-navigator`

## Requirements

To install requirements run,

```bash
pip3 install Django anytree
conda install -c anaconda graphviz python-graphviz numpy
```

## Run

Then to launch the site,

`python3 manage.py runserver`

## Development

- Python3.7 for mathematics backend-logic layer
- Django Python Web framework for Model and View
- Bootstrap for frontend (UI layer)
- `graphviz` python library for recussion tree visualization
- `numpy` for computing calculus
- Tested in Brave and Chrome browsers
