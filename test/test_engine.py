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
        eng.play_action(Actions.CALL,0)
        self.assertEqual(eng.is_sb_turn(),False)
        eng.play_action(Actions.CALL,0)
        self.assertEqual(eng.is_sb_turn(),True)

    def test_get_bet_range(self):
        eng = Engine()
        eng.new_hand()
        b_range = eng.get_bet_range()
        self.assertEqual(b_range, [20,490])
        eng.small_blind = 5
        eng.big_blind = 10
        eng.new_hand(starting_stack=100)
        b_range = eng.get_bet_range()
        self.assertEqual(b_range,[10,95])

        eng.play_action(Actions.CALL,0) # pot [10,10]
        b_range = eng.get_bet_range()
        self.assertEqual(b_range,[10,90])

        eng.play_action(Actions.CALL,0)
        eng.play_action(Actions.BET,10)
        b_range = eng.get_bet_range()
        self.assertEqual(b_range,[20,90])

        eng.play_action(Actions.BET,40) #[50,25] [40,10]
        b_range = eng.get_bet_range()
        self.assertEqual(b_range,[40,80])


if __name__ == '__main__':
    unittest.main()
