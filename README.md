# BILIBILI SPIDER

通过API获取 bilibili 番剧/影视的详细信息和评论。

## 剧集基本信息

``http://api.bilibili.com/pgc/review/user?media_id=28229010``

mid 从番剧/影视的概览页面的 url 中获得（比如 ``https://www.bilibili.com/bangumi/media/md28229010``）。

## 剧集明细信息

方式一：``http://api.bilibili.com/pgc/view/web/season?season_id=33585``

sid 从剧集基本信息中获得。

方式二：``http://api.bilibili.com/pgc/view/web/season?ep_id=327701``

eid 可以属于任意一集。可以通过方式一或者某个视频页面的 url 获得。

## 剧集评论

按热度排序：``https://api.bilibili.com/x/v2/reply/main?type=1&oid=668491196``

按时间排序：``https://api.bilibili.com/x/v2/reply?type=1&oid=668491196``

其中，oid 就是 aid，可以通过剧集明细信息获得。
