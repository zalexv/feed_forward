library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;
library work;
use work.feedf_consts_pack.all;

entity rotate_demod is
	port(
		clk : in STD_LOGIC;
		reset : in std_logic;

		stop_demod: in std_logic;
		start_demod: in std_logic;
		start_rotateI: in std_logic_vector(15 downto 0); --# ������� ��� ��� ������� �� ������� ���������(� �� �� ������� ���� ��������� �������)
		start_rotateQ: in std_logic_vector(15 downto 0);

		i_sampleI: in std_logic_vector(15 downto 0);
		i_sampleQ: in std_logic_vector(15 downto 0);

		demodI: out std_logic_vector(15 downto 0);
		demodQ: out std_logic_vector(15 downto 0);
		demod_ce: out std_logic
		);
end rotate_demod;



architecture rotate_demod of rotate_demod is

signal rotate_it_ce:std_logic;
signal A_I: std_logic_vector(15 downto 0);
signal B_Q: std_logic_vector(15 downto 0);
signal C_I: std_logic_vector(15 downto 0);
signal D_Q: std_logic_vector(15 downto 0);

type Tstm is (WAITING,STARTING,ROTATING);
signal stm:Tstm;

begin

complex_mult_inst: entity work.complex_mult
	generic (
		CONJUGATION:std_logic:='1' --# ��������� �� ����������� �����, ���� '1' - �� ���������
	);
	port(
		clk =>clk,
		i_ce =>rotate_it_ce, --# ���� ����� �� ������ ��������� ���� 16+32+3=51 �����		
		A_I =>A_I,
		B_Q =>B_Q,

		C_I =>C_I,
		D_Q =>D_Q,


		o_I=>open,
		o_Q=>open,
		out_ce =>open
		);



process (clk) is
begin		
	if rising_edge(clk) then
		if reset='1' then
		else
		end if;
	end if;
end process;

	
end rotate_demod;
