#
# PySNMP MIB module NBS-CMMCENUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-CMMCENUM-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsCmmcEnumMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 225))
if mibBuilder.loadTexts: nbsCmmcEnumMib.setLastUpdated('201705240000Z')
if mibBuilder.loadTexts: nbsCmmcEnumMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsCmmcEnumMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsCmmcEnumMib.setDescription('This MIB module defines some frequently updated lists for\n        NBS-CMMC-MIB.')
class NbsCmmcEnumChassisType(TextualConvention, Integer32):
    description = 'The type of Chassis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39))
    namedValues = NamedValues(("other", 1), ("bu16", 2), ("bu4", 3), ("bu1", 4), ("bu5", 5), ("bu3", 6), ("bu2", 7), ("fCpe", 8), ("bmc", 9), ("virtual16", 10), ("bu21", 11), ("bu42", 12), ("virtual1", 13), ("virtual2", 14), ("virtual3", 15), ("virtual4", 16), ("bu22", 17), ("bu82", 18), ("bu3v", 19), ("virtual3v", 20), ("bu12", 21), ("occ48", 22), ("occ96", 23), ("occ128", 24), ("occ320", 25), ("od48", 26), ("virtod48", 27), ("od12", 28), ("virtod12", 29), ("od16", 30), ("virtod16", 31), ("od32", 32), ("virtod32", 33), ("od16lc", 34), ("virtod16lc", 35), ("od6", 36), ("virtod6", 37), ("od4", 38), ("virtod4", 39))

class NbsCmmcEnumSlotOperationType(TextualConvention, Integer32):
    description = 'Mode, or primary function, of card in slot'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("other", 1), ("management", 2), ("converter", 3), ("repeater", 4), ("switch", 5), ("splitterCombiner", 6), ("fastRepeater", 7), ("gigabitRepeater", 8), ("monitor", 9), ("opticSwitch", 10), ("remote", 11), ("redundant", 12), ("centralOffice", 13), ("customerPremise", 14), ("multiplexer", 15), ("deprecated16", 16), ("deprecated17", 17), ("deprecated18", 18), ("optAmpBoosterAGC", 19), ("optAmpBoosterAPC", 20), ("optAmpInlineAGC", 21), ("optAmpInlineAPC", 22), ("optAmpPreampAGC", 23), ("optAmpPreampAPC", 24), ("coDualActive", 25), ("coDualInactive", 26), ("physLayerSwitch", 27), ("packetMux", 28), ("optAmpVariableGain", 29), ("optAmpMidstageAGC", 30), ("optAmpMidstageAPC", 31), ("multiCO1g", 32), ("multiCO10g", 33), ("addDropMux", 34), ("multicast", 35), ("optAttenuator", 36), ("repeater40G", 37), ("multiplexer4x10G", 38), ("optAmpPreampAPPC", 39), ("optPassive", 40), ("transponder", 41), ("muxponder", 42), ("addWssDropSplitter", 43), ("dropWssAddCombiner", 44), ("dualAddWssDropSplitter", 45), ("opticalServiceChannel", 46), ("optAmpMidstageVariableGain", 50), ("optAmpVariableGainMidstageInlinePreamp", 51), ("optAmpVariableGainMidstageInline", 52), ("optAmpVariableGainMidstageBooster", 53), ("optAmpRaman", 54), ("optAmpPreampRaman", 55), ("optAmpBoosterRaman", 56), ("optVariableDispersionCompensation", 57), ("midPointRepeater", 58))

