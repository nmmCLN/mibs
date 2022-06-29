#
# PySNMP MIB module NEXANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nexans/NEXANS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:53 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Unsigned32, TimeTicks, IpAddress, iso, Bits, enterprises, ModuleIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "TimeTicks", "IpAddress", "iso", "Bits", "enterprises", "ModuleIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nexansANS = MibIdentifier((1, 3, 6, 1, 4, 1, 266))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1))
bmSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3))
fiberSwitch100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 1))
copperSwitch100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 2))
fiberSwitch100BmADesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 3))
copperSwitch100BmADesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 4))
fiberSwitch100BmA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 5))
copperSwitch100BmA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 6))
fiberSwitch100BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 7))
copperSwitch100BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 8))
fiberSwitch100BmPlusDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 9))
copperSwitch100BmPlusDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 10))
dualSwitch100BmPlusDeskFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 11))
dualSwitch100BmPlusDeskCopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 12))
dualSwitch100BmPlusDeskCopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 13))
fiberSwitch100BmPlusDeskVersA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 14))
copperSwitch100BmPlusDeskVersA = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 15))
fiberSwitchM100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 16))
copperSwitchM100Bm = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 17))
fiberSwitch100BmPlusDeskVersC = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 18))
copperSwitch100BmPlusDeskVersC = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 19))
fiberSwitch1000BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 20))
dualSwitch1000BmPlusFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 21))
dualSwitch1000BmPlusDeskFibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 22))
dualSwitch1000BmPlusCopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 23))
dualSwitch1000BmPlusCopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 24))
copperSwitch1000BmPlus = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 25))
gigaSwitchG541Desk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 27))
gigaSwitchG542SfpDesk = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 28))
iSwitch740CopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 30))
iSwitch741CopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 31))
iSwitch742FibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 32))
iSwitch1042FibFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 33))
iSwitch1043 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 34))
iSwitch742SfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 35))
iSwitch1043Sfp3Vi = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 36))
iGigaSwitch541 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 37))
iGigaSwitch542Sfp2Vi = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 38))
iGigaSwitch1604 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 40))
iGigaSwitch1608 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 41))
iGigaSwitch1612 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 42))
gigaSwitchBmFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 50))
gigaSwitchBmCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 51))
gigaSwitchV2Fib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 52))
gigaSwitchV2CopFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 53))
gigaSwitchV2CopCop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 54))
gigaSwitchV2SfpFib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 55))
gigaSwitchV2Cop = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 56))
gigaSwitchV3FibTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 60))
gigaSwitchV3SfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 61))
gigaSwitchV3d2SfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 62))
gigaSwitchV3d2SfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 63))
gigaSwitchV3d2Fib = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 64))
fiberSwitch1000BmV3 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 66))
fiberSwitch100BmV3 = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 67))
gigaSwitch641DeskSfpTp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 70))
gigaSwitch642DeskSfpSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 266, 1, 3, 71))
mibBuilder.exportSymbols("NEXANS-MIB", iSwitch742SfpSfp=iSwitch742SfpSfp, copperSwitch100BmPlusDesk=copperSwitch100BmPlusDesk, fiberSwitch1000BmV3=fiberSwitch1000BmV3, gigaSwitchG541Desk=gigaSwitchG541Desk, copperSwitch100BmADesk=copperSwitch100BmADesk, dualSwitch100BmPlusDeskCopCop=dualSwitch100BmPlusDeskCopCop, fiberSwitchM100Bm=fiberSwitchM100Bm, dualSwitch1000BmPlusCopCop=dualSwitch1000BmPlusCopCop, gigaSwitchV3d2SfpSfp=gigaSwitchV3d2SfpSfp, gigaSwitchV2SfpFib=gigaSwitchV2SfpFib, gigaSwitchV2Cop=gigaSwitchV2Cop, copperSwitch100BmA=copperSwitch100BmA, fiberSwitch100BmA=fiberSwitch100BmA, bmSwitch=bmSwitch, iGigaSwitch541=iGigaSwitch541, gigaSwitchV3SfpTp=gigaSwitchV3SfpTp, gigaSwitchBmCop=gigaSwitchBmCop, fiberSwitch1000BmPlus=fiberSwitch1000BmPlus, iSwitch1043Sfp3Vi=iSwitch1043Sfp3Vi, copperSwitch100Bm=copperSwitch100Bm, dualSwitch1000BmPlusDeskFibFib=dualSwitch1000BmPlusDeskFibFib, gigaSwitchV3d2Fib=gigaSwitchV3d2Fib, iSwitch742FibFib=iSwitch742FibFib, fiberSwitch100BmADesk=fiberSwitch100BmADesk, gigaSwitch642DeskSfpSfp=gigaSwitch642DeskSfpSfp, dualSwitch1000BmPlusFibFib=dualSwitch1000BmPlusFibFib, iGigaSwitch542Sfp2Vi=iGigaSwitch542Sfp2Vi, gigaSwitchBmFib=gigaSwitchBmFib, copperSwitchM100Bm=copperSwitchM100Bm, iGigaSwitch1608=iGigaSwitch1608, fiberSwitch100Bm=fiberSwitch100Bm, iGigaSwitch1612=iGigaSwitch1612, fiberSwitch100BmPlusDeskVersC=fiberSwitch100BmPlusDeskVersC, copperSwitch100BmPlusDeskVersC=copperSwitch100BmPlusDeskVersC, iSwitch741CopFib=iSwitch741CopFib, fiberSwitch100BmV3=fiberSwitch100BmV3, copperSwitch100BmPlus=copperSwitch100BmPlus, copperSwitch100BmPlusDeskVersA=copperSwitch100BmPlusDeskVersA, dualSwitch1000BmPlusCopFib=dualSwitch1000BmPlusCopFib, iSwitch740CopCop=iSwitch740CopCop, products=products, copperSwitch1000BmPlus=copperSwitch1000BmPlus, iSwitch1042FibFib=iSwitch1042FibFib, gigaSwitchV3d2SfpTp=gigaSwitchV3d2SfpTp, fiberSwitch100BmPlusDesk=fiberSwitch100BmPlusDesk, dualSwitch100BmPlusDeskFibFib=dualSwitch100BmPlusDeskFibFib, gigaSwitchV2CopCop=gigaSwitchV2CopCop, gigaSwitchV3FibTp=gigaSwitchV3FibTp, iGigaSwitch1604=iGigaSwitch1604, fiberSwitch100BmPlus=fiberSwitch100BmPlus, fiberSwitch100BmPlusDeskVersA=fiberSwitch100BmPlusDeskVersA, dualSwitch100BmPlusDeskCopFib=dualSwitch100BmPlusDeskCopFib, gigaSwitchV2Fib=gigaSwitchV2Fib, gigaSwitch641DeskSfpTp=gigaSwitch641DeskSfpTp, nexansANS=nexansANS, iSwitch1043=iSwitch1043, gigaSwitchG542SfpDesk=gigaSwitchG542SfpDesk, gigaSwitchV2CopFib=gigaSwitchV2CopFib)
