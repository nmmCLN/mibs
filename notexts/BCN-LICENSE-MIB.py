#
# PySNMP MIB module BCN-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-LICENSE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:11 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, iso, Counter64, MibIdentifier, Bits, Gauge32, TimeTicks, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter64", "MibIdentifier", "Bits", "Gauge32", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "NotificationType", "IpAddress")
DateAndTime, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "TextualConvention", "DisplayString")
bcnLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 1))
bcnLicenseMIB.setRevisions(('2010-11-30 12:00',))
if mibBuilder.loadTexts: bcnLicenseMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnLicenseMIB.setOrganization('BlueCat Networks')
bcnLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6))
bcnLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2))
bcnLicenseNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3))
bcnLicenseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4))
bcnLicenseInformation = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1))
if mibBuilder.loadTexts: bcnLicenseInformation.setStatus('current')
bcnLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2), )
if mibBuilder.loadTexts: bcnLicenseTable.setStatus('current')
bcnLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1), ).setIndexNames((0, "BCN-LICENSE-MIB", "bcnLicenseTableIndex"))
if mibBuilder.loadTexts: bcnLicenseEntry.setStatus('current')
bcnLicenseTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnLicenseTableIndex.setStatus('current')
bcnLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singleServer", 1), ("multiServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseType.setStatus('current')
bcnLicenseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseDescription.setStatus('current')
bcnLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseInstalled.setStatus('current')
bcnLicenseExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseExpiry.setStatus('current')
bcnLicenseGracePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseGracePeriod.setStatus('current')
bcnLicenseValid = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseValid.setStatus('current')
bcnLicenseItemsGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseItemsGranted.setStatus('current')
bcnLicenseItemsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseItemsUsed.setStatus('current')
bcnLicenseNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0))
bcnLicenseNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1))
bcnLicenseAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnLicenseAlarmSeverity.setStatus('current')
bcnLicenseExpiryNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseType"), ("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity"), ("BCN-LICENSE-MIB", "bcnLicenseExpiry"), ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"), ("BCN-LICENSE-MIB", "bcnLicenseValid"))
if mibBuilder.loadTexts: bcnLicenseExpiryNotif.setStatus('current')
bcnLicenseServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1))
bcnLicenseServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2))
bcnLicenseServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseType"), ("BCN-LICENSE-MIB", "bcnLicenseDescription"), ("BCN-LICENSE-MIB", "bcnLicenseInstalled"), ("BCN-LICENSE-MIB", "bcnLicenseExpiry"), ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"), ("BCN-LICENSE-MIB", "bcnLicenseValid"), ("BCN-LICENSE-MIB", "bcnLicenseItemsGranted"), ("BCN-LICENSE-MIB", "bcnLicenseItemsUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseServiceStatusGroup = bcnLicenseServiceStatusGroup.setStatus('current')
bcnLicenseNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 2)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseExpiryNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseNotificationEventGroup = bcnLicenseNotificationEventGroup.setStatus('current')
bcnLicenseNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 3)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseNotificationDataGroup = bcnLicenseNotificationDataGroup.setStatus('current')
bcnLicenseStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseServiceStatusGroup"), ("BCN-LICENSE-MIB", "bcnLicenseNotificationEventGroup"), ("BCN-LICENSE-MIB", "bcnLicenseNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseStatusCompliance = bcnLicenseStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-LICENSE-MIB", bcnLicenseNotification=bcnLicenseNotification, bcnLicenseExpiryNotif=bcnLicenseExpiryNotif, bcnLicenseServiceGroups=bcnLicenseServiceGroups, bcnLicenseStatusCompliance=bcnLicenseStatusCompliance, bcnLicenseMIB=bcnLicenseMIB, bcnLicenseObjects=bcnLicenseObjects, bcnLicenseItemsUsed=bcnLicenseItemsUsed, bcnLicenseValid=bcnLicenseValid, bcnLicenseEntry=bcnLicenseEntry, bcnLicenseServiceCompliances=bcnLicenseServiceCompliances, bcnLicenseNotificationData=bcnLicenseNotificationData, bcnLicenseGracePeriod=bcnLicenseGracePeriod, bcnLicenseNotificationEventGroup=bcnLicenseNotificationEventGroup, bcnLicenseServiceStatusGroup=bcnLicenseServiceStatusGroup, bcnLicenseConformance=bcnLicenseConformance, bcnLicenseItemsGranted=bcnLicenseItemsGranted, bcnLicenseType=bcnLicenseType, bcnLicenseNotificationEvents=bcnLicenseNotificationEvents, bcnLicenseInformation=bcnLicenseInformation, bcnLicenseAlarmSeverity=bcnLicenseAlarmSeverity, bcnLicenseNotificationDataGroup=bcnLicenseNotificationDataGroup, bcnLicenseTableIndex=bcnLicenseTableIndex, bcnLicense=bcnLicense, PYSNMP_MODULE_ID=bcnLicenseMIB, bcnLicenseTable=bcnLicenseTable, bcnLicenseExpiry=bcnLicenseExpiry, bcnLicenseDescription=bcnLicenseDescription, bcnLicenseInstalled=bcnLicenseInstalled)
