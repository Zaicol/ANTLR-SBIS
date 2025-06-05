# Generated from ASICParser.g4 by ANTLR 4.13.2
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
        4,1,75,416,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,5,0,108,8,0,10,0,12,0,111,9,0,1,1,1,1,3,1,115,8,1,1,1,3,1,118,
        8,1,1,2,1,2,1,2,3,2,123,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,
        133,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,3,7,143,8,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,156,8,7,3,7,158,8,7,1,8,1,8,
        3,8,162,8,8,1,9,1,9,3,9,166,8,9,1,10,1,10,1,10,1,10,3,10,172,8,10,
        1,11,1,11,1,11,1,11,1,11,3,11,179,8,11,1,12,1,12,1,12,1,12,3,12,
        185,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,194,8,12,1,13,1,
        13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,207,8,15,1,
        16,1,16,1,16,1,16,3,16,213,8,16,1,17,1,17,1,18,1,18,1,19,1,19,1,
        19,1,19,5,19,223,8,19,10,19,12,19,226,9,19,1,20,1,20,1,21,1,21,1,
        21,1,21,5,21,234,8,21,10,21,12,21,237,9,21,1,22,1,22,1,23,1,23,1,
        23,1,23,5,23,245,8,23,10,23,12,23,248,9,23,1,24,1,24,1,25,1,25,1,
        25,1,25,5,25,256,8,25,10,25,12,25,259,9,25,1,26,1,26,1,26,5,26,264,
        8,26,10,26,12,26,267,9,26,1,27,1,27,1,27,5,27,272,8,27,10,27,12,
        27,275,9,27,1,28,1,28,1,28,5,28,280,8,28,10,28,12,28,283,9,28,1,
        29,1,29,1,29,5,29,288,8,29,10,29,12,29,291,9,29,1,30,1,30,1,30,5,
        30,296,8,30,10,30,12,30,299,9,30,1,31,1,31,3,31,303,8,31,1,32,1,
        32,1,32,1,32,1,32,1,33,1,33,1,33,5,33,313,8,33,10,33,12,33,316,9,
        33,1,34,1,34,3,34,320,8,34,1,35,1,35,3,35,324,8,35,1,35,1,35,1,35,
        1,35,3,35,330,8,35,1,35,1,35,3,35,334,8,35,1,36,1,36,3,36,338,8,
        36,1,37,1,37,1,37,1,37,1,37,1,37,3,37,346,8,37,1,38,1,38,1,39,1,
        39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,3,42,359,8,42,1,42,1,42,1,
        43,1,43,1,43,1,43,1,43,4,43,368,8,43,11,43,12,43,369,1,43,1,43,3,
        43,374,8,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,1,47,1,
        47,3,47,387,8,47,1,48,1,48,1,48,3,48,392,8,48,1,49,1,49,1,50,1,50,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,3,51,412,8,51,1,52,1,52,1,52,0,0,53,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,
        0,12,1,0,1,2,2,0,42,43,52,53,1,0,44,46,1,0,42,43,3,0,37,37,39,39,
        59,60,1,0,57,58,1,0,42,45,1,0,3,6,1,0,7,10,1,0,11,15,1,0,19,24,2,
        0,26,26,28,32,408,0,109,1,0,0,0,2,114,1,0,0,0,4,122,1,0,0,0,6,124,
        1,0,0,0,8,128,1,0,0,0,10,134,1,0,0,0,12,138,1,0,0,0,14,157,1,0,0,
        0,16,161,1,0,0,0,18,165,1,0,0,0,20,167,1,0,0,0,22,178,1,0,0,0,24,
        193,1,0,0,0,26,195,1,0,0,0,28,198,1,0,0,0,30,206,1,0,0,0,32,212,
        1,0,0,0,34,214,1,0,0,0,36,216,1,0,0,0,38,218,1,0,0,0,40,227,1,0,
        0,0,42,229,1,0,0,0,44,238,1,0,0,0,46,240,1,0,0,0,48,249,1,0,0,0,
        50,251,1,0,0,0,52,260,1,0,0,0,54,268,1,0,0,0,56,276,1,0,0,0,58,284,
        1,0,0,0,60,292,1,0,0,0,62,302,1,0,0,0,64,304,1,0,0,0,66,309,1,0,
        0,0,68,319,1,0,0,0,70,323,1,0,0,0,72,337,1,0,0,0,74,339,1,0,0,0,
        76,347,1,0,0,0,78,349,1,0,0,0,80,351,1,0,0,0,82,353,1,0,0,0,84,355,
        1,0,0,0,86,373,1,0,0,0,88,375,1,0,0,0,90,377,1,0,0,0,92,379,1,0,
        0,0,94,386,1,0,0,0,96,391,1,0,0,0,98,393,1,0,0,0,100,395,1,0,0,0,
        102,411,1,0,0,0,104,413,1,0,0,0,106,108,3,2,1,0,107,106,1,0,0,0,
        108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,1,1,0,0,0,111,
        109,1,0,0,0,112,115,3,4,2,0,113,115,3,14,7,0,114,112,1,0,0,0,114,
        113,1,0,0,0,115,117,1,0,0,0,116,118,3,104,52,0,117,116,1,0,0,0,117,
        118,1,0,0,0,118,3,1,0,0,0,119,123,3,6,3,0,120,123,3,8,4,0,121,123,
        3,10,5,0,122,119,1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,5,1,
        0,0,0,124,125,5,16,0,0,125,126,3,78,39,0,126,127,3,62,31,0,127,7,
        1,0,0,0,128,129,5,17,0,0,129,132,3,80,40,0,130,133,3,66,33,0,131,
        133,3,64,32,0,132,130,1,0,0,0,132,131,1,0,0,0,133,9,1,0,0,0,134,
        135,5,18,0,0,135,136,3,82,41,0,136,137,3,74,37,0,137,11,1,0,0,0,
        138,139,7,0,0,0,139,13,1,0,0,0,140,158,3,26,13,0,141,143,3,26,13,
        0,142,141,1,0,0,0,142,143,1,0,0,0,143,155,1,0,0,0,144,156,3,16,8,
        0,145,146,3,16,8,0,146,147,5,63,0,0,147,148,3,16,8,0,148,156,1,0,
        0,0,149,150,3,16,8,0,150,151,5,63,0,0,151,152,3,16,8,0,152,153,5,
        63,0,0,153,154,3,16,8,0,154,156,1,0,0,0,155,144,1,0,0,0,155,145,
        1,0,0,0,155,149,1,0,0,0,156,158,1,0,0,0,157,140,1,0,0,0,157,142,
        1,0,0,0,158,15,1,0,0,0,159,162,3,18,9,0,160,162,3,24,12,0,161,159,
        1,0,0,0,161,160,1,0,0,0,162,17,1,0,0,0,163,166,3,20,10,0,164,166,
        3,22,11,0,165,163,1,0,0,0,165,164,1,0,0,0,166,19,1,0,0,0,167,168,
        3,88,44,0,168,171,5,54,0,0,169,172,3,62,31,0,170,172,3,90,45,0,171,
        169,1,0,0,0,171,170,1,0,0,0,172,21,1,0,0,0,173,174,5,3,0,0,174,179,
        5,61,0,0,175,176,3,88,44,0,176,177,5,62,0,0,177,179,1,0,0,0,178,
        173,1,0,0,0,178,175,1,0,0,0,179,23,1,0,0,0,180,181,3,86,43,0,181,
        184,5,54,0,0,182,185,3,100,50,0,183,185,3,98,49,0,184,182,1,0,0,
        0,184,183,1,0,0,0,185,186,1,0,0,0,186,187,3,84,42,0,187,194,1,0,
        0,0,188,189,3,86,43,0,189,190,5,54,0,0,190,191,3,102,51,0,191,194,
        1,0,0,0,192,194,3,102,51,0,193,180,1,0,0,0,193,188,1,0,0,0,193,192,
        1,0,0,0,194,25,1,0,0,0,195,196,3,28,14,0,196,197,5,64,0,0,197,27,
        1,0,0,0,198,199,5,73,0,0,199,29,1,0,0,0,200,207,3,12,6,0,201,207,
        3,78,39,0,202,203,5,34,0,0,203,204,3,62,31,0,204,205,5,35,0,0,205,
        207,1,0,0,0,206,200,1,0,0,0,206,201,1,0,0,0,206,202,1,0,0,0,207,
        31,1,0,0,0,208,213,3,30,15,0,209,210,3,34,17,0,210,211,3,32,16,0,
        211,213,1,0,0,0,212,208,1,0,0,0,212,209,1,0,0,0,213,33,1,0,0,0,214,
        215,7,1,0,0,215,35,1,0,0,0,216,217,7,2,0,0,217,37,1,0,0,0,218,224,
        3,32,16,0,219,220,3,36,18,0,220,221,3,32,16,0,221,223,1,0,0,0,222,
        219,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,
        39,1,0,0,0,226,224,1,0,0,0,227,228,7,3,0,0,228,41,1,0,0,0,229,235,
        3,38,19,0,230,231,3,40,20,0,231,232,3,38,19,0,232,234,1,0,0,0,233,
        230,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,
        43,1,0,0,0,237,235,1,0,0,0,238,239,7,4,0,0,239,45,1,0,0,0,240,246,
        3,42,21,0,241,242,3,44,22,0,242,243,3,42,21,0,243,245,1,0,0,0,244,
        241,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,
        47,1,0,0,0,248,246,1,0,0,0,249,250,7,5,0,0,250,49,1,0,0,0,251,257,
        3,46,23,0,252,253,3,48,24,0,253,254,3,46,23,0,254,256,1,0,0,0,255,
        252,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,
        51,1,0,0,0,259,257,1,0,0,0,260,265,3,50,25,0,261,262,5,48,0,0,262,
        264,3,50,25,0,263,261,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,
        266,1,0,0,0,266,53,1,0,0,0,267,265,1,0,0,0,268,273,3,52,26,0,269,
        270,5,47,0,0,270,272,3,52,26,0,271,269,1,0,0,0,272,275,1,0,0,0,273,
        271,1,0,0,0,273,274,1,0,0,0,274,55,1,0,0,0,275,273,1,0,0,0,276,281,
        3,54,27,0,277,278,5,50,0,0,278,280,3,54,27,0,279,277,1,0,0,0,280,
        283,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,57,1,0,0,0,283,281,
        1,0,0,0,284,289,3,56,28,0,285,286,5,49,0,0,286,288,3,56,28,0,287,
        285,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,
        59,1,0,0,0,291,289,1,0,0,0,292,297,3,58,29,0,293,294,5,51,0,0,294,
        296,3,58,29,0,295,293,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,
        298,1,0,0,0,298,61,1,0,0,0,299,297,1,0,0,0,300,303,3,12,6,0,301,
        303,3,60,30,0,302,300,1,0,0,0,302,301,1,0,0,0,303,63,1,0,0,0,304,
        305,5,27,0,0,305,306,5,34,0,0,306,307,3,66,33,0,307,308,5,35,0,0,
        308,65,1,0,0,0,309,314,3,68,34,0,310,311,5,42,0,0,311,313,3,68,34,
        0,312,310,1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,
        0,315,67,1,0,0,0,316,314,1,0,0,0,317,320,3,70,35,0,318,320,3,72,
        36,0,319,317,1,0,0,0,319,318,1,0,0,0,320,69,1,0,0,0,321,324,3,92,
        46,0,322,324,3,94,47,0,323,321,1,0,0,0,323,322,1,0,0,0,324,329,1,
        0,0,0,325,326,5,40,0,0,326,327,3,62,31,0,327,328,5,41,0,0,328,330,
        1,0,0,0,329,325,1,0,0,0,329,330,1,0,0,0,330,333,1,0,0,0,331,332,
        5,55,0,0,332,334,3,62,31,0,333,331,1,0,0,0,333,334,1,0,0,0,334,71,
        1,0,0,0,335,338,3,82,41,0,336,338,3,74,37,0,337,335,1,0,0,0,337,
        336,1,0,0,0,338,73,1,0,0,0,339,340,5,25,0,0,340,341,5,36,0,0,341,
        342,3,62,31,0,342,345,5,38,0,0,343,344,5,55,0,0,344,346,3,62,31,
        0,345,343,1,0,0,0,345,346,1,0,0,0,346,75,1,0,0,0,347,348,7,6,0,0,
        348,77,1,0,0,0,349,350,5,73,0,0,350,79,1,0,0,0,351,352,5,73,0,0,
        352,81,1,0,0,0,353,354,5,73,0,0,354,83,1,0,0,0,355,358,5,34,0,0,
        356,359,3,80,40,0,357,359,3,66,33,0,358,356,1,0,0,0,358,357,1,0,
        0,0,359,360,1,0,0,0,360,361,5,35,0,0,361,85,1,0,0,0,362,374,3,96,
        48,0,363,364,5,34,0,0,364,367,3,96,48,0,365,366,5,63,0,0,366,368,
        3,96,48,0,367,365,1,0,0,0,368,369,1,0,0,0,369,367,1,0,0,0,369,370,
        1,0,0,0,370,371,1,0,0,0,371,372,5,35,0,0,372,374,1,0,0,0,373,362,
        1,0,0,0,373,363,1,0,0,0,374,87,1,0,0,0,375,376,7,7,0,0,376,89,1,
        0,0,0,377,378,7,8,0,0,378,91,1,0,0,0,379,380,7,9,0,0,380,93,1,0,
        0,0,381,387,5,3,0,0,382,383,5,27,0,0,383,384,5,34,0,0,384,385,5,
        3,0,0,385,387,5,35,0,0,386,381,1,0,0,0,386,382,1,0,0,0,387,95,1,
        0,0,0,388,392,3,92,46,0,389,392,5,67,0,0,390,392,5,68,0,0,391,388,
        1,0,0,0,391,389,1,0,0,0,391,390,1,0,0,0,392,97,1,0,0,0,393,394,7,
        10,0,0,394,99,1,0,0,0,395,396,7,11,0,0,396,101,1,0,0,0,397,412,5,
        69,0,0,398,412,5,70,0,0,399,400,5,71,0,0,400,401,5,34,0,0,401,402,
        3,62,31,0,402,403,5,35,0,0,403,412,1,0,0,0,404,405,5,72,0,0,405,
        406,5,34,0,0,406,407,3,88,44,0,407,408,5,63,0,0,408,409,3,28,14,
        0,409,410,5,35,0,0,410,412,1,0,0,0,411,397,1,0,0,0,411,398,1,0,0,
        0,411,399,1,0,0,0,411,404,1,0,0,0,412,103,1,0,0,0,413,414,5,75,0,
        0,414,105,1,0,0,0,39,109,114,117,122,132,142,155,157,161,165,171,
        178,184,193,206,212,224,235,246,257,265,273,281,289,297,302,314,
        319,323,329,333,337,345,358,369,373,386,391,411
    ]

