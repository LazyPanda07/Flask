import sqlite3
from flask import session
from models import CategoriesModel


class CategoryDoesntExist(Exception):
    pass


class CategoryAlreadyExist(Exception):
    pass


class UnAuthorized(Exception):
    pass


class NoCategories(Exception):
    pass


class CategoriesService:

    @staticmethod
    def _check_same_user(user_id: int, category: dict):
        if category is None or user_id != category["user_id"]:
            raise CategoryDoesntExist

    def __init__(self):
        self.model = CategoriesModel()

    def create_category(self, attributes: dict, user):
        attributes["user_id"] = user["id"]

        try:
            return self.get_category_by_id(self.model.create(attributes), user)
        except sqlite3.Error:
            raise CategoryAlreadyExist

    def get_category_by_id(self, id: int, user):
        category = self.model.get_by_id(id)

        if category is None or category["user_id"] != user["id"]:
            raise CategoryDoesntExist

        return category

    def edit_category_by_id(self, category_id: int, attributes: dict, user):
        check = self.model.get_by_id(category_id)

        self._check_same_user(user["id"], check)

        try:
            self.model.update(category_id, attributes)
        except sqlite3.Error:
            raise CategoryDoesntExist

    def delete_category_by_id(self, category_id: int, user):
        check = self.model.get_by_id(category_id)

        self._check_same_user(user["id"], check)

        try:
            self.model.delete(category_id)
        except sqlite3.Error:
            raise CategoryDoesntExist

    def get_categories(self, user):
        result = self.model.get_list_condition(f"user_id = {user['id']}")

        if result is None:
            raise NoCategories

        return result
