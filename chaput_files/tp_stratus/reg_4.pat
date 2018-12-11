   in d (3 downto 0) X;;
   in ck B;;
  out q (3 downto 0) X;;
   in vdd B;;
   in vss B;;

begin

<          0 ns> : 0 0 ?* 1 0 ;
<         10 ns> : 0 1 ?0 1 0 ;
<         20 ns> : 1 0 ?0 1 0 ;
<         30 ns> : 1 1 ?1 1 0 ;
<         40 ns> : 2 0 ?1 1 0 ;
<         50 ns> : 2 1 ?2 1 0 ;
<         60 ns> : 3 0 ?2 1 0 ;
<         70 ns> : 3 1 ?3 1 0 ;

end;
