#include <string>
#include <iostream>
#include <vector>
#include <memory>
#include <functional>
#include <sstream>


int mul(int a, int b){
    return a * b;
}

class Foo{
    public:
    std::string name;

    void print(){
        std::cout<<name<<std::endl;
    }
};


class GeekyOdyssey{
public:
    static int instances;
    int name;
    std::shared_ptr<Foo> foo;
    std::function<void(std::string)> callable;

    void set_callable(std::function<void(std::string)> _callable){
        callable = _callable;
    }

    void call_callable(std::string message){
        callable(message);
    }


    GeekyOdyssey(){
        ++instances;
        name = -2;
        foo = std::make_shared<Foo>();
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

    std::shared_ptr<Foo> get_shared_foo(){
        return foo;
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