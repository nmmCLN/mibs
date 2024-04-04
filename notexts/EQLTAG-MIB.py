#
# PySNMP MIB module EQLTAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLTAG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:38 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
UTFString, eqlGroupId, eqlStorageGroupAdminAccountIndex = mibBuilder.importSymbols("EQLGROUP-MIB", "UTFString", "eqlGroupId", "eqlStorageGroupAdminAccountIndex")
eqliscsiLocalMemberId, eqliscsiVolumeIndex = mibBuilder.importSymbols("EQLVOLUME-MIB", "eqliscsiLocalMemberId", "eqliscsiVolumeIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, iso, Bits, IpAddress, Gauge32, ObjectIdentity, Counter32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "iso", "Bits", "IpAddress", "Gauge32", "ObjectIdentity", "Counter32", "Integer32", "Counter64")
RowStatus, TextualConvention, DisplayString, RowPointer, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "RowPointer", "TruthValue")
eqltagModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 23))
eqltagModule.setRevisions(('2011-10-02 00:00',))
if mibBuilder.loadTexts: eqltagModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqltagModule.setOrganization('EqualLogic Inc.')
eqltagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 23, 1))
eqltagNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 23, 2))
eqltagConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 23, 3))
eqlTagTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1), )
if mibBuilder.loadTexts: eqlTagTable.setStatus('current')
eqlTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1), ).setIndexNames((0, "EQLTAG-MIB", "eqlTagType"), (0, "EQLTAG-MIB", "eqlTagIndex"))
if mibBuilder.loadTexts: eqlTagEntry.setStatus('current')
eqlTagType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("folder", 1))).clone(1))
if mibBuilder.loadTexts: eqlTagType.setStatus('current')
eqlTagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: eqlTagIndex.setStatus('current')
eqlTagRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlTagRowStatus.setStatus('current')
eqlTagValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlTagValue.setStatus('current')
eqlTagAdminAccountKey = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlTagAdminAccountKey.setStatus('current')
eqlTagValueDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 6), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlTagValueDescription.setStatus('current')
eqlTagObjectTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 23, 1, 2), )
if mibBuilder.loadTexts: eqlTagObjectTable.setStatus('current')
eqlTagObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1), ).setIndexNames((0, "EQLTAG-MIB", "eqlTagType"), (0, "EQLTAG-MIB", "eqlTagIndex"), (0, "EQLTAG-MIB", "eqlTagObjectIndex"))
if mibBuilder.loadTexts: eqlTagObjectEntry.setStatus('current')
eqlTagObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlTagObjectIndex.setStatus('current')
eqlTagObjectTaggedObjectPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 2), RowPointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlTagObjectTaggedObjectPointer.setStatus('current')
eqlTagObjectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlTagObjectRowStatus.setStatus('current')
eqlAdminAccountTagTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 23, 1, 3), )
if mibBuilder.loadTexts: eqlAdminAccountTagTable.setStatus('current')
eqlAdminAccountTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 23, 1, 3, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"), (0, "EQLTAG-MIB", "eqlTagType"), (0, "EQLTAG-MIB", "eqlTagIndex"))
if mibBuilder.loadTexts: eqlAdminAccountTagEntry.setStatus('current')
eqlAdminAccountTagAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-only", 1), ("read-write", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlAdminAccountTagAccess.setStatus('current')
eqlVolumeTagTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 23, 1, 4), )
if mibBuilder.loadTexts: eqlVolumeTagTable.setStatus('current')
eqlVolumeTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 23, 1, 4, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"), (0, "EQLTAG-MIB", "eqlTagType"), (0, "EQLTAG-MIB", "eqlTagIndex"))
if mibBuilder.loadTexts: eqlVolumeTagEntry.setStatus('current')
eqlVolumeTagValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 23, 1, 4, 1, 1), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eqlVolumeTagValue.setStatus('current')
mibBuilder.exportSymbols("EQLTAG-MIB", eqlTagAdminAccountKey=eqlTagAdminAccountKey, eqlTagObjectTable=eqlTagObjectTable, eqltagModule=eqltagModule, eqlTagObjectIndex=eqlTagObjectIndex, eqlTagObjectEntry=eqlTagObjectEntry, eqlVolumeTagTable=eqlVolumeTagTable, eqlAdminAccountTagEntry=eqlAdminAccountTagEntry, eqlTagValueDescription=eqlTagValueDescription, PYSNMP_MODULE_ID=eqltagModule, eqltagObjects=eqltagObjects, eqlAdminAccountTagAccess=eqlAdminAccountTagAccess, eqltagConformance=eqltagConformance, eqlTagObjectTaggedObjectPointer=eqlTagObjectTaggedObjectPointer, eqlVolumeTagEntry=eqlVolumeTagEntry, eqlTagEntry=eqlTagEntry, eqlVolumeTagValue=eqlVolumeTagValue, eqlTagTable=eqlTagTable, eqlTagIndex=eqlTagIndex, eqlTagObjectRowStatus=eqlTagObjectRowStatus, eqltagNotifications=eqltagNotifications, eqlAdminAccountTagTable=eqlAdminAccountTagTable, eqlTagValue=eqlTagValue, eqlTagType=eqlTagType, eqlTagRowStatus=eqlTagRowStatus)
