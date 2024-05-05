from duckduckgo_search import ddg_suggestions
from duckduckgo_search import ddg_translate, ddg, ddg_news
ddg_suggestions("马克龙")

# 1. 直接获取词条
print("suggetstion test:\n", ddg_suggestions("马克龙"), "\n")
'''
suggetstion test:
 [{'phrase': '马克龙竞选拍照钱想报销被拒'}, {'phrase': '马克龙希望德尚继续执教国家队'}, {'phrase': '马克龙被兴奋庆祝的球员晾在一边'}, {'phrase': '马克龙将在g20峰会后致电普京'}, {'phrase': '马克龙晒姆巴佩吉鲁比赛照'}, {'phrase': '马克龙访华'}, {'phrase': '马克龙支持将堕胎权写入法国宪法'}, {'phrase': '马克龙妻子'}] 
'''

# 2. translate
print("translate test: \n", ddg_translate("中国有多少人口", to = "en"))
'''
translate test: 
 [{'detected_language': 'zh-Hans', 'translated': 'How much population is China', 'original': '中国有多少人口'}]
'''

# 3. search page
r = ddg("马克龙、冯德莱恩访华", max_results=5)
for page in r:
    print("page test:\n", page, "\n")

# 4. search news
print("news test:\n", ddg_news("张继科事件", safesearch='Off', time='d', max_results=5))
'''
news test:
 [{'date': '2023-04-15T05:17:00', 'title': '张继科床照事件引发严重质疑，体育明星该如何保持高尚品德和行为', 'body': '近日，一则关于中国乒乓球运动员张继科的床照事件在互联网上引起了轩然大波。这些照片中，张继科被拍到在床上与一名女子拥抱，并且照片中的氛围颇显暧昧，引发了一场轩然大波。 这一事件让人对张继科的品德产生了严重的质疑，让我们不得不重新审视这位曾经被誉为乒乓球界的偶像的行为。 作为一名公众人物，张继科在社会舞台上担负着很大的社会责任。作为中国乒乓球队的一员，他不仅代表了国家和民族的形象，更是年轻一代的榜样。', 'url': 'https://www.163.com/dy/article/I2C9TJ3B05562MYS.html', 'image': None, 'source': '网易'}, {'date': '2023-04-15T02:11:00', 'title': '张继科事件再传!小时候在网上睡觉可不是那么容易被曝光的', 'body': 'Jike被曝欠债，散播前女友景甜的私密视频，惹来不小的风波。而他本人，也从光鲜亮丽的奥运冠军，摇身一变成为红极一时的"绝情男"。 后来，张继科和皮友良之前就谈过恋爱，这个消息更是让大家震惊。两个人在日常生活中可以说是完全格格不入，甚至都没有过交集。张继科和皮友良也是个人。它是如何走到一起的？不少网友对此提出质疑，认为这只是一种宣传手段，或者说反派是想通过这种方式来拉高自己的知名度。毕竟反派是网红，', 'url': 'https://www.163.com/dy/article/I2BVA6FT05561UMW.html', 'image': None, 'source': '网易'}, {'date': '2023-04-14T17:43:00', 'title': '狗仔曝张继科事件内幕又添新料', 'body': '张继科居住在上海，拥有豪车和高端房产，生活非常奢华。他还玩高尔夫等高端运动，与一些有不良嗜好的朋友交往。在不久前的一些八卦事件中，张继科被指控赌博借钱不还、传播女明星的私密照片等问题。 狗仔还提到张继科和现女友张蕊已经生子，但没有领证，女方很有家底，是个富家千金。狗仔最后还说张继科还曾发过别的女性的私密照。大家认为这个消息是真的吗？ 一个人的品德和行为应该是我们选择朋友或伴侣时所关注的首要因素。我', 'url': 'https://new.qq.com/rain/a/20230413A07U8900', 'image': 'https://inews.gtimg.com/om_bt/O7URdZTcE5XJkEV8u4TwAYUcN9khc9uj3FHwyHYpyKETYAA/1000', 'source': '腾讯网'}, {'date': '2023-04-14T11:54:00', 'title': '张继科事件持续发酵!欠债多达1700万，现女友被扒：离过婚生了娃', 'body': '最近一段时间，体坛热度最高的事情，毫无疑问是关于张继科的。这位国乒大满贯得主，目前已经成为众矢之的，而且丑闻仍在持续发酵。最关键的是，现在连娱乐圈也开始扒张继科的猛料了，接下来估计有更多的内幕会被曝光。 众所周知，娱乐圈中有一位"百科全书"式的人物，他有非常多的人脉和资源，因此每次有大事发生之时，吃瓜群众都在等着他发声。没错，这个人就是狗仔卓伟。 近日，卓伟曝光了关于张继科事件的一些后续。他表示，', 'url': 'https://new.qq.com/rain/a/20230414A086WS00', 'image': 'https://inews.gtimg.com/news_bt/ODLPndHCDP435bA9AD5gf85NWhttes0rhCXFFUIl376W8AA/1000', 'source': '腾讯网'}, {'date': '2023-04-14T10:43:00', 'title': '张继科"债主"名单曝光!欠债1.9亿，孙颖莎、陈梦都借给过他钱', 'body': '4月14日，时隔数日，前中国乒乓球运动员、奥运冠军张继科再次登上热搜，成为国内媒体、球迷关注的焦点!日前，娱乐圈第一狗仔卓伟重出江湖，曝出更多关于张继科的猛料、细节，情节远比大家想象中的要恶劣。据卓伟爆料称，张继科将某女明星的隐私视频、照片给债主抵债确有其事。此外，卓伟还在爆料中提到，曾在2020年1月，他接到过一个来自境外的电话，电话那头的人想请他帮忙向景甜要钱。 据电话那头的人透露，张继科因*', 'url': 'https://www.sohu.com/a/666759410_120875314', 'image': 'https://p3.itc.cn/images01/20230414/4d10b6a3d4194ba4bd2c61323b3a9dfe.jpeg', 'source': '搜狐'}]
'''
