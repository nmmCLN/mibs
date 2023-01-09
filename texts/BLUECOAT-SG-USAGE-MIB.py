#
# PySNMP MIB module BLUECOAT-SG-USAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-USAGE-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:50 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Counter64, MibIdentifier, iso, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "MibIdentifier", "iso", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Counter32", "NotificationType")
DisplayString, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention")
deviceUsageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 4))
deviceUsageMIB.setRevisions(('2013-07-11 03:00', '2008-01-16 03:00', '2007-12-07 03:00', '2002-11-06 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceUsageMIB.setRevisionsDescriptions(('Access level changes in deviceUsageTable.', 'Deprecated the usage trap in favour\n                         of using health monitoring.', 'Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceUsageMIB.setLastUpdated('201307110300Z')
if mibBuilder.loadTexts: deviceUsageMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceUsageMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceUsageMIB.setDescription('The usage MIB is used to monitor\n                         resource usage of the device.')
deviceUsageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1))
deviceUsageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2))
deviceUsageMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0))
class Percent(TextualConvention, Integer32):
    description = 'Percent value.'
    status = 'current'
    displayHint = 'd%'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class UsageStatus(TextualConvention, Integer32):
    description = 'Current status of the deviceUsagePercent.\n                ok    - value within limit.\n                high  - value surpassed high limit. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("high", 2))

deviceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1), )
if mibBuilder.loadTexts: deviceUsageTable.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTable.setDescription('This table lists the various resources that\n                         are available.')
deviceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-USAGE-MIB", "deviceUsageIndex"))
if mibBuilder.loadTexts: deviceUsageEntry.setStatus('current')
if mibBuilder.loadTexts: deviceUsageEntry.setDescription('A deviceUsage entry describes the\n                         present usage of a resource.')
deviceUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceUsageIndex.setStatus('current')
if mibBuilder.loadTexts: deviceUsageIndex.setDescription('An arbitrary value which uniquely identifies\n                         a resource.')
deviceUsageTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageTrapEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTrapEnabled.setDescription('This variable controls generation of deviceUsageTrap\n                         for this resource.\n                         When this variable is true(1), generation of\n                         deviceUsageTrap is enabled. When this variable is\n                         false(2), generation of deviceUsageTrap is disabled.\n                         The default start-up value is true(1).')
deviceUsageName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageName.setStatus('current')
if mibBuilder.loadTexts: deviceUsageName.setDescription('The textual name of the resource e.g. Disk.')
deviceUsagePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsagePercent.setStatus('current')
if mibBuilder.loadTexts: deviceUsagePercent.setDescription('Percent of resource in use.')
deviceUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageHigh.setStatus('current')
if mibBuilder.loadTexts: deviceUsageHigh.setDescription('Percent usage which a notification will be sent when\n                         the value is reached. For example, if deviceUsageHigh\n                         is set to 79 then notification will be send when the\n                         value changes from less than 79 to 79. The default is\n                         defined by the device for a particular resource.')
deviceUsageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 6), UsageStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageStatus.setStatus('current')
if mibBuilder.loadTexts: deviceUsageStatus.setDescription('Comparison of deviceUsagePercent with deviceUsageHigh.')
deviceUsageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 7), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUsageTime.setStatus('current')
if mibBuilder.loadTexts: deviceUsageTime.setDescription("Value of 'sysUpTime.0' at last resource reading.")
deviceUsageTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0, 1)).setObjects(("BLUECOAT-SG-USAGE-MIB", "deviceUsageName"), ("BLUECOAT-SG-USAGE-MIB", "deviceUsagePercent"), ("BLUECOAT-SG-USAGE-MIB", "deviceUsageStatus"))
if mibBuilder.loadTexts: deviceUsageTrap.setStatus('deprecated')
if mibBuilder.loadTexts: deviceUsageTrap.setDescription('A notification is sent when the deviceUsagePercent\n                         exceeds a threshold. This is no longer functional.\n                         Use health monitoring instead.')
mibBuilder.exportSymbols("BLUECOAT-SG-USAGE-MIB", deviceUsageTable=deviceUsageTable, deviceUsagePercent=deviceUsagePercent, deviceUsageStatus=deviceUsageStatus, deviceUsageTime=deviceUsageTime, Percent=Percent, deviceUsageMIBNotifications=deviceUsageMIBNotifications, deviceUsageHigh=deviceUsageHigh, deviceUsageTrapEnabled=deviceUsageTrapEnabled, deviceUsageMIB=deviceUsageMIB, deviceUsageMIBObjects=deviceUsageMIBObjects, deviceUsageMIBNotificationsPrefix=deviceUsageMIBNotificationsPrefix, deviceUsageTrap=deviceUsageTrap, PYSNMP_MODULE_ID=deviceUsageMIB, deviceUsageName=deviceUsageName, deviceUsageIndex=deviceUsageIndex, UsageStatus=UsageStatus, deviceUsageEntry=deviceUsageEntry)
