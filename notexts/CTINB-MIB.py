#
# PySNMP MIB module CTINB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTINB-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctINBinfo, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctINBinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, Gauge32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
inbMonarchSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1))
inbMonarchSystemTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1), )
if mibBuilder.loadTexts: inbMonarchSystemTable.setStatus('mandatory')
inbMonarchSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbMonarchINB"))
if mibBuilder.loadTexts: inbMonarchSystemEntry.setStatus('mandatory')
inbMonarchSystemINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSystemINB.setStatus('mandatory')
inbMonarchStatusTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchStatusTimeStamp.setStatus('mandatory')
inbMonarchBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchBandwidth.setStatus('mandatory')
inbMonarchTDMSlotMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("userPolicy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotMode.setStatus('mandatory')
inbMonarchTDMSlotTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchTDMSlotTotal.setStatus('mandatory')
inbMonarchSystemTDMSlotActual = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSystemTDMSlotActual.setStatus('mandatory')
inbMonarchTDMSlotbandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchTDMSlotbandwidth.setStatus('mandatory')
inbMonarch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2))
inbMonarchTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1), )
if mibBuilder.loadTexts: inbMonarchTable.setStatus('mandatory')
inbMonarchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbMonarchSlot"), (0, "CTINB-MIB", "inbMonarchINB"))
if mibBuilder.loadTexts: inbMonarchEntry.setStatus('mandatory')
inbMonarchSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSlot.setStatus('mandatory')
inbMonarchINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchINB.setStatus('mandatory')
inbMonarchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standBy", 1), ("sysUndefined", 2), ("operational", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchStatus.setStatus('mandatory')
inbMonarchLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkUp", 1), ("linkDown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchLinkStatus.setStatus('mandatory')
inbMonarchLinkCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchLinkCapacity.setStatus('mandatory')
inbMonarchTDMSlotRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotRequest.setStatus('mandatory')
inbMonarchTDMSlotActual = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotActual.setStatus('mandatory')
inbMonarchRoundRobinControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchRoundRobinControl.setStatus('mandatory')
inbStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3))
inbStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1), )
if mibBuilder.loadTexts: inbStatsTable.setStatus('mandatory')
inbStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbStatsSlot"), (0, "CTINB-MIB", "inbStatsINB"))
if mibBuilder.loadTexts: inbStatsEntry.setStatus('mandatory')
inbStatsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsSlot.setStatus('mandatory')
inbStatsINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsINB.setStatus('mandatory')
inbStatsIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsIfindex.setStatus('mandatory')
inbStatsUniCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsUniCastCells.setStatus('mandatory')
inbStatsMultiCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsMultiCastCells.setStatus('mandatory')
inbStatsBroadCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsBroadCastCells.setStatus('mandatory')
inbStatsXmitCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsXmitCells.setStatus('mandatory')
inbStatsRecvSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsRecvSeqErrs.setStatus('mandatory')
inbStatsRecvChksumErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsRecvChksumErrs.setStatus('mandatory')
inbStatsxmitToFps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsxmitToFps.setStatus('mandatory')
inbStatsToFpsDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToFpsDrops.setStatus('mandatory')
inbStatsFromInbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsFromInbErrs.setStatus('mandatory')
inbStatsToINBDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToINBDrops.setStatus('mandatory')
inbStatsToInbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToInbErrs.setStatus('mandatory')
mibBuilder.exportSymbols("CTINB-MIB", inbStatsToInbErrs=inbStatsToInbErrs, inbMonarchStatus=inbMonarchStatus, inbMonarchSlot=inbMonarchSlot, inbMonarchLinkStatus=inbMonarchLinkStatus, inbMonarchRoundRobinControl=inbMonarchRoundRobinControl, inbStatsTable=inbStatsTable, inbStatsEntry=inbStatsEntry, inbMonarchBandwidth=inbMonarchBandwidth, inbMonarchTDMSlotMode=inbMonarchTDMSlotMode, inbMonarchTDMSlotbandwidth=inbMonarchTDMSlotbandwidth, inbStatsBroadCastCells=inbStatsBroadCastCells, inbMonarchEntry=inbMonarchEntry, inbMonarchTDMSlotActual=inbMonarchTDMSlotActual, inbMonarchSystemTable=inbMonarchSystemTable, inbStatsINB=inbStatsINB, inbMonarch=inbMonarch, inbStatsXmitCells=inbStatsXmitCells, inbStatsMultiCastCells=inbStatsMultiCastCells, inbStatsToFpsDrops=inbStatsToFpsDrops, inbMonarchSystemTDMSlotActual=inbMonarchSystemTDMSlotActual, inbMonarchLinkCapacity=inbMonarchLinkCapacity, inbMonarchTDMSlotRequest=inbMonarchTDMSlotRequest, inbStatsRecvChksumErrs=inbStatsRecvChksumErrs, inbMonarchSystemEntry=inbMonarchSystemEntry, inbMonarchSystemINB=inbMonarchSystemINB, inbStatsxmitToFps=inbStatsxmitToFps, inbStats=inbStats, inbStatsSlot=inbStatsSlot, inbStatsIfindex=inbStatsIfindex, inbStatsUniCastCells=inbStatsUniCastCells, inbMonarchSystem=inbMonarchSystem, inbMonarchTable=inbMonarchTable, inbStatsRecvSeqErrs=inbStatsRecvSeqErrs, inbMonarchINB=inbMonarchINB, inbMonarchStatusTimeStamp=inbMonarchStatusTimeStamp, inbStatsFromInbErrs=inbStatsFromInbErrs, inbMonarchTDMSlotTotal=inbMonarchTDMSlotTotal, inbStatsToINBDrops=inbStatsToINBDrops)
