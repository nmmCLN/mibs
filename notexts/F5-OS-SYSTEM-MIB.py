#
# PySNMP MIB module F5-OS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-OS-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:00 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
platform, = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Counter64, MibIdentifier, iso, Bits, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "iso", "Bits", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
f5OsSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 3))
f5OsSystem.setRevisions(('2022-04-07 00:00',))
if mibBuilder.loadTexts: f5OsSystem.setLastUpdated('202204070000Z')
if mibBuilder.loadTexts: f5OsSystem.setOrganization('F5 Networks, Inc.')
f5OsSystemModelOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1))
f5OsAppR5x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 1))
f5OsAppR10x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 2))
f5OsAppR2x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 3))
f5OsAppR4x00 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 4))
f5OsVelosCx410 = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 5))
f5OsVelosCx410Partition = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 3, 1, 6))
mibBuilder.exportSymbols("F5-OS-SYSTEM-MIB", f5OsAppR4x00=f5OsAppR4x00, f5OsSystemModelOIDs=f5OsSystemModelOIDs, PYSNMP_MODULE_ID=f5OsSystem, f5OsAppR2x00=f5OsAppR2x00, f5OsSystem=f5OsSystem, f5OsAppR10x00=f5OsAppR10x00, f5OsAppR5x00=f5OsAppR5x00, f5OsVelosCx410=f5OsVelosCx410, f5OsVelosCx410Partition=f5OsVelosCx410Partition)
