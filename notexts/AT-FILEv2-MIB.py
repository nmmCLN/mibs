#
# PySNMP MIB module AT-FILEv2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-FILEv2-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:06 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Gauge32, NotificationType, Bits, Integer32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Gauge32", "NotificationType", "Bits", "Integer32", "Counter32", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
atFilev2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600))
atFilev2.setRevisions(('2017-03-31 00:00', '2014-04-30 00:00', '2014-04-23 00:00', '2014-04-16 00:00', '2014-01-17 00:00', '2012-09-27 00:00', '2012-09-21 00:00', '2012-05-22 05:00', '2012-05-07 00:00', '2011-09-12 00:00', '2011-05-30 00:00', '2011-04-21 00:00', '2011-03-24 00:00', '2011-01-26 00:00', '2010-09-07 00:00', '2010-06-14 04:59', '2008-12-05 00:00', '2008-11-11 00:00', '2008-09-24 00:00',))
if mibBuilder.loadTexts: atFilev2.setLastUpdated('201703310000Z')
if mibBuilder.loadTexts: atFilev2.setOrganization('Allied Telesis Labs New Zealand')
atFilev2TableOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1))
atFilev2Recursive = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2Recursive.setStatus('obsolete')
atFilev2AllFiles = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2AllFiles.setStatus('obsolete')
atFilev2Device = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2Device.setStatus('obsolete')
atFilev2StackID = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 1, 4), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2StackID.setStatus('obsolete')
atFilev2Table = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2), )
if mibBuilder.loadTexts: atFilev2Table.setStatus('obsolete')
atFilev2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1), ).setIndexNames((0, "AT-FILEv2-MIB", "atFilev2Filename"))
if mibBuilder.loadTexts: atFilev2Entry.setStatus('obsolete')
atFilev2Filename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 112))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2Filename.setStatus('obsolete')
atFilev2FileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileSize.setStatus('obsolete')
atFilev2FileCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileCreationTime.setStatus('obsolete')
atFilev2FileAttribs = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileAttribs.setStatus('obsolete')
atFilev2FileOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3))
atFilev2SourceStackID = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2SourceStackID.setStatus('current')
atFilev2SourceDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flash", 1), ("card", 2), ("nvs", 3), ("tftp", 4), ("usb", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2SourceDevice.setStatus('current')
atFilev2SourceFilename = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2SourceFilename.setStatus('current')
atFilev2DestinationStackID = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DestinationStackID.setStatus('current')
atFilev2DestinationDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flash", 1), ("card", 2), ("nvs", 3), ("tftp", 4), ("usb", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DestinationDevice.setStatus('current')
atFilev2DestinationFilename = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DestinationFilename.setStatus('current')
atFilev2CopyBegin = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2CopyBegin.setStatus('current')
atFilev2MoveBegin = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2MoveBegin.setStatus('current')
atFilev2DeleteBegin = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DeleteBegin.setStatus('current')
atFilev2Flash1 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 10))
atFilev2Card2 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 11))
atFilev2Nvs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 12))
atFilev2Tftp4 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13))
atFilev2TftpIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 13, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2TftpIPAddr.setStatus('current')
atFilev2Usb5 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 15))
atFilev2DirOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14))
atFilev2DirStackID = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DirStackID.setStatus('current')
atFilev2DirFileSystem = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("flash", 1), ("card", 2), ("nvs", 3), ("usb", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DirFileSystem.setStatus('current')
atFilev2DirPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DirPath.setStatus('current')
atFilev2SourceDirName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2SourceDirName.setStatus('current')
atFilev2DestDirName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2DestDirName.setStatus('current')
atFilev2BeginDirOperation = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("createDir", 2), ("renameDir", 3), ("deleteEmptyDir", 4), ("deleteForceDir", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2BeginDirOperation.setStatus('current')
atFilev2LastDirOpResult = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 3, 14, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2LastDirOpResult.setStatus('current')
atFilev2SDcardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4), )
if mibBuilder.loadTexts: atFilev2SDcardTable.setStatus('current')
atFilev2SDcardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1), ).setIndexNames((0, "AT-FILEv2-MIB", "atFilev2SDcardStackMemberId"))
if mibBuilder.loadTexts: atFilev2SDcardEntry.setStatus('current')
atFilev2SDcardStackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2SDcardStackMemberId.setStatus('current')
atFilev2SDcardPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notPresent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2SDcardPresence.setStatus('current')
atFilev2InfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5), )
if mibBuilder.loadTexts: atFilev2InfoTable.setStatus('obsolete')
atFilev2InfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1), ).setIndexNames((1, "AT-FILEv2-MIB", "atFilev2InfoFilepath"))
if mibBuilder.loadTexts: atFilev2InfoEntry.setStatus('obsolete')
atFilev2InfoFilepath = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 112))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFilepath.setStatus('obsolete')
atFilev2InfoFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileSize.setStatus('obsolete')
atFilev2InfoFileCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileCreationTime.setStatus('obsolete')
atFilev2InfoFileIsDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileIsDirectory.setStatus('obsolete')
atFilev2InfoFileIsReadable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileIsReadable.setStatus('obsolete')
atFilev2InfoFileIsWriteable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileIsWriteable.setStatus('obsolete')
atFilev2InfoFileIsExecutable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2InfoFileIsExecutable.setStatus('obsolete')
atFilev2USBMediaTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6), )
if mibBuilder.loadTexts: atFilev2USBMediaTable.setStatus('current')
atFilev2USBMediaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1), ).setIndexNames((0, "AT-FILEv2-MIB", "atFilev2USBMediaStackMemberId"))
if mibBuilder.loadTexts: atFilev2USBMediaEntry.setStatus('current')
atFilev2USBMediaStackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2USBMediaStackMemberId.setStatus('current')
atFilev2USBMediaPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notPresent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2USBMediaPresence.setStatus('current')
atFilev2FileViewer = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7))
atFilev2FileViewerStackId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 1), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2FileViewerStackId.setStatus('current')
atFilev2FileViewerDevice = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flash", 1), ("card", 2), ("nvs", 3), ("tftp", 4), ("usb", 5))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2FileViewerDevice.setStatus('current')
atFilev2FileViewerCurrentPath = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFilev2FileViewerCurrentPath.setStatus('current')
atFilev2FileViewerTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4), )
if mibBuilder.loadTexts: atFilev2FileViewerTable.setStatus('current')
atFilev2FileViewerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1), ).setIndexNames((1, "AT-FILEv2-MIB", "atFilev2FileViewerName"))
if mibBuilder.loadTexts: atFilev2FileViewerEntry.setStatus('current')
atFilev2FileViewerName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 112))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerName.setStatus('current')
atFilev2FileViewerSize = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerSize.setStatus('current')
atFilev2FileViewerCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerCreationTime.setStatus('current')
atFilev2FileViewerIsDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerIsDirectory.setStatus('current')
atFilev2FileViewerIsReadable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerIsReadable.setStatus('current')
atFilev2FileViewerIsWriteable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerIsWriteable.setStatus('current')
atFilev2FileViewerIsExecutable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 600, 7, 4, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFilev2FileViewerIsExecutable.setStatus('current')
mibBuilder.exportSymbols("AT-FILEv2-MIB", atFilev2InfoFileIsExecutable=atFilev2InfoFileIsExecutable, atFilev2FileCreationTime=atFilev2FileCreationTime, atFilev2SourceFilename=atFilev2SourceFilename, atFilev2CopyBegin=atFilev2CopyBegin, atFilev2SourceStackID=atFilev2SourceStackID, atFilev2Flash1=atFilev2Flash1, atFilev2Filename=atFilev2Filename, atFilev2InfoFileIsDirectory=atFilev2InfoFileIsDirectory, atFilev2USBMediaPresence=atFilev2USBMediaPresence, atFilev2Card2=atFilev2Card2, atFilev2DirFileSystem=atFilev2DirFileSystem, atFilev2SDcardStackMemberId=atFilev2SDcardStackMemberId, atFilev2InfoTable=atFilev2InfoTable, atFilev2Entry=atFilev2Entry, atFilev2StackID=atFilev2StackID, atFilev2=atFilev2, atFilev2FileViewerStackId=atFilev2FileViewerStackId, atFilev2TftpIPAddr=atFilev2TftpIPAddr, atFilev2DestDirName=atFilev2DestDirName, atFilev2DirPath=atFilev2DirPath, atFilev2FileViewerSize=atFilev2FileViewerSize, atFilev2Table=atFilev2Table, atFilev2FileViewerTable=atFilev2FileViewerTable, atFilev2MoveBegin=atFilev2MoveBegin, atFilev2SDcardPresence=atFilev2SDcardPresence, atFilev2InfoFileSize=atFilev2InfoFileSize, atFilev2FileViewerEntry=atFilev2FileViewerEntry, atFilev2DeleteBegin=atFilev2DeleteBegin, atFilev2InfoEntry=atFilev2InfoEntry, atFilev2InfoFileIsReadable=atFilev2InfoFileIsReadable, atFilev2Recursive=atFilev2Recursive, atFilev2InfoFileCreationTime=atFilev2InfoFileCreationTime, atFilev2InfoFilepath=atFilev2InfoFilepath, atFilev2Nvs3=atFilev2Nvs3, atFilev2USBMediaEntry=atFilev2USBMediaEntry, atFilev2FileViewerCreationTime=atFilev2FileViewerCreationTime, atFilev2DestinationDevice=atFilev2DestinationDevice, atFilev2FileViewerDevice=atFilev2FileViewerDevice, atFilev2TableOptions=atFilev2TableOptions, atFilev2DirStackID=atFilev2DirStackID, PYSNMP_MODULE_ID=atFilev2, atFilev2DestinationFilename=atFilev2DestinationFilename, atFilev2DirOperation=atFilev2DirOperation, atFilev2FileViewerCurrentPath=atFilev2FileViewerCurrentPath, atFilev2FileViewerIsWriteable=atFilev2FileViewerIsWriteable, atFilev2SourceDirName=atFilev2SourceDirName, atFilev2LastDirOpResult=atFilev2LastDirOpResult, atFilev2FileViewerName=atFilev2FileViewerName, atFilev2USBMediaStackMemberId=atFilev2USBMediaStackMemberId, atFilev2FileViewer=atFilev2FileViewer, atFilev2Usb5=atFilev2Usb5, atFilev2USBMediaTable=atFilev2USBMediaTable, atFilev2FileSize=atFilev2FileSize, atFilev2SourceDevice=atFilev2SourceDevice, atFilev2Tftp4=atFilev2Tftp4, atFilev2SDcardTable=atFilev2SDcardTable, atFilev2FileOperation=atFilev2FileOperation, atFilev2InfoFileIsWriteable=atFilev2InfoFileIsWriteable, atFilev2AllFiles=atFilev2AllFiles, atFilev2SDcardEntry=atFilev2SDcardEntry, atFilev2FileViewerIsDirectory=atFilev2FileViewerIsDirectory, atFilev2FileViewerIsReadable=atFilev2FileViewerIsReadable, atFilev2DestinationStackID=atFilev2DestinationStackID, atFilev2FileViewerIsExecutable=atFilev2FileViewerIsExecutable, atFilev2FileAttribs=atFilev2FileAttribs, atFilev2Device=atFilev2Device, atFilev2BeginDirOperation=atFilev2BeginDirOperation)
