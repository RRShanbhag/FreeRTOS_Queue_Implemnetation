# FreeRTOS_Queue_Implemnetation
Aim: To develop communication between two tasks. 

2 tasks were implemented.
  1. Matrix Task: Implemented Matrix Multiplication and sends the result to the queue.
                  Priority: 3
  2. Reader Rask: Constantly waits for queue not to be empty. As Queue is not empty, it reads the last item from the queue.
                  Priority: 1
