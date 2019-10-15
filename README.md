# rich-ipyprompt

A better prompt for IPython interactive shell.


## Features

- Adds the current path if it changes from the default
- Replaces the less useful `In[x]:` prompt (we keep the `Out[x]`, which you are more likely to want to reference) with the classic `>>>`.
- Formats the vi mode nicely if vi mode is set
- Adds the execution time for the previous command if above a minimum delta (by default 5).


## Quickstart

To easily get the theme installed and loading at startup:

```shell
pip install richprompt[hook]
python -m ipython_startup_hook.install
```


## Installation

Install using [`pip`](https://pip.pypa.io/en/stable/):

```shell
pip install richprompt 
```

or with [`conda`](https://conda.io):

```shell
conda install -c lewisacidic richprompt
```

## Usage

Load the prompt with IPython magic:

```shell
%load_ext richprompt
```

To set the prompt back to what you had previously:

```shell
%unload_ext richprompt
```


## Running this at startup

You can either put the following snippet in your IPython startup directory (usually `$HOME/.ipython/profile_default/startup`):

```shell
try:
    from richprompt.startup import load
    load()
    del load  # don't pollute global namespace!!
except ModuleNotFoundError:
    pass
```

Or use [`ipython-startup-hook`](https://github.com/lewisacidic/ipython-startup-hook) (recommended if you use IPython within virtual or conda environments).

This may be done at install with the command given in the [Quickstart](#quickstart).


## Development 

Create the conda environment:

```shell
conda env create -f envs/dev.yml
conda activate richprompt-dev
```

Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

Run the tests with pytest (note we need to use `ipython` rather than `python` for these tests as we need the IPython runtime):

```shell
ipython -m pytest
```
