-- DDS Frequency Synthesizer
--
-- Output frequency is f=ftw_i/2^ftw_width*fclk
-- Output initial phase is phi=phase_i/2^phase_width*2*pi
-- 
-- Copyright (C) 2009 Martin Kumm
-- 
-- This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
-- 
-- This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
-- warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
-- 
-- You should have received a copy of the GNU General Public License along with this program; 
-- if not, see <http://www.gnu.org/licenses/>.

-- Package Definition

library ieee;
use ieee.std_logic_1164.all;
use IEEE.STD_LOGIC_arith.all;
use IEEE.STD_LOGIC_unsigned.all;
use work.sine_lut_pkg.all;

package dds_synthesizer_pipe_pkg is
  component dds_synthesizer_pipe
    generic(
      ftw_width : integer
      );
    port(
      clk_i   : in  std_logic;
      rst_i   : in  std_logic;
      ftw_i   : in  std_logic_vector(ftw_width-1 downto 0);
      phase_i : in  std_logic_vector(PHASE_WIDTH-1 downto 0);
      phase_o : out std_logic_vector(PHASE_WIDTH-1 downto 0);
      ampl_o  : out std_logic_vector(AMPL_WIDTH-1 downto 0)
      );
  end component;
end dds_synthesizer_pipe_pkg;

package body dds_synthesizer_pipe_pkg is
end dds_synthesizer_pipe_pkg;

-- Entity Definition

library ieee;
use ieee.std_logic_1164.all;
use IEEE.STD_LOGIC_arith.all;
use IEEE.STD_LOGIC_unsigned.all;
use work.sine_lut_pkg.all;
library work;
use work.feedf_consts_pack.all;

entity dds_synthesizer_pipe is
  generic(
    ftw_width : integer := 32
    );
  port(
    clk_i   : in  std_logic;
    rst_i   : in  std_logic;
    ftw_i   : in  std_logic_vector(ftw_width-1 downto 0);
    phase_i : in  std_logic_vector(PHASE_WIDTH-1 downto 0);
    phase_o : out std_logic_vector(PHASE_WIDTH-1 downto 0);
    ampl_o  : out std_logic_vector(AMPL_WIDTH-1 downto 0)
    );
end dds_synthesizer_pipe;

architecture dds_synthesizer_arch of dds_synthesizer_pipe is

  signal ftw_accu,ftw_accu_w1               : std_logic_vector(ftw_width-1 downto 0):=(others=>'0');
  signal phase_w3,phase_w2,phase_w1,phase         : std_logic_vector(PHASE_WIDTH-1 downto 0);
  signal lut_in                 : std_logic_vector(PHASE_WIDTH-3 downto 0);
  signal lut_out                : std_logic_vector(AMPL_WIDTH-1 downto 0);
  signal lut_out_delay          : std_logic_vector(AMPL_WIDTH-1 downto 0);
  signal lut_out_inv_delay      : std_logic_vector(AMPL_WIDTH-1 downto 0);
  signal quadrant_2_or_4,quadrant_2_or_4_w1,quadrant_2_or_4_w2        : std_logic;
  signal quadrant_3_or_4        : std_logic;
  signal quadrant_3_or_4_delay  : std_logic;
  signal quadrant_3_or_4_2delay,quadrant_3_or_4_2delay_w1,quadrant_3_or_4_2delay_w2 : std_logic;
  signal ram_value				: std_logic_vector(AMPL_WIDTH-1 downto 0);

begin

  phase_o         <= phase_w2;
  quadrant_2_or_4 <= phase(PHASE_WIDTH-2);
  quadrant_3_or_4 <= phase(PHASE_WIDTH-1);


  process (clk_i) is
  begin
	if rising_edge(clk_i) then

	  if quadrant_2_or_4 = '0' then 
  		lut_in <= phase(PHASE_WIDTH-3 downto 0);
	  else
		lut_in <= conv_std_logic_vector(2**(PHASE_WIDTH-2)-conv_integer(phase(PHASE_WIDTH-3 downto 0)), PHASE_WIDTH-2);
	  end if;

	  if quadrant_3_or_4_2delay_w2 = '0' then
		ampl_o <= lut_out_delay;
	  else
		ampl_o <= lut_out_inv_delay;
	  end if;
	  quadrant_2_or_4_w1<=quadrant_2_or_4;
	  quadrant_2_or_4_w2<=quadrant_2_or_4_w1;
	  quadrant_3_or_4_2delay_w1<=quadrant_3_or_4_2delay;
	  quadrant_3_or_4_2delay_w2<=quadrant_3_or_4_2delay_w1;
	  phase_w1<=phase;
	  phase_w2<=phase_w1;
	  phase_w3<=phase_w2;
	end if;
  end process;


  process (clk_i) is
  begin
	if rising_edge(clk_i) then
		ram_value<=sine_lut(conv_integer(lut_in));
	end if;
  end process;


  process (clk_i, rst_i)
  begin
    if rst_i = '1' then
      phase  <= (others => '0');
      lut_out <= (others => '0');
      lut_out_delay <= (others => '0');
      lut_out_inv_delay <= (others => '0');
      quadrant_3_or_4_delay <= '0';
      quadrant_3_or_4_2delay <= '0';
	  ftw_accu<=(others => '0');
	  ftw_accu_w1<=(others => '0');
    elsif clk_i'event and clk_i = '1' then
  	  ftw_accu_w1<=ftw_accu;
      ftw_accu <= ftw_accu + rats(ftw_i);
      phase    <= ftw_accu_w1(ftw_width-1 downto ftw_width-PHASE_WIDTH) + phase_i;
      if quadrant_2_or_4_w2 = '1' and phase_w2(PHASE_WIDTH - 3 downto 0) = conv_std_logic_vector (0, PHASE_WIDTH - 2) then
        lut_out <= conv_std_logic_vector(2**(AMPL_WIDTH - 1) - 1, AMPL_WIDTH);
      else
        lut_out <= ram_value;--sine_lut(conv_integer(lut_in)); --# time phase_w2 = ram_value
      end if;
      quadrant_3_or_4_delay <= quadrant_3_or_4;
      quadrant_3_or_4_2delay <= quadrant_3_or_4_delay;
      lut_out_inv_delay <= conv_std_logic_vector(-1*conv_integer(lut_out), AMPL_WIDTH);
      lut_out_delay <= lut_out;
    end if;
  end process;

end dds_synthesizer_arch;
