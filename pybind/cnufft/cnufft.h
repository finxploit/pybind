/* cnufft.h */

int nufft1d1(int nj, double* xj, double* cj, int iflag, double eps, int ms, double* fk);
int nufft1d2(int nj, double* xj, double* cj, int iflag, double eps, int ms, double* fk);
int nufft1d3(int nj, double* xj, double* cj, int iflag, double eps, int nk, double* sk, double* fk);

int nufft3d1(int nj, double* xj, double* yj, double* zj, double* cj,
             int iflag, double eps, int ms, int mt, int mu, double* fk);

int nufft3d2(int nj, double* xj, double* yj, double* zj, double* cj,
             int iflag, double eps, int ms, int mt, int mu, double* fk);
