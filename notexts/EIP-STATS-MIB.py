#
# PySNMP MIB module EIP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/efficientip/EIP-STATS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:25 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, enterprises, NotificationType, Counter64, iso, TimeTicks, ModuleIdentity, Unsigned32, Counter32, NotificationType, Gauge32, ObjectIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "NotificationType", "Counter64", "iso", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
eip = MibIdentifier((1, 3, 6, 1, 4, 1, 2440))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1))
eipDns = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 4))
eipDnsStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2))
eipDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 3))
eipDhcpStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2))
eipDhcp6 = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 7))
eipDhcp6Stat = MibIdentifier((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1))
eipDnsStatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3), )
if mibBuilder.loadTexts: eipDnsStatTable.setStatus('mandatory')
eipDnsStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDnsStatName"))
if mibBuilder.loadTexts: eipDnsStatEntry.setStatus('mandatory')
eipDnsStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatIndex.setStatus('mandatory')
eipDnsStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatName.setStatus('mandatory')
eipDnsStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 4, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDnsStatValue.setStatus('mandatory')
eipDhcpStatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22), )
if mibBuilder.loadTexts: eipDhcpStatTable.setStatus('mandatory')
eipDhcpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDhcpStatName"))
if mibBuilder.loadTexts: eipDhcpStatEntry.setStatus('mandatory')
eipDhcpStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatIndex.setStatus('mandatory')
eipDhcpStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatName.setStatus('mandatory')
eipDhcpStatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 3, 2, 22, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcpStatValue.setStatus('mandatory')
eipDhcp6StatTable = MibTable((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1), )
if mibBuilder.loadTexts: eipDhcp6StatTable.setStatus('mandatory')
eipDhcp6StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1), ).setIndexNames((0, "EIP-STATS-MIB", "eipDhcp6StatName"))
if mibBuilder.loadTexts: eipDhcp6StatEntry.setStatus('mandatory')
eipDhcp6StatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatIndex.setStatus('mandatory')
eipDhcp6StatName = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatName.setStatus('mandatory')
eipDhcp6StatValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2440, 1, 7, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eipDhcp6StatValue.setStatus('mandatory')
mibBuilder.exportSymbols("EIP-STATS-MIB", eipDnsStat=eipDnsStat, eipDhcp6StatTable=eipDhcp6StatTable, eipDhcpStatEntry=eipDhcpStatEntry, eipDhcp6StatIndex=eipDhcp6StatIndex, eipDnsStatValue=eipDnsStatValue, eipDhcp6=eipDhcp6, eipDhcp6StatEntry=eipDhcp6StatEntry, eipDhcpStatTable=eipDhcpStatTable, eipDnsStatIndex=eipDnsStatIndex, eipDhcpStat=eipDhcpStat, eip=eip, eipDhcp6Stat=eipDhcp6Stat, eipDhcp6StatValue=eipDhcp6StatValue, eipDns=eipDns, eipDhcpStatValue=eipDhcpStatValue, eipDhcpStatName=eipDhcpStatName, eipDhcp=eipDhcp, eipDhcp6StatName=eipDhcp6StatName, products=products, eipDhcpStatIndex=eipDhcpStatIndex, eipDnsStatEntry=eipDnsStatEntry, eipDnsStatTable=eipDnsStatTable, eipDnsStatName=eipDnsStatName)
