# Logtail Python

Collect logs directly from any Python code, including Django.

**Supported language version:**
- Python 3.6.5 or newer
- `pip` 20.0.2 or newer

To learn more about Logtail and python, visit our [official docs](https://logtail-main.readme.io/docs/installing-logtail).

# Installation

You can install the Logtail python client library using the `pip` command as you would with any other package.

## Install `pip`

`pip` is a package installer for python. You can install `pip` by following the [official installation guide](https://pip.pypa.io/en/stable/installation/).

## Install Logtail client library

To install the client library, run the following command:

```bash
pip install logtail-python
```

# Example project

To help you get started with using Logtail in your Python projects, we have prepared a simple python program that showcases the usage of Logtail logger in Python code.

## Download the example project

You can download the example project from GitHub directly or you can clone it to a select directory.

Then install the `logtail-python` client library as shown before:

```bash
pip install logtail-python
```

## Run the example project

To run the example application, simply run the following command:

```bash
python main.py <source-token>
```

Don't forget to replace `<source-token>` with your actual source toke which you can find in the source settings.

If you have trouble running the command above, check your Python installation and try running it with the `python3` command instead.

You should see the following output:

```
Output:
All done! You can check your logs now.
```

This will create a total of 6 logs. Each corresponds to its respective method.

