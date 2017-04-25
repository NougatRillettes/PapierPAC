IL12+ : True
IL12- : True
IL4+ : True
IL4- : True
STAT4+ : !GATA3 /\ IL12R
STAT4- : (GATA3 \/ !IL12R )
IFNg+ : (STAT4 \/ TBet )
IFNg- : (!STAT4 \/ !TBet )
TBet+ : !TBet /\ !GATA3 /\ STAT1
TBet- : TBet /\ !GATA3 /\ !STAT1
GATA3+ : !TBet /\ STAT6
GATA3- : !TBet /\ !STAT6
STAT1+ : IFNgR
STAT1- : !IFNgR
IFNgR+ : IFNg /\ !SOCS1
IFNgR- : (!IFNg \/ SOCS1 )
SOCS1+ : (TBet \/ STAT1 )
SOCS1- : (!TBet \/ !STAT1 )
IL4R+ : IL4 /\ !SOCS1
IL4R- : (!IL4 \/ SOCS1 )
IL12R+ : IL12 /\ !STAT6
IL12R- : (!IL12 \/ STAT6 )
STAT6+ : IL4R
STAT6- : !IL4R
