class Nobody:
    def __init__(self, name: str):
        self.name = f"I'm Nobody, not {name}" if self.name != 'Nobody' else 'Nobody'