class ASICParser ( Parser ):

    grammarFileName = "ASICParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'$0'", "'$1'", 
                     "'$2'", "'$3'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "'<'", "']'", "'>'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'&'", "'&&'", 
                     "'|'", "'||'", "'!'", "'~'", "'='", "'<<'", "'>>'", 
                     "'=='", "'!='", "'<='", "'>='", "'++'", "'--'", "','", 
                     "':'", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "HEXADECIMAL", "DECIMAL", "R0", "R1", 
                      "R2", "R3", "ARG0", "ARG1", "ARG2", "ARG3", "V1", 
                      "V1H", "V2", "V3", "V4", "DEFINE", "CONFIG", "CONST", 
                      "A1", "A4", "A5", "A128D", "DINV", "SD", "SC", "ID", 
                      "REV", "INV", "AND", "OR", "XOR", "NOT", "EOL", "LPAREN", 
                      "RPAREN", "LBRACKET", "LABRACKET", "RBRACKET", "RABRACKET", 
                      "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", "DIV", 
                      "MOD", "CARET", "AMP", "AMPAMP", "BAR", "BARBAR", 
                      "NEG", "TILDE", "ASSIGN", "LSHIFT", "RSHIFT", "EQUAL", 
                      "NEQUAL", "LEQUAL", "GEQUAL", "PLUSPLUS", "MINUSMINUS", 
                      "COMMA", "COLON", "SEMI", "DOT", "CMP", "OUT", "GEN", 
                      "EOP", "WAIT", "JNZ", "IDENTIFIER", "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_definition = 2
    RULE_define_def = 3
    RULE_config_def = 4
    RULE_const_def = 5
    RULE_constant = 6
    RULE_statement = 7
    RULE_instruction = 8
    RULE_sregop = 9
    RULE_asignment = 10
    RULE_arith = 11
    RULE_operator = 12
    RULE_lbl = 13
    RULE_label = 14
    RULE_primary_expression = 15
    RULE_unary_expression = 16
    RULE_unary_operator = 17
    RULE_mulop = 18
    RULE_multiplicative_expression = 19
    RULE_addop = 20
    RULE_additive_expression = 21
    RULE_relop = 22
    RULE_relational_expression = 23
    RULE_eqop = 24
    RULE_equality_expression = 25
    RULE_and_expression = 26
    RULE_xor_expression = 27
    RULE_or_expression = 28
    RULE_logicaland_expression = 29
    RULE_logicalor_expression = 30
    RULE_expression = 31
    RULE_rev_configuration = 32
    RULE_configuration = 33
    RULE_conf_atom = 34
    RULE_conf_d = 35
    RULE_conf_c = 36
    RULE_const_expr = 37
    RULE_op = 38
    RULE_define_name = 39
    RULE_config_name = 40
    RULE_const_name = 41
    RULE_argument = 42
    RULE_resultexpr = 43
    RULE_sreg = 44
    RULE_arg = 45
    RULE_vreg = 46
    RULE_vreg_r = 47
    RULE_output = 48
    RULE_stdop = 49
    RULE_aluop = 50
    RULE_spcop = 51
    RULE_comment = 52

    ruleNames =  [ "prog", "line", "definition", "define_def", "config_def", 
                   "const_def", "constant", "statement", "instruction", 
                   "sregop", "asignment", "arith", "operator", "lbl", "label", 
                   "primary_expression", "unary_expression", "unary_operator", 
                   "mulop", "multiplicative_expression", "addop", "additive_expression", 
                   "relop", "relational_expression", "eqop", "equality_expression", 
                   "and_expression", "xor_expression", "or_expression", 
                   "logicaland_expression", "logicalor_expression", "expression", 
                   "rev_configuration", "configuration", "conf_atom", "conf_d", 
                   "conf_c", "const_expr", "op", "define_name", "config_name", 
                   "const_name", "argument", "resultexpr", "sreg", "arg", 
                   "vreg", "vreg_r", "output", "stdop", "aluop", "spcop", 
                   "comment" ]

    EOF = Token.EOF
    HEXADECIMAL=1
    DECIMAL=2
    R0=3
    R1=4
    R2=5
    R3=6
    ARG0=7
    ARG1=8
    ARG2=9
    ARG3=10
    V1=11
    V1H=12
    V2=13
    V3=14
    V4=15
    DEFINE=16
    CONFIG=17
    CONST=18
    A1=19
    A4=20
    A5=21
    A128D=22
    DINV=23
    SD=24
    SC=25
    ID=26
    REV=27
    INV=28
    AND=29
    OR=30
    XOR=31
    NOT=32
    EOL=33
    LPAREN=34
    RPAREN=35
    LBRACKET=36
    LABRACKET=37
    RBRACKET=38
    RABRACKET=39
    LBRACE=40
    RBRACE=41
    PLUS=42
    MINUS=43
    STAR=44
    DIV=45
    MOD=46
    CARET=47
    AMP=48
    AMPAMP=49
    BAR=50
    BARBAR=51
    NEG=52
    TILDE=53
    ASSIGN=54
    LSHIFT=55
    RSHIFT=56
    EQUAL=57
    NEQUAL=58
    LEQUAL=59
    GEQUAL=60
    PLUSPLUS=61
    MINUSMINUS=62
    COMMA=63
    COLON=64
    SEMI=65
    DOT=66
    CMP=67
    OUT=68
    GEN=69
    EOP=70
    WAIT=71
    JNZ=72
    IDENTIFIER=73
    WS=74
    LINE_COMMENT=75

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
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17180391544) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 127) != 0):
                self.state = 106
                self.line()
                self.state = 111
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
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 18]:
                self.state = 112
                self.definition()
                pass
            elif token in [3, 4, 5, 6, 11, 12, 13, 14, 15, 34, 67, 68, 69, 70, 71, 72, 73]:
                self.state = 113
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==75:
                self.state = 116
                self.comment()


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
        self.enterRule(localctx, 4, self.RULE_definition)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.define_def()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.config_def()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
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
        self.enterRule(localctx, 6, self.RULE_define_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ASICParser.DEFINE)
            self.state = 125
            self.define_name()
            self.state = 126
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
        self.enterRule(localctx, 8, self.RULE_config_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ASICParser.CONFIG)
            self.state = 129
            self.config_name()
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 130
                self.configuration()
                pass

            elif la_ == 2:
                self.state = 131
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
        self.enterRule(localctx, 10, self.RULE_const_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ASICParser.CONST)
            self.state = 135
            self.const_name()
            self.state = 136
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
        self.enterRule(localctx, 12, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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

        def lbl(self):
            return self.getTypedRuleContext(ASICParser.LblContext,0)


        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.InstructionContext)
            else:
                return self.getTypedRuleContext(ASICParser.InstructionContext,i)


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
        self.enterRule(localctx, 14, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.lbl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==73:
                    self.state = 141
                    self.lbl()


                self.state = 155
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.instruction()
                    pass

                elif la_ == 2:
                    self.state = 145
                    self.instruction()
                    self.state = 146
                    self.match(ASICParser.COMMA)
                    self.state = 147
                    self.instruction()
                    pass

                elif la_ == 3:
                    self.state = 149
                    self.instruction()
                    self.state = 150
                    self.match(ASICParser.COMMA)
                    self.state = 151
                    self.instruction()
                    self.state = 152
                    self.match(ASICParser.COMMA)
                    self.state = 153
                    self.instruction()
                    pass


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
        self.enterRule(localctx, 16, self.RULE_instruction)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.sregop()
                pass
            elif token in [11, 12, 13, 14, 15, 34, 67, 68, 69, 70, 71, 72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
        self.enterRule(localctx, 18, self.RULE_sregop)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.asignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
        self.enterRule(localctx, 20, self.RULE_asignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.sreg()
            self.state = 168
            self.match(ASICParser.ASSIGN)
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 34, 42, 43, 52, 53, 73]:
                self.state = 169
                self.expression()
                pass
            elif token in [7, 8, 9, 10]:
                self.state = 170
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
        self.enterRule(localctx, 22, self.RULE_arith)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(ASICParser.R0)
                self.state = 174
                self.match(ASICParser.PLUSPLUS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.sreg()
                self.state = 176
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



    def operator(self):

        localctx = ASICParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operator)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ASICParser.AluSpOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.resultexpr()
                self.state = 181
                self.match(ASICParser.ASSIGN)
                self.state = 184
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 28, 29, 30, 31, 32]:
                    self.state = 182
                    self.aluop()
                    pass
                elif token in [19, 20, 21, 22, 23, 24]:
                    self.state = 183
                    self.stdop()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 186
                self.argument()
                pass

            elif la_ == 2:
                localctx = ASICParser.SpCopOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.resultexpr()
                self.state = 189
                self.match(ASICParser.ASSIGN)
                self.state = 190
                self.spcop()
                pass

            elif la_ == 3:
                localctx = ASICParser.SpCopOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.spcop()
                pass


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
        self.enterRule(localctx, 26, self.RULE_lbl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.label()
            self.state = 196
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
        self.enterRule(localctx, 28, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 30, self.RULE_primary_expression)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.constant()
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.define_name()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(ASICParser.LPAREN)
                self.state = 203
                self.expression()
                self.state = 204
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
        self.enterRule(localctx, 32, self.RULE_unary_expression)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 34, 73]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.primary_expression()
                pass
            elif token in [42, 43, 52, 53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.unary_operator()
                self.state = 210
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
        self.enterRule(localctx, 34, self.RULE_unary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13523993021644800) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_multiplicative_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.unary_expression()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0):
                self.state = 219
                self.mulop()
                self.state = 220
                self.unary_expression()
                self.state = 226
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
        self.enterRule(localctx, 40, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
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
        self.enterRule(localctx, 42, self.RULE_additive_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.multiplicative_expression()
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    self.addop()
                    self.state = 231
                    self.multiplicative_expression() 
                self.state = 237
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
        self.enterRule(localctx, 44, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382944105037824) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_relational_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.additive_expression()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1729382944105037824) != 0):
                self.state = 241
                self.relop()
                self.state = 242
                self.additive_expression()
                self.state = 248
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
        self.enterRule(localctx, 48, self.RULE_eqop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==57 or _la==58):
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
        self.enterRule(localctx, 50, self.RULE_equality_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.relational_expression()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57 or _la==58:
                self.state = 252
                self.eqop()
                self.state = 253
                self.relational_expression()
                self.state = 259
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
        self.enterRule(localctx, 52, self.RULE_and_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.equality_expression()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 261
                self.match(ASICParser.AMP)
                self.state = 262
                self.equality_expression()
                self.state = 267
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
        self.enterRule(localctx, 54, self.RULE_xor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.and_expression()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 269
                self.match(ASICParser.CARET)
                self.state = 270
                self.and_expression()
                self.state = 275
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
        self.enterRule(localctx, 56, self.RULE_or_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.xor_expression()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 277
                self.match(ASICParser.BAR)
                self.state = 278
                self.xor_expression()
                self.state = 283
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
        self.enterRule(localctx, 58, self.RULE_logicaland_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.or_expression()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 285
                self.match(ASICParser.AMPAMP)
                self.state = 286
                self.or_expression()
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
        self.enterRule(localctx, 60, self.RULE_logicalor_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.logicaland_expression()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 293
                self.match(ASICParser.BARBAR)
                self.state = 294
                self.logicaland_expression()
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
        self.enterRule(localctx, 62, self.RULE_expression)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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
        self.enterRule(localctx, 64, self.RULE_rev_configuration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ASICParser.REV)
            self.state = 305
            self.match(ASICParser.LPAREN)
            self.state = 306
            self.configuration()
            self.state = 307
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
        self.enterRule(localctx, 66, self.RULE_configuration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.conf_atom()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 310
                self.match(ASICParser.PLUS)
                self.state = 311
                self.conf_atom()
                self.state = 316
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
        self.enterRule(localctx, 68, self.RULE_conf_atom)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 11, 12, 13, 14, 15, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.conf_d()
                pass
            elif token in [25, 73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
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
        self.enterRule(localctx, 70, self.RULE_conf_d)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15]:
                self.state = 321
                self.vreg()
                pass
            elif token in [3, 27]:
                self.state = 322
                self.vreg_r()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 325
                self.match(ASICParser.LBRACE)
                self.state = 326
                self.expression()
                self.state = 327
                self.match(ASICParser.RBRACE)


            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 331
                self.match(ASICParser.LSHIFT)
                self.state = 332
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
        self.enterRule(localctx, 72, self.RULE_conf_c)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [73]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.const_name()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
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


    class Const_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SC(self):
            return self.getToken(ASICParser.SC, 0)

        def LBRACKET(self):
            return self.getToken(ASICParser.LBRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ASICParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ASICParser.ExpressionContext,i)


        def RBRACKET(self):
            return self.getToken(ASICParser.RBRACKET, 0)

        def LSHIFT(self):
            return self.getToken(ASICParser.LSHIFT, 0)

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
        self.enterRule(localctx, 74, self.RULE_const_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ASICParser.SC)
            self.state = 340
            self.match(ASICParser.LBRACKET)
            self.state = 341
            self.expression()
            self.state = 342
            self.match(ASICParser.RBRACKET)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 343
                self.match(ASICParser.LSHIFT)
                self.state = 344
                self.expression()


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
        self.enterRule(localctx, 76, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65970697666560) != 0)):
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
        self.enterRule(localctx, 78, self.RULE_define_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
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
        self.enterRule(localctx, 80, self.RULE_config_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
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
        self.enterRule(localctx, 82, self.RULE_const_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
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
        self.enterRule(localctx, 84, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ASICParser.LPAREN)
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 356
                self.config_name()
                pass

            elif la_ == 2:
                self.state = 357
                self.configuration()
                pass


            self.state = 360
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
        self.enterRule(localctx, 86, self.RULE_resultexpr)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15, 67, 68]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.output()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(ASICParser.LPAREN)
                self.state = 364
                self.output()
                self.state = 367 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 365
                    self.match(ASICParser.COMMA)
                    self.state = 366
                    self.output()
                    self.state = 369 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==63):
                        break

                self.state = 371
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
        self.enterRule(localctx, 88, self.RULE_sreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
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
        self.enterRule(localctx, 90, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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
        self.enterRule(localctx, 92, self.RULE_vreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
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
        self.enterRule(localctx, 94, self.RULE_vreg_r)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ASICParser.R0)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(ASICParser.REV)
                self.state = 383
                self.match(ASICParser.LPAREN)
                self.state = 384
                self.match(ASICParser.R0)
                self.state = 385
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


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vreg(self):
            return self.getTypedRuleContext(ASICParser.VregContext,0)


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
        self.enterRule(localctx, 96, self.RULE_output)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.vreg()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(ASICParser.CMP)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
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
        self.enterRule(localctx, 98, self.RULE_stdop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
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
        self.enterRule(localctx, 100, self.RULE_aluop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8388608000) != 0)):
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

        def JNZ(self):
            return self.getToken(ASICParser.JNZ, 0)

        def sreg(self):
            return self.getTypedRuleContext(ASICParser.SregContext,0)


        def COMMA(self):
            return self.getToken(ASICParser.COMMA, 0)

        def label(self):
            return self.getTypedRuleContext(ASICParser.LabelContext,0)


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
        self.enterRule(localctx, 102, self.RULE_spcop)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ASICParser.GEN)
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(ASICParser.EOP)
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(ASICParser.WAIT)
                self.state = 400
                self.match(ASICParser.LPAREN)
                self.state = 401
                self.expression()
                self.state = 402
                self.match(ASICParser.RPAREN)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.match(ASICParser.JNZ)
                self.state = 405
                self.match(ASICParser.LPAREN)
                self.state = 406
                self.sreg()
                self.state = 407
                self.match(ASICParser.COMMA)
                self.state = 408
                self.label()
                self.state = 409
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
        self.enterRule(localctx, 104, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(ASICParser.LINE_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





