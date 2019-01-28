import person

def main():
    print( "Code version " + str( person.Person.VERSION ) )
    p1 = person.Person( "Jay", "Park" )
    p2 = person.Person( "George", "Sterno" )
    print( str( p1 ) + "; " + str( p2 ) )

if __name__ == "__main__":
    main()
