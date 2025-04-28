#!/usr/bin/env python3
"""Module containing an asynchronous generator that yields random numbers."""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Coroutine that yields a random number between 0 and 10, 10 times,
      with 1 second delay each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
