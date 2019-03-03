import sys
import os
import time

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FlipFlopEvaluationFunction as FlipFlopEvaluationFunction
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.UniformCrossOver as UniformCrossOver
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer

from array import array



"""
Commandline parameter(s):
   none
"""

N=80

fill = [2] * N
ranges = array('i', fill)

ITERATIONS = 5000

ef = FlipFlopEvaluationFunction()
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

rhc = RandomizedHillClimbing(hcp)
sa = SimulatedAnnealing(1E11, .95, hcp)
ga = StandardGeneticAlgorithm(200, 100, 10, gap)
mimic = MIMIC(200, 20, pop)

rhc_f = open('out/op/flipflop/rhc.csv', 'w')
sa_f = open('out/op/flipflop/sa.csv', 'w')
ga_f = open('out/op/flipflop/ga.csv', 'w')
mimic_f = open('out/op/flipflop/mimic.csv', 'w')

for i in range(ITERATIONS):
    rhc.train()
    rhc_fitness = ef.value(rhc.getOptimal())
    rhc_f.write('{},{}\n'.format(i, rhc_fitness))

    sa.train()
    sa_fitness = ef.value(sa.getOptimal())
    sa_f.write('{},{}\n'.format(i, sa_fitness))

    ga.train()
    ga_fitness = ef.value(ga.getOptimal())
    ga_f.write('{},{}\n'.format(i, ga_fitness))

    mimic.train()
    mimic_fitness = ef.value(mimic.getOptimal())
    mimic_f.write('{},{}\n'.format(i, mimic_fitness))

rhc_f.close()
sa_f.close()
ga_f.close()
mimic_f.close()

