import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':
    data = dict()

    data[0] = [(999, 0.01670, 0.01886)]

    for r in range(1, 11):
        with open('out/rhc/restarts-%d.csv' % (r), 'r') as f:
            data[r] = [line.split(',') for line in f.readlines()]
            data[r] = [(int(l[0]), float(l[1]), float(l[2])) for l in data[r]]

    labels = ['r={}'.format(i) for i in range(11)]
    y_pos = range(len(labels))
    last_entries_train = {_r: _d[-1][1] for _r, _d in data.items()}
    last_entries_test = {_r: _d[-1][2] for _r, _d in data.items()}

    plt.figure()
    plt.title('Randomized Hill Climbing: Training Error')

    errors = [last_entries_train[i] for i in range(11)]
    plt.barh(y_pos, errors)

    plt.yticks(y_pos, labels)
    plt.xlabel('Error')
    plt.ylabel('Restarts')

    plt.savefig('out/rhc/restarts-training.png')

    plt.figure()
    plt.title('Randomized Hill Climbing: Testing Error')

    errors = [last_entries_test[i] for i in range(11)]
    plt.barh(y_pos, errors)

    plt.yticks(y_pos, labels)
    plt.xlabel('Error')
    plt.ylabel('Restarts')

    plt.savefig('out/rhc/restarts-testing.png')
