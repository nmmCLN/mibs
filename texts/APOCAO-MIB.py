#
# PySNMP MIB module APOCAO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APOCAO-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
apEMSModule, = mibBuilder.importSymbols("APEMS-MIB", "apEMSModule")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, IpAddress, TimeTicks, NotificationType, Counter32, Unsigned32, Bits, MibIdentifier, ModuleIdentity, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
apOCAOModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7))
apOCAOModule.setRevisions(('2015-03-20 09:00', '2015-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apOCAOModule.setRevisionsDescriptions(('Updated contact info', 'Add new traps: apOCAONFcDeploymentFailure, \n                         apOCAONFcDeploymentFailureClear, \n                         apOCAONFcDUAvailabilityFailure, \n                         apOCAONFcDUAvailabilityFailureClear',))
if mibBuilder.loadTexts: apOCAOModule.setLastUpdated('201507100000Z')
if mibBuilder.loadTexts: apOCAOModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apOCAOModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\tsupport@oracle.com')
if mibBuilder.loadTexts: apOCAOModule.setDescription('The MIB for Oracle Communication Application Orchestrator (OCAO)')
apOCAOMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 1))
apOCAONotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2))
apOCAOSourceServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAOSourceServerAddress.setStatus('current')
if mibBuilder.loadTexts: apOCAOSourceServerAddress.setDescription('The address of the Oracle Communication Application Orchestrator (OCAO)')
apOCAOSourceServerName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAOSourceServerName.setStatus('current')
if mibBuilder.loadTexts: apOCAOSourceServerName.setDescription('The name (if available) of the Oracle Communication Application Orchestrator (OCAO)')
apOCAOFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAOFailureReason.setStatus('current')
if mibBuilder.loadTexts: apOCAOFailureReason.setDescription('The reason for failure.')
apOCAONFName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAONFName.setStatus('current')
if mibBuilder.loadTexts: apOCAONFName.setDescription('The name of the Network Function')
apOCAONFcGroupName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAONFcGroupName.setStatus('current')
if mibBuilder.loadTexts: apOCAONFcGroupName.setDescription('The name of the Network Function component group')
apOCAODUName = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apOCAODUName.setStatus('current')
if mibBuilder.loadTexts: apOCAODUName.setDescription('The name of the Deployment Unit')
apOCAONotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3))
apOCAONFcDeploymentStatusNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 1))
apOCAONFcDeploymentStatusNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 1, 0))
apOCAONFcDeploymentFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 1, 0, 1)).setObjects(("APOCAO-MIB", "apOCAOSourceServerAddress"), ("APOCAO-MIB", "apOCAONFName"), ("APOCAO-MIB", "apOCAONFcGroupName"), ("APOCAO-MIB", "apOCAODUName"), ("APOCAO-MIB", "apOCAOFailureReason"))
if mibBuilder.loadTexts: apOCAONFcDeploymentFailure.setStatus('current')
if mibBuilder.loadTexts: apOCAONFcDeploymentFailure.setDescription('The notification will be generated when a deployment of Network Function component fails.')
apOCAONFcDeploymentFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 1, 0, 2)).setObjects(("APOCAO-MIB", "apOCAOSourceServerAddress"), ("APOCAO-MIB", "apOCAONFName"), ("APOCAO-MIB", "apOCAONFcGroupName"), ("APOCAO-MIB", "apOCAODUName"))
if mibBuilder.loadTexts: apOCAONFcDeploymentFailureClear.setStatus('current')
if mibBuilder.loadTexts: apOCAONFcDeploymentFailureClear.setDescription('The notification will be generated to clear a prior apOCAONFcDeploymentFailure notification.')
apOCAOCapacityPlannerNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 2))
apOCAOCapacityPlannerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 2, 0))
apOCAONFcDUAvailabilityFailure = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 2, 0, 1)).setObjects(("APOCAO-MIB", "apOCAOSourceServerAddress"), ("APOCAO-MIB", "apOCAONFName"), ("APOCAO-MIB", "apOCAONFcGroupName"), ("APOCAO-MIB", "apOCAOFailureReason"))
if mibBuilder.loadTexts: apOCAONFcDUAvailabilityFailure.setStatus('current')
if mibBuilder.loadTexts: apOCAONFcDUAvailabilityFailure.setDescription('The notification will be generated when scale out operation fails due to lack of a available Deployment Unit for the Network Function component group.')
apOCAONFcDUAvailabilityFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 3, 2, 0, 2)).setObjects(("APOCAO-MIB", "apOCAOSourceServerAddress"), ("APOCAO-MIB", "apOCAONFName"), ("APOCAO-MIB", "apOCAONFcGroupName"))
if mibBuilder.loadTexts: apOCAONFcDUAvailabilityFailureClear.setStatus('current')
if mibBuilder.loadTexts: apOCAONFcDUAvailabilityFailureClear.setDescription('The notification will be generated to clear a prior apOCAONFcDUAvailabilityFailure notification.')
apOCAOModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4))
apOCAOGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4, 1))
apOCAONotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4, 2))
apOCAONotificationObjectsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4, 3))
apOCAODeploymentStatusNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4, 2, 1)).setObjects(("APOCAO-MIB", "apOCAONFcDeploymentFailure"), ("APOCAO-MIB", "apOCAONFcDeploymentFailureClear"), ("APOCAO-MIB", "apOCAONFcDUAvailabilityFailure"), ("APOCAO-MIB", "apOCAONFcDUAvailabilityFailureClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apOCAODeploymentStatusNotificationsGroup = apOCAODeploymentStatusNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apOCAODeploymentStatusNotificationsGroup.setDescription('Deployment status notifications generated by OCAO Server')
apOCAODeploymentStatusObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 8, 7, 4, 3, 1)).setObjects(("APOCAO-MIB", "apOCAONFName"), ("APOCAO-MIB", "apOCAONFcGroupName"), ("APOCAO-MIB", "apOCAODUName"), ("APOCAO-MIB", "apOCAOFailureReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apOCAODeploymentStatusObjectsGroup = apOCAODeploymentStatusObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apOCAODeploymentStatusObjectsGroup.setDescription('Objects for deployment status notifications.')
mibBuilder.exportSymbols("APOCAO-MIB", apOCAONFcDeploymentFailureClear=apOCAONFcDeploymentFailureClear, apOCAODeploymentStatusObjectsGroup=apOCAODeploymentStatusObjectsGroup, apOCAOSourceServerAddress=apOCAOSourceServerAddress, apOCAOCapacityPlannerNotifications=apOCAOCapacityPlannerNotifications, apOCAONotificationObjects=apOCAONotificationObjects, apOCAONFcDUAvailabilityFailure=apOCAONFcDUAvailabilityFailure, PYSNMP_MODULE_ID=apOCAOModule, apOCAOModule=apOCAOModule, apOCAONotificationsGroups=apOCAONotificationsGroups, apOCAOMIBObjects=apOCAOMIBObjects, apOCAONFcDeploymentStatusNotificationsPrefix=apOCAONFcDeploymentStatusNotificationsPrefix, apOCAOModuleConformance=apOCAOModuleConformance, apOCAODeploymentStatusNotificationsGroup=apOCAODeploymentStatusNotificationsGroup, apOCAONFName=apOCAONFName, apOCAONotificationObjectsGroups=apOCAONotificationObjectsGroups, apOCAONFcDUAvailabilityFailureClear=apOCAONFcDUAvailabilityFailureClear, apOCAODUName=apOCAODUName, apOCAONFcGroupName=apOCAONFcGroupName, apOCAONotifications=apOCAONotifications, apOCAONFcDeploymentFailure=apOCAONFcDeploymentFailure, apOCAONFcDeploymentStatusNotifications=apOCAONFcDeploymentStatusNotifications, apOCAOFailureReason=apOCAOFailureReason, apOCAOSourceServerName=apOCAOSourceServerName, apOCAOCapacityPlannerNotificationsPrefix=apOCAOCapacityPlannerNotificationsPrefix, apOCAOGroups=apOCAOGroups)
