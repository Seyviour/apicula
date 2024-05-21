# These constants are used to interact with the 'logicinfo', 'shortval' and maybe 'longval' tables
# * - it seems that these attributes must always be present (XXX)
# Warning:
# - the names assigned to constants are not exact correspondence with the primitive parameter names
# - some constants are for internal use only
# - not all attribute values have names because for example naming all values from 0 to 63 is tedious.
iob_attrids = {
        'IO_TYPE':               0,
        'SLEWRATE':              1, # *
        'PULLMODE':              2, # *
        'DRIVE':                 3, # *
        'OPENDRAIN':             4, # *
        'HYSTERESIS':            5, # *
        'CLAMP':                 6, # *
        'DIFFRESISTOR':          7, # *
        'SINGLERESISTOR':        8, # *
        'VREF':                  9, # *
        'VCCIO':                 10,
        'DIFFDRIVE':             11,
        'I3C_MODE':              12,
        'MIPI_INPUT':            13,
        'MIPI_OUTPUT':           14,
        'DRIVE_LEVEL':           15,
        'LVDS_OUT':              16, # *
        'LVDS_VCCIO':            17,
        'DDR_DYNTERM':           18,
        'IO_BANK':               19, # *
        'PERSISTENT':            20, # *
        'TO':                    21,
        'ODMUX':                 22,
        'ODMUX_1':               23,
        'PADDI':                 24,
        'PG_MUX':                25,
        'DATA_MUX':              26,
        'TRI_MUX':               27,
        'TRIMUX_PADDT':          28,
        'IOBUF_PADDI':           29,
        'USED':                  30, # *
        'IOBUF_OVERDRIVE':       31,
        'IOBUF_UNDERDRIVE':      32,
        'IOBUF_LVDS25_VCCIO':    33,
        'IN12_MODE':             34,
        'OD':                    35,
        'LPRX_A1':               36,
        'LPRX_A2':               37,
        'MIPI':                  38,
        'LVDS_SEL':              39,
        'VLDS_ON':               40,
        'IOBUF_MIPI_LP':         41,
        'IOBUF_ODT_RESISTOR':    42,
        'IOBUF_CIB_CONTROL':     43,
        'IOBUF_INR_MODE':        44,
        'IOBUF_STDBY_LVDS_MODE': 45,
        'IOBUF_IODUTY':          46,
        'IOBUF_ODT_DYNTERM':     47,
        'MIPI_IBUF_DRIVE':       48,
        'MIPI_IBUF_DRIVE_LEVEL': 49
        }

