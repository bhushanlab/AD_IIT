import math
from IPython import display
from matplotlib import cm, gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset


def my_input_function(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """
    what this function does it to train a linear regression model of one feature
    Args:
        1. features: pandas dataframe of features
        2. target pandas dataframe of targets
        3. batch_size: size of batches to be passed to the model
        4. shuffle: T or F. to shuffle or not to shuffle
        5. num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
        1. the Tuple of (features, labels) for next data batch    
    """
    # convert pandas data into a dict of np arrays
    features = {key: np.array(value) for key, value in dict(features).items()}
    # construct a dataset, and configure batching/repeating
    ds = Dataset.from_tensor_slices((features, targets))
    ds = ds.batch(batch_size).repeat(num_epochs)
    # shuffle the data, if specified
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)
    # return the next batch of data
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv(
    "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv",
    sep=",")

california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0

# a demo of printing out the data
print(california_housing_dataframe)

# after we get our hands on the data we can exam it
# this is the pandas function we learned previously
print(california_housing_dataframe.describe())

## The building of the first model
## The feature column
# define the input feature: total room
my_feature = california_housing_dataframe[['total_rooms']]
# configure a numeric feature column for total_rooms
feature_columns = [tf.feature_column.numeric_column("total_rooms")]

## now we define the target
# define the label 
target = california_housing_dataframe["median_house_value"]

# Use gradient descent as the optimizer for training
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer,5.0)

# Configure the linear regression model with our feature columns and optimizer
# set a learning rate of 0.0000001 for the gradient desent
linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns,optimizer=my_optimizer)

#traning, using the my_input_func()
linear_regressor.train(input_fn = lambda:my_input_function(my_feature,target), steps = 100)

# Create an input function for predictions.
# Note: Since we're making just one prediction for each example, we don't
# need to repeat or shuffle the data here.
def prediction_input_fn(): return my_input_function(
    my_feature, target, num_epochs=1, shuffle=False)


# Call predict() on the linear_regressor to make predictions.
predictions = linear_regressor.predict(input_fn=prediction_input_fn)

# Format predictions as a NumPy array, so we can calculate error metrics.
predictions = np.array([item['predictions'][0] for item in predictions])

# Print Mean Squared Error and Root Mean Squared Error.
mean_squared_error = metrics.mean_squared_error(predictions, target)
root_mean_squared_error = math.sqrt(mean_squared_error)
print ("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print ("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)

min_house_value = california_housing_dataframe["median_house_value"].min()
max_house_value = california_housing_dataframe["median_house_value"].max()
min_max_difference = max_house_value - min_house_value

print ("Min. Median House Value: %0.3f" % min_house_value)
print ("Max. Median House Value: %0.3f" % max_house_value)
print ("Difference between Min. and Max.: %0.3f" % min_max_difference)
print ("Root Mean Squared Error: %0.3f" % root_mean_squared_error)