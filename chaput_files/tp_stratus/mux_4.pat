   in i0 (3 downto 0) X;;
   in i1 (3 downto 0) X;;
   in cmd B;;
  out s (3 downto 0) X;;
   in vdd B;;
   in vss B;;

begin

<          0 ns> : 0 0 0 ?0 1 0 ;
<         10 ns> : 0 0 1 ?0 1 0 ;
<         20 ns> : 0 1 0 ?0 1 0 ;
<         30 ns> : 0 1 1 ?1 1 0 ;
<         40 ns> : 0 2 0 ?0 1 0 ;
<         50 ns> : 0 2 1 ?2 1 0 ;
<         60 ns> : 0 3 0 ?0 1 0 ;
<         70 ns> : 0 3 1 ?3 1 0 ;
<         80 ns> : 1 0 0 ?1 1 0 ;
<         90 ns> : 1 0 1 ?0 1 0 ;
<        100 ns> : 1 1 0 ?1 1 0 ;
<        110 ns> : 1 1 1 ?1 1 0 ;
<        120 ns> : 1 2 0 ?1 1 0 ;
<        130 ns> : 1 2 1 ?2 1 0 ;
<        140 ns> : 1 3 0 ?1 1 0 ;
<        150 ns> : 1 3 1 ?3 1 0 ;
<        160 ns> : 2 0 0 ?2 1 0 ;
<        170 ns> : 2 0 1 ?0 1 0 ;
<        180 ns> : 2 1 0 ?2 1 0 ;
<        190 ns> : 2 1 1 ?1 1 0 ;
<        200 ns> : 2 2 0 ?2 1 0 ;
<        210 ns> : 2 2 1 ?2 1 0 ;
<        220 ns> : 2 3 0 ?2 1 0 ;
<        230 ns> : 2 3 1 ?3 1 0 ;
<        240 ns> : 3 0 0 ?3 1 0 ;
<        250 ns> : 3 0 1 ?0 1 0 ;
<        260 ns> : 3 1 0 ?3 1 0 ;
<        270 ns> : 3 1 1 ?1 1 0 ;
<        280 ns> : 3 2 0 ?3 1 0 ;
<        290 ns> : 3 2 1 ?2 1 0 ;
<        300 ns> : 3 3 0 ?3 1 0 ;
<        310 ns> : 3 3 1 ?3 1 0 ;

end;
