import unittest

from datingapp.services.rating_service import RatingService
from datingapp.services.swipe_direction import SwipeDirection


class RatingServiceTestCase(unittest.TestCase):
    def test_update_rating_swipe_left(self):
        user_rating = 1980
        candidate_rating = 2112
        swipe_direction = SwipeDirection.LEFT

        new_candidate_rating = RatingService.update_rating(user_rating, candidate_rating, swipe_direction)

        self.assertEqual(2090, new_candidate_rating)

    def test_update_rating_swipe_right(self):
        user_rating = 1980
        candidate_rating = 2112
        swipe_direction = SwipeDirection.RIGHT

        new_candidate_rating = RatingService.update_rating(user_rating, candidate_rating, swipe_direction)

        self.assertEqual(2122, new_candidate_rating)


if __name__ == '__main__':
    unittest.main()
