import os, sys
import time
from pdb import pm

sys.path.append('/home/serpilliere/projet/m2_devel')
from miasm2.arch.mips32.arch import *

import sys


filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    execfile(filename)


reg_tests_mips32 = [
    ("004496D8    ADDU       GP, GP, T9",
     "0399E021"),
    ("004496DC    ADDIU      SP, SP, 0xFFFFFDA0",
     "27BDFDA0"),
    ("0449724     NOP        ",
     "00000000"),
    ('00449734    ADDIU      A0, ZERO, 0xA',
     "2404000A"),
    ('00400320    LUI        V1, 0x7FF0',
     "3C037FF0"),
    ('00400350    ORI        V1, V1, 0x1',
     "34630001"),
    ('00400304    SUBU       A0, ZERO, T1',
     "00092023"),
    ("0040031C    OR         A0, A0, T2",
     "008A2025"),
    ("00400344    AND        A1, A2, A1",
     "00C52824"),
    ("00400348    SRL        V0, V0, 0x1F",
     "000217C2"),
    ("00400354    SLTU       V0, V0, V1",
     "0043102B"),
    ("00400374    SRA        V0, T3, 0x1E",
     "000B1783"),
    ("004002F0    SW         RA, 0x1C(SP)",
     "AFBF001C"),
    ("XXXXXXXX    SW         RA, (SP)",
     "AFBF0000"),
    ("004002FC    MFC1       T1, F14",
     "44097000"),
    ("00400324    MOV.D      F0, F12",
     "46206006"),
    ("00400334    BNE        A0, ZERO, 0x28",
     "1480000A"),
    ("00400360    B          0x338",
     "100000CE"),
    ("00400378    LW         T9, 0xFFFF9C90(GP)",
     "8F999C90"),
    ("00400384    JR         T9",
     "03200008"),
    ("0040038C    ANDI       V0, V0, 0x2",
     "30420002"),
    ("00400364    ADD.D      F0, F0, F14",
     "462E0000"),
    ("004003A4    BEQ        S0, V0, 0x120",
     "12020048"),
    ("004003A8    SLTI       V0, S0, 0x3",
     "2A020003"),
    ("004005A4    BGEZ       T3, 0x20",
     "05610008"),
    ("00400428    LWC1       F0, 0x4344(V0)",
     "C4404344"),
    ("004005D0    JALR       T9, RA",
     "0320F809"),
    ("00400500    MTC1       ZERO, F0",
     "44800000"),
    ("004005D4    DIV.D      F12, F0, F14",
     "462E0303"),
    ("0040062C    XOR        V0, A2, A0",
     "00C41026"),
    ("00400684    SUB.D      F0, F12, F0",
     "46206001"),
    ("00400148    LBU        V0, 0xFFFF8880(S1)",
     "92228880"),
    ("004001C4    SB         V0, 0xFFFF8880(S1)",
     "A2228880"),
    ("00400274    BAL        0x4",
     "04110001"),
    ("0040073C    C.LT.D     FCC0, F0, F12",
     "462C003C"),
    ("00400744    BC1F       FCC0, 0x20",
     "45000008"),
    ("00403A80    BC1T       FCC0, 0xB4",
     "4501002D"),
    ("00400764    MUL.D      F12, F0, F0",
     "46200302"),
    ("004007C8    SLL        V1, A2, 0x3",
     "000618C0"),
    ("00400E28    SWC1       F26, 0x5C(SP)",
     "E7BA005C"),
    ("00400EA8    SLT        V0, V1, S2",
     "0072102A"),
    ("00400F30    SUBU       V0, V0, V1",
     "00431023"),
    ("00400F34    SRLV       V1, A1, V0",
     "00451806"),
    ("00400F38    SLLV       V0, V1, V0",
     "00431004"),
    ("00400F60    SRAV       V1, S3, V0",
     "00531807"),
    ("00401040    BLTZ       S6, 0x58",
     "06C00016"),
    ("00400D18    BLEZ       V1, 0x7C",
     "1860001F"),
    ("00401200    BGTZ       S4, 0x10",
     "1E800004"),
    ("004014A4    CVT.D.W    F8, F0",
     "46800221"),
    ("00400864    CVT.W.D    F0, F2",
     "46201024"),
    ("00401748    NOR        A3, ZERO, A3",
     "00073827"),
    ("00403E6C    BREAK      0x1C00",
     "0007000D"),
    ("00405744    SYSCALL    0x0",
     "0000000C"),
    ("004095A4    LH         V0, (V0)",
     "84420000"),
    ("0040ACBC    LB         V0, 0x1(A1)",
     "80A20001"),
    ("00412A34    DIV        A0, V1",
     "0083001A"),
    ("00419ED8    LWL        T0, (A1)",
     "88A80000"),
    ("00419FA4    LWL        T0, (A1)",
     "88A80000"),
    ("0041A024    SWL        A1, (A0)",
     "A8850000"),
    ("0044E194    SWR        V0, 0x3(A0)",
     "B8820003"),
    ("00433974    CVT.S.D    F0, F0",
     "46200020"),


    ("0044A120    MULT       V1, V0",
     "00620018"),
    ("00404194    MULTU      A1, V1",
     "00A30019"),
    ("00403E68    DIVU       V0, T1",
     "0049001B"),
    ("00403E70    MFLO       T4",
     "00006012"),
    ("004040CC    MFHI       A0",
     "00002010"),

    ("00401748    NOR        A3, ZERO, A3",
     "00073827"),

    ("8BA1025C    MTC0       T0, WATCHHI",
     "40889800"),
    ("8BA10260    MTC0       ZERO, WATCHHI",
     "40809800"),
    ("8BA10264    MTC0       ZERO, CAUSE",
     "40806800"),
    ("8BA0FD68    MTC0       V0, ENTRYLO0",
     "40821000"),
    ("8BA0FD70    MTC0       V0, ENTRYLO1",
     "40821800"),
    ("8BA0FD78    MTC0       V0, PAGEMASK",
     "40822800"),
    ("8BA0FD94    MTC0       V1, ENTRYHI",
     "40835000"),


    ("8BA0FDA8    MFC0       V0, INDEX",
     "40020000"),
    ("8BA10268    MFC0       T0, CONFIG",
     "40088000"),
    ("8BA0FBD4    MFC0       V0, COUNT",
     "40024800"),
    ("800001F8    EXT        V0, V1, 0x10, 0x3",
     "7C621400 "),

    ("80000318    J          0x1E0",
     "08000078"),

    ("8BA0F0C0    LHU        V1, 0x20(SP)",
     "97A30020"),

    ("8BA0F168    MUL        V0, V1, S0",
     "70701002"),
    ("8BA0F288    MOVN       A2, T0, V0",
     "0102300B"),

    ("8BA0F32C    XORI       V1, V1, 0x11",
     "38630011"),
    ("8BA0F37C    SEB        S6, V0",
     "7C02B420"),
    ("8BA0F468    DI         ZERO",
     "41606000"),
    ("8BA0F78C    WSBH       V1, V1",
     "7C0318A0"),
    ("8BA0F790    ROTR       V1, V1, 0x10",
     "00231C02"),

    ("8BA0F794    SLTIU      V0, V1, 0x5",
     "2C620005"),
    ("8BA0FDA0    TLBP       ",
     "42000008"),
    ("8BA0FDC0    TLBWI      ",
     "42000002"),
    ("8BA10124    INS        A0, A1, 0x0, 0x8",
     "7CA43804"),

    ("XXXXXXXX    MOVZ       S0, T1, A2",
     "0126800a"),
    ("XXXXXXXX    JAL        0x7C0B0AC",
     "0df02c2b"),

]


ts = time.time()
def h2i(s):
    return s.replace(' ', '').decode('hex')

for s, l in reg_tests_mips32:
    print "-" * 80
    s = s[12:]
    b = h2i((l))
    mn = mn_mips32.dis(b, 'b')
    print [str(x) for x in mn.args]
    print s
    print mn
    assert(str(mn) == s)
    # print hex(b)
    # print [str(x.get()) for x in mn.args]
    l = mn_mips32.fromstring(s, 'b')
    # print l
    assert(str(l) == s)
    a = mn_mips32.asm(l, 'b')
    print [x for x in a]
    print repr(b)
    # print mn.args
    assert(b in a)