iob_attrvals = {
            'UNKNOWN':          0, # possible a dummy value for line 0 in logicinfo?
            # standard
            'MIPI':             1,
            'BLVDS25E':         2,
            'BLVDS25':          3,
            'BLVDS_E':          4,
            'HSTL':             5,
            'HSTL_D':           6,
            'HSTL15_I':         7,
            'HSTL15D_I':        8,
            'HSTL18_I':         9,
            'HSTL18_II':        10,
            'HSTL18D_I':        11,
            'HSTL18D_II':       12,
            'SSTL':             13,
            'SSTL_D':           14,
            'SSTL15':           15,
            'SSTL15D':          16,
            'SSTL18_I':         17,
            'SSTL18_II':        18,
            'SSTL18D_I':        19,
            'SSTL18D_II':       20,
            'SSTL25_I':         21,
            'SSTL25_II':        22,
            'SSTL25D_I':        23,
            'SSTL25D_II':       24,
            'SSTL33_I':         25,
            'SSTL33_II':        26,
            'SSTL33D_I':        27,
            'SSTL33D_II':       28,
            'LVCMOS12':         29,
            'LVCMOS15':         30,
            'LVCMOS18':         31,
            'LVCMOS25':         32,
            'LVCMOS33':         33,
            'LVCMOS_D':         34,
            'LVCMOS12D':        35,
            'LVCMOS15D':        36,
            'LVCMOS18D':        37,
            'LVCMOS25D':        38,
            'LVCMOS33D':        39,
            'LVDS':             40,
            'LVDS_E':           41,
            'LVDS25':           42,
            'LVDS25E':          43,
            'LVPECL33':         44,
            'LVPECL33E':        45,
            'LVTTL33':          46,
            'MLVDS25':          47,
            'MLVDS_E':          48,
            'MLVDS25E':         49,
            'RSDS25E':          50,
            'PCI33':            51,
            'RSDS':             52,
            'RSDS25':           53,
            'RSDS_E':           54,
            'MINILVDS':         55,
            'PPLVDS':           56,
            # vref
            'VREF1_DRIVER':     57,
            'VREF2_DRIVER':     58,
            #
            'LVCMOS33OD25':     59,
            'LVCMOS33OD18':     60,
            'LVCMOS33OD15':     61,
            'LVCMOS25OD18':     62,
            'LVCMOS25OD15':     63,
            'LVCMOS18OD15':     64,
            'LVCMOS15OD12':     65,
            'LVCMOS25UD33':     66,
            'LVCMOS18UD25':     67,
            'LVCMOS18UD33':     68,
            'LVCMOS15UD18':     69,
            'LVCMOS15UD25':     70,
            'LVCMOS15UD33':     71,
            'LVCMOS12UD15':     72,
            'LVCMOS12UD18':     73,
            'LVCMOS12UD25':     74,
            'LVCMOS12UD33':     75,
            'VREF1_LOAD':       76,
            'VREF2_LOAD':       77,
            #
            'ENABLE':           78,
            'TRIMUX':           79,
            'PADDI':            80,
            'PGBUF':            81,
            '0':                82,
            '1':                83,
            'SIG':              84,
            'INV':              85,
            'TO':               86,
            # voltage
            '1.2':              87,
            '1.25':             88,
            '1.5':              89,
            '1.8':              90,
            '2.0':              91,
            '2.5':              92,
            '3.3':              93,
            '3.5':              94,
            # mA
            '2':                95,
            '4':                96,
            '6':                97,
            '8':                98,
            '12':               99,
            '16':               100,
            '20':               101,
            '24':               102,
            # XXX ?
            '80':               103,
            '100':              104,
            '120':              105,
            #
            'NA':               106,
            'ON':               107,
            'OFF':              108,
            # XXX
            'PCI':              109,
            # histeresis
            'HIGH':             110,
            'H2L':              111,
            'L2H':              112,
            # pullmode
            'DOWN':             113,
            'KEEPER':           114,
            'NONE':             115,
            'UP':               116,
            # slew
            'FAST':             117,
            'SLOW':             118,
            # ?IO_BANK?
            'I45':              119,
            'I50':              120,
            'I55':              121,
            'TSREG':            122,
            'TMDDR':            123,
            'OD1':              124,
            'OD2':              125,
            'OD3':              126,
            'UD1':              127,
            'UD3':              128,
            # resistor?
            'INTERNAL':         129,
            'SINGLE':           130,
            'DIFF':             131,
            #
            'IN12':             132,
            'UD2':              133,
            'LVPECL_E':         134,
            #
            '68':               135,
            '3':                136,
            '5':                137,
            '7':                138,
            '9':                139,
            '10':               140,
            '11':               141,
            '4.5':              142,
            'MIPI_IBUF':        143,
            '1.35':             144,
            '5.5':              145,
            '6.5':              146,
            '10.5':             147,
            '13.5':             148,
            '14':               149,
            # more standard
            'TMDS33':           150,
            'LPDDR':            151,
            'HSUL12':           152,
            'HSUL12D':          153,
            'HSTL12_I':         154,
            'HSTL15_II':        155,
            'HSTL15D_II':       156,
            'SSTL12':           157,
            'SSTL135':          158,
            'SSTL135D':         159,
            'LVCMOS10':         160,
            'LVCMOS33OD12':     161,
            'LVCMOS25OD12':     162,
            'LVCMOS18OD12':     163,
        }

# ADC
adc_attrids = {
        'EN':               0,
        'VCCX':             1,
        'IOVREF':           2,
        'VREF':             3,
        'USED_FLAG':        4,
    }

