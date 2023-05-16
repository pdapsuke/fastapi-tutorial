from typing import Optional
from pydantic import BaseModel

class UserResponseSchema(BaseModel):
    """レスポンスで返却する項目と型を定義するクラス"""
    id: int
    username: str
    age: Optional[int]

    class Config:
        # orm_mode = True とすると、DBのレスポンスをシームレスにオブジェクトに変換できる
        orm_mode = True

class UserPostSchema(BaseModel):
    """ユーザー作成APIのリクエストとして渡されるパラメータと型を定義"""
    username: str
    password: str
    age: int

class UserPutSchema(BaseModel):
    password: str
    age: int