#
# PySNMP MIB module HPOV-NNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HPOV-NNM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:56 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Counter32, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32, iso, TimeTicks, IpAddress, ModuleIdentity, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32", "iso", "TimeTicks", "IpAddress", "ModuleIdentity", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
hpOpenView = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 17, 1))
hpOpenView.setRevisions(('2005-09-28 00:00', '1996-07-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpOpenView.setRevisionsDescriptions(('Added definition of trap 58916872', 'Initial revision published as part of hp-unix MIB.\n\t     Updated to add support for SNMPv2 Security Proxy.\n\t     Updated to use the SNMPv2 SMI.',))
if mibBuilder.loadTexts: hpOpenView.setLastUpdated('200509280000Z')
if mibBuilder.loadTexts: hpOpenView.setOrganization('Hewlett-Packard, Network & System Management Division')
if mibBuilder.loadTexts: hpOpenView.setContactInfo('Support: Hewlett-Packard Response Center\n                 Tel: +1 (800) 633-3600')
if mibBuilder.loadTexts: hpOpenView.setDescription('General management information used within the \n             HP OpenView Network Node Manager product.\n\t     \n\t     This object identifier also serves as the \n\t     OpenView Enterprise ID for SNMPv1 Traps.')
class OVTextString(TextualConvention, OctetString):
    description = 'Represents textual information consisting of either \n            single- or multi-byte characters.  \n\n            The character string is interpreted using the locale \n            (language) of the interpreting entity because the locale \n            is NOT included.  Therefore, transmitting an object value \n            of this syntax across different locales is not supported.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

openViewTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 2))
openViewSourceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceId.setStatus('current')
if mibBuilder.loadTexts: openViewSourceId.setDescription('The identifier of the software generating the trap/event.\n\t\t This number is used by HP OpenView software when it sends\n\t\t an event to the OpenView event system.  It identifies\n\t\t which software component sent the event.')
openViewSourceName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 2), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceName.setStatus('current')
if mibBuilder.loadTexts: openViewSourceName.setDescription('The source of the event (may not be the machine upon\n\t\t which the event was generated).  This string is used\n\t\t by HP OpenView software when it sends an event.  It\n\t\t identifies for which node the event is generated.')
openViewObjectId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewObjectId.setStatus('current')
if mibBuilder.loadTexts: openViewObjectId.setDescription('The OpenView Windows object identifier associated \n                 with the source of the trap/event.')
openViewData = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewData.setStatus('current')
if mibBuilder.loadTexts: openViewData.setDescription('Any miscellaneous data sent with an OpenView trap/event.')
openViewSeverity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 5), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSeverity.setStatus('current')
if mibBuilder.loadTexts: openViewSeverity.setDescription('The OpenView event severity associated with the trap/event.')
openViewCategory = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 6), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCategory.setStatus('current')
if mibBuilder.loadTexts: openViewCategory.setDescription('The OpenView event category associated with the trap/event.')
openViewFilter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewFilter.setStatus('current')
if mibBuilder.loadTexts: openViewFilter.setDescription('The event filter for an application connecting to the\n\t\t OpenView event system.')
openViewEntity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 8), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEntity.setStatus('current')
if mibBuilder.loadTexts: openViewEntity.setDescription('The entity (string name) of an application connecting\n\t\t to the OpenView event system.')
openViewAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewAddress.setStatus('current')
if mibBuilder.loadTexts: openViewAddress.setDescription('The IP address of the node from where an application\n\t\t is connecting to the OpenView event system.')
openViewPid = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewPid.setStatus('current')
if mibBuilder.loadTexts: openViewPid.setDescription('The process ID of an application connecting to the\n\t\t OpenView event system.')
openViewCmipManagedObjectClass = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectClass.setStatus('current')
if mibBuilder.loadTexts: openViewCmipManagedObjectClass.setDescription('A cmisEventReport managedObjectClass.  Only valid when\n\t\t running with the HP OpenView DM product.')
openViewCmipEventTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 12), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventTime.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventTime.setDescription('A cmisEventReport eventTime.  Only valid when\n\t\t running with the HP OpenView DM product.')
openViewCmipEventType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventType.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventType.setDescription('A cmisEventReport eventType.  Only valid when\n\t\t running with the HP OpenView DM product.')
openViewCmipEventInfo = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventInfo.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventInfo.setDescription('A cmisEventReport eventInfo.  Only valid when\n\t\t running with the HP OpenView DM product.')
openViewCmipManagedObjectInstanceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 15), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectInstanceId.setStatus('current')
if mibBuilder.loadTexts: openViewCmipManagedObjectInstanceId.setDescription('A cmisEventReport managedObjectInstance.  Only valid when\n\t\t running with the HP OpenView DM product.')
openViewEventUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEventUUID.setStatus('current')
if mibBuilder.loadTexts: openViewEventUUID.setDescription('An OpenView Event UUID which uniquely identifies an event.')
openViewEcsCorrelateEvUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 17), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsCorrelateEvUUID.setStatus('current')
if mibBuilder.loadTexts: openViewEcsCorrelateEvUUID.setDescription('If an OpenView event contains this var-bind, it indicates to\n\t\tthe Event Correlation System that the event should be correlated\n\t\twith the event whose UUID is the value of this var-bind.  If the\n\t\tvar-bind is missing or has a zero length value, then no event\n\t\tcorrelation occurs.')
openViewEcsNodeImportance = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 18), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsNodeImportance.setStatus('current')
if mibBuilder.loadTexts: openViewEcsNodeImportance.setDescription('If an OpenView event contains this var-bind, it indicates to\n\t\tthe Event Correlation System the importance of the node from\n\t\tan event correlation perspective.  In situations where the\n\t\tECS system would normally suppress an event, it may choose not\n\t\tto suppress it if the node is very important (e.g. an important\n\t\tserver node).  The integral value of this MIB object may evolve\n\t\tover time.  For now, non-integral values are invalid, a value of\n\t\tzero indicates that the node is a regular node and a non-zero \n\t\tvalue indicates that the node is an important node.')
hpOVNNMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 1, 0))
hpOVMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 17, 1, 0, 58916872)).setObjects(("HPOV-NNM-MIB", "openViewSourceId"), ("HPOV-NNM-MIB", "openViewSourceName"), ("HPOV-NNM-MIB", "openViewData"), ("HPOV-NNM-MIB", "openViewSeverity"))
if mibBuilder.loadTexts: hpOVMessageTrap.setStatus('current')
if mibBuilder.loadTexts: hpOVMessageTrap.setDescription('This special event can be generated by a user to\n                   display an event message in the event browser.\n                   It assumes the message is in the third variable.\n\n                   To send a message with a popup notification, use the\n                   OV_Popup_Message event.\n\n                   On UNIX, see the trapd.conf(4) manpage for a discussion on\n                   how to set up the parameters to send this event, and a\n                   description of the parameters.  On Windows, see the\n                   trapd.conf reference page in the help file.\n\n                   The data passed with the event is\n                      openViewSourceId: The ID of application sending the event \n                      openViewSourceName: The source of the event, if available\n                      openViewData: The string to display\n                      openViewSeverity: The severity of the event\n\n                   On UNIX, see the trapd.conf(4) manpage for complete details.\n                   On Windows, see the trapd.conf reference page in the help\n                   file.')
mibBuilder.exportSymbols("HPOV-NNM-MIB", openViewCmipManagedObjectClass=openViewCmipManagedObjectClass, openViewPid=openViewPid, nm=nm, openViewEventUUID=openViewEventUUID, hpOVMessageTrap=hpOVMessageTrap, openViewTrapVars=openViewTrapVars, openViewCmipEventInfo=openViewCmipEventInfo, hp=hp, openViewCmipEventTime=openViewCmipEventTime, openViewCategory=openViewCategory, openViewFilter=openViewFilter, openViewEcsNodeImportance=openViewEcsNodeImportance, OVTextString=OVTextString, openViewAddress=openViewAddress, hpOpenView=hpOpenView, openViewSourceId=openViewSourceId, openViewEntity=openViewEntity, openViewCmipEventType=openViewCmipEventType, openViewSourceName=openViewSourceName, PYSNMP_MODULE_ID=hpOpenView, openViewEcsCorrelateEvUUID=openViewEcsCorrelateEvUUID, openViewData=openViewData, openViewCmipManagedObjectInstanceId=openViewCmipManagedObjectInstanceId, hpOVNNMTraps=hpOVNNMTraps, openViewSeverity=openViewSeverity, openViewObjectId=openViewObjectId, openView=openView)
