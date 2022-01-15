#
# PySNMP MIB module XAVI-XG6846-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/inteno/XAVI-XG6846-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:25:21 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, snmpModules, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, enterprises, Integer32, Gauge32, IpAddress, MibIdentifier, NotificationType, mib_2, ObjectIdentity, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "snmpModules", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "enterprises", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "mib-2", "ObjectIdentity", "Unsigned32", "Counter32", "Counter64")
TimeStamp, TextualConvention, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TestAndIncr", "DisplayString")
xg6846 = MibIdentifier((1, 3, 6, 1, 4, 1, 12919))
catv = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 1))
portmode = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 2))
qos = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 3))
vlan = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 4))
portStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 5))
ddminfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 6))
internetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 7))
reboot = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 8))
tftp = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 9))
portPower = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 10))
jumb = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 11))
deviceinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12919, 12))
catvEnable = MibScalar((1, 3, 6, 1, 4, 1, 12919, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: catvEnable.setStatus('current')
if mibBuilder.loadTexts: catvEnable.setDescription('catv switch function.')
lanportTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportTable.setStatus('current')
if mibBuilder.loadTexts: lanportTable.setDescription('LAN port table.')
modeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "lanportIndex"))
if mibBuilder.loadTexts: modeEntry.setStatus('current')
if mibBuilder.loadTexts: modeEntry.setDescription('set port mode entry.')
lanportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanportIndex.setStatus('current')
if mibBuilder.loadTexts: lanportIndex.setDescription('lan port entry index.')
lanportName = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanportName.setStatus('current')
if mibBuilder.loadTexts: lanportName.setDescription('lan port name.')
lanportspeed = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 0), ("speed10mFD", 1), ("speed10mHD", 2), ("speed100mFD", 3), ("speed100mHD", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportspeed.setStatus('current')
if mibBuilder.loadTexts: lanportspeed.setDescription('port speed value.')
lanportpause = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanportpause.setStatus('current')
if mibBuilder.loadTexts: lanportpause.setDescription('port 802.1P enable/disable value.')
qosTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 3, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosTable.setStatus('current')
if mibBuilder.loadTexts: qosTable.setDescription('qos table.')
qosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "qosIndex"))
if mibBuilder.loadTexts: qosEntry.setStatus('current')
if mibBuilder.loadTexts: qosEntry.setDescription('qos list entry.')
qosIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosIndex.setStatus('current')
if mibBuilder.loadTexts: qosIndex.setDescription('qos list entry index.')
qmapping = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qmapping.setStatus('current')
if mibBuilder.loadTexts: qmapping.setDescription('mapping queue value.')
portTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 4, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTable.setStatus('current')
if mibBuilder.loadTexts: portTable.setDescription('all port setting table.')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('current')
if mibBuilder.loadTexts: portEntry.setDescription('port list entry.')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('current')
if mibBuilder.loadTexts: portIndex.setDescription('port num index.')
vlanid = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanid.setStatus('current')
if mibBuilder.loadTexts: vlanid.setDescription('port vlan id value.')
priority = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: priority.setStatus('current')
if mibBuilder.loadTexts: priority.setDescription('port default priority value.')
qmode = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("fallback", 1), ("check", 2), ("secure", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qmode.setStatus('current')
if mibBuilder.loadTexts: qmode.setDescription('port 802.1Q mode value.')
dscpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dscpEnable.setStatus('current')
if mibBuilder.loadTexts: dscpEnable.setDescription('DSCP enable.')
vlangroupTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 4, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlangroupTable.setStatus('current')
if mibBuilder.loadTexts: vlangroupTable.setDescription('VLAN group setting table.')
groupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "groupIndex"))
if mibBuilder.loadTexts: groupEntry.setStatus('current')
if mibBuilder.loadTexts: groupEntry.setDescription('vlan group list entry.')
groupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupIndex.setStatus('current')
if mibBuilder.loadTexts: groupIndex.setDescription('vlan group index.')
groupid = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: groupid.setStatus('current')
if mibBuilder.loadTexts: groupid.setDescription('vlan group id.')
lan1 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan1.setStatus('current')
if mibBuilder.loadTexts: lan1.setDescription('vlan group id.')
lan2 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan2.setStatus('current')
if mibBuilder.loadTexts: lan2.setDescription('vlan group id.')
lan3 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan3.setStatus('current')
if mibBuilder.loadTexts: lan3.setDescription('vlan group id.')
lan4 = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lan4.setStatus('current')
if mibBuilder.loadTexts: lan4.setDescription('vlan group id.')
wan = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notMember", 0), ("egressUntagged", 1), ("egressTagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wan.setStatus('current')
if mibBuilder.loadTexts: wan.setDescription('vlan group id.')
statisticTable = MibTable((1, 3, 6, 1, 4, 1, 12919, 5, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: statisticTable.setStatus('current')
if mibBuilder.loadTexts: statisticTable.setDescription('port statistics table.')
portStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1), ).setMaxAccess("readwrite").setIndexNames((0, "XAVI-XG6846-MIB", "statIndex"))
if mibBuilder.loadTexts: portStatEntry.setStatus('current')
if mibBuilder.loadTexts: portStatEntry.setDescription('port statistics list entry.')
statIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statIndex.setStatus('current')
if mibBuilder.loadTexts: statIndex.setDescription('ports entry index.')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('current')
if mibBuilder.loadTexts: portName.setDescription('port name.')
unicastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unicastsReceived.setStatus('current')
if mibBuilder.loadTexts: unicastsReceived.setDescription('unicasts Received.')
broadcastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadcastsReceived.setStatus('current')
if mibBuilder.loadTexts: broadcastsReceived.setDescription('broadcasts Received.')
multicastsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastsReceived.setStatus('current')
if mibBuilder.loadTexts: multicastsReceived.setDescription('multicasts Received.')
fcsErrorReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsErrorReceived.setStatus('current')
if mibBuilder.loadTexts: fcsErrorReceived.setDescription('fcsError Received.')
pauseReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pauseReceived.setStatus('current')
if mibBuilder.loadTexts: pauseReceived.setDescription('pause Received.')
unicastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unicastsTransmitted.setStatus('current')
if mibBuilder.loadTexts: unicastsTransmitted.setDescription('unicasts Transmitted.')
broadcastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: broadcastsTransmitted.setStatus('current')
if mibBuilder.loadTexts: broadcastsTransmitted.setDescription('broadcasts Transmitted.')
multicastsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: multicastsTransmitted.setStatus('current')
if mibBuilder.loadTexts: multicastsTransmitted.setDescription('multicasts Transmitted.')
fcsErrorTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcsErrorTransmitted.setStatus('current')
if mibBuilder.loadTexts: fcsErrorTransmitted.setDescription('fcsError Transmitted.')
pauseTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pauseTransmitted.setStatus('current')
if mibBuilder.loadTexts: pauseTransmitted.setDescription('pause Transmitted.')
speed = MibTableColumn((1, 3, 6, 1, 4, 1, 12919, 5, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: speed.setStatus('current')
if mibBuilder.loadTexts: speed.setDescription('port speed duplex mode status.')
vendorName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
if mibBuilder.loadTexts: vendorName.setDescription('DDM Vendor Name.')
vendorOui = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorOui.setStatus('current')
if mibBuilder.loadTexts: vendorOui.setDescription('DDM Vendor OUI.')
vendorPn = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorPn.setStatus('current')
if mibBuilder.loadTexts: vendorPn.setDescription('DDM Vendor PN.')
vendorRev = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorRev.setStatus('current')
if mibBuilder.loadTexts: vendorRev.setDescription('DDM Vendor REV.')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('DDM Temperature.')
voltage = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage.setStatus('current')
if mibBuilder.loadTexts: voltage.setDescription('DDM Voltage.')
bias = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bias.setStatus('current')
if mibBuilder.loadTexts: bias.setDescription('DDM Bias.')
txPower = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
if mibBuilder.loadTexts: txPower.setDescription('DDM TX Power.')
rxPower = MibScalar((1, 3, 6, 1, 4, 1, 12919, 6, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxPower.setStatus('current')
if mibBuilder.loadTexts: rxPower.setDescription('DDM Rx Power.')
wanType = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dhcp", 1), ("staticIp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanType.setStatus('current')
if mibBuilder.loadTexts: wanType.setDescription('wan protocol type.')
hostname = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostname.setStatus('current')
if mibBuilder.loadTexts: hostname.setDescription('the dns host name.')
domainame = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: domainame.setStatus('current')
if mibBuilder.loadTexts: domainame.setDescription('the dns domain name.')
staticDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticDns.setStatus('current')
if mibBuilder.loadTexts: staticDns.setDescription('static dns enable.')
primaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: primaryDns.setStatus('current')
if mibBuilder.loadTexts: primaryDns.setDescription('the primary dns.')
secondaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secondaryDns.setStatus('current')
if mibBuilder.loadTexts: secondaryDns.setDescription('the secodary dns.')
staticIpHostName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpHostName.setStatus('current')
if mibBuilder.loadTexts: staticIpHostName.setDescription('the static Ip dns host name.')
staticIpDomainName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpDomainName.setStatus('current')
if mibBuilder.loadTexts: staticIpDomainName.setDescription('the static ip dns domain name.')
staticIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpAddr.setStatus('current')
if mibBuilder.loadTexts: staticIpAddr.setDescription('The static ip address .')
staticIpSubMask = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpSubMask.setStatus('current')
if mibBuilder.loadTexts: staticIpSubMask.setDescription('The static subnet mask .')
staticIpGateway = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpGateway.setStatus('current')
if mibBuilder.loadTexts: staticIpGateway.setDescription('The static gateway .')
staticIpPrimaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpPrimaryDns.setStatus('current')
if mibBuilder.loadTexts: staticIpPrimaryDns.setDescription('the primary dns.')
staticIpSecondaryDns = MibScalar((1, 3, 6, 1, 4, 1, 12919, 7, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticIpSecondaryDns.setStatus('current')
if mibBuilder.loadTexts: staticIpSecondaryDns.setDescription('the secodary dns.')
rebootEnable = MibScalar((1, 3, 6, 1, 4, 1, 12919, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rebootEnable.setStatus('current')
if mibBuilder.loadTexts: rebootEnable.setDescription('catv switch function.')
tftpSevIp = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpSevIp.setStatus('current')
if mibBuilder.loadTexts: tftpSevIp.setDescription('The tftp server ip.')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileName.setStatus('current')
if mibBuilder.loadTexts: fileName.setDescription('The file name.')
fileType = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileType.setStatus('current')
if mibBuilder.loadTexts: fileType.setDescription(' i for image and c for configuration data')
action = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: action.setStatus('current')
if mibBuilder.loadTexts: action.setDescription('Get or Put file action,g for get file and p for put file.')
adminStatus = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminStatus.setStatus('current')
if mibBuilder.loadTexts: adminStatus.setDescription('administrative status.')
operStatus = MibScalar((1, 3, 6, 1, 4, 1, 12919, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: operStatus.setStatus('current')
if mibBuilder.loadTexts: operStatus.setDescription('vendor specific info.')
port1 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port1.setStatus('current')
if mibBuilder.loadTexts: port1.setDescription('lan port enable/disable.')
port2 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port2.setStatus('current')
if mibBuilder.loadTexts: port2.setDescription('lan port enable/disable.')
port3 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port3.setStatus('current')
if mibBuilder.loadTexts: port3.setDescription('lan port enable/disable.')
port4 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 10, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: port4.setStatus('current')
if mibBuilder.loadTexts: port4.setDescription('lan port enable/disable.')
jumblan1 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan1.setStatus('current')
if mibBuilder.loadTexts: jumblan1.setDescription('lan jumb mode 1522/2048/10240.')
jumblan2 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan2.setStatus('current')
if mibBuilder.loadTexts: jumblan2.setDescription('lan jumb mode 1522/2048/10240.')
jumblan3 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan3.setStatus('current')
if mibBuilder.loadTexts: jumblan3.setDescription('lan jumb mode 1522/2048/10240.')
jumblan4 = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumblan4.setStatus('current')
if mibBuilder.loadTexts: jumblan4.setDescription('lan jumb mode 1522/2048/10240.')
jumbwan = MibScalar((1, 3, 6, 1, 4, 1, 12919, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("mode1", 0), ("mode2", 1), ("mode3", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jumbwan.setStatus('current')
if mibBuilder.loadTexts: jumbwan.setDescription('lan jumb mode 1522/2048/10240.')
serialnum = MibScalar((1, 3, 6, 1, 4, 1, 12919, 12, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialnum.setStatus('current')
if mibBuilder.loadTexts: serialnum.setDescription('display device serial number.')
mibBuilder.exportSymbols("XAVI-XG6846-MIB", serialnum=serialnum, broadcastsTransmitted=broadcastsTransmitted, staticIpSubMask=staticIpSubMask, temperature=temperature, qos=qos, vendorRev=vendorRev, statIndex=statIndex, staticIpSecondaryDns=staticIpSecondaryDns, multicastsReceived=multicastsReceived, wan=wan, lan3=lan3, qosEntry=qosEntry, port4=port4, deviceinfo=deviceinfo, vlangroupTable=vlangroupTable, vendorPn=vendorPn, pauseReceived=pauseReceived, portmode=portmode, port2=port2, port1=port1, jumblan4=jumblan4, bias=bias, staticIpDomainName=staticIpDomainName, speed=speed, wanType=wanType, vendorName=vendorName, jumblan3=jumblan3, portPower=portPower, domainame=domainame, multicastsTransmitted=multicastsTransmitted, tftpSevIp=tftpSevIp, vlan=vlan, modeEntry=modeEntry, jumblan2=jumblan2, qosIndex=qosIndex, fileType=fileType, reboot=reboot, rebootEnable=rebootEnable, staticDns=staticDns, lanportName=lanportName, voltage=voltage, lan2=lan2, fileName=fileName, statisticTable=statisticTable, hostname=hostname, lanportpause=lanportpause, portIndex=portIndex, adminStatus=adminStatus, xg6846=xg6846, lan4=lan4, staticIpAddr=staticIpAddr, lanportIndex=lanportIndex, catvEnable=catvEnable, unicastsTransmitted=unicastsTransmitted, qmapping=qmapping, internetPort=internetPort, pauseTransmitted=pauseTransmitted, primaryDns=primaryDns, unicastsReceived=unicastsReceived, fcsErrorTransmitted=fcsErrorTransmitted, staticIpHostName=staticIpHostName, jumb=jumb, fcsErrorReceived=fcsErrorReceived, action=action, catv=catv, portStatistic=portStatistic, priority=priority, jumbwan=jumbwan, lan1=lan1, ddminfo=ddminfo, portStatEntry=portStatEntry, secondaryDns=secondaryDns, broadcastsReceived=broadcastsReceived, vlanid=vlanid, tftp=tftp, txPower=txPower, portEntry=portEntry, staticIpGateway=staticIpGateway, operStatus=operStatus, qmode=qmode, portTable=portTable, staticIpPrimaryDns=staticIpPrimaryDns, groupIndex=groupIndex, lanportTable=lanportTable, rxPower=rxPower, dscpEnable=dscpEnable, port3=port3, vendorOui=vendorOui, groupEntry=groupEntry, jumblan1=jumblan1, lanportspeed=lanportspeed, qosTable=qosTable, groupid=groupid, portName=portName)
