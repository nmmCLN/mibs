#
# PySNMP MIB module IEC-62439-3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iec/IEC-62439-3-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:11:28 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, IpAddress, Gauge32, Counter32, Bits, MibIdentifier, ObjectIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "IpAddress", "Gauge32", "Counter32", "Bits", "MibIdentifier", "ObjectIdentity", "Unsigned32", "NotificationType")
DisplayString, RowStatus, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "MacAddress")
iec62439 = ModuleIdentity((1, 0, 62439))
iec62439.setRevisions(('2014-05-22 00:00', '2012-02-17 00:00', '2011-08-26 00:00', '2008-11-10 00:00', '2006-12-16 00:00',))
if mibBuilder.loadTexts: iec62439.setLastUpdated('201405220000Z')
if mibBuilder.loadTexts: iec62439.setOrganization('IEC/SC 65C')
mrp = MibIdentifier((1, 0, 62439, 1))
prp = MibIdentifier((1, 0, 62439, 2))
crp = MibIdentifier((1, 0, 62439, 3))
brp = MibIdentifier((1, 0, 62439, 4))
drp = MibIdentifier((1, 0, 62439, 5))
rrp = MibIdentifier((1, 0, 62439, 6))
ptp = MibIdentifier((1, 0, 62439, 7))
class SecondFraction(TextualConvention, Integer32):
    reference = 'IEC 62439-3'
    status = 'current'
    displayHint = 'd'

