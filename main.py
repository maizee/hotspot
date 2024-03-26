from dao.models import *
from auth import get_password_hash, authenticate_user, create_access_token
from settings import *
from spider.spider import Crawler
from fastapi.middleware.cors import CORSMiddleware
from schemas import *
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()
# 创建一个加密解密上下文环境
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="API/login")

# 数据库绑定
register_tortoise(
    app,
    db_url="mysql://root:Mysql@1018@localhost:3306/hotspot",
    modules={"models": ["dao.models"]},
    add_exception_handlers=True,
    generate_schemas=True,
)
users_db = {
    "mockuser": {
        "id": 1,
        "username": "mockuser",
        "email": "mock@user.com",
        "password": "$2b$12$sErK932BEaLyIisz30PubepN7w91RLwkISWbAFYgUgoIqh8goJLEW",
    }
}


crawler = Crawler()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


@app.post("/API/register")
async def register(register: UserSign):
    try:
        pass_hash = get_password_hash(register.password)
        await User(username=register.username, password=pass_hash).save()
        return {"result": "注册成功"}
    except Exception as e:
        print("注册过程中发生了异常:", e)  # 打印异常信息
        # 或者记录到日志中
        # logger.error("注册过程中发生了异常: %s", e)
        return {"result": "注册失败"}


@app.post("/API/login")
async def login(login: OAuth2PasswordRequestForm = Depends()):
    signin = await authenticate_user(login.username, login.password)
    if not signin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if signin:
        print(signin)
        return {
            "access_token": create_access_token({"sub": signin.username}),
            "token_type": "bearer",
        }


@app.get("/API/userinfo", response_model=UserInfoModel)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # 用于判断是否处于登陆状态，以及获取用户信息
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.get(username=username)
    if user is None:
        raise credentials_exception
    return user


@app.post("/API/history/update")
async def update_history(
    history: HistoryModel, user: UserInfoModel = Depends(get_current_user)
):
    his = await History.get_or_none(title=history.title)
    if his:
        await his.delete()
    await History(username=user.username, title=history.title, href=history.href).save()
    return {"result": "添加成功"}


@app.post("/API/favor/update")
async def update_favor(
    favor: FavorModel, user: UserInfoModel = Depends(get_current_user)
):
    try:
        await Favor(
            username=user.username, title=favor.title, href=favor.href, site=favor.site
        ).save()
        return {"result": "添加成功"}
    except:
        return {"result": "获取失败"}

@app.get("/API/history/list")
async def get_history(user: UserInfoModel = Depends(get_current_user)):
    try:
        his = await History.filter(username=user.username).order_by("-time")
        return {"result": his}
    except:
        return {"result": "获取失败"}


@app.get("/API/favor/list")
async def get_favor(user: UserInfoModel = Depends(get_current_user)):
    try:
        fav = await Favor.filter(username=user.username)
        return {"result": fav}
    except Exception as e:
        print(e)
        return {"result": "获取失败"}


@app.get("/API/hot/{site}", response_model=RankListsModel)
async def get_site(site: str):
    match site:
        case "weibo":
            result = await crawler.crawler_weibo()
        case "zhihu":
            result = await crawler.crawler_zhihu()
        case "v2ex":
            result = await crawler.crawler_v2ex()
        case "tieba":
            result = await crawler.crawler_tieba()
        case "douban":
            result = await crawler.crawler_douban()
        case "tianya":
            result = await crawler.crawler_tianya()
        case "github":
            result = await crawler.crawler_github()
        case "wangyiyun":
            result = await crawler.crawler_wangyi()
    return RankListsModel(**result)
