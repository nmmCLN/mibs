#
# PySNMP MIB module AT-DNS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-DNS-CLIENT
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:31 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Gauge32, ObjectIdentity, iso, Bits, Unsigned32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "iso", "Bits", "Unsigned32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "MibIdentifier")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
atDNSClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1))
atDNSClient.setRevisions(('2010-06-14 04:45', '2008-09-18 12:00',))
if mibBuilder.loadTexts: atDNSClient.setLastUpdated('201006140445Z')
if mibBuilder.loadTexts: atDNSClient.setOrganization('Allied Telesis, Inc')
atDns = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501))
if mibBuilder.loadTexts: atDns.setStatus('current')
atDNSServerIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDNSServerIndexNext.setStatus('current')
atDNSServerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2), )
if mibBuilder.loadTexts: atDNSServerTable.setStatus('current')
atDNSServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1), ).setIndexNames((0, "AT-DNS-CLIENT-MIB", "atDNSServerIndex"))
if mibBuilder.loadTexts: atDNSServerEntry.setStatus('current')
atDNSServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atDNSServerIndex.setStatus('current')
atDNSServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDNSServerAddrType.setStatus('current')
atDNSServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atDNSServerAddr.setStatus('current')
atDNSServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 4), RowStatus().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atDNSServerStatus.setStatus('current')
mibBuilder.exportSymbols("AT-DNS-CLIENT-MIB", atDNSServerAddrType=atDNSServerAddrType, atDNSServerEntry=atDNSServerEntry, atDNSServerIndex=atDNSServerIndex, atDNSServerIndexNext=atDNSServerIndexNext, PYSNMP_MODULE_ID=atDNSClient, atDNSServerStatus=atDNSServerStatus, atDNSClient=atDNSClient, atDNSServerTable=atDNSServerTable, atDNSServerAddr=atDNSServerAddr, atDns=atDns)
