#
# PySNMP MIB module IBOOTPDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dataprobe/IBOOTPDU-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:28:16 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, IpAddress, Gauge32, Counter64, Integer32, Counter32, ObjectIdentity, NotificationType, iso, TimeTicks, Unsigned32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "Gauge32", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "iso", "TimeTicks", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
iBoot_PDU_Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1418, 6)).setLabel("iBoot-PDU-Agent")
iBoot_PDU_Agent.setRevisions(('2017-10-25 13:23',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: iBoot_PDU_Agent.setRevisionsDescriptions(('New Version',))
if mibBuilder.loadTexts: iBoot_PDU_Agent.setLastUpdated('201710251323Z')
if mibBuilder.loadTexts: iBoot_PDU_Agent.setOrganization('')
if mibBuilder.loadTexts: iBoot_PDU_Agent.setContactInfo('')
if mibBuilder.loadTexts: iBoot_PDU_Agent.setDescription('iBoot-PDU Agent\n\t\tVersion 1.1')
class TC1(TextualConvention, Integer32):
    description = ''
    status = 'current'

dataprobe = MibIdentifier((1, 3, 6, 1, 4, 1, 1418))
device = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 1))
console = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 2))
network = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 3))
snmp = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 4))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 6))
notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1418, 6, 7))
firmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
if mibBuilder.loadTexts: firmwareVersion.setDescription('')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceName.setStatus('current')
if mibBuilder.loadTexts: deviceName.setDescription('This is a 20 character string that contains the name of the iBootBar.')
deviceFamily = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceFamily.setStatus('current')
if mibBuilder.loadTexts: deviceFamily.setDescription('')
deviceModelName = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceModelName.setStatus('current')
if mibBuilder.loadTexts: deviceModelName.setDescription('')
deviceConnector = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nema", 0), ("iec", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceConnector.setStatus('current')
if mibBuilder.loadTexts: deviceConnector.setDescription('')
deviceNumberOfOutlets = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumberOfOutlets.setStatus('current')
if mibBuilder.loadTexts: deviceNumberOfOutlets.setDescription('')
deviceNumberOfLineCords = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("one", 0), ("two", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumberOfLineCords.setStatus('current')
if mibBuilder.loadTexts: deviceNumberOfLineCords.setDescription('')
deviceMaxCurrent = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceMaxCurrent.setStatus('current')
if mibBuilder.loadTexts: deviceMaxCurrent.setDescription('')
deviceTemperatureUnit = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fahrenheit", 0), ("celsius", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceTemperatureUnit.setStatus('current')
if mibBuilder.loadTexts: deviceTemperatureUnit.setDescription('fahrenheit (0)\n\t\tcelsius (1)')
deviceTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceTimeZone.setStatus('current')
if mibBuilder.loadTexts: deviceTimeZone.setDescription('')
deviceCalibrated = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCalibrated.setStatus('current')
if mibBuilder.loadTexts: deviceCalibrated.setDescription('')
modemCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemCountryCode.setStatus('current')
if mibBuilder.loadTexts: modemCountryCode.setDescription('')
outletDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletDelayTime.setStatus('current')
if mibBuilder.loadTexts: outletDelayTime.setDescription('')
cloudServiceEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cloudServiceEnabled.setStatus('current')
if mibBuilder.loadTexts: cloudServiceEnabled.setDescription('')
cloudServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cloudServerAddress.setStatus('current')
if mibBuilder.loadTexts: cloudServerAddress.setDescription('')
cloudActivationCode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cloudActivationCode.setStatus('current')
if mibBuilder.loadTexts: cloudActivationCode.setDescription('')
cloudUUID = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cloudUUID.setStatus('current')
if mibBuilder.loadTexts: cloudUUID.setDescription('')
setFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setFactoryDefaults.setStatus('current')
if mibBuilder.loadTexts: setFactoryDefaults.setDescription('true(1)\n\t\tfalse(0)')
rebootSystem = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rebootSystem.setStatus('current')
if mibBuilder.loadTexts: rebootSystem.setDescription('true(1)\n\t\tfalse(0)')
rebootRequired = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rebootRequired.setStatus('current')
if mibBuilder.loadTexts: rebootRequired.setDescription('')
serialPortEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortEnabled.setStatus('current')
if mibBuilder.loadTexts: serialPortEnabled.setDescription('')
consoleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consoleTimeout.setStatus('current')
if mibBuilder.loadTexts: consoleTimeout.setDescription('')
telnetEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetEnabled.setStatus('current')
if mibBuilder.loadTexts: telnetEnabled.setDescription('Eanlbe the telnet server.')
telnetPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetPort.setStatus('current')
if mibBuilder.loadTexts: telnetPort.setDescription('The port for the telnet server to use.')
sshEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshEnabled.setStatus('current')
if mibBuilder.loadTexts: sshEnabled.setDescription('')
sshPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshPort.setStatus('current')
if mibBuilder.loadTexts: sshPort.setDescription('')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('current')
if mibBuilder.loadTexts: macAddress.setDescription('')
ipMode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("static", 0), ("dhcp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMode.setStatus('current')
if mibBuilder.loadTexts: ipMode.setDescription('static(0)\n\t\tdhcp(1)\n\t\t')
ipAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddress.setStatus('current')
if mibBuilder.loadTexts: ipAddress.setDescription('The IP Address of the device')
subnetMask = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subnetMask.setStatus('current')
if mibBuilder.loadTexts: subnetMask.setDescription('')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gateway.setStatus('current')
if mibBuilder.loadTexts: gateway.setDescription('Address of the default gateway')
dnsServer1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServer1.setStatus('current')
if mibBuilder.loadTexts: dnsServer1.setDescription('')
dnsServer2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServer2.setStatus('current')
if mibBuilder.loadTexts: dnsServer2.setDescription('')
sslEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslEnabled.setStatus('current')
if mibBuilder.loadTexts: sslEnabled.setDescription('Enable secure sockest layer on the web server.')
sslPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslPort.setStatus('current')
if mibBuilder.loadTexts: sslPort.setDescription('')
webEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webEnabled.setStatus('current')
if mibBuilder.loadTexts: webEnabled.setDescription('Use this variable to enable/disable the web server')
webPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webPort.setStatus('current')
if mibBuilder.loadTexts: webPort.setDescription('The port number that the web server will use.  Changing this var will not take effect until \n\t\tthe unit has be reset.')
snmpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpEnabled.setStatus('current')
if mibBuilder.loadTexts: snmpEnabled.setDescription('')
snmpReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpReadCommunity.setStatus('current')
if mibBuilder.loadTexts: snmpReadCommunity.setDescription('')
snmpWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpWriteCommunity.setStatus('current')
if mibBuilder.loadTexts: snmpWriteCommunity.setDescription('')
snmpManagerTable = MibTable((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4), )
if mibBuilder.loadTexts: snmpManagerTable.setStatus('current')
if mibBuilder.loadTexts: snmpManagerTable.setDescription('')
snmpManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1), ).setIndexNames((0, "IBOOTPDU-MIB", "snmpManagerIndex"))
if mibBuilder.loadTexts: snmpManagerEntry.setStatus('current')
if mibBuilder.loadTexts: snmpManagerEntry.setDescription('')
snmpManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpManagerIndex.setStatus('current')
if mibBuilder.loadTexts: snmpManagerIndex.setDescription('The table index')
snmpManagerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpManagerAddress.setStatus('current')
if mibBuilder.loadTexts: snmpManagerAddress.setDescription('')
snmpManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpManagerName.setStatus('current')
if mibBuilder.loadTexts: snmpManagerName.setDescription('')
snmpTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapCommunity.setStatus('current')
if mibBuilder.loadTexts: snmpTrapCommunity.setDescription('')
outletTable = MibTable((1, 3, 6, 1, 4, 1, 1418, 6, 5), )
if mibBuilder.loadTexts: outletTable.setStatus('current')
if mibBuilder.loadTexts: outletTable.setDescription('')
outletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1), ).setIndexNames((0, "IBOOTPDU-MIB", "outletIndex"))
if mibBuilder.loadTexts: outletEntry.setStatus('current')
if mibBuilder.loadTexts: outletEntry.setDescription('')
outletIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletIndex.setStatus('current')
if mibBuilder.loadTexts: outletIndex.setDescription('')
outletName = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletName.setStatus('current')
if mibBuilder.loadTexts: outletName.setDescription('The name of the outlet up to 20 characters')
outletInitialState = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("last", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletInitialState.setStatus('current')
if mibBuilder.loadTexts: outletInitialState.setDescription('')
outletCycleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletCycleTime.setStatus('current')
if mibBuilder.loadTexts: outletCycleTime.setDescription('')
outletControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletControl.setStatus('current')
if mibBuilder.loadTexts: outletControl.setDescription('Use this a a write only variable.  It is used to change the outlets status')
outletStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2), ("reboot", 3), ("pend-on", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletStatus.setStatus('current')
if mibBuilder.loadTexts: outletStatus.setDescription('')
outletActualStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletActualStatus.setStatus('current')
if mibBuilder.loadTexts: outletActualStatus.setDescription('Status of the physical outlet')
voltageLC1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageLC1.setStatus('current')
if mibBuilder.loadTexts: voltageLC1.setDescription('')
currentLC1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentLC1.setStatus('current')
if mibBuilder.loadTexts: currentLC1.setDescription('')
voltageLC2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageLC2.setStatus('current')
if mibBuilder.loadTexts: voltageLC2.setDescription('')
currentLC2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentLC2.setStatus('current')
if mibBuilder.loadTexts: currentLC2.setDescription('')
temperature1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature1.setStatus('current')
if mibBuilder.loadTexts: temperature1.setDescription('')
temperature2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature2.setStatus('current')
if mibBuilder.loadTexts: temperature2.setDescription('')
outletChange = NotificationType((1, 3, 6, 1, 4, 1, 1418, 6, 7, 1)).setObjects(("IBOOTPDU-MIB", "outletIndex"), ("IBOOTPDU-MIB", "outletName"), ("IBOOTPDU-MIB", "outletStatus"))
if mibBuilder.loadTexts: outletChange.setStatus('current')
if mibBuilder.loadTexts: outletChange.setDescription('This trap is sent when ever an outlet changes state.  It contains the name of the outlet.')
mibBuilder.exportSymbols("IBOOTPDU-MIB", deviceNumberOfOutlets=deviceNumberOfOutlets, sensors=sensors, consoleTimeout=consoleTimeout, network=network, outletChange=outletChange, outletActualStatus=outletActualStatus, voltageLC1=voltageLC1, iBoot_PDU_Agent=iBoot_PDU_Agent, snmpReadCommunity=snmpReadCommunity, notifications=notifications, setFactoryDefaults=setFactoryDefaults, outletTable=outletTable, voltageLC2=voltageLC2, snmpEnabled=snmpEnabled, cloudServiceEnabled=cloudServiceEnabled, console=console, PYSNMP_MODULE_ID=iBoot_PDU_Agent, telnetPort=telnetPort, sshPort=sshPort, snmpTrapCommunity=snmpTrapCommunity, outletInitialState=outletInitialState, currentLC2=currentLC2, snmpManagerName=snmpManagerName, telnetEnabled=telnetEnabled, dnsServer2=dnsServer2, outletName=outletName, outletIndex=outletIndex, sslPort=sslPort, cloudServerAddress=cloudServerAddress, serialPortEnabled=serialPortEnabled, deviceName=deviceName, ipMode=ipMode, TC1=TC1, dnsServer1=dnsServer1, cloudActivationCode=cloudActivationCode, snmpManagerTable=snmpManagerTable, outletEntry=outletEntry, gateway=gateway, deviceCalibrated=deviceCalibrated, dataprobe=dataprobe, modemCountryCode=modemCountryCode, subnetMask=subnetMask, outletStatus=outletStatus, currentLC1=currentLC1, snmpManagerAddress=snmpManagerAddress, snmpManagerEntry=snmpManagerEntry, sslEnabled=sslEnabled, deviceConnector=deviceConnector, webEnabled=webEnabled, deviceFamily=deviceFamily, outletControl=outletControl, snmpWriteCommunity=snmpWriteCommunity, temperature2=temperature2, webPort=webPort, deviceTimeZone=deviceTimeZone, sshEnabled=sshEnabled, deviceMaxCurrent=deviceMaxCurrent, macAddress=macAddress, ipAddress=ipAddress, firmwareVersion=firmwareVersion, outletCycleTime=outletCycleTime, deviceModelName=deviceModelName, rebootSystem=rebootSystem, cloudUUID=cloudUUID, device=device, snmp=snmp, deviceTemperatureUnit=deviceTemperatureUnit, snmpManagerIndex=snmpManagerIndex, deviceNumberOfLineCords=deviceNumberOfLineCords, outletDelayTime=outletDelayTime, rebootRequired=rebootRequired, temperature1=temperature1)
