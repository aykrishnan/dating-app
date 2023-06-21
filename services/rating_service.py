import math

from .swipe_direction import SwipeDirection


class RatingService:

    @staticmethod
    def update_rating(user_rating: int, candidate_rating: int, swipe_direction: SwipeDirection) -> int:
        expected_score = 1 / (1 + math.pow(10, (user_rating - candidate_rating) / 400))
        k_factor = 32
        actual_score = 1 if swipe_direction == SwipeDirection.RIGHT else 0

        new_candidate_rating = candidate_rating + k_factor * (actual_score - expected_score)

        return int(new_candidate_rating)
