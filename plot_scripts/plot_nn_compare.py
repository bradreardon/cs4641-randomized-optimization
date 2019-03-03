import sys

from matplotlib import pyplot as plt


if __name__ == '__main__':

    with open('out/error/RHC.csv', 'r') as f:
        rhc_data = [line.split(',') for line in f.readlines()]
        rhc_data = [(int(l[0]), float(l[1]), float(l[2])) for l in rhc_data]

    with open('out/error/SA.csv', 'r') as f:
        sa_data = [line.split(',') for line in f.readlines()]
        sa_data = [(int(l[0]), float(l[1]), float(l[2])) for l in sa_data]

    with open('out/error/GA.csv', 'r') as f:
        ga_data = [line.split(',') for line in f.readlines()]
        ga_data = [(int(l[0]), float(l[1]), float(l[2])) for l in ga_data]


    iter_no = list(range(1000))

    plt.figure()
    plt.title(f'Neural Network: Training Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    plt.plot(iter_no, [_d[1] for _d in rhc_data], label='RHC')
    plt.plot(iter_no, [_d[1] for _d in sa_data], label='SA')
    plt.plot(iter_no, [_d[1] for _d in ga_data], label='GA')

    plt.legend()
    plt.savefig('out/nn-combined-training.png')

    plt.figure()
    plt.title(f'Neural Network: Testing Error')
    plt.xlabel('Number of iterations')
    plt.ylabel('Error')

    plt.plot(iter_no, [_d[2] for _d in rhc_data], label='RHC')
    plt.plot(iter_no, [_d[2] for _d in sa_data], label='SA')
    plt.plot(iter_no, [_d[2] for _d in ga_data], label='GA')
        
    plt.legend()
    plt.savefig('out/nn-combined-testing.png')
