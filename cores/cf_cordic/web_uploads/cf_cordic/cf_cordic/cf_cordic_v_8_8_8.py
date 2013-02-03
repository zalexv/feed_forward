#
#  Copyright (c) 2003 Launchbird Design Systems, Inc.
#  All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
#  INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
#  OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
#  
#  Overview:
#  
#    Cordics (COordinate Rotation DIgital Computers) are used to calculate
#    trigonometric functions and complex plane phase rotations.
#    This vector mode cordic rotates any complex vector to the positive real axis.
#    The resulting angle is the initial angle plus the angle of rotation.
#  
#  Interface:
#  
#    Synchronization:
#      clock_c  : Clock input.
#      enable_i : Synchronous enable.
#      reset_i  : Synchronous reset.
#  
#    Inputs:
#      real_i   : Initial real component (signed).
#      imag_i   : Initial imaginary component (signed).
#      angle_i  : Initial angle (modulo 2PI).
#  
#    Outputs:
#      real_o   : Resulting real component (signed).
#      imag_o   : Resulting imaginary component (signed).
#      angle_o  : Resulting angle (modulo 2PI).
#  
#  Built In Parameters:
#  
#    Cordic Mode    = Vector
#    Vector Width   = 8
#    Angle Width    = 8
#    Cordic Stages  = 8
#  
#  Resulting Pipeline Latency is 10 clock cycles.
#  
#  
#  
#  Generated by Confluence 0.6.3  --  Launchbird Design Systems, Inc.  --  www.launchbird.com
#  
#  Build Date : Fri Aug 22 09:44:19 CDT 2003
#  
#  Interface
#  
#    Build Name    : cf_cordic_v_8_8_8
#    Clock Domains : clock_c  
#    Vector Input  : enable_i(1)
#    Vector Input  : reset_i(1)
#    Vector Input  : real_i(8)
#    Vector Input  : imag_i(8)
#    Vector Input  : ang_i(8)
#    Vector Output : real_o(8)
#    Vector Output : imag_o(8)
#    Vector Output : ang_o(8)
#  
#  
#  

import sys
import time

