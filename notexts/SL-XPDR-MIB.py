#
# PySNMP MIB module SL-XPDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-XPDR-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:44 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ModuleIdentity, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, ObjectIdentity, Gauge32, Counter64, Bits, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "iso", "IpAddress")
TextualConvention, DisplayString, TimeStamp, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "TruthValue", "RowStatus")
slXpdr = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 8))
if mibBuilder.loadTexts: slXpdr.setLastUpdated('200501250000Z')
if mibBuilder.loadTexts: slXpdr.setOrganization('PacketLight Networks Ltd.')
slXpdrConn = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1))
slXpdrLastChange = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 6))
slXpdrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7))
slXpdrTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0))
class TsMaskBits(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class XpdrServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 118, 120, 121, 170, 171, 1701))
    namedValues = NamedValues(("ds3Sts1", 1), ("fe", 2), ("escon", 3), ("dvbVideo", 4), ("fc1gFicon", 5), ("gbE", 6), ("fc2g", 7), ("oc3Stm1", 8), ("oc12Stm4", 9), ("oc48Stm16", 10), ("other", 11), ("fc4g", 12), ("infiniband25G", 13), ("otn27g", 14), ("oc24gpon", 15), ("smpteSdi", 16), ("copperFe", 17), ("copperGbe", 18), ("mux2GbE", 19), ("mux4GbE", 20), ("xpdr5G", 21), ("ficon1g", 22), ("ficon2g", 23), ("stm1", 24), ("stm4", 25), ("stm16", 26), ("gpon248", 27), ("ficon4g", 28), ("eth10m", 29), ("xfp10oc192", 30), ("xfp10stm64", 31), ("xfp10GbEWan", 32), ("xfp10GbELan", 33), ("xfp10otu2", 34), ("xfp10GFC", 35), ("xfp10GbEWanStm64", 36), ("mux1GbE", 37), ("mux1GbERegen", 38), ("mux2GbERegen", 39), ("mux4GbERegen", 40), ("fc8g", 41), ("ficon8g", 42), ("mux10GbE", 43), ("syncEgbE", 44), ("noPm10GbE", 45), ("totu2", 46), ("otu1e", 50), ("otu2e", 51), ("otu1f", 52), ("otu2f", 53), ("oc192ToOtu2", 54), ("stm64ToOtu2", 55), ("gbe10WanToOtu2", 56), ("gbe10LanToOtu2A", 57), ("gbe10LanToOtu1e", 58), ("gbe10LanToOtu2e", 59), ("gbe10LanToOtu2B", 60), ("fc10LanToOtu1f", 61), ("fc10LanToOtu2f", 62), ("fc8LanToOtu2", 63), ("otu3", 64), ("oc768", 65), ("stm256", 66), ("otu4", 67), ("gbe40lan", 68), ("gbe100lan", 69), ("fc16g", 70), ("smpteHdSdi", 71), ("smpteSdSdi", 72), ("smpte3gSdi", 73), ("smpte3dSdi", 74), ("smpteHdSdiNtsc", 75), ("smpte3gSdiNtsc", 76), ("fc16gNoIsl", 77), ("fc32g", 78), ("cpri1", 81), ("cpri2", 82), ("cpri3", 83), ("cpri4", 84), ("cpri5", 85), ("cpri6", 86), ("cpri7", 87), ("enc10GbELan", 91), ("enc1GbELan", 92), ("encfc1g", 93), ("encfc2g", 94), ("encfc4g", 95), ("encfc8g", 96), ("encfc16g", 97), ("encfc10g", 98), ("enc1GbE10g", 99), ("encGbe40lan", 100), ("encGbe100lan", 101), ("encOtu2", 102), ("encOtu2e", 103), ("encOtu3", 104), ("encOtu4", 105), ("encOc192", 106), ("encStm64", 107), ("encfc32g", 108), ("encfc16gNoIsl", 110), ("encCpri1", 111), ("encCpri2", 112), ("encCpri3", 113), ("encCpri4", 114), ("encCpri5", 115), ("encCpri6", 116), ("encCpri7", 117), ("enc10GbENoPm", 118), ("otuc2", 120), ("encOtuc2", 121), ("copper10m", 170), ("copper10mAn", 171), ("copperFeAn", 1701))

xpdrConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1), )
if mibBuilder.loadTexts: xpdrConnConfigTable.setStatus('current')
xpdrConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1), ).setIndexNames((0, "SL-XPDR-MIB", "xpdrConnConfigIf1"), (0, "SL-XPDR-MIB", "xpdrConnConfigIf2"))
if mibBuilder.loadTexts: xpdrConnConfigEntry.setStatus('current')
xpdrConnConfigIf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigIf1.setStatus('current')
xpdrConnConfigIf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigIf2.setStatus('current')
xpdrConnConfigRateControlAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigRateControlAdmin.setStatus('current')
xpdrConnConfigRateControlOper = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrConnConfigRateControlOper.setStatus('current')
xpdrConnConfigLosPropagation = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigLosPropagation.setStatus('current')
xpdrServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 6), XpdrServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrServiceType.setStatus('current')
xpdrConnAddMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask.setStatus('current')
xpdrMuxInbandAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("standby", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrMuxInbandAdmin.setStatus('current')
xpdrMuxInbandOper = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xpdrMuxInbandOper.setStatus('current')
xpdrDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bidirectional", 1), ("unidirectionalTx", 2), ("unidirectionalRx", 3), ("loopback", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrDirection.setStatus('current')
xpdrConnConfigCpriRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnConfigCpriRateControl.setStatus('current')
xpdrFaultPropagationDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrFaultPropagationDelay.setStatus('current')
xpdrFecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrFecMode.setStatus('current')
xpdrConnAddMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 14), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask1.setStatus('current')
xpdrConnAddMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 15), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrConnAddMask2.setStatus('current')
xpdrCryptoUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 1, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xpdrCryptoUser.setStatus('current')
oduXcConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2), )
if mibBuilder.loadTexts: oduXcConnConfigTable.setStatus('current')
oduXcConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1), ).setIndexNames((0, "SL-XPDR-MIB", "oduXcConnConfigP1"), (0, "SL-XPDR-MIB", "oduXcConnConfigP2"))
if mibBuilder.loadTexts: oduXcConnConfigEntry.setStatus('current')
oduXcConnConfigP1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigP1.setStatus('current')
oduXcConnConfigP2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigP2.setStatus('current')
oduXcConnConfigProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigProtected.setStatus('current')
oduXcConnConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oduXcConnConfigRowStatus.setStatus('current')
tribXcConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3), )
if mibBuilder.loadTexts: tribXcConnConfigTable.setStatus('current')
tribXcConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1), ).setIndexNames((0, "SL-XPDR-MIB", "tribXcConnConfigP1"), (0, "SL-XPDR-MIB", "tribXcConnConfigP2"))
if mibBuilder.loadTexts: tribXcConnConfigEntry.setStatus('current')
tribXcConnConfigP1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigP1.setStatus('current')
tribXcConnConfigP2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 2), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigP2.setStatus('current')
tribXcConnServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 3), XpdrServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnServiceType.setStatus('current')
tribXcConnMask1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 4), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnMask1.setStatus('current')
tribXcConnMask2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 5), TsMaskBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tribXcConnMask2.setStatus('current')
tribXcConnConfigProtected = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigProtected.setStatus('current')
tribXcConnConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tribXcConnConfigRowStatus.setStatus('current')
smmOwnerMode = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gui", 1), ("ems", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smmOwnerMode.setStatus('current')
xpdrConnConfigTableChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 1))
if mibBuilder.loadTexts: xpdrConnConfigTableChange.setStatus('current')
xpdrConnConfigTableChange0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 8, 7, 0, 1))
if mibBuilder.loadTexts: xpdrConnConfigTableChange0.setStatus('current')
mibBuilder.exportSymbols("SL-XPDR-MIB", slXpdrTraps=slXpdrTraps, xpdrConnConfigCpriRateControl=xpdrConnConfigCpriRateControl, oduXcConnConfigTable=oduXcConnConfigTable, tribXcConnConfigRowStatus=tribXcConnConfigRowStatus, slXpdrConn=slXpdrConn, tribXcConnConfigP1=tribXcConnConfigP1, TsMaskBits=TsMaskBits, xpdrServiceType=xpdrServiceType, xpdrCryptoUser=xpdrCryptoUser, oduXcConnConfigRowStatus=oduXcConnConfigRowStatus, PYSNMP_MODULE_ID=slXpdr, XpdrServiceType=XpdrServiceType, slXpdrLastChange=slXpdrLastChange, tribXcConnServiceType=tribXcConnServiceType, xpdrConnConfigIf2=xpdrConnConfigIf2, tribXcConnConfigTable=tribXcConnConfigTable, xpdrConnConfigLosPropagation=xpdrConnConfigLosPropagation, oduXcConnConfigP1=oduXcConnConfigP1, oduXcConnConfigProtected=oduXcConnConfigProtected, tribXcConnMask2=tribXcConnMask2, xpdrConnConfigTableChange0=xpdrConnConfigTableChange0, xpdrFecMode=xpdrFecMode, xpdrConnAddMask1=xpdrConnAddMask1, xpdrMuxInbandOper=xpdrMuxInbandOper, xpdrConnConfigEntry=xpdrConnConfigEntry, tribXcConnMask1=tribXcConnMask1, tribXcConnConfigProtected=tribXcConnConfigProtected, oduXcConnConfigEntry=oduXcConnConfigEntry, slXpdrTraps0=slXpdrTraps0, xpdrConnConfigRateControlOper=xpdrConnConfigRateControlOper, xpdrFaultPropagationDelay=xpdrFaultPropagationDelay, smmOwnerMode=smmOwnerMode, xpdrConnConfigRateControlAdmin=xpdrConnConfigRateControlAdmin, xpdrConnAddMask=xpdrConnAddMask, oduXcConnConfigP2=oduXcConnConfigP2, tribXcConnConfigP2=tribXcConnConfigP2, xpdrConnAddMask2=xpdrConnAddMask2, xpdrConnConfigIf1=xpdrConnConfigIf1, slXpdr=slXpdr, xpdrConnConfigTableChange=xpdrConnConfigTableChange, xpdrConnConfigTable=xpdrConnConfigTable, tribXcConnConfigEntry=tribXcConnConfigEntry, xpdrMuxInbandAdmin=xpdrMuxInbandAdmin, xpdrDirection=xpdrDirection)
