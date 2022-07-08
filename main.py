import apiconnect
import dbconnect
    
try:
    conn = dbconnect.connect()
    cur = dbconnect.get_cur(conn)

except Exception as error:
    print("Cannot connect to database")
    print(error)
    raise

dbconnect.create_table(cur)

print("Enter currency pair, 'quit' to exit or 'history' for history of your commands")
inp = input("Enter a currency pair: ")

while inp.lower() != "quit":

    if inp.lower() == "history":
        print("History of your commands:")
        dbconnect.read(cur)
        inp = input("Enter a currency pair: ")

    else:
        if len(inp) != 7:
            print("Not a valid input")
            inp = input("Enter a currency pair: ")
        else:
            output = apiconnect.get_rate(inp)
            try:
                dbconnect.insert(conn, cur, inp, output[0], output[1])
            except Exception as error:
                print("Output was not written to database")
            inp = input("Enter a currency pair: ")

dbconnect.close(conn, cur)



