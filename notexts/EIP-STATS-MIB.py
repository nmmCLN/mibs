#
# PySNMP MIB module EIP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/efficientip/EIP-STATS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:03 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, TimeTicks, Counter32, NotificationType, Integer32, IpAddress, iso, ModuleIdentity, enterprises, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter32", "NotificationType", "Integer32", "IpAddress", "iso", "ModuleIdentity", "enterprises", "ObjectIdentity", "NotificationType")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
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
mibBuilder.exportSymbols("EIP-STATS-MIB", eip=eip, products=products, eipDhcp6Stat=eipDhcp6Stat, eipDhcp6StatIndex=eipDhcp6StatIndex, eipDhcp6StatValue=eipDhcp6StatValue, eipDnsStatIndex=eipDnsStatIndex, eipDhcpStatValue=eipDhcpStatValue, eipDhcp6StatName=eipDhcp6StatName, eipDns=eipDns, eipDhcp6=eipDhcp6, eipDhcpStatTable=eipDhcpStatTable, eipDhcp=eipDhcp, eipDhcpStatName=eipDhcpStatName, eipDhcp6StatEntry=eipDhcp6StatEntry, eipDnsStat=eipDnsStat, eipDnsStatName=eipDnsStatName, eipDhcpStatEntry=eipDhcpStatEntry, eipDnsStatTable=eipDnsStatTable, eipDhcpStat=eipDhcpStat, eipDhcpStatIndex=eipDhcpStatIndex, eipDnsStatEntry=eipDnsStatEntry, eipDnsStatValue=eipDnsStatValue, eipDhcp6StatTable=eipDhcp6StatTable)
