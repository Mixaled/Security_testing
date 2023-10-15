prob_passwords = []
i = -1
while i < 10000-1:
    i+=1
    i_str = str(i).zfill(4)
    prob_passwords.append(i_str)

half_length = len(prob_passwords) // 2
first_half = prob_passwords[:half_length]
second_half = prob_passwords[half_length:]
