from argparse import ArgumentError
from enum import Enum
from typing import Any

from uuid import UUID

class ConversionType(Enum):
    INTEGER_TUPLE = 1
    UUID_TUPLE = 2
    MIXED_TUPLE = 3

class RedisUtils:
    @staticmethod
    def parse_record(record: bytes | str, conversion_type: ConversionType):
        if isinstance(record, bytes):
            record = record.decode()

        if conversion_type == ConversionType.INTEGER_TUPLE:
            record = record[1:-1] # Deleting '(' and ')'
            return tuple(map(int, record.split(',')))
        elif conversion_type == ConversionType.UUID_TUPLE:
            record = record[1:-1] # Deleting '(' and ')'
            return tuple(map(UUID, record.split(',')))
        elif conversion_type == ConversionType.MIXED_TUPLE:
            record = record[1:-1] # Deleting '(' and ')'
            return tuple(record.split(','))




