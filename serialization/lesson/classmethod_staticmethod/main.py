from __future__ import annotations

class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Postion: {self.position} developer"

    @classmethod
    def from_json(cls, data):
        name = data['name']
        language = data.get('language')
        position = data.get('position')
        pr = Programmer(name=name, language=language, position=position)
        pr.enough_coffee = data.get('enough_coffee', False)
        return pr

    @staticmethod
    def to_json(obj: Programmer):
        data = {"name": obj.name, "language": obj.language, "position": obj.position}
        return data


if __name__ == "__main__":
    programmer_info = {"name": "Denis"}

    programmer = Programmer.from_json(programmer_info)

    print(programmer)
