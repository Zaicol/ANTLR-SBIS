# Generated from ASICLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,75,522,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,1,0,1,0,1,0,4,0,213,8,0,11,0,12,0,214,1,1,4,1,218,8,1,11,1,
        12,1,219,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,
        1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,
        15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,
        22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,
        28,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,
        33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,
        38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,
        42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,
        47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,
        50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,
        54,1,54,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,
        57,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,60,1,60,1,60,1,60,1,61,4,
        61,392,8,61,11,61,12,61,393,1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,
        65,1,66,1,66,1,67,1,67,1,68,1,68,1,69,1,69,1,70,1,70,1,71,1,71,1,
        72,1,72,1,73,1,73,1,74,1,74,1,75,1,75,1,76,1,76,1,77,1,77,1,77,1,
        78,1,78,1,79,1,79,1,79,1,80,1,80,1,81,1,81,1,82,1,82,1,83,1,83,1,
        83,1,84,1,84,1,84,1,85,1,85,1,85,1,86,1,86,1,86,1,87,1,87,1,87,1,
        88,1,88,1,88,1,89,1,89,1,89,1,90,1,90,1,90,1,91,1,91,1,92,1,92,1,
        93,1,93,1,94,1,94,1,95,1,95,1,95,1,95,1,96,1,96,1,96,1,96,1,97,1,
        97,1,97,1,97,1,98,1,98,1,98,1,98,1,99,1,99,1,99,1,99,1,99,1,100,
        1,100,1,100,1,100,1,101,1,101,1,101,5,101,500,8,101,10,101,12,101,
        503,9,101,1,102,1,102,1,102,1,102,1,103,1,103,5,103,511,8,103,10,
        103,12,103,514,9,103,1,103,3,103,517,8,103,1,103,1,103,1,103,1,103,
        0,0,104,1,1,3,2,5,0,7,0,9,0,11,0,13,0,15,0,17,0,19,0,21,0,23,0,25,
        0,27,0,29,0,31,0,33,0,35,0,37,0,39,0,41,0,43,0,45,0,47,0,49,0,51,
        0,53,0,55,0,57,0,59,0,61,0,63,3,65,4,67,5,69,6,71,7,73,8,75,9,77,
        10,79,11,81,12,83,13,85,14,87,15,89,16,91,17,93,18,95,19,97,20,99,
        21,101,22,103,23,105,24,107,25,109,26,111,27,113,28,115,29,117,30,
        119,31,121,32,123,33,125,34,127,35,129,36,131,37,133,38,135,39,137,
        40,139,41,141,42,143,43,145,44,147,45,149,46,151,47,153,48,155,49,
        157,50,159,51,161,52,163,53,165,54,167,55,169,56,171,57,173,58,175,
        59,177,60,179,61,181,62,183,63,185,64,187,65,189,66,191,67,193,68,
        195,69,197,70,199,71,201,72,203,73,205,74,207,75,1,0,30,3,0,65,90,
        95,95,97,122,3,0,48,57,65,70,97,102,2,0,65,65,97,97,2,0,66,66,98,
        98,2,0,67,67,99,99,2,0,68,68,100,100,2,0,69,69,101,101,2,0,70,70,
        102,102,2,0,71,71,103,103,2,0,72,72,104,104,2,0,73,73,105,105,2,
        0,74,74,106,106,2,0,75,75,107,107,2,0,76,76,108,108,2,0,77,77,109,
        109,2,0,78,78,110,110,2,0,79,79,111,111,2,0,80,80,112,112,2,0,81,
        81,113,113,2,0,82,82,114,114,2,0,83,83,115,115,2,0,84,84,116,116,
        2,0,85,85,117,117,2,0,86,86,118,118,2,0,87,87,119,119,2,0,88,88,
        120,120,2,0,89,89,121,121,2,0,90,90,122,122,2,0,10,10,13,13,3,0,
        9,10,13,13,32,32,499,0,1,1,0,0,0,0,3,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,
        0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,
        0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,
        0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,0,0,0,151,
        1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,1,0,0,0,
        0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,0,169,1,
        0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,0,177,1,0,0,0,0,
        179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,0,185,1,0,0,0,0,187,1,0,
        0,0,0,189,1,0,0,0,0,191,1,0,0,0,0,193,1,0,0,0,0,195,1,0,0,0,0,197,
        1,0,0,0,0,199,1,0,0,0,0,201,1,0,0,0,0,203,1,0,0,0,0,205,1,0,0,0,
        0,207,1,0,0,0,1,209,1,0,0,0,3,217,1,0,0,0,5,221,1,0,0,0,7,223,1,
        0,0,0,9,225,1,0,0,0,11,227,1,0,0,0,13,229,1,0,0,0,15,231,1,0,0,0,
        17,233,1,0,0,0,19,235,1,0,0,0,21,237,1,0,0,0,23,239,1,0,0,0,25,241,
        1,0,0,0,27,243,1,0,0,0,29,245,1,0,0,0,31,247,1,0,0,0,33,249,1,0,
        0,0,35,251,1,0,0,0,37,253,1,0,0,0,39,255,1,0,0,0,41,257,1,0,0,0,
        43,259,1,0,0,0,45,261,1,0,0,0,47,263,1,0,0,0,49,265,1,0,0,0,51,267,
        1,0,0,0,53,269,1,0,0,0,55,271,1,0,0,0,57,273,1,0,0,0,59,275,1,0,
        0,0,61,277,1,0,0,0,63,279,1,0,0,0,65,282,1,0,0,0,67,285,1,0,0,0,
        69,288,1,0,0,0,71,291,1,0,0,0,73,294,1,0,0,0,75,297,1,0,0,0,77,300,
        1,0,0,0,79,303,1,0,0,0,81,306,1,0,0,0,83,310,1,0,0,0,85,313,1,0,
        0,0,87,316,1,0,0,0,89,319,1,0,0,0,91,326,1,0,0,0,93,333,1,0,0,0,
        95,339,1,0,0,0,97,342,1,0,0,0,99,345,1,0,0,0,101,348,1,0,0,0,103,
        355,1,0,0,0,105,360,1,0,0,0,107,362,1,0,0,0,109,364,1,0,0,0,111,
        367,1,0,0,0,113,371,1,0,0,0,115,375,1,0,0,0,117,379,1,0,0,0,119,
        382,1,0,0,0,121,386,1,0,0,0,123,391,1,0,0,0,125,395,1,0,0,0,127,
        397,1,0,0,0,129,399,1,0,0,0,131,401,1,0,0,0,133,403,1,0,0,0,135,
        405,1,0,0,0,137,407,1,0,0,0,139,409,1,0,0,0,141,411,1,0,0,0,143,
        413,1,0,0,0,145,415,1,0,0,0,147,417,1,0,0,0,149,419,1,0,0,0,151,
        421,1,0,0,0,153,423,1,0,0,0,155,425,1,0,0,0,157,428,1,0,0,0,159,
        430,1,0,0,0,161,433,1,0,0,0,163,435,1,0,0,0,165,437,1,0,0,0,167,
        439,1,0,0,0,169,442,1,0,0,0,171,445,1,0,0,0,173,448,1,0,0,0,175,
        451,1,0,0,0,177,454,1,0,0,0,179,457,1,0,0,0,181,460,1,0,0,0,183,
        463,1,0,0,0,185,465,1,0,0,0,187,467,1,0,0,0,189,469,1,0,0,0,191,
        471,1,0,0,0,193,475,1,0,0,0,195,479,1,0,0,0,197,483,1,0,0,0,199,
        487,1,0,0,0,201,492,1,0,0,0,203,496,1,0,0,0,205,504,1,0,0,0,207,
        508,1,0,0,0,209,210,5,48,0,0,210,212,3,57,28,0,211,213,3,9,4,0,212,
        211,1,0,0,0,213,214,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,
        2,1,0,0,0,216,218,3,7,3,0,217,216,1,0,0,0,218,219,1,0,0,0,219,217,
        1,0,0,0,219,220,1,0,0,0,220,4,1,0,0,0,221,222,7,0,0,0,222,6,1,0,
        0,0,223,224,2,48,57,0,224,8,1,0,0,0,225,226,7,1,0,0,226,10,1,0,0,
        0,227,228,7,2,0,0,228,12,1,0,0,0,229,230,7,3,0,0,230,14,1,0,0,0,
        231,232,7,4,0,0,232,16,1,0,0,0,233,234,7,5,0,0,234,18,1,0,0,0,235,
        236,7,6,0,0,236,20,1,0,0,0,237,238,7,7,0,0,238,22,1,0,0,0,239,240,
        7,8,0,0,240,24,1,0,0,0,241,242,7,9,0,0,242,26,1,0,0,0,243,244,7,
        10,0,0,244,28,1,0,0,0,245,246,7,11,0,0,246,30,1,0,0,0,247,248,7,
        12,0,0,248,32,1,0,0,0,249,250,7,13,0,0,250,34,1,0,0,0,251,252,7,
        14,0,0,252,36,1,0,0,0,253,254,7,15,0,0,254,38,1,0,0,0,255,256,7,
        16,0,0,256,40,1,0,0,0,257,258,7,17,0,0,258,42,1,0,0,0,259,260,7,
        18,0,0,260,44,1,0,0,0,261,262,7,19,0,0,262,46,1,0,0,0,263,264,7,
        20,0,0,264,48,1,0,0,0,265,266,7,21,0,0,266,50,1,0,0,0,267,268,7,
        22,0,0,268,52,1,0,0,0,269,270,7,23,0,0,270,54,1,0,0,0,271,272,7,
        24,0,0,272,56,1,0,0,0,273,274,7,25,0,0,274,58,1,0,0,0,275,276,7,
        26,0,0,276,60,1,0,0,0,277,278,7,27,0,0,278,62,1,0,0,0,279,280,3,
        45,22,0,280,281,5,48,0,0,281,64,1,0,0,0,282,283,3,45,22,0,283,284,
        5,49,0,0,284,66,1,0,0,0,285,286,3,45,22,0,286,287,5,50,0,0,287,68,
        1,0,0,0,288,289,3,45,22,0,289,290,5,51,0,0,290,70,1,0,0,0,291,292,
        5,36,0,0,292,293,5,48,0,0,293,72,1,0,0,0,294,295,5,36,0,0,295,296,
        5,49,0,0,296,74,1,0,0,0,297,298,5,36,0,0,298,299,5,50,0,0,299,76,
        1,0,0,0,300,301,5,36,0,0,301,302,5,51,0,0,302,78,1,0,0,0,303,304,
        3,53,26,0,304,305,5,49,0,0,305,80,1,0,0,0,306,307,3,53,26,0,307,
        308,5,49,0,0,308,309,3,25,12,0,309,82,1,0,0,0,310,311,3,53,26,0,
        311,312,5,50,0,0,312,84,1,0,0,0,313,314,3,53,26,0,314,315,5,51,0,
        0,315,86,1,0,0,0,316,317,3,53,26,0,317,318,5,52,0,0,318,88,1,0,0,
        0,319,320,3,17,8,0,320,321,3,19,9,0,321,322,3,21,10,0,322,323,3,
        27,13,0,323,324,3,37,18,0,324,325,3,19,9,0,325,90,1,0,0,0,326,327,
        3,15,7,0,327,328,3,39,19,0,328,329,3,37,18,0,329,330,3,21,10,0,330,
        331,3,27,13,0,331,332,3,23,11,0,332,92,1,0,0,0,333,334,3,15,7,0,
        334,335,3,39,19,0,335,336,3,37,18,0,336,337,3,47,23,0,337,338,3,
        49,24,0,338,94,1,0,0,0,339,340,3,11,5,0,340,341,5,49,0,0,341,96,
        1,0,0,0,342,343,3,11,5,0,343,344,5,52,0,0,344,98,1,0,0,0,345,346,
        3,11,5,0,346,347,5,53,0,0,347,100,1,0,0,0,348,349,3,11,5,0,349,350,
        5,49,0,0,350,351,5,50,0,0,351,352,5,56,0,0,352,353,1,0,0,0,353,354,
        3,17,8,0,354,102,1,0,0,0,355,356,3,17,8,0,356,357,3,27,13,0,357,
        358,3,37,18,0,358,359,3,53,26,0,359,104,1,0,0,0,360,361,3,17,8,0,
        361,106,1,0,0,0,362,363,3,15,7,0,363,108,1,0,0,0,364,365,3,27,13,
        0,365,366,3,17,8,0,366,110,1,0,0,0,367,368,3,45,22,0,368,369,3,19,
        9,0,369,370,3,53,26,0,370,112,1,0,0,0,371,372,3,27,13,0,372,373,
        3,37,18,0,373,374,3,53,26,0,374,114,1,0,0,0,375,376,3,11,5,0,376,
        377,3,37,18,0,377,378,3,17,8,0,378,116,1,0,0,0,379,380,3,39,19,0,
        380,381,3,45,22,0,381,118,1,0,0,0,382,383,3,57,28,0,383,384,3,39,
        19,0,384,385,3,45,22,0,385,120,1,0,0,0,386,387,3,37,18,0,387,388,
        3,39,19,0,388,389,3,49,24,0,389,122,1,0,0,0,390,392,7,28,0,0,391,
        390,1,0,0,0,392,393,1,0,0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,
        124,1,0,0,0,395,396,5,40,0,0,396,126,1,0,0,0,397,398,5,41,0,0,398,
        128,1,0,0,0,399,400,5,91,0,0,400,130,1,0,0,0,401,402,5,60,0,0,402,
        132,1,0,0,0,403,404,5,93,0,0,404,134,1,0,0,0,405,406,5,62,0,0,406,
        136,1,0,0,0,407,408,5,123,0,0,408,138,1,0,0,0,409,410,5,125,0,0,
        410,140,1,0,0,0,411,412,5,43,0,0,412,142,1,0,0,0,413,414,5,45,0,
        0,414,144,1,0,0,0,415,416,5,42,0,0,416,146,1,0,0,0,417,418,5,47,
        0,0,418,148,1,0,0,0,419,420,5,37,0,0,420,150,1,0,0,0,421,422,5,94,
        0,0,422,152,1,0,0,0,423,424,5,38,0,0,424,154,1,0,0,0,425,426,5,38,
        0,0,426,427,5,38,0,0,427,156,1,0,0,0,428,429,5,124,0,0,429,158,1,
        0,0,0,430,431,5,124,0,0,431,432,5,124,0,0,432,160,1,0,0,0,433,434,
        5,33,0,0,434,162,1,0,0,0,435,436,5,126,0,0,436,164,1,0,0,0,437,438,
        5,61,0,0,438,166,1,0,0,0,439,440,5,60,0,0,440,441,5,60,0,0,441,168,
        1,0,0,0,442,443,5,62,0,0,443,444,5,62,0,0,444,170,1,0,0,0,445,446,
        5,61,0,0,446,447,5,61,0,0,447,172,1,0,0,0,448,449,5,33,0,0,449,450,
        5,61,0,0,450,174,1,0,0,0,451,452,5,60,0,0,452,453,5,61,0,0,453,176,
        1,0,0,0,454,455,5,62,0,0,455,456,5,61,0,0,456,178,1,0,0,0,457,458,
        5,43,0,0,458,459,5,43,0,0,459,180,1,0,0,0,460,461,5,45,0,0,461,462,
        5,45,0,0,462,182,1,0,0,0,463,464,5,44,0,0,464,184,1,0,0,0,465,466,
        5,58,0,0,466,186,1,0,0,0,467,468,5,59,0,0,468,188,1,0,0,0,469,470,
        5,46,0,0,470,190,1,0,0,0,471,472,3,15,7,0,472,473,3,35,17,0,473,
        474,3,41,20,0,474,192,1,0,0,0,475,476,3,39,19,0,476,477,3,51,25,
        0,477,478,3,49,24,0,478,194,1,0,0,0,479,480,3,23,11,0,480,481,3,
        19,9,0,481,482,3,37,18,0,482,196,1,0,0,0,483,484,3,19,9,0,484,485,
        3,39,19,0,485,486,3,41,20,0,486,198,1,0,0,0,487,488,3,55,27,0,488,
        489,3,11,5,0,489,490,3,27,13,0,490,491,3,49,24,0,491,200,1,0,0,0,
        492,493,3,29,14,0,493,494,3,37,18,0,494,495,3,61,30,0,495,202,1,
        0,0,0,496,501,3,5,2,0,497,500,3,5,2,0,498,500,3,7,3,0,499,497,1,
        0,0,0,499,498,1,0,0,0,500,503,1,0,0,0,501,499,1,0,0,0,501,502,1,
        0,0,0,502,204,1,0,0,0,503,501,1,0,0,0,504,505,7,29,0,0,505,506,1,
        0,0,0,506,507,6,102,0,0,507,206,1,0,0,0,508,512,5,59,0,0,509,511,
        8,28,0,0,510,509,1,0,0,0,511,514,1,0,0,0,512,510,1,0,0,0,512,513,
        1,0,0,0,513,516,1,0,0,0,514,512,1,0,0,0,515,517,5,13,0,0,516,515,
        1,0,0,0,516,517,1,0,0,0,517,518,1,0,0,0,518,519,5,10,0,0,519,520,
        1,0,0,0,520,521,6,103,0,0,521,208,1,0,0,0,8,0,214,219,393,499,501,
        512,516,1,6,0,0
    ]

class ASICLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    HEXADECIMAL = 1
    DECIMAL = 2
    R0 = 3
    R1 = 4
    R2 = 5
    R3 = 6
    ARG0 = 7
    ARG1 = 8
    ARG2 = 9
    ARG3 = 10
    V1 = 11
    V1H = 12
    V2 = 13
    V3 = 14
    V4 = 15
    DEFINE = 16
    CONFIG = 17
    CONST = 18
    A1 = 19
    A4 = 20
    A5 = 21
    A128D = 22
    DINV = 23
    SD = 24
    SC = 25
    ID = 26
    REV = 27
    INV = 28
    AND = 29
    OR = 30
    XOR = 31
    NOT = 32
    EOL = 33
    LPAREN = 34
    RPAREN = 35
    LBRACKET = 36
    LABRACKET = 37
    RBRACKET = 38
    RABRACKET = 39
    LBRACE = 40
    RBRACE = 41
    PLUS = 42
    MINUS = 43
    STAR = 44
    DIV = 45
    MOD = 46
    CARET = 47
    AMP = 48
    AMPAMP = 49
    BAR = 50
    BARBAR = 51
    NEG = 52
    TILDE = 53
    ASSIGN = 54
    LSHIFT = 55
    RSHIFT = 56
    EQUAL = 57
    NEQUAL = 58
    LEQUAL = 59
    GEQUAL = 60
    PLUSPLUS = 61
    MINUSMINUS = 62
    COMMA = 63
    COLON = 64
    SEMI = 65
    DOT = 66
    CMP = 67
    OUT = 68
    GEN = 69
    EOP = 70
    WAIT = 71
    JNZ = 72
    IDENTIFIER = 73
    WS = 74
    LINE_COMMENT = 75

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'$0'", "'$1'", "'$2'", "'$3'", "'('", "')'", "'['", "'<'", 
            "']'", "'>'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'^'", "'&'", "'&&'", "'|'", "'||'", "'!'", "'~'", "'='", "'<<'", 
            "'>>'", "'=='", "'!='", "'<='", "'>='", "'++'", "'--'", "','", 
            "':'", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "HEXADECIMAL", "DECIMAL", "R0", "R1", "R2", "R3", "ARG0", "ARG1", 
            "ARG2", "ARG3", "V1", "V1H", "V2", "V3", "V4", "DEFINE", "CONFIG", 
            "CONST", "A1", "A4", "A5", "A128D", "DINV", "SD", "SC", "ID", 
            "REV", "INV", "AND", "OR", "XOR", "NOT", "EOL", "LPAREN", "RPAREN", 
            "LBRACKET", "LABRACKET", "RBRACKET", "RABRACKET", "LBRACE", 
            "RBRACE", "PLUS", "MINUS", "STAR", "DIV", "MOD", "CARET", "AMP", 
            "AMPAMP", "BAR", "BARBAR", "NEG", "TILDE", "ASSIGN", "LSHIFT", 
            "RSHIFT", "EQUAL", "NEQUAL", "LEQUAL", "GEQUAL", "PLUSPLUS", 
            "MINUSMINUS", "COMMA", "COLON", "SEMI", "DOT", "CMP", "OUT", 
            "GEN", "EOP", "WAIT", "JNZ", "IDENTIFIER", "WS", "LINE_COMMENT" ]

    ruleNames = [ "HEXADECIMAL", "DECIMAL", "Letter", "Digit", "HexDigit", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "R0", "R1", "R2", "R3", "ARG0", "ARG1", 
                  "ARG2", "ARG3", "V1", "V1H", "V2", "V3", "V4", "DEFINE", 
                  "CONFIG", "CONST", "A1", "A4", "A5", "A128D", "DINV", 
                  "SD", "SC", "ID", "REV", "INV", "AND", "OR", "XOR", "NOT", 
                  "EOL", "LPAREN", "RPAREN", "LBRACKET", "LABRACKET", "RBRACKET", 
                  "RABRACKET", "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", 
                  "DIV", "MOD", "CARET", "AMP", "AMPAMP", "BAR", "BARBAR", 
                  "NEG", "TILDE", "ASSIGN", "LSHIFT", "RSHIFT", "EQUAL", 
                  "NEQUAL", "LEQUAL", "GEQUAL", "PLUSPLUS", "MINUSMINUS", 
                  "COMMA", "COLON", "SEMI", "DOT", "CMP", "OUT", "GEN", 
                  "EOP", "WAIT", "JNZ", "IDENTIFIER", "WS", "LINE_COMMENT" ]

    grammarFileName = "ASICLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


