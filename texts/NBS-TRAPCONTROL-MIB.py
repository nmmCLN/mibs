#
# PySNMP MIB module NBS-TRAPCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-TRAPCONTROL-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:24:43 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Unsigned32, Bits, ModuleIdentity, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "iso", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsTrapControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 209))
if mibBuilder.loadTexts: nbsTrapControlMib.setLastUpdated('201209260000Z')
if mibBuilder.loadTexts: nbsTrapControlMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsTrapControlMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsTrapControlMib.setDescription('MIB to specify which SNMP Notifications (Traps) are supported,\n       and for which interfaces (ports) each should be sent.')
nbsTrapListGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 1))
if mibBuilder.loadTexts: nbsTrapListGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListGrp.setDescription('List of SNMP Notifications (Traps) emitted by Agent')
nbsTrapIfGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 209, 2))
if mibBuilder.loadTexts: nbsTrapIfGrp.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfGrp.setDescription('List of interfaces managed by Agent')
nbsTrapListTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTableSize.setDescription('The number of entries in nbsTrapListTable.')
nbsTrapListTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 1, 2), )
if mibBuilder.loadTexts: nbsTrapListTable.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTable.setDescription('A table to list SNMP Notifications emitted by Agent')
nbsTrapListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapListIndex"))
if mibBuilder.loadTexts: nbsTrapListEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListEntry.setDescription('Describes a particular SNMP Notification/Trap.')
nbsTrapListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: nbsTrapListIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListIndex.setDescription('Agent-generated unique ID.  Numbering is contiguous\n           and starts from 1.')
nbsTrapListTrapMib = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapMib.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapMib.setDescription('The name of the mib where this SNMP Notification is\n           defined.  An example would be IF-MIB.')
nbsTrapListTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapName.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapName.setDescription('Trap Name; the name given in the NOTIFICATION-TYPE\n           definition. An example would be linkUp')
nbsTrapListTrapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapDescription.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapDescription.setDescription("Brief explanation of this SNMP Notification.  Agent\n           may use the first 100 characters of the DESCRIPTION\n           clause from the Notification's MIB definition.")
nbsTrapListTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapListTrapOID.setStatus('current')
if mibBuilder.loadTexts: nbsTrapListTrapOID.setDescription('Concatenation of the enterprise and the specific-trap number\n           used in the SNMPv1 trap PDU')
nbsTrapIfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 209, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTableSize.setDescription('The number of entries in nbsTrapIfTable.')
nbsTrapIfTable = MibTable((1, 3, 6, 1, 4, 1, 629, 209, 2, 2), )
if mibBuilder.loadTexts: nbsTrapIfTable.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTable.setDescription('A list of all interfaces managed by Agent, and which traps\n           to send for each.')
nbsTrapIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1), ).setIndexNames((0, "NBS-TRAPCONTROL-MIB", "nbsTrapIfIndex"))
if mibBuilder.loadTexts: nbsTrapIfEntry.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfEntry.setDescription('Indicates traps for a particular interface.')
nbsTrapIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsTrapIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfIndex.setDescription('The ifIndex from the Mib2 ifTable.')
nbsTrapIfTrapsCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsTrapIfTrapsCaps.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTrapsCaps.setDescription('Bitmask indicating which SNMP Notifications are supported\n           for this interface.\n\n           Bit 0 is reserved.\n\n           Subsequent bits refer to the nbsTrapListTable.  Bit 1\n           corresponds to the first table entry, Bit 2 to the second\n           entry, and so on.\n\n           A bit is set (1) if that SNMP Notification can be sent for\n           this interface, and cleared (0) if unavailable.\n\n           OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
nbsTrapIfTrapsSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 209, 2, 2, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsTrapIfTrapsSelect.setStatus('current')
if mibBuilder.loadTexts: nbsTrapIfTrapsSelect.setDescription('Bitmask administrating which SNMP Notifications should be\n           sent for this interface.\n\n           Bit 0 is reserved.\n\n           Subsequent bits refer to the nbsTrapListTable.  Bit 1\n           corresponds to the first table entry, Bit 2 to the second\n           entry, and so on.\n\n           A bit is set (1) if that SNMP Notification should be\n           emitted for this interface, and cleared (0) if it should be\n           suppressed.\n\n           OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
mibBuilder.exportSymbols("NBS-TRAPCONTROL-MIB", nbsTrapListTrapMib=nbsTrapListTrapMib, nbsTrapListTrapDescription=nbsTrapListTrapDescription, nbsTrapListTable=nbsTrapListTable, nbsTrapIfEntry=nbsTrapIfEntry, nbsTrapIfIndex=nbsTrapIfIndex, nbsTrapIfGrp=nbsTrapIfGrp, nbsTrapControlMib=nbsTrapControlMib, nbsTrapListIndex=nbsTrapListIndex, nbsTrapListEntry=nbsTrapListEntry, nbsTrapListTrapOID=nbsTrapListTrapOID, nbsTrapIfTableSize=nbsTrapIfTableSize, nbsTrapIfTrapsCaps=nbsTrapIfTrapsCaps, nbsTrapIfTrapsSelect=nbsTrapIfTrapsSelect, PYSNMP_MODULE_ID=nbsTrapControlMib, nbsTrapIfTable=nbsTrapIfTable, nbsTrapListTableSize=nbsTrapListTableSize, nbsTrapListGrp=nbsTrapListGrp, nbsTrapListTrapName=nbsTrapListTrapName)
