#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_p, allocated, idx = 0;
	PyObject *element;

	size_p = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_p);
	printf("[*] Allocated = %ld\n", allocated);
	while (idx < size_p)
	{
		element = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, element->ob_type->tp_name);
		idx++;
	}
}