class NbsCmmcEnumSlotType(TextualConvention, Integer32):
    description = "This data type is used as the syntax of the nbsCmmcSlotType\n        object in the definition of NBS-CMMC-MIB's nbsCmmcSlotTable.\n        This object is used internally by Manager, and is not useful\n        to most end-users."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254), SingleValueConstraint(255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509), SingleValueConstraint(510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764), SingleValueConstraint(765, 766, 767, 768, 769, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 805))
    namedValues = NamedValues(("empty0", 0), ("empty1", 1), ("empty2", 2), ("empty3", 3), ("em316gs1", 4), ("em316gs2", 5), ("em316gs3", 6), ("em316fms1", 7), ("em316fms2", 8), ("em316fms3", 9), ("em316as1", 10), ("em316as2", 11), ("em316as3", 12), ("em316fds1", 13), ("em316fds2", 14), ("em316fds3", 15), ("em316o3s1", 16), ("em316o3s2", 17), ("em316o3s3", 18), ("em316o12s1", 19), ("em316o12s2", 20), ("em316o12s3", 21), ("em316gsfs1", 22), ("em316gsfs2", 23), ("em316gsfs3", 24), ("em316fsfs1", 25), ("em316fsfs2", 26), ("em316fsfsx", 27), ("em316fsfsz", 28), ("em316fmsfs1", 29), ("em316fmsfs2", 30), ("em316fmsfs3", 31), ("em316asfs2", 32), ("em316asfs3", 33), ("em316fdsfs2", 34), ("em316fdsfs3", 35), ("em316o3sfs2", 36), ("em316o3sfs3", 37), ("em316o12sfs2", 38), ("em316o12sfs3", 39), ("em316em", 40), ("em316emx", 41), ("em316es", 42), ("em316esx", 43), ("em315esz", 44), ("em316fm", 45), ("em316fs1", 46), ("em316fs2", 47), ("em316fsx", 48), ("em315fsz", 49), ("em3162swm", 50), ("em3162sws1", 51), ("em3162sws2", 52), ("em3162sws3a", 53), ("em3162sws3b", 54), ("em3164wdm", 55), ("em316nm", 56), ("em3164sw", 57), ("em3164hub", 58), ("em316sc3m", 59), ("em316sc8m", 60), ("em316sc3s", 61), ("em316sc5s", 62), ("em316fr1", 63), ("em316fr2", 64), ("em316fr3", 65), ("em316gr1", 66), ("em316gr2", 67), ("em316gr3", 68), ("em316f21", 69), ("em316f22", 70), ("em316wdm4", 71), ("em316g", 72), ("em316gsf", 73), ("em316fn", 74), ("em316fsfn", 75), ("em316fmsn", 76), ("em316fmsfn", 77), ("em316asn", 78), ("em316asfsn", 79), ("em316fdsn", 80), ("em316fdsfsn", 81), ("em316o3sn", 82), ("em316o3sfsn", 83), ("em316o12sn", 84), ("em316o12sfsn", 85), ("em316emsn", 86), ("em316emsfsn", 87), ("em316ssn", 88), ("em316ssfsn", 89), ("em316tr", 90), ("em316t1", 91), ("em316t1sf", 92), ("nc3162bu", 93), ("em316wdm4o12", 94), ("em316wdm4o3", 95), ("em316grg", 96), ("em316mso12", 97), ("em316mso3", 98), ("em316e1", 99), ("em316e1sf", 100), ("wdmtrnk", 101), ("em316wdm43", 102), ("em316wdm44", 103), ("em104", 104), ("em105", 105), ("em106", 106), ("em316ds31", 107), ("em316ds32", 108), ("em3164sw1", 109), ("em3166sw1", 110), ("em3166sw2", 111), ("em316wfcs", 112), ("em316wfts", 113), ("em316e11", 114), ("em316e12", 115), ("nc316bu31", 116), ("nc316bu32", 117), ("em316od3", 118), ("nc316nw41", 119), ("nc316nw42", 120), ("em316em1", 121), ("em316e2", 122), ("em316fc", 123), ("em316fcsf", 124), ("nc316nw43", 125), ("nc316nw44", 126), ("em316o48", 127), ("em316o48sf", 128), ("ns129", 129), ("ns130", 130), ("ns131", 131), ("em3163sw", 132), ("em3163swsf", 133), ("em316o3c1", 134), ("em316o3csf", 135), ("nc316nw45", 136), ("nc316nw46", 137), ("em316wdm4f", 138), ("em316wdm4fc", 139), ("em316dpg", 140), ("em3162gsws", 141), ("ns142", 142), ("em316wgcs", 143), ("em316wgts", 144), ("em316wfccs", 145), ("em316wfcts", 146), ("em316wecs", 147), ("em316wets", 148), ("em316osw", 149), ("ns150", 150), ("ns151", 151), ("em316fe11l", 152), ("em316ft11l", 153), ("em316wdm81", 154), ("ns155", 155), ("wdm38", 156), ("ns157", 157), ("em316o3f1", 158), ("ns159", 159), ("em316wdm85", 160), ("em316wdmc3", 161), ("ns162", 162), ("em316fmsh", 163), ("ns164", 164), ("ns165", 165), ("ns166", 166), ("em316e31", 167), ("ns168", 168), ("em316fe12r", 169), ("ns170", 170), ("ns171", 171), ("ns172", 172), ("em316gc1", 173), ("em316gcsf", 174), ("ns175", 175), ("ns176", 176), ("em316ds3sh", 177), ("ns178", 178), ("em316nmhb1", 179), ("em316ds3r", 180), ("ns181", 181), ("em316fe11r", 182), ("em316ft11r", 183), ("ns184", 184), ("em316wdmc4", 185), ("em316adsl1", 186), ("ns187", 187), ("ns188", 188), ("ns189", 189), ("ns190", 190), ("ns191", 191), ("ns192", 192), ("ns193", 193), ("ns194", 194), ("em316gccsf", 195), ("em316gctsf", 196), ("em316osh", 197), ("ns198", 198), ("ns199", 199), ("ns200", 200), ("ns201", 201), ("ns202", 202), ("ns203", 203), ("ns204", 204), ("ns205", 205), ("ns206", 206), ("ns207", 207), ("ns208", 208), ("ns209", 209), ("em316sadm1", 210), ("ns211", 211), ("ns212", 212), ("em316flm1", 213), ("em316flm2", 214), ("ns215", 215), ("ns216", 216), ("ns217", 217), ("ns218", 218), ("wdm24ctr", 219), ("ns220", 220), ("wdm24ctl", 221), ("em316frm1", 222), ("em316frm2", 223), ("wdm44sf", 224), ("em316swrfhp", 225), ("ns226", 226), ("em316swhp", 227), ("ns228", 228), ("em316f2rm1", 229), ("em316f2rm2", 230), ("ns231", 231), ("ns232", 232), ("ns233", 233), ("ns234", 234), ("ns235", 235), ("ns236", 236), ("ns237", 237), ("ns238", 238), ("em316wfrmc", 239), ("em316wfrmt", 240), ("em316t1mux1", 241), ("em316t1mux2", 242), ("em316e1mux4j", 243), ("em316e1x4sfj", 244), ("ns245", 245), ("em316efrm1", 246), ("em316efrm2", 247), ("ns248", 248), ("ns249", 249), ("ns250", 250), ("ns251", 251), ("ns252", 252), ("ns253", 253), ("ns254", 254)) + NamedValues(("ns255", 255), ("ns256", 256), ("ns257", 257), ("em316sc1021", 258), ("ns259", 259), ("ns260", 260), ("ns261", 261), ("em316edsc1", 262), ("em316edsc2", 263), ("em316wdmslot", 264), ("em316wdmc265", 265), ("empty266", 266), ("em316wp1", 267), ("em316wp2", 268), ("em316oa", 269), ("em316e1mux1", 270), ("em316e1mux2", 271), ("em3162tsfp", 272), ("em316dmr48", 273), ("ns3162sfpr", 274), ("ns316xp342r", 275), ("em316ef", 276), ("em316efsf", 277), ("em316padms", 278), ("ns279", 279), ("ns280", 280), ("ns281", 281), ("ns316f16csfp", 282), ("ns316sdi8", 283), ("ns284", 284), ("em316wdmpa4", 285), ("em316wdmpa4t", 286), ("ns287", 287), ("em3162gbicl", 288), ("em3162gbicr", 289), ("em316ge1sfl", 290), ("em316ge1sfr", 291), ("em316fchub", 292), ("em316fcr", 293), ("em316mr48", 294), ("ns295", 295), ("em316fe1xx", 296), ("em316ft1sf", 297), ("em316gbicsfp", 298), ("ns299", 299), ("ns300", 300), ("em316pamulc8n", 301), ("em316pamulc4n", 302), ("em316t1muxrrm", 303), ("em316e1muxrrm", 304), ("ns305", 305), ("em316wo3c", 306), ("ns307", 307), ("em316grmah", 308), ("em316grmahsf", 309), ("em316efrmah", 310), ("em316efrmahsf", 311), ("em316erm", 312), ("em316ermsf", 313), ("em316efan", 314), ("em316efansf", 315), ("ns316", 316), ("nc316Xp343r", 317), ("ns318", 318), ("em316pamulc8", 319), ("em316pamulc4", 320), ("cm316fFtth", 321), ("ns322", 322), ("ns323", 323), ("ns324", 324), ("ns325", 325), ("em316padm41mu", 326), ("ns327", 327), ("em316pamuscm4", 328), ("em316pamuscd4", 329), ("em316pamuscm8", 330), ("em316pamuscd8", 331), ("em316muxmusc16", 332), ("em316dmuxmusc16", 333), ("ns334", 334), ("em316dpadms", 335), ("ns336", 336), ("em316dwmux16", 337), ("em316dwdmx16", 338), ("ns339", 339), ("ns340", 340), ("em316fe1sf", 341), ("em316xt1", 342), ("em316fe1rj", 343), ("em316gt1sfv", 344), ("ns345", 345), ("ns346", 346), ("ns347", 347), ("ns348", 348), ("ns349", 349), ("nc316xp322", 350), ("nc316xp323", 351), ("em316wermc", 352), ("em316wermt", 353), ("ns354", 354), ("ns355", 355), ("ns356", 356), ("ns357", 357), ("em316ee1rmft", 358), ("em316xe1rmft", 359), ("em316lx2", 360), ("em316lxm", 361), ("em316dwmux32", 362), ("em316dwdmx32v", 363), ("em316dwmux32nv", 364), ("em316dwdmx32n", 365), ("ns366", 366), ("ns367", 367), ("em316fe1rmft", 368), ("em316efe1ah", 369), ("em316eft1ah", 370), ("em316efe1rj", 371), ("ns372", 372), ("ns373", 373), ("ns374", 374), ("em316grmahsh", 375), ("em316ermahsh", 376), ("ns377", 377), ("ns378", 378), ("em316ermah", 379), ("ns380", 380), ("em3162sfpx", 381), ("ns382", 382), ("pmcwdm8sfp", 383), ("ns384", 384), ("ns385", 385), ("mccSfp36", 386), ("mccGRj36", 387), ("em316osc", 388), ("em316gemx2r", 389), ("em316gemx6r", 390), ("mccSfp72", 391), ("mccGRj72", 392), ("em316gcl", 393), ("em316gclsf", 394), ("em316wgclc", 395), ("em316wgclt", 396), ("ns397", 397), ("ns398", 398), ("ns399", 399), ("ns400", 400), ("ns401", 401), ("ns402", 402), ("ns403", 403), ("ns404", 404), ("ns405", 405), ("ns406", 406), ("ns407", 407), ("ns408", 408), ("ns409", 409), ("ns410", 410), ("ns411", 411), ("ns412", 412), ("ns413", 413), ("ns414", 414), ("ns415", 415), ("ns416", 416), ("em316xfpr", 417), ("oemntgrmah", 418), ("oemntermah", 419), ("oemntnm", 420), ("em316wds3c", 421), ("em316wds3t", 422), ("em316we3c", 423), ("em316we3t", 424), ("ns425", 425), ("ns426", 426), ("em316eft1mua4v", 427), ("em316efx1mub4", 428), ("em316efe1muc4v", 429), ("ns430", 430), ("ns431", 431), ("ns432", 432), ("em316t1mux4rm", 433), ("em316e1muxrjrm", 434), ("em316e1mux4rm", 435), ("em316dmr", 436), ("em316mr", 437), ("ns438", 438), ("ns439", 439), ("ns440", 440), ("em316ge1rjsf", 441), ("em316mr48q", 442), ("em316dmr48q", 443), ("em316mrmx2r", 444), ("ns445", 445), ("ns446", 446), ("ns447", 447), ("ns448", 448), ("ns449", 449), ("ns450", 450), ("mcc9xfp", 451), ("ns452", 452), ("em316cdadd2", 453), ("em316cdadd1", 454), ("ns455", 455), ("ns456", 456), ("em316nmlx12", 457), ("em316nmlx21", 458), ("em316nmlx", 459), ("ns460", 460), ("em316sw22", 461), ("em316sw12", 462), ("em316sw04", 463), ("em316sw13", 464), ("ns465", 465), ("ns466", 466), ("ns467", 467), ("ns468", 468), ("ns469", 469), ("ns470", 470), ("em3164swb", 471), ("ns472", 472), ("ns473", 473), ("ns474", 474), ("em316csadsxx", 475), ("em316csadsxxyy", 476), ("em316csaddxx", 477), ("em316csaddxxyy", 478), ("em3163swb", 479), ("em316ds3", 480), ("em316dt3e3", 481), ("ns482", 482), ("em316mux4xn", 483), ("em316dmx4xn", 484), ("em316mux4xbd", 485), ("em316dmx4xbd", 486), ("em316mux8nbd", 487), ("em316dmx8nbd", 488), ("em316mux8bd", 489), ("em316dmx8bd", 490), ("em316dpadxx", 491), ("em316dpadxxyy", 492), ("em316dpad4xx", 493), ("em316dpad8xx", 494), ("em316wt1c", 495), ("ns496", 496), ("em316gt1rm", 497), ("em316g6t1rm1", 498), ("em316g6t1rm2", 499), ("em316dsadsxx", 500), ("em316ddaddxx", 501), ("em316ddaddxxyy", 502), ("em316edfalv", 503), ("em316psc", 504), ("em316sos", 505), ("em316doscb", 506), ("em316padm8", 507), ("em316csads4", 508), ("ns509", 509)) + NamedValues(("ns510", 510), ("ns511", 511), ("ns512", 512), ("em316plc", 513), ("ns514", 514), ("ns515", 515), ("ns516", 516), ("ns517", 517), ("ns518", 518), ("em316dwmx8", 519), ("ns520", 520), ("em316genpasv", 521), ("em316ge1rm", 522), ("ns523", 523), ("ns524", 524), ("em316g6e1rms2", 525), ("ns526", 526), ("ns527", 527), ("ns528", 528), ("ns529", 529), ("mcc18t1e1", 530), ("ns531", 531), ("ns532", 532), ("mcc18dt3e3", 533), ("em316edfar", 534), ("ns535", 535), ("ns536", 536), ("ns537", 537), ("em316ossh", 538), ("em316sc3", 539), ("ns540", 540), ("em316fc400", 541), ("ns542", 542), ("ns543", 543), ("ns544", 544), ("em316eusmv", 545), ("ns546", 546), ("ns547", 547), ("em316dcm100r", 548), ("em316dcm100l", 549), ("ns550", 550), ("em316twoxfpet", 551), ("em316dwmux16be", 552), ("ns553", 553), ("ns554", 554), ("empmc8xfp", 555), ("ns556", 556), ("em316dwmx16bem", 557), ("ns558", 558), ("em316e1t1xy", 559), ("dwmx32rbm", 560), ("ns561", 561), ("ns562", 562), ("ns563", 563), ("empmc36t1e1", 564), ("ns565", 565), ("em316palc8nl", 566), ("em316palc8nr", 567), ("em316gswxy", 568), ("em316dwd40m5713", 569), ("em316dwd40m5712", 570), ("em316dwd40m5711", 571), ("em316mux535531b", 572), ("ns573", 573), ("em31610gxy", 574), ("ns575", 575), ("ns576", 576), ("ns577", 577), ("ns578", 578), ("ns579", 579), ("ns580", 580), ("ns581", 581), ("ns582", 582), ("ns583", 583), ("ns584", 584), ("em316os2", 585), ("em316osa", 586), ("ns587", 587), ("ns588", 588), ("ns589", 589), ("ns590", 590), ("ns591", 591), ("ns592", 592), ("em316ea", 593), ("ns594", 594), ("em316eusm10gr", 595), ("em316eusm10gl", 596), ("em316dmdxa16b1", 597), ("em316dmdxa16b2", 598), ("em316dmdxa16b3", 599), ("em316dmdxa16b4", 600), ("em316dmdxa16b5", 601), ("em316dmdxa40m01", 602), ("em316dmdxa40m02", 603), ("em316dmdxa40m03", 604), ("em316dmdxa40m04", 605), ("em316dmdxa40m05", 606), ("em316dmdxa40m06", 607), ("em316dmdxa40m07", 608), ("em316dmdxa40m08", 609), ("em316dmdxa40m09", 610), ("em316dmdxa40m10", 611), ("em316dmdxa40m11", 612), ("em316dmdxa16ra", 613), ("em316dmdxa16rb", 614), ("em31620g1", 615), ("em31620g2", 616), ("em31640g3", 617), ("em31640g4", 618), ("em31640g5", 619), ("em316rpon", 620), ("ns621", 621), ("empmc36sas", 622), ("em316osw8", 623), ("ns624", 624), ("ns625", 625), ("em31610g8swxyr", 626), ("em31610g8swxym", 627), ("em31610g8swxyl", 628), ("ns629", 629), ("em316cmux831b", 630), ("ns631", 631), ("em316mdx46ma001", 632), ("em316mdx46ma002", 633), ("em316mdx46ma003", 634), ("em316mdx46ma004", 635), ("em316mdx46ma005", 636), ("em316mdx46ma006", 637), ("em316mdx46ma007", 638), ("em316mdx46ma008", 639), ("em316mdx46ma009", 640), ("em316mdx46ma010", 641), ("em316mdx46ma011", 642), ("em316mdx46ma012", 643), ("em316osw128a", 644), ("em316osw128b", 645), ("em316osw128c", 646), ("em316osw128d", 647), ("em316osw128e", 648), ("em316osw128f", 649), ("em316osw128g", 650), ("em316osw128h", 651), ("em316osw128i", 652), ("em316osw128j", 653), ("em316osw128k", 654), ("em316osw128l", 655), ("em316osw128m", 656), ("ns657", 657), ("em316dcmxx", 658), ("em316osshlc", 659), ("em316eavg2217", 660), ("em316dmr10g3r", 661), ("em316fdt1e1rm", 662), ("em316sw8fxr", 663), ("em316sw8fxlv", 664), ("em316mdx46mx002", 665), ("em316mdx46mb003", 666), ("em316mdx46mb002", 667), ("em316mdx46mc002", 668), ("em316eamlp2017v", 669), ("ns670", 670), ("em316gemx4rr", 671), ("em316gemx4rlv", 672), ("empmcqsfp36", 673), ("ns674", 674), ("ns675", 675), ("em3162qsfp40", 676), ("ns677", 677), ("ns678", 678), ("mcc36ic", 679), ("ns680", 680), ("em316voar", 681), ("em316voalv", 682), ("em316dvmdxa", 683), ("em316dvmdxbv", 684), ("em316cmdxm8al", 685), ("em316cmdxm8ar", 686), ("ns687", 687), ("ns688", 688), ("em316dvmdxav1", 689), ("em316dvmdxav2", 690), ("em316dvmdxav3", 691), ("em316dvmdxav4", 692), ("em316dvmdxav5", 693), ("em316dvmdxav6", 694), ("em316dvmdxav7", 695), ("em316dvmdxav8", 696), ("em316dvmdxav9", 697), ("ns698", 698), ("ns699", 699), ("ns700", 700), ("em316ra12r", 701), ("em316ra12lv", 702), ("ns703", 703), ("em316ra12mv", 704), ("ns705", 705), ("ns706", 706), ("em316dmr10gf", 707), ("ns708", 708), ("ns709", 709), ("ns710", 710), ("ns711", 711), ("ns712", 712), ("ns713", 713), ("ns714", 714), ("odnm", 715), ("ns716", 716), ("ns717", 717), ("ns718", 718), ("ns719", 719), ("oddmr10g3r", 720), ("oddmr10gf", 721), ("od2hwss4dws", 722), ("od2hmxp100g", 723), ("odtxp100gf2c", 724), ("ns725", 725), ("em316raf10", 726), ("ns727", 727), ("odtxp100g2c", 728), ("ns729", 729), ("od2hwss4dcw", 730), ("ns731", 731), ("ns732", 732), ("odugc", 733), ("ns734", 734), ("odgenpassive", 735), ("odfiller", 736), ("odtxp100g2cw1", 737), ("od2hwss4dww", 738), ("ns739", 739), ("ns740", 740), ("ns741", 741), ("ns742", 742), ("ns743", 743), ("ns744", 744), ("ns745", 745), ("ns746", 746), ("em316twoxfp16g", 747), ("od2hdwss4dws", 748), ("odedfa", 749), ("odedfam", 750), ("odraman", 751), ("ns752", 752), ("od2hdmx10g", 753), ("ns754", 754), ("ns755", 755), ("ns756", 756), ("odtxp100gf", 757), ("ns758", 758), ("ns759", 759), ("ns760", 760), ("odgswxy", 761), ("ns762", 762), ("odoscx1addxd", 763), ("ns764", 764)) + NamedValues(("odeusm", 765), ("ns766", 766), ("ns767", 767), ("ns768", 768), ("ns769", 769), ("odctq", 780), ("ns781", 781), ("odceon226f", 782), ("ns783", 783), ("odtxp100gfq", 784), ("odtxp100gq", 785), ("ns786", 786), ("ns787", 787), ("ns788", 788), ("ns789", 789), ("ns790", 790), ("odedfavm", 791), ("odedfavmosc", 792), ("odedfa2xfp", 793), ("od2xfp", 794), ("odtundcm", 795), ("oduxg", 796), ("odedfavmosc2", 805))

