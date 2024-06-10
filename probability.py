import random
from collections import Counter


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create a new hat instance to draw from, so the original hat is not modified
        hat_copy = Hat(**Counter(hat.contents))
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = Counter(drawn_balls)

        # Check if the drawn balls meet the expected balls criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count[color] < count:
                success = False
                break

        if success:
            success_count += 1

    # Return the probability of success
    return success_count / num_experiments


# Example Usage
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"blue": 2, "red": 1}, num_balls_drawn=6, num_experiments=1000)
print(probability)
