#include <stdio.h>
#include <string.h>

void swap(char* x, char* y) {
    char temp = *x;
    *x = *y;
    *y = temp;
}

void wirelessPhoneGame(char* word, int n) {
    int len = strlen(word);
    if (n > len) {
        n = n % len;
    }

    for (int i = 0; i < n / 2; ++i) {
        swap(&word[i], &word[n - i - 1]);
    }
}


int main() {
    char word[100];
    int n;

    printf("Enter a word: ");
    scanf_s("%s", word, (unsigned)sizeof(word));
    printf("Enter the number of players: ");
    scanf_s("%d", &n);

    wirelessPhoneGame(word, n);

    printf("Distorted message: %s\n", word);

    return 0;
}
