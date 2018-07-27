class CharacterModel:

    def __init__(self, title: str):
        self.id = uuid4()
        self.title = title
        self.profils = set()
        self.actions = set()
