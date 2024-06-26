import time
from httpx import AsyncClient,ConnectError
from settings import BASE_HEADERS

client = AsyncClient()

def retry(max_tries=3, wait=1):
    """
    获取失败，进行再次爬取
    :param max_tries: 失败次数
    :param wait: 每次失败时等待时间
    :return:
    """
    def deco(fun):
        def wrapper(*args, **kwargs):
            for i in range(max_tries):
                result = fun(*args, **kwargs)
                if result is None:
                    print('retry%s' %i)
                    time.sleep(wait)
                    continue
                else:
                    return result
        return wrapper
    return deco


@retry()
async def get_text(url, options={}):
    """
    :param method: 请求方法
    :param url: 请求的目标url
    :param options:添加的请求头
    :return:
    """
    headers = dict(BASE_HEADERS, **options)
    print('正在抓取', url)
    try:
        res = await client.get(url=url, headers=headers, timeout=5)
        # print(res.status_code)
        if res.status_code == 200:
            print('抓取成功', url, res.status_code)
            return res
    except ConnectError:
        print('抓取失败', url)
        return None
