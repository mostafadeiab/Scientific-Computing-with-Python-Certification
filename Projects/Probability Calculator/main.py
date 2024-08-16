import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        balls_dict = {}
        for ball in drawn_balls:
            if ball in balls_dict:
                balls_dict[ball] += 1
            else:
                balls_dict[ball] = 1

        success = True
        for ball, count in expected_balls.items():
            if balls_dict.get(ball, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
