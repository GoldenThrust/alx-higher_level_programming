#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints some basic information about a Python list
 * @p: pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, py_size;
	PyObject *item;

	py_size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", py_size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < py_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints some basic information about a Python bytes object
 * @p: pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, py_size;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	py_size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %zd\n", py_size);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", (py_size < 10 ? py_size + 1 : 10));

	for (i = 0; i < py_size && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);
	
	putchar('\n');
}
