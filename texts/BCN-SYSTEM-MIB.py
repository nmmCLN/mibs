#
# PySNMP MIB module BCN-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
bcnMgmt, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnMgmt")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, Counter32, ObjectIdentity, Counter64, NotificationType, TimeTicks, ModuleIdentity, Integer32, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "Counter32", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "IpAddress", "Gauge32", "Unsigned32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
bcnSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 1))
bcnSystemMIB.setRevisions(('2010-11-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnSystemMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnSystemMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnSystemMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnSystemMIB.setContactInfo('BlueCat Networks.\n        Customer Care\n\n        North America\n        Call: +1.866.491.2228\n\n        Europe\n        Call: +44.8081.011.306\n\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnSystemMIB.setDescription('This module contains the objects that define a system.  ')
bcnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2))
bcnSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2))
bcnSystemNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3))
bcnSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4))
bcnSysIdentification = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1))
if mibBuilder.loadTexts: bcnSysIdentification.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdentification.setDescription('Identification of the running system.')
bcnSysIdProduct = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdProduct.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdProduct.setDescription('OIDs for this object are obtained from BCN-PRODUCTS-MIB, i.e.:\n        bcnProductsAdonis250 1.3.6.1.4.1.13315.2.1')
bcnSysIdOSRelease = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdOSRelease.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdOSRelease.setDescription('The BlueCat Networks running OS release.')
bcnSysIdSerial = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdSerial.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdSerial.setDescription('Serial number usually assigned to a hardware platform.')
bcnSysIdServiceTag = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServiceTag.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServiceTag.setDescription('Manufacturer service tag.')
bcnSysIdPlatform = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdPlatform.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdPlatform.setDescription('Platform identification.')
bcnSysIdVendorPlatform = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdVendorPlatform.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdVendorPlatform.setDescription('Platform vendor identification.')
bcnSysIdServicesTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7), )
if mibBuilder.loadTexts: bcnSysIdServicesTable.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServicesTable.setDescription('This table enumerates the services available on this system.')
bcnSysIdServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1), ).setIndexNames((0, "BCN-SYSTEM-MIB", "bcnSysIdServicesIndex"))
if mibBuilder.loadTexts: bcnSysIdServicesEntry.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServicesEntry.setDescription('A logical row in the bcnSysIdServicesTable.')
bcnSysIdServicesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnSysIdServicesIndex.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServicesIndex.setDescription('Table index.')
bcnSysIdServicesOID = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServicesOID.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServicesOID.setDescription('This is the OID of the service available on the system.')
bcnSysIdServicesStateTS = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 1, 7, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnSysIdServicesStateTS.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdServicesStateTS.setDescription('Last time this particular service changed state.')
bcnSysServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 2, 2, 2))
if mibBuilder.loadTexts: bcnSysServices.setStatus('current')
if mibBuilder.loadTexts: bcnSysServices.setDescription('Identification of services or Components available on this system.')
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
if mibBuilder.loadTexts: bcnSysSerOperState.setDescription('System operational states. The possible states are:\n        start(1)\tThe system started.\n        reboot(2)\tThe system is rebooting.\n        shutdown(3)\tThe system is shutting down.\n        ')
bcnSysAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 2), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnSysAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnSysAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnSysAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnSysAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnSysAlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnSysAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 2, 3, 0, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysSerOperState"), ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"), ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
if mibBuilder.loadTexts: bcnSysAlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnSysAlarmNotif.setDescription('This notification is sent when the system starts, reboots or shuts down')
bcnSysServliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1))
bcnSysGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2))
bcnSysIdentificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysIdProduct"), ("BCN-SYSTEM-MIB", "bcnSysIdOSRelease"), ("BCN-SYSTEM-MIB", "bcnSysIdSerial"), ("BCN-SYSTEM-MIB", "bcnSysIdServiceTag"), ("BCN-SYSTEM-MIB", "bcnSysIdPlatform"), ("BCN-SYSTEM-MIB", "bcnSysIdVendorPlatform"), ("BCN-SYSTEM-MIB", "bcnSysIdServicesOID"), ("BCN-SYSTEM-MIB", "bcnSysIdServicesStateTS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysIdentificationGroup = bcnSysIdentificationGroup.setStatus('current')
if mibBuilder.loadTexts: bcnSysIdentificationGroup.setDescription('At a minimum a system must be able to identify itself. This\n        group has to be implemented even by unconfigured systems.')
bcnSysNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 2)).setObjects(("BCN-SYSTEM-MIB", "bcnSysAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysNotificationEventGroup = bcnSysNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnSysNotificationEventGroup.setDescription('System notifications conformance.')
bcnSysNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 2, 3)).setObjects(("BCN-SYSTEM-MIB", "bcnSysSerOperState"), ("BCN-SYSTEM-MIB", "bcnSysAlarmSeverity"), ("BCN-SYSTEM-MIB", "bcnSysAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysNotificationDataGroup = bcnSysNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnSysNotificationDataGroup.setDescription('Server statistics conformance.')
bcnSysServliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 2, 4, 1, 1)).setObjects(("BCN-SYSTEM-MIB", "bcnSysIdentificationGroup"), ("BCN-SYSTEM-MIB", "bcnSysNotificationEventGroup"), ("BCN-SYSTEM-MIB", "bcnSysNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnSysServliance = bcnSysServliance.setStatus('current')
if mibBuilder.loadTexts: bcnSysServliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-SYSTEM-MIB", bcnSysIdServicesOID=bcnSysIdServicesOID, bcnSysServDNSService=bcnSysServDNSService, bcnSysAlarmInfo=bcnSysAlarmInfo, bcnSysIdentificationGroup=bcnSysIdentificationGroup, bcnSysIdServicesStateTS=bcnSysIdServicesStateTS, bcnSysServNetworkInterface=bcnSysServNetworkInterface, bcnSystem=bcnSystem, bcnSysServPowerSupply=bcnSysServPowerSupply, bcnSysIdServiceTag=bcnSysIdServiceTag, bcnSysIdOSRelease=bcnSysIdOSRelease, bcnSysServReplication=bcnSysServReplication, bcnSystemMIB=bcnSystemMIB, bcnSysIdServicesIndex=bcnSysIdServicesIndex, bcnSystemObjects=bcnSystemObjects, bcnSysIdServicesTable=bcnSysIdServicesTable, bcnSysAlarmNotif=bcnSysAlarmNotif, bcnSysServHighAvailability=bcnSysServHighAvailability, bcnSysIdVendorPlatform=bcnSysIdVendorPlatform, bcnSysServTFTP=bcnSysServTFTP, bcnSysIdentification=bcnSysIdentification, bcnSystemNotification=bcnSystemNotification, bcnSystemConformance=bcnSystemConformance, bcnSysIdServicesEntry=bcnSysIdServicesEntry, bcnSysServliance=bcnSysServliance, bcnSysIdProduct=bcnSysIdProduct, bcnSysServTFTPService=bcnSysServTFTPService, bcnSysServliances=bcnSysServliances, bcnSysServDHCPService=bcnSysServDHCPService, bcnSysServLicensing=bcnSysServLicensing, bcnSysNotificationData=bcnSysNotificationData, bcnSysNotificationDataGroup=bcnSysNotificationDataGroup, bcnSysIdPlatform=bcnSysIdPlatform, bcnSysIdSerial=bcnSysIdSerial, bcnSysServices=bcnSysServices, bcnSysNotificationEventGroup=bcnSysNotificationEventGroup, bcnSysAlarmSeverity=bcnSysAlarmSeverity, bcnSysGroups=bcnSysGroups, bcnSysSerOperState=bcnSysSerOperState, bcnSysServSystem=bcnSysServSystem, bcnSysNotificationEvents=bcnSysNotificationEvents, PYSNMP_MODULE_ID=bcnSystemMIB, bcnSysServNTP=bcnSysServNTP)
