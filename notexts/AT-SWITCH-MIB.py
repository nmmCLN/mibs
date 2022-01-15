#
# PySNMP MIB module AT-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SWITCH-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity, iso, ModuleIdentity, Gauge32, Unsigned32, NotificationType, Counter32, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity", "iso", "ModuleIdentity", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swi = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87))
swi.setRevisions(('2006-06-12 12:22',))
if mibBuilder.loadTexts: swi.setLastUpdated('200606121222Z')
if mibBuilder.loadTexts: swi.setOrganization('Allied Telesis, Inc')
swiPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1), )
if mibBuilder.loadTexts: swiPortTable.setStatus('current')
swiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swiPortNumber"))
if mibBuilder.loadTexts: swiPortEntry.setStatus('current')
swiPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortNumber.setStatus('current')
swiPortIngressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortIngressLimit.setStatus('current')
swiPortEgressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortEgressLimit.setStatus('current')
swiPortVlanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4), )
if mibBuilder.loadTexts: swiPortVlanTable.setStatus('current')
swiPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swiPortVlanPortNumber"), (0, "AT-SWITCH-MIB", "swiPortVlanVlanId"))
if mibBuilder.loadTexts: swiPortVlanEntry.setStatus('current')
swiPortVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortVlanPortNumber.setStatus('current')
swiPortVlanVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiPortVlanVlanId.setStatus('current')
swiPortVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swiPortVlanControl.setStatus('current')
swiPortVlanStateNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 9)).setObjects(("AT-SWITCH-MIB", "swiPortVlanPortNumber"), ("AT-SWITCH-MIB", "swiPortVlanVlanId"), ("AT-SWITCH-MIB", "swiPortVlanControl"))
if mibBuilder.loadTexts: swiPortVlanStateNotify.setStatus('current')
swi56xxPortCounterTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2), )
if mibBuilder.loadTexts: swi56xxPortCounterTable.setStatus('current')
swi56xxPortCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1), ).setIndexNames((0, "AT-SWITCH-MIB", "swi56xxPortNumber"))
if mibBuilder.loadTexts: swi56xxPortCounterEntry.setStatus('current')
swi56xxPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortNumber.setStatus('current')
swi56xxRxTx64kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx64kPkts.setStatus('current')
swi56xxRxTx65To127kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx65To127kPkts.setStatus('current')
swi56xxRxTx128To255kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx128To255kPkts.setStatus('current')
swi56xxRxTx256To511kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx256To511kPkts.setStatus('current')
swi56xxRxTx512To1023kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx512To1023kPkts.setStatus('current')
swi56xxRxTx1024ToMaxPktSzPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx1024ToMaxPktSzPkts.setStatus('current')
swi56xxRxTx519To1522kPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxRxTx519To1522kPkts.setStatus('current')
swi56xxPortRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOctets.setStatus('current')
swi56xxPortRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxPkts.setStatus('current')
swi56xxPortRxFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxFCSErrors.setStatus('current')
swi56xxPortRxMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxMulticastPkts.setStatus('current')
swi56xxPortRxBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxBroadcastPkts.setStatus('current')
swi56xxPortRxPauseMACCtlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxPauseMACCtlFrms.setStatus('current')
swi56xxPortRxOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOversizePkts.setStatus('current')
swi56xxPortRxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxFragments.setStatus('current')
swi56xxPortRxJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxJabbers.setStatus('current')
swi56xxPortRxMACControlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxMACControlFrms.setStatus('current')
swi56xxPortRxUnsupportOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxUnsupportOpcode.setStatus('current')
swi56xxPortRxAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxAlignmentErrors.setStatus('current')
swi56xxPortRxOutOfRngeLenFld = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxOutOfRngeLenFld.setStatus('current')
swi56xxPortRxSymErDurCarrier = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxSymErDurCarrier.setStatus('current')
swi56xxPortRxCarrierSenseErr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxCarrierSenseErr.setStatus('current')
swi56xxPortRxUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxUndersizePkts.setStatus('current')
swi56xxPortRxIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortRxIpInHdrErrors.setStatus('current')
swi56xxPortTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxOctets.setStatus('current')
swi56xxPortTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPkts.setStatus('current')
swi56xxPortTxFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFCSErrors.setStatus('current')
swi56xxPortTxMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxMulticastPkts.setStatus('current')
swi56xxPortTxBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxBroadcastPkts.setStatus('current')
swi56xxPortTxPauseMACCtlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPauseMACCtlFrms.setStatus('current')
swi56xxPortTxOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxOversizePkts.setStatus('current')
swi56xxPortTxFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFragments.setStatus('current')
swi56xxPortTxJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxJabbers.setStatus('current')
swi56xxPortTxPauseCtrlFrms = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxPauseCtrlFrms.setStatus('current')
swi56xxPortTxFrameWDeferrdTx = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFrameWDeferrdTx.setStatus('current')
swi56xxPortTxFrmWExcesDefer = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxFrmWExcesDefer.setStatus('current')
swi56xxPortTxSingleCollsnFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxSingleCollsnFrm.setStatus('current')
swi56xxPortTxMultCollsnFrm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxMultCollsnFrm.setStatus('current')
swi56xxPortTxLateCollsns = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxLateCollsns.setStatus('current')
swi56xxPortTxExcessivCollsns = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxExcessivCollsns.setStatus('current')
swi56xxPortTxCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortTxCollisionFrames.setStatus('current')
swi56xxPortMiscDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscDropEvents.setStatus('current')
swi56xxPortMiscTaggedPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscTaggedPktTx.setStatus('current')
swi56xxPortMiscTotalPktTxAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortMiscTotalPktTxAbort.setStatus('current')
swi56xxPortHWMultiTTLexpired = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiTTLexpired.setStatus('current')
swi56xxPortHWMultiBridgedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 47), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiBridgedFrames.setStatus('current')
swi56xxPortHWMultiRxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiRxDrops.setStatus('current')
swi56xxPortHWMultiTxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 2, 1, 49), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swi56xxPortHWMultiTxDrops.setStatus('current')
swiDebugVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3))
swiTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0))
swiDebugMemoryParityErrors = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swiDebugMemoryParityErrors.setStatus('current')
swiIntrusionDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 87, 0, 6)).setObjects(("AT-SWITCH-MIB", "swiPortNumber"))
if mibBuilder.loadTexts: swiIntrusionDetectionTrap.setStatus('current')
mibBuilder.exportSymbols("AT-SWITCH-MIB", swi56xxPortTxFrameWDeferrdTx=swi56xxPortTxFrameWDeferrdTx, swi56xxPortTxOversizePkts=swi56xxPortTxOversizePkts, swiPortVlanEntry=swiPortVlanEntry, swi56xxPortTxJabbers=swi56xxPortTxJabbers, swi56xxPortTxSingleCollsnFrm=swi56xxPortTxSingleCollsnFrm, swi56xxPortTxPauseMACCtlFrms=swi56xxPortTxPauseMACCtlFrms, swi56xxPortTxPkts=swi56xxPortTxPkts, swi56xxPortRxOversizePkts=swi56xxPortRxOversizePkts, swi56xxPortHWMultiBridgedFrames=swi56xxPortHWMultiBridgedFrames, swi56xxPortRxCarrierSenseErr=swi56xxPortRxCarrierSenseErr, swiPortVlanStateNotify=swiPortVlanStateNotify, swiPortVlanPortNumber=swiPortVlanPortNumber, swiTrap=swiTrap, swi56xxPortRxMACControlFrms=swi56xxPortRxMACControlFrms, swi56xxPortRxPkts=swi56xxPortRxPkts, swi56xxPortRxFCSErrors=swi56xxPortRxFCSErrors, swi56xxPortRxUndersizePkts=swi56xxPortRxUndersizePkts, swi56xxPortTxMulticastPkts=swi56xxPortTxMulticastPkts, swiPortVlanTable=swiPortVlanTable, swi56xxPortTxExcessivCollsns=swi56xxPortTxExcessivCollsns, swi56xxRxTx512To1023kPkts=swi56xxRxTx512To1023kPkts, swi56xxPortCounterEntry=swi56xxPortCounterEntry, swi56xxRxTx1024ToMaxPktSzPkts=swi56xxRxTx1024ToMaxPktSzPkts, swi56xxPortRxOctets=swi56xxPortRxOctets, swi56xxRxTx64kPkts=swi56xxRxTx64kPkts, swi56xxRxTx519To1522kPkts=swi56xxRxTx519To1522kPkts, swi56xxPortRxIpInHdrErrors=swi56xxPortRxIpInHdrErrors, swi56xxPortRxUnsupportOpcode=swi56xxPortRxUnsupportOpcode, swi56xxPortTxFCSErrors=swi56xxPortTxFCSErrors, swi56xxPortTxPauseCtrlFrms=swi56xxPortTxPauseCtrlFrms, swiDebugMemoryParityErrors=swiDebugMemoryParityErrors, swi56xxPortMiscDropEvents=swi56xxPortMiscDropEvents, swi56xxPortHWMultiRxDrops=swi56xxPortHWMultiRxDrops, swi56xxPortRxOutOfRngeLenFld=swi56xxPortRxOutOfRngeLenFld, swi56xxPortTxBroadcastPkts=swi56xxPortTxBroadcastPkts, swi56xxPortNumber=swi56xxPortNumber, swiPortVlanVlanId=swiPortVlanVlanId, swi56xxPortMiscTotalPktTxAbort=swi56xxPortMiscTotalPktTxAbort, swi56xxPortHWMultiTTLexpired=swi56xxPortHWMultiTTLexpired, swi56xxPortTxCollisionFrames=swi56xxPortTxCollisionFrames, swiPortEntry=swiPortEntry, swi56xxRxTx65To127kPkts=swi56xxRxTx65To127kPkts, swi56xxPortRxFragments=swi56xxPortRxFragments, swi56xxPortTxFragments=swi56xxPortTxFragments, swi56xxRxTx128To255kPkts=swi56xxRxTx128To255kPkts, swi=swi, swi56xxRxTx256To511kPkts=swi56xxRxTx256To511kPkts, swi56xxPortRxMulticastPkts=swi56xxPortRxMulticastPkts, swi56xxPortRxBroadcastPkts=swi56xxPortRxBroadcastPkts, PYSNMP_MODULE_ID=swi, swiPortNumber=swiPortNumber, swi56xxPortRxAlignmentErrors=swi56xxPortRxAlignmentErrors, swi56xxPortRxJabbers=swi56xxPortRxJabbers, swiPortVlanControl=swiPortVlanControl, swiPortEgressLimit=swiPortEgressLimit, swi56xxPortRxPauseMACCtlFrms=swi56xxPortRxPauseMACCtlFrms, swi56xxPortHWMultiTxDrops=swi56xxPortHWMultiTxDrops, swi56xxPortMiscTaggedPktTx=swi56xxPortMiscTaggedPktTx, swiPortTable=swiPortTable, swi56xxPortTxLateCollsns=swi56xxPortTxLateCollsns, swi56xxPortTxMultCollsnFrm=swi56xxPortTxMultCollsnFrm, swiIntrusionDetectionTrap=swiIntrusionDetectionTrap, swiDebugVariables=swiDebugVariables, swi56xxPortCounterTable=swi56xxPortCounterTable, swi56xxPortTxOctets=swi56xxPortTxOctets, swi56xxPortTxFrmWExcesDefer=swi56xxPortTxFrmWExcesDefer, swi56xxPortRxSymErDurCarrier=swi56xxPortRxSymErDurCarrier, swiPortIngressLimit=swiPortIngressLimit)
