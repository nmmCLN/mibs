#
# PySNMP MIB module ADTRAN-AOS-NETWORK-SYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-NETWORK-SYNC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, NotificationType, Integer32, ObjectIdentity, Bits, Counter32, Counter64, MibIdentifier, TimeTicks, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Integer32", "ObjectIdentity", "Bits", "Counter32", "Counter64", "MibIdentifier", "TimeTicks", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSNetSyncMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 9))
adGenAOSNetSyncMib.setRevisions(('2015-09-18 00:00', '2014-03-05 00:00', '2013-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSNetSyncMib.setRevisionsDescriptions(('The following changes have been made in this version:\n                1. Add a trap for the T4 interface output squelch.', 'The following changes have been made in this version:\n                1. Removed the LTI State from the clock defects trap.\n                2. Added a new trap for the LTI State change.', 'Created the adGenAosNetSync MIB. Revision R10.11',))
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setLastUpdated('201509180000Z')
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setContactInfo('        Technical Support Dept.\n                    Postal: ADTRAN, Inc.\n                    901 Explorer Blvd.\n                    Huntsville, AL 35806\n\n               Tel: +1 800 726-8663\n               Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSNetSyncMib.setDescription('The MIB module defines Network Sync configuration information and traps for AdtranOS products.')
adGenAOSNetSync = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9))
adGenAOSNetSyncTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0))
adGenAOSNetSyncTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1))
adGenAOSNetSyncInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2))
adGenAOSNetSyncTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSNetSyncTrapEnable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncTrapEnable.setDescription('This variable indicates whether the system produces\n            the Network Sync trap.')
adGenAOSNetSyncLTIState = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncLTIState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncLTIState.setDescription("A numerical representation of the chassis's LTI(Loss of Timing Info) state.")
adGenAOSNetSyncClockNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncClockNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncClockNumber.setDescription("A numerical representation of the chassis's Network Sync Clock source.")
adGenAOSNetSyncClockDefectStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectStatus.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectStatus.setDescription('This variable indicates the Network Sync clock defect status.\n             The adGenAOSNetSyncClockDefectStatus is a bit map represented as a\n             sum, therefore, it can represent multiple defects simultaneously.\n             Bit 1 which represents no defects  must be set if and only if no other\n             bits are set.\n             \n              The various bit positions are:\n              1     NONE      No defects\n              2     LOS       Loss of signal\n              4     EFD       Exceeded frequency deviation\n              8     LO_ESMC   Loss of ESMC\n             16     QL_FAILED Quality level failed ')
adGenAOSNetSyncT4SquelchState = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchState.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchState.setDescription('A numerical representation of the T4 interface squelch state.')
adGenAOSNetSyncClockDefectTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"))
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectTrap.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncClockDefectTrap.setDescription('A Network Sync trap signifies a change in clock defect status.')
adGenAOSNetSyncLTIStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 2)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState"))
if mibBuilder.loadTexts: adGenAOSNetSyncLTIStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncLTIStateChangeTrap.setDescription('A Network Sync trap signifies a change in Loss of timing state.')
adGenAOSNetSyncT4SquelchStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 3)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState"))
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchStateChangeTrap.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncT4SquelchStateChangeTrap.setDescription('A Network Sync trap signifies a change in T4 interface squelch state.')
adGenAOSNetSyncConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18))
adGenAOSNetSyncGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1))
adGenAOSNetSyncCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2))
adGenAOSNetSyncFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapCfgGroup"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapGroup"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncFullCompliance = adGenAOSNetSyncFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 2 of the adGenAosNetSync MIB. When this MIB is implemented\n        with support for read-write, then such an implementation can claim\n        full compliance.')
adGenAOSNetSyncTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 1)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncTrapCfgGroup = adGenAOSNetSyncTrapCfgGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncTrapCfgGroup.setDescription('This group contains the objects necessary to enable/disable\n            NetSync failure traps.')
adGenAOSNetSyncTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 2)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncTrapGroup = adGenAOSNetSyncTrapGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncTrapGroup.setDescription('The objects necessary to control NetSync notification messages.')
adGenAOSNetSyncNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 3)).setObjects(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectTrap"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIStateChangeTrap"), ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSNetSyncNotificationGroup = adGenAOSNetSyncNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSNetSyncNotificationGroup.setDescription("Traps which may be used to enhance event driven\n            management of the chassis's Network Sync.")
mibBuilder.exportSymbols("ADTRAN-AOS-NETWORK-SYNC-MIB", adGenAOSNetSyncInfo=adGenAOSNetSyncInfo, adGenAOSNetSyncClockNumber=adGenAOSNetSyncClockNumber, adGenAOSNetSyncTrapGroup=adGenAOSNetSyncTrapGroup, adGenAOSNetSyncGroups=adGenAOSNetSyncGroups, adGenAOSNetSync=adGenAOSNetSync, adGenAOSNetSyncConformance=adGenAOSNetSyncConformance, adGenAOSNetSyncCompliances=adGenAOSNetSyncCompliances, adGenAOSNetSyncTrapControl=adGenAOSNetSyncTrapControl, adGenAOSNetSyncClockDefectStatus=adGenAOSNetSyncClockDefectStatus, PYSNMP_MODULE_ID=adGenAOSNetSyncMib, adGenAOSNetSyncTrapEnable=adGenAOSNetSyncTrapEnable, adGenAOSNetSyncNotificationGroup=adGenAOSNetSyncNotificationGroup, adGenAOSNetSyncClockDefectTrap=adGenAOSNetSyncClockDefectTrap, adGenAOSNetSyncMib=adGenAOSNetSyncMib, adGenAOSNetSyncFullCompliance=adGenAOSNetSyncFullCompliance, adGenAOSNetSyncTrapCfgGroup=adGenAOSNetSyncTrapCfgGroup, adGenAOSNetSyncT4SquelchStateChangeTrap=adGenAOSNetSyncT4SquelchStateChangeTrap, adGenAOSNetSyncTrap=adGenAOSNetSyncTrap, adGenAOSNetSyncT4SquelchState=adGenAOSNetSyncT4SquelchState, adGenAOSNetSyncLTIState=adGenAOSNetSyncLTIState, adGenAOSNetSyncLTIStateChangeTrap=adGenAOSNetSyncLTIStateChangeTrap)
