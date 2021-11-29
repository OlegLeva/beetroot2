class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.general_set = set()

    def how_many(self, args):
        my_set = set()
        for name in args:
            my_set.add(name.lower())
        diff_set = my_set.difference(self.general_set)
        self.general_set |= my_set
        return len(diff_set)


a = Song('Go', 'Pearl Jam')

print(a.how_many(['John', 'john', 'ivan', 'Ivan', 'oleg']))
print((a.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE'])))


'''https://www.codewars.com/kata/search/python?beta=false&q=&r%5B%5D=-7&tags=Classes&xids=played'''