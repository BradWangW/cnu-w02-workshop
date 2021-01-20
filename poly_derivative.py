# Polynomial coefficients
a0 = 1
a1 = -2
a2 = 4.6
a3 = 0.2

# Point at which we evaluate the derivative
x0 = 3.1

coeff = [a0, a1, a2, a3]
coeff_prime = []
for i in range(1, 4):
    coeff_prime.append(i * coeff[i])

print(coeff_prime)

p_prime = coeff_prime[0] + coeff_prime[1] * x0 + coeff_prime[2] * x0 ** 2






# This will be True if the code is correct
print(p_prime == 32.286)