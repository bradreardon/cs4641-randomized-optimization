import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':
    algo = sys.argv[1]
    csv = sys.argv[2]
    out = sys.argv[3]

    iter_no = list()
    train_err = list()
    test_err = list()

    with open(csv, 'r') as f:
        lines = f.readlines()

        for line in lines:
            i, tr, te = line.split(',')
            iter_no.append(int(i))
            train_err.append(float(tr))
            test_err.append(float(te))

    plt.figure()
    plt.title(f'Learning Curve: {algo}')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')
    plt.plot(iter_no, train_err, label='Training error')
    plt.plot(iter_no, test_err, label='Testing error')
    plt.legend()
    plt.savefig(out)
