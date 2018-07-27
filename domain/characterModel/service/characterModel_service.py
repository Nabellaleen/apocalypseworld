import inject

from domain.characterModel.repository.characterModel_repository import CharacterModelRepository

class CharacterModelService:
    
    def __init__(self):
        self.character_model_repository = inject.attr(CharacterModelRepository)

    def create_character(self, model_id) -> None:
        # TODO - create a character from a character model
        pass

    def add_action(self, character_model_id, action) -> None:
        character_model = self.character_model_repository.find(character_model_id)

        assert action.id not in character_model.actions, 'Action {} already in Character Model {}'.format(
            action.id, character_model.id)

        character_model.actions.add(action.id)
        self.character_model_repository.save(character_model)

    def ls(self) -> None:
        for character_model in self.characterModel_repository.ls():
            print('{}: {}'.format(character_model.id, character_model.title))
