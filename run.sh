#!/bin/bash

export CLASSPATH=abagail/ABAGAIL.jar:$CLASSPATH
mkdir -p out/{error,log}

echo "abalone_test_cancer"
jython randomized_optimization/abalone_test_cancer.py