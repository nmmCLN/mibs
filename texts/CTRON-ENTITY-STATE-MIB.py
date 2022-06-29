#
# PySNMP MIB module CTRON-ENTITY-STATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENTITY-STATE-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
EntityStandbyStatus, EntityAlarmStatus, EntityUsageState, EntityOperState, EntityAdminState = mibBuilder.importSymbols("CTRON-ENTITY-STATE-TC-MIB", "EntityStandbyStatus", "EntityAlarmStatus", "EntityUsageState", "EntityOperState", "EntityAdminState")
ctEntityStateMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateMib")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Unsigned32, Gauge32, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, iso, Counter32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Unsigned32", "Gauge32", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity", "NotificationType")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
ctEntityStateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1))
ctEntityStateMIB.setRevisions(('2005-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctEntityStateMIB.setRevisionsDescriptions(('Initial version, published as RFC YYYY.',))
if mibBuilder.loadTexts: ctEntityStateMIB.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateMIB.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: ctEntityStateMIB.setContactInfo(' General Discussion: entmib@ietf.org\n                  To Subscribe:\n                    http://www.ietf.org/mailman/listinfo/entmib\n\n                  http://www.ietf.org/html.charters/entmib-charter.html\n\n                   Sharon Chisholm\n                   Nortel Networks\n                   PO Box 3511 Station C\n                   Ottawa, Ont.  K1Y 4H7\n                   Canada\n                   schishol@nortelnetworks.com\n\n                   David T. Perkins\n                   548 Qualbrook Ct\n                   San Jose, CA 95110\n                   USA\n                   Phone: 408 394-8702\n                   dperkins@snmpinfo.com\n                  ')
if mibBuilder.loadTexts: ctEntityStateMIB.setDescription('This MIB defines a state extension to the Entity MIB.\n\n                Copyright (C) The Internet Society 2005.  This version\n                of this MIB module is part of RFC yyyy;  see the RFC\n                itself for full legal notices.')
ctEntStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1))
ctEntStateTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1), )
if mibBuilder.loadTexts: ctEntStateTable.setStatus('current')
if mibBuilder.loadTexts: ctEntStateTable.setDescription('A table of information about state/status of entities.\n           This is a sparse augment of the entPhysicalTable. Entries\n           appear in this table for values of\n           entPhysicalClass [RFC2737] that in this implementation\n           are able to report any of the state or status stored in\n           this table.\n           ')
ctEntStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ctEntStateEntry.setStatus('current')
if mibBuilder.loadTexts: ctEntStateEntry.setDescription('State information about this physical entity.')
ctEntStateLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateLastChanged.setStatus('current')
if mibBuilder.loadTexts: ctEntStateLastChanged.setDescription('The value of this object is the date and\n         time when the value of any of ctEntStateAdmin,\n         ctEntStateOper, ctEntStateUsage, ctEntStateAlarm,\n         or ctEntStateStandby changed for this entity.\n\n        If there has been no change since\n        the last re-initialization of the local system,\n        this object contains the date and time of\n        local system initialization. If there has been\n        no change since the entity was added to the\n        local system, this object contains the date and\n        time of the insertion.')
ctEntStateAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 2), EntityAdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEntStateAdmin.setStatus('current')
if mibBuilder.loadTexts: ctEntStateAdmin.setDescription("The administrative state for this entity.\n\n                This object refers to an entities administrative\n                permission to service both other entities within\n                its containment hierarchy as well other users of\n                its services defined by means outside the scope\n                of this MIB.\n\n                Setting this object to 'notSupported' will result\n                in an 'inconsistentValue' error. For entities that\n                do not support administrative state, all set\n                operations will result in an 'inconsistentValue'\n                error.\n\n                Some physical entities exhibit only a subset of the\n                remaining administrative state values. Some entities\n                cannot be locked, and hence this object exhibits only\n                the 'unlocked' state. Other entities can not be shutdown\n                gracefully, and hence this object does not exhibit the\n                'shuttingDown' state. A value of 'inconsistentValue'\n                will be returned if attempts are made to set this\n                object to values not supported by its administrative\n                model.")
ctEntStateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 3), EntityOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateOper.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOper.setDescription("The operational state for this entity.\n\n               Note that unlike the state model used within the\n               Interfaces MIB [RFC2863], this object does not follow\n               the administrative state. An administrative state of\n               down does not predict an operational state\n               of disabled.\n\n               A value of 'testing' means that entity currently being\n               tested and cannot there fore report whether it is\n               operational or not.\n\n               A value of 'disabled' means that an entity is totally\n               inoperable and unable to provide service both to entities\n               within its containment hierarchy, or to other receivers\n               of its service as defined in ways outside the scope of\n               this MIB.\n\n               A value of 'enabled' means that an entity is fully or\n               partially operable and able to provide service both to\n               entities within its containment hierarchy, or to other\n               receivers of its service as defined in ways outside the\n               scope of this MIB.\n\n               Note that some implementations may not be able to\n               accurately report ctEntStateOper while the\n               ctEntStateAdmin object has a value other than 'unlocked'.\n               In these cases, this object MUST have a value\n               of 'unknown'.")
ctEntStateUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 4), EntityUsageState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateUsage.setStatus('current')
if mibBuilder.loadTexts: ctEntStateUsage.setDescription("The usage state for this entity.\n\n               This object refers to an entity's ability to service more\n               physical entities in a containment hierarchy. A value\n               of 'idle' means this entity is able to contain other\n               entities but that no other entity is currently\n               contained within this entity.\n\n               A value of 'active' means that at least one entity is\n               contained within this entity, but that it could handle\n               more. A value of 'busy' means that the entity is unable\n               to handle any additional entities being contained in it.\n\n               Some entities will exhibit only a subset of the\n               usage state values. Entities that are unable to ever\n               service any entities within a containment hierarchy will\n               always have a usage state of 'busy'. Some entities will\n               only ever be able to support one entity within its\n               containment hierarchy and will therefore only exhibit\n               values of 'idle' and 'busy'.")
ctEntStateAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 5), EntityAlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateAlarm.setStatus('current')
if mibBuilder.loadTexts: ctEntStateAlarm.setDescription("The alarm status for this entity. It does not include\n               the alarms raised on child components within its\n               containment hierarchy.\n\n               A value of 'unknown' means that this entity is\n               unable to report alarm state. Note that this differs\n               from 'indeterminate' which means that that alarm state\n               is supported and there are alarms against this entity,\n               but the severity of some of the alarms is not known\n\n               If no bits are set, then this entity supports reporting\n               of alarms, but there are currently no active alarms\n               against this entity.\n               ")
ctEntStateStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 1, 1, 1, 6), EntityStandbyStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctEntStateStandby.setStatus('current')
if mibBuilder.loadTexts: ctEntStateStandby.setDescription("The standby status for this entity.\n\n               Some entities will exhibit only a subset of the\n               remaining standby state values. If this entity\n               cannot operate in a standby role, the value of this\n               object will always be 'providingService'.")
ctEntStateNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0))
ctEntStateOperEnabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperEnabled.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOperEnabled.setDescription("An ctEntStateOperEnabled notification signifies that the\n               SNMP entity, acting in an agent role, has detected that\n               the ctEntStateOper object for one of its entities has\n               transitioned into the 'enabled' state.\n\n\n               The entity this notification refers can be identified by\n               extracting the entPhysicalIndex from one of the\n               variable bindings. The ctEntStateAdmin and ctEntStateAlarm\n               varbinds may be examined to find out additional\n               information on the administrative state at the time of\n               the operation state change as well to find out whether\n               there were any known alarms against the entity at that\n               time that may explain why the physical entity has become\n               operationally disabled.")
ctEntStateOperDisabled = NotificationType((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 0, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"))
if mibBuilder.loadTexts: ctEntStateOperDisabled.setStatus('current')
if mibBuilder.loadTexts: ctEntStateOperDisabled.setDescription("An ctEntStateOperDisabled notification signifies that the\n               SNMP entity, acting in an agent role, has detected that\n               the ctEntStateOper object for one of its entities has\n               transitioned into the 'disabled' state.\n\n               The entity this notification refers can be identified by\n               extracting the entPhysicalIndex from one of the\n               variable bindings. The ctEntStateAdmin and ctEntStateAlarm\n               varbinds may be examined to find out additional\n               information on the administrative state at the time of\n               the operation state change as well to find out whether\n               there were any known alarms against the entity at that\n               time that may have affect on the physical entity's\n               ability to stay operationally enabled.")
ctEntStateConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2))
ctEntStateCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1))
ctEntStateCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 1, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateGroup"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateCompliance = ctEntStateCompliance.setStatus('current')
if mibBuilder.loadTexts: ctEntStateCompliance.setDescription('The compliance statement for systems supporting\n             the Entity State MIB.')
ctEntStateGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2))
ctEntStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 1)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateLastChanged"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAdmin"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOper"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateUsage"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateAlarm"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateStandby"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateGroup = ctEntStateGroup.setStatus('current')
if mibBuilder.loadTexts: ctEntStateGroup.setDescription('Standard Entity State group.')
ctEntStateNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52, 4, 2, 31, 1, 2, 2, 2)).setObjects(("CTRON-ENTITY-STATE-MIB", "ctEntStateOperEnabled"), ("CTRON-ENTITY-STATE-MIB", "ctEntStateOperDisabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctEntStateNotificationsGroup = ctEntStateNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ctEntStateNotificationsGroup.setDescription('Standard Entity State Notification group.')
mibBuilder.exportSymbols("CTRON-ENTITY-STATE-MIB", ctEntStateGroups=ctEntStateGroups, ctEntStateUsage=ctEntStateUsage, ctEntityStateMIB=ctEntityStateMIB, ctEntStateEntry=ctEntStateEntry, ctEntStateGroup=ctEntStateGroup, ctEntStateStandby=ctEntStateStandby, ctEntStateLastChanged=ctEntStateLastChanged, ctEntStateAdmin=ctEntStateAdmin, ctEntStateTable=ctEntStateTable, PYSNMP_MODULE_ID=ctEntityStateMIB, ctEntStateOperEnabled=ctEntStateOperEnabled, ctEntStateObjects=ctEntStateObjects, ctEntStateOperDisabled=ctEntStateOperDisabled, ctEntStateConformance=ctEntStateConformance, ctEntStateCompliances=ctEntStateCompliances, ctEntStateAlarm=ctEntStateAlarm, ctEntStateCompliance=ctEntStateCompliance, ctEntStateNotificationsGroup=ctEntStateNotificationsGroup, ctEntStateNotifications=ctEntStateNotifications, ctEntStateOper=ctEntStateOper)
