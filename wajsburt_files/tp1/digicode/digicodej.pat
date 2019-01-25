
-- description generated by Pat driver

--			date     : Wed Jan 23 15:54:03 2019
--			revision : v109

--			sequence : digicode

-- input / output list :
in       ck B;;;
in       vdd B;;;
in       vss B;;;
in       reset B;;;
in       jour B;;;
in       o B;;;
in       kbd B;;;
in       i (3 downto 0) X;;;
out      porte B;;;
out      alarm B;;;

begin

-- Pattern description :

--                                                 c  v  v  r  j  o  k  i   p   a   
--                                                 k  d  s  e  o     b      o   l   
--                                                    d  s  s  u     d      r   a   
--                                                          e  r            t   r   
--                                                          t               e   m   

<          0 ps>init_0                           : 0  1  0  1  0  0  0  0  ?u  ?u  ;
<          0 ps>                                 : 1  1  0  1  0  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  1  0  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  1  0  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  1  1  0  0  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  1  1  0  0  ?1  ?0  ;
<          0 ps>                                 : 0  1  0  0  1  0  0  0  ?1  ?0  ;
<          0 ps>                                 : 1  1  0  0  1  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  1  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  1  0  0  0  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  b  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  b  ?0  ?1  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  b  ?0  ?1  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  b  ?0  ?1  ;
<          0 ps>                                 : 0  1  0  1  0  0  0  b  ?0  ?1  ;
<          0 ps>                                 : 1  1  0  1  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  b  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  5  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  5  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  5  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  5  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  5  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  5  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  3  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  3  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  3  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  3  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  a  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  a  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  a  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  a  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  1  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  1  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  1  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  1  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  1  7  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  7  ?1  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  7  ?1  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  7  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  7  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  7  ?0  ?0  ;
<          0 ps>                                 : 0  1  0  0  0  0  0  7  ?0  ?0  ;
<          0 ps>                                 : 1  1  0  0  0  0  0  7  ?0  ?0  ;

end;
