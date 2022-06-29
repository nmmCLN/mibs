#
# PySNMP MIB module ENVIROMUX-1W-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nti/ENVIROMUX-1W-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:16 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Integer32, TimeTicks, Counter64, IpAddress, NotificationType, iso, enterprises, Counter32, ObjectIdentity, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Counter64", "IpAddress", "NotificationType", "iso", "enterprises", "Counter32", "ObjectIdentity", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
enviromux1W = ModuleIdentity((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12))
enviromux1W.setRevisions(('2020-12-11 02:00', '2020-08-18 14:00', '2016-02-03 14:00',))
if mibBuilder.loadTexts: enviromux1W.setLastUpdated('202012110200Z')
if mibBuilder.loadTexts: enviromux1W.setOrganization('Network Technologies Inc.')
nti = MibIdentifier((1, 3, 6, 1, 4, 1, 3699))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1))
hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 2))
otherProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 200))
masterUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1))
extSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2))
digInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3))
ipDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4))
eAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5))
smAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6))
enviromux1WTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100))
extSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1), )
if mibBuilder.loadTexts: extSensorTable.setStatus('current')
extSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "extSensorIndex"))
if mibBuilder.loadTexts: extSensorEntry.setStatus('current')
extSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: extSensorIndex.setStatus('current')
extSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 24))).clone(namedValues=NamedValues(("undefined", 0), ("temperature", 1), ("humidity", 2), ("dewPoint", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorType.setStatus('current')
extSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorDescription.setStatus('current')
extSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorValue.setStatus('current')
extSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorUnit.setStatus('current')
digInputTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1), )
if mibBuilder.loadTexts: digInputTable.setStatus('current')
digInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "digInputIndex"))
if mibBuilder.loadTexts: digInputEntry.setStatus('current')
digInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: digInputIndex.setStatus('current')
digInputDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digInputDescription.setStatus('current')
digInputValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("closed", 0), ("open", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: digInputValue.setStatus('current')
ipDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1), )
if mibBuilder.loadTexts: ipDeviceTable.setStatus('current')
ipDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "ipDeviceIndex"))
if mibBuilder.loadTexts: ipDeviceEntry.setStatus('current')
ipDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: ipDeviceIndex.setStatus('current')
ipDeviceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDeviceDescription.setStatus('current')
ipDeviceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notResponding", 0), ("responding", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDeviceValue.setStatus('current')
alertTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1), )
if mibBuilder.loadTexts: alertTable.setStatus('current')
alertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "alertIndex"))
if mibBuilder.loadTexts: alertEntry.setStatus('current')
alertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: alertIndex.setStatus('current')
alertEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEnabled.setStatus('current')
alertSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSensor.setStatus('current')
alertSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSensorValue.setStatus('current')
alertThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertThreshold.setStatus('current')
alertThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("lessThan", 0), ("greaterThan", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertThresholdType.setStatus('current')
alertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("enteringCritical", 1), ("critical", 2), ("exitingCritical", 3), ("waitingAckDismiss", 4), ("acknowledged", 5), ("dismissed", 6), ("disconnected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertStatus.setStatus('current')
smAlertTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1), )
if mibBuilder.loadTexts: smAlertTable.setStatus('current')
smAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "smAlertIndex"))
if mibBuilder.loadTexts: smAlertEntry.setStatus('current')
smAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: smAlertIndex.setStatus('current')
smAlertEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smAlertEnabled.setStatus('current')
smAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("enteringCritical", 1), ("critical", 2), ("exitingCritical", 3), ("waitingAckDismiss", 4), ("acknowledged", 5), ("dismissed", 6), ("disconnected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smAlertStatus.setStatus('current')
extSensorsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2))
digitalInputsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3))
ipDevicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4))
extSensor1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor1Trap.setStatus('current')
extSensor2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor2Trap.setStatus('current')
extSensor3Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 3)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor3Trap.setStatus('current')
extSensor4Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 4)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor4Trap.setStatus('current')
extSensor5Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 5)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor5Trap.setStatus('current')
extSensor6Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 6)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor6Trap.setStatus('current')
extSensor7Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 7)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor7Trap.setStatus('current')
extSensor8Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 8)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor8Trap.setStatus('current')
extSensor9Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 9)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor9Trap.setStatus('current')
extSensor10Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 10)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor10Trap.setStatus('current')
extSensor11Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 11)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor11Trap.setStatus('current')
extSensor12Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 12)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor12Trap.setStatus('current')
extSensor13Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 13)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor13Trap.setStatus('current')
extSensor14Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 14)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor14Trap.setStatus('current')
extSensor15Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 15)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor15Trap.setStatus('current')
extSensor16Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 16)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor16Trap.setStatus('current')
extSensor17Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 17)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor17Trap.setStatus('current')
extSensor18Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 18)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor18Trap.setStatus('current')
extSensor19Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 19)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor19Trap.setStatus('current')
extSensor20Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 20)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor20Trap.setStatus('current')
extSensor21Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 21)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor21Trap.setStatus('current')
extSensor22Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 22)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor22Trap.setStatus('current')
extSensor23Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 23)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor23Trap.setStatus('current')
extSensor24Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 24)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor24Trap.setStatus('current')
digInput1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "digInputValue"))
if mibBuilder.loadTexts: digInput1Trap.setStatus('current')
digInput2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "digInputValue"))
if mibBuilder.loadTexts: digInput2Trap.setStatus('current')
ipDevice1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice1Trap.setStatus('current')
ipDevice2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice2Trap.setStatus('current')
ipDevice3Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 3)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice3Trap.setStatus('current')
ipDevice4Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 4)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice4Trap.setStatus('current')
mibBuilder.exportSymbols("ENVIROMUX-1W-MIB", smAlertTable=smAlertTable, extSensorType=extSensorType, ipDevice3Trap=ipDevice3Trap, digInput1Trap=digInput1Trap, digInputValue=digInputValue, digInputTable=digInputTable, hardware=hardware, extSensor4Trap=extSensor4Trap, extSensor13Trap=extSensor13Trap, ipDeviceTable=ipDeviceTable, masterUnit=masterUnit, PYSNMP_MODULE_ID=enviromux1W, nti=nti, ipDevice1Trap=ipDevice1Trap, alertSensor=alertSensor, ipDeviceValue=ipDeviceValue, ipDevicesTraps=ipDevicesTraps, extSensor6Trap=extSensor6Trap, smAlertEntry=smAlertEntry, extSensor17Trap=extSensor17Trap, extSensorValue=extSensorValue, digInputIndex=digInputIndex, alertEnabled=alertEnabled, extSensor11Trap=extSensor11Trap, extSensor8Trap=extSensor8Trap, extSensor9Trap=extSensor9Trap, eAlerts=eAlerts, digInputs=digInputs, extSensor10Trap=extSensor10Trap, enviromux1W=enviromux1W, extSensor1Trap=extSensor1Trap, extSensor5Trap=extSensor5Trap, extSensor23Trap=extSensor23Trap, smAlertStatus=smAlertStatus, alertSensorValue=alertSensorValue, extSensor12Trap=extSensor12Trap, extSensor24Trap=extSensor24Trap, products=products, ipDevice2Trap=ipDevice2Trap, extSensorEntry=extSensorEntry, extSensorIndex=extSensorIndex, enviromux1WTraps=enviromux1WTraps, digInputDescription=digInputDescription, digitalInputsTraps=digitalInputsTraps, ipDeviceEntry=ipDeviceEntry, alertThreshold=alertThreshold, software=software, extSensorsTraps=extSensorsTraps, digInputEntry=digInputEntry, ipDevice4Trap=ipDevice4Trap, extSensor22Trap=extSensor22Trap, extSensor7Trap=extSensor7Trap, extSensor14Trap=extSensor14Trap, extSensor20Trap=extSensor20Trap, extSensor15Trap=extSensor15Trap, extSensorUnit=extSensorUnit, alertThresholdType=alertThresholdType, ipDevices=ipDevices, extSensor21Trap=extSensor21Trap, ipDeviceDescription=ipDeviceDescription, extSensorDescription=extSensorDescription, extSensor19Trap=extSensor19Trap, smAlertIndex=smAlertIndex, smAlerts=smAlerts, extSensor16Trap=extSensor16Trap, alertTable=alertTable, digInput2Trap=digInput2Trap, extSensor2Trap=extSensor2Trap, extSensors=extSensors, extSensor3Trap=extSensor3Trap, otherProduct=otherProduct, smAlertEnabled=smAlertEnabled, extSensor18Trap=extSensor18Trap, alertStatus=alertStatus, alertEntry=alertEntry, alertIndex=alertIndex, ipDeviceIndex=ipDeviceIndex, extSensorTable=extSensorTable)
