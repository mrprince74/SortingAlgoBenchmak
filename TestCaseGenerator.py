import random
from typing import List, Tuple

class TestCaseGenerator:
    @classmethod
    def _generate(cls, min_n: int, max_n: int, min_num: int, max_num: int) -> List[int]:
        n = random.randint(min_n, max_n)
        return [random.randint(min_num, max_num) for _ in range(n)]
    
    @classmethod
    def generate_small(cls) -> List[int]:
        data = cls._generate(10, 500, 0, 1000)
        return data
    
    @classmethod
    def generate_medium(cls) -> List[int]:
        data = cls._generate(500, 10_000, 0, 5000)
        return data
    
    @classmethod
    def generate_large(cls) -> List[int]:
        data = cls._generate(10_000, 100_000, -100_000, 100_000)
        return data
    
    @classmethod
    def generate_already_sorted(cls) -> List[int]:
        size = random.randint(10, 1000)
        return list(range(size))

    @classmethod
    def generate_reverse_sorted(cls) -> List[int]:
        size = random.randint(10, 1000)
        return list(range(size, 0, -1))

    @classmethod
    def generate_identical(cls) -> List[int]:
        size = random.randint(10, 1000)
        return [random.randint(-100, 100)] * size


if __name__ == '__main__':
  # Example usage
  print(f"Generated {len(TestCaseGenerator.generate_reverse_sorted())} items.")
  