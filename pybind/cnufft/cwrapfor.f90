! cwrapfor.f90

module cwrap_nufft
use iso_c_binding, only: c_int, c_double, c_double_complex

contains

subroutine c_nufft1d1f90(nj,xj,cj,iflag,eps,ms,fk,ier) bind(c)
  implicit none
  integer(c_int), intent(in), value :: nj, ms, iflag
  real(c_double), intent(in), value :: eps
  real(c_double), intent(in) :: xj(1:nj)
  complex(c_double_complex), intent(in) :: cj(1:nj)
  complex(c_double_complex), intent(out) :: fk(1:ms)
  integer(c_int), intent(out) :: ier

  call nufft1d1f90(nj,xj,cj,iflag,eps,ms,fk,ier)

end subroutine c_nufft1d1f90

subroutine c_nufft1d2f90(nj,xj,cj,iflag,eps,ms,fk,ier) bind(c)
  implicit none
  integer(c_int), intent(in), value :: nj, ms, iflag
  real(c_double), intent(in), value :: eps
  real(c_double), intent(in) :: xj(1:nj)
  complex(c_double_complex), intent(out) :: cj(1:nj)
  complex(c_double_complex), intent(in) :: fk(1:ms)
  integer(c_int), intent(out) :: ier

  call nufft1d2f90(nj,xj,cj,iflag,eps,ms,fk,ier)

end subroutine c_nufft1d2f90

subroutine c_nufft1d3f90(nj,xj,cj,iflag,eps,nk,sk,fk,ier) bind(c)
    implicit none
    integer(c_int), intent(in), value :: nj, nk, iflag
    real(c_double), intent(in), value :: eps
    real(c_double), intent(in) :: xj(1:nj)
    real(c_double), intent(in) :: sk(1:nk)
    complex(c_double_complex), intent(in) :: cj(1:nj)
    complex(c_double_complex), intent(out) :: fk(1:nk)
    integer(c_int), intent(out) :: ier

    call nufft1d3f90(nj,xj,cj,iflag,eps,nk,sk,fk,ier)

end subroutine c_nufft1d3f90

subroutine c_nufft3d1f90(nj,xj,yj,zj,cj,iflag,eps,ms,mt,mu,fk,ier) bind(c)
  implicit none
  integer(c_int), intent(in), value :: nj, ms, mt, mu, iflag
  real(c_double), intent(in), value :: eps
  real(c_double), intent(in) :: xj(1:nj), yj(1:nj), zj(1:nj)
  complex(c_double_complex), intent(in) :: cj(1:nj)
  complex(c_double_complex), intent(out) :: fk(1:ms,1:mt,1:mu)
  integer(c_int), intent(out) :: ier

  call nufft3d1f90(nj,xj,yj,zj,cj,iflag,eps,ms,mt,mu,fk,ier)

end subroutine c_nufft3d1f90

subroutine c_nufft3d2f90(nj,xj,yj,zj,cj,iflag,eps,ms,mt,mu,fk,ier) bind(c)
  implicit none
  integer(c_int), intent(in), value :: nj, ms, mt, mu, iflag
  real(c_double), intent(in), value :: eps
  real(c_double), intent(in) :: xj(1:nj), yj(1:nj), zj(1:nj)
  complex(c_double_complex), intent(in) :: fk(1:ms,1:mt,1:mu)
  complex(c_double_complex), intent(out) :: cj(1:nj)
  integer(c_int), intent(out) :: ier

  call nufft3d2f90(nj,xj,yj,zj,cj,iflag,eps,ms,mt,mu,fk,ier)

end subroutine c_nufft3d2f90

end module cwrap_nufft
