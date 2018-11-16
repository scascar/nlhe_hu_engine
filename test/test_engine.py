import unittest
from nlhe_hu_engine.engine import Engine
from nlhe_hu_engine.constants import Actions


class TestEngine(unittest.TestCase):

    def test_is_sb_turn(self):
        eng = Engine()
        eng.new_hand()
        self.assertEqual(eng.is_sb_turn(), True)
        eng.play_action(Actions.BET, 100)
        self.assertEqual(eng.is_sb_turn(), False)


if __name__ == '__main__':
    unittest.main()
