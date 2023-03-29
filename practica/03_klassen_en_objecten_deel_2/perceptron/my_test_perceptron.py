#!/usr/bin/env python

from my_perceptron import Perceptron
import itertools
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, filename='logfile_test.txt', filemode='w', force=True)

possibleOutcomes = [0, 1]
xTrain = np.array(
    [element for element in itertools.product(possibleOutcomes, possibleOutcomes)]
)

logging.debug(f"xTrain : {xTrain}")

yTrainAnd = np.array([0, 0, 0, 1])

andPerceptron = Perceptron()
andPerceptron.train(xTrain, yTrainAnd, epochs=100, learningRate=0.1)
testInput = np.array([0, 1])
logging.info(f"testInput : {testInput}")

prediction = andPerceptron.predict(testInput)
logging.info(f"Predicted yAND value : {prediction}")

# OPDDRACHT
# Maak nu zelf het object orPerceptron

yTrainOr = np.array([0, 1, 1, 1])
orPerceptron = Perceptron()
orPerceptron.train(xTrain, yTrainOr, epochs=100, learningRate=0.1)
testInput = np.array([0, 0])
logging.info(f"testInput : {testInput}")

predictionOr = orPerceptron.predict(testInput)
logging.info(f"Predicted yOr value : {predictionOr}")

