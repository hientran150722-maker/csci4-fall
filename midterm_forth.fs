: fsquare 
fdup f*
;

: distance ( x2, y2, x1, y1 -- d)
frot fswap f- fsquare frot frot f- fsquare f+ fsqrt
;
5e 4e 1e 1e distance f.


