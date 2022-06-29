#
# PySNMP MIB module ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ENTITY-STATE-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:21 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EntityUsageState, EntityStandbyStatus, EntityOperState, EntityAdminState, EntityAlarmStatus = mibBuilder.importSymbols("ENTITY-STATE-TC-MIB", "EntityUsageState", "EntityStandbyStatus", "EntityOperState", "EntityAdminState", "EntityAlarmStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, NotificationType, iso, IpAddress, MibIdentifier, Counter32, TimeTicks, Bits, mib_2, Unsigned32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "NotificationType", "iso", "IpAddress", "MibIdentifier", "Counter32", "TimeTicks", "Bits", "mib-2", "Unsigned32", "Integer32", "Counter64")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
entityStateMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 131))
entityStateMIB.setRevisions(('2005-11-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: entityStateMIB.setRevisionsDescriptions(('Initial version, published as RFC 4268.',))
if mibBuilder.loadTexts: entityStateMIB.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: entityStateMIB.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: entityStateMIB.setContactInfo(' General Discussion: entmib@ietf.org\n                To Subscribe:\n                http://www.ietf.org/mailman/listinfo/entmib\n\n                http://www.ietf.org/html.charters/entmib-charter.html\n\n                Sharon Chisholm\n                Nortel Networks\n                PO Box 3511 Station C\n                Ottawa, Ont.  K1Y 4H7\n                Canada\n                schishol@nortel.com\n\n                David T. Perkins\n                548 Qualbrook Ct\n                San Jose, CA 95110\n                USA\n                Phone: 408 394-8702\n                dperkins@snmpinfo.com\n               ')
if mibBuilder.loadTexts: entityStateMIB.setDescription('This MIB defines a state extension to the Entity MIB.\n\n           Copyright (C) The Internet Society 2005.  This version\n           of this MIB module is part of RFC 4268; see the RFC\n           itself for full legal notices.')
entStateObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 1))
entStateTable = MibTable((1, 3, 6, 1, 2, 1, 131, 1, 1), )
if mibBuilder.loadTexts: entStateTable.setStatus('current')
if mibBuilder.loadTexts: entStateTable.setDescription('A table of information about state/status of entities.\n        This is a sparse augment of the entPhysicalTable.  Entries\n        appear in this table for values of\n        entPhysicalClass [RFC4133] that in this implementation\n        are able to report any of the state or status stored in\n        this table.\n\n\n\n        ')
entStateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 131, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entStateEntry.setStatus('current')
if mibBuilder.loadTexts: entStateEntry.setDescription('State information about this physical entity.')
entStateLastChanged = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateLastChanged.setStatus('current')
if mibBuilder.loadTexts: entStateLastChanged.setDescription('The value of this object is the date and\n      time when the value of any of entStateAdmin,\n      entStateOper, entStateUsage, entStateAlarm,\n      or entStateStandby changed for this entity.\n\n      If there has been no change since\n      the last re-initialization of the local system,\n      this object contains the date and time of\n      local system initialization.  If there has been\n      no change since the entity was added to the\n      local system, this object contains the date and\n      time of the insertion.')
entStateAdmin = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entStateAdmin.setStatus('current')
if mibBuilder.loadTexts: entStateAdmin.setDescription("The administrative state for this entity.\n\n\n\n\n             This object refers to an entities administrative\n             permission to service both other entities within\n             its containment hierarchy as well other users of\n             its services defined by means outside the scope\n             of this MIB.\n\n             Setting this object to 'notSupported' will result\n             in an 'inconsistentValue' error.  For entities that\n             do not support administrative state, all set\n             operations will result in an 'inconsistentValue'\n             error.\n\n             Some physical entities exhibit only a subset of the\n             remaining administrative state values.  Some entities\n             cannot be locked, and hence this object exhibits only\n             the 'unlocked' state.  Other entities cannot be shutdown\n             gracefully, and hence this object does not exhibit the\n             'shuttingDown' state.  A value of 'inconsistentValue'\n             will be returned if attempts are made to set this\n             object to values not supported by its administrative\n             model.")
entStateOper = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateOper.setStatus('current')
if mibBuilder.loadTexts: entStateOper.setDescription("The operational state for this entity.\n\n            Note that unlike the state model used within the\n            Interfaces MIB [RFC2863], this object does not follow\n            the administrative state.  An administrative state of\n            down does not predict an operational state\n            of disabled.\n\n            A value of 'testing' means that entity currently being\n            tested and cannot therefore report whether it is\n            operational or not.\n\n            A value of 'disabled' means that an entity is totally\n            inoperable and unable to provide service both to entities\n            within its containment hierarchy, or to other receivers\n            of its service as defined in ways outside the scope of\n            this MIB.\n\n            A value of 'enabled' means that an entity is fully or\n            partially operable and able to provide service both to\n\n\n\n            entities within its containment hierarchy, or to other\n            receivers of its service as defined in ways outside the\n            scope of this MIB.\n\n            Note that some implementations may not be able to\n            accurately report entStateOper while the\n            entStateAdmin object has a value other than 'unlocked'.\n            In these cases, this object MUST have a value\n            of 'unknown'.")
entStateUsage = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateUsage.setStatus('current')
if mibBuilder.loadTexts: entStateUsage.setDescription("The usage state for this entity.\n\n            This object refers to an entity's ability to service more\n            physical entities in a containment hierarchy.  A value\n            of 'idle' means this entity is able to contain other\n            entities but that no other entity is currently\n            contained within this entity.\n\n            A value of 'active' means that at least one entity is\n            contained within this entity, but that it could handle\n            more.  A value of 'busy' means that the entity is unable\n            to handle any additional entities being contained in it.\n\n            Some entities will exhibit only a subset of the\n            usage state values.  Entities that are unable to ever\n            service any entities within a containment hierarchy will\n            always have a usage state of 'busy'.  Some entities will\n            only ever be able to support one entity within its\n            containment hierarchy and will therefore only exhibit\n            values of 'idle' and 'busy'.")
entStateAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateAlarm.setStatus('current')
if mibBuilder.loadTexts: entStateAlarm.setDescription("The alarm status for this entity.  It does not include\n            the alarms raised on child components within its\n            containment hierarchy.\n\n            A value of 'unknown' means that this entity is\n\n\n\n            unable to report alarm state.  Note that this differs\n            from 'indeterminate', which means that alarm state\n            is supported and there are alarms against this entity,\n            but the severity of some of the alarms is not known.\n\n            If no bits are set, then this entity supports reporting\n            of alarms, but there are currently no active alarms\n            against this entity.")
entStateStandby = MibTableColumn((1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entStateStandby.setStatus('current')
if mibBuilder.loadTexts: entStateStandby.setDescription("The standby status for this entity.\n\n            Some entities will exhibit only a subset of the\n            remaining standby state values.  If this entity\n            cannot operate in a standby role, the value of this\n            object will always be 'providingService'.")
entStateNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 0))
entStateOperEnabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 1)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperEnabled.setStatus('current')
if mibBuilder.loadTexts: entStateOperEnabled.setDescription("An entStateOperEnabled notification signifies that the\n            SNMP entity, acting in an agent role, has detected that\n            the entStateOper object for one of its entities has\n            transitioned into the 'enabled' state.\n\n            The entity this notification refers can be identified by\n            extracting the entPhysicalIndex from one of the\n            variable bindings.  The entStateAdmin and entStateAlarm\n            varbinds may be examined to find out additional\n            information on the administrative state at the time of\n            the operation state change as well as to find out whether\n            there were any known alarms against the entity at that\n            time that may explain why the physical entity has become\n            operationally disabled.")
entStateOperDisabled = NotificationType((1, 3, 6, 1, 2, 1, 131, 0, 2)).setObjects(("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateAlarm"))
if mibBuilder.loadTexts: entStateOperDisabled.setStatus('current')
if mibBuilder.loadTexts: entStateOperDisabled.setDescription("An entStateOperDisabled notification signifies that the\n            SNMP entity, acting in an agent role, has detected that\n            the entStateOper object for one of its entities has\n            transitioned into the 'disabled' state.\n\n            The entity this notification refers can be identified by\n            extracting the entPhysicalIndex from one of the\n            variable bindings.  The entStateAdmin and entStateAlarm\n            varbinds may be examined to find out additional\n            information on the administrative state at the time of\n            the operation state change as well as to find out whether\n            there were any known alarms against the entity at that\n            time that may affect the physical entity's\n            ability to stay operationally enabled.")
entStateConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2))
entStateCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 1))
entStateCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 131, 2, 1, 1)).setObjects(("ENTITY-STATE-MIB", "entStateGroup"), ("ENTITY-STATE-MIB", "entStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateCompliance = entStateCompliance.setStatus('current')
if mibBuilder.loadTexts: entStateCompliance.setDescription('The compliance statement for systems supporting\n          the Entity State MIB.')
entStateGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 131, 2, 2))
entStateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 1)).setObjects(("ENTITY-STATE-MIB", "entStateLastChanged"), ("ENTITY-STATE-MIB", "entStateAdmin"), ("ENTITY-STATE-MIB", "entStateOper"), ("ENTITY-STATE-MIB", "entStateUsage"), ("ENTITY-STATE-MIB", "entStateAlarm"), ("ENTITY-STATE-MIB", "entStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateGroup = entStateGroup.setStatus('current')
if mibBuilder.loadTexts: entStateGroup.setDescription('Standard Entity State group.')
entStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 131, 2, 2, 2)).setObjects(("ENTITY-STATE-MIB", "entStateOperEnabled"), ("ENTITY-STATE-MIB", "entStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entStateNotificationsGroup = entStateNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: entStateNotificationsGroup.setDescription('Standard Entity State Notification group.')
mibBuilder.exportSymbols("ENTITY-STATE-MIB", entStateAdmin=entStateAdmin, entStateNotificationsGroup=entStateNotificationsGroup, entityStateMIB=entityStateMIB, entStateGroups=entStateGroups, entStateConformance=entStateConformance, entStateOperDisabled=entStateOperDisabled, entStateUsage=entStateUsage, entStateLastChanged=entStateLastChanged, entStateCompliances=entStateCompliances, entStateAlarm=entStateAlarm, entStateTable=entStateTable, entStateGroup=entStateGroup, entStateObjects=entStateObjects, PYSNMP_MODULE_ID=entityStateMIB, entStateCompliance=entStateCompliance, entStateStandby=entStateStandby, entStateOper=entStateOper, entStateOperEnabled=entStateOperEnabled, entStateEntry=entStateEntry, entStateNotifications=entStateNotifications)
