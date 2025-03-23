from data import UNSORTED_LIST
from pytest_benchmark.fixture import BenchmarkFixture
from selection_sort import selection_sort


def test_selection_sort_benchmark(benchmark: BenchmarkFixture) -> None:
    benchmark.pedantic(
        target=selection_sort,
        args=(UNSORTED_LIST,),
        rounds=100,
        warmup_rounds=5,
        iterations=30,
    )