adc_attrvals = {
        'UNKNOWN':          0,
        'ENABLE':           1,
        '3.3':              2,
        '2.80':             3,
        '2.55':             4,
        '2.39':             5,
        '2.23':             6,
        '1.81':             7,
        '1.65':             8,
        '2.5':              9,
        '2.12':             10,
        '1.94':             11,
        '1.69':             12,
        '1.37':             13,
        '1.25':             14,
        '1.8':              15,
        '1.53':             16,
        '1.39':             17,
        '1.30':             18,
        '1.21':             19,
        '0.99':             20,
        '0.9':              21,
        'ON':               22
    }


# BSRAM
bsram_attrids = {
        'CEMUX_CEA':        0,
        'CEMUX_CEB':        1,
        'CLKMUX_CLKA':      2,
        'CLKMUX_CLKB':      3,
        'CSA2':             4,
        'CSA_0':            5,
        'CSA_1':            6,
        'CSA_2':            7,
        'CSB2':             8,
        'CSB_0':            9,
        'CSB_1':            10,
        'CSB_2':            11,
        'DBLWA':            12,
        'DBLWB':            13,
        'GSR':              14,
        'MODE':             15,
        'OUTREG_ASYNC':     16,
        'OUTREG_CEA':       17,
        'OUTREG_CEB':       18,
        'PORTB_IBEH':       19,
        'REGSET_RSTA':      20,
        'REGSET_RSTB':      21,
        'REGSET_WEB':       22,
        'SYNC':             23,
        'WEMUX_WEA':        24,
        'WEMUX_WEB':        25,
        'DPA_DATA_WIDTH':   26,
        'DPB_DATA_WIDTH':   27,
        'DPA_BEHB':         28,
        'DPA_BELB':         29,
        'DPA_MODE':         30,
        'DPA_REGMODE':      31,
        'DPB_BEHB':         32,
        'DPB_BELB':         33,
        'DPB_MODE':         34,
        'DPB_REGMODE':      35,
        'SDPA_DATA_WIDTH':  36,
        'SDPB_DATA_WIDTH':  37,
        'SDPA_BEHB':        38,
        'SDPA_BELB':        39,
        'SDPA_MODE':        40,
        'SDPA_REGMODE':     41,
        'SDPB_BEHB':        42,
        'SDPB_BELB':        43,
        'SDPB_MODE':        44,
        'SDPB_REGMODE':     45,
        'SPA_DATA_WIDTH':   46,
        'SPB_DATA_WIDTH':   47,
        'SPA_BEHB':         48,
        'SPA_BELB':         49,
        'SPB_BEHB':         50,
        'SPB_BELB':         51,
        'SPA_MODE':         52,
        'SPA_REGMODE':      53,
        'SPB_MODE':         54,
        'SPB_REGMODE':      55,
        'ROMA_DATA_WIDTH':  56,
        'ROMB_DATA_WIDTH':  57,
        'ROM_DATA_WIDTH':   58,
        'ROM_PORTA_BEHB':   59,
        'ROM_PORTA_BELB':   60,
        'ROMA_REGMODE':     61,
        'ROMB_REGMODE':     62,
        'PORTB_BELB':       63,
        'PORTA_MODE':       64,
        'PORTB_MODE':       65,
        'PORTB_BEHB':       66
    }

bsram_attrvals = {
        'UNKNOWN':          0,
        'INV':              1,
        'ENABLE':           2,
        'SET':              3,
        'X36':              4,
        '1':                5,
        '2':                6,
        '4':                7,
        '9':                8,
        '16':               9,
        'RBW':              10,
        'WT':               11,
        'OUTREG':           12,
        'DISABLE':          13,
        'RESET':            14
    }

# slice
cls_attrids = {
        'MODE':             0,
        'REGMODE':          1,
        'SRMODE':           2,
        'GSR':              3,
        'LSRONMUX':         4,
        'CEMUX_1':          5,
        'CEMUX_CE':         6,
        'CLKMUX_1':         7,
        'CLKMUX_CLK':       8,
        'LSR_MUX_1':        9,
        'LSR_MUX_LSR':      10,
        'REG0_SD':          11,
        'REG1_SD':          12,
        'REG0_REGSET':      13,
        'REG1_REGSET':      14
    }

