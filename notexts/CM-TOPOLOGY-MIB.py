#
# PySNMP MIB module CM-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-TOPOLOGY-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:26 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
shelfIndex, slotIndex, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "slotIndex", "neIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Gauge32, MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, Counter64, Counter32, IpAddress, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Gauge32", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "Unsigned32", "Bits")
TextualConvention, DateAndTime, VariablePointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "VariablePointer", "DisplayString")
cmTopologyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9))
cmTopologyMIB.setRevisions(('2008-03-03 00:00',))
if mibBuilder.loadTexts: cmTopologyMIB.setLastUpdated('200803030000Z')
if mibBuilder.loadTexts: cmTopologyMIB.setOrganization('ADVA Optical Networking')
cmTopologyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1))
cmTopologyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2))
cmTopologyRegionId = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyRegionId.setStatus('current')
cmTopologyRegionDescr = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyRegionDescr.setStatus('current')
cmTopologyRegionLastUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyRegionLastUpdateTime.setStatus('current')
cmTopologyItemTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4), )
if mibBuilder.loadTexts: cmTopologyItemTable.setStatus('current')
cmTopologyItemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"))
if mibBuilder.loadTexts: cmTopologyItemEntry.setStatus('current')
cmTopologyItemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyItemId.setStatus('current')
cmTopologyItemDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyItemDescr.setStatus('current')
cmTopologyLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5), )
if mibBuilder.loadTexts: cmTopologyLinkTable.setStatus('current')
cmTopologyLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1), ).setIndexNames((0, "CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"))
if mibBuilder.loadTexts: cmTopologyLinkEntry.setStatus('current')
cmTopologyLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyLinkId.setStatus('current')
cmTopologyLinkFromPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 2), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyLinkFromPort.setStatus('current')
cmTopologyLinkToPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyLinkToPort.setStatus('current')
cmTopologyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1))
cmTopologyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2))
cmTopologyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1, 1)).setObjects(("CM-TOPOLOGY-MIB", "cmTopologyObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmTopologyCompliance = cmTopologyCompliance.setStatus('current')
cmTopologyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2, 1)).setObjects(("CM-TOPOLOGY-MIB", "cmTopologyRegionId"), ("CM-TOPOLOGY-MIB", "cmTopologyRegionDescr"), ("CM-TOPOLOGY-MIB", "cmTopologyRegionLastUpdateTime"), ("CM-TOPOLOGY-MIB", "cmTopologyItemId"), ("CM-TOPOLOGY-MIB", "cmTopologyItemDescr"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkId"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkToPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmTopologyObjectGroup = cmTopologyObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CM-TOPOLOGY-MIB", cmTopologyLinkEntry=cmTopologyLinkEntry, cmTopologyItemEntry=cmTopologyItemEntry, cmTopologyCompliances=cmTopologyCompliances, cmTopologyMIB=cmTopologyMIB, cmTopologyItemDescr=cmTopologyItemDescr, cmTopologyRegionId=cmTopologyRegionId, cmTopologyItemId=cmTopologyItemId, cmTopologyGroups=cmTopologyGroups, PYSNMP_MODULE_ID=cmTopologyMIB, cmTopologyItemTable=cmTopologyItemTable, cmTopologyRegionLastUpdateTime=cmTopologyRegionLastUpdateTime, cmTopologyLinkId=cmTopologyLinkId, cmTopologyCompliance=cmTopologyCompliance, cmTopologyObjects=cmTopologyObjects, cmTopologyRegionDescr=cmTopologyRegionDescr, cmTopologyLinkFromPort=cmTopologyLinkFromPort, cmTopologyObjectGroup=cmTopologyObjectGroup, cmTopologyConformance=cmTopologyConformance, cmTopologyLinkTable=cmTopologyLinkTable, cmTopologyLinkToPort=cmTopologyLinkToPort)
