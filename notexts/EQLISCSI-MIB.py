#
# PySNMP MIB module EQLISCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLISCSI-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:55 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
iscsiSessionStatsEntry, iscsiSessionAttributesEntry = mibBuilder.importSymbols("ISCSI-MIB", "iscsiSessionStatsEntry", "iscsiSessionAttributesEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, experimental, enterprises, Integer32, ObjectIdentity, Opaque, iso, ModuleIdentity, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "experimental", "enterprises", "Integer32", "ObjectIdentity", "Opaque", "iso", "ModuleIdentity", "Counter32", "Unsigned32", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
eqliscsiExtModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 11))
eqliscsiExtModule.setRevisions(('2002-06-26 00:00',))
if mibBuilder.loadTexts: eqliscsiExtModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqliscsiExtModule.setOrganization('EqualLogic Inc.')
eqliscsiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 11, 1))
eqliscsiSessionStatsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1), )
if mibBuilder.loadTexts: eqliscsiSessionStatsTable.setStatus('current')
eqliscsiSessionStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1), )
iscsiSessionStatsEntry.registerAugmentions(("EQLISCSI-MIB", "eqliscsiSessionStatsEntry"))
eqliscsiSessionStatsEntry.setIndexNames(*iscsiSessionStatsEntry.getIndexNames())
if mibBuilder.loadTexts: eqliscsiSessionStatsEntry.setStatus('current')
eqliscsiSsnErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnErrorCount.setStatus('current')
eqliscsiSsnTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTimeUp.setStatus('current')
eqliscsiSsnTotalDataTrnsfrd = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 3), Counter32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd.setStatus('deprecated')
eqliscsiNodeUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiNodeUuid.setStatus('current')
eqliscsiSsnTotalDataTrnsfrd64 = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 5), Counter64()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnTotalDataTrnsfrd64.setStatus('deprecated')
eqliscsiSsnMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 6), Opaque().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnMembers.setStatus('current')
eqliscsiSsnRouteStats = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 7), Opaque().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnRouteStats.setStatus('current')
eqliscsiSsnLoadValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSsnLoadValue.setStatus('current')
eqliscsiSessionAttributesTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2), )
if mibBuilder.loadTexts: eqliscsiSessionAttributesTable.setStatus('current')
eqliscsiSessionAttributesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1), )
iscsiSessionAttributesEntry.registerAugmentions(("EQLISCSI-MIB", "eqliscsiSessionAttributesEntry"))
eqliscsiSessionAttributesEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())
if mibBuilder.loadTexts: eqliscsiSessionAttributesEntry.setStatus('current')
eqliscsiSessionAttributesType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 11, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("external", 1), ("syncrepl", 2), ("xcopy", 3), ("replica", 4))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqliscsiSessionAttributesType.setStatus('current')
mibBuilder.exportSymbols("EQLISCSI-MIB", eqliscsiSsnRouteStats=eqliscsiSsnRouteStats, eqliscsiSsnErrorCount=eqliscsiSsnErrorCount, eqliscsiSsnTotalDataTrnsfrd64=eqliscsiSsnTotalDataTrnsfrd64, eqliscsiSessionStatsTable=eqliscsiSessionStatsTable, eqliscsiSsnTotalDataTrnsfrd=eqliscsiSsnTotalDataTrnsfrd, eqliscsiNodeUuid=eqliscsiNodeUuid, eqliscsiSessionAttributesEntry=eqliscsiSessionAttributesEntry, eqliscsiSsnLoadValue=eqliscsiSsnLoadValue, eqliscsiExtModule=eqliscsiExtModule, eqliscsiSessionAttributesTable=eqliscsiSessionAttributesTable, eqliscsiSessionAttributesType=eqliscsiSessionAttributesType, eqliscsiSsnTimeUp=eqliscsiSsnTimeUp, eqliscsiSsnMembers=eqliscsiSsnMembers, PYSNMP_MODULE_ID=eqliscsiExtModule, eqliscsiExtObjects=eqliscsiExtObjects, eqliscsiSessionStatsEntry=eqliscsiSessionStatsEntry)
