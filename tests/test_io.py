from typing import Dict

import pytest

from chris.utils.io import print_map


@pytest.fixture(scope="class")
def example_score_map() -> Dict[str, float]:
    return {
        'a': 2.1,
        'b': 4.0,
        'c': 0.5,
    }


class TestPrint:
    def test_print_map(
        self,
        capsys: pytest.CaptureFixture,
        example_score_map: Dict[str, float],
    ) -> None:
        print_map(example_score_map)
        captured = capsys.readouterr()
        assert captured.out == 'b: 4.0\na: 2.1\nc: 0.5\n'

    def test_print_map_desc(
        self,
        capsys: pytest.CaptureFixture,
        example_score_map: Dict[str, float],
    ) -> None:
        print_map(example_score_map, asc=True)
        captured = capsys.readouterr()
        assert captured.out == 'c: 0.5\na: 2.1\nb: 4.0\n'

    def test_print_map_format(
        self,
        capsys: pytest.CaptureFixture,
        example_score_map: Dict[str, float],
    ) -> None:
        print_map(example_score_map, line_format="- {}->{}\n")
        captured = capsys.readouterr()
        assert captured.out == '- b->4.0\n- a->2.1\n- c->0.5\n'
