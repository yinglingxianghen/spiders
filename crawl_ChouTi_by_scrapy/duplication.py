
class RepeatFilter(object):
    def __init__(self):  2 对象初始化
        self.visited_set = set()
    @classmethod   1#创建了对象
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        if request.url in self.visited_set:
            return True 4 检查是否爬取过
        self.visited_set.add(request.url)
        return False

    def open(self):  # can return deferred
        # print('open')3 开始爬取
        pass

    def close(self, reason):  # can return a deferred
        # print('close') 5停止
        pass
    def log(self, request, spider):  # log that a request has been filtered
        # print('log....')
        pass