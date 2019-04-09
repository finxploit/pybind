import pytest
import numba as nb
import numpy as np
import re
from pybind.cnufft.cnufft import njit_nufft1d1

NJ=2000

@nb.jit(nopython=True, parallel=True, nogil=True)
def parallel_numba_loop(dset1, dset2, times, fn, arg):
    nj = dset1.shape[0]
    result = np.zeros((times * nj, 2*arg))

    for count in nb.prange(times):  # pylint: disable=not-an-iterable
        res = fn(dset1, dset2, arg, eps=1E-12)
        result[nj * count : nj * (count + 1)] = res

    return result

@nb.jit(nopython=True, parallel=True, nogil=True)
def parallel_numba_loop_no_return(dset1, dset2, times, fn, arg):
    nj = dset1.shape[0]

    for count in nb.prange(times):  # pylint: disable=not-an-iterable
        fn(dset1, dset2, arg, eps=1E-12)

@nb.jit(nopython=True)
def no_parallel_numba_loop(dset1, dset2, times, fn, arg):
    nj = dset1.shape[0]
    result = np.zeros((times * nj, 2*arg))

    for count in range(times):
        res = fn(dset1, dset2, arg, eps=1E-12)
        result[nj * count : nj * (count + 1)] = res

    return result

def test_concurrent_return():
    xj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)

    fft = parallel_numba_loop(xj, cj, 100, njit_nufft1d1, 10)
    assert fft.shape == (NJ*100, 2*10)


def test_concurrent_noreturn():
    xj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)

    parallel_numba_loop_no_return(xj, cj, 100, njit_nufft1d1, 10)

def test_noconcurrent_return():
    xj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)

    fft = no_parallel_numba_loop(xj, cj, 100, njit_nufft1d1, 10)

    assert fft.shape == (NJ*100, 2*10)
