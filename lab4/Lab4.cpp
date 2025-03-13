#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     
    int num;        
    int capacity;   

public:
    Stack(int initialCapacity) {  
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }
    
    void push(int x) {
        if (num + 1 >= capacity) {
            increaseCapacity();
        }
        
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        
        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack underflow." << endl;
            return -1; 
        }
        
        int topValue = head->data;
        
        Node* temp = head;
        head = head->next;
        delete temp;
        
        num--;
        
        return topValue;
    }
    
    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return -1; 
        }
        
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity = capacity * 2;
        cout << "Capacity increased to " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            return false;
        }
        
        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            num--;
            return true;
        }

        Node* current = head;
        Node* prev = nullptr;
        
        while (current != nullptr) {
            if (current->data == val) {
                prev->next = current->next;
                delete current;
                num--;
                return true;
            }
            prev = current;
            current = current->next;
        }
        
        return false;
    }
};

int main() {
    Stack myStack(3);
    
    cout << "Pushing elements: 10, 20, 30" << endl;
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    
    cout << "Top element: " << myStack.peek() << endl;
    
    cout << "Pushing element: 40" << endl;
    myStack.push(40);
    
    cout << "Popping elements:" << endl;
    cout << myStack.pop() << endl;
    cout << myStack.pop() << endl;
    
    cout << "Deleting element 10:" << endl;
    bool deleted = myStack.deleteElement(10);
    cout << "Deletion " << (deleted ? "successful" : "failed") << endl;
    
    cout << "Remaining elements:" << endl;
    while (!myStack.isEmpty()) {
        cout << myStack.pop() << endl;
    }
    
    return 0;
}