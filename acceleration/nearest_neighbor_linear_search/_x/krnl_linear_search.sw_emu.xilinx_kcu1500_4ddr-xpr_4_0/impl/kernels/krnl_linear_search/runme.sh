#!/bin/sh

# 
# xocc(TM)
# runme.sh: a xocc-generated Runs Script for UNIX
# Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
# 

if [ -z "$PATH" ]; then
  PATH=/opt/Xilinx/SDK/2018.2/bin:/opt/Xilinx/SDx/2018.2/bin:/opt/Xilinx/Vivado/2018.2/bin
else
  PATH=/opt/Xilinx/SDK/2018.2/bin:/opt/Xilinx/SDx/2018.2/bin:/opt/Xilinx/Vivado/2018.2/bin:$PATH
fi
export PATH

if [ -z "$LD_LIBRARY_PATH" ]; then
  LD_LIBRARY_PATH=
else
  LD_LIBRARY_PATH=:$LD_LIBRARY_PATH
fi
export LD_LIBRARY_PATH

HD_PWD='/mnt/project/tl6/example_repo/SDAccel_Examples/acceleration/nearest_neighbor_linear_search/_x/krnl_linear_search.sw_emu.xilinx_kcu1500_4ddr-xpr_4_0/impl/kernels/krnl_linear_search'
cd "$HD_PWD"

HD_LOG=runme.log
/bin/touch $HD_LOG

ISEStep="./ISEWrap.sh"
EAStep()
{
     $ISEStep $HD_LOG "$@" >> $HD_LOG 2>&1
     if [ $? -ne 0 ]
     then
         exit
     fi
}

EAStep vivado_hls -f krnl_linear_search.tcl -messageDb vivado_hls.pb
