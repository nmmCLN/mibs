#
# PySNMP MIB module RADLAN-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-COPY-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:33:27 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Bits, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Gauge32, IpAddress, TimeTicks, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "TimeTicks", "ModuleIdentity", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlCopy = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 87))
rlCopy.setRevisions(('2006-02-02 00:00', '2003-09-22 00:00',))
if mibBuilder.loadTexts: rlCopy.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: rlCopy.setOrganization('Radlan Computer Communications Ltd.')
class RlCopyApplicationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mcli", 1), ("cli", 2), ("ewb", 3), ("nms", 4), ("initerm", 5), ("serial", 6))

class RlCopyLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("local", 1), ("anotherUnit", 2), ("tftp", 3), ("xmodem", 4), ("scp", 5), ("serial", 6))

class RlCopyFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("runningConfig", 2), ("startupConfig", 3), ("backupConfig", 4), ("runningMibConfig", 5), ("startupMibConfig", 6), ("backupMibConfig", 7), ("image", 8), ("boot", 9), ("null", 10))

rlCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMibVersion.setStatus('current')
rlCopyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 2), )
if mibBuilder.loadTexts: rlCopyTable.setStatus('current')
rlCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 2, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyIndex"))
if mibBuilder.loadTexts: rlCopyEntry.setStatus('current')
rlCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyIndex.setStatus('current')
rlCopyApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyApplicationId.setStatus('current')
rlCopySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceLocation.setStatus('current')
rlCopySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceIpAddress.setStatus('current')
rlCopySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceUnitNumber.setStatus('current')
rlCopySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileName.setStatus('current')
rlCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileType.setStatus('current')
rlCopyDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationLocation.setStatus('current')
rlCopyDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationIpAddress.setStatus('current')
rlCopyDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationUnitNumber.setStatus('current')
rlCopyDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileName.setStatus('current')
rlCopyDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileType.setStatus('current')
rlCopyUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyUpTime.setStatus('current')
rlCopyOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyOperationState.setStatus('current')
rlCopyBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyBytesTransferred.setStatus('current')
rlCopyInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInBackground.setStatus('current')
rlCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyRowStatus.setStatus('current')
rlCopyHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryIndex.setStatus('current')
rlCopyFreeHistoryIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyFreeHistoryIndex.setStatus('current')
rlCopyHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 4), )
if mibBuilder.loadTexts: rlCopyHistoryTable.setStatus('current')
rlCopyHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 4, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyHistoryHistoryIndex"))
if mibBuilder.loadTexts: rlCopyHistoryEntry.setStatus('current')
rlCopyHistoryHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryHistoryIndex.setStatus('current')
rlCopyHistoryApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryApplicationId.setStatus('current')
rlCopyHistorySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceLocation.setStatus('current')
rlCopyHistorySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceIpAddress.setStatus('current')
rlCopyHistorySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceUnitNumber.setStatus('current')
rlCopyHistorySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileName.setStatus('current')
rlCopyHistorySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileType.setStatus('current')
rlCopyHistoryDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationLocation.setStatus('current')
rlCopyHistoryDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationIpAddress.setStatus('current')
rlCopyHistoryDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationUnitNumber.setStatus('current')
rlCopyHistoryDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileName.setStatus('current')
rlCopyHistoryDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileType.setStatus('current')
rlCopyHistoryUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryUpTime.setStatus('current')
rlCopyHistoryOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryOperationState.setStatus('current')
rlCopyHistoryBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryBytesTransferred.setStatus('current')
rlCopyHistoryInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInBackground.setStatus('current')
rlCopyHistoryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryRowStatus.setStatus('current')
rlCopyHistoryErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryErrorMessage.setStatus('current')
rlCopyAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyAuditingEnable.setStatus('current')
rlCopyMessagesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 6), )
if mibBuilder.loadTexts: rlCopyMessagesTable.setStatus('current')
rlCopyMessagesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 6, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyMessagesCopyIndex"), (0, "RADLAN-COPY-MIB", "rlCopyMessagesMessageIndex"))
if mibBuilder.loadTexts: rlCopyMessagesEntry.setStatus('current')
rlCopyMessagesCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesCopyIndex.setStatus('current')
rlCopyMessagesMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesMessageIndex.setStatus('current')
rlCopyMessagesMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMessagesMessageText.setStatus('current')
rlCopyMessagesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesStatus.setStatus('current')
rlCopyMessagesTableRemoveEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesTableRemoveEntries.setStatus('current')
mibBuilder.exportSymbols("RADLAN-COPY-MIB", rlCopyHistorySourceFileType=rlCopyHistorySourceFileType, rlCopyIndex=rlCopyIndex, rlCopyHistoryTable=rlCopyHistoryTable, RlCopyLocationType=RlCopyLocationType, rlCopyHistoryDestinationUnitNumber=rlCopyHistoryDestinationUnitNumber, rlCopyHistoryApplicationId=rlCopyHistoryApplicationId, rlCopyFreeHistoryIndex=rlCopyFreeHistoryIndex, rlCopyInBackground=rlCopyInBackground, rlCopyHistoryIndex=rlCopyHistoryIndex, rlCopyAuditingEnable=rlCopyAuditingEnable, rlCopyHistoryInBackground=rlCopyHistoryInBackground, rlCopy=rlCopy, rlCopySourceIpAddress=rlCopySourceIpAddress, rlCopyBytesTransferred=rlCopyBytesTransferred, rlCopyHistoryBytesTransferred=rlCopyHistoryBytesTransferred, rlCopyHistoryErrorMessage=rlCopyHistoryErrorMessage, rlCopyHistoryDestinationLocation=rlCopyHistoryDestinationLocation, rlCopyOperationState=rlCopyOperationState, rlCopySourceLocation=rlCopySourceLocation, rlCopyMessagesMessageIndex=rlCopyMessagesMessageIndex, rlCopySourceFileType=rlCopySourceFileType, rlCopyHistorySourceFileName=rlCopyHistorySourceFileName, rlCopyHistorySourceUnitNumber=rlCopyHistorySourceUnitNumber, rlCopyDestinationLocation=rlCopyDestinationLocation, rlCopyHistoryDestinationFileType=rlCopyHistoryDestinationFileType, rlCopyMessagesEntry=rlCopyMessagesEntry, rlCopyDestinationIpAddress=rlCopyDestinationIpAddress, rlCopyMessagesStatus=rlCopyMessagesStatus, rlCopyHistoryOperationState=rlCopyHistoryOperationState, rlCopyMessagesMessageText=rlCopyMessagesMessageText, rlCopyApplicationId=rlCopyApplicationId, rlCopyRowStatus=rlCopyRowStatus, rlCopyHistoryRowStatus=rlCopyHistoryRowStatus, rlCopyTable=rlCopyTable, RlCopyApplicationType=RlCopyApplicationType, rlCopyMessagesTableRemoveEntries=rlCopyMessagesTableRemoveEntries, rlCopyHistorySourceLocation=rlCopyHistorySourceLocation, rlCopyMessagesCopyIndex=rlCopyMessagesCopyIndex, rlCopyMessagesTable=rlCopyMessagesTable, rlCopyDestinationFileName=rlCopyDestinationFileName, rlCopyHistoryHistoryIndex=rlCopyHistoryHistoryIndex, rlCopySourceUnitNumber=rlCopySourceUnitNumber, rlCopyHistoryDestinationFileName=rlCopyHistoryDestinationFileName, rlCopyEntry=rlCopyEntry, PYSNMP_MODULE_ID=rlCopy, rlCopyHistoryUpTime=rlCopyHistoryUpTime, rlCopyHistorySourceIpAddress=rlCopyHistorySourceIpAddress, RlCopyFileType=RlCopyFileType, rlCopyDestinationUnitNumber=rlCopyDestinationUnitNumber, rlCopyMibVersion=rlCopyMibVersion, rlCopyUpTime=rlCopyUpTime, rlCopyHistoryDestinationIpAddress=rlCopyHistoryDestinationIpAddress, rlCopyDestinationFileType=rlCopyDestinationFileType, rlCopyHistoryEntry=rlCopyHistoryEntry, rlCopySourceFileName=rlCopySourceFileName)
