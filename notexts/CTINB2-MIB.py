#
# PySNMP MIB module CTINB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTINB2-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:40 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctINBinfo2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctINBinfo2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Bits, NotificationType, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter32", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctInbUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1))
ctInbUtilInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctInbUtilInterval.setStatus('mandatory')
ctInbUtilTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2), )
if mibBuilder.loadTexts: ctInbUtilTable.setStatus('mandatory')
ctInbUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1), ).setIndexNames((0, "CTINB2-MIB", "ctInbUtilSrcSlot"), (0, "CTINB2-MIB", "ctInbUtilDestSlot"))
if mibBuilder.loadTexts: ctInbUtilEntry.setStatus('mandatory')
ctInbUtilSrcSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilSrcSlot.setStatus('mandatory')
ctInbUtilDestSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilDestSlot.setStatus('mandatory')
ctInbUtilHiByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountA.setStatus('mandatory')
ctInbUtilLoByteCountA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountA.setStatus('mandatory')
ctInbUtilHiByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilHiByteCountB.setStatus('mandatory')
ctInbUtilLoByteCountB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilLoByteCountB.setStatus('mandatory')
ctInbUtilAbsoluteA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteA.setStatus('mandatory')
ctInbUtilAbsoluteB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteB.setStatus('mandatory')
ctInbUtilAbsoluteTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctInbUtilAbsoluteTotal.setStatus('mandatory')
mibBuilder.exportSymbols("CTINB2-MIB", ctInbUtilDestSlot=ctInbUtilDestSlot, ctInbUtilAbsoluteA=ctInbUtilAbsoluteA, ctInbUtilAbsoluteB=ctInbUtilAbsoluteB, ctInbUtilEntry=ctInbUtilEntry, ctInbUtilHiByteCountA=ctInbUtilHiByteCountA, ctInbUtilLoByteCountA=ctInbUtilLoByteCountA, ctInbUtilTable=ctInbUtilTable, ctInbUtilSrcSlot=ctInbUtilSrcSlot, ctInbUtilInterval=ctInbUtilInterval, ctInbUtilLoByteCountB=ctInbUtilLoByteCountB, ctInbUtil=ctInbUtil, ctInbUtilAbsoluteTotal=ctInbUtilAbsoluteTotal, ctInbUtilHiByteCountB=ctInbUtilHiByteCountB)
