# template for making PartyAnimal objects
class PartyAnimal:
    # each PartyAnimal object has a bit of data
    x = 0

    def party(self):
        self.x = self.x +1
        print("So far", self.x)

# construct a PartyAnimal object and store in a variable
an = PartyAnimal()

# PartyAnimal.party(an)
an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir ", dir(an))
