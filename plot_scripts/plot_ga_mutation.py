import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':
    data = dict()

    for x in [10, 25, 50]:
        with open('out/ga/mutation-%d.csv' % (x), 'r') as f:
            data[x] = [line.split(',') for line in f.readlines()]
            data[x] = [(int(l[0]), float(l[1]), float(l[2])) for l in data[x]]


    iter_no = list(range(1000))

    plt.figure()
    plt.title(f'Genetic Algorithm: Training Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    for x, _data in data.items():
        d = [_d[1] for _d in _data]
        plt.plot(iter_no, d, label='mutation=%d' % (x))

    plt.legend()
    plt.savefig('out/ga/mutation-training.png')

    plt.figure()
    plt.title(f'Genetic Algorithm: Testing Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    for x, _data in data.items():
        d = [_d[2] for _d in _data]
        plt.plot(iter_no, d, label='mutation=%d' % (x))
        
    plt.legend()
    plt.savefig('out/ga/mutation-testing.png')
