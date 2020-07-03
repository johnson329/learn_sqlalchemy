Association Proxy

不使用外键表示多对多关系


数据库事务的一致性 

https://www.zhihu.com/question/31346392

就是在既有约束下，从一个正确状态转为另外一个正确状态

https://mp.weixin.qq.com/s?__biz=MjM5Njc0MjIwMA==&mid=2649655932&idx=2&sn=ee6a400d343ae2ad2a57af78a8116780&chksm=befebf2b8989363d10660b34910077560d5954c916b7ccfd03afceb233cb6ff9f29c275ffb61&mpshare=1&scene=1&srcid=07030luMIJ1x9WhlyFfyBcz6&sharer_sharetime=1593765323104&sharer_shareid=13f00c24585f20b036a48b2ea739decb&key=a911e594c822c15b9b9d3fbeeb111e7ac39be665b8c789a9ecd4fdb52ee7fc2f8e65bad98defadaf624cfc09812f788ee6de0835f789c26d1fb23b7b6abd2a522ef1b782ac652e5693929e172fcf0beb&ascene=1&uin=MTgwMzAzNjI4NA%3D%3D&devicetype=Windows+10+x64&version=6209007b&lang=zh_CN&exportkey=AdcBp2rV%2FZIFPnCUegSu8io%3D&pass_ticket=awXdsGTfGsLF4rBSwphBaCGLGP3DyOkqoyqEeWJwDJikez%2BN5r%2BICotJBUhWGkDj

为什么数据库不应该使用外键

1.如果能够接受在一个时间窗口数据不一致的情况，那么可以不用外键，提高性能

2.数据库级联更新或者删除，会检查引用该表的表记录，性能要高于应用程序内操作，但如果多个表引用该表，级联更新或者删除会带来大量性能损失，所以放弃级联删除

或者更新，提高性能，

3.插入数据检查外键是否存在，交给应用程序



orm定义部分不变，但是数据库手动生成，没有外键，那么on_delete级联删除失效

