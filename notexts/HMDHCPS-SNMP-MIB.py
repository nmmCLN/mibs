#
# PySNMP MIB module HMDHCPS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/hmdhcps
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:49 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmConfiguration, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hmConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, iso, Unsigned32, Bits, Gauge32, TimeTicks, ObjectIdentity, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "iso", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "ObjectIdentity", "NotificationType", "ModuleIdentity")
RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
hmDhcps = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 16))
hmDhcps.setRevisions(('2013-04-18 12:00', '2011-12-20 12:00', '2007-10-16 12:00',))
if mibBuilder.loadTexts: hmDhcps.setLastUpdated('201304181200Z')
if mibBuilder.loadTexts: hmDhcps.setOrganization('Hirschmann Automation and Control GmbH')
hmDHCPServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 16, 1))
hmDHCPServerConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1))
hmDHCPServerLeaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2))
hmDHCPServerInterfaceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3))
hmDHCPServerCounterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4))
hmDHCPServerMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDHCPServerMode.setStatus('current')
hmDHCPServerMaxPoolEntries = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerMaxPoolEntries.setStatus('current')
hmDHCPServerMaxLeaseEntries = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerMaxLeaseEntries.setStatus('current')
hmDHCPServerAddrProbe = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDHCPServerAddrProbe.setStatus('current')
hmDHCPServerPoolTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5), )
if mibBuilder.loadTexts: hmDHCPServerPoolTable.setStatus('current')
hmDHCPServerPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1), ).setIndexNames((0, "HMDHCPS-SNMP-MIB", "hmDHCPServerPoolIndex"))
if mibBuilder.loadTexts: hmDHCPServerPoolEntry.setStatus('current')
hmDHCPServerPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerPoolIndex.setStatus('current')
hmDHCPServerPoolStartIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDHCPServerPoolStartIpAddress.setStatus('current')
hmDHCPServerPoolEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolEndIpAddress.setStatus('current')
hmDHCPServerPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 4), Unsigned32().clone(86400)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolLeaseTime.setStatus('current')
hmDHCPServerPoolFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 5), Bits().clone(namedValues=NamedValues(("interface", 0), ("mac", 1), ("gateway", 2), ("clientid", 3), ("remoteid", 4), ("circuitid", 5), ("dynamic", 6), ("vlanid", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolFlags.setStatus('current')
hmDHCPServerPoolIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolIfIndex.setStatus('current')
hmDHCPServerPoolMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 7), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolMacAddress.setStatus('current')
hmDHCPServerPoolGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolGateway.setStatus('current')
hmDHCPServerPoolClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 9), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolClientId.setStatus('current')
hmDHCPServerPoolRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 10), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolRemoteId.setStatus('current')
hmDHCPServerPoolCircuitId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 11), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolCircuitId.setStatus('current')
hmDHCPServerPoolHirschmannClient = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolHirschmannClient.setStatus('current')
hmDHCPServerPoolVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolVlanId.setStatus('current')
hmDHCPServerPoolOptionConfFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 70))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionConfFileName.setStatus('current')
hmDHCPServerPoolOptionGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 31), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionGateway.setStatus('current')
hmDHCPServerPoolOptionNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 32), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionNetmask.setStatus('current')
hmDHCPServerPoolOptionWINS = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 33), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionWINS.setStatus('current')
hmDHCPServerPoolOptionDNS = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 34), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionDNS.setStatus('current')
hmDHCPServerPoolOptionHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 35), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionHostname.setStatus('current')
hmDHCPServerPoolOptionVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 36), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolOptionVendor.setStatus('current')
hmDHCPServerPoolErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 99), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerPoolErrorStatus.setStatus('current')
hmDHCPServerPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 100), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmDHCPServerPoolRowStatus.setStatus('current')
hmDHCPServerLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1), )
if mibBuilder.loadTexts: hmDHCPServerLeaseTable.setStatus('current')
hmDHCPServerLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1), ).setIndexNames((0, "HMDHCPS-SNMP-MIB", "hmDHCPServerLeasePoolIndex"), (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerLeaseIpAddress"))
if mibBuilder.loadTexts: hmDHCPServerLeaseEntry.setStatus('current')
hmDHCPServerLeasePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeasePoolIndex.setStatus('current')
hmDHCPServerLeaseIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseIpAddress.setStatus('current')
hmDHCPServerLeaseState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("bootp", 1), ("offering", 2), ("requesting", 3), ("bound", 4), ("renewing", 5), ("rebinding", 6), ("declined", 7), ("released", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseState.setStatus('current')
hmDHCPServerLeaseTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseTimeRemaining.setStatus('current')
hmDHCPServerLeaseIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseIfIndex.setStatus('current')
hmDHCPServerLeaseClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseClientMacAddress.setStatus('current')
hmDHCPServerLeaseGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseGateway.setStatus('current')
hmDHCPServerLeaseClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseClientId.setStatus('current')
hmDHCPServerLeaseRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseRemoteId.setStatus('current')
hmDHCPServerLeaseCircuitId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseCircuitId.setStatus('current')
hmDHCPServerLeaseStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseStartTime.setStatus('current')
hmDHCPServerLeaseAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("release", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDHCPServerLeaseAction.setStatus('current')
hmDHCPServerLeaseVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerLeaseVlanId.setStatus('current')
hmDHCPServerIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1), )
if mibBuilder.loadTexts: hmDHCPServerIfConfigTable.setStatus('current')
hmDHCPServerIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1), ).setIndexNames((0, "HMDHCPS-SNMP-MIB", "hmDHCPServerIfConfigIndex"))
if mibBuilder.loadTexts: hmDHCPServerIfConfigEntry.setStatus('current')
hmDHCPServerIfConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerIfConfigIndex.setStatus('current')
hmDHCPServerIfConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmDHCPServerIfConfigMode.setStatus('current')
hmDHCPServerCounterIfTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2), )
if mibBuilder.loadTexts: hmDHCPServerCounterIfTable.setStatus('current')
hmDHCPServerCounterIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1), ).setIndexNames((0, "HMDHCPS-SNMP-MIB", "hmDHCPServerCounterIfIndex"))
if mibBuilder.loadTexts: hmDHCPServerCounterIfEntry.setStatus('current')
hmDHCPServerCounterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterIfIndex.setStatus('current')
hmDHCPServerCounterBootpRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterBootpRequests.setStatus('current')
hmDHCPServerCounterBootpInvalids = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterBootpInvalids.setStatus('current')
hmDHCPServerCounterBootpReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterBootpReplies.setStatus('current')
hmDHCPServerCounterBootpDroppedUnknownClients = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterBootpDroppedUnknownClients.setStatus('current')
hmDHCPServerCounterBootpDroppedNotServingSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterBootpDroppedNotServingSubnet.setStatus('current')
hmDHCPServerCounterDhcpv4Discovers = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Discovers.setStatus('current')
hmDHCPServerCounterDhcpv4Offers = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Offers.setStatus('current')
hmDHCPServerCounterDhcpv4Requests = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Requests.setStatus('current')
hmDHCPServerCounterDhcpv4Declines = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Declines.setStatus('current')
hmDHCPServerCounterDhcpv4Acks = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Acks.setStatus('current')
hmDHCPServerCounterDhcpv4Naks = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Naks.setStatus('current')
hmDHCPServerCounterDhcpv4Releases = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Releases.setStatus('current')
hmDHCPServerCounterDhcpv4Informs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Informs.setStatus('current')
hmDHCPServerCounterDhcpv4ForcedRenews = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4ForcedRenews.setStatus('current')
hmDHCPServerCounterDhcpv4Invalids = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4Invalids.setStatus('current')
hmDHCPServerCounterDhcpv4DroppedUnknownClient = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4DroppedUnknownClient.setStatus('current')
hmDHCPServerCounterDhcpv4DroppedNotServingSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterDhcpv4DroppedNotServingSubnet.setStatus('current')
hmDHCPServerCounterMiscOtherDhcpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmDHCPServerCounterMiscOtherDhcpServer.setStatus('current')
mibBuilder.exportSymbols("HMDHCPS-SNMP-MIB", hmDHCPServerCounterIfIndex=hmDHCPServerCounterIfIndex, hmDHCPServerCounterDhcpv4Informs=hmDHCPServerCounterDhcpv4Informs, hmDHCPServerMaxPoolEntries=hmDHCPServerMaxPoolEntries, hmDHCPServerPoolOptionWINS=hmDHCPServerPoolOptionWINS, hmDHCPServerIfConfigMode=hmDHCPServerIfConfigMode, hmDHCPServerPoolLeaseTime=hmDHCPServerPoolLeaseTime, hmDHCPServerPoolOptionDNS=hmDHCPServerPoolOptionDNS, hmDHCPServerLeaseClientId=hmDHCPServerLeaseClientId, hmDHCPServerLeaseVlanId=hmDHCPServerLeaseVlanId, hmDHCPServerCounterDhcpv4Declines=hmDHCPServerCounterDhcpv4Declines, hmDHCPServerCounterDhcpv4Acks=hmDHCPServerCounterDhcpv4Acks, hmDHCPServerMaxLeaseEntries=hmDHCPServerMaxLeaseEntries, hmDHCPServerLeaseTimeRemaining=hmDHCPServerLeaseTimeRemaining, hmDHCPServerIfConfigEntry=hmDHCPServerIfConfigEntry, hmDHCPServerCounterDhcpv4DroppedUnknownClient=hmDHCPServerCounterDhcpv4DroppedUnknownClient, hmDHCPServerGroup=hmDHCPServerGroup, hmDHCPServerIfConfigTable=hmDHCPServerIfConfigTable, hmDHCPServerCounterBootpDroppedNotServingSubnet=hmDHCPServerCounterBootpDroppedNotServingSubnet, hmDHCPServerPoolIfIndex=hmDHCPServerPoolIfIndex, hmDHCPServerInterfaceGroup=hmDHCPServerInterfaceGroup, hmDHCPServerPoolEntry=hmDHCPServerPoolEntry, hmDHCPServerLeaseGroup=hmDHCPServerLeaseGroup, hmDHCPServerPoolOptionVendor=hmDHCPServerPoolOptionVendor, hmDHCPServerPoolTable=hmDHCPServerPoolTable, hmDHCPServerCounterGroup=hmDHCPServerCounterGroup, hmDHCPServerLeaseIpAddress=hmDHCPServerLeaseIpAddress, hmDHCPServerCounterBootpInvalids=hmDHCPServerCounterBootpInvalids, hmDHCPServerCounterDhcpv4DroppedNotServingSubnet=hmDHCPServerCounterDhcpv4DroppedNotServingSubnet, hmDHCPServerPoolErrorStatus=hmDHCPServerPoolErrorStatus, hmDHCPServerMode=hmDHCPServerMode, hmDHCPServerAddrProbe=hmDHCPServerAddrProbe, hmDHCPServerLeaseTable=hmDHCPServerLeaseTable, hmDhcps=hmDhcps, hmDHCPServerLeaseState=hmDHCPServerLeaseState, hmDHCPServerCounterBootpRequests=hmDHCPServerCounterBootpRequests, PYSNMP_MODULE_ID=hmDhcps, hmDHCPServerCounterMiscOtherDhcpServer=hmDHCPServerCounterMiscOtherDhcpServer, hmDHCPServerLeaseAction=hmDHCPServerLeaseAction, hmDHCPServerPoolOptionHostname=hmDHCPServerPoolOptionHostname, hmDHCPServerCounterDhcpv4Invalids=hmDHCPServerCounterDhcpv4Invalids, hmDHCPServerCounterDhcpv4Discovers=hmDHCPServerCounterDhcpv4Discovers, hmDHCPServerIfConfigIndex=hmDHCPServerIfConfigIndex, hmDHCPServerCounterDhcpv4Naks=hmDHCPServerCounterDhcpv4Naks, hmDHCPServerPoolClientId=hmDHCPServerPoolClientId, hmDHCPServerCounterDhcpv4Offers=hmDHCPServerCounterDhcpv4Offers, hmDHCPServerCounterDhcpv4Requests=hmDHCPServerCounterDhcpv4Requests, hmDHCPServerPoolOptionNetmask=hmDHCPServerPoolOptionNetmask, hmDHCPServerCounterDhcpv4ForcedRenews=hmDHCPServerCounterDhcpv4ForcedRenews, hmDHCPServerCounterIfEntry=hmDHCPServerCounterIfEntry, hmDHCPServerLeaseRemoteId=hmDHCPServerLeaseRemoteId, hmDHCPServerCounterIfTable=hmDHCPServerCounterIfTable, hmDHCPServerCounterDhcpv4Releases=hmDHCPServerCounterDhcpv4Releases, hmDHCPServerPoolOptionConfFileName=hmDHCPServerPoolOptionConfFileName, hmDHCPServerPoolRowStatus=hmDHCPServerPoolRowStatus, hmDHCPServerLeaseIfIndex=hmDHCPServerLeaseIfIndex, hmDHCPServerPoolIndex=hmDHCPServerPoolIndex, hmDHCPServerPoolStartIpAddress=hmDHCPServerPoolStartIpAddress, hmDHCPServerLeaseEntry=hmDHCPServerLeaseEntry, hmDHCPServerPoolCircuitId=hmDHCPServerPoolCircuitId, hmDHCPServerPoolHirschmannClient=hmDHCPServerPoolHirschmannClient, hmDHCPServerLeaseStartTime=hmDHCPServerLeaseStartTime, hmDHCPServerCounterBootpDroppedUnknownClients=hmDHCPServerCounterBootpDroppedUnknownClients, hmDHCPServerPoolEndIpAddress=hmDHCPServerPoolEndIpAddress, hmDHCPServerPoolVlanId=hmDHCPServerPoolVlanId, hmDHCPServerPoolRemoteId=hmDHCPServerPoolRemoteId, hmDHCPServerLeaseCircuitId=hmDHCPServerLeaseCircuitId, hmDHCPServerConfigGroup=hmDHCPServerConfigGroup, hmDHCPServerLeasePoolIndex=hmDHCPServerLeasePoolIndex, hmDHCPServerLeaseClientMacAddress=hmDHCPServerLeaseClientMacAddress, hmDHCPServerPoolOptionGateway=hmDHCPServerPoolOptionGateway, hmDHCPServerLeaseGateway=hmDHCPServerLeaseGateway, hmDHCPServerPoolGateway=hmDHCPServerPoolGateway, hmDHCPServerCounterBootpReplies=hmDHCPServerCounterBootpReplies, hmDHCPServerPoolFlags=hmDHCPServerPoolFlags, hmDHCPServerPoolMacAddress=hmDHCPServerPoolMacAddress)
