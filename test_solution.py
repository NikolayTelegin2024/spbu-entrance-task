import unittest
from solution import find_universal_vertices

class TestGraph(unittest.TestCase):
    """тесты"""

    def test_single_node(self):
        matrix = [[0]]
        self.assertEqual(find_universal_vertices(matrix), [1])

    def test_path(self):
        matrix = [
            [-1,  0],
            [ 1, -1],
            [ 0,  1]
        ]
        self.assertEqual(find_universal_vertices(matrix), [3])

    def test_cycle(self):
        matrix = [
            [-1,  0,  1],
            [ 1, -1,  0],
            [ 0,  1, -1]
        ]
        self.assertEqual(find_universal_vertices(matrix), [1, 2, 3])

    def test_fork(self):
        matrix = [
            [-1, -1],
            [ 1,  0],
            [ 0,  1]
        ]
        self.assertEqual(find_universal_vertices(matrix), [])

    def test_disconnected(self):
        matrix = [
            [-1],
            [ 1],
            [ 0]
        ]
        self.assertEqual(find_universal_vertices(matrix), [])


if __name__ == "__main__":
    unittest.main()