cls_attrvals = {
        'UNKNOWN':          0,
        '0':                1,
        '1':                2,
        'SIG':              3,
        'INV':              4,
        'ENGSR':            5,
        'DISGSR':           6,
        'LSRMUX':           7,
        'LUT':              8,
        'LOGIC':            9,
        'ALU':              10,
        'SSRAM':            11,
        'FF':               12,
        'LATCH':            13,
        'ASYNC':            14,
        'LSR_OVER_CE':      15,
        'SET':              16,
        'RESET':            17
    }
# DLL
dll_attrids = {
        'CLKSEL':           0,
        'CODESCAL':         1,
        'CODESCALEN':       2,
        'DIVSEL':           3,
        'FORCE':            4,
        'GSR':              5,
        'ROSC':             6,
        'ROUNDOFF':         7,
        'RSTPOL':           8,
        'CLKMUX_SYSCLK':    9
    }

dll_attrvals = {
        'UNKNOWN':          0,
        'HECLK0':           1,
        'HECLK1':           2,
        'HECLK2':           3,
        'HECLK3':           4,
        'SYSCLK':           5,
        'POS_22':           6,
        'POS_33':           7,
        'POS_44':           8,
        'NEG_11':           9,
        'NEG_22':           10,
        'NEG_33':           11,
        'NEG_44':           12,
        'ENABLE':           13,
        'FAST':             14,
        'DISABLE':          15,
        'NOINV':            16,
        'POS_11':           17,
        'INV':              18
        }

# HCLK
hclk_attrids = {
        'BK00DIV2_RST':     0,
        'BK01DIV2_RST':     1,
        'BK0MUX0_OUTSEL':   2,
        'BK0MUX1_OUTSEL':   3,
        'BK10DIV2_RST':     4,
        'BK11DIV2_RST':     5,
        'BK1MUX0_OUTSEL':   6,
        'BK1MUX1_OUTSEL':   7,
        'BRGMUX0_BRGOUT':   8,
        'BRGMUX0_INSEL':    9,
        'BRGMUX1_BRGOUT':  10,
        'BRGMUX1_INSEL':   11,
        'BRGMUX0_BRGSTOP': 12,
        'BRGMUX1_BRGSTOP': 13,
        'HCLKDIV0_DIV':    14,
        'HCLKDIV0_RST':    15,
        'HCLKDIV1_DIV':    16,
        'HCLKDIV1_RST':    17,
        'HSB0MUX0_HSTOP':  18,
        'HSB0MUX1_HSTOP':  19,
        'HSB1MUX0_HSTOP':  20,
        'HSB1MUX1_HSTOP':  21,
        'HCLKDCS0_SEL':    22,
        'HCLKDCS1_SEL':    23,
        'DCC0':            24,
        'DCC1':            25,
        'DLYMUX':          26,
        'HCLKDIV_DIV':     27,
        'HCLKDIV_RST':     28,
        }

hclk_attrvals = {
        'UNKNOWN':          0,
        'DIVCIBRST2':       1,
        'DIVCIBRST3':       2,
        'DIV2':             3,
        'DIVCIBRST0':       4, 
        'DIVCIBRST1':       5,
        'DIVCIBRST4':       6,
        'DIVCIBRST5':       7,
        'ENABLE':           8,
        'BRGCIBSEL0':       9,
        'BRGCIBSEL1':      10,
        'BRGCIBSTOP0':     11,
        'BRGCIBSTOP1':     12,
        '2':               13,
        '3.5':             14,
        '4':               15,
        '5':               16,
        'HCLKCIBSTOP0':    17,
        'HCLKCIBSTOP1':    18,
        'HCLKCIBSTOP2':    19,
        'HCLKCIBSTOP3':    20,
        'HCLKBK10':        21,
        'HCLKBK11':        22,
        '8':               23,
        'DIVCIBRST':       24,
        'NEG_80':          25,
        '80':              26,
        }


