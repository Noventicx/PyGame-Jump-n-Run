from states import SplashState


class StateMananger(object):
    def __init__(self):
        self.go_to(SplashState())

    def go_to(self, state):
        self.state = state
        self.state.manager = self