from distutils.core import setup, Extension

argon2d_hash_module = Extension('argon2d_hash', sources = ['argon2dmodule.c', 'argon2.c', 'blake2b.c', 'core.c', 'encoding.c', 'opt.c', 'thread.c'], extra_compile_args=['-march=native'])

setup (name = 'argon2d_hash',
       version = '1.0',
       ext_modules = [argon2d_hash_module])
