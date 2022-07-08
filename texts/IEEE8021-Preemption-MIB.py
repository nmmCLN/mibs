#
# PySNMP MIB module IEEE8021-Preemption-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-Preemption-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:11:37 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ieee8021BridgeBasePort, ieee8021BridgeBaseComponentId = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBaseComponentId")
ieee802dot1mibs, IEEE8021PriorityValue = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs", "IEEE8021PriorityValue")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, MibIdentifier, TimeTicks, iso, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ieee8021PreemptionMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 29))
ieee8021PreemptionMib.setRevisions(('2018-06-21 00:00', '2016-08-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021PreemptionMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2017 revision.\n            Cross references updated and corrected.', 'Initial version published as part of IEEE Std 802.1Qbu.',))
if mibBuilder.loadTexts: ieee8021PreemptionMib.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: ieee8021PreemptionMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021PreemptionMib.setContactInfo('  WG-URL: http://www.ieee802.org/1/\n         WG-EMail: STDS-802-1-L@ieee.org\n\n          Contact: IEEE 802.1 Working Group Chair\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   Piscataway\n                   NJ 08854\n                   USA\n           E-mail: STDS-802-1-L@ieee.org')
if mibBuilder.loadTexts: ieee8021PreemptionMib.setDescription('The Bridge MIB module for managing devices that support\n        the frame preemption enhancements\n        for IEEE 802.1Q Bridges.\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1Q.\n\n        Copyright (C) IEEE (2018).\n        This version of this MIB module is part of IEEE Std 802.1Q;\n        see the draft itself for full legal notices.')
ieee8021PreemptionNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 0))
ieee8021PreemptionObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 1))
ieee8021PreemptionConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2))
ieee8021PreemptionParameters = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 1, 1))
ieee8021PreemptionParameterTable = MibTable((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021PreemptionParameterTable.setReference('6.7.2, 12.30.1')
if mibBuilder.loadTexts: ieee8021PreemptionParameterTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionParameterTable.setDescription('A table containing a set of frame preemption \n        parameters, one for each priority value.\n        All writeable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021PreemptionParameterEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-Preemption-MIB", "ieee8021PreemptionPriority"))
if mibBuilder.loadTexts: ieee8021PreemptionParameterEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionParameterEntry.setDescription('A list of objects containing preemption parameters \n        for each  priority value.')
ieee8021PreemptionPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 1), IEEE8021PriorityValue())
if mibBuilder.loadTexts: ieee8021PreemptionPriority.setReference('6.7.2, 12.30.1')
if mibBuilder.loadTexts: ieee8021PreemptionPriority.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionPriority.setDescription('The priority number associated with the row of\n        the table.\n\n        A row in this table is created for each priority value.')
ieee8021FramePreemptionAdminStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("express", 1), ("preemptible", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021FramePreemptionAdminStatus.setReference('6.7.2, 12.30.1')
if mibBuilder.loadTexts: ieee8021FramePreemptionAdminStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021FramePreemptionAdminStatus.setDescription('The value of the framePreemptionAdminStatus parameter\n        for the traffic class.\n\n        The default value of the framePreemptionAdminStatus parameter \n        is express (1).\n\n        The value of this object MUST be retained across\n        reinitializations of the management system.')
ieee8021PreemptionConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2), )
if mibBuilder.loadTexts: ieee8021PreemptionConfigTable.setReference('6.7.2, 12.30.1')
if mibBuilder.loadTexts: ieee8021PreemptionConfigTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionConfigTable.setDescription('A table containing a set of frame preemption \n        parameters, one for each Port.\n        All writeable objects in this table must be\n        persistent over power up restart/reboot.')
ieee8021PreemptionConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PreemptionConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionConfigEntry.setDescription('A list of objects containing preemption parameters \n        for each Port.')
ieee8021FramePreemptionHoldAdvance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldAdvance.setReference('6.7.2, 12.30.1.2')
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldAdvance.setStatus('current')
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldAdvance.setDescription('The value of the holdAdvance parameter\n        for the Port in nanoseconds.\n\n        There is no default value; the holdAdvance is \n        a property of the underlying MAC.')
ieee8021FramePreemptionReleaseAdvance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionReleaseAdvance.setReference('6.7.2, 12.30.1.3')
if mibBuilder.loadTexts: ieee8021FramePreemptionReleaseAdvance.setStatus('current')
if mibBuilder.loadTexts: ieee8021FramePreemptionReleaseAdvance.setDescription('The value of the releaseAdvance parameter\n        for the Port in nanoseconds.\n\n        There is no default value; the releaseAdvance is \n        a property of the underlying MAC.')
ieee8021FramePreemptionActive = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionActive.setReference('6.7.2, 12.30.1.4')
if mibBuilder.loadTexts: ieee8021FramePreemptionActive.setStatus('current')
if mibBuilder.loadTexts: ieee8021FramePreemptionActive.setDescription('The value is active (2) when preemption is operationally\n        active for the Port, and idle (1) otherwise.')
ieee8021FramePreemptionHoldRequest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hold", 1), ("release", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldRequest.setReference('6.7.2, Table 8-7, 12.30.1.5')
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldRequest.setStatus('current')
if mibBuilder.loadTexts: ieee8021FramePreemptionHoldRequest.setDescription('The value is hold (1) when the sequence of gate operations\n        for the Port has executed a Set-And-Hold-MAC operation,\n        and release (2) when the sequence of gate operations has \n        executed a Set-And-Release-MAC operation. The \n        value of this object is release (2) on system\n        initialization.')
ieee8021PreemptionCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2, 1))
ieee8021PreemptionGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 29, 2, 2))
ieee8021PreemptionGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 29, 2, 2, 1)).setObjects(("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionAdminStatus"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldAdvance"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionReleaseAdvance"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionActive"), ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PreemptionGroup = ieee8021PreemptionGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionGroup.setDescription('Objects that allow management of frame preemption.')
ieee8021PreemptionCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 29, 2, 1, 1)).setObjects(("IEEE8021-Preemption-MIB", "ieee8021PreemptionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PreemptionCompliance = ieee8021PreemptionCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021PreemptionCompliance.setDescription('The compliance statement for devices supporting \n        frame preemption. \n\n        Support of the objects defined in this MIB module\n        also requires support of the IEEE8021-BRIDGE-MIB; the\n        provisions of 17.3.2 apply to implementations claiming\n        support of this MIB. ')
mibBuilder.exportSymbols("IEEE8021-Preemption-MIB", ieee8021PreemptionMib=ieee8021PreemptionMib, ieee8021PreemptionParameters=ieee8021PreemptionParameters, ieee8021FramePreemptionAdminStatus=ieee8021FramePreemptionAdminStatus, ieee8021FramePreemptionActive=ieee8021FramePreemptionActive, ieee8021FramePreemptionReleaseAdvance=ieee8021FramePreemptionReleaseAdvance, ieee8021PreemptionConfigEntry=ieee8021PreemptionConfigEntry, ieee8021PreemptionConformance=ieee8021PreemptionConformance, ieee8021PreemptionCompliances=ieee8021PreemptionCompliances, ieee8021PreemptionCompliance=ieee8021PreemptionCompliance, ieee8021PreemptionNotifications=ieee8021PreemptionNotifications, ieee8021PreemptionConfigTable=ieee8021PreemptionConfigTable, ieee8021PreemptionPriority=ieee8021PreemptionPriority, PYSNMP_MODULE_ID=ieee8021PreemptionMib, ieee8021PreemptionObjects=ieee8021PreemptionObjects, ieee8021PreemptionParameterTable=ieee8021PreemptionParameterTable, ieee8021FramePreemptionHoldRequest=ieee8021FramePreemptionHoldRequest, ieee8021PreemptionParameterEntry=ieee8021PreemptionParameterEntry, ieee8021PreemptionGroup=ieee8021PreemptionGroup, ieee8021FramePreemptionHoldAdvance=ieee8021FramePreemptionHoldAdvance, ieee8021PreemptionGroups=ieee8021PreemptionGroups)
