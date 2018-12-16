library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity reset_synchronizer is
	port ( i   : in  std_logic;
	       clk : in  std_logic;
	       q   : out std_logic );
end reset_synchronizer;

architecture behav of reset_synchronizer is
	signal reg0 : std_logic;
	signal reg1 : std_logic;
begin
	q    <= reg1;
	clocked : process(clk)
	begin
		if rising_edge(clk) then
			reg0 <= i   ;
			reg1 <= reg0;
		else
			reg0 <= reg0;
			reg1 <= reg1;
		end if;
	end process clocked;
end behav;
