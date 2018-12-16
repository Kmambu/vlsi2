library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity reset_synchronizer_tb is
end reset_synchronizer_tb;

architecture behav of reset_synchronizer_tb is
	-- Definition of the component
	component reset_synchronizer
	port ( i   : in  std_logic;
	       clk : in  std_logic;
	       q   : out std_logic );
	end component;
	-- Definition of the signals
	signal i   : std_logic;
	signal clk : std_logic := '0';
	signal q   : std_logic;
begin
	-- Instantiation of the clock
	clk <= not clk after 5 ns;
	-- Instantiation of the component
	U0 : reset_synchronizer
	port map ( i   => i,
	           clk => clk,
			   q   => q );
	process
	begin
		i <= '0';
		wait for 30 ns;
		i <= '1';
		wait for 30 ns;
		assert false report "Testbench successful" severity note;
		wait;
	end process;
end behav;
