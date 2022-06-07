from states import SplashState


# Der StateManager wird zum wechseln der States verwendet
class StateMananger(object):
    def __init__(self):
        self.go_to(SplashState())

    def go_to(self, state):
        self.state = state
        self.state.manager = self

# Quelle für den StateManager https://stackoverflow.com/a/14727074