class NbsCmmcEnumPortConnector(TextualConvention, Integer32):
    description = 'The Port Connector.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("unknown", 1), ("removed", 2), ("foDSC", 3), ("foSC", 4), ("cuRj45", 5), ("foLC", 6), ("coaxF", 7), ("coaxBNC", 8), ("coax2BNC", 9), ("cuRj45wLEDs", 10), ("cuRj11", 11), ("cuDb9", 12), ("cuHssdc", 13), ("coaxHeader", 14), ("foFiberJack", 15), ("foMtRj", 16), ("foMu", 17), ("sg", 18), ("foPigtail", 19), ("cuPigtail", 20), ("smb", 21), ("firewireA", 22), ("firewireB", 23), ("cuRj48", 24), ("fo1LC", 25), ("fo2ST", 26), ("sataDevicePlug", 27), ("sataHostPlug", 28), ("miniCoax", 29), ("mpo", 30), ("miniSAS4x", 31), ("reserved", 32), ("cxpCuPassive", 33), ("cxpCuActive", 34), ("cxpFoActive", 35), ("cxpFoConnect", 36), ("fc", 37), ("cuMicroUsbB", 38), ("rj45wUSBRJ45Active", 39), ("rj45wUSBUSBActive", 40))

class NbsCmmcChannelBand(TextualConvention, Integer32):
    description = "The ITU grid labels DWDM channels with a letter 'band' and a\n         numeric channel.  Within this mib, the band is indicated by\n         this object, and the channel number is shown in the object\n         nbsOsaChannelNumber.\n\n         Frequencies of at least 180100 GHz but less than 190100 GHz\n         are considered the L spectrum, and frequencies of at least\n         190100 but less than 200100 GHz are considered the C spectrum.\n\n         Frequencies evenly divisible by 100 GHz are designated with\n         a 'C' or 'L' prepended to the channel number.  Frequencies\n         that are offset by 50 GHz are designated 'H' within the C\n         spectrum, and 'Q' within the L spectrum."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 0), ("cBand", 1), ("hBand", 2), ("lBand", 3), ("qBand", 4))

mibBuilder.exportSymbols("NBS-CMMCENUM-MIB", NbsCmmcEnumPortConnector=NbsCmmcEnumPortConnector, nbsCmmcEnumMib=nbsCmmcEnumMib, PYSNMP_MODULE_ID=nbsCmmcEnumMib, NbsCmmcEnumSlotOperationType=NbsCmmcEnumSlotOperationType, NbsCmmcEnumSlotType=NbsCmmcEnumSlotType, NbsCmmcChannelBand=NbsCmmcChannelBand, NbsCmmcEnumChassisType=NbsCmmcEnumChassisType)
