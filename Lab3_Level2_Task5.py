def char_frequency(s):
    freq = {}
    length = len(s)

    for i in range(length):
        ch = s[i]
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] += 1
    return freq

# приклад:
text = input("Введіть рядок: ")
result = char_frequency(text)
print("Частота символів:", result)
