#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>

long long isPrime(long long n, long long iterations);
long long gcd(long long a, long long b);
long long modInverse(long long a, long long m);
long long modPow(long long base, long long exponent, long long mod);
void generateRandomPrimes(long long *p, long long *q, long long min, long long max);
void generateKeys(long long p, long long q, long long *n, long long *e, long long *d);
void encryptString(const char *input, long long *encrypted, long long e, long long n);
void decryptString(const long long *encrypted, char *output, long long d, long long n);

long long main() {
    srand(time(NULL));

    long long p, q;
    generateRandomPrimes(&p, &q, 100, 300);

    long long n, e, d;
    generateKeys(p, q, &n, &e, &d);

    char input[] = "FaV, 1221EC - IoT";
    long long encrypted[strlen(input)];
    char decrypted[strlen(input) + 1];

    encryptString(input, encrypted, e, n);
    decryptString(encrypted, decrypted, d, n);

    printf("Original: %s\n", input);
    printf("Encrypted: ");
    for (long long i = 0; encrypted[i] != -1; i++) {
        printf("%d ", encrypted[i]);
    }
    printf("\nDecrypted: %s\n", decrypted);

    return 0;
}

void generateRandomPrimes(long long *p, long long *q, long long min, long long max) {
    do {
        *p = min + rand() % (max - min);
    } while (!isPrime(*p, 5));

    do {
        *q = min + rand() % (max - min);
    } while (!isPrime(*q, 5) || *q == *p);
}

long long isPrime(long long n, long long iterations) {
    if (n <= 1 || (n > 2 && n % 2 == 0)) return 0;
    for (long long i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

long long gcd(long long a, long long b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

long long modInverse(long long a, long long m) {
    for (long long x = 1; x < m; x++) {
        if (((a%m) * (x%m)) % m == 1)
            return x;
    }
    return -1;
}

long long modPow(long long base, long long exponent, long long mod) {
    long long result = 1;
    base = base % mod;
    while (exponent > 0) {
        if (exponent % 2 == 1)
            result = (result * base) % mod;
        exponent = exponent >> 1;
        base = (base * base) % mod;
    }
    return result;
}

void generateKeys(long long p, long long q, long long *n, long long *e, long long *d) {
    *n = p * q;
    long long phi = (p - 1) * (q - 1);

    *e = 3;
    while (gcd(*e, phi) != 1) {
        (*e)++;
    }

    *d = modInverse(*e, phi);
}

void encryptString(const char *input, long long *encrypted, long long e, long long n) {
    long long i = 0;
    while (input[i] != '\0') {
        encrypted[i] = modPow(input[i], e, n);
        i++;
    }
    encrypted[i] = -1;
}

void decryptString(const long long *encrypted, char *output, long long d, long long n) {
    long long i = 0;
    while (encrypted[i] != -1) {
        output[i] = modPow(encrypted[i], d, n);
        i++;
    }
    output[i] = '\0';
}
