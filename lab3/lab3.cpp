#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

class Queue {
private:
    Node* front;
    Node* rear;  
    int count;   
public:
    Queue() : front(nullptr), rear(nullptr), count(0) {}

    void enqueue(int value) {
        Node* newNode = new Node(value);
        if (rear) {
            rear->next = newNode; 
        }
        rear = newNode; 
        if (!front) {
            front = newNode; 
        }
        count++; 
    }

    int dequeue() {
        if (isEmpty()) {
            std::cerr << "Queue is empty. Cannot dequeue." << std::endl;
            return -1; 
        }
        Node* temp = front; 
        int value = front->data; 
        if (!front) {
            rear = nullptr; 
        }
        delete temp; 
        count--;
        return value; 
    }

    int top() {
        if (isEmpty()) {
            std::cerr << "Queue is empty. No top element." << std::endl;
            return -1; 
        }
        return front->data; 
    }

    bool isEmpty() {
        return count == 0; 
    }

    int size() {
        return count; 
    }

    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }
};

int main() {
    Queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    std::cout << "Front element: " << q.top() << std::endl;
    std::cout << "Queue size: " << q.size() << std::endl; 

    std::cout << "Dequeued: " << q.dequeue() << std::endl; 
    std::cout << "Front element: " << q.top() << std::endl; 
    std::cout << "Queue size: " << q.size() << std::endl; 

    q.dequeue();
    q.dequeue();
    std::cout << "Is queue empty? " << (q.isEmpty() ? "Yes" : "No") << std::endl; 
    return 0;
}