# PLL
pll_attrids = {
        'BYPCK':            0,
        'BYPCKDIV':         1,
        'BYPCKPS':          2,
        'CLKOUTDIV3':       3,
        'CLKOUTDIV3SEL':    4,
        'CLKOUTDIV':        5,
        'CLKOUTDIVSEL':     6,
        'CLKOUTPS':         7,
        'CRIPPLE':          8,
        'DUTY':             9,
        'DUTYSEL':          10,
        'DPSEL':            11,
        'FBSEL':            12,
        'FDIV':             13,
        'FDIVSEL':          14,
        'FDLYPWD':          15,
        'FLDCOUNT':         16,
        'FLOCK':            17,
        'FLTOP':            18,
        'GMCGAIN':          19,
        'GMCMODE':          20,
        'GMCOUT':           21,
        'GMCVREF':          22,
        'ICPSEL':           23,
        'IDIV':             24,
        'IDIVSEL':          25,
        'INSEL':            26,
        'IRSTEN':           27,
        'KVCO':             28,
        'LPR':              29,
        'ODIV':             30,
        'ODIVSEL':          31,
        'OPDLY':            32,
        'OSDLY':            33,
        'PASEL':            34,
        'PDN':              35,
        'PHASE':            36,
        'PLOCK':            37,
        'PSDLY':            38,
        'PWDEN':            39,
        'RSTEN':            40,
        'RSTLF':            41,
        'SDIV':             42,
        'SELIN':            43,
        'SFTDLY':           44,
        'SRSTEN':           45,
        'CLKMUX_CLKIN2':    46,
        'CLKMUX_CLKIN1':    47,
        'CLKMUX_CLKFB0':    48,
        'PLLVCC0':          49,
        'PLLVCC0_BYPASS':   50,
        'PLLVCC0_TRIM0':    51,
        'PLLVCC0_TRIM1':    52,
        'PLLVCC1':          53,
        'PLLVCC1_BYPASS':   54,
        'PLLVCC1_TRIM0':    55,
        'PLLVCC1_TRIM1':    56,
        'VCOBIAS_EN_D':     57,
        'VCOBIAS_EN_U':     58,
        'DIVA':             59,
        'DIVB':             60,
        'DIVC':             61,
        'DIVD':             62,
        'DPAEN':            63,
        'DUTY_TRIM_A':      64,
        'DUTY_TRIM_B':      65,
        'ICPDYN_SEL':       66,
        'LPR_SEL':          67,
        'INTFB':            68,
        'MON':              69,
        'CKA':              70,
        'CKB':              71,
        'CKC':              72,
        'CKD':              73,
        'CKA_OUT':          74,
        'CKB_OUT':          75,
        'CKC_OUT':          76,
        'CKD_OUT':          77,
        'CKA_IN':           78,
        'CKB_IN':           79,
        'CKC_IN':           80,
        'CKD_IN':           81,
        'PSA_COARSE':       82,
        'PSB_COARSE':       83,
        'PSC_COARSE':       84,
        'PSD_COARSE':       85,
        'PSA_FINE':         86,
        'PSB_FINE':         87,
        'PSC_FINE':         88,
        'PSD_FINE':         89,
        'DTA_SEL':          90,
        'DTB_SEL':          91,
        'PSA_SEL':          92,
        'PSB_SEL':          93,
        'PSC_SEL':          94,
        'PSD_SEL':          95,
        'DIVA_SEL':         96,
        'DIVB_SEL':         97,
        'DIVC_SEL':         98,
        'DIVD_SEL':         99,
        'DTMS_ENA':         100,
        'DTMS_ENB':         101,
        'DTMS_ENC':         102,
        'DTMS_END':         103,
        'VCCREG_TRIM0':     104,
        'VCCREG_TRIM1':     105,
        'PLLREG0':          106,
    }
