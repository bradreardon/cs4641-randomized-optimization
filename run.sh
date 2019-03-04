#!/bin/bash
export PYENV_VERSION=cs4641
export CLASSPATH=abagail/ABAGAIL.jar:$CLASSPATH
mkdir -p out/{error,log,plot,rhc,sa,ga,op}
mkdir -p out/op/{countones,fourpeaks,salesman,flipflop}



# echo "test neural nets"
# jython randomized_optimization/nn_test_cancer.py

# echo "test RHC restarts"
# jython randomized_optimization/rhc_cancer_restarts.py

# echo "test SA cooling"
# jython randomized_optimization/sa_cancer_cooling.py

# echo "test GA population size"
# jython randomized_optimization/ga_population.py

# echo "test GA mating rate"
# jython randomized_optimization/ga_mating.py

# echo "test GA mutation rate"
# jython randomized_optimization/ga_mutation.py



# echo "plotting learning curves"
# python plot_scripts/plot_learning.py "Randomized Hill Climbing" out/error/RHC.csv out/plot/RHC.png
# python plot_scripts/plot_learning.py "Simulated Annealing" out/error/SA.csv out/plot/SA.png
# python plot_scripts/plot_learning.py "Genetic Algorithm" out/error/GA.csv out/plot/GA.png

# echo "plotting comparison"
# python plot_scripts/plot_nn_compare.py

# echo "plotting RHC restarts"
# python plot_scripts/plot_rhc_restarts.py

# echo "plotting SA cooling"
# python plot_scripts/plot_sa_cooling.py

# echo "plotting GA population"
# python plot_scripts/plot_ga_population.py

# echo "plotting GA mating"
# python plot_scripts/plot_ga_mating.py

# echo "plotting GA mutation"
# python plot_scripts/plot_ga_mutation.py



# echo "test count ones (?)"
# jython randomized_optimization/op_countones.py

# echo "test flip flop (SA)"
# jython randomized_optimization/op_flipflop.py

# echo "test four peaks (MIMIC)"
# jython randomized_optimization/op_fourpeaks.py

# echo "test traveling salesman (GA)"
# jython randomized_optimization/op_travelingsalesman.py



# echo "plotting optimization problems"
# python plot_scripts/plot_op_fitness.py "Count Ones" countones out/op/countones/fitness.png 5000
# python plot_scripts/plot_op_fitness.py "Flip Flop" flipflop out/op/flipflop/fitness.png 5000
# python plot_scripts/plot_op_fitness.py "Four Peaks" fourpeaks out/op/fourpeaks/fitness.png 5000
# python plot_scripts/plot_op_fitness.py "Traveling Salesman" salesman out/op/salesman/fitness.png 5000
