class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current