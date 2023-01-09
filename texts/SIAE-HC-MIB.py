#
# PySNMP MIB module SIAE-HC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-HC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:29 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, NotificationType, iso, Counter32, Unsigned32, Integer32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "iso", "Counter32", "Unsigned32", "Integer32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
headerCompression = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 79))
headerCompression.setRevisions(('2014-10-07 00:00', '2014-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: headerCompression.setRevisionsDescriptions(('Changed MAX-ACCESS clause of some objects in\n             headerCompressionTable\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: headerCompression.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: headerCompression.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: headerCompression.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: headerCompression.setDescription('Management information for equipment header compression.\n            ')
headerCompressionMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: headerCompressionMibVersion.setStatus('current')
if mibBuilder.loadTexts: headerCompressionMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
headerCompressionTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2), )
if mibBuilder.loadTexts: headerCompressionTable.setStatus('current')
if mibBuilder.loadTexts: headerCompressionTable.setDescription('Table with header compression entries')
headerCompressionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1), ).setIndexNames((0, "SIAE-HC-MIB", "headerCompressionIndex"))
if mibBuilder.loadTexts: headerCompressionEntry.setStatus('current')
if mibBuilder.loadTexts: headerCompressionEntry.setDescription('Header compression records')
headerCompressionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: headerCompressionIndex.setStatus('current')
if mibBuilder.loadTexts: headerCompressionIndex.setDescription('Header compression index.')
headerCompressionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionAdminStatus.setStatus('current')
if mibBuilder.loadTexts: headerCompressionAdminStatus.setDescription('This object is used to enable instance of header compression.')
headerCompressionContextDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ctx16bytes", 1), ("ctx32bytes", 2), ("ctx64byets", 3), ("ctx128bytes", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionContextDepth.setStatus('current')
if mibBuilder.loadTexts: headerCompressionContextDepth.setDescription('This object is used to set context depth of the specified instance\n             of header compression.')
headerCompressionParsingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("semiMpls", 2), ("semiIPv4IPv6", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionParsingMode.setStatus('current')
if mibBuilder.loadTexts: headerCompressionParsingMode.setDescription('This object is used to specify the mode of parsing packets.')
headerCompressionTagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionTagEnable.setStatus('current')
if mibBuilder.loadTexts: headerCompressionTagEnable.setDescription('This object is used to enable or disable TAG management.')
headerCompressionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 79, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: headerCompressionRowStatus.setStatus('current')
if mibBuilder.loadTexts: headerCompressionRowStatus.setDescription('Row Status object of the header compression table.')
mibBuilder.exportSymbols("SIAE-HC-MIB", headerCompressionTagEnable=headerCompressionTagEnable, headerCompressionEntry=headerCompressionEntry, headerCompressionContextDepth=headerCompressionContextDepth, headerCompressionRowStatus=headerCompressionRowStatus, PYSNMP_MODULE_ID=headerCompression, headerCompressionAdminStatus=headerCompressionAdminStatus, headerCompressionMibVersion=headerCompressionMibVersion, headerCompressionIndex=headerCompressionIndex, headerCompressionParsingMode=headerCompressionParsingMode, headerCompressionTable=headerCompressionTable, headerCompression=headerCompression)
