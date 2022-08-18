class Nobody:
    """Класс Nobody: принимает создает оъект с атрибутом 'name', который сохраняет в значение
    'Nobody' либо переданное имя со строкой I'm Nobody, not {name}"""
    def __init__(self, name: str):
        self.name = f"I'm Nobody, not {name}" if self.name != 'Nobody' else 'Nobody'
