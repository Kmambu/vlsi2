   in d (1 downto 0) X;;
   in ck B;;
  out q (1 downto 0) X;;
   in vdd B;;
   in vss B;;

begin

<          0 ns> : 0 0 ?* 1 0 ;
<         10 ns> : 0 1 ?0 1 0 ;
<         20 ns> : 1 0 ?0 1 0 ;
<         30 ns> : 1 1 ?1 1 0 ;

end;
