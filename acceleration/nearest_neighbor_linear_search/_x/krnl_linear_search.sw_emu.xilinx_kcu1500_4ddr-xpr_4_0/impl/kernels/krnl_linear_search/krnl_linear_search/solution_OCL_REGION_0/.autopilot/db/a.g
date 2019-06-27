#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /mnt/project/tl6/example_repo/SDAccel_Examples/acceleration/nearest_neighbor_linear_search/_x/krnl_linear_search.sw_emu.xilinx_kcu1500_4ddr-xpr_4_0/impl/kernels/krnl_linear_search/krnl_linear_search/solution_OCL_REGION_0/.autopilot/db/a.g.bc ${1+"$@"}
