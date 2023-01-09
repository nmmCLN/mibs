#
# PySNMP MIB module OPENBSD-MEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-MEM-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:15 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, TimeTicks, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, Counter32, IpAddress, MibIdentifier, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
memMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 5))
memMIBObjects.setRevisions(('2012-02-09 00:00', '2008-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: memMIBObjects.setRevisionsDescriptions(('Correct problems reported by smilint.', 'Add the OPENBSD-MEM-MIB to snmpd.',))
if mibBuilder.loadTexts: memMIBObjects.setLastUpdated('201202090000Z')
if mibBuilder.loadTexts: memMIBObjects.setOrganization('OpenBSD')
if mibBuilder.loadTexts: memMIBObjects.setContactInfo('Editor:     Reyk Floeter\n\t    EMail:      reyk@openbsd.org\n\t    WWW:        http://www.openbsd.org/')
if mibBuilder.loadTexts: memMIBObjects.setDescription('The MIB module exporting OpenBSD memory statistics.')
memMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memMIBVersion.setStatus('current')
if mibBuilder.loadTexts: memMIBVersion.setDescription('The current version of this MIB supported by the agent.\n\t    The memory MIB might be updated frequently to export\n\t    statistics specific to the latest version of OpenBSD.\n\t    The client should check this version.')
memIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 5, 2), )
if mibBuilder.loadTexts: memIfTable.setStatus('current')
if mibBuilder.loadTexts: memIfTable.setDescription('A list of interface entries.  The number of entries is given\n\t    by the value of ifNumber.')
memIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: memIfEntry.setStatus('current')
if mibBuilder.loadTexts: memIfEntry.setDescription('An entry containing memory and systems statistics applicable\n\t    to a particular interface.')
memIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfName.setStatus('current')
if mibBuilder.loadTexts: memIfName.setDescription("The textual name of the interface as assigned by the operating\n\t    system.  For example, `lo0' for the first loopback device or\n\t    `em1' for the second Ethernet device using the `em' driver.")
memIfLiveLocks = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfLiveLocks.setStatus('current')
if mibBuilder.loadTexts: memIfLiveLocks.setDescription('The number of times the growth of the interface receive ring\n\t    was limited as a response to high system load.')
mibBuilder.exportSymbols("OPENBSD-MEM-MIB", memMIBVersion=memMIBVersion, memIfEntry=memIfEntry, PYSNMP_MODULE_ID=memMIBObjects, memIfTable=memIfTable, memIfName=memIfName, memIfLiveLocks=memIfLiveLocks, memMIBObjects=memMIBObjects)
