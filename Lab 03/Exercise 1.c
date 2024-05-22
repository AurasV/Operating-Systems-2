#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int add = 0;  
int rem = 0;
int num = 0;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t can_produce = PTHREAD_COND_INITIALIZER;
pthread_cond_t can_consume = PTHREAD_COND_INITIALIZER;

void* producer(void* arg) {
    for (int i = 0; i < 25; ++i) {
        pthread_mutex_lock(&mutex);
        while (num == BUFFER_SIZE) {
            pthread_cond_wait(&can_produce, &mutex);
        }

        buffer[add] = i;
        add = (add + 1) % BUFFER_SIZE;
        ++num;

        printf("Waiter added order %d\n", i);
        pthread_cond_signal(&can_consume);
        pthread_mutex_unlock(&mutex); 

        sleep(1);
    }
    return NULL;
}

void* consumer(void* arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        while (num == 0) {
            pthread_cond_wait(&can_consume, &mutex);
        }

        int order = buffer[rem];
        rem = (rem + 1) % BUFFER_SIZE;
        --num;

        printf("Cook prepared order %d\n", order);
        pthread_cond_signal(&can_produce);
        pthread_mutex_unlock(&mutex); 

        sleep(2);
    }
    return NULL;
}

int main() {
    pthread_t ptid, ctid;

    pthread_create(&ptid, NULL, producer, NULL);
    pthread_create(&ctid, NULL, consumer, NULL);

    pthread_join(ptid, NULL);
    pthread_join(ctid, NULL);

    return 0;
}