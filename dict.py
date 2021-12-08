class dict:
    def __init__(self,l=[]):
        self.ht = []
        self.update(l)
    def __getitem__(self,key):
        return self.get(key,-1)
    def __str__(self):
        return str(self.items())
    def __setitem__(self,key,value):
        self.setdefault(key,value)
    def __contains__(self,key):
        for e in self.ht:
            if e[0] == key: return True
        return False
    def update(self,l):
        for e in l:
            self.setdefault(e[0],e[1])
    def copy(self):
        return dict(self.items())
    def clear(self):
        self.ht = []
    def findIndex(self,key):
        def hash(key):
            ans = key
            if not isinstance(key,int):
                ans = 0
                for i in key:
                    ans = (ans+ord(i)) % 17
            return ans%17
        h = hash(key)
        while True:
            if h>len(self.ht) or self.ht[h][0]=='' or self.ht[h][0]==key:
                return h
            h+=17
    def setdefault(self,key,value):
        index = self.findIndex(key)
        if index>len(self.ht):
            self.ht += [["",""] for _ in range(17)]
        self.ht[index] = [key,value]
        return self.ht[index]
    def get(self,key,value):
        index = self.findIndex(key)
        if index>len(self.ht) or self.ht[index][0]=='':
            return value
        return self.ht[index][1]
    def keys(self):
        keys = []
        for e in self.ht:
            if e[0]!='':
                keys.append(e[0])
        return keys
    def values(self):
        values = []
        for e in self.ht:
            if e[0]!='':
                values.append(e[1])
        return values
    def items(self):
        items = []
        for e in self.ht:
            if e[0]!='':
                items.append(e)
        return items
    def pop(self,key):
        index = findIndex(key)
        if self.ht[index][0]==key:
            self.ht.pop(index)
d = dict()
d["123"]=12
a = d
print(a["123"])
a[123]=12
print(a)
print(d)
