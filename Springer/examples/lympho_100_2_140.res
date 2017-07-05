IL12+ : !IL12 /\ (!TBet \/ !GATA3 ) /\ (!TBet \/ !IL4R ) /\ (!TBet \/ !STAT6 )
IL12- : IL12 /\ (!TBet \/ !GATA3 )
IL4+ : !IL4
IL4- : IL4
STAT4+ : !STAT4 /\ !GATA3 /\ IL12R
STAT4- : STAT4 /\ (GATA3 \/ !IL12R )
IFNg+ : !IFNg /\ (STAT4 \/ TBet )
IFNg- : IFNg /\ (!STAT4 \/ !TBet )
TBet+ : !TBet /\ !GATA3 /\ STAT1
TBet- : TBet /\ (GATA3 \/ !STAT1 )
GATA3+ : !TBet /\ !GATA3 /\ STAT6
GATA3- : GATA3 /\ (TBet \/ !STAT6 )
STAT1+ : !STAT1 /\ IFNgR
STAT1- : STAT1 /\ !IFNgR
IFNgR+ : IFNg /\ !IFNgR /\ !SOCS1
IFNgR- : IFNgR /\ (!IFNg \/ SOCS1 )
SOCS1+ : !SOCS1 /\ (TBet \/ STAT1 )
SOCS1- : SOCS1 /\ (!TBet \/ !STAT1 )
IL4R+ : IL4 /\ !SOCS1 /\ !IL4R
IL4R- : IL4R /\ (!IL4 \/ SOCS1 )
IL12R+ : IL12 /\ !IL12R /\ !STAT6 /\ (!TBet \/ !GATA3 )
IL12R- : IL12R /\ (!IL12 \/ STAT6 )
STAT6+ : IL4R /\ !STAT6 /\ (!TBet \/ !GATA3 )
STAT6- : !IL4R /\ STAT6 /\ (!TBet \/ !GATA3 )
