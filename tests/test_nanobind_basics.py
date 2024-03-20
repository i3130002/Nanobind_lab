import nanobind_example
from icecream import ic
import time

def test_shared_ptr_foo():
    shared_foo_test = nanobind_example.GeekyOdyssey()
    foo1 = shared_foo_test.get_shared_foo()
    foo1.name = "foo1"
    print("foo1.print():", end=" ", flush=True)
    foo1.print()

    foo2 = shared_foo_test.get_shared_foo()
    print("foo2.print():", end=" ", flush=True)
    foo2.print()

    assert foo2.name == "foo1"

def test_add():
    ic(nanobind_example.add(1, 2))
    assert nanobind_example.add(1, 2) == 3

def test_mul():
    ic(nanobind_example.mul(1, 2))
    assert nanobind_example.mul(1, 2) == 2

def test_mul2():
    ic(nanobind_example.mul2(1, 2))
    assert nanobind_example.mul2(1, 2) == 2
   

def test_mul3():
    ic(nanobind_example.mul3(1, 2))
    assert nanobind_example.mul3(1, 2) == 2
   
def test_variable():
    geekyOdyssey = nanobind_example.GeekyOdyssey()
    ic(geekyOdyssey.print())
    ic(geekyOdyssey.name)
    geekyOdyssey.name = 4
    ic(geekyOdyssey.name)
    assert geekyOdyssey.name == 4

def test_static():
    _start = nanobind_example.GeekyOdyssey.instances
    assert nanobind_example.GeekyOdyssey.instances == 0 + _start
    nanobind_example.GeekyOdyssey()
    assert nanobind_example.GeekyOdyssey.instances == 1 + _start
    nanobind_example.GeekyOdyssey()
    assert nanobind_example.GeekyOdyssey.instances == 2 + _start

def test_return_string():
    ic(nanobind_example.GeekyOdyssey.sprint())
    assert nanobind_example.GeekyOdyssey.sprint() == "GeekyOdyssey>sprint"

def test_get_vector():
    geekyOdyssey = nanobind_example.GeekyOdyssey()
    vec = geekyOdyssey.get_vector()
    assert vec[0] == 10
    assert vec[1] == 20
    assert vec[2] == 30

def test_print_vector():
    geekyOdyssey = nanobind_example.GeekyOdyssey()
    geekyOdyssey.print_vector([1,2,3,4,5,6])
    assert True


def test_callable_via_set_function():
    global last_called_message
    last_called_message = ""
    geekyOdyssey = nanobind_example.GeekyOdyssey()
    def func(msg):
        global last_called_message
        last_called_message = msg
    geekyOdyssey.set_callable(func)
    geekyOdyssey.call_callable("hello")
    assert last_called_message == "hello"



def test_callable_via_direct_assignment():
    global last_called_message
    last_called_message = ""
    geekyOdyssey = nanobind_example.GeekyOdyssey()
    def func(msg):
        global last_called_message
        last_called_message = msg
    geekyOdyssey.callable = func
    geekyOdyssey.call_callable("hello")
    assert last_called_message == "hello"