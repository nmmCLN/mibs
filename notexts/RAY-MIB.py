#
# PySNMP MIB module RAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ray/RAY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:02 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Counter64, ModuleIdentity, TimeTicks, mib_2, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, Gauge32, NotificationType, MibIdentifier, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "TimeTicks", "mib-2", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "Gauge32", "NotificationType", "MibIdentifier", "IpAddress", "enterprises")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
ray = ModuleIdentity((1, 3, 6, 1, 4, 1, 33555, 1))
ray.setRevisions(('2016-10-04 00:00',))
if mibBuilder.loadTexts: ray.setLastUpdated('201610040000Z')
if mibBuilder.loadTexts: ray.setOrganization('Racom s.r.o')
class DisplayString(OctetString):
    pass

class PhysAddress(OctetString):
    pass

class ServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class AlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2), ("ack", 3))

class OptionSetting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("on", 1), ("off", 2))

class ModulationList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("na", 0), ("qpsk", 1), ("qam16", 2), ("qam32", 3), ("qam64", 4), ("qam128", 5), ("qam256", 6))

racom = MibIdentifier((1, 3, 6, 1, 4, 1, 33555))
station = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1))
interface = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 2))
statistic = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 3))
rayTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 10))
ray2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 11))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 1))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 2))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 4))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 5))
access = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6))
authorization = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 7))
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8))
productName = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
unitType = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitType.setStatus('current')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('current')
swVer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVer.setStatus('current')
swVerRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVerRadio.setStatus('current')
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("ok", 1), ("warning", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
lineStatus = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("na", 0), ("ok", 1), ("analyzer", 2), ("connecting", 3), ("searching", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineStatus.setStatus('current')
peerNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: peerNumber.setStatus('current')
rfPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerStatus.setStatus('current')
searchModeDisabled = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 5), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: searchModeDisabled.setStatus('current')
ethPeer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 6), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethPeer.setStatus('current')
securePeerMode = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 7), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securePeerMode.setStatus('current')
lineStatusII = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("na", 0), ("setup", 1), ("single", 2), ("connecting", 3), ("authorizing", 4), ("ok", 5), ("analyzer", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineStatusII.setStatus('current')
eth1Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 9), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth1Link.setStatus('current')
eth2Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 3, 10), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2Link.setStatus('current')
temperatureModem = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureModem.setStatus('current')
temperatureRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureRadio.setStatus('current')
voltageUnit = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageUnit.setStatus('current')
voltageSource = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("aux", 1), ("poe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSource.setStatus('current')
useCpu = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: useCpu.setStatus('current')
useMemory = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: useMemory.setStatus('current')
useLogStorage = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: useLogStorage.setStatus('current')
sshd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("onlykey", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshd.setStatus('current')
telnetd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telnetd.setStatus('current')
httpd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 3), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: httpd.setStatus('current')
ip = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ip.setStatus('current')
mac = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mac.setStatus('current')
managementVlan = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 6), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlan.setStatus('current')
managementVlanId = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlanId.setStatus('current')
wifiHAP = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 6, 8), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wifiHAP.setStatus('current')
keyTable = MibTable((1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1), )
if mibBuilder.loadTexts: keyTable.setStatus('current')
keyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1, 1), ).setIndexNames((0, "RAY-MIB", "keyName"))
if mibBuilder.loadTexts: keyEntry.setStatus('current')
keyName = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 1, 7, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: keyName.setStatus('current')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 1), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('current')
alarmVoltageLow = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 2), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageLow.setStatus('current')
alarmVoltageHigh = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 3), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageHigh.setStatus('current')
alarmRss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 4), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmRss.setStatus('current')
alarmSnr = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 5), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSnr.setStatus('current')
alarmBer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 6), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmBer.setStatus('current')
alarmPeerDisconnected = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 7), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPeerDisconnected.setStatus('current')
alarmEth1Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 8), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth1Down.setStatus('current')
alarmEth2Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 9), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth2Down.setStatus('current')
alarmRfPowerFail = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 10), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmRfPowerFail.setStatus('current')
alarmNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 11), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNetBitrate.setStatus('current')
alarmWifiOn = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 1, 8, 12), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmWifiOn.setStatus('current')
ifRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1))
ifEth = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2))
rxChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxChannel.setStatus('current')
txChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: txChannel.setStatus('current')
rxFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFreq.setStatus('current')
txFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txFreq.setStatus('current')
rxModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulation.setStatus('current')
txModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulation.setStatus('current')
rxModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 7), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulationIndex.setStatus('current')
txModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 8), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulationIndex.setStatus('current')
bandwidth = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("bw-28MHz", 1), ("bw-14MHz", 2), ("bw-7MHz", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bandwidth.setStatus('current')
coding = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("low", 1), ("hi", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coding.setStatus('current')
matching = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 11), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matching.setStatus('current')
rfPowerConfigured = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerConfigured.setStatus('current')
netBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netBitrate.setStatus('current')
maxNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNetBitrate.setStatus('current')
bandwidthKHz = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bandwidthKHz.setStatus('current')
channelArrangement = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("accp", 1), ("acap", 2), ("ccdp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelArrangement.setStatus('current')
rfPowerCurrent = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerCurrent.setStatus('current')
ifEthTable = MibTable((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1), )
if mibBuilder.loadTexts: ifEthTable.setStatus('current')
ifEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1), ).setIndexNames((0, "RAY-MIB", "speed"))
if mibBuilder.loadTexts: ifEthEntry.setStatus('current')
speed = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: speed.setStatus('current')
duplex = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("full", 1), ("half", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duplex.setStatus('current')
mdix = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("mdi", 1), ("mdi-x", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdix.setStatus('current')
autonego = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 4), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autonego.setStatus('current')
pause = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 5), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pause.setStatus('current')
asymPause = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 1, 1, 6), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asymPause.setStatus('current')
prioritized = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prioritized.setStatus('current')
vlanId = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanId.setStatus('current')
serviceVlanId = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceVlanId.setStatus('current')
modemR = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1))
radio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 1, 3, 3))
rxPauseFrames = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxPauseFrames.setStatus('current')
rxControlFrames = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxControlFrames.setStatus('current')
rxBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxBroadcast.setStatus('current')
rxMulticast = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxMulticast.setStatus('current')
rxDones = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDones.setStatus('current')
rxOutOfRangeErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxOutOfRangeErrors.setStatus('current')
rxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxCrcErrors.setStatus('current')
rxCodeErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxCodeErrors.setStatus('current')
rxFalseCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFalseCarrierErrors.setStatus('current')
rxDroppedPkts = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxDroppedPkts.setStatus('current')
rxHCBytes = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxHCBytes.setStatus('current')
txPauseFrames = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPauseFrames.setStatus('current')
txControlFrames = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txControlFrames.setStatus('current')
txBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txBroadcast.setStatus('current')
txMulticast = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txMulticast.setStatus('current')
txDones = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txDones.setStatus('current')
txLengthCheckErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txLengthCheckErrors.setStatus('current')
txCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txCrcErrors.setStatus('current')
txCollisions = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txCollisions.setStatus('current')
txHCBytes = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txHCBytes.setStatus('current')
rss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rss.setStatus('current')
snr = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snr.setStatus('current')
fecBlockCounter = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fecBlockCounter.setStatus('current')
fecUncorrectBlockCounter = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fecUncorrectBlockCounter.setStatus('current')
timeAllConnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllConnect.setStatus('current')
timeAllDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllDisconnect.setStatus('current')
timeMaxDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeMaxDisconnect.setStatus('current')
numDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numDisconnect.setStatus('current')
reliability = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reliability.setStatus('current')
linkUptime = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkUptime.setStatus('current')
ber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ber.setStatus('current')
ethInThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethInThroughput.setStatus('current')
ethOutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethOutThroughput.setStatus('current')
eth2InThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2InThroughput.setStatus('current')
eth2OutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 1, 3, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2OutThroughput.setStatus('current')
airDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 1)).setObjects(("RAY-MIB", "lineStatus"))
if mibBuilder.loadTexts: airDisconnect.setStatus('current')
airConnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 2)).setObjects(("RAY-MIB", "lineStatus"))
if mibBuilder.loadTexts: airConnect.setStatus('current')
airWdog = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 3)).setObjects(("RAY-MIB", "lineStatus"))
if mibBuilder.loadTexts: airWdog.setStatus('current')
tempAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 4)).setObjects(("RAY-MIB", "temperatureModem"))
if mibBuilder.loadTexts: tempAlarm.setStatus('current')
powerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 5)).setObjects(("RAY-MIB", "voltageUnit"))
if mibBuilder.loadTexts: powerAlarm.setStatus('current')
memoryAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 6)).setObjects(("RAY-MIB", "useMemory"))
if mibBuilder.loadTexts: memoryAlarm.setStatus('current')
rssAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 7)).setObjects(("RAY-MIB", "rss"))
if mibBuilder.loadTexts: rssAlarm.setStatus('current')
snrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 8)).setObjects(("RAY-MIB", "snr"))
if mibBuilder.loadTexts: snrAlarm.setStatus('current')
berAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 9)).setObjects(("RAY-MIB", "fecUncorrectBlockCounter"), ("RAY-MIB", "fecBlockCounter"))
if mibBuilder.loadTexts: berAlarm.setStatus('current')
rfPowerFail = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 10)).setObjects(("RAY-MIB", "rfPowerStatus"))
if mibBuilder.loadTexts: rfPowerFail.setStatus('current')
peerEthLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 10, 11)).setObjects(("RAY-MIB", "ethPeer"))
if mibBuilder.loadTexts: peerEthLinkDown.setStatus('current')
tr2TemperatureAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 1)).setObjects(("RAY-MIB", "temperatureModem"), ("RAY-MIB", "alarmTemperature"))
if mibBuilder.loadTexts: tr2TemperatureAlarm.setStatus('current')
tr2VoltageLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 2)).setObjects(("RAY-MIB", "voltageUnit"), ("RAY-MIB", "alarmVoltageLow"))
if mibBuilder.loadTexts: tr2VoltageLowAlarm.setStatus('current')
tr2VoltageHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 3)).setObjects(("RAY-MIB", "voltageUnit"), ("RAY-MIB", "alarmVoltageHigh"))
if mibBuilder.loadTexts: tr2VoltageHighAlarm.setStatus('current')
tr2RssAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 4)).setObjects(("RAY-MIB", "rss"), ("RAY-MIB", "alarmRss"))
if mibBuilder.loadTexts: tr2RssAlarm.setStatus('current')
tr2SnrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 5)).setObjects(("RAY-MIB", "snr"), ("RAY-MIB", "alarmSnr"))
if mibBuilder.loadTexts: tr2SnrAlarm.setStatus('current')
tr2BerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 6)).setObjects(("RAY-MIB", "ber"), ("RAY-MIB", "alarmBer"))
if mibBuilder.loadTexts: tr2BerAlarm.setStatus('current')
tr2AirDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 7)).setObjects(("RAY-MIB", "lineStatusII"), ("RAY-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr2AirDisconnect.setStatus('current')
tr2AirConnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 8)).setObjects(("RAY-MIB", "lineStatusII"), ("RAY-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr2AirConnect.setStatus('current')
tr2Eth1LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 9)).setObjects(("RAY-MIB", "eth1Link"), ("RAY-MIB", "alarmEth1Down"))
if mibBuilder.loadTexts: tr2Eth1LinkDown.setStatus('current')
tr2Eth21LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 10)).setObjects(("RAY-MIB", "eth2Link"), ("RAY-MIB", "alarmEth2Down"))
if mibBuilder.loadTexts: tr2Eth21LinkDown.setStatus('current')
tr2RfPowerFail = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 11)).setObjects(("RAY-MIB", "rfPowerStatus"), ("RAY-MIB", "alarmRfPowerFail"))
if mibBuilder.loadTexts: tr2RfPowerFail.setStatus('current')
tr2NetBitrate = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 12)).setObjects(("RAY-MIB", "netBitrate"), ("RAY-MIB", "alarmNetBitrate"))
if mibBuilder.loadTexts: tr2NetBitrate.setStatus('current')
tr2WifiOn = NotificationType((1, 3, 6, 1, 4, 1, 33555, 1, 11, 13)).setObjects(("RAY-MIB", "wifiHAP"), ("RAY-MIB", "alarmWifiOn"))
if mibBuilder.loadTexts: tr2WifiOn.setStatus('current')
mibBuilder.exportSymbols("RAY-MIB", httpd=httpd, radio=radio, ray=ray, tr2RssAlarm=tr2RssAlarm, ethOutThroughput=ethOutThroughput, berAlarm=berAlarm, alarmEth1Down=alarmEth1Down, unitType=unitType, tr2BerAlarm=tr2BerAlarm, timeMaxDisconnect=timeMaxDisconnect, lineStatusII=lineStatusII, ifEthTable=ifEthTable, interface=interface, useCpu=useCpu, coding=coding, autonego=autonego, asymPause=asymPause, txBroadcast=txBroadcast, mdix=mdix, txFreq=txFreq, txControlFrames=txControlFrames, rxMulticast=rxMulticast, powerAlarm=powerAlarm, eth1Link=eth1Link, PYSNMP_MODULE_ID=ray, ethPeer=ethPeer, rssAlarm=rssAlarm, peerEthLinkDown=peerEthLinkDown, ifEthEntry=ifEthEntry, txMulticast=txMulticast, txHCBytes=txHCBytes, swVer=swVer, keyEntry=keyEntry, rxCodeErrors=rxCodeErrors, txCrcErrors=txCrcErrors, status=status, tr2AirConnect=tr2AirConnect, sshd=sshd, alarmSnr=alarmSnr, matching=matching, tr2SnrAlarm=tr2SnrAlarm, product=product, fecUncorrectBlockCounter=fecUncorrectBlockCounter, voltageUnit=voltageUnit, chassis=chassis, tempAlarm=tempAlarm, tr2VoltageHighAlarm=tr2VoltageHighAlarm, alarmRss=alarmRss, alarmTemperature=alarmTemperature, ethernet=ethernet, txLengthCheckErrors=txLengthCheckErrors, alarmWifiOn=alarmWifiOn, alarmBer=alarmBer, ModulationList=ModulationList, netBitrate=netBitrate, serviceVlanId=serviceVlanId, ber=ber, rxChannel=rxChannel, alarmPeerDisconnected=alarmPeerDisconnected, airWdog=airWdog, mac=mac, airDisconnect=airDisconnect, ifEth=ifEth, telnetd=telnetd, reliability=reliability, rfPowerStatus=rfPowerStatus, useLogStorage=useLogStorage, eth2OutThroughput=eth2OutThroughput, eth2InThroughput=eth2InThroughput, voltageSource=voltageSource, rfPowerConfigured=rfPowerConfigured, alarmEth2Down=alarmEth2Down, serialNumber=serialNumber, DisplayString=DisplayString, rxDroppedPkts=rxDroppedPkts, keyTable=keyTable, timeAllDisconnect=timeAllDisconnect, fecBlockCounter=fecBlockCounter, ifRadio=ifRadio, keyName=keyName, securePeerMode=securePeerMode, rxModulation=rxModulation, airConnect=airConnect, snrAlarm=snrAlarm, temperatureModem=temperatureModem, rxModulationIndex=rxModulationIndex, systemStatus=systemStatus, txPauseFrames=txPauseFrames, alarmNetBitrate=alarmNetBitrate, linkUptime=linkUptime, ethInThroughput=ethInThroughput, tr2Eth1LinkDown=tr2Eth1LinkDown, bandwidth=bandwidth, txChannel=txChannel, duplex=duplex, productName=productName, txModulationIndex=txModulationIndex, tr2WifiOn=tr2WifiOn, pause=pause, timeAllConnect=timeAllConnect, ray2Traps=ray2Traps, temperatureRadio=temperatureRadio, maxNetBitrate=maxNetBitrate, info=info, system=system, ip=ip, alarm=alarm, managementVlan=managementVlan, txCollisions=txCollisions, alarmVoltageLow=alarmVoltageLow, alarmRfPowerFail=alarmRfPowerFail, memoryAlarm=memoryAlarm, AlarmState=AlarmState, alarmVoltageHigh=alarmVoltageHigh, rfPowerCurrent=rfPowerCurrent, rxPauseFrames=rxPauseFrames, PhysAddress=PhysAddress, ServiceState=ServiceState, tr2Eth21LinkDown=tr2Eth21LinkDown, rss=rss, bandwidthKHz=bandwidthKHz, rayTraps=rayTraps, station=station, rxHCBytes=rxHCBytes, channelArrangement=channelArrangement, rxCrcErrors=rxCrcErrors, prioritized=prioritized, snr=snr, peerNumber=peerNumber, racom=racom, rxBroadcast=rxBroadcast, txModulation=txModulation, numDisconnect=numDisconnect, rfPowerFail=rfPowerFail, vlanId=vlanId, authorization=authorization, deviceName=deviceName, tr2TemperatureAlarm=tr2TemperatureAlarm, tr2RfPowerFail=tr2RfPowerFail, modemR=modemR, statistic=statistic, managementVlanId=managementVlanId, tr2VoltageLowAlarm=tr2VoltageLowAlarm, rxOutOfRangeErrors=rxOutOfRangeErrors, tr2AirDisconnect=tr2AirDisconnect, OptionSetting=OptionSetting, useMemory=useMemory, tr2NetBitrate=tr2NetBitrate, lineStatus=lineStatus, rxControlFrames=rxControlFrames, txDones=txDones, swVerRadio=swVerRadio, rxFalseCarrierErrors=rxFalseCarrierErrors, access=access, eth2Link=eth2Link, speed=speed, wifiHAP=wifiHAP, searchModeDisabled=searchModeDisabled, rxFreq=rxFreq, rxDones=rxDones)
