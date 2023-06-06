# DistributionGenerator
Part of simulation laboratory assignment № 14. 

## Description
In this project we are creating an API to generate random variable using [Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution) and [Exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution) from [numpy](https://numpy.org/) library. Later the API will be used by [Bank Simulation Mobile App](https://github.com/Steven2110/BankSimulation) to generate random variable to simulate bank queueing system.

## How to deploy API:
1. Install all requirements from `requirements.txt` using this command `pip install -r requirements.txt`. Wait until all required libraries finished installed.
2. Run this command `python3 main.py`, wait until you see text that says `* Running on http://127.0.0.1:5000` then you can open that link from your browser, and you will see text `Hello World!` printed on the browser screen.
3. There are two routes to generate random variable with different distribution:
    1. Open this route `/poisson` and add your integer value for `lambda` as URL parameters like this: `http://127.0.0.1:5000/predict?lambda=[int value]`. You can use this link as an example: `http://127.0.0.1:5000/poisson?lambda=5`
    2. Open this route `/exponential` for generating random variable using exponential distribution and add your floating value for `lambda` as URL parameters like this: `http://127.0.0.1:5000/exponential?lambda=[floating value]`. You can use this link as an example: `http://127.0.0.1:5000/exponential?lambda=10.0`