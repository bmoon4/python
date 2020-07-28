class TagCloud:
    def __init__(self):
        self.__tags = {}  # dictionary

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(
            tag.lower(), 0) + 1  # key, value

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
print(cloud.__dict__)
print(cloud._TagCloud__tags)
# 키는 그대로 파이썬이고 밸류값(count)만 계속 바뀌는 코드
