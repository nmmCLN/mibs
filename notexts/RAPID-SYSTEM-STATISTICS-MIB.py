#
# PySNMP MIB module RAPID-SYSTEM-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-SYSTEM-STATISTICS-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:03 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, NotificationType, TimeTicks, Gauge32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Counter32, IpAddress, enterprises, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Counter32", "IpAddress", "enterprises", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-05-16 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0105161200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
rsSystemStatisticsMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 3))
if mibBuilder.loadTexts: rsSystemStatisticsMIB.setStatus('current')
rsSystemCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil.setStatus('current')
rsSystemTotalSendBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalSendBytes.setStatus('current')
rsSystemTotalRecvBytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalRecvBytes.setStatus('current')
rsSystemTotalSendPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalSendPackets.setStatus('current')
rsSystemTotalRecvPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemTotalRecvPackets.setStatus('current')
rsSystemStreamReqTotal = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemStreamReqTotal.setStatus('current')
rsSystemStreamReqDrop = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemStreamReqDrop.setStatus('current')
rsSystemCpuUtil1 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 77), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil1.setStatus('current')
rsSystemCpuUtil5 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 78), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil5.setStatus('current')
rsSystemCpuUtil15 = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 3, 79), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemCpuUtil15.setStatus('current')
mibBuilder.exportSymbols("RAPID-SYSTEM-STATISTICS-MIB", PYSNMP_MODULE_ID=rsInfoModule, rsInfoModule=rsInfoModule, rsSystemTotalSendPackets=rsSystemTotalSendPackets, rsSystemCpuUtil15=rsSystemCpuUtil15, rsSystemStreamReqTotal=rsSystemStreamReqTotal, rsSystemCpuUtil1=rsSystemCpuUtil1, rsSystemTotalSendBytes=rsSystemTotalSendBytes, rsSystemCpuUtil5=rsSystemCpuUtil5, rsSystemCpuUtil=rsSystemCpuUtil, rsSystemTotalRecvBytes=rsSystemTotalRecvBytes, rsSystemTotalRecvPackets=rsSystemTotalRecvPackets, rsSystemStatisticsMIB=rsSystemStatisticsMIB, rsSystemStreamReqDrop=rsSystemStreamReqDrop)
