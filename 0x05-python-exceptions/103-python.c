#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - prints information about a python 
 * list object.
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	PyObject *item;
	
	fflush(stdout);
	printf("[*] Python llist info\n");
	if (!PyList_CheckExact(p))
	{
		print("  [ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
		i++;
	}
}

/**
 * print_python_bytes - prints information about
 * a python bytes object.
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	py_ssize_t size = 0, i = 0;
	pyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size >= 10 ? 10 : ((PyVarObject *)p)->ob_size + 1;
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %zd bytes:", size);

	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", bytes->ob_sval[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_float - prints information about Python float object.
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;
	PyFloatObject *flobj = (PyFloatObject *)p;

	fflush(stdout);
	
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(flobj->ob_fval, 'r', 0,Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
