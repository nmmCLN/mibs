#
# PySNMP MIB module ACD-SHAPER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-SHAPER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:37 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, ModuleIdentity, Counter32, MibIdentifier, iso, NotificationType, Integer32, IpAddress, Gauge32, ObjectIdentity, Unsigned32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "iso", "NotificationType", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acdShaper = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 10))
acdShaper.setRevisions(('2009-11-01 01:00',))
if mibBuilder.loadTexts: acdShaper.setLastUpdated('200911010100Z')
if mibBuilder.loadTexts: acdShaper.setOrganization('Accedian Networks, Inc.')
acdShaper1 = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1))
acdShaper1MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1))
acdShaper1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2))
acdShaper1Config = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 1))
acdShaper1Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2))
acdShaper1CodePointStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1), )
if mibBuilder.loadTexts: acdShaper1CodePointStatsTable.setStatus('current')
acdShaper1CodePointStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1), ).setIndexNames((0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsDstID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsSrcID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsColorID"), (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsPcpID"))
if mibBuilder.loadTexts: acdShaper1CodePointStatsEntry.setStatus('current')
acdShaper1CodePointStatsDstID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsDstID.setStatus('current')
acdShaper1CodePointStatsSrcID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsSrcID.setStatus('current')
acdShaper1CodePointStatsColorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2))))
if mibBuilder.loadTexts: acdShaper1CodePointStatsColorID.setStatus('current')
acdShaper1CodePointStatsPcpID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: acdShaper1CodePointStatsPcpID.setStatus('current')
acdShaper1CodePointStatsFwdOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 5), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdOctets.setStatus('current')
acdShaper1CodePointStatsFwdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdPkts.setStatus('current')
acdShaper1CodePointStatsFwdRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 7), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsFwdRate.setStatus('current')
acdShaper1CodePointStatsDelayedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 8), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedOctets.setStatus('current')
acdShaper1CodePointStatsDelayedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 9), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedPkts.setStatus('current')
acdShaper1CodePointStatsDelayedRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 10), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsDelayedRate.setStatus('current')
acdShaper1CodePointStatsOverflowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowOctets.setStatus('current')
acdShaper1CodePointStatsOverflowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 12), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowPkts.setStatus('current')
acdShaper1CodePointStatsOverflowRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 13), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsOverflowRate.setStatus('current')
acdShaper1CodePointStatsQMgmtDropOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 14), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropOctets.setStatus('current')
acdShaper1CodePointStatsQMgmtDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 15), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropPkts.setStatus('current')
acdShaper1CodePointStatsQMgmtDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 16), Gauge32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdShaper1CodePointStatsQMgmtDropRate.setStatus('current')
acdShaper1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1))
acdShaper1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2))
acdShaper1CodePointStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2, 1)).setObjects(("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowRate"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropOctets"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropPkts"), ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdShaper1CodePointStatsGroup = acdShaper1CodePointStatsGroup.setStatus('current')
acdShaper1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1, 1)).setObjects(("ACD-SHAPER-MIB", "acdShaper1CodePointStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdShaper1Compliance = acdShaper1Compliance.setStatus('current')
mibBuilder.exportSymbols("ACD-SHAPER-MIB", acdShaper1Groups=acdShaper1Groups, acdShaper1CodePointStatsEntry=acdShaper1CodePointStatsEntry, acdShaper1CodePointStatsQMgmtDropOctets=acdShaper1CodePointStatsQMgmtDropOctets, acdShaper=acdShaper, acdShaper1CodePointStatsOverflowPkts=acdShaper1CodePointStatsOverflowPkts, PYSNMP_MODULE_ID=acdShaper, acdShaper1CodePointStatsGroup=acdShaper1CodePointStatsGroup, acdShaper1CodePointStatsPcpID=acdShaper1CodePointStatsPcpID, acdShaper1Config=acdShaper1Config, acdShaper1CodePointStatsDstID=acdShaper1CodePointStatsDstID, acdShaper1CodePointStatsFwdPkts=acdShaper1CodePointStatsFwdPkts, acdShaper1CodePointStatsDelayedPkts=acdShaper1CodePointStatsDelayedPkts, acdShaper1CodePointStatsOverflowOctets=acdShaper1CodePointStatsOverflowOctets, acdShaper1=acdShaper1, acdShaper1CodePointStatsColorID=acdShaper1CodePointStatsColorID, acdShaper1CodePointStatsOverflowRate=acdShaper1CodePointStatsOverflowRate, acdShaper1Compliance=acdShaper1Compliance, acdShaper1Conformance=acdShaper1Conformance, acdShaper1CodePointStatsTable=acdShaper1CodePointStatsTable, acdShaper1CodePointStatsSrcID=acdShaper1CodePointStatsSrcID, acdShaper1Compliances=acdShaper1Compliances, acdShaper1CodePointStatsQMgmtDropPkts=acdShaper1CodePointStatsQMgmtDropPkts, acdShaper1CodePointStatsFwdOctets=acdShaper1CodePointStatsFwdOctets, acdShaper1MIBObjects=acdShaper1MIBObjects, acdShaper1Stats=acdShaper1Stats, acdShaper1CodePointStatsFwdRate=acdShaper1CodePointStatsFwdRate, acdShaper1CodePointStatsDelayedOctets=acdShaper1CodePointStatsDelayedOctets, acdShaper1CodePointStatsDelayedRate=acdShaper1CodePointStatsDelayedRate, acdShaper1CodePointStatsQMgmtDropRate=acdShaper1CodePointStatsQMgmtDropRate)
