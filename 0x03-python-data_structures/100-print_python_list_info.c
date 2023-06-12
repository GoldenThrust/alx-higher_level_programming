#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p), i;
	PyObject *item;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

