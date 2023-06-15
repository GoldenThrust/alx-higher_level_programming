#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints some basic information
 * about a Python bytes object
 * @p: pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	long int i, py_size;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	py_size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", py_size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", (py_size < 10 ? py_size + 1 : 10));

	for (i = 0; i < py_size && i < 10; i++)
		printf(" %02x", (unsigned char)str[i]);

	printf("\n");
}


/**
 * print_python_list - prints some basic information about a Python list
 * @p: pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	long int i, py_size;
	PyObject *item;

	py_size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", py_size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < py_size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

