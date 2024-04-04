#
# PySNMP MIB module BTI8xx-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-SFP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:28 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
mainSystem, = mibBuilder.importSymbols("BTI8xx-TC-MIB", "mainSystem")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter64, IpAddress, ObjectIdentity, MibIdentifier, ModuleIdentity, Unsigned32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Unsigned32", "TimeTicks", "Counter32")
MacAddress, TruthValue, DateAndTime, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention", "RowStatus")
sfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6))
sfp.setRevisions(('2015-11-20 12:00', '2013-12-27 12:00',))
if mibBuilder.loadTexts: sfp.setLastUpdated('201511201200Z')
if mibBuilder.loadTexts: sfp.setOrganization('Actus Networks Ltd.')
sfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1), )
if mibBuilder.loadTexts: sfpInfoTable.setStatus('current')
sfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpInfoIndex"))
if mibBuilder.loadTexts: sfpInfoEntry.setStatus('current')
sfpInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoIndex.setStatus('current')
sfpInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoLocation.setStatus('current')
sfpInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoSerialNumber.setStatus('current')
sfpInfoProductCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoProductCode.setStatus('current')
sfpInfoWigth = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoWigth.setStatus('current')
sfpInfoDistanceFiber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceFiber1.setStatus('current')
sfpInfoDistanceFiber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceFiber2.setStatus('current')
sfpInfoDistanceCopper = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInfoDistanceCopper.setStatus('current')
sfpInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2), )
if mibBuilder.loadTexts: sfpInventoryTable.setStatus('current')
sfpInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpInventoryIndex"))
if mibBuilder.loadTexts: sfpInventoryEntry.setStatus('current')
sfpInventoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryIndex.setStatus('current')
sfpInventoryLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryLocation.setStatus('current')
sfpInventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryType.setStatus('current')
sfpInventoryPecCode = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryPecCode.setStatus('current')
sfpInventoryCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryCLEI.setStatus('current')
sfpInventoryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryStatus.setStatus('current')
sfpInventoryEqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipped", 1), ("unEquipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpInventoryEqStatus.setStatus('current')
sfpDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3), )
if mibBuilder.loadTexts: sfpDiagnosticTable.setStatus('current')
sfpDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpDiagnosticIndex"))
if mibBuilder.loadTexts: sfpDiagnosticEntry.setStatus('current')
sfpDiagnosticIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticIndex.setStatus('current')
sfpDiagnosticLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticLocation.setStatus('current')
sfpDiagnosticCalibration = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticCalibration.setStatus('current')
sfpDiagnosticTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTemperature.setStatus('current')
sfpDiagnosticVoltageV = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticVoltageV.setStatus('current')
sfpDiagnosticTxBiasMA = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTxBiasMA.setStatus('current')
sfpDiagnosticTxPowerDbm = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticTxPowerDbm.setStatus('current')
sfpDiagnosticRxPowerDbm = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpDiagnosticRxPowerDbm.setStatus('current')
sfpStatusTable = MibTable((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4), )
if mibBuilder.loadTexts: sfpStatusTable.setStatus('current')
sfpStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1), ).setIndexNames((0, "BTI8xx-SFP-MIB", "sfpStatusIndex"))
if mibBuilder.loadTexts: sfpStatusEntry.setStatus('current')
sfpStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusIndex.setStatus('current')
sfpStatusLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusLocation.setStatus('current')
sfpStatusEqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("equipped", 1), ("unEquipped", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusEqStatus.setStatus('current')
sfpStatusRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusRxStatus.setStatus('current')
sfpStatusTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 6, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpStatusTxStatus.setStatus('current')
mibBuilder.exportSymbols("BTI8xx-SFP-MIB", sfpInfoDistanceFiber1=sfpInfoDistanceFiber1, sfpInventoryStatus=sfpInventoryStatus, sfpDiagnosticIndex=sfpDiagnosticIndex, sfpStatusIndex=sfpStatusIndex, sfpDiagnosticVoltageV=sfpDiagnosticVoltageV, sfpDiagnosticCalibration=sfpDiagnosticCalibration, sfpInventoryIndex=sfpInventoryIndex, sfpInfoProductCode=sfpInfoProductCode, sfp=sfp, sfpStatusTable=sfpStatusTable, sfpInfoDistanceFiber2=sfpInfoDistanceFiber2, sfpStatusEntry=sfpStatusEntry, sfpInfoDistanceCopper=sfpInfoDistanceCopper, sfpInventoryCLEI=sfpInventoryCLEI, sfpStatusRxStatus=sfpStatusRxStatus, sfpStatusEqStatus=sfpStatusEqStatus, sfpInfoIndex=sfpInfoIndex, sfpInfoSerialNumber=sfpInfoSerialNumber, sfpStatusLocation=sfpStatusLocation, sfpInfoLocation=sfpInfoLocation, sfpInfoEntry=sfpInfoEntry, sfpDiagnosticLocation=sfpDiagnosticLocation, sfpInventoryPecCode=sfpInventoryPecCode, sfpInventoryTable=sfpInventoryTable, PYSNMP_MODULE_ID=sfp, sfpDiagnosticTxPowerDbm=sfpDiagnosticTxPowerDbm, sfpStatusTxStatus=sfpStatusTxStatus, sfpInventoryEqStatus=sfpInventoryEqStatus, sfpDiagnosticTxBiasMA=sfpDiagnosticTxBiasMA, sfpDiagnosticRxPowerDbm=sfpDiagnosticRxPowerDbm, sfpInfoTable=sfpInfoTable, sfpInventoryLocation=sfpInventoryLocation, sfpDiagnosticTemperature=sfpDiagnosticTemperature, sfpDiagnosticTable=sfpDiagnosticTable, sfpDiagnosticEntry=sfpDiagnosticEntry, sfpInventoryEntry=sfpInventoryEntry, sfpInventoryType=sfpInventoryType, sfpInfoWigth=sfpInfoWigth)
