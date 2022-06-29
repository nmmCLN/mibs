#
# PySNMP MIB module ADTRAN-AOS-SIP-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:43 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
iso, ObjectIdentity, Counter32, Integer32, Bits, TimeTicks, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter32", "Integer32", "Bits", "TimeTicks", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipRegistration = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4))
adGenAOSSipRegistration.setRevisions(('2010-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSSipRegistration.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSSipRegistration.setLastUpdated('201011020000Z')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setContactInfo('Technical Support Dept.\n        Postal: ADTRAN, Inc.\n        901 Explorer Blvd.\n        Huntsville, AL 35806\n\n        Tel: +1 800 726-8663\n        Fax: +1 256 963 6217\n        E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setDescription('This MIB contains information regarding SIP registrations.')
adSipRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4))
adSipRegistrationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0))
adSipTrunkRegistrationAlarmTrunkIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setDescription('This DisplayString contains the three digit (i.e. T01) trunk\n         identifier associated with this failed REGISTER attempt.')
adSipTrunkRegistrationAlarmSipIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setDescription('This DisplayString represents the SIP identity for a failed\n         REGISTER attempt.')
adSipTrunkRegistrationAlarmRegistrar = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setDescription('The adSipTrunkRegistrationAlarmRegistrar contains the IP address\n         of the SIP registrar for a failed REGISTER attempt.')
adSipTrunkRegistrationAlarmTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setDescription('The time (seconds since epoch) that a failed REGISTER attempt\n         occurred and not necessarily the when the trap was sent.')
adSipTrunkRegistrationTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5), )
if mibBuilder.loadTexts: adSipTrunkRegistrationTable.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationTable.setDescription('Contains a list of trunk registrations and associated statistics.')
adSipTrunkRegistrationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1), ).setIndexNames((0, "ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTableIndex"))
if mibBuilder.loadTexts: adSipTrunkRegistrationEntry.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationEntry.setDescription('Each entry in the list defines all sip registration fields.')
adSipTrunkRegistrationTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: adSipTrunkRegistrationTableIndex.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationTableIndex.setDescription('This Unsigned32 represents the index of the table.')
adSipTrunkRegistrationTrunkIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationTrunkIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationTrunkIdentity.setDescription('This DisplayString contains the three digit (i.e. T01) trunk\n        identifier.')
adSipTrunkRegistrationSipIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationSipIdentity.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationSipIdentity.setDescription('This DisplayString represents the SIP identity.')
adSipTrunkRegistrationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationStatus.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationStatus.setDescription('This DisplayString represents the registered state (yes/no) \n        of this SIP identity.')
adSipTrunkRegistrarIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrarIpAddress.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrarIpAddress.setDescription('The IP Address of the SIP Registrar.')
adSipTrunkRegistrationGrantTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationGrantTime.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationGrantTime.setDescription('The granted registration time in seconds.')
adSipTrunkRegistrationExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationExpireTime.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationExpireTime.setDescription('The time remaining in seconds until expiration.')
adSipTrunkRegistrationSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationSuccesses.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationSuccesses.setDescription('The number of successful registration attempts.')
adSipTrunkRegistrationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationFailures.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationFailures.setDescription('The number of failed registration attempts.')
adSipTrunkRegistrationRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationRequests.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationRequests.setDescription('The number of registration requests sent.')
adSipTrunkRegistrationChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationChallenges.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationChallenges.setDescription('The number of registration challenges.')
adSipTrunkRegistrationRollovers = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationRollovers.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationRollovers.setDescription('The number of registration rollovers.')
adSipTrunkRegistrationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setStatus('current')
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setDescription('This trap indicates that a SIP trunk registration attempt failed.\n         The sysName is the exact same as defined in SNMPv2-MIB.\n         adSipTrunkRegistrationAlarmTrunkIdentity specifies the three\n         character trunk identity associated with the failed attempt.\n         The corresponding SIP identity and registrar server are contained\n         in adSipTrunkRegistrationAlarmSipIdentity and \n         adSipTrunkRegistrationAlarmRegistrar respectively. The \n         adSipTrunkRegistrationAlarmTimestamp indicates when this condition \n         occurred and not necessarily when the trap was sent. ')
adSipRegistrationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12))
adSipRegistrationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1))
adSipRegistrationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2))
adSipRegistrationFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationFullCompliance = adSipRegistrationFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 2 of the adGenAosSipRegistration MIB. When this MIB is \n        fully implemented, then such an implementation can claim\n        full compliance.')
adSipRegistrationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationGroup = adSipRegistrationNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationNotificationGroup.setDescription('This group contains notifications about SIP registration conditions.')
adSipRegistrationNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationUtilityGroup = adSipRegistrationNotificationUtilityGroup.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationNotificationUtilityGroup.setDescription('A collection of objects accessible only for notifications.')
adSipRegistrationStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 3)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationStatus"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrarIpAddress"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationGrantTime"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationExpireTime"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSuccesses"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationFailures"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRequests"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationChallenges"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRollovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationStatisticsGroup = adSipRegistrationStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: adSipRegistrationStatisticsGroup.setDescription('A collection of readable objects for SIP registration statistics.')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-REGISTRATION", adSipTrunkRegistrationTable=adSipTrunkRegistrationTable, adSipTrunkRegistrationFailures=adSipTrunkRegistrationFailures, adSipTrunkRegistrationAlarmTrunkIdentity=adSipTrunkRegistrationAlarmTrunkIdentity, adSipTrunkRegistrarIpAddress=adSipTrunkRegistrarIpAddress, adSipTrunkRegistrationStatus=adSipTrunkRegistrationStatus, adSipRegistrationNotificationGroup=adSipRegistrationNotificationGroup, adSipTrunkRegistrationTableIndex=adSipTrunkRegistrationTableIndex, adSipTrunkRegistrationRequests=adSipTrunkRegistrationRequests, adSipTrunkRegistrationChallenges=adSipTrunkRegistrationChallenges, adSipTrunkRegistrationGrantTime=adSipTrunkRegistrationGrantTime, adSipRegistrationCompliances=adSipRegistrationCompliances, adSipTrunkRegistrationEntry=adSipTrunkRegistrationEntry, adSipTrunkRegistrationSipIdentity=adSipTrunkRegistrationSipIdentity, adSipRegistrationConformance=adSipRegistrationConformance, adSipTrunkRegistrationSuccesses=adSipTrunkRegistrationSuccesses, adSipTrunkRegistrationTrunkIdentity=adSipTrunkRegistrationTrunkIdentity, adSipTrunkRegistrationAlarm=adSipTrunkRegistrationAlarm, adSipRegistration=adSipRegistration, adSipRegistrationGroups=adSipRegistrationGroups, adSipRegistrationStatisticsGroup=adSipRegistrationStatisticsGroup, adGenAOSSipRegistration=adGenAOSSipRegistration, adSipRegistrationNotificationUtilityGroup=adSipRegistrationNotificationUtilityGroup, adSipRegistrationTraps=adSipRegistrationTraps, adSipTrunkRegistrationAlarmSipIdentity=adSipTrunkRegistrationAlarmSipIdentity, PYSNMP_MODULE_ID=adGenAOSSipRegistration, adSipTrunkRegistrationRollovers=adSipTrunkRegistrationRollovers, adSipTrunkRegistrationAlarmTimestamp=adSipTrunkRegistrationAlarmTimestamp, adSipRegistrationFullCompliance=adSipRegistrationFullCompliance, adSipTrunkRegistrationExpireTime=adSipTrunkRegistrationExpireTime, adSipTrunkRegistrationAlarmRegistrar=adSipTrunkRegistrationAlarmRegistrar)
