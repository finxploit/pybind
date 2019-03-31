/* cnufft.c */

#include "cnufft.h"

int nufft1d1(int nj, double* xj, double* cj, int iflag, double eps, int ms, double* fk) {
  int ier = -1;
  c_nufft1d1f90(nj, xj, cj, iflag, eps, ms, fk, &ier);

  return ier;
}


int nufft1d2(int nj, double* xj, double* cj, int iflag, double eps, int ms, double* fk) {
  int ier = -1;
  c_nufft1d2f90(nj, xj, cj, iflag, eps, ms, fk, &ier);

  return ier;
}


int nufft1d3(int nj, double* xj, double* cj, int iflag, double eps, int nk, double* sk, double* fk) {
  int ier = -1;
  c_nufft1d3f90(nj, xj, cj, iflag, eps, nk, sk, fk, &ier);

  return ier;
}


int nufft3d1(int nj, double* xj, double* yj, double* zj, double* cj,
             int iflag, double eps, int ms, int mt, int mu, double* fk) {

  int ier = -1;
  c_nufft3d1f90(nj, xj, yj, zj, cj, iflag, eps, ms, mt, mu, fk, &ier);

  return ier;
}


int nufft3d2(int nj, double* xj, double* yj, double* zj, double* cj,
             int iflag, double eps, int ms, int mt, int mu, double* fk) {

  int ier = -1;
  c_nufft3d2f90(nj, xj, yj, zj, cj, iflag, eps, ms, mt, mu, fk, &ier);

  return ier;
}
