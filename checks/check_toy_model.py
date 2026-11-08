"""Consistency checks for the hypothesis paper (standard library only).

These arithmetic checks are NOT a formal proof of nonamenability, and
they are NOT an experiment on the photoelectric effect.
"""
from fractions import Fraction


def f0(x):
    if x <= Fraction(1, 2):
        return x / 2
    if x <= Fraction(3, 4):
        return x - Fraction(1, 4)
    return 2 * x - 1


def check_dyadic_unitary_example():
    edges_in = [Fraction(0), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
    edges_out = [f0(x) for x in edges_in]
    slopes = [Fraction(1, 2), Fraction(1), Fraction(2)]
    assert edges_out == [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1)]
    # Uniform input psi(x)=1; transformed intensity is 1/f0'(f0^-1(x)).
    probabilities = [
        (right-left)/slope
        for left, right, slope in zip(edges_out[:-1], edges_out[1:], slopes)
    ]
    assert probabilities == [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)]
    assert sum(probabilities) == 1
    return probabilities


def check_finite_support_identity_on_Z():
    # The identity holds for ANY discrete group, including amenable Z.
    A = {-2, -1, 0, 1, 2}
    shifted = {g+1 for g in A}
    overlap = Fraction(len(A.intersection(shifted)), len(A))
    squared_displacement = Fraction(len(A.symmetric_difference(shifted)), len(A))
    assert squared_displacement == 2 - 2*overlap
    return overlap, squared_displacement


def check_amenable_negative_control(N=10000):
    A = set(range(-N, N+1))
    shifted = {g+1 for g in A}
    fraction = Fraction(len(A.symmetric_difference(shifted)), len(A))
    assert fraction == Fraction(2, 2*N + 1)
    assert fraction < Fraction(1, 1000)
    return fraction


if __name__ == "__main__":
    print("Dyadic bins:", check_dyadic_unitary_example())
    print("Regular representation identity:", check_finite_support_identity_on_Z())
    print("Amenable negative control:", check_amenable_negative_control())
    print("All elementary consistency checks passed.")
