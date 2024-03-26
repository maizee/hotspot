from pydantic import BaseModel

# 用于检测爬虫返回数据
class LinkModel(BaseModel):
    title: str
    href: str


class RankListsModel(BaseModel):
    hot_name: str
    content: list[LinkModel]
    url: str


# 用户登录数据验证
class UserSign(BaseModel):
    username: str
    password: str


class HistoryModel(BaseModel):
    title: str
    href: str


class FavorModel(BaseModel):
    site: str
    title: str
    href: str


class UserInfoModel(BaseModel):
    username: str


class TokenModel(BaseModel):
    token: str
