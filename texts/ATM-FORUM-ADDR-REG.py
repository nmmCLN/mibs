#
# PySNMP MIB module ATM-FORUM-ADDR-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ATM-FORUM-ADDR-REG
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
atmfAddressGroup, atmfNetPrefixGroup, NetPrefix, atmfAddressRegistrationAdminGroup, AtmAddress = mibBuilder.importSymbols("ATM-FORUM-TC-MIB", "atmfAddressGroup", "atmfNetPrefixGroup", "NetPrefix", "atmfAddressRegistrationAdminGroup", "AtmAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmfNetPrefixTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 7, 1), )
if mibBuilder.loadTexts: atmfNetPrefixTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfNetPrefixTable.setDescription('A table implemented by the user-side IME, containing the\n                network-prefix(es) for ATM-layer addresses in effect on\n                the user side of the UNI.')
atmfNetPrefixEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPort"), (0, "ATM-FORUM-ADDR-REG", "atmfNetPrefixPrefix"))
if mibBuilder.loadTexts: atmfNetPrefixEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfNetPrefixEntry.setDescription('Information about a single network-prefix for\n                ATM-layer addresses in effect on the user-side IME.\n                Note that the index variable atmNetPrefixPrefix is a\n                variable-length string, and as such the rule for\n                variable-length strings in section 4.1.6 of RFC 1212\n                applies.')
atmfNetPrefixPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfNetPrefixPort.setStatus('mandatory')
if mibBuilder.loadTexts: atmfNetPrefixPort.setDescription('A unique value which identifies the UNI port for\n                which the network prefix for ATM addresses is in\n                effect.  The value of 0 has the special meaning of\n                identifying the local UNI.')
atmfNetPrefixPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 2), NetPrefix()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfNetPrefixPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: atmfNetPrefixPrefix.setDescription('The network prefix for ATM addresses which is in\n                effect on the user side of the ATM UNI port.')
atmfNetPrefixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfNetPrefixStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmfNetPrefixStatus.setDescription('An indication of the validity of the network prefix\n                for ATM addresses on the user side of the UNI port.\n                To configure a new network prefix in this table, the\n                network-side IME must set the appropriate instance of this\n                object to the value valid(1).  To delete an existing\n                network prefix in this table, the network-side IME must\n                set the appropriate instance of this object to the\n                value invalid(2).\n\n                If circumstances occur on the user-side IME which cause a\n                prefix to become invalid, the user-side IME modifies the\n                value of the appropriate instance of this object to invalid(2).\n\n                Whenever the value of this object for a particular\n                prefix becomes invalid(2), the conceptual row for that\n                prefix may be removed from the table at any time,\n                either immediately or subsequently.')
atmfAddressTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 6, 1), )
if mibBuilder.loadTexts: atmfAddressTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressTable.setDescription('A table implemented by the network-side IME, containing the\n                ATM-layer addresses in effect on the user side of the UNI.')
atmfAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfAddressPort"), (0, "ATM-FORUM-ADDR-REG", "atmfAddressAtmAddress"))
if mibBuilder.loadTexts: atmfAddressEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressEntry.setDescription('Information about a single ATM-layer address in effect\n                on the user-side IME.  Note that the index variable\n                atmAddressAtmAddress is a variable-length string, and as\n                such the rule for variable-length strings in section\n                4.1.6 of RFC 1212 applies.')
atmfAddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressPort.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressPort.setDescription('A unique value which identifies the UNI port for\n                which the ATM address is in effect.  The value of 0\n                has the special meaning of identifying the local UNI.')
atmfAddressAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 2), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressAtmAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressAtmAddress.setDescription('The ATM address which is in effect on the user side\n                of the ATM UNI port.')
atmfAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfAddressStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressStatus.setDescription('An indication of the validity of the ATM address at\n                the user side of the UNI port.  To configure a new\n                address in this table, the user-side IME must set the\n                appropriate instance of this object to the value\n                valid(1).  To delete an existing address in this table,\n                the user-side IME must set the appropriate instance of\n                this object to the value invalid(2).\n\n                If circumstances occur on the network-side IME which cause\n                an address to become invalid, the network-side IME\n                modifies the value of the appropriate instance of this\n                object to invalid(2).\n\n                Whenever the value of this object for a particular\n                address becomes invalid(2), the conceptual row for\n                that address may be removed from the table at any\n                time, either immediately or subsequently.')
atmfAddressOrgScope = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("localNetwork", 1), ("localNetworkPlusOne", 2), ("localNetworkPlusTwo", 3), ("siteMinusOne", 4), ("intraSite", 5), ("sitePlusOne", 6), ("organizationMinusOne", 7), ("intraOrganization", 8), ("organizationPlusOne", 9), ("communityMinusOne", 10), ("intraCommunity", 11), ("communityPlusOne", 12), ("regional", 13), ("interRegional", 14), ("global", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmfAddressOrgScope.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressOrgScope.setDescription("This object indicates the organizational\n                scope for the referenced address. The information of\n                the referenced address shall not be distributed\n                outside the indicated scope. If the user-side IME does\n                not specify a value for the atmfAddressOrgScope object,\n                the network shall set the value of this object to\n                localNetwork(1), if the registered address is an ATM group\n                address, or to global(15), if the registered address is \n                an individual address.  Refer to Annex 6.0\n                of ATM Forum UNI Signalling 4.0 for guidelines regarding\n                the use of organizational scopes.\n\n                This organization hierarchy may be mapped to ATM network's\n                routing hierarchy such as PNNI's routing level and\n                the mapping shall be configurable in\n                nodes. Use of this object in a public network is for\n                further study.\n                The default values for organizational scope are\n                localNetwork(1) for ATM group addresses, and global(15)\n                for individual addresses.")
atmfAddressRegistrationAdminTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 11, 1), )
if mibBuilder.loadTexts: atmfAddressRegistrationAdminTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressRegistrationAdminTable.setDescription('A table of Address Registration administrative\n                information for the ATM Interface.')
atmfAddressRegistrationAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1), ).setIndexNames((0, "ATM-FORUM-ADDR-REG", "atmfAddressRegistrationAdminIndex"))
if mibBuilder.loadTexts: atmfAddressRegistrationAdminEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressRegistrationAdminEntry.setDescription('An entry in the table, containing Address\n                Registration administrative information for the ATM\n                Interface.')
atmfAddressRegistrationAdminIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressRegistrationAdminIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressRegistrationAdminIndex.setDescription('The value of 0 which has the special meaning of\n                identifying the ATM Interface over which this message\n                was received.')
atmfAddressRegistrationAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("unsupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfAddressRegistrationAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmfAddressRegistrationAdminStatus.setDescription('An indication of whether or not Address Registration\n                is supported on this ATM Interface. Supported(1)\n                indicates that this ATM Interface supports address\n                registration. Unsupported(2) indicates that this ATM\n                Interface does not support address registration.')
mibBuilder.exportSymbols("ATM-FORUM-ADDR-REG", atmfAddressTable=atmfAddressTable, atmfNetPrefixEntry=atmfNetPrefixEntry, atmfAddressAtmAddress=atmfAddressAtmAddress, atmfNetPrefixTable=atmfNetPrefixTable, atmfAddressOrgScope=atmfAddressOrgScope, atmfAddressRegistrationAdminTable=atmfAddressRegistrationAdminTable, atmfAddressRegistrationAdminStatus=atmfAddressRegistrationAdminStatus, atmfAddressRegistrationAdminEntry=atmfAddressRegistrationAdminEntry, atmfAddressRegistrationAdminIndex=atmfAddressRegistrationAdminIndex, atmfAddressEntry=atmfAddressEntry, atmfAddressPort=atmfAddressPort, atmfNetPrefixPort=atmfNetPrefixPort, atmfNetPrefixPrefix=atmfNetPrefixPrefix, atmfNetPrefixStatus=atmfNetPrefixStatus, atmfAddressStatus=atmfAddressStatus)
