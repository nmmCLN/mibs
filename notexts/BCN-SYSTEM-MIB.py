#
# PySNMP MIB module BCN-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:04:01 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
bcnMgmt, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnMgmt")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, ModuleIdentity, NotificationType, TimeTicks, Gauge32, Counter32, Integer32, Unsigned32, Bits, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "Counter32", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "Counter64")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
bcnSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 1))
bcnSystemMIB.setRevisions(('2010-11-30 12:00',))
if mibBuilder.loadTexts: bcnSystemMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnSystemMIB.setOrganization('BlueCat Networks')
bcnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2))
bcnSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2))
bcnSystemNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3))
bcnSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4))
bcnSysIdentification = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1))
if mibBuilder.loadTexts: bcnSysIdentification.setStatus('current')
bcnSysIdProduct = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdProduct.setStatus('current')
bcnSysIdOSRelease = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdOSRelease.setStatus('current')
bcnSysIdSerial = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdSerial.setStatus('current')
bcnSysIdServiceTag = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServiceTag.setStatus('current')
bcnSysIdPlatform = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdPlatform.setStatus('current')
bcnSysIdVendorPlatform = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdVendorPlatform.setStatus('current')
bcnSysIdServicesTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7), )
if mibBuilder.loadTexts: bcnSysIdServicesTable.setStatus('current')
bcnSysIdServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1), ).setIndexNames((0, "BCN-SYSTEM-MIB", "bcnSysIdServicesIndex"))
if mibBuilder.loadTexts: bcnSysIdServicesEntry.setStatus('current')
bcnSysIdServicesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnSysIdServicesIndex.setStatus('current')
bcnSysIdServicesOID = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServicesOID.setStatus('current')
bcnSysIdServicesStateTS = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServicesStateTS.setStatus('current')
bcnSysServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2))
if mibBuilder.loadTexts: bcnSysServices.setStatus('current')
bcnSysServDNSService = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 1))
bcnSysServDHCPService = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 2))
bcnSysServTFTPService = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 3))
bcnSysServLicensing = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 4))
bcnSysServTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 5))
bcnSysServNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 6))
bcnSysServPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 7))
bcnSysServNetworkInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 8))
bcnSysServHighAvailability = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 9))
bcnSysServReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 10))
bcnSysServSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2, 11))
bcnSysNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 0))
bcnSysNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1))
bcnSysSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("reboot", 2), ("shutdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysSerOperState.setStatus('current')
bcnSysAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 2), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnSysAlarmSeverity.setStatus('current')
bcnSysAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnSysAlarmInfo.setStatus('current')
bcnSysAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 0, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysSerOperState"), ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"), ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
if mibBuilder.loadTexts: bcnSysAlarmNotif.setStatus('current')
bcnSysServliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1))
bcnSysGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2))
bcnSysIdentificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysIdProduct"), ("BCN-SYSTEM-MIB", "bcnSysIdOSRelease"), ("BCN-SYSTEM-MIB", "bcnSysIdSerial"), ("BCN-SYSTEM-MIB", "bcnSysIdServiceTag"), ("BCN-SYSTEM-MIB", "bcnSysIdPlatform"), ("BCN-SYSTEM-MIB", "bcnSysIdVendorPlatform"), ("BCN-SYSTEM-MIB", "bcnSysIdServicesOID"), ("BCN-SYSTEM-MIB", "bcnSysIdServicesStateTS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysIdentificationGroup = bcnSysIdentificationGroup.setStatus('current')
bcnSysNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 2)).setObjects(("BCN-SYSTEM-MIB", "bcnSysAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysNotificationEventGroup = bcnSysNotificationEventGroup.setStatus('current')
bcnSysNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 3)).setObjects(("BCN-SYSTEM-MIB", "bcnSysSerOperState"), ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"), ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysNotificationDataGroup = bcnSysNotificationDataGroup.setStatus('current')
bcnSysServliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysIdentificationGroup"), ("BCN-SYSTEM-MIB", "bcnSysNotificationEventGroup"), ("BCN-SYSTEM-MIB", "bcnSysNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysServliance = bcnSysServliance.setStatus('current')
mibBuilder.exportSymbols("BCN-SYSTEM-MIB", bcnSysServices=bcnSysServices, bcnSysIdServiceTag=bcnSysIdServiceTag, bcnSysGroups=bcnSysGroups, bcnSysServSystem=bcnSysServSystem, bcnSysNotificationEventGroup=bcnSysNotificationEventGroup, bcnSysServliance=bcnSysServliance, bcnSysAlarmNotif=bcnSysAlarmNotif, bcnSysIdOSRelease=bcnSysIdOSRelease, bcnSysIdServicesOID=bcnSysIdServicesOID, bcnSysServHighAvailability=bcnSysServHighAvailability, bcnSysServDHCPService=bcnSysServDHCPService, bcnSysIdServicesEntry=bcnSysIdServicesEntry, bcnSysIdServicesStateTS=bcnSysIdServicesStateTS, bcnSysIdentification=bcnSysIdentification, bcnSysServTFTPService=bcnSysServTFTPService, bcnSystem=bcnSystem, bcnSysIdServicesIndex=bcnSysIdServicesIndex, PYSNMP_MODULE_ID=bcnSystemMIB, bcnSysAlarmInfo=bcnSysAlarmInfo, bcnSysIdPlatform=bcnSysIdPlatform, bcnSysIdSerial=bcnSysIdSerial, bcnSysNotificationData=bcnSysNotificationData, bcnSysNotificationDataGroup=bcnSysNotificationDataGroup, bcnSysServDNSService=bcnSysServDNSService, bcnSysNotificationEvents=bcnSysNotificationEvents, bcnSysServliances=bcnSysServliances, bcnSysServLicensing=bcnSysServLicensing, bcnSystemMIB=bcnSystemMIB, bcnSysIdProduct=bcnSysIdProduct, bcnSysServNTP=bcnSysServNTP, bcnSysSerOperState=bcnSysSerOperState, bcnSysIdentificationGroup=bcnSysIdentificationGroup, bcnSysAlarmSeverity=bcnSysAlarmSeverity, bcnSysServNetworkInterface=bcnSysServNetworkInterface, bcnSystemNotification=bcnSystemNotification, bcnSysIdServicesTable=bcnSysIdServicesTable, bcnSysServTFTP=bcnSysServTFTP, bcnSysIdVendorPlatform=bcnSysIdVendorPlatform, bcnSysServPowerSupply=bcnSysServPowerSupply, bcnSystemObjects=bcnSystemObjects, bcnSysServReplication=bcnSysServReplication, bcnSystemConformance=bcnSystemConformance)
