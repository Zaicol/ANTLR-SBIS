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
        4,1,86,467,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,1,0,5,0,126,8,0,10,0,12,0,129,9,0,1,1,1,
        1,1,1,1,1,3,1,135,8,1,1,1,3,1,138,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,4,3,4,152,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,3,6,162,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,3,9,171,8,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,184,8,9,1,9,3,9,187,8,9,1,
        10,1,10,3,10,191,8,10,1,11,1,11,3,11,195,8,11,1,12,1,12,1,12,1,12,
        3,12,201,8,12,1,13,1,13,1,13,1,13,1,13,3,13,208,8,13,1,14,1,14,1,
        14,1,14,3,14,214,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,
        14,224,8,14,1,14,3,14,227,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,244,8,18,1,19,1,19,
        1,19,1,19,3,19,250,8,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,
        5,22,260,8,22,10,22,12,22,263,9,22,1,23,1,23,1,24,1,24,1,24,1,24,
        5,24,271,8,24,10,24,12,24,274,9,24,1,25,1,25,1,26,1,26,1,26,1,26,
        5,26,282,8,26,10,26,12,26,285,9,26,1,27,1,27,1,28,1,28,1,28,1,28,
        5,28,293,8,28,10,28,12,28,296,9,28,1,29,1,29,1,29,5,29,301,8,29,
        10,29,12,29,304,9,29,1,30,1,30,1,30,5,30,309,8,30,10,30,12,30,312,
        9,30,1,31,1,31,1,31,5,31,317,8,31,10,31,12,31,320,9,31,1,32,1,32,
        1,32,5,32,325,8,32,10,32,12,32,328,9,32,1,33,1,33,1,33,5,33,333,
        8,33,10,33,12,33,336,9,33,1,34,1,34,3,34,340,8,34,1,35,1,35,1,35,
        1,35,1,35,1,36,1,36,1,36,5,36,350,8,36,10,36,12,36,353,9,36,1,37,
        1,37,3,37,357,8,37,1,38,1,38,3,38,361,8,38,1,38,1,38,1,38,1,38,3,
        38,367,8,38,1,38,1,38,3,38,371,8,38,1,39,1,39,3,39,375,8,39,1,40,
        1,40,1,40,1,40,3,40,381,8,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,
        3,42,390,8,42,1,42,3,42,393,8,42,1,43,1,43,1,44,1,44,1,45,1,45,1,
        46,1,46,1,47,1,47,1,47,1,47,3,47,407,8,47,1,47,1,47,1,48,1,48,1,
        48,1,48,1,48,4,48,416,8,48,11,48,12,48,417,1,48,1,48,3,48,422,8,
        48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,53,1,53,1,
        53,3,53,437,8,53,1,54,1,54,1,55,1,55,1,55,1,55,3,55,445,8,55,1,56,
        1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,60,1,60,1,60,
        1,60,1,60,1,60,1,60,1,61,1,61,1,61,0,0,62,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,
        104,106,108,110,112,114,116,118,120,122,0,14,1,0,1,4,2,0,48,49,58,
        59,1,0,50,52,1,0,48,49,3,0,43,43,45,45,65,66,1,0,63,64,1,0,48,51,
        1,0,5,8,1,0,9,12,1,0,13,17,2,0,13,13,15,17,1,0,74,75,1,0,22,29,2,
        0,31,31,34,38,457,0,127,1,0,0,0,2,134,1,0,0,0,4,139,1,0,0,0,6,146,
        1,0,0,0,8,151,1,0,0,0,10,153,1,0,0,0,12,157,1,0,0,0,14,163,1,0,0,
        0,16,167,1,0,0,0,18,186,1,0,0,0,20,190,1,0,0,0,22,194,1,0,0,0,24,
        196,1,0,0,0,26,207,1,0,0,0,28,226,1,0,0,0,30,228,1,0,0,0,32,232,
        1,0,0,0,34,235,1,0,0,0,36,243,1,0,0,0,38,249,1,0,0,0,40,251,1,0,
        0,0,42,253,1,0,0,0,44,255,1,0,0,0,46,264,1,0,0,0,48,266,1,0,0,0,
        50,275,1,0,0,0,52,277,1,0,0,0,54,286,1,0,0,0,56,288,1,0,0,0,58,297,
        1,0,0,0,60,305,1,0,0,0,62,313,1,0,0,0,64,321,1,0,0,0,66,329,1,0,
        0,0,68,339,1,0,0,0,70,341,1,0,0,0,72,346,1,0,0,0,74,356,1,0,0,0,
        76,360,1,0,0,0,78,374,1,0,0,0,80,376,1,0,0,0,82,384,1,0,0,0,84,387,
        1,0,0,0,86,394,1,0,0,0,88,396,1,0,0,0,90,398,1,0,0,0,92,400,1,0,
        0,0,94,402,1,0,0,0,96,421,1,0,0,0,98,423,1,0,0,0,100,425,1,0,0,0,
        102,427,1,0,0,0,104,429,1,0,0,0,106,436,1,0,0,0,108,438,1,0,0,0,
        110,444,1,0,0,0,112,446,1,0,0,0,114,448,1,0,0,0,116,450,1,0,0,0,
        118,452,1,0,0,0,120,457,1,0,0,0,122,464,1,0,0,0,124,126,3,2,1,0,
        125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,
        128,1,1,0,0,0,129,127,1,0,0,0,130,135,3,8,4,0,131,135,3,18,9,0,132,
        135,3,4,2,0,133,135,3,6,3,0,134,130,1,0,0,0,134,131,1,0,0,0,134,
        132,1,0,0,0,134,133,1,0,0,0,135,137,1,0,0,0,136,138,3,122,61,0,137,
        136,1,0,0,0,137,138,1,0,0,0,138,3,1,0,0,0,139,140,5,76,0,0,140,141,
        5,40,0,0,141,142,3,98,49,0,142,143,5,69,0,0,143,144,3,16,8,0,144,
        145,5,41,0,0,145,5,1,0,0,0,146,147,5,77,0,0,147,7,1,0,0,0,148,152,
        3,10,5,0,149,152,3,12,6,0,150,152,3,14,7,0,151,148,1,0,0,0,151,149,
        1,0,0,0,151,150,1,0,0,0,152,9,1,0,0,0,153,154,5,19,0,0,154,155,3,
        88,44,0,155,156,3,68,34,0,156,11,1,0,0,0,157,158,5,20,0,0,158,161,
        3,90,45,0,159,162,3,72,36,0,160,162,3,70,35,0,161,159,1,0,0,0,161,
        160,1,0,0,0,162,13,1,0,0,0,163,164,5,21,0,0,164,165,3,92,46,0,165,
        166,3,84,42,0,166,15,1,0,0,0,167,168,7,0,0,0,168,17,1,0,0,0,169,
        171,3,32,16,0,170,169,1,0,0,0,170,171,1,0,0,0,171,183,1,0,0,0,172,
        184,3,20,10,0,173,174,3,20,10,0,174,175,5,69,0,0,175,176,3,20,10,
        0,176,184,1,0,0,0,177,178,3,20,10,0,178,179,5,69,0,0,179,180,3,20,
        10,0,180,181,5,69,0,0,181,182,3,20,10,0,182,184,1,0,0,0,183,172,
        1,0,0,0,183,173,1,0,0,0,183,177,1,0,0,0,184,187,1,0,0,0,185,187,
        3,32,16,0,186,170,1,0,0,0,186,185,1,0,0,0,187,19,1,0,0,0,188,191,
        3,22,11,0,189,191,3,28,14,0,190,188,1,0,0,0,190,189,1,0,0,0,191,
        21,1,0,0,0,192,195,3,24,12,0,193,195,3,26,13,0,194,192,1,0,0,0,194,
        193,1,0,0,0,195,23,1,0,0,0,196,197,3,98,49,0,197,200,5,60,0,0,198,
        201,3,68,34,0,199,201,3,100,50,0,200,198,1,0,0,0,200,199,1,0,0,0,
        201,25,1,0,0,0,202,203,5,5,0,0,203,208,5,67,0,0,204,205,3,98,49,
        0,205,206,5,68,0,0,206,208,1,0,0,0,207,202,1,0,0,0,207,204,1,0,0,
        0,208,27,1,0,0,0,209,210,3,96,48,0,210,213,5,60,0,0,211,214,3,114,
        57,0,212,214,3,112,56,0,213,211,1,0,0,0,213,212,1,0,0,0,214,215,
        1,0,0,0,215,216,3,94,47,0,216,227,1,0,0,0,217,218,5,13,0,0,218,219,
        5,60,0,0,219,227,5,80,0,0,220,224,3,116,58,0,221,224,3,118,59,0,
        222,224,3,120,60,0,223,220,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,
        0,224,227,1,0,0,0,225,227,3,30,15,0,226,209,1,0,0,0,226,217,1,0,
        0,0,226,223,1,0,0,0,226,225,1,0,0,0,227,29,1,0,0,0,228,229,5,79,
        0,0,229,230,5,60,0,0,230,231,5,17,0,0,231,31,1,0,0,0,232,233,3,34,
        17,0,233,234,5,70,0,0,234,33,1,0,0,0,235,236,5,84,0,0,236,35,1,0,
        0,0,237,244,3,16,8,0,238,244,3,88,44,0,239,240,5,40,0,0,240,241,
        3,68,34,0,241,242,5,41,0,0,242,244,1,0,0,0,243,237,1,0,0,0,243,238,
        1,0,0,0,243,239,1,0,0,0,244,37,1,0,0,0,245,250,3,36,18,0,246,247,
        3,40,20,0,247,248,3,38,19,0,248,250,1,0,0,0,249,245,1,0,0,0,249,
        246,1,0,0,0,250,39,1,0,0,0,251,252,7,1,0,0,252,41,1,0,0,0,253,254,
        7,2,0,0,254,43,1,0,0,0,255,261,3,38,19,0,256,257,3,42,21,0,257,258,
        3,38,19,0,258,260,1,0,0,0,259,256,1,0,0,0,260,263,1,0,0,0,261,259,
        1,0,0,0,261,262,1,0,0,0,262,45,1,0,0,0,263,261,1,0,0,0,264,265,7,
        3,0,0,265,47,1,0,0,0,266,272,3,44,22,0,267,268,3,46,23,0,268,269,
        3,44,22,0,269,271,1,0,0,0,270,267,1,0,0,0,271,274,1,0,0,0,272,270,
        1,0,0,0,272,273,1,0,0,0,273,49,1,0,0,0,274,272,1,0,0,0,275,276,7,
        4,0,0,276,51,1,0,0,0,277,283,3,48,24,0,278,279,3,50,25,0,279,280,
        3,48,24,0,280,282,1,0,0,0,281,278,1,0,0,0,282,285,1,0,0,0,283,281,
        1,0,0,0,283,284,1,0,0,0,284,53,1,0,0,0,285,283,1,0,0,0,286,287,7,
        5,0,0,287,55,1,0,0,0,288,294,3,52,26,0,289,290,3,54,27,0,290,291,
        3,52,26,0,291,293,1,0,0,0,292,289,1,0,0,0,293,296,1,0,0,0,294,292,
        1,0,0,0,294,295,1,0,0,0,295,57,1,0,0,0,296,294,1,0,0,0,297,302,3,
        56,28,0,298,299,5,54,0,0,299,301,3,56,28,0,300,298,1,0,0,0,301,304,
        1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,59,1,0,0,0,304,302,1,
        0,0,0,305,310,3,58,29,0,306,307,5,53,0,0,307,309,3,58,29,0,308,306,
        1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,61,1,
        0,0,0,312,310,1,0,0,0,313,318,3,60,30,0,314,315,5,56,0,0,315,317,
        3,60,30,0,316,314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,
        1,0,0,0,319,63,1,0,0,0,320,318,1,0,0,0,321,326,3,62,31,0,322,323,
        5,55,0,0,323,325,3,62,31,0,324,322,1,0,0,0,325,328,1,0,0,0,326,324,
        1,0,0,0,326,327,1,0,0,0,327,65,1,0,0,0,328,326,1,0,0,0,329,334,3,
        64,32,0,330,331,5,57,0,0,331,333,3,64,32,0,332,330,1,0,0,0,333,336,
        1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,67,1,0,0,0,336,334,1,
        0,0,0,337,340,3,16,8,0,338,340,3,66,33,0,339,337,1,0,0,0,339,338,
        1,0,0,0,340,69,1,0,0,0,341,342,5,32,0,0,342,343,5,40,0,0,343,344,
        3,72,36,0,344,345,5,41,0,0,345,71,1,0,0,0,346,351,3,74,37,0,347,
        348,5,48,0,0,348,350,3,74,37,0,349,347,1,0,0,0,350,353,1,0,0,0,351,
        349,1,0,0,0,351,352,1,0,0,0,352,73,1,0,0,0,353,351,1,0,0,0,354,357,
        3,76,38,0,355,357,3,78,39,0,356,354,1,0,0,0,356,355,1,0,0,0,357,
        75,1,0,0,0,358,361,3,102,51,0,359,361,3,106,53,0,360,358,1,0,0,0,
        360,359,1,0,0,0,361,366,1,0,0,0,362,363,5,46,0,0,363,364,3,68,34,
        0,364,365,5,47,0,0,365,367,1,0,0,0,366,362,1,0,0,0,366,367,1,0,0,
        0,367,370,1,0,0,0,368,369,5,61,0,0,369,371,3,68,34,0,370,368,1,0,
        0,0,370,371,1,0,0,0,371,77,1,0,0,0,372,375,3,92,46,0,373,375,3,84,
        42,0,374,372,1,0,0,0,374,373,1,0,0,0,375,79,1,0,0,0,376,380,5,42,
        0,0,377,381,3,68,34,0,378,381,3,104,52,0,379,381,3,98,49,0,380,377,
        1,0,0,0,380,378,1,0,0,0,380,379,1,0,0,0,381,382,1,0,0,0,382,383,
        5,44,0,0,383,81,1,0,0,0,384,385,5,61,0,0,385,386,3,68,34,0,386,83,
        1,0,0,0,387,389,5,30,0,0,388,390,3,80,40,0,389,388,1,0,0,0,389,390,
        1,0,0,0,390,392,1,0,0,0,391,393,3,82,41,0,392,391,1,0,0,0,392,393,
        1,0,0,0,393,85,1,0,0,0,394,395,7,6,0,0,395,87,1,0,0,0,396,397,5,
        84,0,0,397,89,1,0,0,0,398,399,5,84,0,0,399,91,1,0,0,0,400,401,5,
        84,0,0,401,93,1,0,0,0,402,406,5,40,0,0,403,407,3,90,45,0,404,407,
        3,72,36,0,405,407,3,70,35,0,406,403,1,0,0,0,406,404,1,0,0,0,406,
        405,1,0,0,0,407,408,1,0,0,0,408,409,5,41,0,0,409,95,1,0,0,0,410,
        422,3,110,55,0,411,412,5,40,0,0,412,415,3,110,55,0,413,414,5,69,
        0,0,414,416,3,110,55,0,415,413,1,0,0,0,416,417,1,0,0,0,417,415,1,
        0,0,0,417,418,1,0,0,0,418,419,1,0,0,0,419,420,5,41,0,0,420,422,1,
        0,0,0,421,410,1,0,0,0,421,411,1,0,0,0,422,97,1,0,0,0,423,424,7,7,
        0,0,424,99,1,0,0,0,425,426,7,8,0,0,426,101,1,0,0,0,427,428,7,9,0,
        0,428,103,1,0,0,0,429,430,7,10,0,0,430,105,1,0,0,0,431,437,5,5,0,
        0,432,433,5,33,0,0,433,434,5,40,0,0,434,435,5,5,0,0,435,437,5,41,
        0,0,436,431,1,0,0,0,436,432,1,0,0,0,437,107,1,0,0,0,438,439,7,11,
        0,0,439,109,1,0,0,0,440,445,3,102,51,0,441,445,3,108,54,0,442,445,
        5,78,0,0,443,445,5,79,0,0,444,440,1,0,0,0,444,441,1,0,0,0,444,442,
        1,0,0,0,444,443,1,0,0,0,445,111,1,0,0,0,446,447,7,12,0,0,447,113,
        1,0,0,0,448,449,7,13,0,0,449,115,1,0,0,0,450,451,5,81,0,0,451,117,
        1,0,0,0,452,453,5,82,0,0,453,454,5,40,0,0,454,455,3,68,34,0,455,
        456,5,41,0,0,456,119,1,0,0,0,457,458,5,83,0,0,458,459,5,40,0,0,459,
        460,3,98,49,0,460,461,5,69,0,0,461,462,3,34,17,0,462,463,5,41,0,
        0,463,121,1,0,0,0,464,465,5,86,0,0,465,123,1,0,0,0,41,127,134,137,
        151,161,170,183,186,190,194,200,207,213,223,226,243,249,261,272,
        283,294,302,310,318,326,334,339,351,356,360,366,370,374,380,389,
        392,406,417,421,436,444
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'['", "'<'", 
                     "']'", "'>'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'&'", "'&&'", "'|'", "'||'", "'!'", 
                     "'~'", "'='", "'<<'", "'>>'", "'=='", "'!='", "'<='", 
                     "'>='", "'++'", "'--'", "','", "':'", "';'", "'.'", 
                     "'#'" ]

    symbolicNames = [ "<INVALID>", "HEXADECIMAL", "DECIMAL", "BINARY", "OCTAL", 
                      "R0", "R1", "R2", "R3", "ARG0", "ARG1", "ARG2", "ARG3", 
                      "V1", "V1H", "V2", "V3", "V4", "PROCCHAR", "DEFINE", 
                      "CONFIG", "CONST", "A1", "A4", "A5", "A128D", "DINV", 
                      "SD", "D_K64", "DINV_K64", "SC", "ID", "REV", "REV_REG", 
                      "INV", "AND", "OR", "XOR", "NOT", "EOL", "LPAREN", 
                      "RPAREN", "LBRACKET", "LABRACKET", "RBRACKET", "RABRACKET", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", "DIV", 
                      "MOD", "CARET", "AMP", "AMPAMP", "BAR", "BARBAR", 
                      "NEG", "TILDE", "ASSIGN", "LSHIFT", "RSHIFT", "EQUAL", 
                      "NEQUAL", "LEQUAL", "GEQUAL", "PLUSPLUS", "MINUSMINUS", 
                      "COMMA", "COLON", "SEMI", "DOT", "HASH", "V2N", "V4M", 
                      "FOR", "ENDFOR", "CMP", "OUT", "GEN", "EOP", "WAIT", 
                      "JNZ", "IDENTIFIER", "WS", "LINE_COMMENT" ]

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
    RULE_eop = 58
    RULE_wait = 59
    RULE_jump = 60
    RULE_comment = 61

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
                   "vreg_special", "output", "stdop", "aluop", "eop", "wait", 
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
    D_K64=28
    DINV_K64=29
    SC=30
    ID=31
    REV=32
    REV_REG=33
    INV=34
    AND=35
    OR=36
    XOR=37
    NOT=38
    EOL=39
    LPAREN=40
    RPAREN=41
    LBRACKET=42
    LABRACKET=43
    RBRACKET=44
    RABRACKET=45
    LBRACE=46
    RBRACE=47
    PLUS=48
    MINUS=49
    STAR=50
    DIV=51
    MOD=52
    CARET=53
    AMP=54
    AMPAMP=55
    BAR=56
    BARBAR=57
    NEG=58
    TILDE=59
    ASSIGN=60
    LSHIFT=61
    RSHIFT=62
    EQUAL=63
    NEQUAL=64
    LEQUAL=65
    GEQUAL=66
    PLUSPLUS=67
    MINUSMINUS=68
    COMMA=69
    COLON=70
    SEMI=71
    DOT=72
    HASH=73
    V2N=74
    V4M=75
    FOR=76
    ENDFOR=77
    CMP=78
    OUT=79
    GEN=80
    EOP=81
    WAIT=82
    JNZ=83
    IDENTIFIER=84
    WS=85
    LINE_COMMENT=86

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
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1099515552224) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 1983) != 0):
                self.state = 124
                self.line()
                self.state = 129
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21]:
                self.state = 130
                self.definition()
                pass
            elif token in [5, 6, 7, 8, 13, 14, 15, 16, 17, 40, 74, 75, 78, 79, 81, 82, 83, 84]:
                self.state = 131
                self.statement()
                pass
            elif token in [76]:
                self.state = 132
                self.forloop()
                pass
            elif token in [77]:
                self.state = 133
                self.endfor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==86:
                self.state = 136
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
            self.state = 139
            self.match(ASICParser.FOR)
            self.state = 140
            self.match(ASICParser.LPAREN)
            self.state = 141
            self.sreg()
            self.state = 142
            self.match(ASICParser.COMMA)
            self.state = 143
            self.constant()
            self.state = 144
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
            self.state = 146
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.define_def()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.config_def()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
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
            self.state = 153
            self.match(ASICParser.DEFINE)
            self.state = 154
            self.define_name()
            self.state = 155
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
            self.state = 157
            self.match(ASICParser.CONFIG)
            self.state = 158
            self.config_name()
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 13, 14, 15, 16, 17, 30, 33, 84]:
                self.state = 159
                self.configuration()
                pass
            elif token in [32]:
                self.state = 160
                self.rev_configuration()
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
            self.state = 163
            self.match(ASICParser.CONST)
            self.state = 164
            self.const_name()
            self.state = 165
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
            self.state = 167
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==84:
                    self.state = 169
                    self.lbl()


                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 172
                    self.instruction()
                    pass

                elif la_ == 2:
                    self.state = 173
                    self.instruction()
                    self.state = 174
                    self.match(ASICParser.COMMA)
                    self.state = 175
                    self.instruction()
                    pass

                elif la_ == 3:
                    self.state = 177
                    self.instruction()
                    self.state = 178
                    self.match(ASICParser.COMMA)
                    self.state = 179
                    self.instruction()
                    self.state = 180
                    self.match(ASICParser.COMMA)
                    self.state = 181
                    self.instruction()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.sregop()
                pass
            elif token in [13, 14, 15, 16, 17, 40, 74, 75, 78, 79, 81, 82, 83]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.asignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
            self.state = 196
            self.sreg()
            self.state = 197
            self.match(ASICParser.ASSIGN)
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 40, 48, 49, 58, 59, 84]:
                self.state = 198
                self.expression()
                pass
            elif token in [9, 10, 11, 12]:
                self.state = 199
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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(ASICParser.R0)
                self.state = 203
                self.match(ASICParser.PLUSPLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.sreg()
                self.state = 205
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


    class SpCopContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def eop(self):
            return self.getTypedRuleContext(ASICParser.EopContext,0)

        def wait(self):
            return self.getTypedRuleContext(ASICParser.WaitContext,0)

        def jump(self):
            return self.getTypedRuleContext(ASICParser.JumpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpCop" ):
                listener.enterSpCop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpCop" ):
                listener.exitSpCop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpCop" ):
                return visitor.visitSpCop(self)
            else:
                return visitor.visitChildren(self)


    class GenOpContext(OperatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ASICParser.OperatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def V1(self):
            return self.getToken(ASICParser.V1, 0)
        def ASSIGN(self):
            return self.getToken(ASICParser.ASSIGN, 0)
        def GEN(self):
            return self.getToken(ASICParser.GEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGenOp" ):
                listener.enterGenOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGenOp" ):
                listener.exitGenOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenOp" ):
                return visitor.visitGenOp(self)
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ASICParser.AluSpOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.resultexpr()
                self.state = 210
                self.match(ASICParser.ASSIGN)
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31, 34, 35, 36, 37, 38]:
                    self.state = 211
                    self.aluop()
                    pass
                elif token in [22, 23, 24, 25, 26, 27, 28, 29]:
                    self.state = 212
                    self.stdop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215
                self.argument()
                pass

            elif la_ == 2:
                localctx = ASICParser.GenOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(ASICParser.V1)
                self.state = 218
                self.match(ASICParser.ASSIGN)
                self.state = 219
                self.match(ASICParser.GEN)
                pass

            elif la_ == 3:
                localctx = ASICParser.SpCopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [81]:
                    self.state = 220
                    self.eop()
                    pass
                elif token in [82]:
                    self.state = 221
                    self.wait()
                    pass
                elif token in [83]:
                    self.state = 222
                    self.jump()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                localctx = ASICParser.OutOpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 225
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
            self.state = 228
            self.match(ASICParser.OUT)
            self.state = 229
            self.match(ASICParser.ASSIGN)
            self.state = 230
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
            self.state = 232
            self.label()
            self.state = 233
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
            self.state = 235
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
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.constant()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.define_name()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(ASICParser.LPAREN)
                self.state = 240
                self.expression()
                self.state = 241
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
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 40, 84]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.primary_expression()
                pass
            elif token in [48, 49, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.unary_operator()
                self.state = 247
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
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 865535553385267200) != 0)):
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
            self.state = 253
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7881299347898368) != 0)):
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
            self.state = 255
            self.unary_expression()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7881299347898368) != 0):
                self.state = 256
                self.mulop()
                self.state = 257
                self.unary_expression()
                self.state = 263
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
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
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
            self.state = 266
            self.multiplicative_expression()
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 267
                    self.addop()
                    self.state = 268
                    self.multiplicative_expression() 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 275
            _la = self._input.LA(1)
            if not(((((_la - 43)) & ~0x3f) == 0 and ((1 << (_la - 43)) & 12582917) != 0)):
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
            self.state = 277
            self.additive_expression()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 43)) & ~0x3f) == 0 and ((1 << (_la - 43)) & 12582917) != 0):
                self.state = 278
                self.relop()
                self.state = 279
                self.additive_expression()
                self.state = 285
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
            self.state = 286
            _la = self._input.LA(1)
            if not(_la==63 or _la==64):
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
            self.state = 288
            self.relational_expression()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63 or _la==64:
                self.state = 289
                self.eqop()
                self.state = 290
                self.relational_expression()
                self.state = 296
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
            self.state = 297
            self.equality_expression()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 298
                self.match(ASICParser.AMP)
                self.state = 299
                self.equality_expression()
                self.state = 304
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
            self.state = 305
            self.and_expression()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 306
                self.match(ASICParser.CARET)
                self.state = 307
                self.and_expression()
                self.state = 312
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
            self.state = 313
            self.xor_expression()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==56:
                self.state = 314
                self.match(ASICParser.BAR)
                self.state = 315
                self.xor_expression()
                self.state = 320
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
            self.state = 321
            self.or_expression()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 322
                self.match(ASICParser.AMPAMP)
                self.state = 323
                self.or_expression()
                self.state = 328
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
            self.state = 329
            self.logicaland_expression()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 330
                self.match(ASICParser.BARBAR)
                self.state = 331
                self.logicaland_expression()
                self.state = 336
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
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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
            self.state = 341
            self.match(ASICParser.REV)
            self.state = 342
            self.match(ASICParser.LPAREN)
            self.state = 343
            self.configuration()
            self.state = 344
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
            self.state = 346
            self.conf_atom()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 347
                self.match(ASICParser.PLUS)
                self.state = 348
                self.conf_atom()
                self.state = 353
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
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 13, 14, 15, 16, 17, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.conf_d()
                pass
            elif token in [30, 84]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17]:
                self.state = 358
                self.vreg()
                pass
            elif token in [5, 33]:
                self.state = 359
                self.vreg_r()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 362
                self.match(ASICParser.LBRACE)
                self.state = 363
                self.expression()
                self.state = 364
                self.match(ASICParser.RBRACE)


            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 368
                self.match(ASICParser.LSHIFT)
                self.state = 369
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
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [84]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.const_name()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
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
            self.state = 376
            self.match(ASICParser.LBRACKET)
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 40, 48, 49, 58, 59, 84]:
                self.state = 377
                self.expression()
                pass
            elif token in [13, 15, 16, 17]:
                self.state = 378
                self.vreg_d()
                pass
            elif token in [5, 6, 7, 8]:
                self.state = 379
                self.sreg()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 382
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
            self.state = 384
            self.match(ASICParser.LSHIFT)
            self.state = 385
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
            self.state = 387
            self.match(ASICParser.SC)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 388
                self.const_addr()


            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 391
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
            self.state = 394
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4222124650659840) != 0)):
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
            self.state = 396
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
            self.state = 398
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
            self.state = 400
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
            self.state = 402
            self.match(ASICParser.LPAREN)
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 403
                self.config_name()
                pass

            elif la_ == 2:
                self.state = 404
                self.configuration()
                pass

            elif la_ == 3:
                self.state = 405
                self.rev_configuration()
                pass


            self.state = 408
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
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17, 74, 75, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.output()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(ASICParser.LPAREN)
                self.state = 412
                self.output()
                self.state = 415 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 413
                    self.match(ASICParser.COMMA)
                    self.state = 414
                    self.output()
                    self.state = 417 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==69):
                        break

                self.state = 419
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
            self.state = 423
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
            self.state = 425
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
            self.state = 427
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
            self.state = 429
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

        def REV_REG(self):
            return self.getToken(ASICParser.REV_REG, 0)

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
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(ASICParser.R0)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(ASICParser.REV_REG)
                self.state = 433
                self.match(ASICParser.LPAREN)
                self.state = 434
                self.match(ASICParser.R0)
                self.state = 435
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
            self.state = 438
            _la = self._input.LA(1)
            if not(_la==74 or _la==75):
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
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.vreg()
                pass
            elif token in [74, 75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.vreg_special()
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.match(ASICParser.CMP)
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
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

        def D_K64(self):
            return self.getToken(ASICParser.D_K64, 0)

        def DINV_K64(self):
            return self.getToken(ASICParser.DINV_K64, 0)

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
            self.state = 446
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1069547520) != 0)):
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
            self.state = 448
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 534723428352) != 0)):
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


    class EopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOP(self):
            return self.getToken(ASICParser.EOP, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_eop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEop" ):
                listener.enterEop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEop" ):
                listener.exitEop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEop" ):
                return visitor.visitEop(self)
            else:
                return visitor.visitChildren(self)




    def eop(self):

        localctx = ASICParser.EopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_eop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ASICParser.EOP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(ASICParser.WAIT, 0)

        def LPAREN(self):
            return self.getToken(ASICParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ASICParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ASICParser.RPAREN, 0)

        def getRuleIndex(self):
            return ASICParser.RULE_wait

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWait" ):
                listener.enterWait(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWait" ):
                listener.exitWait(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWait" ):
                return visitor.visitWait(self)
            else:
                return visitor.visitChildren(self)




    def wait(self):

        localctx = ASICParser.WaitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_wait)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(ASICParser.WAIT)
            self.state = 453
            self.match(ASICParser.LPAREN)
            self.state = 454
            self.expression()
            self.state = 455
            self.match(ASICParser.RPAREN)
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
        self.enterRule(localctx, 120, self.RULE_jump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(ASICParser.JNZ)
            self.state = 458
            self.match(ASICParser.LPAREN)
            self.state = 459
            self.sreg()
            self.state = 460
            self.match(ASICParser.COMMA)
            self.state = 461
            self.label()
            self.state = 462
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
        self.enterRule(localctx, 122, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.match(ASICParser.LINE_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





