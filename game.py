class Game:
    def __init__(self):
        # 0 normal, 1: spare, 2: strike
        self._before_frame_status = 0
        self._current_frame_status = 0

        self._current_frame = 0
        self._current_frame_step = 0
        self._score = 0
        self._score_card = [[0 for _ in range(2)] for _ in range(10)]

    def roll(self, point):
        self._score_card[self._current_frame][self._current_frame_step] = point

        if self.check_before_strike():
            pass
        elif self.check_before_spare():
            pass
        elif self.check_before_normal():
            self._score += point
            if self._current_frame_step == 0:
                self._current_frame_step = 1
            elif self._current_frame_step == 1:
                self._current_frame_step = 0
                self._current_frame += 1

        if self._current_frame_step == 0 and point == 10:
            self._current_frame += 1
            self._before_frame_status = 2

        elif (self._current_frame_step == 1 and
              self._score_card[self._current_frame][self._current_frame_step-1] + self._score_card[self._current_frame][self._current_frame_step] == 10):
            self._current_frame += 1
            self._before_frame_status = 1

        else:
            if self._current_frame_step == 0:
                self._current_frame_step = 1

            elif self._current_frame_step == 1:
                self._current_frame_step = 0
                self._current_frame += 1
                self._before_frame_status = 0


        self._score += point

    def check_before_normal(self):
        return (not self.check_before_spare()) and (not self.check_before_strike())

    def check_before_spare(self):
        if self._current_frame == 0:
            return False
        elif (self._score_card[self._current_frame - 1][0] != 10
              and self._score_card[self._current_frame - 1][0] + self._score_card[self._current_frame - 1][1] == 10):
            return True
        return False

    def check_before_strike(self):
        if self._current_frame == 0:
            return False
        if self._score_card[self._current_frame - 1][0] == 10:
            return True
        return False

        return is_before_strike

    def score(self):
        return self._score
