#
# PySNMP MIB module CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ucopia/CONTROLLER-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:55 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, iso, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, IpAddress, NotificationType, ModuleIdentity, Integer32, Counter64, Unsigned32, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "IpAddress", "NotificationType", "ModuleIdentity", "Integer32", "Counter64", "Unsigned32", "ObjectIdentity", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ucopia = ModuleIdentity((1, 3, 6, 1, 4, 1, 31218))
ucopia.setRevisions(('2017-01-24 00:00',))
if mibBuilder.loadTexts: ucopia.setLastUpdated('201701240000Z')
if mibBuilder.loadTexts: ucopia.setOrganization('www.ucopia.com')
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
servicesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 31218, 1, 1, 2)).setObjects(("CONTROLLER-MIB", "webServerService"), ("CONTROLLER-MIB", "sqlServerService"), ("CONTROLLER-MIB", "urlSnifferService"), ("CONTROLLER-MIB", "portalService"), ("CONTROLLER-MIB", "webProxyService"), ("CONTROLLER-MIB", "autodisconnectService"), ("CONTROLLER-MIB", "printingServerService"), ("CONTROLLER-MIB", "dhcpServerService"), ("CONTROLLER-MIB", "dnsServerService"), ("CONTROLLER-MIB", "staticIpManagerService"), ("CONTROLLER-MIB", "highAvailabilityService"), ("CONTROLLER-MIB", "ldapDirectoryService"), ("CONTROLLER-MIB", "ldapReplicationManagerService"), ("CONTROLLER-MIB", "timeServerService"), ("CONTROLLER-MIB", "radiusServerService"), ("CONTROLLER-MIB", "sambaService"), ("CONTROLLER-MIB", "sshService"), ("CONTROLLER-MIB", "syslogService"), ("CONTROLLER-MIB", "usersLogService"), ("CONTROLLER-MIB", "pmsClientService"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    servicesGroup = servicesGroup.setStatus('current')
notificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 31218, 1, 1, 3)).setObjects(("CONTROLLER-MIB", "ucpServiceFaultStateNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    notificationsGroup = notificationsGroup.setStatus('current')
ucpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 31218, 1, 2, 2)).setObjects(("CONTROLLER-MIB", "statesGroup"), ("CONTROLLER-MIB", "servicesGroup"), ("CONTROLLER-MIB", "notificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ucpCompliance = ucpCompliance.setStatus('current')
totalConnectedUsers = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalConnectedUsers.setStatus('current')
debugValue = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: debugValue.setStatus('current')
cpuTemperature = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuTemperature.setStatus('current')
diskTemperature = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
licenseUsers = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseUsers.setStatus('current')
sysObjectDescription = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectDescription.setStatus('current')
highAvailabilityStatus = MibScalar((1, 3, 6, 1, 4, 1, 31218, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 0), ("master", 1), ("active", 2), ("passive", 3), ("fault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityStatus.setStatus('current')
webServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webServerService.setStatus('current')
sqlServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sqlServerService.setStatus('current')
urlSnifferService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: urlSnifferService.setStatus('current')
portalService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portalService.setStatus('current')
webProxyService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: webProxyService.setStatus('current')
autodisconnectService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: autodisconnectService.setStatus('current')
printingServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: printingServerService.setStatus('current')
dhcpServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpServerService.setStatus('current')
dnsServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dnsServerService.setStatus('current')
staticIpManagerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: staticIpManagerService.setStatus('current')
highAvailabilityService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailabilityService.setStatus('current')
ldapDirectoryService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldapDirectoryService.setStatus('current')
ldapReplicationManagerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldapReplicationManagerService.setStatus('current')
timeServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeServerService.setStatus('current')
radiusServerService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: radiusServerService.setStatus('current')
sambaService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sambaService.setStatus('current')
sshService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshService.setStatus('current')
syslogService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogService.setStatus('current')
usersLogService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usersLogService.setStatus('current')
pmsClientService = MibScalar((1, 3, 6, 1, 4, 1, 31218, 4, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("stopped", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmsClientService.setStatus('current')
ucpServiceFaultStateNotification = NotificationType((1, 3, 6, 1, 4, 1, 31218, 2, 0, 1))
if mibBuilder.loadTexts: ucpServiceFaultStateNotification.setStatus('current')
mibBuilder.exportSymbols("CONTROLLER-MIB", ucpMIBGroups=ucpMIBGroups, ucpNotifications=ucpNotifications, dnsServerService=dnsServerService, syslogService=syslogService, diskTemperature=diskTemperature, radiusServerService=radiusServerService, ucpServiceFaultStateNotification=ucpServiceFaultStateNotification, ucpNotificationPrefix=ucpNotificationPrefix, staticIpManagerService=staticIpManagerService, servicesGroup=servicesGroup, totalConnectedUsers=totalConnectedUsers, sshService=sshService, webProxyService=webProxyService, sambaService=sambaService, ucopia=ucopia, pmsClientService=pmsClientService, printingServerService=printingServerService, autodisconnectService=autodisconnectService, usersLogService=usersLogService, highAvailabilityStatus=highAvailabilityStatus, portalService=portalService, serviceStatus=serviceStatus, ldapReplicationManagerService=ldapReplicationManagerService, ucpState=ucpState, timeServerService=timeServerService, ucpMIBCompliances=ucpMIBCompliances, cpuTemperature=cpuTemperature, licenseUsers=licenseUsers, highAvailabilityService=highAvailabilityService, statesGroup=statesGroup, urlSnifferService=urlSnifferService, ucpCompliance=ucpCompliance, sqlServerService=sqlServerService, ucpMIBConformance=ucpMIBConformance, sysObjectDescription=sysObjectDescription, debugValue=debugValue, notificationsGroup=notificationsGroup, ldapDirectoryService=ldapDirectoryService, webServerService=webServerService, PYSNMP_MODULE_ID=ucopia, dhcpServerService=dhcpServerService)
