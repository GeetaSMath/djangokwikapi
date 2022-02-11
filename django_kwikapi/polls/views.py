from kwikapi import API
from logging import Logger

class BaseCalc():
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

class StandardCalc():
    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        return a / b

api=API(log=Logger, default_version='v1')
api.register(BaseCalc(), 'v1')
api.register(StandardCalc(), "v2")