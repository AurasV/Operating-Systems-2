#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <dirent.h>
#include <pthread.h>

#define MAX_FILES 100
#define MAX_FILENAME_LEN 256
#define MAX_WORD_LEN 100

char filenames[MAX_FILES][MAX_FILENAME_LEN];
int file_count = 0;
char search_word[MAX_WORD_LEN];
int word_count = 0;
pthread_mutex_t lock;

void strtolower(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

void* count_word_occurrences(void* arg) {
    long tid = (long)arg;
    int start = (file_count / 4) * tid;
    int end = (tid == 3) ? file_count : start + (file_count / 4);

    for (int i = start; i < end; ++i) {
        FILE* file = fopen(filenames[i], "r");
        if (!file) continue;

        char word[MAX_WORD_LEN];
        while (fscanf(file, "%99s", word) == 1) {
            strtolower(word);
            if (strcmp(word, search_word) == 0) {
                pthread_mutex_lock(&lock);
                ++word_count;
                pthread_mutex_unlock(&lock);
            }
        }
        fclose(file);
    }
    return NULL;
}

int main() {
    char path[256];
    printf("Enter the path to the directory: ");
    scanf("%s", path);
    printf("Enter the word to search for: ");
    scanf("%s", search_word);
    strtolower(search_word);

    DIR* dir = opendir(path);
    if (!dir) {
        printf("Failed to open directory: %s\n", path);
        return 1;
    }

    struct dirent* entry;
    while ((entry = readdir(dir)) != NULL && file_count < MAX_FILES) {
        if (entry->d_type == DT_REG) {
            snprintf(filenames[file_count++], MAX_FILENAME_LEN, "%s/%s", path, entry->d_name);
        }
    }
    closedir(dir);

    pthread_t threads[4];
    pthread_mutex_init(&lock, NULL);

    for (int i = 0; i < 4; i++) {
        pthread_create(&threads[i], NULL, count_word_occurrences, (void*)(size_t)i);
    }

    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("The word '%s' was found %d times.\n", search_word, word_count);
    pthread_mutex_destroy(&lock);

    return 0;
}
