"""An example of for... in syntax."""

names: list[str] = ["Nick", "Bill", "Josh", "Jose"]

# Example of iterating through a list of names using a while loop.
print("while output.")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for... in loop is the same as above
print("For.. in output.")
for name in names:
    print(name)