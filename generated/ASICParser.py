# Generated from grammar/ASICParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,83,465,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,1,0,5,0,124,8,0,10,0,12,0,127,9,0,1,1,1,1,1,1,1,1,
        3,1,133,8,1,1,1,3,1,136,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,4,1,4,1,4,3,4,150,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,160,
        8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,3,9,169,8,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,182,8,9,1,9,3,9,185,8,9,1,10,1,10,3,
        10,189,8,10,1,11,1,11,3,11,193,8,11,1,12,1,12,1,12,1,12,3,12,199,
        8,12,1,13,1,13,1,13,1,13,1,13,3,13,206,8,13,1,14,1,14,1,14,1,14,
        3,14,212,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,222,8,
        14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,239,8,18,1,19,1,19,1,19,1,19,3,19,245,8,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,1,22,5,22,255,8,22,10,22,12,22,258,
        9,22,1,23,1,23,1,24,1,24,1,24,1,24,5,24,266,8,24,10,24,12,24,269,
        9,24,1,25,1,25,1,26,1,26,1,26,1,26,5,26,277,8,26,10,26,12,26,280,
        9,26,1,27,1,27,1,28,1,28,1,28,1,28,5,28,288,8,28,10,28,12,28,291,
        9,28,1,29,1,29,1,29,5,29,296,8,29,10,29,12,29,299,9,29,1,30,1,30,
        1,30,5,30,304,8,30,10,30,12,30,307,9,30,1,31,1,31,1,31,5,31,312,
        8,31,10,31,12,31,315,9,31,1,32,1,32,1,32,5,32,320,8,32,10,32,12,
        32,323,9,32,1,33,1,33,1,33,5,33,328,8,33,10,33,12,33,331,9,33,1,
        34,1,34,3,34,335,8,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,5,
        36,345,8,36,10,36,12,36,348,9,36,1,37,1,37,3,37,352,8,37,1,38,1,
        38,3,38,356,8,38,1,38,1,38,1,38,1,38,3,38,362,8,38,1,38,1,38,3,38,
        366,8,38,1,39,1,39,3,39,370,8,39,1,40,1,40,1,40,1,40,3,40,376,8,
        40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,3,42,385,8,42,1,42,3,42,388,
        8,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,1,47,
        3,47,402,8,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,4,48,411,8,48,11,
        48,12,48,412,1,48,1,48,3,48,417,8,48,1,49,1,49,1,50,1,50,1,51,1,
        51,1,52,1,52,1,53,1,53,1,53,1,53,1,53,3,53,432,8,53,1,54,1,54,1,
        55,1,55,1,55,1,55,3,55,440,8,55,1,56,1,56,1,57,1,57,1,58,1,58,1,
        58,1,58,1,58,1,58,1,58,1,58,3,58,454,8,58,1,59,1,59,1,59,1,59,1,
        59,1,59,1,59,1,60,1,60,1,60,0,0,61,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        108,110,112,114,116,118,120,0,14,1,0,1,4,2,0,45,46,55,56,1,0,47,
        49,1,0,45,46,3,0,40,40,42,42,62,63,1,0,60,61,1,0,45,48,1,0,5,8,1,
        0,9,12,1,0,13,17,2,0,13,13,15,17,1,0,71,72,1,0,22,27,2,0,29,29,31,
        35,457,0,125,1,0,0,0,2,132,1,0,0,0,4,137,1,0,0,0,6,144,1,0,0,0,8,
        149,1,0,0,0,10,151,1,0,0,0,12,155,1,0,0,0,14,161,1,0,0,0,16,165,
        1,0,0,0,18,184,1,0,0,0,20,188,1,0,0,0,22,192,1,0,0,0,24,194,1,0,
        0,0,26,205,1,0,0,0,28,221,1,0,0,0,30,223,1,0,0,0,32,227,1,0,0,0,
        34,230,1,0,0,0,36,238,1,0,0,0,38,244,1,0,0,0,40,246,1,0,0,0,42,248,
        1,0,0,0,44,250,1,0,0,0,46,259,1,0,0,0,48,261,1,0,0,0,50,270,1,0,
        0,0,52,272,1,0,0,0,54,281,1,0,0,0,56,283,1,0,0,0,58,292,1,0,0,0,
        60,300,1,0,0,0,62,308,1,0,0,0,64,316,1,0,0,0,66,324,1,0,0,0,68,334,
        1,0,0,0,70,336,1,0,0,0,72,341,1,0,0,0,74,351,1,0,0,0,76,355,1,0,
        0,0,78,369,1,0,0,0,80,371,1,0,0,0,82,379,1,0,0,0,84,382,1,0,0,0,
        86,389,1,0,0,0,88,391,1,0,0,0,90,393,1,0,0,0,92,395,1,0,0,0,94,397,
        1,0,0,0,96,416,1,0,0,0,98,418,1,0,0,0,100,420,1,0,0,0,102,422,1,
        0,0,0,104,424,1,0,0,0,106,431,1,0,0,0,108,433,1,0,0,0,110,439,1,
        0,0,0,112,441,1,0,0,0,114,443,1,0,0,0,116,453,1,0,0,0,118,455,1,
        0,0,0,120,462,1,0,0,0,122,124,3,2,1,0,123,122,1,0,0,0,124,127,1,
        0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,1,1,0,0,0,127,125,1,0,
        0,0,128,133,3,8,4,0,129,133,3,18,9,0,130,133,3,4,2,0,131,133,3,6,
        3,0,132,128,1,0,0,0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,
        0,0,133,135,1,0,0,0,134,136,3,120,60,0,135,134,1,0,0,0,135,136,1,
        0,0,0,136,3,1,0,0,0,137,138,5,73,0,0,138,139,5,37,0,0,139,140,3,
        98,49,0,140,141,5,66,0,0,141,142,3,16,8,0,142,143,5,38,0,0,143,5,
        1,0,0,0,144,145,5,74,0,0,145,7,1,0,0,0,146,150,3,10,5,0,147,150,
        3,12,6,0,148,150,3,14,7,0,149,146,1,0,0,0,149,147,1,0,0,0,149,148,
        1,0,0,0,150,9,1,0,0,0,151,152,5,19,0,0,152,153,3,88,44,0,153,154,
        3,68,34,0,154,11,1,0,0,0,155,156,5,20,0,0,156,159,3,90,45,0,157,
        160,3,72,36,0,158,160,3,70,35,0,159,157,1,0,0,0,159,158,1,0,0,0,
        160,13,1,0,0,0,161,162,5,21,0,0,162,163,3,92,46,0,163,164,3,84,42,
        0,164,15,1,0,0,0,165,166,7,0,0,0,166,17,1,0,0,0,167,169,3,32,16,
        0,168,167,1,0,0,0,168,169,1,0,0,0,169,181,1,0,0,0,170,182,3,20,10,
        0,171,172,3,20,10,0,172,173,5,66,0,0,173,174,3,20,10,0,174,182,1,
        0,0,0,175,176,3,20,10,0,176,177,5,66,0,0,177,178,3,20,10,0,178,179,
        5,66,0,0,179,180,3,20,10,0,180,182,1,0,0,0,181,170,1,0,0,0,181,171,
        1,0,0,0,181,175,1,0,0,0,182,185,1,0,0,0,183,185,3,32,16,0,184,168,
        1,0,0,0,184,183,1,0,0,0,185,19,1,0,0,0,186,189,3,22,11,0,187,189,
        3,28,14,0,188,186,1,0,0,0,188,187,1,0,0,0,189,21,1,0,0,0,190,193,
        3,24,12,0,191,193,3,26,13,0,192,190,1,0,0,0,192,191,1,0,0,0,193,
        23,1,0,0,0,194,195,3,98,49,0,195,198,5,57,0,0,196,199,3,68,34,0,
        197,199,3,100,50,0,198,196,1,0,0,0,198,197,1,0,0,0,199,25,1,0,0,
        0,200,201,5,5,0,0,201,206,5,64,0,0,202,203,3,98,49,0,203,204,5,65,
        0,0,204,206,1,0,0,0,205,200,1,0,0,0,205,202,1,0,0,0,206,27,1,0,0,
        0,207,208,3,96,48,0,208,211,5,57,0,0,209,212,3,114,57,0,210,212,
        3,112,56,0,211,209,1,0,0,0,211,210,1,0,0,0,212,213,1,0,0,0,213,214,
        3,94,47,0,214,222,1,0,0,0,215,216,3,96,48,0,216,217,5,57,0,0,217,
        218,3,116,58,0,218,222,1,0,0,0,219,222,3,116,58,0,220,222,3,30,15,
        0,221,207,1,0,0,0,221,215,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,
        0,222,29,1,0,0,0,223,224,5,76,0,0,224,225,5,57,0,0,225,226,5,17,
        0,0,226,31,1,0,0,0,227,228,3,34,17,0,228,229,5,67,0,0,229,33,1,0,
        0,0,230,231,5,81,0,0,231,35,1,0,0,0,232,239,3,16,8,0,233,239,3,88,
        44,0,234,235,5,37,0,0,235,236,3,68,34,0,236,237,5,38,0,0,237,239,
        1,0,0,0,238,232,1,0,0,0,238,233,1,0,0,0,238,234,1,0,0,0,239,37,1,
        0,0,0,240,245,3,36,18,0,241,242,3,40,20,0,242,243,3,38,19,0,243,
        245,1,0,0,0,244,240,1,0,0,0,244,241,1,0,0,0,245,39,1,0,0,0,246,247,
        7,1,0,0,247,41,1,0,0,0,248,249,7,2,0,0,249,43,1,0,0,0,250,256,3,
        38,19,0,251,252,3,42,21,0,252,253,3,38,19,0,253,255,1,0,0,0,254,
        251,1,0,0,0,255,258,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,
        45,1,0,0,0,258,256,1,0,0,0,259,260,7,3,0,0,260,47,1,0,0,0,261,267,
        3,44,22,0,262,263,3,46,23,0,263,264,3,44,22,0,264,266,1,0,0,0,265,
        262,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,
        49,1,0,0,0,269,267,1,0,0,0,270,271,7,4,0,0,271,51,1,0,0,0,272,278,
        3,48,24,0,273,274,3,50,25,0,274,275,3,48,24,0,275,277,1,0,0,0,276,
        273,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,
        53,1,0,0,0,280,278,1,0,0,0,281,282,7,5,0,0,282,55,1,0,0,0,283,289,
        3,52,26,0,284,285,3,54,27,0,285,286,3,52,26,0,286,288,1,0,0,0,287,
        284,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,
        57,1,0,0,0,291,289,1,0,0,0,292,297,3,56,28,0,293,294,5,51,0,0,294,
        296,3,56,28,0,295,293,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,
        298,1,0,0,0,298,59,1,0,0,0,299,297,1,0,0,0,300,305,3,58,29,0,301,
        302,5,50,0,0,302,304,3,58,29,0,303,301,1,0,0,0,304,307,1,0,0,0,305,
        303,1,0,0,0,305,306,1,0,0,0,306,61,1,0,0,0,307,305,1,0,0,0,308,313,
        3,60,30,0,309,310,5,53,0,0,310,312,3,60,30,0,311,309,1,0,0,0,312,
        315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,63,1,0,0,0,315,313,
        1,0,0,0,316,321,3,62,31,0,317,318,5,52,0,0,318,320,3,62,31,0,319,
        317,1,0,0,0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,
        65,1,0,0,0,323,321,1,0,0,0,324,329,3,64,32,0,325,326,5,54,0,0,326,
        328,3,64,32,0,327,325,1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,329,
        330,1,0,0,0,330,67,1,0,0,0,331,329,1,0,0,0,332,335,3,16,8,0,333,
        335,3,66,33,0,334,332,1,0,0,0,334,333,1,0,0,0,335,69,1,0,0,0,336,
        337,5,30,0,0,337,338,5,37,0,0,338,339,3,72,36,0,339,340,5,38,0,0,
        340,71,1,0,0,0,341,346,3,74,37,0,342,343,5,45,0,0,343,345,3,74,37,
        0,344,342,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,
        0,347,73,1,0,0,0,348,346,1,0,0,0,349,352,3,76,38,0,350,352,3,78,
        39,0,351,349,1,0,0,0,351,350,1,0,0,0,352,75,1,0,0,0,353,356,3,102,
        51,0,354,356,3,106,53,0,355,353,1,0,0,0,355,354,1,0,0,0,356,361,
        1,0,0,0,357,358,5,43,0,0,358,359,3,68,34,0,359,360,5,44,0,0,360,
        362,1,0,0,0,361,357,1,0,0,0,361,362,1,0,0,0,362,365,1,0,0,0,363,
        364,5,58,0,0,364,366,3,68,34,0,365,363,1,0,0,0,365,366,1,0,0,0,366,
        77,1,0,0,0,367,370,3,92,46,0,368,370,3,84,42,0,369,367,1,0,0,0,369,
        368,1,0,0,0,370,79,1,0,0,0,371,375,5,39,0,0,372,376,3,68,34,0,373,
        376,3,104,52,0,374,376,3,98,49,0,375,372,1,0,0,0,375,373,1,0,0,0,
        375,374,1,0,0,0,376,377,1,0,0,0,377,378,5,41,0,0,378,81,1,0,0,0,
        379,380,5,58,0,0,380,381,3,68,34,0,381,83,1,0,0,0,382,384,5,28,0,
        0,383,385,3,80,40,0,384,383,1,0,0,0,384,385,1,0,0,0,385,387,1,0,
        0,0,386,388,3,82,41,0,387,386,1,0,0,0,387,388,1,0,0,0,388,85,1,0,
        0,0,389,390,7,6,0,0,390,87,1,0,0,0,391,392,5,81,0,0,392,89,1,0,0,
        0,393,394,5,81,0,0,394,91,1,0,0,0,395,396,5,81,0,0,396,93,1,0,0,
        0,397,401,5,37,0,0,398,402,3,90,45,0,399,402,3,72,36,0,400,402,3,
        70,35,0,401,398,1,0,0,0,401,399,1,0,0,0,401,400,1,0,0,0,402,403,
        1,0,0,0,403,404,5,38,0,0,404,95,1,0,0,0,405,417,3,110,55,0,406,407,
        5,37,0,0,407,410,3,110,55,0,408,409,5,66,0,0,409,411,3,110,55,0,
        410,408,1,0,0,0,411,412,1,0,0,0,412,410,1,0,0,0,412,413,1,0,0,0,
        413,414,1,0,0,0,414,415,5,38,0,0,415,417,1,0,0,0,416,405,1,0,0,0,
        416,406,1,0,0,0,417,97,1,0,0,0,418,419,7,7,0,0,419,99,1,0,0,0,420,
        421,7,8,0,0,421,101,1,0,0,0,422,423,7,9,0,0,423,103,1,0,0,0,424,
        425,7,10,0,0,425,105,1,0,0,0,426,432,5,5,0,0,427,428,5,30,0,0,428,
        429,5,37,0,0,429,430,5,5,0,0,430,432,5,38,0,0,431,426,1,0,0,0,431,
        427,1,0,0,0,432,107,1,0,0,0,433,434,7,11,0,0,434,109,1,0,0,0,435,
        440,3,102,51,0,436,440,3,108,54,0,437,440,5,75,0,0,438,440,5,76,
        0,0,439,435,1,0,0,0,439,436,1,0,0,0,439,437,1,0,0,0,439,438,1,0,
        0,0,440,111,1,0,0,0,441,442,7,12,0,0,442,113,1,0,0,0,443,444,7,13,
        0,0,444,115,1,0,0,0,445,454,5,77,0,0,446,454,5,78,0,0,447,448,5,
        79,0,0,448,449,5,37,0,0,449,450,3,68,34,0,450,451,5,38,0,0,451,454,
        1,0,0,0,452,454,3,118,59,0,453,445,1,0,0,0,453,446,1,0,0,0,453,447,
        1,0,0,0,453,452,1,0,0,0,454,117,1,0,0,0,455,456,5,80,0,0,456,457,
        5,37,0,0,457,458,3,98,49,0,458,459,5,66,0,0,459,460,3,34,17,0,460,
        461,5,38,0,0,461,119,1,0,0,0,462,463,5,83,0,0,463,121,1,0,0,0,41,
        125,132,135,149,159,168,181,184,188,192,198,205,211,221,238,244,
        256,267,278,289,297,305,313,321,329,334,346,351,355,361,365,369,
        375,384,387,401,412,416,431,439,453
    ]

