class Hand:
    def __init__(self, hand):
        if hand == "グー":
            self.hand = Rock()
        elif hand == "パー":
            self.hand = Paper()
        else:
            self.hand = Scissor()


class Rock:
    def __str__(self):
        return "グー"

    def __eq__(self, other):
        if isinstance(other, Rock):
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Paper):
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Scissor):
            return True
        else:
            return False


class Paper:
    def __str__(self):
        return "パー"

    def __eq__(self, other):
        if isinstance(other, Paper):
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Scissor):
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Rock):
            return True
        else:
            return False


class Scissor:
    def __str__(self):
        return "チョキ"

    def __eq__(self, other):
        if isinstance(other, Scissor):
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rock):
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Paper):
            return True
        else:
            return False
