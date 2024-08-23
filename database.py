from typing import Optional, Any

import pymongo
import uuid
from datetime import datetime

import config


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client["My_Big_bot"]

        self.user_collection = self.db["user"]
        self.dialog_collection = self.db["dialog"]

    def check_if_user_exists(self, user_id: int, raise_exception: bool = False):
        if self.user_collection.count_documents({"_id": user_id}) > 0:
            return True
        else:
            if raise_exception:
                raise ValueError(f"User {user_id} does not exist")
            else:
                return False

    def add_new_user(
        self,
        user_id: int,
        chat_id: int,
        username: str = "",
        first_name: str = "",
        last_name: str = "",
        phonenumber: str = "None",
        balance: int = 0,
        channels: str = "None",
        posts: str = "",
        totalwithdraw: int = 0
    ):
        user_dict = {
            "_id": user_id,
            "chat_id": chat_id,

            "username": username,
            "first_name": first_name,
            "last_name": last_name,

            "last_interaction": datetime.now(),
            "first_seen": datetime.now(),

            "phonenumber": phonenumber,
            "balance": balance,
            "channels": channels,

            "posts": posts,

            "totalwithdraw": totalwithdraw
        }

        if not self.check_if_user_exists(user_id):
            self.user_collection.insert_one(user_dict)

    
    def get_user_attribute(
        self,
        user_id: int,
        username: str,
        first_name:str,
        last_name:str,
        phonenumber:str,
        balance: int,
        channels:str,
        posts:str,
        totalwithdraw:int,
        key: str):
        self.check_if_user_exists(user_id, raise_exception=True)
        user_dict = self.user_collection.find_one({
            "_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "phonenumber": phonenumber,
            "balance": balance,
            "channels": channels,

            "posts": posts,

            "totalwithdraw": totalwithdraw})

        if key not in user_dict:
            return None

        return user_dict[key]

    def set_user_attribute(self, user_id: int, key: str, value: Any):
        self.check_if_user_exists(user_id, raise_exception=True)
        self.user_collection.update_one({"_id": user_id}, {"$set": {key: value}})

    def update_balance(self, user_id: int, balance: int, totalwithdraw: int):
        update_balance = self.get_user_attribute(user_id, "balance","totalwithdraw")

        for updated_balance in update_balance:
            updated_balance == int(update_balance["balance"]) - int(update_balance['totalwithdraw'])
            return updated_balance
        
        self.set_user_attribute(user_id, "balance", updated_balance)

    def get_dialog_messages(self, user_id: int, dialog_id: Optional[str] = None):
        self.check_if_user_exists(user_id, raise_exception=True)

        if dialog_id is None:
            dialog_id = self.get_user_attribute(user_id, "current_dialog_id")

        dialog_dict = self.dialog_collection.find_one({"_id": dialog_id, "user_id": user_id})
        return dialog_dict["messages"]

    