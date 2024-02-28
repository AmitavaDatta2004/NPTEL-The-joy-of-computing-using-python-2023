def create_real_dict(sequence):
    real_dict = {}
    words = sequence.split(",")
    for word in words:
        first_letter = word[0]
        if first_letter not in real_dict:
            real_dict[first_letter] = []
        real_dict[first_letter].append(word)
    return real_dict
  
sequence=str(input(""))
real_dict = create_real_dict(sequence)
