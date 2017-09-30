from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np
import random
import math

fig, ax = plt.subplots(1, 1)
intervals = [10, 100, 1000, 5000, 10000, 20000]
seeds = [66, 67]


zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def dict_init(a):
    return dict(enumerate(a))


def interval(a, dic, step):
    for number in a:
        key = math.trunc((number-14666)/step)
        dic[key] += 1


def print_count(a, step):
    dic = dict_init(zeros)
    interval(a, dic, step)
    print(dic)


def generate_uniform(a, b, size, seed):
    l = []
    random.seed(seed)
    for i in range(size):
        number = random.uniform(a, b)
        l.append(number)
    return l


def generate_expon(number, lambd, seed):
    l = []
    random.seed(seed)
    for i in range(number):
        number = random.expovariate(lambd)
        if number > 285334:
            number = 285334
        l.append(14666 + number)
    return l


def generate_gamma(number, lambd, seed):
    l = []
    random.seed(seed)
    for i in range(number):
        number = random.gammavariate(3, lambd)
        if number > 285334:
            number = 285334
        l.append(14666 + number)
    return l


def uniform_deviation():
    for seed in seeds:
        np.random.seed(seed)
        for interval in intervals:
            e = generate_uniform(14666, 161334, interval, seed)
            print_count(e, 14666.8)

            r = np.asarray(e)
            plt.hist(r, bins=10)
            plt.title("Interval -  {}. Mean: {}. Seed: {}".format(interval, round(r.mean(), 3), seed))
            plt.show()
            print('Mean for interval {} is {}'.format(interval, r.mean()))
            print('Standard deviation for interval {} is {}'.format(interval, r.std()))
            print('Koefficient variacii for interval {} is {}\n'.format(interval, r.std()/r.mean()))
        print(''.join(['-' for x in range(80)]))


def exponential_deviation():
    for seed in seeds:
        for interval in intervals:
            e = generate_expon(interval, 1/73334, seed)
            print_count(e, 28554)

            r = np.asarray(e)
            plt.hist(r, bins=10)
            plt.title("Interval -  {}. Mean: {}. Seed: {}".format(interval, r.mean(), seed))
            plt.show()
            print('Mean for interval {} is {}'.format(interval, r.mean()))
            print('Standard deviation for interval {} is {}'.format(interval, r.std()))
            print('Koefficient variacii for interval {} is {}\n'.format(interval, r.std()/r.mean()))
        print(''.join(['-' for x in range(80)]))


def erlang_deviation():
    for seed in seeds:
        np.random.seed(seed)
        for interval in intervals:
            e = generate_gamma(interval, 24445, seed)
            print_count(e, 28554)

            e = np.asarray(e)
            plt.hist(e, bins=10)
            plt.title("Interval -  {}. Mean: {}. Seed: {}".format(interval, e.mean(), seed))
            plt.show()
            print('Mean for interval {} is {}'.format(interval, e.mean()))
            print('Standard deviation for interval {} is {}'.format(interval, e.std()))
            print('Koefficient variacii for interval {} is {}\n'.format(interval, e.std()/e.mean()))
        print(''.join(['-' for x in range(80)]))

erlang_deviation()
