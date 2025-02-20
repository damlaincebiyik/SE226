#include <iostream>
#include <string>

using namespace std;

void main() {
    string name;
    cout << "What is your name?" << endl;
    getline(cin, name);
    cout << "Hello " << name << endl;
    string student_id;
    cout << "What is your Student ID?" << endl;
    getline(cin, student_id);
    cout << "Your ID is " << student_id << endl;



    float var1, var2;
    cout << "Enter var1: ";
    cin >> var1;
    cout << "Enter var2: ";
    cin >> var2;
    float var_sum = var1 + var2;
    float var_diff = var1 - var2;
    float var_prod = var1 * var2;
    cout << "var1 = " << var1 << endl;
    cout << "var2 = " << var2 << endl;
    cout << "var_sum = " << var_sum << endl;
    cout << "var_diff = " << var_diff << endl;
    cout << "var_prod = " << var_prod << endl;


    cout << "What is your name?" << endl;
    getline(cin, name);
    getline(cin, name);
    float lab_grade, midterm_grade, final_grade;
    cout << "What is your lab grade?" << endl;
    cin >> lab_grade;
    cout << "What is your midterm grade?" << endl;
    cin >> midterm_grade;
    cout << "What is your final grade?" << endl;
    cin >> final_grade;
    float last_score = lab_grade * 0.25 + midterm_grade * 0.35 + final_grade * 0.40;



    cout << "Name: " << name << endl;
    cout << "Lab Grade: " << lab_grade << endl;
    cout << "Midterm Grade: " << midterm_grade << endl;
    cout << "Final Grade: " << final_grade << endl;
    cout << "Last Score: " << last_score << endl;



    cout << "*\n**\n***\n**\n*\n";

}