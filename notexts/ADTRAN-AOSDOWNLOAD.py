#
# PySNMP MIB module ADTRAN-AOSDOWNLOAD (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSDOWNLOAD
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:37 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, iso, Counter64, NotificationType, MibIdentifier, Bits, Counter32, IpAddress, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "NotificationType", "MibIdentifier", "Bits", "Counter32", "IpAddress", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "ModuleIdentity")
TDomain, TAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TAddress", "TextualConvention", "DisplayString", "RowStatus")
adAOSDownloadMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 3))
adAOSDownloadMib.setRevisions(('2004-09-21 22:16',))
if mibBuilder.loadTexts: adAOSDownloadMib.setLastUpdated('200409212216Z')
if mibBuilder.loadTexts: adAOSDownloadMib.setOrganization('ADTRAN, Inc.')
adAOSDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3))
adAOSDownloadTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1), )
if mibBuilder.loadTexts: adAOSDownloadTable.setStatus('current')
adAOSDownloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1), ).setIndexNames((0, "ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"))
if mibBuilder.loadTexts: adAOSDownloadEntry.setStatus('current')
adAOSDownloadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dlInstance", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadIndex.setStatus('current')
adAOSDownloadOwnerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOwnerAddress.setStatus('current')
adAOSDownloadOwnerDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 3), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOwnerDomain.setStatus('current')
adAOSDownloadTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 4), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadTAddress.setStatus('current')
adAOSDownloadTDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 5), TDomain()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadTDomain.setStatus('current')
adAOSDownloadFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadFilename.setStatus('current')
adAOSDownloadResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("warmReset", 2), ("factoryReset", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadResetType.setStatus('current')
adAOSDownloadErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("fileNotFound", 1), ("accessViolation", 2), ("diskFull", 3), ("illegalOperation", 4), ("unknownTID", 5), ("fileExists", 6), ("noSuchUser", 7), ("notDefined", 8), ("corruptFile", 9), ("noServer", 10), ("tftpTimeout", 11), ("hardwareError", 12), ("success", 13), ("aborted", 14), ("inProgress", 15), ("idle", 16), ("erasingEeprom", 17), ("incompleteFirmware", 18), ("requirePowerCycle", 19), ("cannotUpgrade", 20), ("cannotDowngrade", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadErrorStatus.setStatus('current')
adAOSDownloadErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadErrorText.setStatus('current')
adAOSDownloadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadStatus.setStatus('current')
adAOSDownloadPassesLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadPassesLeft.setStatus('current')
adAOSDownloadOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOctetCount.setStatus('current')
adAOSDownloadDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone('/os/primary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadDestination.setStatus('deprecated')
adAOSDownloadDestinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("config", 3), ("remote", 4), ("other", 5))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadDestinationType.setStatus('current')
adAOSDownloadLogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadLogMaxSize.setStatus('current')
adAOSDownloadLogSize = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadLogSize.setStatus('current')
adAOSDownloadLogTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4), )
if mibBuilder.loadTexts: adAOSDownloadLogTable.setStatus('current')
adAOSDownloadLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1), ).setIndexNames((0, "ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"))
if mibBuilder.loadTexts: adAOSDownloadLogEntry.setStatus('current')
adAOSDlLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogIndex.setStatus('current')
adAOSDlLogOwnerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogOwnerAddress.setStatus('current')
adAOSDlLogOwnerDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 3), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogOwnerDomain.setStatus('current')
adAOSDlLogTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogTAddress.setStatus('current')
adAOSDlLogTDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 5), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogTDomain.setStatus('current')
adAOSDlLogFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogFilename.setStatus('current')
adAOSDlLogResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("warmReset", 2), ("factoryReset", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogResetType.setStatus('current')
adAOSDlLogErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fileNotFound", 1), ("accessViolation", 2), ("diskFull", 3), ("illegalOperation", 4), ("unknownTID", 5), ("fileExists", 6), ("noSuchUser", 7), ("notDefined", 8), ("corruptFile", 9), ("noServer", 10), ("tftpTimeout", 11), ("hardwareError", 12), ("success", 13), ("aborted", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogErrorStatus.setStatus('current')
adAOSDlLogErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogErrorText.setStatus('current')
adAOSDownloadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3))
adAOSDownloadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1))
adAOSDownloadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2))
adAOSDownloadConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1, 1)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDownloadConfigGroup"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadConfigCompliance = adAOSDownloadConfigCompliance.setStatus('current')
adAOSDownloadLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 1)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogFilename"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogResetType"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadLogGroup = adAOSDownloadLogGroup.setStatus('current')
adAOSDownloadConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 2)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadFilename"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadResetType"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorText"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadPassesLeft"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOctetCount"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadDestination"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogMaxSize"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadConfigGroup = adAOSDownloadConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSDOWNLOAD", adAOSDownloadTDomain=adAOSDownloadTDomain, adAOSDownloadConfigCompliance=adAOSDownloadConfigCompliance, adAOSDownloadIndex=adAOSDownloadIndex, adAOSDownloadOctetCount=adAOSDownloadOctetCount, adAOSDownloadLogTable=adAOSDownloadLogTable, adAOSDlLogErrorStatus=adAOSDlLogErrorStatus, adAOSDownloadErrorText=adAOSDownloadErrorText, adAOSDownloadDestinationType=adAOSDownloadDestinationType, adAOSDownloadTAddress=adAOSDownloadTAddress, adAOSDlLogResetType=adAOSDlLogResetType, adAOSDownloadErrorStatus=adAOSDownloadErrorStatus, adAOSDownloadLogGroup=adAOSDownloadLogGroup, adAOSDownloadTable=adAOSDownloadTable, adAOSDownloadStatus=adAOSDownloadStatus, adAOSDlLogOwnerAddress=adAOSDlLogOwnerAddress, adAOSDownloadLogSize=adAOSDownloadLogSize, adAOSDlLogIndex=adAOSDlLogIndex, adAOSDownloadLogEntry=adAOSDownloadLogEntry, PYSNMP_MODULE_ID=adAOSDownloadMib, adAOSDownloadLogMaxSize=adAOSDownloadLogMaxSize, adAOSDlLogFilename=adAOSDlLogFilename, adAOSDownloadPassesLeft=adAOSDownloadPassesLeft, adAOSDownloadGroups=adAOSDownloadGroups, adAOSDownloadDestination=adAOSDownloadDestination, adAOSDownloadOwnerAddress=adAOSDownloadOwnerAddress, adAOSDlLogOwnerDomain=adAOSDlLogOwnerDomain, adAOSDownloadFilename=adAOSDownloadFilename, adAOSDownloadMib=adAOSDownloadMib, adAOSDlLogTAddress=adAOSDlLogTAddress, adAOSDownloadResetType=adAOSDownloadResetType, adAOSDownloadEntry=adAOSDownloadEntry, adAOSDownloadConfigGroup=adAOSDownloadConfigGroup, adAOSDownloadOwnerDomain=adAOSDownloadOwnerDomain, adAOSDownloadCompliances=adAOSDownloadCompliances, adAOSDlLogTDomain=adAOSDlLogTDomain, adAOSDownloadConformance=adAOSDownloadConformance, adAOSDownload=adAOSDownload, adAOSDlLogErrorText=adAOSDlLogErrorText)