linkRedundancyEntityNotifications = MibIdentifier((1, 0, 62439, 2, 20))
linkRedundancyEntityObjects = MibIdentifier((1, 0, 62439, 2, 21))
linkRedundancyEntityConformance = MibIdentifier((1, 0, 62439, 2, 22))
lreConfiguration = MibIdentifier((1, 0, 62439, 2, 21, 0))
lreStatistics = MibIdentifier((1, 0, 62439, 2, 21, 1))
lreConfigurationGeneralGroup = MibIdentifier((1, 0, 62439, 2, 21, 0, 0))
lreConfigurationInterfaceGroup = MibIdentifier((1, 0, 62439, 2, 21, 0, 1))
lreStatisticsInterfaceGroup = MibIdentifier((1, 0, 62439, 2, 21, 1, 1))
lreManufacturerName = MibScalar((1, 0, 62439, 2, 21, 0, 0, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreManufacturerName.setStatus('current')
lreInterfaceCount = MibScalar((1, 0, 62439, 2, 21, 0, 0, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreInterfaceCount.setStatus('current')
lreConfigurationInterfaces = MibIdentifier((1, 0, 62439, 2, 21, 0, 1, 0))
lreInterfaceConfigTable = MibTable((1, 0, 62439, 2, 21, 0, 1, 0, 1), )
if mibBuilder.loadTexts: lreInterfaceConfigTable.setStatus('current')
lreInterfaceConfigEntry = MibTableRow((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1), ).setIndexNames((0, "IEC-62439-3-MIB", "lreInterfaceConfigIndex"))
if mibBuilder.loadTexts: lreInterfaceConfigEntry.setStatus('current')
lreInterfaceConfigIndex = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lreInterfaceConfigIndex.setStatus('current')
lreRowStatus = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lreRowStatus.setStatus('current')
lreNodeType = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("prpmode1", 1), ("hsr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreNodeType.setStatus('current')
lreNodeName = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreNodeName.setStatus('current')
lreVersionName = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreVersionName.setStatus('current')
lreMacAddress = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreMacAddress.setStatus('current')
lrePortAdminStateA = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notActive", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lrePortAdminStateA.setStatus('current')
lrePortAdminStateB = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notActive", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lrePortAdminStateB.setStatus('current')
lreLinkStatusA = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreLinkStatusA.setStatus('current')
lreLinkStatusB = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreLinkStatusB.setStatus('current')
lreDuplicateDiscard = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("doNotDiscard", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreDuplicateDiscard.setStatus('current')
lreTransparentReception = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("removeRCT", 1), ("passRCT", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreTransparentReception.setStatus('current')
lreHsrLREMode = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("modeh", 1), ("moden", 2), ("modet", 3), ("modeu", 4), ("modem", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreHsrLREMode.setStatus('current')
lreSwitchingEndNode = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("nonbridgingnode", 1), ("bridgingunspecified", 2), ("prpnode", 3), ("hsrredboxsan", 4), ("hsrnode", 5), ("hsrredboxhsr", 6), ("hsrredboxprpa", 7), ("hsrredboxprpb", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreSwitchingEndNode.setStatus('current')
lreRedBoxIdentity = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("id1a", 2), ("id1b", 3), ("id2a", 4), ("id2b", 5), ("id3a", 6), ("id3b", 7), ("id4a", 8), ("id4b", 9), ("id5a", 10), ("id5b", 11), ("id6a", 12), ("id6b", 13), ("id7a", 14), ("id7b", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreRedBoxIdentity.setStatus('current')
lreEvaluateSupervision = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreEvaluateSupervision.setStatus('current')
lreNodesTableClear = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noOp", 0), ("clearNodeTable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreNodesTableClear.setStatus('current')
lreProxyNodeTableClear = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noOp", 0), ("clearProxyNodeTable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreProxyNodeTableClear.setStatus('current')
lreDupListResideMaxTime = MibTableColumn((1, 0, 62439, 2, 21, 0, 1, 0, 1, 1, 19), SecondFraction().clone(26214)).setUnits('binaryFractionOfSecond').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lreDupListResideMaxTime.setStatus('current')
lreStatisticsInterfaces = MibIdentifier((1, 0, 62439, 2, 21, 1, 1, 0))
lreInterfaceStatsTable = MibTable((1, 0, 62439, 2, 21, 1, 1, 0, 1), )
if mibBuilder.loadTexts: lreInterfaceStatsTable.setStatus('current')
lreInterfaceStatsEntry = MibTableRow((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1), ).setIndexNames((0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"))
if mibBuilder.loadTexts: lreInterfaceStatsEntry.setStatus('current')
lreInterfaceStatsIndex = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lreInterfaceStatsIndex.setStatus('current')
lreCntTxA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntTxA.setStatus('current')
lreCntTxB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntTxB.setStatus('current')
lreCntTxC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntTxC.setStatus('current')
lreCntErrWrongLanA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrWrongLanA.setStatus('current')
lreCntErrWrongLanB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrWrongLanB.setStatus('current')
lreCntErrWrongLanC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrWrongLanC.setStatus('current')
lreCntRxA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntRxA.setStatus('current')
lreCntRxB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntRxB.setStatus('current')
lreCntRxC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntRxC.setStatus('current')
lreCntErrorsA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrorsA.setStatus('current')
lreCntErrorsB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrorsB.setStatus('current')
lreCntErrorsC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntErrorsC.setStatus('current')
lreCntNodes = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntNodes.setStatus('current')
lreCntProxyNodes = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntProxyNodes.setStatus('current')
lreCntUniqueA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntUniqueA.setStatus('current')
lreCntUniqueB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntUniqueB.setStatus('current')
lreCntUniqueC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntUniqueC.setStatus('current')
lreCntDuplicateA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntDuplicateA.setStatus('current')
lreCntDuplicateB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntDuplicateB.setStatus('current')
lreCntDuplicateC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntDuplicateC.setStatus('current')
lreCntMultiA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntMultiA.setStatus('current')
lreCntMultiB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntMultiB.setStatus('current')
lreCntMultiC = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntMultiC.setStatus('current')
lreCntOwnRxA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntOwnRxA.setStatus('current')
lreCntOwnRxB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreCntOwnRxB.setStatus('current')
lreNodesTable = MibTable((1, 0, 62439, 2, 21, 1, 1, 0, 2), )
if mibBuilder.loadTexts: lreNodesTable.setStatus('current')
lreNodesEntry = MibTableRow((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1), ).setIndexNames((0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"), (0, "IEC-62439-3-MIB", "lreNodesIndex"))
if mibBuilder.loadTexts: lreNodesEntry.setStatus('current')
lreNodesIndex = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lreNodesIndex.setStatus('current')
lreNodesMacAddress = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreNodesMacAddress.setStatus('current')
lreTimeLastSeenA = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreTimeLastSeenA.setStatus('current')
lreTimeLastSeenB = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreTimeLastSeenB.setStatus('current')
lreRemNodeType = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("danp", 0), ("redboxp", 1), ("vdanp", 2), ("danh", 3), ("redboxh", 4), ("vdanh", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreRemNodeType.setStatus('current')
lreProxyNodeTable = MibTable((1, 0, 62439, 2, 21, 1, 1, 0, 3), )
if mibBuilder.loadTexts: lreProxyNodeTable.setStatus('current')
lreProxyNodeEntry = MibTableRow((1, 0, 62439, 2, 21, 1, 1, 0, 3, 1), ).setIndexNames((0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"), (0, "IEC-62439-3-MIB", "lreProxyNodeIndex"))
if mibBuilder.loadTexts: lreProxyNodeEntry.setStatus('current')
lreProxyNodeIndex = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lreProxyNodeIndex.setStatus('current')
lreProxyNodeMacAddress = MibTableColumn((1, 0, 62439, 2, 21, 1, 1, 0, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lreProxyNodeMacAddress.setStatus('current')
linkRedundancyConformance = MibIdentifier((1, 0, 62439, 2, 22, 1))
lreGroups = MibIdentifier((1, 0, 62439, 2, 22, 1, 1))
lreDefaultGrp = ObjectGroup((1, 0, 62439, 2, 22, 1, 1, 1)).setObjects(("IEC-62439-3-MIB", "lreManufacturerName"), ("IEC-62439-3-MIB", "lreInterfaceCount"), ("IEC-62439-3-MIB", "lreRowStatus"), ("IEC-62439-3-MIB", "lreNodeType"), ("IEC-62439-3-MIB", "lreNodeName"), ("IEC-62439-3-MIB", "lreVersionName"), ("IEC-62439-3-MIB", "lreMacAddress"), ("IEC-62439-3-MIB", "lrePortAdminStateA"), ("IEC-62439-3-MIB", "lrePortAdminStateB"), ("IEC-62439-3-MIB", "lreLinkStatusA"), ("IEC-62439-3-MIB", "lreLinkStatusB"), ("IEC-62439-3-MIB", "lreDuplicateDiscard"), ("IEC-62439-3-MIB", "lreTransparentReception"), ("IEC-62439-3-MIB", "lreHsrLREMode"), ("IEC-62439-3-MIB", "lreSwitchingEndNode"), ("IEC-62439-3-MIB", "lreRedBoxIdentity"), ("IEC-62439-3-MIB", "lreEvaluateSupervision"), ("IEC-62439-3-MIB", "lreNodesTableClear"), ("IEC-62439-3-MIB", "lreProxyNodeTableClear"), ("IEC-62439-3-MIB", "lreDupListResideMaxTime"), ("IEC-62439-3-MIB", "lreCntTxA"), ("IEC-62439-3-MIB", "lreCntTxB"), ("IEC-62439-3-MIB", "lreCntTxC"), ("IEC-62439-3-MIB", "lreCntErrWrongLanA"), ("IEC-62439-3-MIB", "lreCntErrWrongLanB"), ("IEC-62439-3-MIB", "lreCntErrWrongLanC"), ("IEC-62439-3-MIB", "lreCntRxA"), ("IEC-62439-3-MIB", "lreCntRxB"), ("IEC-62439-3-MIB", "lreCntRxC"), ("IEC-62439-3-MIB", "lreCntErrorsA"), ("IEC-62439-3-MIB", "lreCntErrorsB"), ("IEC-62439-3-MIB", "lreCntErrorsC"), ("IEC-62439-3-MIB", "lreCntNodes"), ("IEC-62439-3-MIB", "lreCntProxyNodes"), ("IEC-62439-3-MIB", "lreCntUniqueA"), ("IEC-62439-3-MIB", "lreCntUniqueB"), ("IEC-62439-3-MIB", "lreCntUniqueC"), ("IEC-62439-3-MIB", "lreCntDuplicateA"), ("IEC-62439-3-MIB", "lreCntDuplicateB"), ("IEC-62439-3-MIB", "lreCntDuplicateC"), ("IEC-62439-3-MIB", "lreCntMultiA"), ("IEC-62439-3-MIB", "lreCntMultiB"), ("IEC-62439-3-MIB", "lreCntMultiC"), ("IEC-62439-3-MIB", "lreCntOwnRxA"), ("IEC-62439-3-MIB", "lreCntOwnRxB"), ("IEC-62439-3-MIB", "lreNodesMacAddress"), ("IEC-62439-3-MIB", "lreTimeLastSeenA"), ("IEC-62439-3-MIB", "lreTimeLastSeenB"), ("IEC-62439-3-MIB", "lreRemNodeType"), ("IEC-62439-3-MIB", "lreProxyNodeMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lreDefaultGrp = lreDefaultGrp.setStatus('current')
linkRedundancyCompliances = MibIdentifier((1, 0, 62439, 2, 22, 2))
linkRedundancyCompliance = ModuleCompliance((1, 0, 62439, 2, 22, 2, 1)).setObjects(("IEC-62439-3-MIB", "lreDefaultGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linkRedundancyCompliance = linkRedundancyCompliance.setStatus('current')
mibBuilder.exportSymbols("IEC-62439-3-MIB", lreEvaluateSupervision=lreEvaluateSupervision, lreNodeName=lreNodeName, lreCntDuplicateA=lreCntDuplicateA, lreCntNodes=lreCntNodes, lreInterfaceStatsEntry=lreInterfaceStatsEntry, lreNodesIndex=lreNodesIndex, lreDupListResideMaxTime=lreDupListResideMaxTime, lreCntUniqueC=lreCntUniqueC, lreGroups=lreGroups, lreManufacturerName=lreManufacturerName, lreVersionName=lreVersionName, lreCntUniqueB=lreCntUniqueB, lreConfiguration=lreConfiguration, lreNodeType=lreNodeType, brp=brp, lreInterfaceStatsIndex=lreInterfaceStatsIndex, SecondFraction=SecondFraction, lreCntProxyNodes=lreCntProxyNodes, lreTimeLastSeenA=lreTimeLastSeenA, linkRedundancyEntityNotifications=linkRedundancyEntityNotifications, lreConfigurationInterfaceGroup=lreConfigurationInterfaceGroup, lreCntRxA=lreCntRxA, iec62439=iec62439, lreCntMultiC=lreCntMultiC, lreMacAddress=lreMacAddress, lreCntErrWrongLanA=lreCntErrWrongLanA, lreCntDuplicateB=lreCntDuplicateB, lreCntRxB=lreCntRxB, lreStatistics=lreStatistics, lreInterfaceCount=lreInterfaceCount, lreDefaultGrp=lreDefaultGrp, lreNodesTableClear=lreNodesTableClear, crp=crp, PYSNMP_MODULE_ID=iec62439, lreSwitchingEndNode=lreSwitchingEndNode, lreProxyNodeTableClear=lreProxyNodeTableClear, lreTransparentReception=lreTransparentReception, lreLinkStatusA=lreLinkStatusA, lreCntErrWrongLanB=lreCntErrWrongLanB, lreProxyNodeTable=lreProxyNodeTable, lreProxyNodeEntry=lreProxyNodeEntry, lreCntOwnRxB=lreCntOwnRxB, lrePortAdminStateB=lrePortAdminStateB, lreStatisticsInterfaces=lreStatisticsInterfaces, lreCntRxC=lreCntRxC, linkRedundancyCompliance=linkRedundancyCompliance, lreHsrLREMode=lreHsrLREMode, lreCntErrorsC=lreCntErrorsC, lreCntUniqueA=lreCntUniqueA, lreCntOwnRxA=lreCntOwnRxA, lreCntTxB=lreCntTxB, lreInterfaceStatsTable=lreInterfaceStatsTable, lreCntErrorsA=lreCntErrorsA, lreRowStatus=lreRowStatus, lreCntDuplicateC=lreCntDuplicateC, drp=drp, lreCntTxA=lreCntTxA, ptp=ptp, linkRedundancyCompliances=linkRedundancyCompliances, lreNodesEntry=lreNodesEntry, lreRemNodeType=lreRemNodeType, prp=prp, lreDuplicateDiscard=lreDuplicateDiscard, mrp=mrp, lreCntErrWrongLanC=lreCntErrWrongLanC, lreNodesTable=lreNodesTable, linkRedundancyConformance=linkRedundancyConformance, lrePortAdminStateA=lrePortAdminStateA, lreConfigurationGeneralGroup=lreConfigurationGeneralGroup, lreStatisticsInterfaceGroup=lreStatisticsInterfaceGroup, lreNodesMacAddress=lreNodesMacAddress, lreInterfaceConfigEntry=lreInterfaceConfigEntry, lreCntMultiA=lreCntMultiA, lreCntMultiB=lreCntMultiB, lreProxyNodeIndex=lreProxyNodeIndex, lreProxyNodeMacAddress=lreProxyNodeMacAddress, lreInterfaceConfigTable=lreInterfaceConfigTable, linkRedundancyEntityConformance=linkRedundancyEntityConformance, lreConfigurationInterfaces=lreConfigurationInterfaces, lreLinkStatusB=lreLinkStatusB, lreRedBoxIdentity=lreRedBoxIdentity, lreTimeLastSeenB=lreTimeLastSeenB, rrp=rrp, linkRedundancyEntityObjects=linkRedundancyEntityObjects, lreCntErrorsB=lreCntErrorsB, lreInterfaceConfigIndex=lreInterfaceConfigIndex, lreCntTxC=lreCntTxC)
