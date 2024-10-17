def twelve_days_of_christmas():
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves and",
        "Three french hens",
        "Four calling birds",
        "Five golden rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
    ]
    
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    for day in range(12):
        print(f"On the {ordinals[day]} day of Christmas")
        print("My true love sent to me:")
        
        for gift in range(day, -1, -1):
            if day > 0 and gift == 0:
                print(f"And {gifts[gift]}")
            else:
                print(gifts[gift])
        print()

# Chamar a função para exibir a música completa
twelve_days_of_christmas()
