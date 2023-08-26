#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt") -> None:
        self.name=name
        self.breed=breed


fido=Dog("Fido","Beagle")
print(fido.breed)
