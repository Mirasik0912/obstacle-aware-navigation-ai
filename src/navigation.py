class NavigationEngine:
    """
    Rule-based navigation using obstacle position and relative size.
    """

    def __init__(self, image_width):
        self.image_width = image_width

    def decide(self, obstacles):
        left_risk, center_risk, right_risk = 0, 0, 0

        for obs in obstacles:
            x1, y1, x2, y2 = obs["bbox"]
            width = x2 - x1
            cx = (x1 + x2) / 2

            # width ~ closeness (bigger = closer)
            if cx < self.image_width / 3:
                left_risk += width
            elif cx < 2 * self.image_width / 3:
                center_risk += width
            else:
                right_risk += width

        if center_risk == 0:
            return "Move forward"
        elif left_risk < right_risk:
            return "Move slightly left"
        else:
            return "Move slightly right"
