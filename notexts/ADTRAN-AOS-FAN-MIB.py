#
# PySNMP MIB module ADTRAN-AOS-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-FAN-MIB
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
TimeTicks, iso, Counter64, NotificationType, MibIdentifier, Bits, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Unsigned32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "NotificationType", "MibIdentifier", "Bits", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSFanMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 8))
adGenAOSFanMib.setRevisions(('2013-10-22 00:00',))
if mibBuilder.loadTexts: adGenAOSFanMib.setLastUpdated('201310220000Z')
if mibBuilder.loadTexts: adGenAOSFanMib.setOrganization('ADTRAN, Inc.')
adGenAOSFan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8))
adGenAOSFanTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0))
adGenAOSFanTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1))
adGenAOSFanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2))
adGenAOSFanTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSFanTrapEnable.setStatus('current')
adGenAOSFanNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSFanNumber.setStatus('current')
adGenAOSFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if mibBuilder.loadTexts: adGenAOSFanFailure.setStatus('current')
adGenAOSFanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17))
adGenAOSFanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1))
adGenAOSFanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2))
adGenAOSFanFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapCfgGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanFullCompliance = adGenAOSFanFullCompliance.setStatus('current')
adGenAOSFanTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapCfgGroup = adGenAOSFanTrapCfgGroup.setStatus('current')
adGenAOSFanTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 2)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapGroup = adGenAOSFanTrapGroup.setStatus('current')
adGenAOSFanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 3)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanNotificationGroup = adGenAOSFanNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-FAN-MIB", adGenAOSFanTrapControl=adGenAOSFanTrapControl, adGenAOSFanMib=adGenAOSFanMib, adGenAOSFanConformance=adGenAOSFanConformance, adGenAOSFanCompliances=adGenAOSFanCompliances, adGenAOSFanNumber=adGenAOSFanNumber, adGenAOSFanTrap=adGenAOSFanTrap, adGenAOSFanInfo=adGenAOSFanInfo, adGenAOSFanGroups=adGenAOSFanGroups, adGenAOSFanFullCompliance=adGenAOSFanFullCompliance, adGenAOSFanTrapCfgGroup=adGenAOSFanTrapCfgGroup, adGenAOSFanNotificationGroup=adGenAOSFanNotificationGroup, adGenAOSFanFailure=adGenAOSFanFailure, adGenAOSFan=adGenAOSFan, adGenAOSFanTrapEnable=adGenAOSFanTrapEnable, PYSNMP_MODULE_ID=adGenAOSFanMib, adGenAOSFanTrapGroup=adGenAOSFanTrapGroup)
