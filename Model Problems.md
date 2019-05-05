# What model can solve these problems?


## Problem 1
_Predict the running times of prospective Olympic sprinters using data from the last 20 Olympics._


One way we could solve this is using regression model. We could use a linear regression model to predict the running times as they are continuous outcome. We could also use some other variations, such as Ridge if we'd like to regularize for the test case. If we had a large amount of features, such as amount of water drank, BMI, air pressure, ambient temperature, sneaker friction coefficient, height, weight, age, etc, we could use another linear approach like Lasso to perform feature selection as well as regularization.

For the most part, we can assume that most of the features will be correlated in one way or another, and won't be entirely independent. The advantage of using a linear model is that we have a great amount of explanatory power. I.e. we can tell exactly what features are the most predictive, as well as how much.


Another set of models we could run would be an RandomForrest approach. The RandomForrest approach has a few downsides, one being that the bounds for the regression will only be within the space it has seen. For example, if the max value passed to the regression was 30s, and the min was 10s, the model would not be able to predict outside those bounds. The second downside is the loss of explanatory power. The decision tree follows random paths to minimize the entropy in the tree, vs a regression line that follows a strict mathematical formula that can be interpreted. A RandomForrest might still provide some value in determining how much potential variance can be explained from the data provided.

## Problem 2
_You have more features (columns) than rows in your dataset._


One approach I can think of is some sort of dimensionality reduction like PCA. I'm not sure of the negative side effects of PCA on a dataset like this, but let's just throw it out there.


The other approach I can think of is Lasso regression (in the case of a regression problem). Lasso is L1 regularization and will sum the absolute value of the coefficients to create a penalty, making irrelevant coefficients "fade away". Lasso also has the added bonus of under fitting the training set to trade for a better test score.

## Problem 3
_Identify the most important characteristic predicting likelihood of being jailed before age 20._

The first thing that comes to mind is using an ensemble model and from that model returning the features with highest relative feature importance.

The other approach would be to find the coefficients with the highest value after fitting the model to the data.

## Problem 4

_Implement a filter to “highlight” emails that might be important to the recipient_

For this I'd use an NLP approach with a Bayesian classification model. We could assume the words in the email are independent from each other, which would satisfy the constraint of the Bayesian model. We could do a binary classification model with this. 0 for not important, 1 for important.

## Problem 5

_You have 1000+ features._

Cry? I don't really know. I'm guessing one thing you could do is to do dimensionality reduction with PCA because only god knows how long that matrix will take to run through a model. You might have to use some domain knowledge to refine the feature space, and then compare it against PCA model results.

## Problem 6

_Predict whether someone who adds items to their cart on a website will purchase the items._


This is cool because we'll require lots of previous data. I would use a regression approach like Logistic Regression. We could have data points like session duration after adding to cart, and other data points like if the user has purchased before, etc.


## Problem 7

_Your dataset dimensions are 982400 x 500_

Try PCA first if you just care about prediction. To run this would require a model that could be parallelized. This is pretty ambiguous as I don't know much about the content of the data.


## Problem 8

_Identify faces in an image._

DCNN. We could use SVD or something to that effect. Maybe PCA or another downsampling technique.

## Problem 9
_Predict which of three flavors of ice cream will be most popular with boys vs girls._

Multi-class logistic regression or a naive Bayes model maybe? Features would be maybe other favorite foods, whether or not they're a boy or a girl, age, favorite color, etc.
