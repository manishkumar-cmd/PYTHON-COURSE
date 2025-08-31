marks={
    "manish":100,
    "karan":44,
    "rahul":45,
    0:"manish"
}

print(len(marks))
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"manish":99,"manjeet":88})
print(marks)

print(marks.get("manish"))
print(marks.get("manish1"))#shows none
print(marks["manish"])
