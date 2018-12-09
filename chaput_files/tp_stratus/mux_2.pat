   in i0 (1 downto 0) X;;
   in i1 (1 downto 0) X;;
   in cmd B;;
  out s (1 downto 0) X;;
   in vdd B;;
   in vss B;;

begin

<          0 ns> : 0 0 0 ?0 1 0 ;
<         10 ns> : 0 0 1 ?0 1 0 ;
<         20 ns> : 0 1 0 ?0 1 0 ;
<         30 ns> : 0 1 1 ?1 1 0 ;
<         40 ns> : 1 0 0 ?1 1 0 ;
<         50 ns> : 1 0 1 ?0 1 0 ;
<         60 ns> : 1 1 0 ?1 1 0 ;
<         70 ns> : 1 1 1 ?1 1 0 ;

end;
