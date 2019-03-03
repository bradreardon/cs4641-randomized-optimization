#!/bin/bash
export PYENV_VERSION=cs4641
export CLASSPATH=abagail/ABAGAIL.jar:$CLASSPATH
mkdir -p out/{error,log,plot,rhc,sa,ga}

# echo "test neural nets"
# jython randomized_optimization/nn_test_cancer.py

echo "test RHC restarts"
jython randomized_optimization/rhc_cancer_restarts.py

# echo "plotting"
# python plot.py "Randomized Hill Climbing" out/error/RHC.csv out/plot/RHC.png
# python plot.py "Simulated Annealing" out/error/SA.csv out/plot/SA.png
# python plot.py "Genetic Algorithm" out/error/GA.csv out/plot/GA.png