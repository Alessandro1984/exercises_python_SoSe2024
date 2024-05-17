def buchstaben_zählen(wort):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöü"
    wort_lower =  wort.lower()
    wort_list = list(wort_lower)
    wort_letter = [buchstabe for buchstabe in wort_list if buchstabe in alphabet]
    print(len(wort_letter))
    
buchstaben_zählen("Hallo, Berlin!ß")