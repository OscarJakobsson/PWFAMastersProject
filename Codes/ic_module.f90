
MODULE ic_module

  USE shared_data
  USE helper

  IMPLICIT NONE

  PRIVATE

  PUBLIC :: manual_load

CONTAINS

	SUBROUTINE manual_load
	  TYPE(particle), POINTER :: current
	  INTEGER, PARAMETER :: np_local = 1000
	  INTEGER :: ispecies, ip, i, nlines, IOstatus
	  REAL(num) :: temperature, stdev2, tail_width, tail_height, tail_drift
	  REAL(num) :: frac, tail_frac, min_p, max_p, dp_local, p2, tail_p2
	  REAL(num), DIMENSION(np_local) :: p_axis, distfn_axis
	  REAL(num) :: row, x, y, z, energy, weight
	  temperature = 1e15_num
	  tail_width = 0.05_num
	  tail_height = 9_num
	  tail_drift = 0.5_num
	  DO ispecies = 1, 1
	    stdev2 = kb * temperature * species_list(ispecies)%mass
	    frac = 1.0_num / (2.0_num * stdev2)
	    tail_frac = 1.0_num / (2.0_num * stdev2 * tail_width)
	    max_p = 7.0_num * SQRT(stdev2)
	    min_p = 0.5_num * max_p
	    dp_local = (max_p - min_p) / REAL(np_local-1, num)
	    DO ip = 1, np_local
			p_axis(ip) = min_p + (ip - 1) * dp_local
			p2 = p_axis(ip)
			tail_p2 = (p_axis(ip) - tail_drift * max_p)**2
			distfn_axis(ip) = EXP(-p2**2 * frac) * 0.5_num * (sign(1.0_num,4.8e-19_num-p2 )+1.0_num)


	    ENDDO
	    current=>species_list(ispecies)%attached_list%head

	    OPEN(UNIT = 17, FILE = "test_data2.csv")

	    DO WHILE(ASSOCIATED(current))

			READ(17,*, end=10) row, x, y, z, energy, weight

			current%part_p(1) = energy/299792456
			current%part_pos(1) = x-0.25_num
			current%part_pos(2) = y
			current%weight = weight
   			current=>current%next

			!PRINT *, x
			!PRINT *, y
			!PRINT *, z
	    ENDDO
		5	format (f5.2,f5.2,f5.2,f5.2,f5.2,f5.2) 
		10	ClOSE(17)
	   ENDDO


	   DO ispecies = 2, 2

	    current=>species_list(ispecies)%attached_list%head

	    OPEN(UNIT = 18, FILE = "electrondist0250_2.csv")

	    DO WHILE(ASSOCIATED(current))

			READ(18,*, end=11) row, x, y, z, energy, weight

			current%part_p(1) = energy/299792456
			current%part_pos(1) = x-0.25_num
			current%part_pos(2) = y
			current%weight = weight
   			current=>current%next

			!PRINT *, x
			!PRINT *, y
			!PRINT *, z
	    ENDDO
		4	format (f5.2,f5.2,f5.2,f5.2,f5.2,f5.2) 
		11	ClOSE(18)
	   ENDDO

	   DO ispecies = 3, 3

	    current=>species_list(ispecies)%attached_list%head

	    OPEN(UNIT = 19, FILE = "iondist0250_2.csv")

	    DO WHILE(ASSOCIATED(current))

			READ(19,*, end=12) row, x, y, z, weight

			! current%part_p(1) = energy/299792456
			current%part_pos(1) = x-0.25_num
			current%part_pos(2) = y
			current%weight = weight
   			current=>current%next

			!PRINT *, x
			!PRINT *, y
			!PRINT *, z
	    ENDDO
		3	format (f5.2,f5.2,f5.2,f5.2,f5.2,f5.2) 
		12	ClOSE(19)
	   ENDDO

	END SUBROUTINE manual_load


END MODULE ic_module
