#include <string>
#include <iostream>
#include <vector>
// #include <memory>
#include <nanobind/nanobind.h>

#include <nanobind/stl/shared_ptr.h>


int mul(int a, int b){
    return a * b;
}



class GeekyOdyssey{
public:
    static int instances;
    int name;
    std::shared_ptr<std::vector<int>> shared_vint;

    GeekyOdyssey(){
        ++instances;
        name = -2;
        shared_vint = std::make_shared<std::vector<int>>();
        shared_vint->push_back(100);
        shared_vint->push_back(200);
        shared_vint->push_back(300);
    }
    std::string print(){
        return "GeekyOdyssey>print";
    }

    static std::string sprint() { 
        return "GeekyOdyssey>sprint";

    }

    std::vector<int> get_vector(){
        std::vector<int> numbers;
        numbers.push_back(10);
        numbers.push_back(20);
        numbers.push_back(30);
        return numbers;  

    }

    std::shared_ptr<std::vector<int>> get_shared_vint(){
        return shared_vint;
    }


    // void set_shared_vint(std::shared_ptr<std::vector<int>> new_vint){
    //     shared_vint = num;
    // }



    void print_vector(std::vector<int> numbers){
        for (int num : numbers) {
            std::cout << num << " ";
        }
    }

};

int GeekyOdyssey::instances = 0;