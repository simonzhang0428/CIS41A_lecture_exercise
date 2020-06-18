class Counter:
    def __init__(self, counter, limit):
        self.counter = counter
        self.limit = limit

    def increment(self):
        if self.counter < self.limit:
            self.counter += 1

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1

    def get_value(self):
        return self.counter


class ContestResult:
    def __init__(self):
        self.winner = ''
        self.second_place = ''
        self.third_place = ''

    def set_winner(self, winner):
        self.winner = winner

    def set_second_place(self, second):
        self.second_place = second

    def set_third_place(self, third):
        self.third_place = third

    def get_winner(self):
        return self.winner

    def get_second_place(self):
        return self.second_place

    def get_third_place(self):
        return self.third_place


class Calculator:
    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            return 'You can\'t divide by zero!'
        else:
            return n1 / n2


c = Calculator()
print(c.divide(4, 4))
print(c.divide(4, 0))


class Alarm:
    code = ''
    armed = False


myAlarm = Alarm()
myAlarm.code = '3579'
print(myAlarm.armed)
