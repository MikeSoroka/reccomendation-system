from config import PROJECT_ROOT
from src.api.models.entities.user_model import UserModel


class DatasetExporter:
    def __init__(self, user: UserModel, dataset: Dataset):
        self.user = user
        self.dataset = dataset