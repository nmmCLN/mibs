#
# PySNMP MIB module OPENBSD-MEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-MEM-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 12:49:38 2022
# On host fv-az343-100 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Integer32, IpAddress, MibIdentifier, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, ModuleIdentity, Unsigned32, Counter32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter32", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
memMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 5))
memMIBObjects.setRevisions(('2012-02-09 00:00', '2008-12-23 00:00',))
if mibBuilder.loadTexts: memMIBObjects.setLastUpdated('201202090000Z')
if mibBuilder.loadTexts: memMIBObjects.setOrganization('OpenBSD')
memMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memMIBVersion.setStatus('current')
memIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 5, 2), )
if mibBuilder.loadTexts: memIfTable.setStatus('current')
memIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: memIfEntry.setStatus('current')
memIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfName.setStatus('current')
memIfLiveLocks = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfLiveLocks.setStatus('current')
mibBuilder.exportSymbols("OPENBSD-MEM-MIB", memIfEntry=memIfEntry, memMIBVersion=memMIBVersion, memIfName=memIfName, memIfTable=memIfTable, memIfLiveLocks=memIfLiveLocks, memMIBObjects=memMIBObjects, PYSNMP_MODULE_ID=memMIBObjects)
