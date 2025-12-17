class NavigationEngine:
    """
    Simple rule-based navigation logic based on obstacle positions.
    """

    def __init__(self, image_width):
        self.image_width = image_width

    def decide(self, obstacles):
        left, center, right = 0, 0, 0

        for obs in obstacles:
            x1, _, x2, _ = obs["bbox"]
            cx = (x1 + x2) / 2

            if cx < self.image_width / 3:
                left += 1
            elif cx < 2 * self.image_width / 3:
                center += 1
            else:
                right += 1

        if center == 0:
            return "Move forward"
        elif left < right:
            return "Move slightly left"
        else:
            return "Move slightly right"
