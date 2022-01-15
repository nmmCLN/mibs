#
# PySNMP MIB module AT-PLUGGABLE-DIAGNOSTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-PLUGGABLE-DIAGNOSTICS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, ObjectIdentity, Counter32, ModuleIdentity, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "ObjectIdentity", "Counter32", "ModuleIdentity", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atPluggableDiag = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28))
atPluggableDiag.setRevisions(('2015-07-17 00:00',))
if mibBuilder.loadTexts: atPluggableDiag.setLastUpdated('201507170000Z')
if mibBuilder.loadTexts: atPluggableDiag.setOrganization('Allied Telesis, Inc')
atPluggableDiagTable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1))
atPluggableDiagTempTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1), )
if mibBuilder.loadTexts: atPluggableDiagTempTable.setStatus('current')
atPluggableDiagTempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTempChannel"))
if mibBuilder.loadTexts: atPluggableDiagTempEntry.setStatus('current')
atPluggableDiagTempIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTempIfIndex.setStatus('current')
atPluggableDiagTempChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTempChannel.setStatus('current')
atPluggableDiagTempStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 3), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempStatusReading.setStatus('current')
atPluggableDiagTempCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempCurrentAlarm.setStatus('current')
atPluggableDiagTempAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 5), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMax.setStatus('current')
atPluggableDiagTempAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 6), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempAlarmMin.setStatus('current')
atPluggableDiagTempCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempCurrentWarning.setStatus('current')
atPluggableDiagTempWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 8), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempWarningMax.setStatus('current')
atPluggableDiagTempWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 1, 1, 9), Integer32()).setUnits('0.001 degree C').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTempWarningMin.setStatus('current')
atPluggableDiagVccTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2), )
if mibBuilder.loadTexts: atPluggableDiagVccTable.setStatus('current')
atPluggableDiagVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagVccChannel"))
if mibBuilder.loadTexts: atPluggableDiagVccEntry.setStatus('current')
atPluggableDiagVccIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagVccIfIndex.setStatus('current')
atPluggableDiagVccChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagVccChannel.setStatus('current')
atPluggableDiagVccStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 3), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccStatusReading.setStatus('current')
atPluggableDiagVccCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccCurrentAlarm.setStatus('current')
atPluggableDiagVccAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 5), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMax.setStatus('current')
atPluggableDiagVccAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 6), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccAlarmMin.setStatus('current')
atPluggableDiagVccCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccCurrentWarning.setStatus('current')
atPluggableDiagVccWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 8), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccWarningMax.setStatus('current')
atPluggableDiagVccWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 2, 1, 9), Integer32()).setUnits('0.0001 volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagVccWarningMin.setStatus('current')
atPluggableDiagTxBiasTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3), )
if mibBuilder.loadTexts: atPluggableDiagTxBiasTable.setStatus('current')
atPluggableDiagTxBiasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxBiasChannel"))
if mibBuilder.loadTexts: atPluggableDiagTxBiasEntry.setStatus('current')
atPluggableDiagTxBiasIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTxBiasIfIndex.setStatus('current')
atPluggableDiagTxBiasChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTxBiasChannel.setStatus('current')
atPluggableDiagTxBiasStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 3), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasStatusReading.setStatus('current')
atPluggableDiagTxBiasCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentAlarm.setStatus('current')
atPluggableDiagTxBiasAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 5), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMax.setStatus('current')
atPluggableDiagTxBiasAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 6), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasAlarmMin.setStatus('current')
atPluggableDiagTxBiasCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasCurrentWarning.setStatus('current')
atPluggableDiagTxBiasWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 8), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMax.setStatus('current')
atPluggableDiagTxBiasWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 3, 1, 9), Integer32()).setUnits('0.001 mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxBiasWarningMin.setStatus('current')
atPluggableDiagTxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4), )
if mibBuilder.loadTexts: atPluggableDiagTxPowerTable.setStatus('current')
atPluggableDiagTxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagTxPowerChannel"))
if mibBuilder.loadTexts: atPluggableDiagTxPowerEntry.setStatus('current')
atPluggableDiagTxPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagTxPowerIfIndex.setStatus('current')
atPluggableDiagTxPowerChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagTxPowerChannel.setStatus('current')
atPluggableDiagTxPowerStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 3), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerStatusReading.setStatus('current')
atPluggableDiagTxPowerCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentAlarm.setStatus('current')
atPluggableDiagTxPowerAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 5), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMax.setStatus('current')
atPluggableDiagTxPowerAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 6), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerAlarmMin.setStatus('current')
atPluggableDiagTxPowerCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerCurrentWarning.setStatus('current')
atPluggableDiagTxPowerWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 8), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMax.setStatus('current')
atPluggableDiagTxPowerWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 4, 1, 9), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagTxPowerWarningMin.setStatus('current')
atPluggableDiagRxPowerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5), )
if mibBuilder.loadTexts: atPluggableDiagRxPowerTable.setStatus('current')
atPluggableDiagRxPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxPowerChannel"))
if mibBuilder.loadTexts: atPluggableDiagRxPowerEntry.setStatus('current')
atPluggableDiagRxPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagRxPowerIfIndex.setStatus('current')
atPluggableDiagRxPowerChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagRxPowerChannel.setStatus('current')
atPluggableDiagRxPowerStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 3), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerStatusReading.setStatus('current')
atPluggableDiagRxPowerCurrentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentAlarm.setStatus('current')
atPluggableDiagRxPowerAlarmMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 5), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMax.setStatus('current')
atPluggableDiagRxPowerAlarmMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 6), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerAlarmMin.setStatus('current')
atPluggableDiagRxPowerCurrentWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerCurrentWarning.setStatus('current')
atPluggableDiagRxPowerWarningMax = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 8), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMax.setStatus('current')
atPluggableDiagRxPowerWarningMin = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 5, 1, 9), Integer32()).setUnits('0.0001 mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxPowerWarningMin.setStatus('current')
atPluggableDiagRxLosTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6), )
if mibBuilder.loadTexts: atPluggableDiagRxLosTable.setStatus('current')
atPluggableDiagRxLosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1), ).setIndexNames((0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosIfIndex"), (0, "AT-PLUGGABLE-DIAGNOSTICS-MIB", "atPluggableDiagRxLosChannel"))
if mibBuilder.loadTexts: atPluggableDiagRxLosEntry.setStatus('current')
atPluggableDiagRxLosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: atPluggableDiagRxLosIfIndex.setStatus('current')
atPluggableDiagRxLosChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: atPluggableDiagRxLosChannel.setStatus('current')
atPluggableDiagRxLosStatusReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 28, 1, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atPluggableDiagRxLosStatusReading.setStatus('current')
mibBuilder.exportSymbols("AT-PLUGGABLE-DIAGNOSTICS-MIB", atPluggableDiagRxLosChannel=atPluggableDiagRxLosChannel, atPluggableDiagTxPowerEntry=atPluggableDiagTxPowerEntry, atPluggableDiagTxPowerCurrentWarning=atPluggableDiagTxPowerCurrentWarning, atPluggableDiagRxLosEntry=atPluggableDiagRxLosEntry, atPluggableDiagVccAlarmMax=atPluggableDiagVccAlarmMax, atPluggableDiagVccStatusReading=atPluggableDiagVccStatusReading, atPluggableDiagTempWarningMax=atPluggableDiagTempWarningMax, atPluggableDiagTempAlarmMin=atPluggableDiagTempAlarmMin, atPluggableDiagTempTable=atPluggableDiagTempTable, atPluggableDiagTempChannel=atPluggableDiagTempChannel, atPluggableDiagVccAlarmMin=atPluggableDiagVccAlarmMin, atPluggableDiagTxPowerAlarmMax=atPluggableDiagTxPowerAlarmMax, atPluggableDiagTempIfIndex=atPluggableDiagTempIfIndex, atPluggableDiagTxBiasEntry=atPluggableDiagTxBiasEntry, PYSNMP_MODULE_ID=atPluggableDiag, atPluggableDiagRxPowerWarningMin=atPluggableDiagRxPowerWarningMin, atPluggableDiagTxPowerChannel=atPluggableDiagTxPowerChannel, atPluggableDiag=atPluggableDiag, atPluggableDiagRxLosTable=atPluggableDiagRxLosTable, atPluggableDiagTxBiasWarningMax=atPluggableDiagTxBiasWarningMax, atPluggableDiagTempStatusReading=atPluggableDiagTempStatusReading, atPluggableDiagRxLosIfIndex=atPluggableDiagRxLosIfIndex, atPluggableDiagTxBiasAlarmMax=atPluggableDiagTxBiasAlarmMax, atPluggableDiagVccCurrentAlarm=atPluggableDiagVccCurrentAlarm, atPluggableDiagTxBiasTable=atPluggableDiagTxBiasTable, atPluggableDiagTxBiasCurrentWarning=atPluggableDiagTxBiasCurrentWarning, atPluggableDiagTxBiasWarningMin=atPluggableDiagTxBiasWarningMin, atPluggableDiagTxPowerAlarmMin=atPluggableDiagTxPowerAlarmMin, atPluggableDiagTxPowerWarningMax=atPluggableDiagTxPowerWarningMax, atPluggableDiagRxPowerAlarmMax=atPluggableDiagRxPowerAlarmMax, atPluggableDiagRxLosStatusReading=atPluggableDiagRxLosStatusReading, atPluggableDiagTxBiasIfIndex=atPluggableDiagTxBiasIfIndex, atPluggableDiagTempAlarmMax=atPluggableDiagTempAlarmMax, atPluggableDiagTempEntry=atPluggableDiagTempEntry, atPluggableDiagTxPowerStatusReading=atPluggableDiagTxPowerStatusReading, atPluggableDiagTable=atPluggableDiagTable, atPluggableDiagRxPowerAlarmMin=atPluggableDiagRxPowerAlarmMin, atPluggableDiagVccEntry=atPluggableDiagVccEntry, atPluggableDiagVccWarningMin=atPluggableDiagVccWarningMin, atPluggableDiagRxPowerStatusReading=atPluggableDiagRxPowerStatusReading, atPluggableDiagTempWarningMin=atPluggableDiagTempWarningMin, atPluggableDiagTxPowerWarningMin=atPluggableDiagTxPowerWarningMin, atPluggableDiagRxPowerEntry=atPluggableDiagRxPowerEntry, atPluggableDiagRxPowerCurrentAlarm=atPluggableDiagRxPowerCurrentAlarm, atPluggableDiagRxPowerTable=atPluggableDiagRxPowerTable, atPluggableDiagRxPowerChannel=atPluggableDiagRxPowerChannel, atPluggableDiagRxPowerIfIndex=atPluggableDiagRxPowerIfIndex, atPluggableDiagVccIfIndex=atPluggableDiagVccIfIndex, atPluggableDiagTxBiasStatusReading=atPluggableDiagTxBiasStatusReading, atPluggableDiagVccCurrentWarning=atPluggableDiagVccCurrentWarning, atPluggableDiagTempCurrentWarning=atPluggableDiagTempCurrentWarning, atPluggableDiagTxBiasAlarmMin=atPluggableDiagTxBiasAlarmMin, atPluggableDiagTxPowerIfIndex=atPluggableDiagTxPowerIfIndex, atPluggableDiagVccChannel=atPluggableDiagVccChannel, atPluggableDiagTxBiasCurrentAlarm=atPluggableDiagTxBiasCurrentAlarm, atPluggableDiagTxPowerTable=atPluggableDiagTxPowerTable, atPluggableDiagVccWarningMax=atPluggableDiagVccWarningMax, atPluggableDiagTempCurrentAlarm=atPluggableDiagTempCurrentAlarm, atPluggableDiagTxBiasChannel=atPluggableDiagTxBiasChannel, atPluggableDiagRxPowerWarningMax=atPluggableDiagRxPowerWarningMax, atPluggableDiagRxPowerCurrentWarning=atPluggableDiagRxPowerCurrentWarning, atPluggableDiagVccTable=atPluggableDiagVccTable, atPluggableDiagTxPowerCurrentAlarm=atPluggableDiagTxPowerCurrentAlarm)