class cf_cordic_v_8_8_8:

  def init(self):
    self.n632 = 0L
    self.n630 = 0L
    self.n628 = 0L
    self.n626 = 0L
    self.n624 = 0L
    self.n622 = 0L
    self.n620 = 0L
    self.n618 = 0L
    self.n616 = 0L
    self.n579 = 0L
    self.n574 = 0L
    self.n573 = 0L
    self.n572 = 0L
    self.n561 = 0L
    self.n549 = 0L
    self.n540 = 0L
    self.n527 = 0L
    self.n518 = 0L
    self.n514 = 0L
    self.n506 = 0L
    self.n504 = 0L
    self.n492 = 0L
    self.n480 = 0L
    self.n472 = 0L
    self.n459 = 0L
    self.n451 = 0L
    self.n447 = 0L
    self.n439 = 0L
    self.n437 = 0L
    self.n425 = 0L
    self.n413 = 0L
    self.n406 = 0L
    self.n393 = 0L
    self.n386 = 0L
    self.n382 = 0L
    self.n374 = 0L
    self.n372 = 0L
    self.n360 = 0L
    self.n348 = 0L
    self.n342 = 0L
    self.n329 = 0L
    self.n323 = 0L
    self.n319 = 0L
    self.n311 = 0L
    self.n309 = 0L
    self.n297 = 0L
    self.n285 = 0L
    self.n280 = 0L
    self.n267 = 0L
    self.n262 = 0L
    self.n258 = 0L
    self.n250 = 0L
    self.n248 = 0L
    self.n236 = 0L
    self.n224 = 0L
    self.n220 = 0L
    self.n207 = 0L
    self.n203 = 0L
    self.n199 = 0L
    self.n191 = 0L
    self.n189 = 0L
    self.n177 = 0L
    self.n165 = 0L
    self.n162 = 0L
    self.n149 = 0L
    self.n146 = 0L
    self.n142 = 0L
    self.n134 = 0L
    self.n132 = 0L
    self.n120 = 0L
    self.n108 = 0L
    self.n93 = 0L
    self.n87 = 0L
    self.n79 = 0L
    self.n77 = 0L
    self.n46 = 0L
    self.n44 = 0L
    self.n38 = 0L
    self.n32 = 0L
    self.n30 = 0L
    self.n7 = 0L
    self.n6 = 0L
    self.n5 = 0L
    self.n4 = 0L
    self.n3 = 0L
    self.n563 = 0L
    self.n562 = 0L
    self.n543 = 0L
    self.n521 = 0L
    self.n505 = 0L
    self.n494 = 0L
    self.n493 = 0L
    self.n475 = 0L
    self.n454 = 0L
    self.n438 = 0L
    self.n427 = 0L
    self.n426 = 0L
    self.n409 = 0L
    self.n389 = 0L
    self.n373 = 0L
    self.n362 = 0L
    self.n361 = 0L
    self.n345 = 0L
    self.n326 = 0L
    self.n310 = 0L
    self.n299 = 0L
    self.n298 = 0L
    self.n283 = 0L
    self.n265 = 0L
    self.n249 = 0L
    self.n238 = 0L
    self.n237 = 0L
    self.n223 = 0L
    self.n206 = 0L
    self.n190 = 0L
    self.n179 = 0L
    self.n178 = 0L
    self.n166 = 0L
    self.n150 = 0L
    self.n133 = 0L
    self.n122 = 0L
    self.n121 = 0L
    self.n111 = 0L
    self.n110 = 0L
    self.n96 = 0L
    self.n95 = 0L
    self.n78 = 0L
    self.n51 = 0L
    self.n47 = 0L
    self.n45 = 0L
    self.n31 = 0L
    self.n28 = 0L
    self.n28r = 0L
    self.n28e = 0L
    self.n28d = 0L
    self.n21 = 0L
    self.n21r = 0L
    self.n21e = 0L
    self.n21d = 0L
    self.n14 = 0L
    self.n14r = 0L
    self.n14e = 0L
    self.n14d = 0L
    self.n544 = 0L
    self.n522 = 0L
    self.n507 = 0L
    self.n476 = 0L
    self.n455 = 0L
    self.n440 = 0L
    self.n410 = 0L
    self.n390 = 0L
    self.n375 = 0L
    self.n346 = 0L
    self.n327 = 0L
    self.n312 = 0L
    self.n284 = 0L
    self.n266 = 0L
    self.n251 = 0L
    self.n225 = 0L
    self.n208 = 0L
    self.n192 = 0L
    self.n168 = 0L
    self.n167 = 0L
    self.n152 = 0L
    self.n151 = 0L
    self.n135 = 0L
    self.n80 = 0L
    self.n33 = 0L
    self.n545 = 0L
    self.n523 = 0L
    self.n515 = 0L
    self.n477 = 0L
    self.n456 = 0L
    self.n448 = 0L
    self.n411 = 0L
    self.n391 = 0L
    self.n383 = 0L
    self.n347 = 0L
    self.n328 = 0L
    self.n320 = 0L
    self.n286 = 0L
    self.n268 = 0L
    self.n259 = 0L
    self.n227 = 0L
    self.n226 = 0L
    self.n210 = 0L
    self.n209 = 0L
    self.n200 = 0L
    self.n143 = 0L
    self.n88 = 0L
    self.n39 = 0L
    self.n546 = 0L
    self.n524 = 0L
    self.n516 = 0L
    self.n478 = 0L
    self.n457 = 0L
    self.n449 = 0L
    self.n412 = 0L
    self.n392 = 0L
    self.n384 = 0L
    self.n349 = 0L
    self.n330 = 0L
    self.n321 = 0L
    self.n288 = 0L
    self.n287 = 0L
    self.n270 = 0L
    self.n269 = 0L
    self.n260 = 0L
    self.n201 = 0L
    self.n144 = 0L
    self.n89 = 0L
    self.n42 = 0L
    self.n547 = 0L
    self.n525 = 0L
    self.n517 = 0L
    self.n479 = 0L
    self.n458 = 0L
    self.n450 = 0L
    self.n414 = 0L
    self.n394 = 0L
    self.n385 = 0L
    self.n351 = 0L
    self.n350 = 0L
    self.n332 = 0L
    self.n331 = 0L
    self.n322 = 0L
    self.n261 = 0L
    self.n202 = 0L
    self.n145 = 0L
    self.n90 = 0L
    self.n43 = 0L
    self.n564 = 0L
    self.n548 = 0L
    self.n539 = 0L
    self.n526 = 0L
    self.n495 = 0L
    self.n481 = 0L
    self.n471 = 0L
    self.n460 = 0L
    self.n428 = 0L
    self.n416 = 0L
    self.n415 = 0L
    self.n405 = 0L
    self.n396 = 0L
    self.n395 = 0L
    self.n363 = 0L
    self.n341 = 0L
    self.n333 = 0L
    self.n300 = 0L
    self.n279 = 0L
    self.n271 = 0L
    self.n239 = 0L
    self.n219 = 0L
    self.n211 = 0L
    self.n180 = 0L
    self.n161 = 0L
    self.n153 = 0L
    self.n123 = 0L
    self.n105 = 0L
    self.n97 = 0L
    self.n68 = 0L
    self.n60 = 0L
    self.n52 = 0L
    self.n571 = 0L
    self.n571r = 0L
    self.n571e = 0L
    self.n571d = 0L
    self.n550 = 0L
    self.n528 = 0L
    self.n502 = 0L
    self.n502r = 0L
    self.n502e = 0L
    self.n502d = 0L
    self.n483 = 0L
    self.n482 = 0L
    self.n462 = 0L
    self.n461 = 0L
    self.n435 = 0L
    self.n435r = 0L
    self.n435e = 0L
    self.n435d = 0L
    self.n417 = 0L
    self.n397 = 0L
    self.n370 = 0L
    self.n370r = 0L
    self.n370e = 0L
    self.n370d = 0L
    self.n352 = 0L
    self.n340 = 0L
    self.n340r = 0L
    self.n340e = 0L
    self.n340d = 0L
    self.n307 = 0L
    self.n307r = 0L
    self.n307e = 0L
    self.n307d = 0L
    self.n289 = 0L
    self.n278 = 0L
    self.n278r = 0L
    self.n278e = 0L
    self.n278d = 0L
    self.n246 = 0L
    self.n246r = 0L
    self.n246e = 0L
    self.n246d = 0L
    self.n228 = 0L
    self.n218 = 0L
    self.n218r = 0L
    self.n218e = 0L
    self.n218d = 0L
    self.n187 = 0L
    self.n187r = 0L
    self.n187e = 0L
    self.n187d = 0L
    self.n169 = 0L
    self.n160 = 0L
    self.n160r = 0L
    self.n160e = 0L
    self.n160d = 0L
    self.n130 = 0L
    self.n130r = 0L
    self.n130e = 0L
    self.n130d = 0L
    self.n112 = 0L
    self.n104 = 0L
    self.n104r = 0L
    self.n104e = 0L
    self.n104d = 0L
    self.n75 = 0L
    self.n75r = 0L
    self.n75e = 0L
    self.n75d = 0L
    self.n67 = 0L
    self.n67r = 0L
    self.n67e = 0L
    self.n67d = 0L
    self.n59 = 0L
    self.n59r = 0L
    self.n59e = 0L
    self.n59d = 0L
    self.n552 = 0L
    self.n551 = 0L
    self.n530 = 0L
    self.n529 = 0L
    self.n484 = 0L
    self.n463 = 0L
    self.n424 = 0L
    self.n424r = 0L
    self.n424e = 0L
    self.n424d = 0L
    self.n404 = 0L
    self.n404r = 0L
    self.n404e = 0L
    self.n404d = 0L
    self.n359 = 0L
    self.n359r = 0L
    self.n359e = 0L
    self.n359d = 0L
    self.n296 = 0L
    self.n296r = 0L
    self.n296e = 0L
    self.n296d = 0L
    self.n235 = 0L
    self.n235r = 0L
    self.n235e = 0L
    self.n235d = 0L
    self.n176 = 0L
    self.n176r = 0L
    self.n176e = 0L
    self.n176d = 0L
    self.n119 = 0L
    self.n119r = 0L
    self.n119e = 0L
    self.n119d = 0L
    self.n553 = 0L
    self.n531 = 0L
    self.n491 = 0L
    self.n491r = 0L
    self.n491e = 0L
    self.n491d = 0L
    self.n470 = 0L
    self.n470r = 0L
    self.n470e = 0L
    self.n470d = 0L
    self.n560 = 0L
    self.n560r = 0L
    self.n560e = 0L
    self.n560d = 0L
    self.n538 = 0L
    self.n538r = 0L
    self.n538e = 0L
    self.n538d = 0L
    self.calc(0L, 0L, 0L, 0L, 0L, )

  def calc(self, enable_i, reset_i, real_i, imag_i, ang_i, ):
    self.n632 = 0x080L
    self.n630 = 0x080L
    self.n628 = 0x080L
    self.n626 = 0x080L
    self.n624 = 0x080L
    self.n622 = 0x080L
    self.n620 = 0x080L
    self.n618 = 0x080L
    self.n616 = 0x080L
    self.n579 = 0x80L
    ang_o = self.n571
    self.n574 = self.n571
    imag_o = self.n560
    self.n573 = self.n560
    real_o = self.n538
    self.n572 = self.n538
    self.n561 = 0x00L
    self.n549 = ((self.n470 & 0x80L) >> 7)
    self.n540 = ((self.n470 & 0x80L) >> 7)
    self.n527 = ((self.n491 & 0x80L) >> 7)
    self.n518 = ((self.n491 & 0x80L) >> 7)
    self.n514 = 0x0L
    self.n506 = (self.n491 & 0x40L) | (self.n491 & 0x20L) | (self.n491 & 0x10L) | (self.n491 & 0x8L) | (self.n491 & 0x4L) | (self.n491 & 0x2L) | (self.n491 & 0x1L)
    self.n504 = ((self.n491 & 0x80L) >> 7)
    self.n492 = 0x01L
    self.n480 = ((self.n404 & 0x80L) >> 6) | ((self.n404 & 0x40L) >> 6)
    self.n472 = ((self.n404 & 0x80L) >> 7)
    self.n459 = ((self.n424 & 0x80L) >> 6) | ((self.n424 & 0x40L) >> 6)
    self.n451 = ((self.n424 & 0x80L) >> 7)
    self.n447 = 0x0L
    self.n439 = (self.n424 & 0x40L) | (self.n424 & 0x20L) | (self.n424 & 0x10L) | (self.n424 & 0x8L) | (self.n424 & 0x4L) | (self.n424 & 0x2L) | (self.n424 & 0x1L)
    self.n437 = ((self.n424 & 0x80L) >> 7)
    self.n425 = 0x01L
    self.n413 = ((self.n340 & 0x80L) >> 5) | ((self.n340 & 0x40L) >> 5) | ((self.n340 & 0x20L) >> 5)
    self.n406 = ((self.n340 & 0x80L) >> 7)
    self.n393 = ((self.n359 & 0x80L) >> 5) | ((self.n359 & 0x40L) >> 5) | ((self.n359 & 0x20L) >> 5)
    self.n386 = ((self.n359 & 0x80L) >> 7)
    self.n382 = 0x0L
    self.n374 = (self.n359 & 0x40L) | (self.n359 & 0x20L) | (self.n359 & 0x10L) | (self.n359 & 0x8L) | (self.n359 & 0x4L) | (self.n359 & 0x2L) | (self.n359 & 0x1L)
    self.n372 = ((self.n359 & 0x80L) >> 7)
    self.n360 = 0x03L
    self.n348 = ((self.n278 & 0x80L) >> 4) | ((self.n278 & 0x40L) >> 4) | ((self.n278 & 0x20L) >> 4) | ((self.n278 & 0x10L) >> 4)
    self.n342 = ((self.n278 & 0x80L) >> 7)
    self.n329 = ((self.n296 & 0x80L) >> 4) | ((self.n296 & 0x40L) >> 4) | ((self.n296 & 0x20L) >> 4) | ((self.n296 & 0x10L) >> 4)
    self.n323 = ((self.n296 & 0x80L) >> 7)
    self.n319 = 0x0L
    self.n311 = (self.n296 & 0x40L) | (self.n296 & 0x20L) | (self.n296 & 0x10L) | (self.n296 & 0x8L) | (self.n296 & 0x4L) | (self.n296 & 0x2L) | (self.n296 & 0x1L)
    self.n309 = ((self.n296 & 0x80L) >> 7)
    self.n297 = 0x05L
    self.n285 = ((self.n218 & 0x80L) >> 3) | ((self.n218 & 0x40L) >> 3) | ((self.n218 & 0x20L) >> 3) | ((self.n218 & 0x10L) >> 3) | ((self.n218 & 0x8L) >> 3)
    self.n280 = ((self.n218 & 0x80L) >> 7)
    self.n267 = ((self.n235 & 0x80L) >> 3) | ((self.n235 & 0x40L) >> 3) | ((self.n235 & 0x20L) >> 3) | ((self.n235 & 0x10L) >> 3) | ((self.n235 & 0x8L) >> 3)
    self.n262 = ((self.n235 & 0x80L) >> 7)
    self.n258 = 0x0L
    self.n250 = (self.n235 & 0x40L) | (self.n235 & 0x20L) | (self.n235 & 0x10L) | (self.n235 & 0x8L) | (self.n235 & 0x4L) | (self.n235 & 0x2L) | (self.n235 & 0x1L)
    self.n248 = ((self.n235 & 0x80L) >> 7)
    self.n236 = 0x0AL
    self.n224 = ((self.n160 & 0x80L) >> 2) | ((self.n160 & 0x40L) >> 2) | ((self.n160 & 0x20L) >> 2) | ((self.n160 & 0x10L) >> 2) | ((self.n160 & 0x8L) >> 2) | ((self.n160 & 0x4L) >> 2)
    self.n220 = ((self.n160 & 0x80L) >> 7)
    self.n207 = ((self.n176 & 0x80L) >> 2) | ((self.n176 & 0x40L) >> 2) | ((self.n176 & 0x20L) >> 2) | ((self.n176 & 0x10L) >> 2) | ((self.n176 & 0x8L) >> 2) | ((self.n176 & 0x4L) >> 2)
    self.n203 = ((self.n176 & 0x80L) >> 7)
    self.n199 = 0x0L
    self.n191 = (self.n176 & 0x40L) | (self.n176 & 0x20L) | (self.n176 & 0x10L) | (self.n176 & 0x8L) | (self.n176 & 0x4L) | (self.n176 & 0x2L) | (self.n176 & 0x1L)
    self.n189 = ((self.n176 & 0x80L) >> 7)
    self.n177 = 0x13L
    self.n165 = ((self.n104 & 0x80L) >> 1) | ((self.n104 & 0x40L) >> 1) | ((self.n104 & 0x20L) >> 1) | ((self.n104 & 0x10L) >> 1) | ((self.n104 & 0x8L) >> 1) | ((self.n104 & 0x4L) >> 1) | ((self.n104 & 0x2L) >> 1)
    self.n162 = ((self.n104 & 0x80L) >> 7)
    self.n149 = ((self.n119 & 0x80L) >> 1) | ((self.n119 & 0x40L) >> 1) | ((self.n119 & 0x20L) >> 1) | ((self.n119 & 0x10L) >> 1) | ((self.n119 & 0x8L) >> 1) | ((self.n119 & 0x4L) >> 1) | ((self.n119 & 0x2L) >> 1)
    self.n146 = ((self.n119 & 0x80L) >> 7)
    self.n142 = 0x0L
    self.n134 = (self.n119 & 0x40L) | (self.n119 & 0x20L) | (self.n119 & 0x10L) | (self.n119 & 0x8L) | (self.n119 & 0x4L) | (self.n119 & 0x2L) | (self.n119 & 0x1L)
    self.n132 = ((self.n119 & 0x80L) >> 7)
    self.n120 = 0x20L
    self.n108 = (self.n59 & 0x80L) | (self.n59 & 0x40L) | (self.n59 & 0x20L) | (self.n59 & 0x10L) | (self.n59 & 0x8L) | (self.n59 & 0x4L) | (self.n59 & 0x2L) | (self.n59 & 0x1L)
    self.n93 = (self.n67 & 0x80L) | (self.n67 & 0x40L) | (self.n67 & 0x20L) | (self.n67 & 0x10L) | (self.n67 & 0x8L) | (self.n67 & 0x4L) | (self.n67 & 0x2L) | (self.n67 & 0x1L)
    self.n87 = 0x0L
    self.n79 = (self.n67 & 0x40L) | (self.n67 & 0x20L) | (self.n67 & 0x10L) | (self.n67 & 0x8L) | (self.n67 & 0x4L) | (self.n67 & 0x2L) | (self.n67 & 0x1L)
    self.n77 = ((self.n67 & 0x80L) >> 7)
    self.n46 = 0x00L
    self.n44 = 0x00L
    self.n38 = 0x0L
    self.n32 = (self.n14 & 0x40L) | (self.n14 & 0x20L) | (self.n14 & 0x10L) | (self.n14 & 0x8L) | (self.n14 & 0x4L) | (self.n14 & 0x2L) | (self.n14 & 0x1L)
    self.n30 = ((self.n14 & 0x80L) >> 7)
    self.n7 = ang_i
    self.n6 = imag_i
    self.n5 = real_i
    self.n4 = reset_i
    self.n3 = enable_i
    self.n563 = (self.n502 - self.n561) & 0xFFL
    self.n562 = (self.n502 + self.n561) & 0xFFL
    self.n543 = self.n540 << 1 | self.n540
    self.n521 = self.n518 << 1 | self.n518
    self.n505 = ~self.n504 & 0x1L
    self.n494 = (self.n435 - self.n492) & 0xFFL
    self.n493 = (self.n435 + self.n492) & 0xFFL
    self.n475 = self.n472 << 1 | self.n472
    self.n454 = self.n451 << 1 | self.n451
    self.n438 = ~self.n437 & 0x1L
    self.n427 = (self.n370 - self.n425) & 0xFFL
    self.n426 = (self.n370 + self.n425) & 0xFFL
    self.n409 = self.n406 << 1 | self.n406
    self.n389 = self.n386 << 1 | self.n386
    self.n373 = ~self.n372 & 0x1L
    self.n362 = (self.n307 - self.n360) & 0xFFL
    self.n361 = (self.n307 + self.n360) & 0xFFL
    self.n345 = self.n342 << 1 | self.n342
    self.n326 = self.n323 << 1 | self.n323
    self.n310 = ~self.n309 & 0x1L
    self.n299 = (self.n246 - self.n297) & 0xFFL
    self.n298 = (self.n246 + self.n297) & 0xFFL
    self.n283 = self.n280 << 1 | self.n280
    self.n265 = self.n262 << 1 | self.n262
    self.n249 = ~self.n248 & 0x1L
    self.n238 = (self.n187 - self.n236) & 0xFFL
    self.n237 = (self.n187 + self.n236) & 0xFFL
    self.n223 = self.n220 << 1 | self.n220
    self.n206 = self.n203 << 1 | self.n203
    self.n190 = ~self.n189 & 0x1L
    self.n179 = (self.n130 - self.n177) & 0xFFL
    self.n178 = (self.n130 + self.n177) & 0xFFL
    self.n166 = self.n162 << 7 | self.n165
    self.n150 = self.n146 << 7 | self.n149
    self.n133 = ~self.n132 & 0x1L
    self.n122 = (self.n75 - self.n120) & 0xFFL
    self.n121 = (self.n75 + self.n120) & 0xFFL
    self.n111 = (self.n67 - self.n108) & 0xFFL
    self.n110 = (self.n67 + self.n108) & 0xFFL
    self.n96 = (self.n59 - self.n93) & 0xFFL
    self.n95 = (self.n59 + self.n93) & 0xFFL
    self.n78 = ~self.n77 & 0x1L
    self.n51 = (self.n28 - self.n579) & 0xFFL
    self.n47 = (self.n46 - self.n21) & 0xFFL
    self.n45 = (self.n44 - self.n14) & 0xFFL
    self.n31 = ~self.n30 & 0x1L
    self.n28r = self.n4
    self.n28e = self.n3
    self.n28d = self.n7
    self.n21r = self.n4
    self.n21e = self.n3
    self.n21d = self.n6
    self.n14r = self.n4
    self.n14e = self.n3
    self.n14d = self.n5
    self.n544 = self.n540 << 2 | self.n543
    self.n522 = self.n518 << 2 | self.n521
    self.n507 = self.n505 << 7 | self.n506
    self.n476 = self.n472 << 2 | self.n475
    self.n455 = self.n451 << 2 | self.n454
    self.n440 = self.n438 << 7 | self.n439
    self.n410 = self.n406 << 2 | self.n409
    self.n390 = self.n386 << 2 | self.n389
    self.n375 = self.n373 << 7 | self.n374
    self.n346 = self.n342 << 2 | self.n345
    self.n327 = self.n323 << 2 | self.n326
    self.n312 = self.n310 << 7 | self.n311
    self.n284 = self.n280 << 2 | self.n283
    self.n266 = self.n262 << 2 | self.n265
    self.n251 = self.n249 << 7 | self.n250
    self.n225 = self.n223 << 6 | self.n224
    self.n208 = self.n206 << 6 | self.n207
    self.n192 = self.n190 << 7 | self.n191
    self.n168 = (self.n119 - self.n166) & 0xFFL
    self.n167 = (self.n119 + self.n166) & 0xFFL
    self.n152 = (self.n104 - self.n150) & 0xFFL
    self.n151 = (self.n104 + self.n150) & 0xFFL
    self.n135 = self.n133 << 7 | self.n134
    self.n80 = self.n78 << 7 | self.n79
    self.n33 = self.n31 << 7 | self.n32
    self.n545 = self.n540 << 3 | self.n544
    self.n523 = self.n518 << 3 | self.n522
    self.n515 = self.n514 << 8 | self.n507
    self.n477 = self.n472 << 3 | self.n476
    self.n456 = self.n451 << 3 | self.n455
    self.n448 = self.n447 << 8 | self.n440
    self.n411 = self.n406 << 3 | self.n410
    self.n391 = self.n386 << 3 | self.n390
    self.n383 = self.n382 << 8 | self.n375
    self.n347 = self.n342 << 3 | self.n346
    self.n328 = self.n323 << 3 | self.n327
    self.n320 = self.n319 << 8 | self.n312
    self.n286 = self.n284 << 5 | self.n285
    self.n268 = self.n266 << 5 | self.n267
    self.n259 = self.n258 << 8 | self.n251
    self.n227 = (self.n176 - self.n225) & 0xFFL
    self.n226 = (self.n176 + self.n225) & 0xFFL
    self.n210 = (self.n160 - self.n208) & 0xFFL
    self.n209 = (self.n160 + self.n208) & 0xFFL
    self.n200 = self.n199 << 8 | self.n192
    self.n143 = self.n142 << 8 | self.n135
    self.n88 = self.n87 << 8 | self.n80
    self.n39 = self.n38 << 8 | self.n33
    self.n546 = self.n540 << 4 | self.n545
    self.n524 = self.n518 << 4 | self.n523
    self.n516 = (self.n632 - self.n515) & 0x1FFL
    self.n478 = self.n472 << 4 | self.n477
    self.n457 = self.n451 << 4 | self.n456
    self.n449 = (self.n630 - self.n448) & 0x1FFL
    self.n412 = self.n406 << 4 | self.n411
    self.n392 = self.n386 << 4 | self.n391
    self.n384 = (self.n628 - self.n383) & 0x1FFL
    self.n349 = self.n347 << 4 | self.n348
    self.n330 = self.n328 << 4 | self.n329
    self.n321 = (self.n626 - self.n320) & 0x1FFL
    self.n288 = (self.n235 - self.n286) & 0xFFL
    self.n287 = (self.n235 + self.n286) & 0xFFL
    self.n270 = (self.n218 - self.n268) & 0xFFL
    self.n269 = (self.n218 + self.n268) & 0xFFL
    self.n260 = (self.n624 - self.n259) & 0x1FFL
    self.n201 = (self.n622 - self.n200) & 0x1FFL
    self.n144 = (self.n620 - self.n143) & 0x1FFL
    self.n89 = (self.n618 - self.n88) & 0x1FFL
    self.n42 = (self.n39 - self.n616) & 0x1FFL
    self.n547 = self.n540 << 5 | self.n546
    self.n525 = self.n518 << 5 | self.n524
    self.n517 = ((self.n516 & 0x100L) >> 8)
    self.n479 = self.n472 << 5 | self.n478
    self.n458 = self.n451 << 5 | self.n457
    self.n450 = ((self.n449 & 0x100L) >> 8)
    self.n414 = self.n412 << 3 | self.n413
    self.n394 = self.n392 << 3 | self.n393
    self.n385 = ((self.n384 & 0x100L) >> 8)
    self.n351 = (self.n296 - self.n349) & 0xFFL
    self.n350 = (self.n296 + self.n349) & 0xFFL
    self.n332 = (self.n278 - self.n330) & 0xFFL
    self.n331 = (self.n278 + self.n330) & 0xFFL
    self.n322 = ((self.n321 & 0x100L) >> 8)
    self.n261 = ((self.n260 & 0x100L) >> 8)
    self.n202 = ((self.n201 & 0x100L) >> 8)
    self.n145 = ((self.n144 & 0x100L) >> 8)
    self.n90 = ((self.n89 & 0x100L) >> 8)
    self.n43 = ((self.n42 & 0x100L) >> 8)
    if self.n517:
      self.n564 = self.n562
    else:
      self.n564 = self.n563
    self.n548 = self.n540 << 6 | self.n547
    self.n539 = ~self.n517 & 0x1L
    self.n526 = self.n518 << 6 | self.n525
    if self.n450:
      self.n495 = self.n493
    else:
      self.n495 = self.n494
    self.n481 = self.n479 << 2 | self.n480
    self.n471 = ~self.n450 & 0x1L
    self.n460 = self.n458 << 2 | self.n459
    if self.n385:
      self.n428 = self.n426
    else:
      self.n428 = self.n427
    self.n416 = (self.n359 - self.n414) & 0xFFL
    self.n415 = (self.n359 + self.n414) & 0xFFL
    self.n405 = ~self.n385 & 0x1L
    self.n396 = (self.n340 - self.n394) & 0xFFL
    self.n395 = (self.n340 + self.n394) & 0xFFL
    if self.n322:
      self.n363 = self.n361
    else:
      self.n363 = self.n362
    self.n341 = ~self.n322 & 0x1L
    if self.n322:
      self.n333 = self.n331
    else:
      self.n333 = self.n332
    if self.n261:
      self.n300 = self.n298
    else:
      self.n300 = self.n299
    self.n279 = ~self.n261 & 0x1L
    if self.n261:
      self.n271 = self.n269
    else:
      self.n271 = self.n270
    if self.n202:
      self.n239 = self.n237
    else:
      self.n239 = self.n238
    self.n219 = ~self.n202 & 0x1L
    if self.n202:
      self.n211 = self.n209
    else:
      self.n211 = self.n210
    if self.n145:
      self.n180 = self.n178
    else:
      self.n180 = self.n179
    self.n161 = ~self.n145 & 0x1L
    if self.n145:
      self.n153 = self.n151
    else:
      self.n153 = self.n152
    if self.n90:
      self.n123 = self.n121
    else:
      self.n123 = self.n122
    self.n105 = ~self.n90 & 0x1L
    if self.n90:
      self.n97 = self.n95
    else:
      self.n97 = self.n96
    if self.n43:
      self.n68 = self.n51
    else:
      self.n68 = self.n28
    if self.n43:
      self.n60 = self.n47
    else:
      self.n60 = self.n21
    if self.n43:
      self.n52 = self.n45
    else:
      self.n52 = self.n14
    self.n571r = self.n4
    self.n571e = self.n3
    self.n571d = self.n564
    self.n550 = self.n548 << 1 | self.n549
    self.n528 = self.n526 << 1 | self.n527
    self.n502r = self.n4
    self.n502e = self.n3
    self.n502d = self.n495
    self.n483 = (self.n424 - self.n481) & 0xFFL
    self.n482 = (self.n424 + self.n481) & 0xFFL
    self.n462 = (self.n404 - self.n460) & 0xFFL
    self.n461 = (self.n404 + self.n460) & 0xFFL
    self.n435r = self.n4
    self.n435e = self.n3
    self.n435d = self.n428
    if self.n405:
      self.n417 = self.n415
    else:
      self.n417 = self.n416
    if self.n385:
      self.n397 = self.n395
    else:
      self.n397 = self.n396
    self.n370r = self.n4
    self.n370e = self.n3
    self.n370d = self.n363
    if self.n341:
      self.n352 = self.n350
    else:
      self.n352 = self.n351
    self.n340r = self.n4
    self.n340e = self.n3
    self.n340d = self.n333
    self.n307r = self.n4
    self.n307e = self.n3
    self.n307d = self.n300
    if self.n279:
      self.n289 = self.n287
    else:
      self.n289 = self.n288
    self.n278r = self.n4
    self.n278e = self.n3
    self.n278d = self.n271
    self.n246r = self.n4
    self.n246e = self.n3
    self.n246d = self.n239
    if self.n219:
      self.n228 = self.n226
    else:
      self.n228 = self.n227
    self.n218r = self.n4
    self.n218e = self.n3
    self.n218d = self.n211
    self.n187r = self.n4
    self.n187e = self.n3
    self.n187d = self.n180
    if self.n161:
      self.n169 = self.n167
    else:
      self.n169 = self.n168
    self.n160r = self.n4
    self.n160e = self.n3
    self.n160d = self.n153
    self.n130r = self.n4
    self.n130e = self.n3
    self.n130d = self.n123
    if self.n105:
      self.n112 = self.n110
    else:
      self.n112 = self.n111
    self.n104r = self.n4
    self.n104e = self.n3
    self.n104d = self.n97
    self.n75r = self.n4
    self.n75e = self.n3
    self.n75d = self.n68
    self.n67r = self.n4
    self.n67e = self.n3
    self.n67d = self.n60
    self.n59r = self.n4
    self.n59e = self.n3
    self.n59d = self.n52
    self.n552 = (self.n491 - self.n550) & 0xFFL
    self.n551 = (self.n491 + self.n550) & 0xFFL
    self.n530 = (self.n470 - self.n528) & 0xFFL
    self.n529 = (self.n470 + self.n528) & 0xFFL
    if self.n471:
      self.n484 = self.n482
    else:
      self.n484 = self.n483
    if self.n450:
      self.n463 = self.n461
    else:
      self.n463 = self.n462
    self.n424r = self.n4
    self.n424e = self.n3
    self.n424d = self.n417
    self.n404r = self.n4
    self.n404e = self.n3
    self.n404d = self.n397
    self.n359r = self.n4
    self.n359e = self.n3
    self.n359d = self.n352
    self.n296r = self.n4
    self.n296e = self.n3
    self.n296d = self.n289
    self.n235r = self.n4
    self.n235e = self.n3
    self.n235d = self.n228
    self.n176r = self.n4
    self.n176e = self.n3
    self.n176d = self.n169
    self.n119r = self.n4
    self.n119e = self.n3
    self.n119d = self.n112
    if self.n539:
      self.n553 = self.n551
    else:
      self.n553 = self.n552
    if self.n517:
      self.n531 = self.n529
    else:
      self.n531 = self.n530
    self.n491r = self.n4
    self.n491e = self.n3
    self.n491d = self.n484
    self.n470r = self.n4
    self.n470e = self.n3
    self.n470d = self.n463
    self.n560r = self.n4
    self.n560e = self.n3
    self.n560d = self.n553
    self.n538r = self.n4
    self.n538e = self.n3
    self.n538d = self.n531
    return (real_o, imag_o, ang_o, )

  def cycle_clock(self):
    if self.n14r:
      self.n14 = 0L
    elif self.n14e:
        self.n14 = self.n14d
    if self.n21r:
      self.n21 = 0L
    elif self.n21e:
        self.n21 = self.n21d
    if self.n28r:
      self.n28 = 0L
    elif self.n28e:
        self.n28 = self.n28d
    if self.n59r:
      self.n59 = 0L
    elif self.n59e:
        self.n59 = self.n59d
    if self.n67r:
      self.n67 = 0L
    elif self.n67e:
        self.n67 = self.n67d
    if self.n75r:
      self.n75 = 0L
    elif self.n75e:
        self.n75 = self.n75d
    if self.n104r:
      self.n104 = 0L
    elif self.n104e:
        self.n104 = self.n104d
    if self.n119r:
      self.n119 = 0L
    elif self.n119e:
        self.n119 = self.n119d
    if self.n130r:
      self.n130 = 0L
    elif self.n130e:
        self.n130 = self.n130d
    if self.n160r:
      self.n160 = 0L
    elif self.n160e:
        self.n160 = self.n160d
    if self.n176r:
      self.n176 = 0L
    elif self.n176e:
        self.n176 = self.n176d
    if self.n187r:
      self.n187 = 0L
    elif self.n187e:
        self.n187 = self.n187d
    if self.n218r:
      self.n218 = 0L
    elif self.n218e:
        self.n218 = self.n218d
    if self.n235r:
      self.n235 = 0L
    elif self.n235e:
        self.n235 = self.n235d
    if self.n246r:
      self.n246 = 0L
    elif self.n246e:
        self.n246 = self.n246d
    if self.n278r:
      self.n278 = 0L
    elif self.n278e:
        self.n278 = self.n278d
    if self.n296r:
      self.n296 = 0L
    elif self.n296e:
        self.n296 = self.n296d
    if self.n307r:
      self.n307 = 0L
    elif self.n307e:
        self.n307 = self.n307d
    if self.n340r:
      self.n340 = 0L
    elif self.n340e:
        self.n340 = self.n340d
    if self.n359r:
      self.n359 = 0L
    elif self.n359e:
        self.n359 = self.n359d
    if self.n370r:
      self.n370 = 0L
    elif self.n370e:
        self.n370 = self.n370d
    if self.n404r:
      self.n404 = 0L
    elif self.n404e:
        self.n404 = self.n404d
    if self.n424r:
      self.n424 = 0L
    elif self.n424e:
        self.n424 = self.n424d
    if self.n435r:
      self.n435 = 0L
    elif self.n435e:
        self.n435 = self.n435d
    if self.n470r:
      self.n470 = 0L
    elif self.n470e:
        self.n470 = self.n470d
    if self.n491r:
      self.n491 = 0L
    elif self.n491e:
        self.n491 = self.n491d
    if self.n502r:
      self.n502 = 0L
    elif self.n502e:
        self.n502 = self.n502d
    if self.n538r:
      self.n538 = 0L
    elif self.n538e:
        self.n538 = self.n538d
    if self.n560r:
      self.n560 = 0L
    elif self.n560e:
        self.n560 = self.n560d
    if self.n571r:
      self.n571 = 0L
    elif self.n571e:
        self.n571 = self.n571d

  def sim_init(self, vcdFile):
    self.sim_file = open(vcdFile, 'w')
    self.sim_count = 1
    self.init()
    self.sim_n3 = self.n3
    self.sim_n4 = self.n4
    self.sim_n5 = self.n5
    self.sim_n6 = self.n6
    self.sim_n7 = self.n7
    self.sim_n572 = self.n572
    self.sim_n573 = self.n573
    self.sim_n574 = self.n574
    self.sim_file.write("$date\n")
    self.sim_file.write("  " + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "\n")
    self.sim_file.write("$end\n")
    self.sim_file.write("$version\n  Confluence 0.6.3 -- Launchbird Design Systems, Inc.\n$end\n")
    self.sim_file.write("$timescale\n  1 ns\n$end\n")
    self.sim_file.write("$scope module cf_cordic_v_8_8_8 $end\n")
    self.sim_file.write("$var wire 1 ! enable_i $end\n")
    self.sim_file.write("$var wire 1 \" reset_i $end\n")
    self.sim_file.write("$var wire 8 # real_i $end\n")
    self.sim_file.write("$var wire 8 $ imag_i $end\n")
    self.sim_file.write("$var wire 8 % ang_i $end\n")
    self.sim_file.write("$var wire 8 & real_o $end\n")
    self.sim_file.write("$var wire 8 ' imag_o $end\n")
    self.sim_file.write("$var wire 8 ( ang_o $end\n")
    self.sim_file.write("$upscope $end\n")
    self.sim_file.write("$enddefinitions $end\n")
    self.sim_file.write("#0\n")
    self.sim_file.write("$dumpvars\n")
    if self.n3:
      self.sim_file.write("1!\n")
    else:
      self.sim_file.write("0!\n")
    if self.n4:
      self.sim_file.write("1\"\n")
    else:
      self.sim_file.write("0\"\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n5 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n5 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" #\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n6 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n6 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" $\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n7 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n7 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" %\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n572 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n572 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" &\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n573 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n573 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" '\n")
    found = 0
    for bit in range(7, -1, -1):
      if found:
        if self.n574 & (2L ** bit):
          self.sim_file.write("1")
        else:
          self.sim_file.write("0")
      else:
        if self.n574 & (2L ** bit):
          self.sim_file.write("b1")
          found = 1
    if not found:
      self.sim_file.write("b0")
    self.sim_file.write(" (\n")
    self.sim_file.write("$end\n")

  def sim_end(self):
    self.sim_file.write("#%d\n" % self.sim_count)
    self.sim_file.close()

  def sim_sample(self):
    changed = 0
    if self.sim_n3 != self.n3:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      if self.n3:
        self.sim_file.write("1!\n")
      else:
        self.sim_file.write("0!\n")
      self.sim_n3 = self.n3
    if self.sim_n4 != self.n4:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      if self.n4:
        self.sim_file.write("1\"\n")
      else:
        self.sim_file.write("0\"\n")
      self.sim_n4 = self.n4
    if self.sim_n5 != self.n5:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n5 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n5 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" #\n")
      self.sim_n5 = self.n5
    if self.sim_n6 != self.n6:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n6 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n6 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" $\n")
      self.sim_n6 = self.n6
    if self.sim_n7 != self.n7:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n7 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n7 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" %\n")
      self.sim_n7 = self.n7
    if self.sim_n572 != self.n572:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n572 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n572 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" &\n")
      self.sim_n572 = self.n572
    if self.sim_n573 != self.n573:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n573 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n573 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" '\n")
      self.sim_n573 = self.n573
    if self.sim_n574 != self.n574:
      if not changed:
        changed = 1
        self.sim_file.write("#%d\n" % self.sim_count)
      found = 0
      for bit in range(7, -1, -1):
        if found:
          if self.n574 & (2L ** bit):
            self.sim_file.write("1")
          else:
            self.sim_file.write("0")
        else:
          if self.n574 & (2L ** bit):
            self.sim_file.write("b1")
            found = 1
      if not found:
        self.sim_file.write("b0")
      self.sim_file.write(" (\n")
      self.sim_n574 = self.n574
    self.sim_count = self.sim_count + 1

