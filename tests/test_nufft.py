import pytest
import nufft as f2p_nufft
# import pybind.cnufft._cnufft as cff_nufft
import pybind.cnufft._cnufft as cff_nufft
import numpy as np
from numba import cffi_support
from pybind.cnufft.cnufft import njit_nufft3d1

# Testing Constants
EPS = 1E-12
NJ = 10
MS = 5
MT = 2
MU = 3
NK = 8
IFLAG = 1

def numpy_pointer(array, dtype='double*'):
    assert array.flags['F_CONTIGUOUS']
    return cffi_support.ffi.cast(dtype, array.ctypes.data)


def test_all_equal_nufft1d1():
    xj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)

    fk1 = np.zeros((MS), dtype=np.complex128)

    ier = cff_nufft.lib.nufft1d1(
        NJ,
        numpy_pointer(np.copy(xj)),
        numpy_pointer(np.copy(cj)),
        IFLAG, EPS, MS,
        numpy_pointer(fk1))

    fk2 = f2p_nufft.nufft1d1(xj, cj, MS, df=1.0, eps=EPS, iflag=IFLAG)

    assert np.allclose(fk1, fk2)


def test_all_equal_nufft1d2():
    xj = np.random.random_sample(NJ)
    fk = np.random.random_sample(MS).astype(
        np.complex128)

    cj1 = np.zeros((NJ), dtype=np.complex128)

    ier = cff_nufft.lib.nufft1d2(
        NJ,
        numpy_pointer(np.copy(xj)),
        numpy_pointer(cj1),
        IFLAG, EPS, MS,
        numpy_pointer(np.copy(fk)))

    cj2 = f2p_nufft.nufft1d2(xj, fk, df=1.0, eps=EPS, iflag=IFLAG)

    assert np.allclose(cj1, cj2)


# TODO: Check why developer of that nufft
# package is dividing by 10 at the end
@pytest.mark.skip
def test_all_equal_nufft1d3():
    xj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)
    sk = np.random.random_sample(NK)
    fk1 = np.zeros((NK), dtype=np.complex128)


    ier = cff_nufft.lib.nufft1d3(
        NJ,
        numpy_pointer(np.copy(xj)),
        numpy_pointer(np.copy(cj)),
        IFLAG, EPS, NK,
        numpy_pointer(np.copy(sk)),
        numpy_pointer(fk1))

    fk2 = f2p_nufft.nufft1d3(xj, cj, sk, eps=EPS, iflag=IFLAG)

    assert np.allclose(fk1, fk2)


def test_all_equal_nufft3d1():
    xj = np.random.random_sample(NJ)
    yj = np.random.random_sample(NJ)
    zj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)
    # fk1 = np.asfortranarray(np.zeros((MS,MT,MU), dtype=np.complex128))
    fk1 = np.zeros((MS*MT*MU), dtype=np.complex128)


    ier = cff_nufft.lib.nufft3d1(
        NJ,
        numpy_pointer(np.copy(xj)),
        numpy_pointer(np.copy(yj)),
        numpy_pointer(np.copy(zj)),
        numpy_pointer(np.copy(cj)),
        IFLAG, EPS,
        MS, MT, MU,
        numpy_pointer(fk1))

    # Reshape back the fortran array to original form
    # Not sure why the transpose is needed but looks
    # like it is needed indeed
    fk1 = fk1.reshape((MU, MT, MS)).T

    fk2 = f2p_nufft.nufft3d1(xj, yj, zj, cj, MS, MT, MU, eps=EPS, iflag=IFLAG)

    assert np.allclose(fk1, fk2)


def test_all_equal_numba_nufft3d1():
    xj = np.random.random_sample(NJ)
    yj = np.random.random_sample(NJ)
    zj = np.random.random_sample(NJ)
    cj = np.sin(xj).astype(dtype=np.complex128)

    fk1 = njit_nufft3d1(
        xj, yj, zj, cj,
        MS, MT, MU,
        df=1, eps=EPS, iflag=IFLAG)

    # Reshape and convert from fortran ordered
    fk1 = fk1.view(np.complex128).reshape(
        (MS, MT, MU), order='F')

    fk2 = f2p_nufft.nufft3d1(xj, yj, zj, cj, MS, MT, MU, eps=EPS, iflag=IFLAG)

    assert np.allclose(fk1, fk2)


# TODO fix the different results that we are getting
# compared to f2py implementation
@pytest.mark.skip
def test_all_equal_nufft3d2():
    MS = 2
    MT = 2
    MU = 2
    NJ = 3
    xj = np.random.random_sample(NJ)
    yj = np.random.random_sample(NJ)
    zj = np.random.random_sample(NJ)
    fk = np.random.random_sample((MS,MT,MU)).astype(np.complex128)

    fk1 = np.asfortranarray(fk)

    cj1 = np.zeros((NJ), dtype=np.complex128)

    ier = cff_nufft.lib.nufft3d2(
        NJ,
        numpy_pointer(np.copy(xj)),
        numpy_pointer(np.copy(yj)),
        numpy_pointer(np.copy(zj)),
        numpy_pointer(cj1),
        IFLAG, EPS,
        MU, MT, MS,
        cffi_support.ffi.cast(
            'double *',
            fk1.ctypes.data)
        )

    cj2 = f2p_nufft.nufft3d2(
        xj, yj, zj, fk,
        eps=EPS, iflag=IFLAG)

    import ipdb; ipdb.set_trace()
    assert np.allclose(cj1, cj2)




# @njit
# def nb_nufft3d1():
#     iflag = 1
#     EPS = 1E-12
#     NJ = 10
#     MS = 2
#     MT = 2
#     MU = 2

#     xj = np.ascontiguousarray(np.random.random_sample(NJ))
#     yj = np.ascontiguousarray(np.random.random_sample(NJ))
#     zj = np.ascontiguousarray(np.random.random_sample(NJ))
#     cj = np.ascontiguousarray(np.random.random_sample(NJ))
#     fk = np.ascontiguousarray(np.zeros((MS*MU*MT*2)))

#     ier = ext_nufft3d1(
#         NJ,
#         cffi_support.ffi.from_buffer(xj),
#         cffi_support.ffi.from_buffer(yj),
#         cffi_support.ffi.from_buffer(zj),
#         cffi_support.ffi.from_buffer(cj),
#         iflag,
#         EPS,
#         MS, MT, MU,
#         cffi_support.ffi.from_buffer(fk))

#     return fk
