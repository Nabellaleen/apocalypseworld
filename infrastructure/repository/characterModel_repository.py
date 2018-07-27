from domain.characterModel.repository.characterModel_repository import CharacterModelRepository as CharacterModelRepositoryInterface

class CharacterModelRepository(CharacterModelRepositoryInterface):

    models = {}

    def __init__(self):
        definitions = [
            {'title': "L'ange gardien"},
            {'title': "L'arrangeur"},
        ]
        for character_model_kw in definitions:
            character_model = CharacterModel(**character_model_kw)
            self.save(character_model)

    def find(self, id):
        return self.models.get(id)

    def save(self, characterModel):
        self.models[characterModel.id] = characterModel

    def ls(self):
        for model in self.models.values():
            yield model
