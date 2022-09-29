#
# PySNMP MIB module ADTRAN-AOS-POWER (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-POWER
# Produced by pysmi-1.1.8 at Thu Sep 29 12:38:35 2022
# On host fv-az343-100 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
adGenAOSPower, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSPower", "adGenAOSConformance")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, MibIdentifier, Counter32, Integer32, IpAddress, Gauge32, TimeTicks, ObjectIdentity, iso, Unsigned32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Counter32", "Integer32", "IpAddress", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "Unsigned32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
adGenAOSPowerMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1))
adGenAOSPowerMonitor.setRevisions(('2010-09-10 00:00', '2013-02-10 00:00',))
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setLastUpdated('201009100000Z')
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setOrganization('ADTRAN, Inc.')
adGenAOSPowerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0))
adGenAOSPowerRollOverCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1))
adGenAOSPowerEpsRps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2))
class AdEpsPowerDeliveryStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("delivering", 1), ("notDelivering", 2), ("failed", 3), ("unknown", 4))

class AdRpsPowerDeliveryStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("failed", 1), ("busy", 2), ("delivering", 3), ("available", 4), ("unknown", 5))

class AdPowerConnectionStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("connected", 1), ("notConnected", 2), ("notApplicable", 3), ("unknown", 4))

adGenAOSPowerRolloverOnAC = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRolloverOnAC.setStatus('current')
adGenAOSPwrRollOvrEvntSecSinceEpoch = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSPwrRollOvrEvntSecSinceEpoch.setStatus('current')
adGenAOSPowerEpsRpsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1), )
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsTable.setStatus('current')
adGenAOSPowerEpsRpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"))
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsEntry.setStatus('current')
adGenAOSPowerEpsRpsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsInstanceId.setStatus('current')
adGenAOSPowerEpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 2), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsConnectionState.setStatus('current')
adGenAOSPowerEpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 3), AdEpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsDeliveryState.setStatus('current')
adGenAOSPowerRpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 4), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsConnectionState.setStatus('current')
adGenAOSPowerRpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 5), AdRpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsDeliveryState.setStatus('current')
adGenAOSPowerRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"), ("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"))
if mibBuilder.loadTexts: adGenAOSPowerRollover.setStatus('current')
adGenAOSEpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSEpsConnectionChange.setStatus('current')
adGenAOSEpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSEpsDeliveryChange.setStatus('current')
adGenAOSRpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSRpsConnectionChange.setStatus('current')
adGenAOSRpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSRpsDeliveryChange.setStatus('current')
adGenAOSPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11))
adGenAOSPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1))
adGenAOSPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2))
adGenAOSPowerFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollOverCtlGroup"), ("ADTRAN-AOS-POWER", "adGenAOSPowerNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsRpsConfigurationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSRpsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerFullCompliance = adGenAOSPowerFullCompliance.setStatus('current')
adGenAOSPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerNotificationGroup = adGenAOSPowerNotificationGroup.setStatus('current')
adGenAOSPowerRollOverCtlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerRollOverCtlGroup = adGenAOSPowerRollOverCtlGroup.setStatus('current')
adGenAOSEpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSEpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSEpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsNotificationGroup = adGenAOSEpsNotificationGroup.setStatus('current')
adGenAOSRpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSRpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSRpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSRpsNotificationGroup = adGenAOSRpsNotificationGroup.setStatus('current')
adGenAOSEpsRpsConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsRpsConfigurationGroup = adGenAOSEpsRpsConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-POWER", AdRpsPowerDeliveryStateTC=AdRpsPowerDeliveryStateTC, adGenAOSEpsConnectionChange=adGenAOSEpsConnectionChange, adGenAOSPowerEpsRps=adGenAOSPowerEpsRps, adGenAOSPowerEpsRpsEntry=adGenAOSPowerEpsRpsEntry, adGenAOSPowerRolloverOnAC=adGenAOSPowerRolloverOnAC, adGenAOSEpsRpsConfigurationGroup=adGenAOSEpsRpsConfigurationGroup, adGenAOSEpsNotificationGroup=adGenAOSEpsNotificationGroup, adGenAOSPowerRollover=adGenAOSPowerRollover, adGenAOSPwrRollOvrEvntSecSinceEpoch=adGenAOSPwrRollOvrEvntSecSinceEpoch, adGenAOSPowerEpsRpsInstanceId=adGenAOSPowerEpsRpsInstanceId, adGenAOSPowerConformance=adGenAOSPowerConformance, adGenAOSPowerEpsDeliveryState=adGenAOSPowerEpsDeliveryState, adGenAOSPowerRollOverCtl=adGenAOSPowerRollOverCtl, adGenAOSPowerCompliances=adGenAOSPowerCompliances, adGenAOSPowerFullCompliance=adGenAOSPowerFullCompliance, PYSNMP_MODULE_ID=adGenAOSPowerMonitor, adGenAOSPowerEpsRpsTable=adGenAOSPowerEpsRpsTable, adGenAOSPowerRpsConnectionState=adGenAOSPowerRpsConnectionState, adGenAOSPowerTraps=adGenAOSPowerTraps, AdPowerConnectionStateTC=AdPowerConnectionStateTC, adGenAOSEpsDeliveryChange=adGenAOSEpsDeliveryChange, AdEpsPowerDeliveryStateTC=AdEpsPowerDeliveryStateTC, adGenAOSRpsConnectionChange=adGenAOSRpsConnectionChange, adGenAOSPowerMonitor=adGenAOSPowerMonitor, adGenAOSPowerEpsConnectionState=adGenAOSPowerEpsConnectionState, adGenAOSPowerRpsDeliveryState=adGenAOSPowerRpsDeliveryState, adGenAOSPowerGroups=adGenAOSPowerGroups, adGenAOSPowerNotificationGroup=adGenAOSPowerNotificationGroup, adGenAOSRpsDeliveryChange=adGenAOSRpsDeliveryChange, adGenAOSPowerRollOverCtlGroup=adGenAOSPowerRollOverCtlGroup, adGenAOSRpsNotificationGroup=adGenAOSRpsNotificationGroup)
