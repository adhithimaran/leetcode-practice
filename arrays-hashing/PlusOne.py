def plusOne(digits):
    # Start from the rightmost digit
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

digits = [8,9,9,9]
print(plusOne(digits))