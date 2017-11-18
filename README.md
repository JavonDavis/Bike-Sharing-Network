# Bike Sharing Network

In this project I implemented a basic neural network to predict how many bikes a bike sharing company would need to have based on some data about previous bike sharing rides. 


[//]: # (Image References)
[image1]: ./readme_images/graph.png

The repository has 2 files:

* Your_first_neural_network.ipynb
* my_answers.py

The Jupyter notebook contains the code for loading and preprocessing the data and the calls upon the functions defined in the my_ansers.py file to train the network. 

### Network Architecture

The network archicture used is simple and consists of 6 hidden nodes and 1 ouput nodes and uses the sigmoid activation function to propogate the results from the hidden layer to the output layer. It trains using the Gradient Descent Technique over 3000 epochs and achieved a minimum of 0.077 Training loss and a 0.129 validation loss with a learning rate of 1. 

Here's a graph of the model's results agest the test set:

![Graph][image1]

### Short Discussion about the results

#### How well does the model predict the data? Where does it fail? Why does it fail where it does?

The model predicts the data relatively well as can be seen in the graph above but seems to not do so well when the number of bike sharing rides is low. Could be that since there isn't much occurences of months with low rde count the model could not properly predict these cases. Normalization Techniques might resolve this problem.
