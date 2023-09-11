#include "object.h"
#include "listobject.h"
void print_python_list_info(PyObject *p)
{
    int index;
    int l;

    l = PyList_Size(p)
    for (i = 0 ; i < l ; i++)
    {
            printf("[*] Size of the Python List = %d", l);
    }
}
