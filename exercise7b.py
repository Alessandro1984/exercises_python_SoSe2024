def buchstaben_zählen_(wort):
    letter_count = 0
    
    for buchstabe in wort:
        if buchstabe.isalpha():
            letter_count += 1
    
    return letter_count

print(buchstaben_zählen_("Hallo, Berlin!"))
