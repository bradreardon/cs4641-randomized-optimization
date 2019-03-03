import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':
    prob = sys.argv[1]
    folder = sys.argv[2]
    out = sys.argv[3]
    iter_n = int(sys.argv[4])

    iter_no = list(range(iter_n))
    rhc_fitness = list()
    sa_fitness = list()
    ga_fitness = list()
    mimic_fitness = list()

    with open('out/op/{}/rhc.csv'.format(folder), 'r') as f:
        lines = f.readlines()

        for line in lines:
            i, fit = line.split(',')
            rhc_fitness.append(float(fit))

    with open('out/op/{}/sa.csv'.format(folder), 'r') as f:
        lines = f.readlines()

        for line in lines:
            i, fit = line.split(',')
            sa_fitness.append(float(fit))

    with open('out/op/{}/ga.csv'.format(folder), 'r') as f:
        lines = f.readlines()

        for line in lines:
            i, fit = line.split(',')
            ga_fitness.append(float(fit))

    with open('out/op/{}/mimic.csv'.format(folder), 'r') as f:
        lines = f.readlines()

        for line in lines:
            i, fit = line.split(',')
            mimic_fitness.append(float(fit))

    plt.figure()
    plt.title(f'Fitness Curve: {prob}')
    plt.xlabel('Number of iterations')
    plt.ylabel('Fitness')
    plt.plot(iter_no, rhc_fitness, label='RHC')
    plt.plot(iter_no, sa_fitness, label='SA')
    plt.plot(iter_no, ga_fitness, label='GA')
    plt.plot(iter_no, mimic_fitness, label='MIMIC')
    plt.legend()
    plt.savefig(out)
