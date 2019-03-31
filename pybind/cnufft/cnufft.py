import numpy as np
from numba import jit, cffi_support
from . import _cnufft

cffi_support.register_module(_cnufft)


nufft3d1 = _cnufft.lib.nufft3d1
@jit(nopython=True)
def njit_nufft3d1(x, y, z, c, ms, mt, mu, df=1, eps=1e-15, iflag=1, direct=False):
    nj = x.shape[0]
    x = np.ascontiguousarray(x)
    y = np.ascontiguousarray(y)
    z = np.ascontiguousarray(z)
    c = np.ascontiguousarray(c)
    fk = np.ascontiguousarray(np.zeros((ms*mt*mu*2)))

    return_code = nufft3d1(
        np.int32(nj),
        cffi_support.ffi.from_buffer(x.view(np.float64)),
        cffi_support.ffi.from_buffer(y.view(np.float64)),
        cffi_support.ffi.from_buffer(z.view(np.float64)),
        cffi_support.ffi.from_buffer(c.view(np.float64)),
        iflag, eps,
        np.int32(ms), np.int32(mt), np.int32(mu),
        cffi_support.ffi.from_buffer(fk.view(np.float64)))

    return fk
