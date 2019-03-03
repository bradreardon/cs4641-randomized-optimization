import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':
    data = dict()

    for cr in [.95, .8, .65, .5, .35, .2]:
        with open('out/sa/cooling-%0.02f.csv' % (cr), 'r') as f:
            data[cr] = [line.split(',') for line in f.readlines()]
            data[cr] = [(int(l[0]), float(l[1]), float(l[2])) for l in data[cr]]


    iter_no = list(range(1000))

    plt.figure()
    plt.title(f'Simulated Annealing: Training Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    for cr, _data in data.items():
        d = [_d[1] for _d in _data]
        plt.plot(iter_no, d, label='cooling=%0.02f' % (cr))

    plt.legend()
    plt.savefig('out/sa/cooling-error-training.png')

    plt.figure()
    plt.title(f'Simulated Annealing: Training Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    for cr, _data in data.items():
        d = [_d[2] for _d in _data]
        plt.plot(iter_no, d, label='cooling=%0.02f' % (cr))
        
    plt.legend()
    plt.savefig('out/sa/cooling-error-testing.png')
