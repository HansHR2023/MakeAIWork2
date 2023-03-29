import logging
import numpy as np

logging.basicConfig(level=logging.INFO, filename='logfile_train.txt')

# OPDDRACHT
# Voeg de ontbrekende code toe zodanig dat je met deze
# class Perceptron objecten kunt maken
# Zie test_perceptron.py voor testcases

# BONUS OPDRACHT
# Voeg de methode display toe om de perceptron te visualiseren
# kijk in perceptron.dot hoe je dat met de graphviz library
# kunt doen


class Perceptron:

    """
    Perceptron class to simulate a Neuron
    """

    # Constructor
    # 'dunder init'
    def __init__(self):
        self.weightVector = None
        self.bias = 0

    def initialize(self, nrOfFeatures):
        """Initialize w and b as zero"""

        # Create initial weight vector for each feature
        self.weightVector = np.zeros(nrOfFeatures)

        # Initialize bias
        self.bias = 0

    def predict(self, inputVector):
            """
            Determine outputvalue by multiplying
            inputvector with weightvector
            HINT: use np.dot()
            """
            activation = np.dot(inputVector, self.weightVector) + self.bias

            logging.debug(f"activation : {activation}")

            return 1 if activation > 0 else 0
    
    def train(self, X, y, epochs=100, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels
        """
        # Initialize weights and bias
        nrOfFeatures = X.shape[1]
        self.initialize(nrOfFeatures)

        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            logging.debug(f"epoch : {epoch}")

            # For each inputVector
            for inputVector, label in zip(X, y):
                logging.debug(f"inputVector : {inputVector}")

                # Labeled output
                logging.debug(f"label : {label}")

                # Predict output
                prediction = self.predict(inputVector)
                logging.debug(f"prediction : {prediction}")

                # Determine error
                error = label - prediction
                logging.debug(f"error : {error}")

                # update weight and b
                # de formule is dus weight = weight + error * lr, 
                # maar de deltaWeight is al het verschil in weight
                deltaWeight = inputVector * error * learningRate
                self.weightVector += deltaWeight 
                logging.debug(f"deltaWeight : {deltaWeight}")

                logging.debug(f"learningRate : {learningRate}")
                deltaBias = error * learningRate
                self.bias += deltaBias
                logging.debug(f"deltaBias : {deltaBias}")

                print()

    
