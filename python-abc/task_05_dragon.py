#!/usr/bin/env python3
"""
This module demonstrates using mixins to add modular behavior to classes.
A Dragon class is able to swim and fly by inheriting SwimMixin and FlyMixin.
"""


class SwimMixin:
    """Provides swimming ability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
