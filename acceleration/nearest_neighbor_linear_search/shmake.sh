#!/bin/bash
make clean
make all TARGETS=sw_emu DEVICES=xilinx:xil-accel-rd-ku115:4ddr-xpr:4.0
./namechange.sh
