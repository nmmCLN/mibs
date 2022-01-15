#
# PySNMP MIB module ADTRAN-AOSUNIT (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSUNIT
# Produced by pysmi-1.1.8 at Sat Jan 15 20:07:29 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, iso, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Bits, NotificationType, Counter32, Unsigned32, MibIdentifier, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "Integer32", "ModuleIdentity")
TAddress, TDomain, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TDomain", "DisplayString", "TextualConvention", "RowStatus")
adGenAOSUnitMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 1))
adGenAOSUnitMib.setRevisions(('2004-09-28 00:00', '2005-05-12 00:00', '2008-07-30 00:00', '2010-04-09 00:00',))
if mibBuilder.loadTexts: adGenAOSUnitMib.setLastUpdated('200409240000Z')
if mibBuilder.loadTexts: adGenAOSUnitMib.setOrganization('ADTRAN, Inc.')
adGenAOSUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1))
class Utf8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

adAOSBootRevision = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSBootRevision.setStatus('current')
adAOSCurrentImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSCurrentImage.setStatus('current')
adAOSRunConfigChecksum = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSRunConfigChecksum.setStatus('current')
adAOSStartConfigChecksum = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSStartConfigChecksum.setStatus('current')
adAOSDeviceIndex = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceIndex.setStatus('current')
adAOSDeviceGlobalUniqueID = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 6), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceGlobalUniqueID.setStatus('current')
adAOSDeviceHealth = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("unused", 2), ("ok", 3), ("warning", 4), ("critical", 5), ("nonrecoverable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceHealth.setStatus('current')
adAOSDeviceSysObjID = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 8), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceSysObjID.setStatus('current')
adAOSDeviceManagementURL = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 9), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceManagementURL.setStatus('current')
adAOSDeviceManagementURLLabel = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 10), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceManagementURLLabel.setStatus('current')
adAOSDeviceManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 11), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceManufacturer.setStatus('current')
adAOSDeviceProductName = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 12), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceProductName.setStatus('current')
adAOSDeviceSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 13), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceSerialNumber.setStatus('current')
adAOSDeviceVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 14), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceVersion.setStatus('current')
adAOSDeviceHWVersion = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 15), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDeviceHWVersion.setStatus('current')
adAOSDeviceContactPerson = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 16), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPerson.setStatus('current')
adAOSDeviceContactPhone = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 17), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPhone.setStatus('current')
adAOSDeviceContactEmail = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 18), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactEmail.setStatus('current')
adAOSDeviceContactPagerNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 19), Utf8String().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceContactPagerNumber.setStatus('current')
adAOSDeviceLocation = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 20), Utf8String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSDeviceLocation.setStatus('current')
adGenAOSSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("saveconfig", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSSaveConfig.setStatus('current')
adGenAOSReloadSystem = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSReloadSystem.setStatus('current')
adGenAOSCancelReload = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("cancelreload", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSCancelReload.setStatus('current')
adAOSPrimaryImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSPrimaryImage.setStatus('current')
adAOSBackupImage = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSBackupImage.setStatus('current')
adAOSDevicePartNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1, 26), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDevicePartNumber.setStatus('current')
adGenAOSUnitConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1))
adAOSUnitCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1))
adAOSUnitGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2))
adAOSCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 1, 1)).setObjects(("ADTRAN-AOSUNIT", "adGenAOSUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSCompliance = adAOSCompliance.setStatus('current')
adGenAOSUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 1, 2, 1)).setObjects(("ADTRAN-AOSUNIT", "adAOSBootRevision"), ("ADTRAN-AOSUNIT", "adAOSCurrentImage"), ("ADTRAN-AOSUNIT", "adAOSRunConfigChecksum"), ("ADTRAN-AOSUNIT", "adAOSStartConfigChecksum"), ("ADTRAN-AOSUNIT", "adAOSDeviceIndex"), ("ADTRAN-AOSUNIT", "adAOSDeviceGlobalUniqueID"), ("ADTRAN-AOSUNIT", "adAOSDeviceHealth"), ("ADTRAN-AOSUNIT", "adAOSDeviceSysObjID"), ("ADTRAN-AOSUNIT", "adAOSDeviceManagementURL"), ("ADTRAN-AOSUNIT", "adAOSDeviceManufacturer"), ("ADTRAN-AOSUNIT", "adAOSDeviceProductName"), ("ADTRAN-AOSUNIT", "adAOSDeviceSerialNumber"), ("ADTRAN-AOSUNIT", "adAOSDeviceVersion"), ("ADTRAN-AOSUNIT", "adAOSDeviceHWVersion"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPerson"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPhone"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactEmail"), ("ADTRAN-AOSUNIT", "adAOSDeviceContactPagerNumber"), ("ADTRAN-AOSUNIT", "adAOSDeviceLocation"), ("ADTRAN-AOSUNIT", "adGenAOSSaveConfig"), ("ADTRAN-AOSUNIT", "adGenAOSReloadSystem"), ("ADTRAN-AOSUNIT", "adGenAOSCancelReload"), ("ADTRAN-AOSUNIT", "adAOSPrimaryImage"), ("ADTRAN-AOSUNIT", "adAOSBackupImage"), ("ADTRAN-AOSUNIT", "adAOSDevicePartNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSUnitGroup = adGenAOSUnitGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSUNIT", adAOSDeviceIndex=adAOSDeviceIndex, adAOSRunConfigChecksum=adAOSRunConfigChecksum, adGenAOSUnitConformance=adGenAOSUnitConformance, adAOSDeviceHWVersion=adAOSDeviceHWVersion, adAOSDeviceHealth=adAOSDeviceHealth, adGenAOSUnit=adGenAOSUnit, adAOSBootRevision=adAOSBootRevision, adGenAOSUnitMib=adGenAOSUnitMib, adAOSCompliance=adAOSCompliance, adAOSDeviceGlobalUniqueID=adAOSDeviceGlobalUniqueID, adAOSDeviceContactPhone=adAOSDeviceContactPhone, adAOSDeviceManufacturer=adAOSDeviceManufacturer, adAOSUnitCompliances=adAOSUnitCompliances, adAOSDeviceVersion=adAOSDeviceVersion, adGenAOSUnitGroup=adGenAOSUnitGroup, Utf8String=Utf8String, adAOSDeviceManagementURL=adAOSDeviceManagementURL, adGenAOSCancelReload=adGenAOSCancelReload, adAOSDeviceSerialNumber=adAOSDeviceSerialNumber, adGenAOSReloadSystem=adGenAOSReloadSystem, adAOSDevicePartNumber=adAOSDevicePartNumber, adAOSDeviceContactPerson=adAOSDeviceContactPerson, adAOSDeviceManagementURLLabel=adAOSDeviceManagementURLLabel, adAOSStartConfigChecksum=adAOSStartConfigChecksum, adAOSDeviceSysObjID=adAOSDeviceSysObjID, adAOSDeviceContactPagerNumber=adAOSDeviceContactPagerNumber, adAOSDeviceLocation=adAOSDeviceLocation, adAOSCurrentImage=adAOSCurrentImage, adGenAOSSaveConfig=adGenAOSSaveConfig, PYSNMP_MODULE_ID=adGenAOSUnitMib, adAOSDeviceContactEmail=adAOSDeviceContactEmail, adAOSUnitGroups=adAOSUnitGroups, adAOSPrimaryImage=adAOSPrimaryImage, adAOSDeviceProductName=adAOSDeviceProductName, adAOSBackupImage=adAOSBackupImage)
