#
# PySNMP MIB module ARRIS-C3-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-IF-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:09 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Unsigned32, Counter64, IpAddress, enterprises, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Unsigned32", "Counter64", "IpAddress", "enterprises", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmtsC3IfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12))
if mibBuilder.loadTexts: cmtsC3IfMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3IfMIB.setOrganization('Arris International')
dcxIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1))
dcxIfTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1), )
if mibBuilder.loadTexts: dcxIfTable.setStatus('current')
dcxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1), )
ifEntry.registerAugmentions(("ARRIS-C3-IF-MIB", "dcxIfEntry"))
dcxIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: dcxIfEntry.setStatus('current')
dcxIfLoadInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIfLoadInterval.setStatus('current')
dcxIfInputBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfInputBitRate.setStatus('current')
dcxIfInputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfInputPacketRate.setStatus('current')
dcxIfOutputBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfOutputBitRate.setStatus('current')
dcxIfOutputPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 12, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxIfOutputPacketRate.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-IF-MIB", dcxIfTable=dcxIfTable, cmtsC3IfMIB=cmtsC3IfMIB, dcxIfInputPacketRate=dcxIfInputPacketRate, PYSNMP_MODULE_ID=cmtsC3IfMIB, dcxIfOutputBitRate=dcxIfOutputBitRate, dcxIfOutputPacketRate=dcxIfOutputPacketRate, dcxIfObjects=dcxIfObjects, dcxIfEntry=dcxIfEntry, dcxIfLoadInterval=dcxIfLoadInterval, dcxIfInputBitRate=dcxIfInputBitRate)
