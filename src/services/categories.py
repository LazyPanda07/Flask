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

    def __init__(self):
        self.model = CategoriesModel()

    def create_category(self, attributes: dict):
        if "user_id" not in session:
            raise UnAuthorized

        attributes["user_id"] = session["user_id"]

        try:
            return self.get_category_by_id(self.model.create(attributes))
        except sqlite3.Error:
            raise CategoryAlreadyExist

    def get_category_by_name(self, attributes: dict):
        pass

    def get_category_by_id(self, id: int):
        if "user_id" not in session:
            raise UnAuthorized

        category = self.model.get_by_id(id)

        if category is None:
            raise CategoryDoesntExist

        return category

    def edit_category_by_id(self, category_id: int, attributes: dict):
        if "user_id" not in session:
            raise UnAuthorized

        if self.model.get_by_id(category_id)["user_id"] != session["user_id"]:
            raise CategoryDoesntExist

        try:
            self.model.update(category_id, attributes)
        except sqlite3.Error:
            raise CategoryDoesntExist

    def delete_category_by_id(self, category_id: int):
        if "user_id" not in session:
            raise UnAuthorized

        if self.model.get_by_id(category_id)["user_id"] != session["user_id"]:
            raise CategoryDoesntExist

        try:
            self.model.delete(category_id)
        except sqlite3.Error:
            raise CategoryDoesntExist

    def get_categories(self):
        if "user_id" not in session:
            raise UnAuthorized

        result = self.model.get_by_field("user_id", session["user_id"])

        if result is None:
            raise NoCategories

        return result
