class TagCloud:
    def __init__(self):
        self.tags = {}  # dictionary

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(
            tag.lower(), 0) + 1  # key, value

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
print(len(cloud))

cloud.add("Python")
print(cloud.tags)

cloud.add("pYthon")
print(cloud.tags)

cloud.add("pyThon")
print(cloud.tags)
print(len(cloud))

print(cloud.__getitem__("python"))

# 키는 그대로 파이썬이고 밸류값(count)만 계속 바뀌는 코드
