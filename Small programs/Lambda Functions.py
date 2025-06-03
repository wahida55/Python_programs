#Lambda functions are small anonymous functions defined using the keyword lambda.

#uppercase = lambda s: s.lower()
#print(uppercase("WahIda"))

# vowels = lambda v: for v in "aeiou"
# print(vowels("Wahida"))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(6))
print(n(-3))
print(n(0))