class ASICParser ( Parser ):

    grammarFileName = "ASICParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'$0'", "'$1'", "'$2'", "'$3'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "'<'", "']'", "'>'", "'{'", "'}'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'", "'&'", "'&&'", "'|'", "'||'", 
                     "'!'", "'~'", "'='", "'<<'", "'>>'", "'=='", "'!='", 
                     "'<='", "'>='", "'++'", "'--'", "','", "':'", "';'", 
                     "'.'", "'#'" ]

    symbolicNames = [ "<INVALID>", "HEXADECIMAL", "DECIMAL", "BINARY", "OCTAL", 
                      "R0", "R1", "R2", "R3", "ARG0", "ARG1", "ARG2", "ARG3", 
                      "V1", "V1H", "V2", "V3", "V4", "PROCCHAR", "DEFINE", 
                      "CONFIG", "CONST", "A1", "A4", "A5", "A128D", "DINV", 
                      "SD", "SC", "ID", "REV", "INV", "AND", "OR", "XOR", 
                      "NOT", "EOL", "LPAREN", "RPAREN", "LBRACKET", "LABRACKET", 
                      "RBRACKET", "RABRACKET", "LBRACE", "RBRACE", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "CARET", "AMP", "AMPAMP", 
                      "BAR", "BARBAR", "NEG", "TILDE", "ASSIGN", "LSHIFT", 
                      "RSHIFT", "EQUAL", "NEQUAL", "LEQUAL", "GEQUAL", "PLUSPLUS", 
                      "MINUSMINUS", "COMMA", "COLON", "SEMI", "DOT", "HASH", 
                      "V2N", "V4M", "FOR", "ENDFOR", "CMP", "OUT", "GEN", 
                      "EOP", "WAIT", "JNZ", "IDENTIFIER", "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_forloop = 2
    RULE_endfor = 3
    RULE_definition = 4
    RULE_define_def = 5
    RULE_config_def = 6
    RULE_const_def = 7
    RULE_constant = 8
    RULE_statement = 9
    RULE_instruction = 10
    RULE_sregop = 11
    RULE_asignment = 12
    RULE_arith = 13
    RULE_operator = 14
    RULE_resultout = 15
    RULE_lbl = 16
    RULE_label = 17
    RULE_primary_expression = 18
    RULE_unary_expression = 19
    RULE_unary_operator = 20
    RULE_mulop = 21
    RULE_multiplicative_expression = 22
    RULE_addop = 23
    RULE_additive_expression = 24
    RULE_relop = 25
    RULE_relational_expression = 26
    RULE_eqop = 27
    RULE_equality_expression = 28
    RULE_and_expression = 29
    RULE_xor_expression = 30
    RULE_or_expression = 31
    RULE_logicaland_expression = 32
    RULE_logicalor_expression = 33
    RULE_expression = 34
    RULE_rev_configuration = 35
    RULE_configuration = 36
    RULE_conf_atom = 37
    RULE_conf_d = 38
    RULE_conf_c = 39
    RULE_const_addr = 40
    RULE_const_shift = 41
    RULE_const_expr = 42
    RULE_op = 43
    RULE_define_name = 44
    RULE_config_name = 45
    RULE_const_name = 46
    RULE_argument = 47
    RULE_resultexpr = 48
    RULE_sreg = 49
    RULE_arg = 50
    RULE_vreg = 51
    RULE_vreg_d = 52
    RULE_vreg_r = 53
    RULE_vreg_special = 54
    RULE_output = 55
    RULE_stdop = 56
    RULE_aluop = 57
    RULE_spcop = 58
    RULE_jump = 59
    RULE_comment = 60

    ruleNames =  [ "prog", "line", "forloop", "endfor", "definition", "define_def", 
                   "config_def", "const_def", "constant", "statement", "instruction", 
                   "sregop", "asignment", "arith", "operator", "resultout", 
                   "lbl", "label", "primary_expression", "unary_expression", 
                   "unary_operator", "mulop", "multiplicative_expression", 
                   "addop", "additive_expression", "relop", "relational_expression", 
                   "eqop", "equality_expression", "and_expression", "xor_expression", 
                   "or_expression", "logicaland_expression", "logicalor_expression", 
                   "expression", "rev_configuration", "configuration", "conf_atom", 
                   "conf_d", "conf_c", "const_addr", "const_shift", "const_expr", 
                   "op", "define_name", "config_name", "const_name", "argument", 
                   "resultexpr", "sreg", "arg", "vreg", "vreg_d", "vreg_r", 
                   "vreg_special", "output", "stdop", "aluop", "spcop", 
                   "jump", "comment" ]

    EOF = Token.EOF
    HEXADECIMAL=1
    DECIMAL=2
    BINARY=3
    OCTAL=4
    R0=5
    R1=6
    R2=7
    R3=8
    ARG0=9
    ARG1=10
    ARG2=11
    ARG3=12
    V1=13
    V1H=14
    V2=15
    V3=16
    V4=17
    PROCCHAR=18
    DEFINE=19
    CONFIG=20
    CONST=21
    A1=22
    A4=23
    A5=24
    A128D=25
    DINV=26
    SD=27
    SC=28
    ID=29
    REV=30
    INV=31
    AND=32
    OR=33
    XOR=34
    NOT=35
    EOL=36
    LPAREN=37
    RPAREN=38
    LBRACKET=39
    LABRACKET=40
    RBRACKET=41
    RABRACKET=42
    LBRACE=43
    RBRACE=44
    PLUS=45
    MINUS=46
    STAR=47
    DIV=48
    MOD=49
    CARET=50
    AMP=51
    AMPAMP=52
    BAR=53
    BARBAR=54
    NEG=55
    TILDE=56
    ASSIGN=57
    LSHIFT=58
    RSHIFT=59
    EQUAL=60
    NEQUAL=61
    LEQUAL=62
    GEQUAL=63
    PLUSPLUS=64
    MINUSMINUS=65
    COMMA=66
    COLON=67
    SEMI=68
    DOT=69
    HASH=70
    V2N=71
    V4M=72
    FOR=73
    ENDFOR=74
    CMP=75
    OUT=76
    GEN=77
    EOP=78
    WAIT=79
    JNZ=80
    IDENTIFIER=81
    WS=82
    LINE_COMMENT=83

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.LineContext)
            else:
                return self.getTypedRuleContext(ASICParser.LineContext,i)


        def getRuleIndex(self):
            return ASICParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ASICParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137442877920) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 2047) != 0):
                self.state = 122
                self.line()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition(self):
            return self.getTypedRuleContext(ASICParser.DefinitionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ASICParser.StatementContext,0)


        def forloop(self):
            return self.getTypedRuleContext(ASICParser.ForloopContext,0)


        def endfor(self):
            return self.getTypedRuleContext(ASICParser.EndforContext,0)


        def comment(self):
            return self.getTypedRuleContext(ASICParser.CommentContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ASICParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21]:
                self.state = 128
                self.definition()
                pass
            elif token in [5, 6, 7, 8, 13, 14, 15, 16, 17, 37, 71, 72, 75, 76, 77, 78, 79, 80, 81]:
                self.state = 129
                self.statement()
                pass
            elif token in [73]:
                self.state = 130
                self.forloop()
                pass
            elif token in [74]:
                self.state = 131
                self.endfor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==83:
                self.state = 134
                self.comment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForloopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ASICParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def COMMA(self):
            return self.getToken(ASICParser.COMMA, 0)

        def constant(self):
            return self.getTypedRuleContext(ASICParser.ConstantContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_forloop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForloop" ):
                listener.enterForloop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForloop" ):
                listener.exitForloop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop" ):
                return visitor.visitForloop(self)
            else:
                return visitor.visitChildren(self)




    def forloop(self):

        localctx = ASICParser.ForloopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forloop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(ASICParser.FOR)
            self.state = 138
            self.match(ASICParser.LPAREN)
            self.state = 139
            self.sreg()
            self.state = 140
            self.match(ASICParser.COMMA)
            self.state = 141
            self.constant()
            self.state = 142
            self.match(ASICParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDFOR(self):
            return self.getToken(ASICParser.ENDFOR, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_endfor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndfor" ):
                listener.enterEndfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndfor" ):
                listener.exitEndfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndfor" ):
                return visitor.visitEndfor(self)
            else:
                return visitor.visitChildren(self)




    def endfor(self):

        localctx = ASICParser.EndforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endfor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ASICParser.ENDFOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_def(self):
            return self.getTypedRuleContext(ASICParser.Define_defContext,0)


        def config_def(self):
            return self.getTypedRuleContext(ASICParser.Config_defContext,0)


        def const_def(self):
            return self.getTypedRuleContext(ASICParser.Const_defContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinition" ):
                listener.enterDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinition" ):
                listener.exitDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition" ):
                return visitor.visitDefinition(self)
            else:
                return visitor.visitChildren(self)




    def definition(self):

        localctx = ASICParser.DefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definition)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.define_def()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.config_def()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.const_def()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(ASICParser.DEFINE, 0)

        def define_name(self):
            return self.getTypedRuleContext(ASICParser.Define_nameContext,0)


        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_define_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_def" ):
                listener.enterDefine_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_def" ):
                listener.exitDefine_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_def" ):
                return visitor.visitDefine_def(self)
            else:
                return visitor.visitChildren(self)




    def define_def(self):

        localctx = ASICParser.Define_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_define_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ASICParser.DEFINE)
            self.state = 152
            self.define_name()
            self.state = 153
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIG(self):
            return self.getToken(ASICParser.CONFIG, 0)

        def config_name(self):
            return self.getTypedRuleContext(ASICParser.Config_nameContext,0)


        def configuration(self):
            return self.getTypedRuleContext(ASICParser.ConfigurationContext,0)


        def rev_configuration(self):
            return self.getTypedRuleContext(ASICParser.Rev_configurationContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_config_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig_def" ):
                listener.enterConfig_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig_def" ):
                listener.exitConfig_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_def" ):
                return visitor.visitConfig_def(self)
            else:
                return visitor.visitChildren(self)




    def config_def(self):

        localctx = ASICParser.Config_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_config_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ASICParser.CONFIG)
            self.state = 156
            self.config_name()
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 157
                self.configuration()
                pass

            elif la_ == 2:
                self.state = 158
                self.rev_configuration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(ASICParser.CONST, 0)

        def const_name(self):
            return self.getTypedRuleContext(ASICParser.Const_nameContext,0)


        def const_expr(self):
            return self.getTypedRuleContext(ASICParser.Const_exprContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_const_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_def" ):
                listener.enterConst_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_def" ):
                listener.exitConst_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_def" ):
                return visitor.visitConst_def(self)
            else:
                return visitor.visitChildren(self)




    def const_def(self):

        localctx = ASICParser.Const_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_const_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ASICParser.CONST)
            self.state = 162
            self.const_name()
            self.state = 163
            self.const_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEXADECIMAL(self):
            return self.getToken(ASICParser.HEXADECIMAL, 0)

        def DECIMAL(self):
            return self.getToken(ASICParser.DECIMAL, 0)

        def BINARY(self):
            return self.getToken(ASICParser.BINARY, 0)

        def OCTAL(self):
            return self.getToken(ASICParser.OCTAL, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = ASICParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.InstructionContext)
            else:
                return self.getTypedRuleContext(ASICParser.InstructionContext,i)


        def lbl(self):
            return self.getTypedRuleContext(ASICParser.LblContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.COMMA)
            else:
                return self.getToken(ASICParser.COMMA, i)

        def getRuleIndex(self):
            return ASICParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ASICParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 167
                    self.lbl()


                self.state = 181
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.instruction()
                    pass

                elif la_ == 2:
                    self.state = 171
                    self.instruction()
                    self.state = 172
                    self.match(ASICParser.COMMA)
                    self.state = 173
                    self.instruction()
                    pass

                elif la_ == 3:
                    self.state = 175
                    self.instruction()
                    self.state = 176
                    self.match(ASICParser.COMMA)
                    self.state = 177
                    self.instruction()
                    self.state = 178
                    self.match(ASICParser.COMMA)
                    self.state = 179
                    self.instruction()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.lbl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sregop(self):
            return self.getTypedRuleContext(ASICParser.SregopContext,0)


        def operator(self):
            return self.getTypedRuleContext(ASICParser.OperatorContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = ASICParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instruction)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.sregop()
                pass
            elif token in [13, 14, 15, 16, 17, 37, 71, 72, 75, 76, 77, 78, 79, 80]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.operator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SregopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignment(self):
            return self.getTypedRuleContext(ASICParser.AsignmentContext,0)


        def arith(self):
            return self.getTypedRuleContext(ASICParser.ArithContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_sregop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSregop" ):
                listener.enterSregop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSregop" ):
                listener.exitSregop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSregop" ):
                return visitor.visitSregop(self)
            else:
                return visitor.visitChildren(self)




    def sregop(self):

        localctx = ASICParser.SregopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sregop)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.asignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.arith()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def ASSIGN(self):
            return self.getToken(ASICParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def arg(self):
            return self.getTypedRuleContext(ASICParser.ArgContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_asignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignment" ):
                listener.enterAsignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignment" ):
                listener.exitAsignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignment" ):
                return visitor.visitAsignment(self)
            else:
                return visitor.visitChildren(self)




    def asignment(self):

        localctx = ASICParser.AsignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_asignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.sreg()
            self.state = 195
            self.match(ASICParser.ASSIGN)
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 37, 45, 46, 55, 56, 81]:
                self.state = 196
                self.expression()
                pass
            elif token in [9, 10, 11, 12]:
                self.state = 197
                self.arg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def R0(self):
            return self.getToken(ASICParser.R0, 0)

        def PLUSPLUS(self):
            return self.getToken(ASICParser.PLUSPLUS, 0)

        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def MINUSMINUS(self):
            return self.getToken(ASICParser.MINUSMINUS, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_arith

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith" ):
                listener.enterArith(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith" ):
                listener.exitArith(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith" ):
                return visitor.visitArith(self)
            else:
                return visitor.visitChildren(self)




    def arith(self):

        localctx = ASICParser.ArithContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arith)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(ASICParser.R0)
                self.state = 201
                self.match(ASICParser.PLUSPLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.sreg()
                self.state = 203
                self.match(ASICParser.MINUSMINUS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ASICParser.RULE_operator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AluSpOpContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resultexpr(self):
            return self.getTypedRuleContext(ASICParser.ResultexprContext,0)

        def ASSIGN(self):
            return self.getToken(ASICParser.ASSIGN, 0)
        def argument(self):
            return self.getTypedRuleContext(ASICParser.ArgumentContext,0)

        def aluop(self):
            return self.getTypedRuleContext(ASICParser.AluopContext,0)

        def stdop(self):
            return self.getTypedRuleContext(ASICParser.StdopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAluSpOp" ):
                listener.enterAluSpOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAluSpOp" ):
                listener.exitAluSpOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAluSpOp" ):
                return visitor.visitAluSpOp(self)
            else:
                return visitor.visitChildren(self)


    class SpCopOpContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resultexpr(self):
            return self.getTypedRuleContext(ASICParser.ResultexprContext,0)

        def ASSIGN(self):
            return self.getToken(ASICParser.ASSIGN, 0)
        def spcop(self):
            return self.getTypedRuleContext(ASICParser.SpcopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpCopOp" ):
                listener.enterSpCopOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpCopOp" ):
                listener.exitSpCopOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpCopOp" ):
                return visitor.visitSpCopOp(self)
            else:
                return visitor.visitChildren(self)


    class SpCopOnlyContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def spcop(self):
            return self.getTypedRuleContext(ASICParser.SpcopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpCopOnly" ):
                listener.enterSpCopOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpCopOnly" ):
                listener.exitSpCopOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpCopOnly" ):
                return visitor.visitSpCopOnly(self)
            else:
                return visitor.visitChildren(self)


    class OutOpContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resultout(self):
            return self.getTypedRuleContext(ASICParser.ResultoutContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutOp" ):
                listener.enterOutOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutOp" ):
                listener.exitOutOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutOp" ):
                return visitor.visitOutOp(self)
            else:
                return visitor.visitChildren(self)



    def operator(self):

        localctx = ASICParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operator)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ASICParser.AluSpOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.resultexpr()
                self.state = 208
                self.match(ASICParser.ASSIGN)
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [29, 31, 32, 33, 34, 35]:
                    self.state = 209
                    self.aluop()
                    pass
                elif token in [22, 23, 24, 25, 26, 27]:
                    self.state = 210
                    self.stdop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self.argument()
                pass

            elif la_ == 2:
                localctx = ASICParser.SpCopOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.resultexpr()
                self.state = 216
                self.match(ASICParser.ASSIGN)
                self.state = 217
                self.spcop()
                pass

            elif la_ == 3:
                localctx = ASICParser.SpCopOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.spcop()
                pass

            elif la_ == 4:
                localctx = ASICParser.OutOpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 220
                self.resultout()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultoutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUT(self):
            return self.getToken(ASICParser.OUT, 0)

        def ASSIGN(self):
            return self.getToken(ASICParser.ASSIGN, 0)

        def V4(self):
            return self.getToken(ASICParser.V4, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_resultout

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResultout" ):
                listener.enterResultout(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResultout" ):
                listener.exitResultout(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResultout" ):
                return visitor.visitResultout(self)
            else:
                return visitor.visitChildren(self)




    def resultout(self):

        localctx = ASICParser.ResultoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_resultout)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ASICParser.OUT)
            self.state = 224
            self.match(ASICParser.ASSIGN)
            self.state = 225
            self.match(ASICParser.V4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LblContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(ASICParser.LabelContext,0)


        def COLON(self):
            return self.getToken(ASICParser.COLON, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_lbl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLbl" ):
                listener.enterLbl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLbl" ):
                listener.exitLbl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLbl" ):
                return visitor.visitLbl(self)
            else:
                return visitor.visitChildren(self)




    def lbl(self):

        localctx = ASICParser.LblContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lbl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.label()
            self.state = 228
            self.match(ASICParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASICParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ASICParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ASICParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(ASICParser.ConstantContext,0)


        def define_name(self):
            return self.getTypedRuleContext(ASICParser.Define_nameContext,0)


        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = ASICParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary_expression)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.constant()
                pass
            elif token in [81]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.define_name()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(ASICParser.LPAREN)
                self.state = 235
                self.expression()
                self.state = 236
                self.match(ASICParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(ASICParser.Primary_expressionContext,0)


        def unary_operator(self):
            return self.getTypedRuleContext(ASICParser.Unary_operatorContext,0)


        def unary_expression(self):
            return self.getTypedRuleContext(ASICParser.Unary_expressionContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)




    def unary_expression(self):

        localctx = ASICParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unary_expression)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 37, 81]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.primary_expression()
                pass
            elif token in [45, 46, 55, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.unary_operator()
                self.state = 242
                self.unary_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ASICParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ASICParser.MINUS, 0)

        def TILDE(self):
            return self.getToken(ASICParser.TILDE, 0)

        def NEG(self):
            return self.getToken(ASICParser.NEG, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_operator" ):
                listener.enterUnary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_operator" ):
                listener.exitUnary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_operator" ):
                return visitor.visitUnary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_operator(self):

        localctx = ASICParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 108191944173158400) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ASICParser.STAR, 0)

        def DIV(self):
            return self.getToken(ASICParser.DIV, 0)

        def MOD(self):
            return self.getToken(ASICParser.MOD, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulop" ):
                return visitor.visitMulop(self)
            else:
                return visitor.visitChildren(self)




    def mulop(self):

        localctx = ASICParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Unary_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Unary_expressionContext,i)


        def mulop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.MulopContext)
            else:
                return self.getTypedRuleContext(ASICParser.MulopContext,i)


        def getRuleIndex(self):
            return ASICParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expression" ):
                return visitor.visitMultiplicative_expression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative_expression(self):

        localctx = ASICParser.Multiplicative_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.unary_expression()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0):
                self.state = 251
                self.mulop()
                self.state = 252
                self.unary_expression()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ASICParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ASICParser.MINUS, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddop" ):
                return visitor.visitAddop(self)
            else:
                return visitor.visitChildren(self)




    def addop(self):

        localctx = ASICParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==45 or _la==46):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Multiplicative_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Multiplicative_expressionContext,i)


        def addop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.AddopContext)
            else:
                return self.getTypedRuleContext(ASICParser.AddopContext,i)


        def getRuleIndex(self):
            return ASICParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expression" ):
                return visitor.visitAdditive_expression(self)
            else:
                return visitor.visitChildren(self)




    def additive_expression(self):

        localctx = ASICParser.Additive_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additive_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.multiplicative_expression()
            self.state = 267
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 262
                    self.addop()
                    self.state = 263
                    self.multiplicative_expression() 
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABRACKET(self):
            return self.getToken(ASICParser.LABRACKET, 0)

        def RABRACKET(self):
            return self.getToken(ASICParser.RABRACKET, 0)

        def LEQUAL(self):
            return self.getToken(ASICParser.LEQUAL, 0)

        def GEQUAL(self):
            return self.getToken(ASICParser.GEQUAL, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = ASICParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -4611680520869249024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Additive_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Additive_expressionContext,i)


        def relop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.RelopContext)
            else:
                return self.getTypedRuleContext(ASICParser.RelopContext,i)


        def getRuleIndex(self):
            return ASICParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)




    def relational_expression(self):

        localctx = ASICParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.additive_expression()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4611680520869249024) != 0):
                self.state = 273
                self.relop()
                self.state = 274
                self.additive_expression()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ASICParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(ASICParser.NEQUAL, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_eqop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqop" ):
                listener.enterEqop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqop" ):
                listener.exitEqop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqop" ):
                return visitor.visitEqop(self)
            else:
                return visitor.visitChildren(self)




    def eqop(self):

        localctx = ASICParser.EqopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_eqop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==60 or _la==61):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Relational_expressionContext,i)


        def eqop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.EqopContext)
            else:
                return self.getTypedRuleContext(ASICParser.EqopContext,i)


        def getRuleIndex(self):
            return ASICParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expression" ):
                return visitor.visitEquality_expression(self)
            else:
                return visitor.visitChildren(self)




    def equality_expression(self):

        localctx = ASICParser.Equality_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_equality_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.relational_expression()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60 or _la==61:
                self.state = 284
                self.eqop()
                self.state = 285
                self.relational_expression()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Equality_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Equality_expressionContext,i)


        def AMP(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.AMP)
            else:
                return self.getToken(ASICParser.AMP, i)

        def getRuleIndex(self):
            return ASICParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expression" ):
                return visitor.visitAnd_expression(self)
            else:
                return visitor.visitChildren(self)




    def and_expression(self):

        localctx = ASICParser.And_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.equality_expression()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 293
                self.match(ASICParser.AMP)
                self.state = 294
                self.equality_expression()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Xor_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.And_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.And_expressionContext,i)


        def CARET(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.CARET)
            else:
                return self.getToken(ASICParser.CARET, i)

        def getRuleIndex(self):
            return ASICParser.RULE_xor_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXor_expression" ):
                listener.enterXor_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXor_expression" ):
                listener.exitXor_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXor_expression" ):
                return visitor.visitXor_expression(self)
            else:
                return visitor.visitChildren(self)




    def xor_expression(self):

        localctx = ASICParser.Xor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_xor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.and_expression()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 301
                self.match(ASICParser.CARET)
                self.state = 302
                self.and_expression()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xor_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Xor_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Xor_expressionContext,i)


        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.BAR)
            else:
                return self.getToken(ASICParser.BAR, i)

        def getRuleIndex(self):
            return ASICParser.RULE_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expression" ):
                listener.enterOr_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expression" ):
                listener.exitOr_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expression" ):
                return visitor.visitOr_expression(self)
            else:
                return visitor.visitChildren(self)




    def or_expression(self):

        localctx = ASICParser.Or_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.xor_expression()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 309
                self.match(ASICParser.BAR)
                self.state = 310
                self.xor_expression()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logicaland_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Or_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Or_expressionContext,i)


        def AMPAMP(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.AMPAMP)
            else:
                return self.getToken(ASICParser.AMPAMP, i)

        def getRuleIndex(self):
            return ASICParser.RULE_logicaland_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicaland_expression" ):
                listener.enterLogicaland_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicaland_expression" ):
                listener.exitLogicaland_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicaland_expression" ):
                return visitor.visitLogicaland_expression(self)
            else:
                return visitor.visitChildren(self)




    def logicaland_expression(self):

        localctx = ASICParser.Logicaland_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_logicaland_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.or_expression()
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 317
                self.match(ASICParser.AMPAMP)
                self.state = 318
                self.or_expression()
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logicalor_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicaland_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Logicaland_expressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.Logicaland_expressionContext,i)


        def BARBAR(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.BARBAR)
            else:
                return self.getToken(ASICParser.BARBAR, i)

        def getRuleIndex(self):
            return ASICParser.RULE_logicalor_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalor_expression" ):
                listener.enterLogicalor_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalor_expression" ):
                listener.exitLogicalor_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalor_expression" ):
                return visitor.visitLogicalor_expression(self)
            else:
                return visitor.visitChildren(self)




    def logicalor_expression(self):

        localctx = ASICParser.Logicalor_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_logicalor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.logicaland_expression()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 325
                self.match(ASICParser.BARBAR)
                self.state = 326
                self.logicaland_expression()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(ASICParser.ConstantContext,0)


        def logicalor_expression(self):
            return self.getTypedRuleContext(ASICParser.Logicalor_expressionContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ASICParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.logicalor_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rev_configurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REV(self):
            return self.getToken(ASICParser.REV, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def configuration(self):
            return self.getTypedRuleContext(ASICParser.ConfigurationContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_rev_configuration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRev_configuration" ):
                listener.enterRev_configuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRev_configuration" ):
                listener.exitRev_configuration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRev_configuration" ):
                return visitor.visitRev_configuration(self)
            else:
                return visitor.visitChildren(self)




    def rev_configuration(self):

        localctx = ASICParser.Rev_configurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_rev_configuration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ASICParser.REV)
            self.state = 337
            self.match(ASICParser.LPAREN)
            self.state = 338
            self.configuration()
            self.state = 339
            self.match(ASICParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conf_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.Conf_atomContext)
            else:
                return self.getTypedRuleContext(ASICParser.Conf_atomContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.PLUS)
            else:
                return self.getToken(ASICParser.PLUS, i)

        def getRuleIndex(self):
            return ASICParser.RULE_configuration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfiguration" ):
                listener.enterConfiguration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfiguration" ):
                listener.exitConfiguration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfiguration" ):
                return visitor.visitConfiguration(self)
            else:
                return visitor.visitChildren(self)




    def configuration(self):

        localctx = ASICParser.ConfigurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_configuration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.conf_atom()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 342
                self.match(ASICParser.PLUS)
                self.state = 343
                self.conf_atom()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conf_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conf_d(self):
            return self.getTypedRuleContext(ASICParser.Conf_dContext,0)


        def conf_c(self):
            return self.getTypedRuleContext(ASICParser.Conf_cContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_conf_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConf_atom" ):
                listener.enterConf_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConf_atom" ):
                listener.exitConf_atom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConf_atom" ):
                return visitor.visitConf_atom(self)
            else:
                return visitor.visitChildren(self)




    def conf_atom(self):

        localctx = ASICParser.Conf_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_conf_atom)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 13, 14, 15, 16, 17, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.conf_d()
                pass
            elif token in [28, 81]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.conf_c()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conf_dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vreg(self):
            return self.getTypedRuleContext(ASICParser.VregContext,0)


        def vreg_r(self):
            return self.getTypedRuleContext(ASICParser.Vreg_rContext,0)


        def LBRACE(self):
            return self.getToken(ASICParser.LBRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.ExpressionContext,i)


        def RBRACE(self):
            return self.getToken(ASICParser.RBRACE, 0)

        def LSHIFT(self):
            return self.getToken(ASICParser.LSHIFT, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_conf_d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConf_d" ):
                listener.enterConf_d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConf_d" ):
                listener.exitConf_d(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConf_d" ):
                return visitor.visitConf_d(self)
            else:
                return visitor.visitChildren(self)




    def conf_d(self):

        localctx = ASICParser.Conf_dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_conf_d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17]:
                self.state = 353
                self.vreg()
                pass
            elif token in [5, 30]:
                self.state = 354
                self.vreg_r()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 357
                self.match(ASICParser.LBRACE)
                self.state = 358
                self.expression()
                self.state = 359
                self.match(ASICParser.RBRACE)


            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 363
                self.match(ASICParser.LSHIFT)
                self.state = 364
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conf_cContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_name(self):
            return self.getTypedRuleContext(ASICParser.Const_nameContext,0)


        def const_expr(self):
            return self.getTypedRuleContext(ASICParser.Const_exprContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_conf_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConf_c" ):
                listener.enterConf_c(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConf_c" ):
                listener.exitConf_c(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConf_c" ):
                return visitor.visitConf_c(self)
            else:
                return visitor.visitChildren(self)




    def conf_c(self):

        localctx = ASICParser.Conf_cContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_conf_c)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [81]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.const_name()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.const_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_addrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ASICParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ASICParser.RBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def vreg_d(self):
            return self.getTypedRuleContext(ASICParser.Vreg_dContext,0)


        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_const_addr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_addr" ):
                listener.enterConst_addr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_addr" ):
                listener.exitConst_addr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_addr" ):
                return visitor.visitConst_addr(self)
            else:
                return visitor.visitChildren(self)




    def const_addr(self):

        localctx = ASICParser.Const_addrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_const_addr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(ASICParser.LBRACKET)
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 37, 45, 46, 55, 56, 81]:
                self.state = 372
                self.expression()
                pass
            elif token in [13, 15, 16, 17]:
                self.state = 373
                self.vreg_d()
                pass
            elif token in [5, 6, 7, 8]:
                self.state = 374
                self.sreg()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 377
            self.match(ASICParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_shiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSHIFT(self):
            return self.getToken(ASICParser.LSHIFT, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_const_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_shift" ):
                listener.enterConst_shift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_shift" ):
                listener.exitConst_shift(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_shift" ):
                return visitor.visitConst_shift(self)
            else:
                return visitor.visitChildren(self)




    def const_shift(self):

        localctx = ASICParser.Const_shiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_const_shift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ASICParser.LSHIFT)
            self.state = 380
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SC(self):
            return self.getToken(ASICParser.SC, 0)

        def const_addr(self):
            return self.getTypedRuleContext(ASICParser.Const_addrContext,0)


        def const_shift(self):
            return self.getTypedRuleContext(ASICParser.Const_shiftContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_const_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_expr" ):
                listener.enterConst_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_expr" ):
                listener.exitConst_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_expr" ):
                return visitor.visitConst_expr(self)
            else:
                return visitor.visitChildren(self)




    def const_expr(self):

        localctx = ASICParser.Const_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_const_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ASICParser.SC)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 383
                self.const_addr()


            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 386
                self.const_shift()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ASICParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ASICParser.MINUS, 0)

        def STAR(self):
            return self.getToken(ASICParser.STAR, 0)

        def DIV(self):
            return self.getToken(ASICParser.DIV, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = ASICParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 527765581332480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASICParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_define_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_name" ):
                listener.enterDefine_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_name" ):
                listener.exitDefine_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_name" ):
                return visitor.visitDefine_name(self)
            else:
                return visitor.visitChildren(self)




    def define_name(self):

        localctx = ASICParser.Define_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_define_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(ASICParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Config_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASICParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_config_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig_name" ):
                listener.enterConfig_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig_name" ):
                listener.exitConfig_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfig_name" ):
                return visitor.visitConfig_name(self)
            else:
                return visitor.visitChildren(self)




    def config_name(self):

        localctx = ASICParser.Config_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_config_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ASICParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ASICParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_const_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_name" ):
                listener.enterConst_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_name" ):
                listener.exitConst_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_name" ):
                return visitor.visitConst_name(self)
            else:
                return visitor.visitChildren(self)




    def const_name(self):

        localctx = ASICParser.Const_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_const_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(ASICParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def config_name(self):
            return self.getTypedRuleContext(ASICParser.Config_nameContext,0)


        def configuration(self):
            return self.getTypedRuleContext(ASICParser.ConfigurationContext,0)


        def rev_configuration(self):
            return self.getTypedRuleContext(ASICParser.Rev_configurationContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ASICParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ASICParser.LPAREN)
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 398
                self.config_name()
                pass

            elif la_ == 2:
                self.state = 399
                self.configuration()
                pass

            elif la_ == 3:
                self.state = 400
                self.rev_configuration()
                pass


            self.state = 403
            self.match(ASICParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def output(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.OutputContext)
            else:
                return self.getTypedRuleContext(ASICParser.OutputContext,i)


        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ASICParser.COMMA)
            else:
                return self.getToken(ASICParser.COMMA, i)

        def getRuleIndex(self):
            return ASICParser.RULE_resultexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResultexpr" ):
                listener.enterResultexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResultexpr" ):
                listener.exitResultexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResultexpr" ):
                return visitor.visitResultexpr(self)
            else:
                return visitor.visitChildren(self)




    def resultexpr(self):

        localctx = ASICParser.ResultexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_resultexpr)
        self._la = 0 # Token type
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17, 71, 72, 75, 76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.output()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(ASICParser.LPAREN)
                self.state = 407
                self.output()
                self.state = 410 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 408
                    self.match(ASICParser.COMMA)
                    self.state = 409
                    self.output()
                    self.state = 412 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==66):
                        break

                self.state = 414
                self.match(ASICParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SregContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def R0(self):
            return self.getToken(ASICParser.R0, 0)

        def R1(self):
            return self.getToken(ASICParser.R1, 0)

        def R2(self):
            return self.getToken(ASICParser.R2, 0)

        def R3(self):
            return self.getToken(ASICParser.R3, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_sreg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSreg" ):
                listener.enterSreg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSreg" ):
                listener.exitSreg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSreg" ):
                return visitor.visitSreg(self)
            else:
                return visitor.visitChildren(self)




    def sreg(self):

        localctx = ASICParser.SregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_sreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARG0(self):
            return self.getToken(ASICParser.ARG0, 0)

        def ARG1(self):
            return self.getToken(ASICParser.ARG1, 0)

        def ARG2(self):
            return self.getToken(ASICParser.ARG2, 0)

        def ARG3(self):
            return self.getToken(ASICParser.ARG3, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ASICParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VregContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V1(self):
            return self.getToken(ASICParser.V1, 0)

        def V1H(self):
            return self.getToken(ASICParser.V1H, 0)

        def V2(self):
            return self.getToken(ASICParser.V2, 0)

        def V3(self):
            return self.getToken(ASICParser.V3, 0)

        def V4(self):
            return self.getToken(ASICParser.V4, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_vreg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg" ):
                listener.enterVreg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg" ):
                listener.exitVreg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVreg" ):
                return visitor.visitVreg(self)
            else:
                return visitor.visitChildren(self)




    def vreg(self):

        localctx = ASICParser.VregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_vreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 253952) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vreg_dContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V1(self):
            return self.getToken(ASICParser.V1, 0)

        def V2(self):
            return self.getToken(ASICParser.V2, 0)

        def V3(self):
            return self.getToken(ASICParser.V3, 0)

        def V4(self):
            return self.getToken(ASICParser.V4, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_vreg_d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg_d" ):
                listener.enterVreg_d(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg_d" ):
                listener.exitVreg_d(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVreg_d" ):
                return visitor.visitVreg_d(self)
            else:
                return visitor.visitChildren(self)




    def vreg_d(self):

        localctx = ASICParser.Vreg_dContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_vreg_d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 237568) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vreg_rContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def R0(self):
            return self.getToken(ASICParser.R0, 0)

        def REV(self):
            return self.getToken(ASICParser.REV, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_vreg_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg_r" ):
                listener.enterVreg_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg_r" ):
                listener.exitVreg_r(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVreg_r" ):
                return visitor.visitVreg_r(self)
            else:
                return visitor.visitChildren(self)




    def vreg_r(self):

        localctx = ASICParser.Vreg_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_vreg_r)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(ASICParser.R0)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(ASICParser.REV)
                self.state = 428
                self.match(ASICParser.LPAREN)
                self.state = 429
                self.match(ASICParser.R0)
                self.state = 430
                self.match(ASICParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vreg_specialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V2N(self):
            return self.getToken(ASICParser.V2N, 0)

        def V4M(self):
            return self.getToken(ASICParser.V4M, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_vreg_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg_special" ):
                listener.enterVreg_special(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg_special" ):
                listener.exitVreg_special(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVreg_special" ):
                return visitor.visitVreg_special(self)
            else:
                return visitor.visitChildren(self)




    def vreg_special(self):

        localctx = ASICParser.Vreg_specialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_vreg_special)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==71 or _la==72):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vreg(self):
            return self.getTypedRuleContext(ASICParser.VregContext,0)


        def vreg_special(self):
            return self.getTypedRuleContext(ASICParser.Vreg_specialContext,0)


        def CMP(self):
            return self.getToken(ASICParser.CMP, 0)

        def OUT(self):
            return self.getToken(ASICParser.OUT, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = ASICParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_output)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.vreg()
                pass
            elif token in [71, 72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.vreg_special()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(ASICParser.CMP)
                pass
            elif token in [76]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.match(ASICParser.OUT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StdopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A1(self):
            return self.getToken(ASICParser.A1, 0)

        def A4(self):
            return self.getToken(ASICParser.A4, 0)

        def A5(self):
            return self.getToken(ASICParser.A5, 0)

        def A128D(self):
            return self.getToken(ASICParser.A128D, 0)

        def SD(self):
            return self.getToken(ASICParser.SD, 0)

        def DINV(self):
            return self.getToken(ASICParser.DINV, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_stdop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStdop" ):
                listener.enterStdop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStdop" ):
                listener.exitStdop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdop" ):
                return visitor.visitStdop(self)
            else:
                return visitor.visitChildren(self)




    def stdop(self):

        localctx = ASICParser.StdopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stdop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AluopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ASICParser.ID, 0)

        def INV(self):
            return self.getToken(ASICParser.INV, 0)

        def AND(self):
            return self.getToken(ASICParser.AND, 0)

        def OR(self):
            return self.getToken(ASICParser.OR, 0)

        def XOR(self):
            return self.getToken(ASICParser.XOR, 0)

        def NOT(self):
            return self.getToken(ASICParser.NOT, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_aluop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAluop" ):
                listener.enterAluop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAluop" ):
                listener.exitAluop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAluop" ):
                return visitor.visitAluop(self)
            else:
                return visitor.visitChildren(self)




    def aluop(self):

        localctx = ASICParser.AluopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_aluop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67108864000) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpcopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GEN(self):
            return self.getToken(ASICParser.GEN, 0)

        def EOP(self):
            return self.getToken(ASICParser.EOP, 0)

        def WAIT(self):
            return self.getToken(ASICParser.WAIT, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def jump(self):
            return self.getTypedRuleContext(ASICParser.JumpContext,0)


        def getRuleIndex(self):
            return ASICParser.RULE_spcop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpcop" ):
                listener.enterSpcop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpcop" ):
                listener.exitSpcop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpcop" ):
                return visitor.visitSpcop(self)
            else:
                return visitor.visitChildren(self)




    def spcop(self):

        localctx = ASICParser.SpcopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_spcop)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [77]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.match(ASICParser.GEN)
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(ASICParser.EOP)
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.match(ASICParser.WAIT)
                self.state = 448
                self.match(ASICParser.LPAREN)
                self.state = 449
                self.expression()
                self.state = 450
                self.match(ASICParser.RPAREN)
                pass
            elif token in [80]:
                self.enterOuterAlt(localctx, 4)
                self.state = 452
                self.jump()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JNZ(self):
            return self.getToken(ASICParser.JNZ, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def COMMA(self):
            return self.getToken(ASICParser.COMMA, 0)

        def label(self):
            return self.getTypedRuleContext(ASICParser.LabelContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump" ):
                return visitor.visitJump(self)
            else:
                return visitor.visitChildren(self)




    def jump(self):

        localctx = ASICParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_jump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(ASICParser.JNZ)
            self.state = 456
            self.match(ASICParser.LPAREN)
            self.state = 457
            self.sreg()
            self.state = 458
            self.match(ASICParser.COMMA)
            self.state = 459
            self.label()
            self.state = 460
            self.match(ASICParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(ASICParser.LINE_COMMENT, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = ASICParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ASICParser.LINE_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





