#
# PySNMP MIB module ADTRAN-AOS-NETWORK-SYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-NETWORK-SYNC-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:13 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, IpAddress, TimeTicks, iso, ObjectIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, ModuleIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "ModuleIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSNetSyncMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 9))
adGenAOSNetSyncMib.setRevisions(('2015-09-18 00:00', '2014-03-05 00:00', '2013-11-07 00:00',))
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setLastUpdated('201509180000Z')
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setOrganization('ADTRAN, Inc.')
adGenAOSNetSync = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9))
adGenAOSNetSyncTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0))
adGenAOSNetSyncTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1))
adGenAOSNetSyncInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2))
adGenAOSNetSyncTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSNetSyncTrapEnable.setStatus('current')
adGenAOSNetSyncLTIState = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncLTIState.setStatus('current')
adGenAOSNetSyncClockNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncClockNumber.setStatus('current')
adGenAOSNetSyncClockDefectStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectStatus.setStatus('current')
adGenAOSNetSyncT4SquelchState = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchState.setStatus('current')
adGenAOSNetSyncClockDefectTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"))
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectTrap.setStatus('current')
adGenAOSNetSyncLTIStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 2)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState"))
if mibBuilder.loadTexts: adGenAOSNetSyncLTIStateChangeTrap.setStatus('current')
adGenAOSNetSyncT4SquelchStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 3)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState"))
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchStateChangeTrap.setStatus('current')
adGenAOSNetSyncConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18))
adGenAOSNetSyncGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1))
adGenAOSNetSyncCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2))
adGenAOSNetSyncFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapCfgGroup"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapGroup"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncFullCompliance = adGenAOSNetSyncFullCompliance.setStatus('current')
adGenAOSNetSyncTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncTrapCfgGroup = adGenAOSNetSyncTrapCfgGroup.setStatus('current')
adGenAOSNetSyncTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 2)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncTrapGroup = adGenAOSNetSyncTrapGroup.setStatus('current')
adGenAOSNetSyncNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 3)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectTrap"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIStateChangeTrap"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncNotificationGroup = adGenAOSNetSyncNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-NETWORK-SYNC-MIB", adGenAOSNetSyncClockNumber=adGenAOSNetSyncClockNumber, adGenAOSNetSyncClockDefectTrap=adGenAOSNetSyncClockDefectTrap, adGenAOSNetSyncTrap=adGenAOSNetSyncTrap, adGenAOSNetSyncT4SquelchStateChangeTrap=adGenAOSNetSyncT4SquelchStateChangeTrap, adGenAOSNetSyncTrapCfgGroup=adGenAOSNetSyncTrapCfgGroup, adGenAOSNetSyncTrapEnable=adGenAOSNetSyncTrapEnable, adGenAOSNetSyncT4SquelchState=adGenAOSNetSyncT4SquelchState, adGenAOSNetSyncLTIStateChangeTrap=adGenAOSNetSyncLTIStateChangeTrap, adGenAOSNetSyncNotificationGroup=adGenAOSNetSyncNotificationGroup, adGenAOSNetSyncConformance=adGenAOSNetSyncConformance, adGenAOSNetSyncLTIState=adGenAOSNetSyncLTIState, adGenAOSNetSync=adGenAOSNetSync, adGenAOSNetSyncTrapGroup=adGenAOSNetSyncTrapGroup, adGenAOSNetSyncTrapControl=adGenAOSNetSyncTrapControl, adGenAOSNetSyncFullCompliance=adGenAOSNetSyncFullCompliance, adGenAOSNetSyncClockDefectStatus=adGenAOSNetSyncClockDefectStatus, adGenAOSNetSyncGroups=adGenAOSNetSyncGroups, adGenAOSNetSyncInfo=adGenAOSNetSyncInfo, adGenAOSNetSyncMib=adGenAOSNetSyncMib, adGenAOSNetSyncCompliances=adGenAOSNetSyncCompliances, PYSNMP_MODULE_ID=adGenAOSNetSyncMib)
