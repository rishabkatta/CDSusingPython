class Person:
    VERSION = 3.2

    __slots__ = ( "given", "family" )

    def __init__( self, givenName, familyName ):
        self.given = givenName
        self.family = familyName

    def __str__( self ):
        return self.family + ", " + self.given