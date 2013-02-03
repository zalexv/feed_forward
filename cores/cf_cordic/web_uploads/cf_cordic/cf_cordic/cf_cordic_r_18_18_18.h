//
//  Copyright (c) 2003 Launchbird Design Systems, Inc.
//  All rights reserved.
//  
//  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
//    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
//    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
//  
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
//  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
//  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
//  OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
//  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
//  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//  
//  
//  Overview:
//  
//    Cordics (COordinate Rotation DIgital Computers) are used to calculate
//    trigonometric functions and complex plane phase rotations.
//    This rotation mode cordic rotates a complex vector by the initial angle.
//    If the rotation will transition through +-PI/2 then the "flip_i" control
//    input must be set.
//  
//  Interface:
//  
//    Synchronization:
//      clock_c  : Clock input.
//      enable_i : Synchronous enable.
//      reset_i  : Synchronous reset.
//  
//    Inputs:
//      flip_i   : Set to perform initial rotation if rotation will transition through +-PI/2
//      real_i   : Initial real component (signed).
//      imag_i   : Initial imaginary component (signed).
//      angle_i  : Initial angle (modulo 2PI).
//  
//    Outputs:
//      real_o   : Resulting real component (signed).
//      imag_o   : Resulting imaginary component (signed).
//      angle_o  : Resulting angle (modulo 2PI).
//  
//  Built In Parameters:
//  
//    Cordic Mode    = Rotation
//    Vector Width   = 18
//    Angle Width    = 18
//    Cordic Stages  = 18
//  
//  Resulting Pipeline Latency is 20 clock cycles.
//  
//  
//  
//  Generated by Confluence 0.6.3  --  Launchbird Design Systems, Inc.  --  www.launchbird.com
//  
//  Build Date : Fri Aug 22 09:44:26 CDT 2003
//  
//  Interface
//  
//    Build Name    : cf_cordic_r_18_18_18
//    Clock Domains : clock_c  
//    Vector Input  : enable_i(1)
//    Vector Input  : reset_i(1)
//    Vector Input  : flip_i(1)
//    Vector Input  : real_i(18)
//    Vector Input  : imag_i(18)
//    Vector Input  : ang_i(18)
//    Vector Output : real_o(18)
//    Vector Output : imag_o(18)
//    Vector Output : ang_o(18)
//  
//  
//  

#ifdef __cplusplus
extern "C" {
#endif

void cf_cordic_r_18_18_18_ports(unsigned char* port_enable_i, unsigned char* port_reset_i, unsigned char* port_flip_i, unsigned char* port_real_i, unsigned char* port_imag_i, unsigned char* port_ang_i, unsigned char* port_real_o, unsigned char* port_imag_o, unsigned char* port_ang_o);
void cf_cordic_r_18_18_18_init();
void cf_cordic_r_18_18_18_calc();
void cf_cordic_r_18_18_18_cycle_clock();
void cf_cordic_r_18_18_18_sim_init(const char* file);
void cf_cordic_r_18_18_18_sim_end();
void cf_cordic_r_18_18_18_sim_sample();

#ifdef __cplusplus
}
#endif

