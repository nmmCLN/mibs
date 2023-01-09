#
# PySNMP MIB module RADLAN-File (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-File
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rlFile, = mibBuilder.importSymbols("RADLAN-MIB", "rlFile")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, MibIdentifier, Counter32, iso, ObjectIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Bits, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Bits", "Gauge32", "ModuleIdentity")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
rlFileMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileMibVersion.setStatus('current')
rlFileTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 2), )
if mibBuilder.loadTexts: rlFileTable.setStatus('current')
rlFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 2, 1), ).setIndexNames((0, "RADLAN-File", "rlFileName"))
if mibBuilder.loadTexts: rlFileEntry.setStatus('current')
rlFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileName.setStatus('current')
rlFilePermission = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("readWrite", 3), ("noReadNoWrite", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFilePermission.setStatus('current')
rlFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileSize.setStatus('current')
rlFileModificationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationDate.setStatus('current')
rlFileModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationTime.setStatus('current')
rlFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileRowStatus.setStatus('current')
rlFileFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFlashSize.setStatus('current')
rlFileActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 3), )
if mibBuilder.loadTexts: rlFileActionTable.setStatus('current')
rlFileActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 3, 1), ).setIndexNames((0, "RADLAN-File", "rlFileActionName"))
if mibBuilder.loadTexts: rlFileActionEntry.setStatus('current')
rlFileActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionName.setStatus('current')
rlFileActionNewName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionNewName.setStatus('current')
rlFileActionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionRowStatus.setStatus('current')
rlFileActionCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rename", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionCommand.setStatus('current')
rlFileTotalSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileTotalSizeOfFlash.setStatus('current')
rlFileFreeSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFreeSizeOfFlash.setStatus('current')
rlFileAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileAuditingEnable.setStatus('current')
mibBuilder.exportSymbols("RADLAN-File", rlFileEntry=rlFileEntry, rlFileActionRowStatus=rlFileActionRowStatus, rlFileActionTable=rlFileActionTable, rlFileMibVersion=rlFileMibVersion, rlFileSize=rlFileSize, rlFileModificationDate=rlFileModificationDate, rlFileActionName=rlFileActionName, rlFileActionEntry=rlFileActionEntry, rlFileAuditingEnable=rlFileAuditingEnable, rlFileFreeSizeOfFlash=rlFileFreeSizeOfFlash, rlFileFlashSize=rlFileFlashSize, rlFileTotalSizeOfFlash=rlFileTotalSizeOfFlash, rlFilePermission=rlFilePermission, rlFileName=rlFileName, rlFileActionNewName=rlFileActionNewName, rlFileModificationTime=rlFileModificationTime, rlFileRowStatus=rlFileRowStatus, rlFileActionCommand=rlFileActionCommand, rlFileTable=rlFileTable)
