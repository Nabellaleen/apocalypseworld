import inject

from infrastructure.repository.characterModel_repository import CharacterModelRepository
from domain.characterModel.repository.characterModel_repository import CharacterModelRepository as CharacterModelRepositoryInterface

def my_config(binder):
    binder.bind(CharacterModelRepositoryInterface, CharacterModelRepository())

inject.configure(my_config)
