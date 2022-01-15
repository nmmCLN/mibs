#
# PySNMP MIB module CTRON-CSMACD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-CSMACD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctCSMACD, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctCSMACD")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFnbCSMACD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1))
ctFnbPortConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2))
ctFnbCSMACDTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1), )
if mibBuilder.loadTexts: ctFnbCSMACDTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDTable.setDescription('A list of entries that provide connection status of\n                    CSMA/CD subsystems, for the FNB.')
ctFnbCSMACDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1), ).setIndexNames((0, "CTRON-CSMACD-MIB", "ctFnbCSMACDIndex"))
if mibBuilder.loadTexts: ctFnbCSMACDEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDEntry.setDescription('An entry in the ctFnbCSMACDTable containing objects\n                    that provide FNB connection status for a CSMA/CD\n                    subsystem.')
ctFnbCSMACDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbCSMACDIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDIndex.setDescription("An unique value for each CSMACD subsystem.  Its\n                    value ranges between 1 and chassisSlots.  The value\n                    for each interface must remain constant, at least,\n                    from one re-initialization of the entity's network\n                    management system to the next re-initialization.")
ctFnbConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("connectB", 1), ("connectC", 2), ("disconnect", 3), ("connectA", 4), ("subnetB", 5), ("subnetC", 6), ("multiChannel", 7), ("frontpanel", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbConnect.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbConnect.setDescription('Denotes the connection status of the CSMA/CD board\n                    to the inter-RIC bus.  The values of 1, 2, and 4 define\n                    connection status of connect for the subsystem, values 5\n                    and 6 define connection status of subnet connect for\n                    the subsystem, value 8 is defined as a front panel\n                    connection on the module, and a value of 3 defines\n                    disconnect status.')
ctFnbPortChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortChanges.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortChanges.setDescription("Denotes the number of times any port on the\n                        given MIM has changed it's connection to the\n                        inter-RIC bus.")
ctFnbPortConnectTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1), )
if mibBuilder.loadTexts: ctFnbPortConnectTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectTable.setDescription('This table is used to control port\n                        association on ethernet devices.  Only\n                        those boards that support port switching\n                        will be listed in this table.')
ctFnbPortConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-CSMACD-MIB", "ctFnbPortConnectBoardIndex"), (0, "CTRON-CSMACD-MIB", "ctFnbPortConnectPortIndex"))
if mibBuilder.loadTexts: ctFnbPortConnectEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectEntry.setDescription('Describes a specific port connection entry.')
ctFnbPortConnectBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectBoardIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectBoardIndex.setDescription('An instance of a board for which this port\n                        assignment relationship exists.')
ctFnbPortConnectPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectPortIndex.setDescription('An instance of a port for which this\n                        assignment relationship exists.')
ctFnbPortConnectPortAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connectA", 1), ("connectB", 2), ("connectC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbPortConnectPortAssignment.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectPortAssignment.setDescription('The specific channel that the port is\n                        assigned.')
ctFnbPortCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortCompID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortCompID.setDescription('This is the component ID as defined in the chassis\n                        MIB that this port is associated with.  These\n                        components will be repeater components.')
ctFnbPortConnectionChanges = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectionChanges.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectionChanges.setDescription("Maintains the number of times any port within\n                        the mangement domain of this MIM changes it's\n                        port assignment.")
mibBuilder.exportSymbols("CTRON-CSMACD-MIB", ctFnbCSMACDTable=ctFnbCSMACDTable, ctFnbPortConnectEntry=ctFnbPortConnectEntry, ctFnbCSMACDEntry=ctFnbCSMACDEntry, ctFnbPortConnectionChanges=ctFnbPortConnectionChanges, ctFnbCSMACD=ctFnbCSMACD, ctFnbPortConnectPortAssignment=ctFnbPortConnectPortAssignment, ctFnbPortConnectTable=ctFnbPortConnectTable, ctFnbConnect=ctFnbConnect, ctFnbPortConnectPortIndex=ctFnbPortConnectPortIndex, ctFnbCSMACDIndex=ctFnbCSMACDIndex, ctFnbPortConnectBoardIndex=ctFnbPortConnectBoardIndex, ctFnbPortChanges=ctFnbPortChanges, ctFnbPortConnect=ctFnbPortConnect, ctFnbPortCompID=ctFnbPortCompID)
