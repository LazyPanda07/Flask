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

    def _check_same_user_id(function):
        def wrapper(self, *args):
            try:
                if self.model.get_by_id(args[0])["user_id"] != session["user_id"]:
                    raise CategoryDoesntExist
            except Exception:  # None
                raise CategoryDoesntExist

            return function(self, *args)

        return wrapper

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

    @_check_same_user_id
    def edit_category_by_id(self, category_id: int, attributes: dict):
        try:
            self.model.update(category_id, attributes)
        except sqlite3.Error:
            raise CategoryDoesntExist

    @_check_same_user_id
    def delete_category_by_id(self, category_id: int):
        try:
            self.model.delete(category_id)
        except sqlite3.Error:
            raise CategoryDoesntExist

    def get_categories(self, user):
        result = self.model.get_list_condition(f"user_id = {user['id']}")

        if result is None:
            raise NoCategories

        return result
