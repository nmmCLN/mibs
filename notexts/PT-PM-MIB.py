#
# PySNMP MIB module PT-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-PM-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 09:40:13 2022
# On host fv-az196-500 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, Gauge32, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ptPM = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 5))
ptPM.setRevisions(('2018-08-29 12:30', '2016-03-09 12:30', '2016-02-10 12:30',))
if mibBuilder.loadTexts: ptPM.setLastUpdated('201808291230Z')
if mibBuilder.loadTexts: ptPM.setOrganization('Ericsson')
ptPMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2))
ptPMTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1), )
if mibBuilder.loadTexts: ptPMTable.setStatus('current')
ptPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1), ).setIndexNames((0, "PT-PM-MIB", "queueIndex"))
if mibBuilder.loadTexts: ptPMEntry.setStatus('current')
queueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: queueIndex.setStatus('current')
forwardingPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingPacket.setStatus('current')
forwardingOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forwardingOctets.setStatus('current')
discardPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardPackets.setStatus('current')
discardOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: discardOctets.setStatus('current')
inputPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputPackets.setStatus('current')
inputOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inputOctets.setStatus('current')
ptPMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1))
ptPMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2))
ptPMFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 1, 1)).setObjects(("PT-PM-MIB", "ptPMCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMFullCompliance = ptPMFullCompliance.setStatus('current')
ptPMCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 5, 2, 2, 1)).setObjects(("PT-PM-MIB", "forwardingPacket"), ("PT-PM-MIB", "forwardingOctets"), ("PT-PM-MIB", "discardPackets"), ("PT-PM-MIB", "discardOctets"), ("PT-PM-MIB", "inputPackets"), ("PT-PM-MIB", "inputOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptPMCompleteGroup = ptPMCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-PM-MIB", discardOctets=discardOctets, inputPackets=inputPackets, discardPackets=discardPackets, forwardingOctets=forwardingOctets, ptPMGroups=ptPMGroups, ptPMConformance=ptPMConformance, PYSNMP_MODULE_ID=ptPM, ptPMTable=ptPMTable, ptPM=ptPM, queueIndex=queueIndex, inputOctets=inputOctets, ptPMEntry=ptPMEntry, ptPMFullCompliance=ptPMFullCompliance, ptPMCompleteGroup=ptPMCompleteGroup, ptPMCompliances=ptPMCompliances, forwardingPacket=forwardingPacket)
