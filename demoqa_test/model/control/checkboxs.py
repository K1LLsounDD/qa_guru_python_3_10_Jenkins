from selene.support.conditions import have
from selene.support.shared import browser


class Checkbox:
    def __init__(self, selector):
        self.selector = selector

    def hobby(self, value):
        self.selector.element_by(have.text(value)).click()
        return self