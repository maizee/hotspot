import logging
from typing import Dict, List

from lxml import etree
from .utils import get_text


class Crawler:
    # 缓存内容
    weibo = {}
    zhihu = {}
    v2ex = {}
    tieba = {}
    douban = {}
    tianya = {}
    github = {}
    wangyi = {}

    async def crawler_weibo(self) -> Dict[str, List[Dict[str, str]]]:
        """
        爬取微博热榜
        :return:
        """
        if self.weibo != {}:
            return self.weibo
        web_base_url = "https://s.weibo.com/weibo?q=%23{}%23"
        m_url = "https://m.weibo.cn/api/container/getIndex?containerid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot&title=%E5%BE%AE%E5%8D%9A%E7%83%AD%E6%90%9C&extparam=seat%3D1%26pos%3D0_0%26dgr%3D0%26mi_cid%3D100103%26cate%3D10103%26filter_type%3Drealtimehot%26c_type%3D30%26display_time%3D1638445376%26pre_seqid%3D52252862&luicode=10000011&lfid=231583"
        response_html = await get_text(m_url)
        content_list = []
        if response_html:
            res_json = response_html.json()
            try:
                card_group = res_json.get("data").get("cards")[0].get("card_group")
                for card in card_group:
                    title = card.get("desc")
                    href = web_base_url.format(title)
                    content_list.append({"title": title, "href": href})
            except Exception as e:
                logging.error("新浪微博 parser error {}".format(e))
        if self.weibo == {}:
            print("创建缓存")
            self.weibo = {"hot_name": "新浪微博", "content": content_list, "url": "https://weibo.com/hot/weibo/102803"}
        return self.weibo

    async def crawler_zhihu(self) -> Dict[str, List[Dict[str, str]]]:
        """
        获取知乎热榜
        :return:
        """
        if self.zhihu != {}:
            return self.zhihu
        url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"
        headers = {
            "path": "/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true",
            "x-api-version": "3.0.76",
            "x-requested-with": "fetch",
        }
        content_list = []
        response_html = await get_text(url, options=headers)
        if response_html:
            data_list = response_html.json().get("data", "")
            # print(data_list)
            if data_list:
                for data in data_list:
                    title = data.get("target").get("title_area").get("text", "")
                    href = data.get("target").get("link").get("url", "")
                    content_list.append({"title": title, "href": href})
        if self.zhihu == {}:
            print("创建缓存")
            self.zhihu = {"hot_name": "知乎热榜", "content": content_list, "url": url}
        return self.zhihu

    async def crawler_v2ex(self) -> Dict[str, List[Dict[str, str]]]:
        """
        爬取v2ex热榜
        :return:
        """
        if self.v2ex != {}:
            return self.v2ex
        url = "https://www.v2ex.com/?tab=hot"
        headers = {"authority": "www.v2ex.com", "referer": "https://www.v2ex.com/"}
        response_html = await get_text(url, options=headers)
        content_list = []
        if response_html:
            tree = etree.HTML(response_html.text)
            span_list = tree.xpath(
                "//div[@class='box']/div[@class='cell item']/table/tr/td[3]/span[1]"
            )
            for span in span_list:
                title = span.xpath("./a/text()")[0]
                href = "https://www.v2ex.com%s" % span.xpath("./a/@href")[0]
                content_list.append({"title": title, "href": href})
        if self.v2ex == {}:
            print("创建缓存")
            self.v2ex = {"hot_name": "V2EX", "content": content_list, "url": url}
        return self.v2ex

    async def crawler_tieba(self) -> Dict[str, List[Dict[str, str]]]:
        """
        获取贴吧热榜
        :return:
        """
        if self.tieba != {}:
            return self.tieba
        url = "http://tieba.baidu.com/hottopic/browse/topicList"
        content_list = []
        response_html = await get_text(url=url)
        if response_html:
            req_json = response_html.json()
            for i in req_json.get("data").get("bang_topic").get("topic_list"):
                title = i.get("topic_name")
                href = i.get("topic_url").replace("amp;", "")
                content_list.append({"title": title, "href": href})
        if self.tieba == {}:
            print("创建缓存")
            self.tieba = {"hot_name": "贴吧", "content": content_list, "url": url}
        return self.tieba

    async def crawler_douban(self) -> Dict[str, List[Dict[str, str]]]:
        """
        豆瓣讨论精选
        :return:
        """
        if self.douban != {}:
            return self.douban
        url = "https://www.douban.com/group/explore"
        headers = {
            "Host": "www.douban.com",
            "Referer": "https://www.douban.com/group/explore",
        }
        response_html = await get_text(url, options=headers)
        content_list = []
        if response_html:

            tree = etree.HTML(response_html.text)
            h3_list = tree.xpath("//div[@class='channel-item']/div[@class='bd']/h3")
            if h3_list.__len__() <= 0:
                h3_list = etree.HTML(response_html.content).xpath(
                    "//div[@class='channel-item']/div[@class='bd']/h3"
                )
            for h3 in h3_list:
                title = h3.xpath("./a/text()")[0]
                href = h3.xpath("./a/@href")[0]
                content_list.append({"title": title, "href": href})
        if self.douban == {}:
            print("创建缓存")
            self.douban = {"hot_name": "豆瓣", "content": content_list, "url": url}
        return self.douban

    async def crawler_tianya(self) -> Dict[str, List[Dict[str, str]]]:
        """
        获取天涯热榜贴
        :return:
        """
        if self.tianya != {}:
            return self.tianya
        url = "http://bbs.tianya.cn/hotArticle.jsp"
        headers = {"Host": "bbs.tianya.cn"}
        response_html = await get_text(url, options=headers)
        content_list = []
        if response_html:
            tree = etree.HTML(response_html.text)
            # print(response_html)
            tbody_list = tree.xpath("//div[@class='mt5']/table/tbody")[1:]
            for tbody in tbody_list:
                for tr in tbody.xpath("./tr"):
                    title = tr.xpath("./td[@class='td-title']/a/text()")[0]
                    href = (
                        "http://bbs.tianya.cn"
                        + tr.xpath("./td[@class='td-title']/a/@href")[0]
                    )
                    content_list.append({"title": title, "href": href})
        if self.tianya == {}:
            print("创建缓存")
            self.tianya = {"hot_name": "天涯", "content": content_list, "url": url}
        return self.tianya

    async def crawler_github(self) -> Dict[str, List[Dict[str, str]]]:
        """
        获取github 热榜
        :return:
        """
        if self.github != {}:
            return self.github
        url = "https://github.com/trending"
        headers = {"Host": "github.com", "Referer": "https://github.com/explore"}
        response_html = await get_text(url, options=headers)
        content_list = []
        if response_html:
            tree = etree.HTML(response_html.text)
            if tree == None:
                tree = etree.HTML(response_html.content)
            article_list = tree.xpath("//article[@class='Box-row']")
            for article in article_list:
                title = article.xpath("string(./h1/a)").strip()
                href = "https://github.com/%s" % article.xpath("./h1/a/@href")[0]
                describe = article.xpath("string(./p)").strip()
                content_list.append(
                    {"title": "%s---%s" % (title, describe), "href": href}
                )
        if self.github == {}:
            print("创建缓存")
            self.github = {"hot_name": "github", "content": content_list, "url": url}
        return self.github

    async def crawler_wangyi(self) -> Dict[str, List[Dict[str, str]]]:
        """
        爬取网易云音乐榜单
        :return:
        """
        if self.wangyi != {}:
            return self.wangyi
        url = "https://music.163.com/discover/toplist?id=19723756"
        headers = {
            "authority": "music.163.com",
            "referer": "https://music.163.com/",
        }
        response_html = await get_text(url, options=headers)
        content_list = []
        if response_html:
            tree = etree.HTML(response_html.text)
            ul_list = tree.xpath(
                '//div[@id="song-list-pre-cache"]/ul[@class="f-hide"]/li'
            )
            for li in ul_list:
                title = li.xpath("./a/text()")[0]
                href = "https://music.163.com/#%s" % li.xpath("./a/@href")[0]
                content_list.append({"title": title, "href": href})
        if self.wangyi == {}:
            print("创建缓存")
            self.wangyi = {"hot_name": "云音乐飙升榜", "content": content_list, "url": url}
        return self.wangyi


if __name__ == "__main__":
    pass
