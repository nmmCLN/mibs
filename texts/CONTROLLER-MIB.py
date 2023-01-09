#
# PySNMP MIB module CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ucopia/CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:38:21 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
enterprises, Counter32, IpAddress, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Bits, Counter64, ObjectIdentity, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucopia = ModuleIdentity((1, 3, 6, 1, 4, 1, 31218))
ucopia.setRevisions(('2017-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ucopia.setRevisionsDescriptions(('The MIB module for SNMP variables specific to UCOPIA controller.',))
if mibBuilder.loadTexts: ucopia.setLastUpdated('201701240000Z')
if mibBuilder.loadTexts: ucopia.setOrganization('www.ucopia.com')
if mibBuilder.loadTexts: ucopia.setContactInfo('UCOPIA Communications\n\t\tpostal: 201, avenue Pierre Brossolette\n\t\t\t\t92120 MONTROUGE, France\n\t\temail:  contactus@ucopia.com')
if mibBuilder.loadTexts: ucopia.setDescription('Re-design notifications')
ucpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 1))
ucpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 2))
ucpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 1, 1))
ucpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 1, 2))
ucpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 2, 0))
ucpState = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 3))
serviceStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 31218, 4))
statesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 31218, 1, 1, 1)).setObjects(("CONTROLLER-MIB", "totalConnectedUsers"), ("CONTROLLER-MIB", "debugValue"), ("CONTROLLER-MIB", "cpuTemperature"), ("CONTROLLER-MIB", "diskTemperature"), ("CONTROLLER-MIB", "licenseUsers"), ("CONTROLLER-MIB", "sysObjectDescription"), ("CONTROLLER-MIB", "highAvailabilityStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    statesGroup = statesGroup.setStatus('current')
if mibBuilder.loadTexts: statesGroup.setDescription('The objects relating to controller states.')
servicesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 31218, 1, 1, 2)).setObjects(("CONTROLLER-MIB", "webServerService"), ("CONTROLLER-MIB", "sqlServerService"), ("CONTROLLER-MIB", "urlSnifferService"), ("CONTROLLER-MIB", "portalService"), ("CONTROLLER-MIB", "webProxyService"), ("CONTROLLER-MIB", "autodisconnectService"), ("CONTROLLER-MIB", "printingServerService"), ("CONTROLLER-MIB", "dhcpServerService"), ("CONTROLLER-MIB", "dnsServerService"), ("CONTROLLER-MIB", "staticIpManagerService"), ("CONTROLLER-MIB", "highAvailabilityService"), ("CONTROLLER-MIB", "ldapDirectoryService"), ("CONTROLLER-MIB", "ldapReplicationManagerService"), ("CONTROLLER-MIB", "timeServerService"), ("CONTROLLER-MIB", "radiusServerService"), ("CONTROLLER-MIB", "sambaService"), ("CONTROLLER-MIB", "sshService"), ("CONTROLLER-MIB", "syslogService"), ("CONTROLLER-MIB", "usersLogService"), ("CONTROLLER-MIB", "pmsClientService"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    servicesGroup = servicesGroup.setStatus('current')
if mibBuilder.loadTexts: servicesGroup.setDescription('The objects relating to controller services.')
notificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 31218, 1, 1, 3)).setObjects(("CONTROLLER-MIB", "ucpServiceFaultStateNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationsGroup = notificationsGroup.setStatus('current')
if mibBuilder.loadTexts: notificationsGroup.setDescription('The notifications relating to the services status of the controller.')
ucpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 31218, 1, 2, 2)).setObjects(("CONTROLLER-MIB", "statesGroup"), ("CONTROLLER-MIB", "servicesGroup"), ("CONTROLLER-MIB", "notificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ucpCompliance = ucpCompliance.setStatus('current')
if mibBuilder.loadTexts: ucpCompliance.setDescription('The compliance statement for the controller MIB.')
totalConnectedUsers = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalConnectedUsers.setStatus('current')
if mibBuilder.loadTexts: totalConnectedUsers.setDescription('A value which indicates the number of connected users on this controller.')
debugValue = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: debugValue.setStatus('current')
if mibBuilder.loadTexts: debugValue.setDescription('A value which indicates the debug level.\n\t\tNumerical\tSeverity\n\t\t0\tEmergency: system is unusable\n\t\t1\tAlert: action must be taken immediately\n\t\t2\tCritical: critical conditions\n\t\t3\tError: error conditions\n\t\t4\tWarning: warning conditions\n\t\t5\tNotice: normal but significant condition\n\t\t6\tInformational: informational messages\n\t\t7\tDebug: debug-level messages')
cpuTemperature = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTemperature.setStatus('current')
if mibBuilder.loadTexts: cpuTemperature.setDescription('Processor temperature (in degree Celsius)')
diskTemperature = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
if mibBuilder.loadTexts: diskTemperature.setDescription('Disk temperature (in degree Celsius)')
licenseUsers = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseUsers.setStatus('current')
if mibBuilder.loadTexts: licenseUsers.setDescription('The number of users that the license allow to be connected simulteaneously.')
sysObjectDescription = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectDescription.setStatus('current')
if mibBuilder.loadTexts: sysObjectDescription.setDescription("The description of 'what kind of the box' is being managed.")
highAvailabilityStatus = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 0), ("master", 1), ("active", 2), ("passive", 3), ("fault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityStatus.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityStatus.setDescription('Indicates the controller current status in high availability cluster\n\t\t(0) Standalone\n\t\t(1) Master (HA)\n\t\t(2) Active node (HA)\n\t\t(3) Passive node (HA)\n\t\t(4) FAULT (HA)')
webServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webServerService.setStatus('current')
if mibBuilder.loadTexts: webServerService.setDescription('Indicates the status of Web Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
sqlServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sqlServerService.setStatus('current')
if mibBuilder.loadTexts: sqlServerService.setDescription('Indicates the status of SQL Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
urlSnifferService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: urlSnifferService.setStatus('current')
if mibBuilder.loadTexts: urlSnifferService.setDescription('Indicates the status of URL sniffer service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
portalService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portalService.setStatus('current')
if mibBuilder.loadTexts: portalService.setDescription('Indicates the status of Portal service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
webProxyService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webProxyService.setStatus('current')
if mibBuilder.loadTexts: webProxyService.setDescription('Indicates the status of Web Proxy service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
autodisconnectService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: autodisconnectService.setStatus('current')
if mibBuilder.loadTexts: autodisconnectService.setDescription('Indicates the status of Autodisconnect service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
printingServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: printingServerService.setStatus('current')
if mibBuilder.loadTexts: printingServerService.setDescription('Indicates the status of Printing Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
dhcpServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerService.setStatus('current')
if mibBuilder.loadTexts: dhcpServerService.setDescription('Indicates status of DHCP server.\n\t\t\t\t(1) running\tservice is running\n\t\t\t\t(2) stopped\tservice is stopped or crashed\n\t\t\t\t(3) disabled\tservice is disabled by configuration.')
dnsServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServerService.setStatus('current')
if mibBuilder.loadTexts: dnsServerService.setDescription('Indicates the status of DNS Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
staticIpManagerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: staticIpManagerService.setStatus('current')
if mibBuilder.loadTexts: staticIpManagerService.setDescription('Indicates the status of Static IP Manager service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
highAvailabilityService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityService.setStatus('current')
if mibBuilder.loadTexts: highAvailabilityService.setDescription('Indicates the status of High-Availability service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
ldapDirectoryService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldapDirectoryService.setStatus('current')
if mibBuilder.loadTexts: ldapDirectoryService.setDescription('Indicates the status of LDAP Directory service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
ldapReplicationManagerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldapReplicationManagerService.setStatus('current')
if mibBuilder.loadTexts: ldapReplicationManagerService.setDescription('Indicates the status of LDAP Replication Manager service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
timeServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeServerService.setStatus('current')
if mibBuilder.loadTexts: timeServerService.setDescription('Indicates the status of Time Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
radiusServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusServerService.setStatus('current')
if mibBuilder.loadTexts: radiusServerService.setDescription('Indicates the status of Radius Server service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
sambaService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sambaService.setStatus('current')
if mibBuilder.loadTexts: sambaService.setDescription('Indicates the status of Samba service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
sshService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshService.setStatus('current')
if mibBuilder.loadTexts: sshService.setDescription('Indicates the status of Ssh service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
syslogService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogService.setStatus('current')
if mibBuilder.loadTexts: syslogService.setDescription('Indicates the status of Syslog service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
usersLogService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usersLogService.setStatus('current')
if mibBuilder.loadTexts: usersLogService.setDescription('Indicates the status of Users Log service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
pmsClientService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmsClientService.setStatus('current')
if mibBuilder.loadTexts: pmsClientService.setDescription('Indicates the status of PMSClient service\n\t\t(1) Running, service is running\n\t\t(2) Stopped, service is stopped or crashed\n\t\t(3) Disabled, service is disabled by configuration.')
ucpServiceFaultStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 31218, 2, 0, 1))
if mibBuilder.loadTexts: ucpServiceFaultStateNotification.setStatus('current')
if mibBuilder.loadTexts: ucpServiceFaultStateNotification.setDescription('A notification, used to alert that a service has entered a fault state')
mibBuilder.exportSymbols("CONTROLLER-MIB", ucpMIBConformance=ucpMIBConformance, printingServerService=printingServerService, ucpServiceFaultStateNotification=ucpServiceFaultStateNotification, diskTemperature=diskTemperature, dhcpServerService=dhcpServerService, dnsServerService=dnsServerService, urlSnifferService=urlSnifferService, cpuTemperature=cpuTemperature, serviceStatus=serviceStatus, ucopia=ucopia, statesGroup=statesGroup, highAvailabilityStatus=highAvailabilityStatus, ucpNotifications=ucpNotifications, autodisconnectService=autodisconnectService, webServerService=webServerService, usersLogService=usersLogService, servicesGroup=servicesGroup, PYSNMP_MODULE_ID=ucopia, syslogService=syslogService, licenseUsers=licenseUsers, ucpNotificationPrefix=ucpNotificationPrefix, pmsClientService=pmsClientService, ucpMIBCompliances=ucpMIBCompliances, webProxyService=webProxyService, debugValue=debugValue, sambaService=sambaService, highAvailabilityService=highAvailabilityService, portalService=portalService, ldapDirectoryService=ldapDirectoryService, sysObjectDescription=sysObjectDescription, timeServerService=timeServerService, ucpCompliance=ucpCompliance, ucpMIBGroups=ucpMIBGroups, staticIpManagerService=staticIpManagerService, totalConnectedUsers=totalConnectedUsers, ldapReplicationManagerService=ldapReplicationManagerService, ucpState=ucpState, sshService=sshService, radiusServerService=radiusServerService, notificationsGroup=notificationsGroup, sqlServerService=sqlServerService)
