#
# PySNMP MIB module RADLAN-DNSCL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-DNSCL-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dnsResConfigSbeltEntry, = mibBuilder.importSymbols("DNS-RESOLVER-MIB", "dnsResConfigSbeltEntry")
DnsName, = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsName")
rlDnsCl, = mibBuilder.importSymbols("RADLAN-MIB", "rlDnsCl")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, Counter32, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlDnsClMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClMibVersion.setStatus('current')
rlDnsClEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClEnable.setStatus('current')
rlDnsClDomainNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 3), )
if mibBuilder.loadTexts: rlDnsClDomainNameTable.setStatus('current')
rlDnsClDomainNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 3, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClDomainNameName"))
if mibBuilder.loadTexts: rlDnsClDomainNameEntry.setStatus('current')
rlDnsClDomainNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 1), DnsName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameName.setStatus('current')
rlDnsClDomainNameOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameOwner.setStatus('current')
rlDnsClDomainNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClDomainNameRowStatus.setStatus('current')
rlDnsClMaxNumOfRetransmissions = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMaxNumOfRetransmissions.setStatus('current')
rlDnsClMinRetransmissionInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 93, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClMinRetransmissionInterval.setStatus('current')
rlDnsClNamesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 6), )
if mibBuilder.loadTexts: rlDnsClNamesTable.setStatus('current')
rlDnsClNamesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 6, 1), ).setIndexNames((0, "RADLAN-DNSCL-MIB", "rlDnsClNamesName"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesOwner"), (0, "RADLAN-DNSCL-MIB", "rlDnsClNamesIndex"))
if mibBuilder.loadTexts: rlDnsClNamesEntry.setStatus('current')
rlDnsClNamesName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 1), DnsName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlDnsClNamesName.setStatus('current')
rlDnsClNamesOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesOwner.setStatus('current')
rlDnsClNamesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlDnsClNamesIndex.setStatus('current')
rlDnsClNamesAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesAddr.setStatus('current')
rlDnsClNamesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDnsClNamesRowStatus.setStatus('current')
dnsResConfigSbeltExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 93, 7), )
if mibBuilder.loadTexts: dnsResConfigSbeltExtTable.setStatus('current')
dnsResConfigSbeltExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 93, 7, 1), )
dnsResConfigSbeltEntry.registerAugmentions(("RADLAN-DNSCL-MIB", "dnsResConfigSbeltExtEntry"))
dnsResConfigSbeltExtEntry.setIndexNames(*dnsResConfigSbeltEntry.getIndexNames())
if mibBuilder.loadTexts: dnsResConfigSbeltExtEntry.setStatus('current')
dnsResConfigSbeltOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 93, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dnsResConfigSbeltOwner.setStatus('current')
mibBuilder.exportSymbols("RADLAN-DNSCL-MIB", rlDnsClNamesOwner=rlDnsClNamesOwner, rlDnsClNamesRowStatus=rlDnsClNamesRowStatus, rlDnsClNamesEntry=rlDnsClNamesEntry, rlDnsClMinRetransmissionInterval=rlDnsClMinRetransmissionInterval, dnsResConfigSbeltExtTable=dnsResConfigSbeltExtTable, rlDnsClDomainNameName=rlDnsClDomainNameName, rlDnsClMibVersion=rlDnsClMibVersion, rlDnsClEnable=rlDnsClEnable, rlDnsClMaxNumOfRetransmissions=rlDnsClMaxNumOfRetransmissions, rlDnsClDomainNameEntry=rlDnsClDomainNameEntry, dnsResConfigSbeltOwner=dnsResConfigSbeltOwner, rlDnsClDomainNameOwner=rlDnsClDomainNameOwner, rlDnsClNamesName=rlDnsClNamesName, rlDnsClDomainNameRowStatus=rlDnsClDomainNameRowStatus, rlDnsClNamesAddr=rlDnsClNamesAddr, rlDnsClNamesTable=rlDnsClNamesTable, rlDnsClNamesIndex=rlDnsClNamesIndex, dnsResConfigSbeltExtEntry=dnsResConfigSbeltExtEntry, rlDnsClDomainNameTable=rlDnsClDomainNameTable)
