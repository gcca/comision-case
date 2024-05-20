#!/usr/bin/env python
import argparse
import numpy as np


def generate_rates(𝜇, σ, n):
    return np.random.normal(𝜇, σ, n)


def generate_targets(κ, ρ, n):
    return np.random.choice(κ, n, p=ρ)


def generate(args):
    assert args.t is not None
    assert args.p is not None
    assert len(args.t) == len(args.p)

    r = int(args.r)
    rates = generate_rates(float(args.m), float(args.s), r)
    targets = generate_targets(
        np.array(args.t).astype(int), np.array(args.p).astype(float), r
    )
    sales = rates * targets

    data = [np.arange(1, r + 1), targets, sales]

    if args.o == "-":
        import sys

        save_csv(sys.stdout, data)
    else:
        with open(args.o) as output:
            save_csv(output, data)


def save_csv(csvfile, data):
    import csv

    wr = csv.writer(csvfile)
    data = [arr.round(2) for arr in data]
    wr.writerow(("n", "target", "sale"))
    wr.writerows(zip(*data))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-m", type=float, help="mean")
    argparser.add_argument("-s", type=float, help="std")
    argparser.add_argument("-r", type=int, help="repetitions")
    argparser.add_argument("-o", default="-", help="output")
    argparser.add_argument("-t", action="append")
    argparser.add_argument("-p", action="append")

    args = argparser.parse_args()
    generate(args)


if "__main__" == __name__:
    main()
