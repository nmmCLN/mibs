#
# PySNMP MIB module ENVIROMUX-1W-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nti/ENVIROMUX-1W-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:27 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, ObjectIdentity, Unsigned32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, MibIdentifier, enterprises, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "MibIdentifier", "enterprises", "Gauge32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
enviromux1W = ModuleIdentity((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12))
enviromux1W.setRevisions(('2020-12-11 02:00', '2020-08-18 14:00', '2016-02-03 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: enviromux1W.setRevisionsDescriptions(('Rev. 1.02 - Updated Digital Input 2 SNMP Trap ID', 'Rev. 1.01 - Adding extended external sensor trap OIDs', 'Rev. 1.00 - Initial version',))
if mibBuilder.loadTexts: enviromux1W.setLastUpdated('202012110200Z')
if mibBuilder.loadTexts: enviromux1W.setOrganization('Network Technologies Inc.')
if mibBuilder.loadTexts: enviromux1W.setContactInfo('Network Technologies Inc.\n         \n          Postal: 1275 Danner Dr,\n                  Aurora, OH 442022\n                  US\n                 \n          Tel: 330-562-7070\n          Fax: 330-562-1999\n             \n          WEB: www.networktechinc.com')
if mibBuilder.loadTexts: enviromux1W.setDescription('E-1W MIB file.')
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
if mibBuilder.loadTexts: extSensorTable.setDescription('Table of external Sensors entries')
extSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "extSensorIndex"))
if mibBuilder.loadTexts: extSensorEntry.setStatus('current')
if mibBuilder.loadTexts: extSensorEntry.setDescription('An external sensor entry')
extSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: extSensorIndex.setStatus('current')
if mibBuilder.loadTexts: extSensorIndex.setDescription('The index of the external sensor entry 1..6')
extSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 24))).clone(namedValues=NamedValues(("undefined", 0), ("temperature", 1), ("humidity", 2), ("dewPoint", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorType.setStatus('current')
if mibBuilder.loadTexts: extSensorType.setDescription('Sensor Type')
extSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorDescription.setStatus('current')
if mibBuilder.loadTexts: extSensorDescription.setDescription('Sensor Description')
extSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorValue.setStatus('current')
if mibBuilder.loadTexts: extSensorValue.setDescription('The value of the external sensor reading. For temperature, voltage, current or low voltage,  it is presented in tenths of degrees/volts')
extSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extSensorUnit.setStatus('current')
if mibBuilder.loadTexts: extSensorUnit.setDescription('The measuremnet unit for this sensor in numeric format. It is important only for temperature')
digInputTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1), )
if mibBuilder.loadTexts: digInputTable.setStatus('current')
if mibBuilder.loadTexts: digInputTable.setDescription('Table of digital input entries')
digInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "digInputIndex"))
if mibBuilder.loadTexts: digInputEntry.setStatus('current')
if mibBuilder.loadTexts: digInputEntry.setDescription('A digital input entry')
digInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: digInputIndex.setStatus('current')
if mibBuilder.loadTexts: digInputIndex.setDescription('The index of the digital input entry 1..2')
digInputDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digInputDescription.setStatus('current')
if mibBuilder.loadTexts: digInputDescription.setDescription('Sensor Description')
digInputValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("closed", 0), ("open", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: digInputValue.setStatus('current')
if mibBuilder.loadTexts: digInputValue.setDescription('The value of the digital reading')
ipDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1), )
if mibBuilder.loadTexts: ipDeviceTable.setStatus('current')
if mibBuilder.loadTexts: ipDeviceTable.setDescription('Table of digital input entries')
ipDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "ipDeviceIndex"))
if mibBuilder.loadTexts: ipDeviceEntry.setStatus('current')
if mibBuilder.loadTexts: ipDeviceEntry.setDescription('A digital input entry')
ipDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: ipDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: ipDeviceIndex.setDescription('The index of the ip device entry 1..4')
ipDeviceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDeviceDescription.setStatus('current')
if mibBuilder.loadTexts: ipDeviceDescription.setDescription('Sensor Description')
ipDeviceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notResponding", 0), ("responding", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipDeviceValue.setStatus('current')
if mibBuilder.loadTexts: ipDeviceValue.setDescription('The result of the ip device ping test')
alertTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1), )
if mibBuilder.loadTexts: alertTable.setStatus('current')
if mibBuilder.loadTexts: alertTable.setDescription('Table of alert entries')
alertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "alertIndex"))
if mibBuilder.loadTexts: alertEntry.setStatus('current')
if mibBuilder.loadTexts: alertEntry.setDescription('An alert entry')
alertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: alertIndex.setStatus('current')
if mibBuilder.loadTexts: alertIndex.setDescription('The index of the alert entry 1..32')
alertEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEnabled.setStatus('current')
if mibBuilder.loadTexts: alertEnabled.setDescription('Shows if alert is enabled 0..1')
alertSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSensor.setStatus('current')
if mibBuilder.loadTexts: alertSensor.setDescription('Alert Sensor Description')
alertSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSensorValue.setStatus('current')
if mibBuilder.loadTexts: alertSensorValue.setDescription('The value of the sensor for analog sensors or open/closed for digital inputs')
alertThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertThreshold.setStatus('current')
if mibBuilder.loadTexts: alertThreshold.setDescription('The value of the alert threshold for analog sensors, irrelevant for alerts for digital inputs')
alertThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("lessThan", 0), ("greaterThan", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertThresholdType.setStatus('current')
if mibBuilder.loadTexts: alertThresholdType.setDescription('The type of the alert threshold for analog sensors, irrelevant for alerts for digital inputs')
alertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("enteringCritical", 1), ("critical", 2), ("exitingCritical", 3), ("waitingAckDismiss", 4), ("acknowledged", 5), ("dismissed", 6), ("disconnected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertStatus.setStatus('current')
if mibBuilder.loadTexts: alertStatus.setDescription('The current status of the alert')
smAlertTable = MibTable((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1), )
if mibBuilder.loadTexts: smAlertTable.setStatus('current')
if mibBuilder.loadTexts: smAlertTable.setDescription('Table of alert entries')
smAlertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1), ).setIndexNames((0, "ENVIROMUX-1W-MIB", "smAlertIndex"))
if mibBuilder.loadTexts: smAlertEntry.setStatus('current')
if mibBuilder.loadTexts: smAlertEntry.setDescription('A smart alert entry')
smAlertIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: smAlertIndex.setStatus('current')
if mibBuilder.loadTexts: smAlertIndex.setDescription('The index of the alert entry (only one)')
smAlertEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smAlertEnabled.setStatus('current')
if mibBuilder.loadTexts: smAlertEnabled.setDescription('Shows if alert is enabled 0..1')
smAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("normal", 0), ("enteringCritical", 1), ("critical", 2), ("exitingCritical", 3), ("waitingAckDismiss", 4), ("acknowledged", 5), ("dismissed", 6), ("disconnected", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smAlertStatus.setStatus('current')
if mibBuilder.loadTexts: smAlertStatus.setDescription('The current status of the alert')
extSensorsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2))
digitalInputsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3))
ipDevicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4))
extSensor1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor1Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor1Trap.setDescription('Trap issued when external sensor 1 has a notification to send')
extSensor2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor2Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor2Trap.setDescription('Trap issued when external sensor 2 has a notification to send')
extSensor3Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 3)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor3Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor3Trap.setDescription('Trap issued when external sensor 3 has a notification to send')
extSensor4Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 4)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor4Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor4Trap.setDescription('Trap issued when external sensor 4 has a notification to send')
extSensor5Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 5)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor5Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor5Trap.setDescription('Trap issued when external sensor 5 has a notification to send')
extSensor6Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 6)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor6Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor6Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor7Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 7)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor7Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor7Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor8Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 8)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor8Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor8Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor9Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 9)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor9Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor9Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor10Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 10)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor10Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor10Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor11Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 11)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor11Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor11Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor12Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 12)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor12Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor12Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor13Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 13)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor13Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor13Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor14Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 14)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor14Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor14Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor15Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 15)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor15Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor15Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor16Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 16)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor16Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor16Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor17Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 17)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor17Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor17Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor18Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 18)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor18Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor18Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor19Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 19)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor19Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor19Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor20Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 20)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor20Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor20Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor21Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 21)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor21Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor21Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor22Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 22)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor22Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor22Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor23Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 23)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor23Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor23Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
extSensor24Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 24)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "extSensorValue"), ("ENVIROMUX-1W-MIB", "extSensorUnit"))
if mibBuilder.loadTexts: extSensor24Trap.setStatus('current')
if mibBuilder.loadTexts: extSensor24Trap.setDescription('Trap issued when external sensor 6 has a notification to send')
digInput1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "digInputValue"))
if mibBuilder.loadTexts: digInput1Trap.setStatus('current')
if mibBuilder.loadTexts: digInput1Trap.setDescription('Trap issued when digital input 1 has a notification to send')
digInput2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "digInputValue"))
if mibBuilder.loadTexts: digInput2Trap.setStatus('current')
if mibBuilder.loadTexts: digInput2Trap.setDescription('Trap issued when digital input 2 has a notification to send')
ipDevice1Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 1)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice1Trap.setStatus('current')
if mibBuilder.loadTexts: ipDevice1Trap.setDescription('Trap issued when IP device 1 has a notification to send')
ipDevice2Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 2)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice2Trap.setStatus('current')
if mibBuilder.loadTexts: ipDevice2Trap.setDescription('Trap issued when IP device 2 has a notification to send')
ipDevice3Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 3)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice3Trap.setStatus('current')
if mibBuilder.loadTexts: ipDevice3Trap.setDescription('Trap issued when IP device 3 has a notification to send')
ipDevice4Trap = NotificationType((1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 4)).setObjects(("ENVIROMUX-1W-MIB", "alertStatus"), ("ENVIROMUX-1W-MIB", "ipDeviceValue"))
if mibBuilder.loadTexts: ipDevice4Trap.setStatus('current')
if mibBuilder.loadTexts: ipDevice4Trap.setDescription('Trap issued when IP device 4 has a notification to send')
mibBuilder.exportSymbols("ENVIROMUX-1W-MIB", alertEnabled=alertEnabled, ipDeviceValue=ipDeviceValue, software=software, ipDevice4Trap=ipDevice4Trap, smAlertEnabled=smAlertEnabled, extSensor10Trap=extSensor10Trap, extSensorUnit=extSensorUnit, alertThresholdType=alertThresholdType, extSensor23Trap=extSensor23Trap, smAlertEntry=smAlertEntry, otherProduct=otherProduct, ipDevices=ipDevices, extSensor22Trap=extSensor22Trap, extSensor12Trap=extSensor12Trap, extSensor24Trap=extSensor24Trap, extSensorIndex=extSensorIndex, smAlertIndex=smAlertIndex, digInputEntry=digInputEntry, alertIndex=alertIndex, extSensor9Trap=extSensor9Trap, ipDeviceEntry=ipDeviceEntry, ipDevice1Trap=ipDevice1Trap, hardware=hardware, alertSensor=alertSensor, ipDeviceIndex=ipDeviceIndex, masterUnit=masterUnit, extSensor11Trap=extSensor11Trap, extSensor19Trap=extSensor19Trap, extSensors=extSensors, alertTable=alertTable, extSensor20Trap=extSensor20Trap, extSensor13Trap=extSensor13Trap, extSensor8Trap=extSensor8Trap, extSensor21Trap=extSensor21Trap, digitalInputsTraps=digitalInputsTraps, extSensor17Trap=extSensor17Trap, extSensor7Trap=extSensor7Trap, ipDevice2Trap=ipDevice2Trap, digInputDescription=digInputDescription, nti=nti, extSensorValue=extSensorValue, extSensorEntry=extSensorEntry, smAlerts=smAlerts, enviromux1WTraps=enviromux1WTraps, extSensor1Trap=extSensor1Trap, ipDevice3Trap=ipDevice3Trap, extSensor14Trap=extSensor14Trap, digInputs=digInputs, extSensor4Trap=extSensor4Trap, extSensor18Trap=extSensor18Trap, extSensor3Trap=extSensor3Trap, extSensor15Trap=extSensor15Trap, digInputTable=digInputTable, smAlertTable=smAlertTable, products=products, extSensorTable=extSensorTable, digInputValue=digInputValue, extSensor6Trap=extSensor6Trap, ipDeviceTable=ipDeviceTable, ipDeviceDescription=ipDeviceDescription, alertSensorValue=alertSensorValue, digInput2Trap=digInput2Trap, PYSNMP_MODULE_ID=enviromux1W, extSensorType=extSensorType, ipDevicesTraps=ipDevicesTraps, alertThreshold=alertThreshold, extSensor5Trap=extSensor5Trap, extSensor2Trap=extSensor2Trap, smAlertStatus=smAlertStatus, digInputIndex=digInputIndex, extSensor16Trap=extSensor16Trap, enviromux1W=enviromux1W, alertStatus=alertStatus, extSensorsTraps=extSensorsTraps, extSensorDescription=extSensorDescription, alertEntry=alertEntry, eAlerts=eAlerts, digInput1Trap=digInput1Trap)
