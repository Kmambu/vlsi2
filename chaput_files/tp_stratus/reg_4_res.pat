
-- description generated by Pat driver

--			date     : Mon Dec 10 10:21:38 2018
--			revision : v109

--			sequence : reg_4

-- input / output list :
in       d (3 downto 0) X;;
in       ck B;;
out      q (3 downto 0) X;;
in       vdd B;;
in       vss B;;

begin

-- Pattern description :

--                  d c  q v v  
--                    k    d s  
--                         d s  

<          0 ps>  : 0 0 ?u 1 0 ;
<      10000 ps>  : 0 1 ?0 1 0 ;
<      20000 ps>  : 1 0 ?0 1 0 ;
<      30000 ps>  : 1 1 ?1 1 0 ;
<      40000 ps>  : 2 0 ?1 1 0 ;
<      50000 ps>  : 2 1 ?2 1 0 ;
<      60000 ps>  : 3 0 ?2 1 0 ;
<      70000 ps>  : 3 1 ?3 1 0 ;

end;
