#include <Python.h>

#include "argon2.h"

static void Argon2dHash(const char *input, int length, char *output)
{
    // uint32_t t_cost = 1; // 1 iteration
    // uint32_t m_cost = 4096; // use 4MB
    // uint32_t parallelism = 1; // 1 thread, 2 lanes
    
    //yescrypt_bsty((const uint8_t*)input, length, (const uint8_t*)input, length, 2048, 8, 1, (uint8_t*)output, 32);
    argon2d_hash_raw(1, 4096, 1, (const uint8_t*)input, length, (const uint8_t*)input, length, (uint8_t*)output, 32);
    
}

static PyObject *argon2d_gethash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    int length;
    if (!PyArg_ParseTuple(args, "Si", &input, &length))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    Argon2dHash((char *)PyBytes_AsString((PyObject*) input), 80, output);
#else
    Argon2dHash((char *)PyString_AsString((PyObject*) input), 80, output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef Argon2dMethods[] = {
    { "getHash", argon2d_gethash, METH_VARARGS, "Returns the Argon2d hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef Argon2dModule = {
    PyModuleDef_HEAD_INIT,
    "argon2d_hash",
    "...",
    -1,
    Argon2dMethods
};

PyMODINIT_FUNC PyInit_argon2d_hash(void) {
    return PyModule_Create(&Argon2dModule);
}

#else

PyMODINIT_FUNC initargon2d_hash(void) {
    (void) Py_InitModule("argon2d_hash", Argon2dMethods);
}
#endif
