#
# PySNMP MIB module APSWINVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APSWINVENTORY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, IpAddress, TimeTicks, NotificationType, Counter32, Unsigned32, Bits, MibIdentifier, ModuleIdentity, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apSwInventoryModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 4))
apSwInventoryModule.setRevisions(('2012-07-13 00:00', '2014-06-26 00:00', '2019-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apSwInventoryModule.setRevisionsDescriptions(('Updated contact info', 'Updated Organization and Contact info.', 'Updated Description of apSwBootTable.',))
if mibBuilder.loadTexts: apSwInventoryModule.setLastUpdated('201905210000Z')
if mibBuilder.loadTexts: apSwInventoryModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apSwInventoryModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apSwInventoryModule.setDescription(' The software inventory MIB for Oracle Communications Acme Packet SBCs')
apSwInventoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1))
apSwInventoryBootObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1))
apSwInventoryCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2))
apSwBootTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1), )
if mibBuilder.loadTexts: apSwBootTable.setStatus('current')
if mibBuilder.loadTexts: apSwBootTable.setDescription('The table of booting software inventory. The inventory includes \n                 the boot software currently in use, and these previously being used. \n                 Please note that it is NOT an inventory of software images \n                 in any storage device.')
apSwBootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1), ).setIndexNames((0, "APSWINVENTORY-MIB", "apSwBootIndex"))
if mibBuilder.loadTexts: apSwBootEntry.setStatus('current')
if mibBuilder.loadTexts: apSwBootEntry.setDescription('An entry in the software inventory table')
apSwBootIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apSwBootIndex.setStatus('current')
if mibBuilder.loadTexts: apSwBootIndex.setDescription('Unique index for the software inventory table. \n\t\tIndex always begins at 1, and increases by 1. \n\t\tThe table length depends on the size of software inventory. \n\t\tThe index is not associated with any specific inventory entry')
apSwBootDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootDescr.setStatus('current')
if mibBuilder.loadTexts: apSwBootDescr.setDescription("Textual description of the software image.\n\t\tIt maybe file name, data and time this image was built,\n\t\tor the unique identifier of this software.\n\t\tExamples are: \n\t\t1.  boot image: 10.0.1.12/sd121p3.gz \n\t\tfor host address is 10.0.1.12, and image name is sd121p3.gz\n\t\t2. boot image: /tffs0/sd121p3.gz \n\t\tfor boot from flash 0, and image name is sd121p3.gz\n  \t\t3. boot loader: bank0:03/18/2004 10:58:25 \n\t\tfor boot from bank 0, and version is 'march 18 2003, 10:58:25'\n\t        4. boot loader: <card>:<version>")
apSwBootType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bootImage", 1), ("bootLoader", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootType.setStatus('current')
if mibBuilder.loadTexts: apSwBootType.setDescription('The software entity type')
apSwBootStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("currentUsing", 1), ("previousUsed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootStatus.setStatus('current')
if mibBuilder.loadTexts: apSwBootStatus.setDescription('The software entity status')
apSwCfgCurrentVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgCurrentVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgCurrentVersion.setDescription('current version of saved configuration')
apSwCfgRunningVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgRunningVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgRunningVersion.setDescription('current version of running configuration')
apSwCfgBackuptable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3), )
if mibBuilder.loadTexts: apSwCfgBackuptable.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackuptable.setDescription('The table of backup configuration files')
apSwCfgBackupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1), ).setIndexNames((0, "APSWINVENTORY-MIB", "apSwCfgBackupIndex"))
if mibBuilder.loadTexts: apSwCfgBackupEntry.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupEntry.setDescription('An entry in the backup configuration files table')
apSwCfgBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apSwCfgBackupIndex.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupIndex.setDescription('Unique index for the backup configuration files table. \n                Index always begins at 1, and increases by 1. \n                The table length depends on the size of backup configuration. \n                The index is not associated with any specific entry')
apSwCfgBackupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgBackupName.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupName.setDescription('Textual description of the condifuration file name.\n                Examples are: p1604, 063004-cfg')
apSwInventoryNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2))
apSwCfgNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1))
apSwCfgTrapPreviousVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apSwCfgTrapPreviousVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgTrapPreviousVersion.setDescription('The previous version before this trap happened')
apSwCfgTrapCurrentVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apSwCfgTrapCurrentVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgTrapCurrentVersion.setDescription('The current version after this trap happened')
apSwInventoryNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3))
apSwInventoryNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0))
apSwCfgActivateNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0, 1)).setObjects(("APSWINVENTORY-MIB", "apSwCfgTrapPreviousVersion"), ("APSWINVENTORY-MIB", "apSwCfgTrapCurrentVersion"))
if mibBuilder.loadTexts: apSwCfgActivateNotification.setStatus('current')
if mibBuilder.loadTexts: apSwCfgActivateNotification.setDescription('This trap is sent if <activate-config> is \n\t\tissued and configuration has been changed at runtime.')
apSwInventoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4))
apSwInventoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 1))
apSwInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2))
apSwInventoryNotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3))
apSwBootObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 1)).setObjects(("APSWINVENTORY-MIB", "apSwBootDescr"), ("APSWINVENTORY-MIB", "apSwBootType"), ("APSWINVENTORY-MIB", "apSwBootStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwBootObjectsGroup = apSwBootObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwBootObjectsGroup.setDescription('A collection of objects providing the software booting inventory')
apSwCfgObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 2)).setObjects(("APSWINVENTORY-MIB", "apSwCfgCurrentVersion"), ("APSWINVENTORY-MIB", "apSwCfgRunningVersion"), ("APSWINVENTORY-MIB", "apSwCfgBackupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwCfgObjectsGroup = apSwCfgObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwCfgObjectsGroup.setDescription('A collection of objects providing the configuraion files')
apSwInventoryNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3, 1)).setObjects(("APSWINVENTORY-MIB", "apSwCfgActivateNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryNotificationsGroup = apSwInventoryNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwInventoryNotificationsGroup.setDescription('A collection of notifications providing the change \n                  for software inventory.')
mibBuilder.exportSymbols("APSWINVENTORY-MIB", apSwBootObjectsGroup=apSwBootObjectsGroup, apSwInventoryNotificationsGroup=apSwInventoryNotificationsGroup, apSwInventoryNotificationObjects=apSwInventoryNotificationObjects, apSwCfgActivateNotification=apSwCfgActivateNotification, apSwCfgBackupIndex=apSwCfgBackupIndex, apSwInventoryCfgObjects=apSwInventoryCfgObjects, apSwCfgRunningVersion=apSwCfgRunningVersion, apSwBootDescr=apSwBootDescr, apSwInventoryConformance=apSwInventoryConformance, apSwBootType=apSwBootType, apSwCfgTrapPreviousVersion=apSwCfgTrapPreviousVersion, apSwCfgNotificationObjects=apSwCfgNotificationObjects, apSwCfgBackupName=apSwCfgBackupName, apSwInventoryGroups=apSwInventoryGroups, apSwCfgCurrentVersion=apSwCfgCurrentVersion, apSwInventoryCompliances=apSwInventoryCompliances, apSwInventoryMIBObjects=apSwInventoryMIBObjects, apSwBootIndex=apSwBootIndex, apSwCfgObjectsGroup=apSwCfgObjectsGroup, apSwBootStatus=apSwBootStatus, PYSNMP_MODULE_ID=apSwInventoryModule, apSwInventoryNotifications=apSwInventoryNotifications, apSwInventoryBootObjects=apSwInventoryBootObjects, apSwBootEntry=apSwBootEntry, apSwCfgBackuptable=apSwCfgBackuptable, apSwInventoryNotificationsGroups=apSwInventoryNotificationsGroups, apSwBootTable=apSwBootTable, apSwCfgBackupEntry=apSwCfgBackupEntry, apSwCfgTrapCurrentVersion=apSwCfgTrapCurrentVersion, apSwInventoryModule=apSwInventoryModule, apSwInventoryNotificationPrefix=apSwInventoryNotificationPrefix)
