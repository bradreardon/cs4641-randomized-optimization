"""
Implementation of randomized hill climbing, simulated annealing, and genetic algorithm to
find optimal weights to a neural network that is classifying abalone as having either fewer
or more than 15 rings.

Based on AbaloneTest.java by Hannah Lau
"""
from __future__ import with_statement

import os
import csv
import time

from func.nn.backprop import BackPropagationNetworkFactory
from shared import SumOfSquaresError, DataSet, Instance
from opt.example import NeuralNetworkOptimizationProblem

import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm

import shared.filt.RandomOrderFilter as RandomOrderFilter
import shared.filt.TestTrainSplitFilter as TestTrainSplitFilter

INPUT_FILE = os.path.join("datasets", "breastcancer", "breast-cancer-wisconsin-trunc.data")

INPUT_LAYER = 9
HIDDEN_LAYER = 5
OUTPUT_LAYER = 1
TRAINING_ITERATIONS = 1000
TRAIN_TEST_SPLIT = 80


def initialize_instances():
    """Read the abalone.txt CSV data into a list of instances."""
    instances = []

    # Read in the abalone.txt CSV file
    with open(INPUT_FILE, "r") as abalone:
        reader = csv.reader(abalone)

        for row in reader:
            instance = Instance([float(value) for value in row[1:-1]])
            instance.setLabel(Instance(0 if float(row[-1]) == 2 else 1))  # 2 is benign, 4 malignant
            instances.append(instance)

    return instances


def train(oa, network, oaName, train_set, test_set, measure, max_iterations=TRAINING_ITERATIONS):
    """Train a given network on a set of instances.

    :param OptimizationAlgorithm oa:
    :param BackPropagationNetwork network:
    :param str oaName:
    :param list[Instance] instances:
    :param AbstractErrorMeasure measure:
    """

    train_instances = train_set.getInstances()
    test_instances = test_set.getInstances()

    fname = 'out/error/%s.csv' % (oaName)

    with open(fname, 'w') as f:
        # print "\nError results for %s\n---------------------------" % (oaName,)
        for iteration in xrange(max_iterations):
            oa.train()

            train_error = test_error = 0.00

            for train_instance in train_instances:
                network.setInputValues(train_instance.getData())
                network.run()

                output = train_instance.getLabel()
                output_values = network.getOutputValues()
                example = Instance(output_values, Instance(output_values.get(0)))
                train_error += measure.value(output, example)

            for test_instance in test_instances:
                network.setInputValues(test_instance.getData())
                network.run()

                output = test_instance.getLabel()
                output_values = network.getOutputValues()
                example = Instance(output_values, Instance(output_values.get(0)))
                test_error += measure.value(output, example)

            train_error_norm = train_error / len(train_instances)
            test_error_norm = test_error / len(test_instances)

            f.write("%d,%0.05f,%0.05f\n" % (iteration,train_error_norm,test_error_norm))

    print('Error written to %s' % (fname))


def main():
    """Run algorithms on the cancer dataset."""

    instances = initialize_instances()
    factory = BackPropagationNetworkFactory()
    measure = SumOfSquaresError()
    data_set = DataSet(instances)

    max_iterations = TRAINING_ITERATIONS

    hidden_layer_size = HIDDEN_LAYER

    networks = []  # BackPropagationNetwork
    nnop = []  # NeuralNetworkOptimizationProblem
    oa = []  # OptimizationAlgorithm
    oa_names = ["RHC", "SA", "GA"]
    results = ""

    RandomOrderFilter().filter(data_set)
    train_test_split = TestTrainSplitFilter(TRAIN_TEST_SPLIT)
    train_test_split.filter(data_set)

    train_set = train_test_split.getTrainingSet()
    test_set = train_test_split.getTestingSet()

    for name in oa_names:
        classification_network = factory.createClassificationNetwork([INPUT_LAYER, hidden_layer_size, OUTPUT_LAYER])
        networks.append(classification_network)
        nnop.append(NeuralNetworkOptimizationProblem(train_set, classification_network, measure))

    oa.append(RandomizedHillClimbing(nnop[0]))
    oa.append(SimulatedAnnealing(1E11, .95, nnop[1]))
    oa.append(StandardGeneticAlgorithm(200, 100, 10, nnop[2]))

    for i, name in enumerate(oa_names):
        start = time.time()
        correct = 0
        incorrect = 0

        train(oa[i], networks[i], oa_names[i], train_set, test_set, measure, max_iterations=max_iterations)
        end = time.time()
        training_time = end - start

        optimal_instance = oa[i].getOptimal()
        networks[i].setWeights(optimal_instance.getData())

        start = time.time()
        for instance in test_set.getInstances():
            networks[i].setInputValues(instance.getData())
            networks[i].run()

            predicted = instance.getLabel().getContinuous()
            actual = networks[i].getOutputValues().get(0)

            if abs(predicted - actual) < 0.5:
                correct += 1
            else:
                incorrect += 1

        end = time.time()
        testing_time = end - start

        _results = ""
        _results += "\n[%s] hidden_layer=%d, iterations=%d" % (name, hidden_layer_size, max_iterations)
        _results += "\nResults for %s: \nCorrectly classified %d instances." % (name, correct)
        _results += "\nIncorrectly classified %d instances.\nPercent correctly classified: %0.03f%%" % (incorrect, float(correct)/(correct+incorrect)*100.0)
        _results += "\nTraining time: %0.03f seconds" % (training_time,)
        _results += "\nTesting time: %0.03f seconds\n" % (testing_time,)

        with open('out/log/%s.log' % (oa_names[i]), 'w') as f:
            f.write(_results)

        results += _results

    print results


if __name__ == "__main__":
    main()

