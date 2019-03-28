module fmesh_wrapper

use iso_c_binding, only: c_double, c_int
use fmesh, only: mesh_exp

implicit none

contains

subroutine c_mesh_exp(r_min, r_max, a, N, mesh) bind(c)
real(c_double), intent(in) :: r_min
real(c_double), intent(in) :: r_max
real(c_double), intent(in) :: a
integer(c_int), intent(in) :: N
real(c_double), intent(out) :: mesh(N)
call mesh_exp(r_min, r_max, a, N, mesh)
end subroutine

! wrap more functions here
! ...

end module

