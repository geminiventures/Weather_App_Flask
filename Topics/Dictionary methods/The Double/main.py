# put your python code here
alpha = list(map(chr, range(97, 123)))
alpha_double = [letter + letter for letter in alpha]
double_alphabet = {alpha[letter]: alpha_double[letter] for letter in range(len(alpha_double))}
