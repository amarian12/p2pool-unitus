from distutils.core import setup, Extension

yescrypt_hash_module = Extension('yescrypt_hash', sources = ['yescryptmodule.c'], extra_compile_args=['-march=native'])

setup (name = 'yescrypt_hash',
       version = '1.0',
       ext_modules = [yescrypt_hash_module])
