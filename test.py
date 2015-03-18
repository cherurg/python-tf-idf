import tfidf

table = tfidf.tfidf()
table.addDocument("foo", ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel"])
table.addDocument("bar", ["alpha", "bravo", "charlie", "india", "juliet", "kilo"])
table.addDocument("baz", ["kilo", "lima", "mike", "november"])

# print(table.vector("foo"))
# print(table.vector("bar"))
# print(table.vector("baz"))
# print(table._vectors)

table.vector("foo")
table.vector("bar")
table.vector("baz")
print(table.vectors())

print(table.cos("foo", "baz"))