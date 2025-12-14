#define _GNU_SOURCE
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Helper function for case-insensitive strstr
static char* strcasestr_custom(const char* haystack, const char* needle) {
    if (!*needle) return (char*)haystack;
    for (; *haystack; haystack++) {
        const char* h = haystack;
        const char* n = needle;
        while (*h && *n && tolower((unsigned char)*h) == tolower((unsigned char)*n)) {
            h++;
            n++;
        }
        if (!*n) return (char*)haystack;
    }
    return NULL;
}

static PyObject* search_in_file(PyObject* self, PyObject* args, PyObject* kwargs) {
    const char* filepath;
    const char* keyword;
    int case_sensitive = 1;

    static char* kwlist[] = {"filepath", "keyword", "case_sensitive", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "ss|p", kwlist,
                                     &filepath, &keyword, &case_sensitive))
        return NULL;

    FILE* fp = fopen(filepath, "r");
    if (!fp) Py_RETURN_NONE;

    size_t len = 0;
    char* line = NULL;
    ssize_t read;
    int lineno = 0;

    PyObject* result_list = PyList_New(0);
    PyObject* py_filepath = PyUnicode_FromString(filepath); // pre-create filepath

    while ((read = getline(&line, &len, fp)) != -1) {
        lineno++;
        char* found = NULL;
        if (case_sensitive) {
            found = strstr(line, keyword);
        } else {
            found = strcasestr_custom(line, keyword);
        }

        if (found) {
            PyObject* py_lineno = PyLong_FromLong(lineno);
            PyObject* tuple = PyTuple_New(2);
            Py_INCREF(py_filepath);
            PyTuple_SET_ITEM(tuple, 0, py_filepath);
            PyTuple_SET_ITEM(tuple, 1, py_lineno);
            PyList_Append(result_list, tuple);
            Py_DECREF(tuple);
        }
    }

    Py_DECREF(py_filepath);
    free(line);
    fclose(fp);

    return result_list;
}

// Method definition
static PyMethodDef FastMethods[] = {
    {"search_in_file", (PyCFunction)search_in_file, METH_VARARGS | METH_KEYWORDS, "Fast keyword search"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef fastmodule = {
    PyModuleDef_HEAD_INIT,
    "_fastsearch",
    NULL,
    -1,
    FastMethods
};

// Module initialization
PyMODINIT_FUNC PyInit__fastsearch(void) {
    return PyModule_Create(&fastmodule);
}
