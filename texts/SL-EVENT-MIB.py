#
# PySNMP MIB module SL-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-EVENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Counter64, iso, Integer32, NotificationType, Bits, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "iso", "Integer32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
slEventMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22))
if mibBuilder.loadTexts: slEventMib.setLastUpdated('200708280000Z')
if mibBuilder.loadTexts: slEventMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slEventMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slEventMib.setDescription('This MIB module describes the configuration change and inventory events.')
class SlGenEventType(TextualConvention, Integer32):
    description = 'The event types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("swUpgradeEvent", 1), ("remoteUnitFailEvent", 2), ("alsOperStatus", 3))

class SlEventType(TextualConvention, Integer32):
    description = 'The event types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("edDate", 1), ("rstProv", 2), ("edIp", 3), ("initPm", 4), ("dltIpRoute", 5), ("edSys", 6), ("setSid", 7), ("addUser", 8), ("dltUser", 9), ("rmvFac", 10), ("rstFac", 11), ("edFac", 12), ("oprLoopback", 13), ("rlsLoopback", 14), ("entAps", 15), ("dltAps", 16), ("oprProtSw", 17), ("rlsProtSw", 18), ("oprAco", 19), ("rstProvCommit", 20), ("savProvStart", 21), ("savProvComplete", 22), ("savProvFailed", 23), ("swLoadUpgrade", 24))

class SlEventInventoryAction(TextualConvention, Integer32):
    description = 'The event inventory types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inserted", 1), ("removed", 2))

class SlEventInventoryType(TextualConvention, Integer32):
    description = 'The event inventory types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("psu", 1), ("optics", 2), ("fan", 3))

slEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1))
slEventTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2))
slEventTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0))
slEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1), )
if mibBuilder.loadTexts: slEventConfigTable.setStatus('current')
if mibBuilder.loadTexts: slEventConfigTable.setDescription('This table contains objects to configure the event.')
slEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slEventIfIndex"), (0, "SL-EVENT-MIB", "slEventType"))
if mibBuilder.loadTexts: slEventConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slEventConfigEntry.setDescription('An entry exist for each type of event.\n             The entry describes the event properties.')
slEventIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventIfIndex.setStatus('current')
if mibBuilder.loadTexts: slEventIfIndex.setDescription('The corresponding interface index.')
slEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 2), SlEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventType.setStatus('current')
if mibBuilder.loadTexts: slEventType.setDescription('The event type.')
slEventVal = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventVal.setStatus('current')
if mibBuilder.loadTexts: slEventVal.setDescription('The changed value')
slEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventUser.setStatus('current')
if mibBuilder.loadTexts: slEventUser.setDescription('The user that made the change')
slEventCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventCtag.setStatus('current')
if mibBuilder.loadTexts: slEventCtag.setDescription('The TL1 Correlation Tag of the event message')
slEventTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventTid.setStatus('current')
if mibBuilder.loadTexts: slEventTid.setDescription('The TL1 Target Identfier of the node')
slEventInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2), )
if mibBuilder.loadTexts: slEventInventoryTable.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryTable.setDescription('This table contains objects to configure the event.')
slEventInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slEventInventoryIfIndex"), (0, "SL-EVENT-MIB", "slEventInventoryType"))
if mibBuilder.loadTexts: slEventInventoryEntry.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryEntry.setDescription('An entry describe an event of inventory change.')
slEventInventoryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryIfIndex.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryIfIndex.setDescription('The corresponding interface index.')
slEventInventoryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 2), SlEventInventoryAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryAction.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryAction.setDescription('The inventory action.')
slEventInventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 3), SlEventInventoryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryType.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryType.setDescription('The inventory type.')
slEventInventorySerial = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventInventorySerial.setStatus('current')
if mibBuilder.loadTexts: slEventInventorySerial.setDescription('The changed value')
slEventInventoryPartnum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventInventoryPartnum.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryPartnum.setDescription('The user that made the change')
slGenEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3), )
if mibBuilder.loadTexts: slGenEventConfigTable.setStatus('current')
if mibBuilder.loadTexts: slGenEventConfigTable.setDescription('This table contains objects to configure the event.')
slGenEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slGenEventIfIndex"), (0, "SL-EVENT-MIB", "slGenEventType"))
if mibBuilder.loadTexts: slGenEventConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slGenEventConfigEntry.setDescription('An entry exist for each type of event.\n             The entry describes the event properties.')
slGenEventIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slGenEventIfIndex.setStatus('current')
if mibBuilder.loadTexts: slGenEventIfIndex.setDescription('The corresponding interface index.')
slGenEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 2), SlGenEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slGenEventType.setStatus('current')
if mibBuilder.loadTexts: slGenEventType.setDescription('The event type.')
slGenEventVal = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventVal.setStatus('current')
if mibBuilder.loadTexts: slGenEventVal.setDescription('The changed value')
slGenEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventUser.setStatus('current')
if mibBuilder.loadTexts: slGenEventUser.setDescription('The user that made the change')
slGenEventCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventCtag.setStatus('current')
if mibBuilder.loadTexts: slGenEventCtag.setDescription('The TL1 Correlation Tag of the event message')
slGenEventTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventTid.setStatus('current')
if mibBuilder.loadTexts: slGenEventTid.setDescription('The TL1 Target Identfier of the node')
slEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 2)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
if mibBuilder.loadTexts: slEventTrap.setStatus('current')
if mibBuilder.loadTexts: slEventTrap.setDescription('An slEventTrap notification is sent when an configuration change occures.')
slEventTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 2)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
if mibBuilder.loadTexts: slEventTrap0.setStatus('current')
if mibBuilder.loadTexts: slEventTrap0.setDescription("An slEventTrap notification is sent when an configuration change occures.\n               It is defined to support browsers that don't recognize RFC 2576.")
slEventInventoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 3)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
if mibBuilder.loadTexts: slEventInventoryTrap.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryTrap.setDescription('An slInventoryEventTrap notification is sent when the node inventory is changed.')
slEventInventoryTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 3)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
if mibBuilder.loadTexts: slEventInventoryTrap0.setStatus('current')
if mibBuilder.loadTexts: slEventInventoryTrap0.setDescription("An slInventoryEventTrap notification is sent when the node inventory is changed.]\n               It is defined to support browsers that don't recognize RFC 2576.")
slGenEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 4)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
if mibBuilder.loadTexts: slGenEventTrap.setStatus('current')
if mibBuilder.loadTexts: slGenEventTrap.setDescription('An slEventTrap notification is sent when an configuration change occures.')
slGenEventTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 4)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
if mibBuilder.loadTexts: slGenEventTrap0.setStatus('current')
if mibBuilder.loadTexts: slGenEventTrap0.setDescription("An slEventTrap notification is sent when an configuration change occures.\n               It is defined to support browsers that don't recognize RFC 2576.")
mibBuilder.exportSymbols("SL-EVENT-MIB", SlEventInventoryAction=SlEventInventoryAction, slEventConfigEntry=slEventConfigEntry, slGenEventConfigTable=slGenEventConfigTable, slGenEventIfIndex=slGenEventIfIndex, slEventTraps=slEventTraps, slEventTid=slEventTid, slGenEventVal=slGenEventVal, slEventTrap0=slEventTrap0, slGenEventType=slGenEventType, slEventInventoryTrap0=slEventInventoryTrap0, slEventVal=slEventVal, slEventIfIndex=slEventIfIndex, slEventInventoryType=slEventInventoryType, slEventInventoryAction=slEventInventoryAction, slEventTraps0=slEventTraps0, slEventInventoryTable=slEventInventoryTable, SlEventType=SlEventType, SlEventInventoryType=SlEventInventoryType, slGenEventConfigEntry=slGenEventConfigEntry, slEventConfigTable=slEventConfigTable, slEventCtag=slEventCtag, slEventInventoryPartnum=slEventInventoryPartnum, slEventConfig=slEventConfig, slEventInventoryIfIndex=slEventInventoryIfIndex, slGenEventCtag=slGenEventCtag, slEventInventoryEntry=slEventInventoryEntry, slEventTrap=slEventTrap, slEventInventorySerial=slEventInventorySerial, SlGenEventType=SlGenEventType, slEventMib=slEventMib, slGenEventTrap0=slGenEventTrap0, PYSNMP_MODULE_ID=slEventMib, slEventUser=slEventUser, slEventType=slEventType, slGenEventTrap=slGenEventTrap, slEventInventoryTrap=slEventInventoryTrap, slGenEventUser=slGenEventUser, slGenEventTid=slGenEventTid)
