#
# PySNMP MIB module CT-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-BROADCAST-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 16:08:15 2022
# On host fv-az208-754 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ctBroadcast, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctBroadcast")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, IpAddress, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, NotificationType, Bits, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "NotificationType", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctBroadcastCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1))
ctBroadcastCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1), )
if mibBuilder.loadTexts: ctBroadcastCtlTable.setStatus('mandatory')
ctBroadcastCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1), ).setIndexNames((0, "CT-BROADCAST-MIB", "ctBroadcastCtlSlotID"), (0, "CT-BROADCAST-MIB", "ctBroadcastCtlInterface"))
if mibBuilder.loadTexts: ctBroadcastCtlEntry.setStatus('mandatory')
ctBroadcastCtlSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastCtlSlotID.setStatus('mandatory')
ctBroadcastCtlInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastCtlInterface.setStatus('mandatory')
ctBroadcastTotalBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastTotalBroadcastFrames.setStatus('mandatory')
ctBroadcastPeakBroadcastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastRate.setStatus('mandatory')
ctBroadcastPeakBroadcastRateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastRateTime.setStatus('mandatory')
ctBroadcastPeakBroadcastClear = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noClear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBroadcastPeakBroadcastClear.setStatus('mandatory')
ctBroadcastDesiredBroadcastThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctBroadcastDesiredBroadcastThreshold.setStatus('mandatory')
mibBuilder.exportSymbols("CT-BROADCAST-MIB", ctBroadcastPeakBroadcastRateTime=ctBroadcastPeakBroadcastRateTime, ctBroadcastCtlSlotID=ctBroadcastCtlSlotID, ctBroadcastCtlTable=ctBroadcastCtlTable, ctBroadcastDesiredBroadcastThreshold=ctBroadcastDesiredBroadcastThreshold, ctBroadcastCtlInterface=ctBroadcastCtlInterface, ctBroadcastCtlEntry=ctBroadcastCtlEntry, ctBroadcastTotalBroadcastFrames=ctBroadcastTotalBroadcastFrames, ctBroadcastPeakBroadcastClear=ctBroadcastPeakBroadcastClear, ctBroadcastCtl=ctBroadcastCtl, ctBroadcastPeakBroadcastRate=ctBroadcastPeakBroadcastRate)
