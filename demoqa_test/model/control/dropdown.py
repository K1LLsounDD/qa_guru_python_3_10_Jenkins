from selene.support.conditions import have
from selene.support.shared import browser


class Dropdown:
    def __init__(self, selector, selectors):
        self.selector = selector
        self.selectors = selectors

    def select(self, text):
        self.selector.click()
        self.selectors.element_by(have.exact_text(text)).click()
        return self