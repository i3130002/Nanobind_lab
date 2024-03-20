#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/stl/shared_ptr.h>
#include "code.cpp"

namespace nb = nanobind;

using namespace nb::literals;

NB_MODULE(nanobind_example_ext, m) {
    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);
    m.def("mul", [](int a, int b) { return a * b; }, "a"_a, "b"_a);

    m.def("mul2", &mul, "a1"_a, "b"_a);
    m.def("mul3", &mul, nb::arg("a"), nb::arg("b"));

    nb::class_<GeekyOdyssey>(m, "GeekyOdyssey")
       .def(nb::init<>())
       .def_rw_static("instances", &GeekyOdyssey::instances)
       .def_rw("name", &GeekyOdyssey::name)
       .def("print", &GeekyOdyssey::print)
       .def("get_vector", &GeekyOdyssey::get_vector)
       .def("print_vector", &GeekyOdyssey::print_vector, nb::arg("numbers"))
       .def_static("sprint", &GeekyOdyssey::sprint)

       .def("get_shared_vint", &GeekyOdyssey::get_shared_vint)
    //    .def("set_shared_int", &GeekyOdyssey::set_shared_int, nb::arg("num"))
    //    .def_rw("shared_vint", &GeekyOdyssey::shared_vint)

       ;
}
