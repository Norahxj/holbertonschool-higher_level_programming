#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance with a FlyingFish class
that inherits behaviors from both Fish and Bird.
"""


class Fish:
    """Represents a fish with swimming ability."""

    def swim(self):
        """Print swimming action."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying ability."""

    def fly(self):
        """Print flying action."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish inherits from both Fish and Bird.

    Demonstrates multiple inheritance and method resolution order.
    """

    def swim(self):
        """Override swim to customize for FlyingFish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly to customize for FlyingFish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat to reflect dual environment."""
        print("The flying fish lives both in water and the sky!")