pll_attrvals = {
        'UNKNOWN':          0,
        'BYPASS':           1,
        'DISABLE':          2,
        'ENABLE':           3,
        'CLKOUTPS':         4,
        'C1':               5,
        'C2':               6,
        'C3':               7,
        'DYN':              8,
        'PWD':              9,
        'CLKFB0':           10,
        'CLKFB1':           11,
        'CLKFB2':           12,
        'CLKFB3':           13,
        'CLKFB4':           14,
        'CLKFN0':           15,
        'FORCE0':           16,
        'FORCE1':           17,
        'CLKIN0':           18,
        'CLKIN1':           19,
        'CLKIN2':           20,
        'CLKIN3':           21,
        'CLKIN4':           22,
        'R1':               23,
        'R2':               24,
        'R3':               25,
        'R4':               26,
        'R5':               27,
        'R6':               28,
        'R7':               29,
        'RESET':            30,
        'INV':              31,
        '0':                32,
        'P0':               33,
        'P50':              34,
        'P100':             35,
        'P200':             36,
        'M0':               37,
        'M50':              38,
        'M100':             39,
        'M200':             40,
        'CKB':              41,
        'CKC':              42,
        'CKD':              43,
        'VSO':              44,
        'CASCADE':          45,
        'ICLK':             46,
        'FCLK':             47,
        'CLKOUT':           48
    }

#OSCillator
osc_attrids = {
        'MCLKCIB':          0,
        'NORMAL':           1,
        'POWER_SAVE':       2,
        'USERPOWER_SAVE':   3,
        'MCLKCIB_EN':       4,
        'TRIM':             5,
        'OSCREG':           6, # I guess it is REGULATOR_EN
        'MCK2PLL':          7,
        'USED_FLAG':        10
    }

osc_attrvals = {
        'UNKNOWN':          0,
        'ENABLE':           1,
        'ON':               2
    }

# config
cfg_attrids = {
        'DONE_AS_GPIO':     0,
        'GSR':              2,
        'JTAG_AS_GPIO':     6,
        'READY_AS_GPIO':    7,
        'MSPI_AS_GPIO':     8,
        'RECONFIG_AS_GPIO': 9,
        'SSPI_AS_GPIO':     10,
        'I2C_AS_GPIO':      20,
        'JTAG_EN':          21,
        'POR':              24, # power on reset
    }

cfg_attrvals = {
        'UNKNOWN':          0,
        'YES':              1,
        'ACTIVE_LOW':       2,
        'F0':               3,
        'F1':               4,
        'F2':               5,
        'F3':               6,
        'USED':             7,
        'UNUSED':           8,
        'FALSE':            9
    }

# global set/reset
gsr_attrids = {
        'GSRMODE':          0,
        'SYNCMODE':         1,
    }

gsr_attrvals = {
        'UNKNOWN':          0,
        'ACTIVE_LOW':       1,
        'SYNC':             2,
    }

