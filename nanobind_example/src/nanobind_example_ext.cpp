#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/shared_ptr.h>
#include <nanobind/stl/function.h>

#include "code.cpp"

namespace nb = nanobind;

using namespace nb::literals;

NB_MODULE(nanobind_example_ext, m) {
    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);
    m.def("mul", [](int a, int b) { return a * b; }, "a"_a, "b"_a);

    m.def("mul2", &mul, "a1"_a, "b"_a);
    m.def("mul3", &mul, nb::arg("a"), nb::arg("b"));

    nb::class_<Foo>(m, "Foo")
      .def(nb::init<>())
      .def_rw("name", &Foo::name)
      .def("print", &Foo::print);

    nb::class_<GeekyOdyssey>(m, "GeekyOdyssey")
       .def(nb::init<>())
       .def_rw_static("instances", &GeekyOdyssey::instances)
       .def_rw("name", &GeekyOdyssey::name)
       .def("print", &GeekyOdyssey::print)
       .def("get_vector", &GeekyOdyssey::get_vector)
       .def("print_vector", &GeekyOdyssey::print_vector, nb::arg("numbers"))
       .def_static("sprint", &GeekyOdyssey::sprint)
       .def("get_shared_foo", &GeekyOdyssey::get_shared_foo)
       .def("set_callable", &GeekyOdyssey::set_callable, nb::arg("callable"))
       .def_rw("callable", &GeekyOdyssey::callable)
       .def("call_callable", &GeekyOdyssey::call_callable)
       .def("loop", &GeekyOdyssey::loop, nb::arg("count"))
       ;
}
