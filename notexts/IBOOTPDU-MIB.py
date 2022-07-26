#
# PySNMP MIB module IBOOTPDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dataprobe/IBOOTPDU-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:26:13 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, IpAddress, Integer32, Counter64, ObjectIdentity, enterprises, ModuleIdentity, NotificationType, Counter32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "IpAddress", "Integer32", "Counter64", "ObjectIdentity", "enterprises", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
iBoot_PDU_Agent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1418, 6)).setLabel("iBoot-PDU-Agent")
iBoot_PDU_Agent.setRevisions(('2017-10-25 13:23',))
if mibBuilder.loadTexts: iBoot_PDU_Agent.setLastUpdated('201710251323Z')
if mibBuilder.loadTexts: iBoot_PDU_Agent.setOrganization('')
class TC1(TextualConvention, Integer32):
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
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceName.setStatus('current')
deviceFamily = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceFamily.setStatus('current')
deviceModelName = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceModelName.setStatus('current')
deviceConnector = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nema", 0), ("iec", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceConnector.setStatus('current')
deviceNumberOfOutlets = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumberOfOutlets.setStatus('current')
deviceNumberOfLineCords = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("one", 0), ("two", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumberOfLineCords.setStatus('current')
deviceMaxCurrent = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceMaxCurrent.setStatus('current')
deviceTemperatureUnit = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fahrenheit", 0), ("celsius", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: deviceTemperatureUnit.setStatus('current')
deviceTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceTimeZone.setStatus('current')
deviceCalibrated = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceCalibrated.setStatus('current')
modemCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modemCountryCode.setStatus('current')
outletDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletDelayTime.setStatus('current')
cloudServiceEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cloudServiceEnabled.setStatus('current')
cloudServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cloudServerAddress.setStatus('current')
cloudActivationCode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cloudActivationCode.setStatus('current')
cloudUUID = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cloudUUID.setStatus('current')
setFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setFactoryDefaults.setStatus('current')
rebootSystem = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rebootSystem.setStatus('current')
rebootRequired = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rebootRequired.setStatus('current')
serialPortEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortEnabled.setStatus('current')
consoleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: consoleTimeout.setStatus('current')
telnetEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetEnabled.setStatus('current')
telnetPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetPort.setStatus('current')
sshEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshEnabled.setStatus('current')
sshPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshPort.setStatus('current')
macAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('current')
ipMode = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("static", 0), ("dhcp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipMode.setStatus('current')
ipAddress = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipAddress.setStatus('current')
subnetMask = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subnetMask.setStatus('current')
gateway = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gateway.setStatus('current')
dnsServer1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServer1.setStatus('current')
dnsServer2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsServer2.setStatus('current')
sslEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslEnabled.setStatus('current')
sslPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sslPort.setStatus('current')
webEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webEnabled.setStatus('current')
webPort = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webPort.setStatus('current')
snmpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpEnabled.setStatus('current')
snmpReadCommunity = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpReadCommunity.setStatus('current')
snmpWriteCommunity = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 4, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpWriteCommunity.setStatus('current')
snmpManagerTable = MibTable((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4), )
if mibBuilder.loadTexts: snmpManagerTable.setStatus('current')
snmpManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1), ).setIndexNames((0, "IBOOTPDU-MIB", "snmpManagerIndex"))
if mibBuilder.loadTexts: snmpManagerEntry.setStatus('current')
snmpManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpManagerIndex.setStatus('current')
snmpManagerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpManagerAddress.setStatus('current')
snmpManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpManagerName.setStatus('current')
snmpTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 4, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapCommunity.setStatus('current')
outletTable = MibTable((1, 3, 6, 1, 4, 1, 1418, 6, 5), )
if mibBuilder.loadTexts: outletTable.setStatus('current')
outletEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1), ).setIndexNames((0, "IBOOTPDU-MIB", "outletIndex"))
if mibBuilder.loadTexts: outletEntry.setStatus('current')
outletIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletIndex.setStatus('current')
outletName = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletName.setStatus('current')
outletInitialState = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("last", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletInitialState.setStatus('current')
outletCycleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletCycleTime.setStatus('current')
outletControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outletControl.setStatus('current')
outletStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cycle", 2), ("reboot", 3), ("pend-on", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletStatus.setStatus('current')
outletActualStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1418, 6, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: outletActualStatus.setStatus('current')
voltageLC1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageLC1.setStatus('current')
currentLC1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentLC1.setStatus('current')
voltageLC2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageLC2.setStatus('current')
currentLC2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentLC2.setStatus('current')
temperature1 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature1.setStatus('current')
temperature2 = MibScalar((1, 3, 6, 1, 4, 1, 1418, 6, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature2.setStatus('current')
outletChange = NotificationType((1, 3, 6, 1, 4, 1, 1418, 6, 7, 1)).setObjects(("IBOOTPDU-MIB", "outletIndex"), ("IBOOTPDU-MIB", "outletName"), ("IBOOTPDU-MIB", "outletStatus"))
if mibBuilder.loadTexts: outletChange.setStatus('current')
mibBuilder.exportSymbols("IBOOTPDU-MIB", snmpManagerIndex=snmpManagerIndex, ipMode=ipMode, network=network, snmpManagerEntry=snmpManagerEntry, voltageLC2=voltageLC2, sslPort=sslPort, PYSNMP_MODULE_ID=iBoot_PDU_Agent, outletCycleTime=outletCycleTime, temperature1=temperature1, macAddress=macAddress, currentLC1=currentLC1, firmwareVersion=firmwareVersion, modemCountryCode=modemCountryCode, setFactoryDefaults=setFactoryDefaults, dataprobe=dataprobe, outletActualStatus=outletActualStatus, cloudUUID=cloudUUID, telnetEnabled=telnetEnabled, outletInitialState=outletInitialState, outletDelayTime=outletDelayTime, sslEnabled=sslEnabled, device=device, rebootRequired=rebootRequired, webEnabled=webEnabled, outletTable=outletTable, telnetPort=telnetPort, deviceNumberOfLineCords=deviceNumberOfLineCords, cloudServerAddress=cloudServerAddress, deviceFamily=deviceFamily, serialPortEnabled=serialPortEnabled, sshEnabled=sshEnabled, dnsServer1=dnsServer1, deviceModelName=deviceModelName, deviceCalibrated=deviceCalibrated, rebootSystem=rebootSystem, outletChange=outletChange, snmpWriteCommunity=snmpWriteCommunity, TC1=TC1, sshPort=sshPort, sensors=sensors, snmpTrapCommunity=snmpTrapCommunity, deviceTimeZone=deviceTimeZone, currentLC2=currentLC2, deviceMaxCurrent=deviceMaxCurrent, deviceTemperatureUnit=deviceTemperatureUnit, snmpManagerName=snmpManagerName, outletControl=outletControl, snmpReadCommunity=snmpReadCommunity, consoleTimeout=consoleTimeout, subnetMask=subnetMask, console=console, deviceConnector=deviceConnector, snmp=snmp, cloudActivationCode=cloudActivationCode, snmpManagerTable=snmpManagerTable, outletName=outletName, deviceName=deviceName, deviceNumberOfOutlets=deviceNumberOfOutlets, snmpEnabled=snmpEnabled, voltageLC1=voltageLC1, webPort=webPort, outletEntry=outletEntry, snmpManagerAddress=snmpManagerAddress, notifications=notifications, ipAddress=ipAddress, outletStatus=outletStatus, outletIndex=outletIndex, gateway=gateway, temperature2=temperature2, dnsServer2=dnsServer2, iBoot_PDU_Agent=iBoot_PDU_Agent, cloudServiceEnabled=cloudServiceEnabled)
