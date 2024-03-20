import nanobind_example
from icecream import ic
import time
# ic(nanobind_example.add(1, 2))
# ic(nanobind_example.mul(1, 2))
# ic(nanobind_example.mul2(1, 2))
# ic(nanobind_example.mul3(1, 2))

geekyOdyssey = nanobind_example.GeekyOdyssey()
# ic(geekyOdyssey.print())
# ic(geekyOdyssey.name)
# geekyOdyssey.name = 4
# ic(geekyOdyssey.name)


# ic(nanobind_example.GeekyOdyssey.instances)
# nanobind_example.GeekyOdyssey()
# ic(nanobind_example.GeekyOdyssey.instances)

# ic(nanobind_example.GeekyOdyssey.sprint())

# ic(geekyOdyssey.get_vector())
# ic(geekyOdyssey.print_vector([1,2,3,4]))


# shared_int = geekyOdyssey.get_shared_int()
# ic(shared_int)

# geekyOdyssey.set_shared_int(10)
# ic(shared_int)


shared_foo_test = nanobind_example.GeekyOdyssey()
foo1 = shared_foo_test.get_shared_foo()
foo1.name = "foo1"
print("foo1.print():", end=" ", flush=True)
foo1.print()

foo2 = shared_foo_test.get_shared_foo()
print("foo2.print():", end=" ", flush=True)
foo2.print()

assert foo2.name == "foo1"