#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_PARKING_SPACES 5
#define NUM_CARS 10

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t can_park = PTHREAD_COND_INITIALIZER;

int available_spaces = MAX_PARKING_SPACES;

void* car_routine(void* arg) {
    int car_id = (int)arg;
    srand(time(NULL) ^ (car_id << 16));

    while (1) {
        pthread_mutex_lock(&mutex);

        while (available_spaces <= 0) {
            printf("Car %d is waiting for a parking space.\n", car_id);
            pthread_cond_wait(&can_park, &mutex);
        }

        available_spaces--;
        printf("Car %d has entered the parking lot. Spaces left: %d\n", car_id, available_spaces);

        pthread_mutex_unlock(&mutex);

        sleep(rand() % 3 + 1);

        pthread_mutex_lock(&mutex);
        available_spaces++;
        printf("Car %d has left the parking lot. Spaces available: %d\n", car_id, available_spaces);
        pthread_mutex_unlock(&mutex);

        pthread_cond_signal(&can_park);

        sleep(rand() % 5 + 1);
    }

    free(arg);
    return NULL;
}

int main() {
    pthread_t cars[NUM_CARS];

    for (int i = 0; i < NUM_CARS; i++) {
        int* car_id = malloc(sizeof(int));
        *car_id = i;
        if (pthread_create(&cars[i], NULL, car_routine, (void*)(intptr_t)*car_id) != 0) {
            perror("Failed to create the car thread");
            return 1;
        }
        free(car_id);
    }

    for (int i = 0; i < NUM_CARS; i++) {
        pthread_join(cars[i], NULL);
    }

    return 0;
}
