class Game:
    def __init__(self):
        self.total_score = 0
        self.rolls = [0 for _ in range(21)]
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        result = 0

        frame_index = 0
        for frame in range(10):
            if self.rolls[frame_index] == 10:
                result += 10
                result += self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                result += 10
                result += self.spare_bonus(frame_index)
                frame_index += 2
            else:
                result += self.basic_frame_score(frame_index)
                frame_index += 2

        return result

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def basic_frame_score(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10