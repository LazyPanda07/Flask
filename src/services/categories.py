from flask import session
from models import CategoriesModel


class CategoryDoesntExist(Exception):
    pass


class CategoryAlreadyExist(Exception):
    pass


class UnAuthorized(Exception):
    pass


class CategoriesService:

    def __init__(self):
        self.model = CategoriesModel()

    def create_category(self, attributes: dict):
        if not "user_id" in session:
            raise UnAuthorized

        return self.get_category_by_id(self.model.create(attributes))

    def get_category_by_name(self, attributes: dict):
        pass

    def get_category_by_id(self, id: int):
        category = self.model.get_by_id(id)

        if category is None:
            raise CategoryDoesntExist

        return category

    def edit_category_by_id(self, attributes: dict):
        pass

    def delete_category_by_id(self, attributes: dict):
        pass

    def get_categories(self):
        pass
