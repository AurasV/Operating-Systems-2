#include <stdio.h>
#include <string.h>
#include <ctype.h>

void swap(char* x, char* y) {
    char temp = *x;
    *x = *y;
    *y = temp;
}

int isVowel(char c) {
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

void toChickenLanguage(char* word, char* result) {
    while (*word != '\0') {
        *result++ = *word; 
        if (isVowel(*word)) {
            *result++ = 'p';
            *result++ = *word;
        }
        word++;
    }
    *result = '\0';
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
    char word[100], chickenWord[300] = { 0 }; 
    int n;

    printf("Enter a word: ");
    scanf_s("%s", word, (unsigned)sizeof(word));

    toChickenLanguage(word, chickenWord);
    printf("In Chicken Language: %s\n", chickenWord);

    printf("Enter the number of players: ");
    scanf_s("%d", &n);

    wirelessPhoneGame(chickenWord, n);

    printf("Distorted message: %s\n", chickenWord);

    return 0;
}
