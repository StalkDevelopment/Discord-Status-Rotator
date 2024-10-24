import unittest
from src.statuses import get_next_status, statuses
import itertools

class TestStatuses(unittest.TestCase):
    def setUp(self):
        self.status_cycle = itertools.cycle(statuses)

    def test_get_next_status(self):
        first_status = get_next_status(self.status_cycle)
        second_status = get_next_status(self.status_cycle)
        third_status = get_next_status(self.status_cycle)

        self.assertEqual(first_status, statuses[0])
        self.assertEqual(second_status, statuses[1])
        self.assertEqual(third_status, statuses[2])

if __name__ == "__main__":
    unittest.main()
