#include <stdio.h>
#include <pthread.h>

#define NUM_YEARS 10

double interestRate = 0.007;
double deposit = 1000.0;
int currentYear = 0;

pthread_mutex_t lock;
pthread_cond_t cond;

void* performCalculation(void* arg) {
    long year = (long)arg;

    pthread_mutex_lock(&lock);
    while (year != currentYear) {
        pthread_cond_wait(&cond, &lock);
    }

    for (int i = 0; i < 12; i++) {
        deposit += deposit * interestRate;
    }
    printf("Year %ld: Deposit = %.2f\n", year + 1, deposit);

    currentYear++; 
    pthread_cond_broadcast(&cond);
    pthread_mutex_unlock(&lock);

    return NULL;
}

int main() {
    pthread_t threads[NUM_YEARS];
    pthread_mutex_init(&lock, NULL);
    pthread_cond_init(&cond, NULL);

    for (long i = 0; i < NUM_YEARS; i++) {
        pthread_create(&threads[i], NULL, performCalculation, (void*)i);
    }

    for (int i = 0; i < NUM_YEARS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&lock);
    pthread_cond_destroy(&cond);

    printf("Final Deposit after %d years: %.2f\n", NUM_YEARS, deposit);
    return 0;
}
