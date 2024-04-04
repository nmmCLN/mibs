#
# PySNMP MIB module SIAE-HC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-HC-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Counter64, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
headerCompression = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 79))
headerCompression.setRevisions(('2014-10-07 00:00', '2014-03-31 00:00',))
if mibBuilder.loadTexts: headerCompression.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: headerCompression.setOrganization('SIAE MICROELETTRONICA spa')
headerCompressionMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: headerCompressionMibVersion.setStatus('current')
headerCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2), )
if mibBuilder.loadTexts: headerCompressionTable.setStatus('current')
headerCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1), ).setIndexNames((0, "SIAE-HC-MIB", "headerCompressionIndex"))
if mibBuilder.loadTexts: headerCompressionEntry.setStatus('current')
headerCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: headerCompressionIndex.setStatus('current')
headerCompressionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionAdminStatus.setStatus('current')
headerCompressionContextDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ctx16bytes", 1), ("ctx32bytes", 2), ("ctx64byets", 3), ("ctx128bytes", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionContextDepth.setStatus('current')
headerCompressionParsingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("semiMpls", 2), ("semiIPv4IPv6", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionParsingMode.setStatus('current')
headerCompressionTagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionTagEnable.setStatus('current')
headerCompressionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionRowStatus.setStatus('current')
mibBuilder.exportSymbols("SIAE-HC-MIB", headerCompressionAdminStatus=headerCompressionAdminStatus, headerCompressionParsingMode=headerCompressionParsingMode, headerCompressionIndex=headerCompressionIndex, headerCompressionContextDepth=headerCompressionContextDepth, headerCompression=headerCompression, headerCompressionMibVersion=headerCompressionMibVersion, headerCompressionRowStatus=headerCompressionRowStatus, headerCompressionEntry=headerCompressionEntry, headerCompressionTagEnable=headerCompressionTagEnable, headerCompressionTable=headerCompressionTable, PYSNMP_MODULE_ID=headerCompression)
