#
# PySNMP MIB module ATM-FORUM-ADDR-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-ADDR-REG
# Produced by pysmi-1.1.8 at Mon Jan  9 10:23:39 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
atmfAddressRegistrationAdminGroup, atmfAddressGroup, AtmAddress, NetPrefix, atmfNetPrefixGroup = mibBuilder.importSymbols("ATM-FORUM-TC-MIB", "atmfAddressRegistrationAdminGroup", "atmfAddressGroup", "AtmAddress", "NetPrefix", "atmfNetPrefixGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Gauge32, ObjectIdentity, Counter64, TimeTicks, Unsigned32, iso, MibIdentifier, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks", "Unsigned32", "iso", "MibIdentifier", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmfNetPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 7, 1), )
if mibBuilder.loadTexts: atmfNetPrefixTable.setStatus('mandatory')
atmfNetPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPort"), (0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPrefix"))
if mibBuilder.loadTexts: atmfNetPrefixEntry.setStatus('mandatory')
atmfNetPrefixPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfNetPrefixPort.setStatus('mandatory')
atmfNetPrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 2), NetPrefix()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfNetPrefixPrefix.setStatus('mandatory')
atmfNetPrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfNetPrefixStatus.setStatus('mandatory')
atmfAddressTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 6, 1), )
if mibBuilder.loadTexts: atmfAddressTable.setStatus('mandatory')
atmfAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfAddressPort"), (0, "ATM-FORUM-ADDR-REG", "atmfAddressAtmAddress"))
if mibBuilder.loadTexts: atmfAddressEntry.setStatus('mandatory')
atmfAddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressPort.setStatus('mandatory')
atmfAddressAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 2), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressAtmAddress.setStatus('mandatory')
atmfAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfAddressStatus.setStatus('mandatory')
atmfAddressOrgScope = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("localNetwork", 1), ("localNetworkPlusOne", 2), ("localNetworkPlusTwo", 3), ("siteMinusOne", 4), ("intraSite", 5), ("sitePlusOne", 6), ("organizationMinusOne", 7), ("intraOrganization", 8), ("organizationPlusOne", 9), ("communityMinusOne", 10), ("intraCommunity", 11), ("communityPlusOne", 12), ("regional", 13), ("interRegional", 14), ("global", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfAddressOrgScope.setStatus('mandatory')
atmfAddressRegistrationAdminTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 11, 1), )
if mibBuilder.loadTexts: atmfAddressRegistrationAdminTable.setStatus('mandatory')
atmfAddressRegistrationAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfAddressRegistrationAdminIndex"))
if mibBuilder.loadTexts: atmfAddressRegistrationAdminEntry.setStatus('mandatory')
atmfAddressRegistrationAdminIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressRegistrationAdminIndex.setStatus('mandatory')
atmfAddressRegistrationAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressRegistrationAdminStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-FORUM-ADDR-REG", atmfNetPrefixPort=atmfNetPrefixPort, atmfAddressStatus=atmfAddressStatus, atmfNetPrefixPrefix=atmfNetPrefixPrefix, atmfAddressAtmAddress=atmfAddressAtmAddress, atmfAddressRegistrationAdminIndex=atmfAddressRegistrationAdminIndex, atmfAddressPort=atmfAddressPort, atmfAddressRegistrationAdminTable=atmfAddressRegistrationAdminTable, atmfNetPrefixTable=atmfNetPrefixTable, atmfNetPrefixStatus=atmfNetPrefixStatus, atmfNetPrefixEntry=atmfNetPrefixEntry, atmfAddressTable=atmfAddressTable, atmfAddressOrgScope=atmfAddressOrgScope, atmfAddressRegistrationAdminEntry=atmfAddressRegistrationAdminEntry, atmfAddressEntry=atmfAddressEntry, atmfAddressRegistrationAdminStatus=atmfAddressRegistrationAdminStatus)
