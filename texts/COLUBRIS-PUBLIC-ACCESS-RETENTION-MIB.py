#
# PySNMP MIB module COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 20:23:08 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSIDOrNone, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSIDOrNone")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Integer32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, iso, Gauge32, NotificationType, Unsigned32, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "iso", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "ModuleIdentity")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
colubrisPublicAccessRetentionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 15))
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setLastUpdated('200410280000Z')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setDescription('Colubris Networks Public Access MIB.')
colubrisPublicAccessRetentionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1))
publicAccessRetentionSessionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1))
publicAccessRetentionPeriodicStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2))
publicAccessRetentionSessionsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxCount.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxCount.setDescription('The maximum number of entries inside the publicAccessRetentionSessionTable.\n                 The maximum value for this is 250% the maximum number of users configured inside the product.')
publicAccessRetentionSessionsMaxTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxTime.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxTime.setDescription("The maximum number of seconds for an entry to remain in the table.  When expired the\n                 session's state changes to Unassigned.")
publicAccessRetentionSessionTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3), )
if mibBuilder.loadTexts: publicAccessRetentionSessionTable.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionTable.setDescription('A table containing information about existing or past authenticated\n                 user sessions.')
publicAccessRetentionSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionIndex"))
if mibBuilder.loadTexts: publicAccessRetentionSessionEntry.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionEntry.setDescription('Information about a particular authenticated user session.\n                 publicAccessRetentionSessionIndex - Uniquely identifies a session in the\n                                                     table.')
publicAccessRetentionSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessRetentionSessionIndex.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionIndex.setDescription('Index of a session in the publicAccessRetentionSessionTable.')
publicAccessRetentionSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unassigned", 0), ("connected", 2), ("reconnecting", 3), ("disconnecting", 4), ("disconnected", 5), ("disconnectingAdministrative", 6), ("disconnectedAdministrative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionState.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionState.setDescription("Indicates the current state of the user's session.")
publicAccessRetentionSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionUserName.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionUserName.setDescription("Indicates the last user's name used for RADIUS authentication.")
publicAccessRetentionSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStartTime.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionStartTime.setDescription('Indicates when this user session was started.')
publicAccessRetentionSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionDuration.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionDuration.setDescription("Indicates how long the user's session has been active.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.")
publicAccessRetentionSessionStationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStationIpAddress.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionStationIpAddress.setDescription("Indicates the user's IP address.")
publicAccessRetentionSessionPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsSent.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsSent.setDescription('Indicates the total number of IP packets sent by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
publicAccessRetentionSessionPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsReceived.setDescription('Indicates the total number of IP packets received by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
publicAccessRetentionSessionBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesSent.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesSent.setDescription('Indicates the total number of bytes sent by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
publicAccessRetentionSessionBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesReceived.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesReceived.setDescription('Indicates the total number of bytes received by the user.\n                 When this counter reaches its maximum value, it wraps\n                 around and starts increasing again from zero.')
publicAccessRetentionSessionSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 11), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionSSID.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionSSID.setDescription("Indicates the user's Access Point SSID (ONLY when\n                 Location-aware is enabled and properly configured).\n                 If this information is not available, a zero-length\n                 string will be returned.")
publicAccessRetentionPeriodicStatsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsMaxCount.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsMaxCount.setDescription('Specifies the maximum number of periods to keep inside the table.')
publicAccessRetentionPeriodicStatsDuration = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsDuration.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsDuration.setDescription('Specifies the amount of time for a period of an entry inside the table.\n                 Changing the value will erase the table contents.')
publicAccessRetentionPeriodTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3), )
if mibBuilder.loadTexts: publicAccessRetentionPeriodTable.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodTable.setDescription("A table containing statistics information about number of\n                 authentication user's sessions pending and terminated.")
publicAccessRetentionPeriodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodIndex"))
if mibBuilder.loadTexts: publicAccessRetentionPeriodEntry.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodEntry.setDescription('Statistics information about the number of authenticated user sessions\n                 in a given period of time.')
publicAccessRetentionPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999)))
if mibBuilder.loadTexts: publicAccessRetentionPeriodIndex.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodIndex.setDescription('Index of a statistics period.')
publicAccessRetentionPeriodStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStartTime.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodStartTime.setDescription("Indicates the start time for the statistical period.\n                 If zero, then the period doesn't contains valid information.")
publicAccessRetentionPeriodStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStopTime.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodStopTime.setDescription('Indicates the stop time for the statistical period.\n                 If zero, the period is not terminated yet.')
publicAccessRetentionPeriodHighestSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodHighestSessionCount.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodHighestSessionCount.setDescription('Indicates the highest number of simultaneous authenticated user sessions within\n                 this time period.')
publicAccessRetentionPeriodTotalSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodTotalSessionCount.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionPeriodTotalSessionCount.setDescription("Indicates the total number of authenticated user's session within this time period.")
publicAccessRetentionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2))
publicAccessRetentionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0))
publicAccessRetentionSessionMaxCountReachedTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"))
if mibBuilder.loadTexts: publicAccessRetentionSessionMaxCountReachedTrap.setStatus('current')
if mibBuilder.loadTexts: publicAccessRetentionSessionMaxCountReachedTrap.setDescription('This notification is sent whenever the number of session exceed the\n                 value of publicAccessRetentionSessionsMaxCount.')
colubrisPublicAccessRetentionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3))
colubrisPublicAccessRetentionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1))
colubrisPublicAccessRetentionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2))
colubrisPublicAccessRetentionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionSessionsMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionPeriodicStatsMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionMIBCompliance = colubrisPublicAccessRetentionMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIBCompliance.setDescription('The compliance statement for entities which implement\n                 the Colubris Public Access Retention MIB.')
colubrisPublicAccessRetentionSessionsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionState"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionUserName"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStartTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionDuration"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStationIpAddress"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsSent"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsReceived"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesSent"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesReceived"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionSSID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionSessionsMIBGroup = colubrisPublicAccessRetentionSessionsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionSessionsMIBGroup.setDescription('A collection of objects providing the Public Access Retention Sessions MIB\n                 capability.')
colubrisPublicAccessRetentionPeriodicStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 2)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsDuration"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStartTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStopTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodHighestSessionCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodTotalSessionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionPeriodicStatsMIBGroup = colubrisPublicAccessRetentionPeriodicStatsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionPeriodicStatsMIBGroup.setDescription('A collection of objects providing the Public Access Retention PeriodicStats MIB\n                 capability.')
colubrisPublicAccessRetentionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 3)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionMaxCountReachedTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionNotificationGroup = colubrisPublicAccessRetentionNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", publicAccessRetentionSessionStationIpAddress=publicAccessRetentionSessionStationIpAddress, publicAccessRetentionSessionEntry=publicAccessRetentionSessionEntry, colubrisPublicAccessRetentionMIBConformance=colubrisPublicAccessRetentionMIBConformance, colubrisPublicAccessRetentionMIBGroups=colubrisPublicAccessRetentionMIBGroups, publicAccessRetentionSessionBytesSent=publicAccessRetentionSessionBytesSent, publicAccessRetentionPeriodEntry=publicAccessRetentionPeriodEntry, PYSNMP_MODULE_ID=colubrisPublicAccessRetentionMIB, publicAccessRetentionPeriodTable=publicAccessRetentionPeriodTable, publicAccessRetentionSessionState=publicAccessRetentionSessionState, colubrisPublicAccessRetentionPeriodicStatsMIBGroup=colubrisPublicAccessRetentionPeriodicStatsMIBGroup, publicAccessRetentionSessionsGroup=publicAccessRetentionSessionsGroup, publicAccessRetentionSessionSSID=publicAccessRetentionSessionSSID, publicAccessRetentionPeriodTotalSessionCount=publicAccessRetentionPeriodTotalSessionCount, publicAccessRetentionPeriodHighestSessionCount=publicAccessRetentionPeriodHighestSessionCount, publicAccessRetentionSessionStartTime=publicAccessRetentionSessionStartTime, publicAccessRetentionMIBNotifications=publicAccessRetentionMIBNotifications, colubrisPublicAccessRetentionNotificationGroup=colubrisPublicAccessRetentionNotificationGroup, publicAccessRetentionSessionPacketsSent=publicAccessRetentionSessionPacketsSent, publicAccessRetentionSessionUserName=publicAccessRetentionSessionUserName, colubrisPublicAccessRetentionMIBObjects=colubrisPublicAccessRetentionMIBObjects, publicAccessRetentionMIBNotificationPrefix=publicAccessRetentionMIBNotificationPrefix, publicAccessRetentionPeriodicStatsGroup=publicAccessRetentionPeriodicStatsGroup, colubrisPublicAccessRetentionSessionsMIBGroup=colubrisPublicAccessRetentionSessionsMIBGroup, publicAccessRetentionSessionsMaxCount=publicAccessRetentionSessionsMaxCount, publicAccessRetentionSessionMaxCountReachedTrap=publicAccessRetentionSessionMaxCountReachedTrap, publicAccessRetentionPeriodStopTime=publicAccessRetentionPeriodStopTime, colubrisPublicAccessRetentionMIBCompliances=colubrisPublicAccessRetentionMIBCompliances, publicAccessRetentionSessionTable=publicAccessRetentionSessionTable, publicAccessRetentionSessionBytesReceived=publicAccessRetentionSessionBytesReceived, publicAccessRetentionSessionPacketsReceived=publicAccessRetentionSessionPacketsReceived, publicAccessRetentionPeriodIndex=publicAccessRetentionPeriodIndex, publicAccessRetentionPeriodicStatsDuration=publicAccessRetentionPeriodicStatsDuration, publicAccessRetentionPeriodicStatsMaxCount=publicAccessRetentionPeriodicStatsMaxCount, colubrisPublicAccessRetentionMIB=colubrisPublicAccessRetentionMIB, publicAccessRetentionSessionIndex=publicAccessRetentionSessionIndex, colubrisPublicAccessRetentionMIBCompliance=colubrisPublicAccessRetentionMIBCompliance, publicAccessRetentionSessionsMaxTime=publicAccessRetentionSessionsMaxTime, publicAccessRetentionPeriodStartTime=publicAccessRetentionPeriodStartTime, publicAccessRetentionSessionDuration=publicAccessRetentionSessionDuration)
