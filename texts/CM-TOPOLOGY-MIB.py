#
# PySNMP MIB module CM-TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-TOPOLOGY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:40 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
neIndex, slotIndex, shelfIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex", "slotIndex", "shelfIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter64, Gauge32, IpAddress, MibIdentifier, ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "NotificationType")
DateAndTime, TextualConvention, DisplayString, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString", "VariablePointer")
cmTopologyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9))
cmTopologyMIB.setRevisions(('2008-03-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmTopologyMIB.setRevisionsDescriptions(('Notes from release 200803030000Z,\n             (1)MIB version ready for release FSP150CM 3.1.',))
if mibBuilder.loadTexts: cmTopologyMIB.setLastUpdated('200803030000Z')
if mibBuilder.loadTexts: cmTopologyMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: cmTopologyMIB.setContactInfo('        Raghav Trivedi\n                     ADVA Optical Networking, Inc.\n                Tel: +1 972 759-1239\n             E-mail: rtrivedi@advaoptical.com\n             Postal: 2301 N. Greenville Ave. #300\n                     Richardson, TX USA 75082')
if mibBuilder.loadTexts: cmTopologyMIB.setDescription('This module defines the Topology MIB definitions \n             used by the F3 (FSP150CM/CC) product lines.  \n             Copyright (C) ADVA Optical Networking.')
cmTopologyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1))
cmTopologyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2))
cmTopologyRegionId = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyRegionId.setStatus('current')
if mibBuilder.loadTexts: cmTopologyRegionId.setDescription('User specified name of the topology region.')
cmTopologyRegionDescr = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyRegionDescr.setStatus('current')
if mibBuilder.loadTexts: cmTopologyRegionDescr.setDescription('Description of the topology region.')
cmTopologyRegionLastUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyRegionLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: cmTopologyRegionLastUpdateTime.setDescription('Time when the topology region was last updated.')
cmTopologyItemTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4), )
if mibBuilder.loadTexts: cmTopologyItemTable.setStatus('current')
if mibBuilder.loadTexts: cmTopologyItemTable.setDescription('A list of entries corresponding to the topology items. \n             Entries cannot be created in this table by management\n             application action.')
cmTopologyItemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"))
if mibBuilder.loadTexts: cmTopologyItemEntry.setStatus('current')
if mibBuilder.loadTexts: cmTopologyItemEntry.setDescription('An entry containing information applicable to a particular\n             topology item.')
cmTopologyItemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyItemId.setStatus('current')
if mibBuilder.loadTexts: cmTopologyItemId.setDescription('User specified name of the topology item.')
cmTopologyItemDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyItemDescr.setStatus('current')
if mibBuilder.loadTexts: cmTopologyItemDescr.setDescription('Description of the topology item.')
cmTopologyLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5), )
if mibBuilder.loadTexts: cmTopologyLinkTable.setStatus('current')
if mibBuilder.loadTexts: cmTopologyLinkTable.setDescription('A list of entries corresponding to the topology links. \n             Entries cannot be created in this table by management\n             application action.')
cmTopologyLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1), ).setIndexNames((0, "CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"))
if mibBuilder.loadTexts: cmTopologyLinkEntry.setStatus('current')
if mibBuilder.loadTexts: cmTopologyLinkEntry.setDescription('An entry containing information applicable to a particular\n             topology item.')
cmTopologyLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmTopologyLinkId.setStatus('current')
if mibBuilder.loadTexts: cmTopologyLinkId.setDescription('User specified name of the topology link.')
cmTopologyLinkFromPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 2), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyLinkFromPort.setStatus('current')
if mibBuilder.loadTexts: cmTopologyLinkFromPort.setDescription('Topology Link connects two Network Elements.  This object\n          points to the FROM end Port.')
cmTopologyLinkToPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 1, 5, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmTopologyLinkToPort.setStatus('current')
if mibBuilder.loadTexts: cmTopologyLinkToPort.setDescription('Topology Link connects two Network Elements.  This object\n          points to the TO end point.')
cmTopologyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1))
cmTopologyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2))
cmTopologyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 1, 1)).setObjects(("CM-TOPOLOGY-MIB", "cmTopologyObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmTopologyCompliance = cmTopologyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmTopologyCompliance.setDescription('Describes the requirements for conformance to the CM Topology\n             group.')
cmTopologyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 9, 2, 2, 1)).setObjects(("CM-TOPOLOGY-MIB", "cmTopologyRegionId"), ("CM-TOPOLOGY-MIB", "cmTopologyRegionDescr"), ("CM-TOPOLOGY-MIB", "cmTopologyRegionLastUpdateTime"), ("CM-TOPOLOGY-MIB", "cmTopologyItemId"), ("CM-TOPOLOGY-MIB", "cmTopologyItemDescr"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkId"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkFromPort"), ("CM-TOPOLOGY-MIB", "cmTopologyLinkToPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmTopologyObjectGroup = cmTopologyObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cmTopologyObjectGroup.setDescription('A collection of objects used to manage the CM Topology\n             group.')
mibBuilder.exportSymbols("CM-TOPOLOGY-MIB", cmTopologyConformance=cmTopologyConformance, cmTopologyMIB=cmTopologyMIB, cmTopologyItemId=cmTopologyItemId, cmTopologyItemTable=cmTopologyItemTable, cmTopologyGroups=cmTopologyGroups, cmTopologyRegionId=cmTopologyRegionId, cmTopologyItemEntry=cmTopologyItemEntry, cmTopologyLinkEntry=cmTopologyLinkEntry, cmTopologyRegionLastUpdateTime=cmTopologyRegionLastUpdateTime, cmTopologyItemDescr=cmTopologyItemDescr, cmTopologyCompliance=cmTopologyCompliance, cmTopologyRegionDescr=cmTopologyRegionDescr, cmTopologyObjects=cmTopologyObjects, cmTopologyLinkId=cmTopologyLinkId, PYSNMP_MODULE_ID=cmTopologyMIB, cmTopologyLinkTable=cmTopologyLinkTable, cmTopologyLinkFromPort=cmTopologyLinkFromPort, cmTopologyLinkToPort=cmTopologyLinkToPort, cmTopologyObjectGroup=cmTopologyObjectGroup, cmTopologyCompliances=cmTopologyCompliances)
