#
# PySNMP MIB module BCN-TFTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-TFTP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:04:01 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, NotificationType, TimeTicks, Gauge32, Counter32, Integer32, Unsigned32, Bits, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "Counter32", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "Counter64")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
bcnTftpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 1))
bcnTftpMIB.setRevisions(('2010-11-30 12:00',))
if mibBuilder.loadTexts: bcnTftpMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnTftpMIB.setOrganization('BlueCat Networks')
bcnTftp = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3))
bcnTftpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2))
bcnTftpNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3))
bcnTftpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4))
bcnTftpServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 1))
if mibBuilder.loadTexts: bcnTftpServiceStatus.setStatus('current')
bcnTftpSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnTftpSerOperState.setStatus('current')
bcnTftpServiceStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2))
if mibBuilder.loadTexts: bcnTftpServiceStatistics.setStatus('current')
bcnTftpSerDirs = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnTftpSerDirs.setStatus('current')
bcnTftpSerFiles = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnTftpSerFiles.setStatus('current')
bcnTftpSerFilesSize = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 3), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnTftpSerFilesSize.setStatus('current')
bcnTftpSerPartialList = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 2, 2, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnTftpSerPartialList.setStatus('current')
bcnTftpNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 0))
bcnTftpNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1))
bcnTftpAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnTftpAlarmSeverity.setStatus('current')
bcnTftpAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnTftpAlarmInfo.setStatus('current')
bcnTftpAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 3, 0, 1)).setObjects(("BCN-TFTP-MIB", "bcnTftpSerOperState"), ("BCN-TFTP-MIB", "bcnTftpAlarmSeverity"), ("BCN-TFTP-MIB", "bcnTftpAlarmInfo"))
if mibBuilder.loadTexts: bcnTftpAlarmNotif.setStatus('current')
bcnTftpServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 1))
bcnTftpServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2))
bcnTftpServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 1)).setObjects(("BCN-TFTP-MIB", "bcnTftpSerOperState"), ("BCN-TFTP-MIB", "bcnTftpSerDirs"), ("BCN-TFTP-MIB", "bcnTftpSerFiles"), ("BCN-TFTP-MIB", "bcnTftpSerFilesSize"), ("BCN-TFTP-MIB", "bcnTftpSerPartialList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnTftpServiceStatusGroup = bcnTftpServiceStatusGroup.setStatus('current')
bcnTftpNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 2)).setObjects(("BCN-TFTP-MIB", "bcnTftpAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnTftpNotificationEventGroup = bcnTftpNotificationEventGroup.setStatus('current')
bcnTftpNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 2, 3)).setObjects(("BCN-TFTP-MIB", "bcnTftpAlarmSeverity"), ("BCN-TFTP-MIB", "bcnTftpAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnTftpNotificationDataGroup = bcnTftpNotificationDataGroup.setStatus('current')
bcnTftpStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 3, 4, 1, 1)).setObjects(("BCN-TFTP-MIB", "bcnTftpServiceStatusGroup"), ("BCN-TFTP-MIB", "bcnTftpNotificationEventGroup"), ("BCN-TFTP-MIB", "bcnTftpNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnTftpStatusCompliance = bcnTftpStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-TFTP-MIB", bcnTftpNotification=bcnTftpNotification, bcnTftpSerPartialList=bcnTftpSerPartialList, bcnTftpSerFilesSize=bcnTftpSerFilesSize, bcnTftpServiceStatus=bcnTftpServiceStatus, bcnTftpServiceStatusGroup=bcnTftpServiceStatusGroup, bcnTftpSerDirs=bcnTftpSerDirs, bcnTftpNotificationDataGroup=bcnTftpNotificationDataGroup, bcnTftpServiceCompliances=bcnTftpServiceCompliances, bcnTftpNotificationData=bcnTftpNotificationData, bcnTftpMIB=bcnTftpMIB, bcnTftpStatusCompliance=bcnTftpStatusCompliance, PYSNMP_MODULE_ID=bcnTftpMIB, bcnTftpObjects=bcnTftpObjects, bcnTftpSerOperState=bcnTftpSerOperState, bcnTftpSerFiles=bcnTftpSerFiles, bcnTftpAlarmNotif=bcnTftpAlarmNotif, bcnTftpAlarmInfo=bcnTftpAlarmInfo, bcnTftpConformance=bcnTftpConformance, bcnTftpServiceGroups=bcnTftpServiceGroups, bcnTftp=bcnTftp, bcnTftpServiceStatistics=bcnTftpServiceStatistics, bcnTftpAlarmSeverity=bcnTftpAlarmSeverity, bcnTftpNotificationEventGroup=bcnTftpNotificationEventGroup, bcnTftpNotificationEvents=bcnTftpNotificationEvents)
