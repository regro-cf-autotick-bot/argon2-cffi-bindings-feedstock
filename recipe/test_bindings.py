from _argon2_cffi_bindings import ffi, lib


assert repr(ffi).startswith("<_cffi_backend.FFI object at")
assert repr(lib).startswith("<Lib object for")
assert lib.ARGON2_VERSION_NUMBER == 19
assert lib.argon2_encodedlen(1, 2, 3, 4, 5, lib.Argon2_id) == 42