# iologic
iologic_attrids = {
        'INMODE':                   0,
        'OUTMODE':                  1,
        'SRMODE':                   2,
        'CLKIDDRMUX':               3,
        'DELMUX':                   4,
        'GSR':                      5,
        'TSHX':                     6,
        'MARGINTEST':               7,
        'CEMUX_CE':                 8,
        'CEIMUX_1':                 9,
        'CEOMUX_1':                10,
        'CLKMUX_CLK':              11,
        'CLKIMUX_1':               12,
        'CLKIMUX_CLK':             13,
        'CLKOMUX_1':               14,
        'CLKOMUX_CLK':             15,
        'CLKIDDRMUX_CLKIDDR':      16,
        'CLKODDRMUX_CLKODDR':      17,
        'CLKODDRMUX_CLKOMUX':      18,
        'LSRMUX_LSR':              19,
        'LSRIMUX_0':               20,
        'LSROMUX_0':               21,
        'TSMUX_1':                 22,
        'TSMUX_TS':                23,
        'FF_INREGMODE':            24,
        'IREG_INREGMODE':          25,
        'IREG_REGSET':             26,
        'OREG_OUTREGMODE':         27,
        'OREG_REGSET':             28,
        'TREG_INREGMODE':          29,
        'TREG_OUTREGMODE':         30,
        'TREG_REGSET':             31,
        'DELAY_DEL0':              32,
        'DELAY_DEL1':              33,
        'DELAY_DEL2':              34,
        'DELAY_DEL3':              35,
        'DELAY_DEL4':              36,
        'DELAY_DEL5':              37,
        'DELAY_DEL6':              38,
        'IMON':                    39,
        'IMON_CENTSEL':            40,
        'IMON_SDR':                41,
        'ISIDEL':                  42,
        'IMARG':                   43,
        'UPDATE':                  44,
        'INDEL':                   45,
        'OUTDEL':                  46,
        'FIFO':                    47,
        'SGMII':                   48,
        'ISI':                     49,
        'CEIOMUX_CE':              50,
        'ECLKMUX_CLK':             51,
        'CLKODDRMUX_ECLK':         52,
        'CLKODDRMUX_WRCLK':        53,
        'CLKIDDRMUX_ECLK':         54,
        'CLKODDRMUX_WRCLKCLKODDR': 55,
        'CLKIMUX':                 56,
        'CLKOMUX':                 57,
        'OUTCLK':                  58,
        'OUTSEL0':                 59,
        'OUTSEL1':                 60,
        'DYNAMICCIBCONTROL':       61,
        'IODELAY_CIB':             62,
        'DELAYCHAIN':              63,
        'DLYMUX_MUX0':             64,
        'DLYMUX_MUX1':             65,
        'INDEL_0':                 66,
        'INDEL_1':                 67,
        'IMON_CENTSEL_0':          68,
        'IMON_CENTSEL_1':          69,
    }

iologic_attrvals = {
        'UNKNOWN':              0,
        '0':                    1,
        '1':                    2,
        'INV':                  3,
        'SIG':                  4,
        'IDDR_ODDR':            5,
        'IDDR_OREG':            6,
        'IREG_ODDR':            7,
        'IREG_OREG':            8,
        'IDDRX1':               9,
        'IDDRX2':              10,
        'IDDRX4':              11,
        'IDDRX5':              12,
        'ODDRX1':              13,
        'ODDRX2':              14,
        'ODDRX4':              15,
        'ODDRX5':              16,
        'ODDRX7':              17,
        'ODDRXN':              18,
        'MIDDRX1':             19,
        'MIDDRX2':             20,
        'MIDDRX4':             21,
        'MODDRX1':             22,
        'MODDRX2':             23,
        'MODDRX4':             24,
        'MODDRX21':            25,
        'MODDRX22':            26,
        'MODDRXN':             27,
        'MOSHX20':             28,
        'MOSHX22':             29,
        'MOSHX4':              30,
        'MTSHX21':             31,
        'MTSHX22':             32,
        'MTSHX4':              33,
        'MTXHX21':             34,
        'MTXHX1':              35,
        'DDRENABLE':           36,
        'CDRCLK':              37,
        'ECLK0':               38,
        'ECLK1':               39,
        'NEXTCLK':             40,
        'DQSW':                41,
        'DQSW270':             42,
        'DLY':                 43,
        'DQR90':               44,
        'ENGSR':               45,
        'DISGSR':              46,
        'EDGE':                47,
        'FIFO':                48,
        'OREG':                49,
        'VIDEORX':             50,
        'ASYNC':               51,
        'LSR_OVER_CE':         52,
        'FF':                  53,
        'LATCH':               54,
        'SET':                 55,
        'RESET':               56,
        'MTSH1':               57,
        'MTSH2':               58,
        'MTSH4':               59,
        'TREG':                60,
        'ENABLE':              61,
        'SAME':                62,
        '25PS':                63,
        '50PS':                64,
        '100PS':               65,
        'ONE':                 66,
        'IDDRX8':              67,
        'ODDRX8':              68,
        'DIRECTIONB':          69,
        'MOVEB':               70,
        'MONDISLIVEA0':        71,
        'MONDISLIVEA1':        72,
}

# num -> attr name
iologic_num2val = {v: k for k, v in iologic_attrvals.items()}
iob_num2val = {v: k for k, v in iob_attrvals.items()}

