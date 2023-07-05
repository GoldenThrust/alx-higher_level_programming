#include <Python.h>
#include <stdio.h>

/**
 * print_symbol_string - prints Python strings.
 * @p: PyObject
 */

void print_python_string(PyObject *p)
{
       	fflush(stdout);
	
	if (PyUnicode_Check(p))
       	{
	       	printf("[.] string object info\n");
		printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ?
			       	"compact ascii" : "compact unicode object");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
    	}
       	else
       	{
	       	printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
       	}
}

