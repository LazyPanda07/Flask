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


def check_authorization(function):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            raise UnAuthorized

        return function(*args, **kwargs)

    return wrapper


class CategoriesService:

    def __init__(self):
        self.model = CategoriesModel()

    @check_authorization
    def create_category(self, attributes: dict):
        attributes["user_id"] = session["user_id"]

        try:
            return self.get_category_by_id(self.model.create(attributes))
        except sqlite3.Error:
            raise CategoryAlreadyExist

    @check_authorization
    def get_category_by_id(self, id: int):
        category = self.model.get_by_id(id)

        if category is None or category["user_id"] != session["user_id"]:
            raise CategoryDoesntExist

        return category

    @check_authorization
    def edit_category_by_id(self, category_id: int, attributes: dict):
        if self.model.get_by_id(category_id)["user_id"] != session["user_id"]:
            raise CategoryDoesntExist

        try:
            self.model.update(category_id, attributes)
        except sqlite3.Error:
            raise CategoryDoesntExist

    @check_authorization
    def delete_category_by_id(self, category_id: int):
        if self.model.get_by_id(category_id)["user_id"] != session["user_id"]:
            raise CategoryDoesntExist

        try:
            self.model.delete(category_id)
        except sqlite3.Error:
            raise CategoryDoesntExist

    @check_authorization
    def get_categories(self):
        result = self.model.get_list_condition(f"user_id = {session['user_id']}")

        if result is None:
            raise NoCategories

        return result
