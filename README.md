#predicting_stock_prices
Stock Prediction Challenge by @Sirajology on [Youtube](https://youtu.be/SSu00IRRraY).

##Overview

This is the code for the Stock Price Prediction challenge for 'Learn Python for Data Science #3' by @Sirajology on [YouTube](https://youtu.be/SSu00IRRraY). The code uses the [scikit-learn](https://github.com/scikit-learn/scikit-learn) machine learning library to train a [support vector regression](https://en.wikipedia.org/wiki/Support_vector_machine) on a stock price dataset from [Google Finance](https://en.wikipedia.org/wiki/Support_vector_machine) to predict a future price. In the video, I use scikit-learn to build an ML model, but for the challenge you'll use the [Keras](https://keras.io) library.

There are two scripts. `demo.py` is the code in the video and `challenge.py` is a template for the coding challenge you will complete.

##Dependencies

* numpy (http://www.numpy.org/)
* tweepy (http://www.tweepy.org)
* csv (https://pypi.python.org/pypi/csv)
* textblob (https://textblob.readthedocs.io/en/dev/)
* keras (https://keras.io)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

##Demo Usage

Once you have your dependencies installed via pip, run the demo script in terminal via

```
python demo.py
```

##Challenge 

You'll find the challenge template in this repo labeled `challenge.py`. The instructions are 

1. Use the Tweepy library to retrieve tweets about a company stock from twitter
2. Use the TextBlob library to classify those tweets as either positive or negative given a threshold you define.
3. If the majority of tweets are positive, then use the Keras library to build a neural network that predicts the next stock price given a dataset of past stock prices that you pull from Google Finance. [This](http://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras/) tutorial may be useful to you. 

If you want to use your own template, that's fine too. Submit your code in the comments section and I'll announce the winner in
the next video. Good luck!

##Credits

This code is 100% Siraj
