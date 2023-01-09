#
# PySNMP MIB module MITEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:34:15 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Bits, NotificationType, Counter32, ObjectIdentity, Integer32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, enterprises, iso, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "Counter32", "ObjectIdentity", "Integer32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "enterprises", "iso", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027))
mitel.setRevisions(('2014-02-11 12:00', '2011-07-14 00:00', '2006-01-01 00:00', '2005-04-12 21:34', '2004-02-23 00:00', '1999-02-23 00:00', '1996-04-26 00:00',))
if mibBuilder.loadTexts: mitel.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitel.setOrganization('MITEL Networks Corporation')
class MitelIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dnic", 1))

class MitelNotifyTransportType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mitelNotifTransV1Trap", 1), ("mitelNotifTransV2Trap", 2), ("mitelNotifTransInform", 3))

mitelIdentification = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1))
if mibBuilder.loadTexts: mitelIdentification.setStatus('current')
mitelExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 2))
if mibBuilder.loadTexts: mitelExperimental.setStatus('current')
mitelExtensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 3))
if mibBuilder.loadTexts: mitelExtensions.setStatus('current')
mitelProprietary = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4))
if mibBuilder.loadTexts: mitelProprietary.setStatus('current')
mitelConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5))
if mibBuilder.loadTexts: mitelConformance.setStatus('current')
mitelIdMgmtPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 1))
if mibBuilder.loadTexts: mitelIdMgmtPlatforms.setStatus('current')
mitelIdCallServers = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2))
if mibBuilder.loadTexts: mitelIdCallServers.setStatus('current')
mitelIdTerminals = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 3))
if mibBuilder.loadTexts: mitelIdTerminals.setStatus('current')
mitelIdInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 4))
if mibBuilder.loadTexts: mitelIdInterfaces.setStatus('current')
mitelIdCtiPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 5))
if mibBuilder.loadTexts: mitelIdCtiPlatforms.setStatus('current')
mitelIdApplicationPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6))
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setStatus('current')
mitelIdCsMc2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 1))
if mibBuilder.loadTexts: mitelIdCsMc2.setStatus('current')
mitelIdCs2000Light = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 2))
if mibBuilder.loadTexts: mitelIdCs2000Light.setStatus('current')
mitelIdCsIpera3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 3))
if mibBuilder.loadTexts: mitelIdCsIpera3000.setStatus('current')
mitelExtInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 3, 2))
if mibBuilder.loadTexts: mitelExtInterfaces.setStatus('current')
mitelIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 1027, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfNumber.setStatus('current')
mitelIfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2), )
if mibBuilder.loadTexts: mitelIfTable.setStatus('current')
mitelIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIfTableEntry.setStatus('current')
mitelIfTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1), MitelIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfTblType.setStatus('current')
mitelPropApplications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1))
if mibBuilder.loadTexts: mitelPropApplications.setStatus('current')
mitelPropTransmission = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 2))
if mibBuilder.loadTexts: mitelPropTransmission.setStatus('current')
mitelPropProtocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 3))
if mibBuilder.loadTexts: mitelPropProtocols.setStatus('current')
mitelPropUtilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 4))
if mibBuilder.loadTexts: mitelPropUtilities.setStatus('current')
mitelPropHardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 5))
if mibBuilder.loadTexts: mitelPropHardware.setStatus('current')
mitelPropNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 6))
if mibBuilder.loadTexts: mitelPropNotifications.setStatus('current')
mitelPropReset = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 7))
if mibBuilder.loadTexts: mitelPropReset.setStatus('current')
mitelPropCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9))
if mibBuilder.loadTexts: mitelPropCommon.setStatus('current')
mitelAppCallServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1))
if mibBuilder.loadTexts: mitelAppCallServer.setStatus('current')
mitelConfCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 1))
if mibBuilder.loadTexts: mitelConfCompliances.setStatus('current')
mitelConfGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2))
if mibBuilder.loadTexts: mitelConfGroups.setStatus('current')
mitelGrpCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1))
if mibBuilder.loadTexts: mitelGrpCommon.setStatus('current')
mitelGrpCs2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3))
if mibBuilder.loadTexts: mitelGrpCs2000.setStatus('current')
mitelGrpIpera3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 4))
if mibBuilder.loadTexts: mitelGrpIpera3000.setStatus('current')
mitelConfAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 3))
if mibBuilder.loadTexts: mitelConfAgents.setStatus('current')
mitelComplMitel = ModuleCompliance((1, 3, 6, 1, 4, 1, 1027, 5, 1, 1)).setObjects(("MITEL-MIB", "mitelGrpCmnInterfaces"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelComplMitel = mitelComplMitel.setStatus('current')
mitelGrpCmnInterfaces = ObjectGroup((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6)).setObjects(("MITEL-MIB", "mitelIfNumber"), ("MITEL-MIB", "mitelIfTblType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelGrpCmnInterfaces = mitelGrpCmnInterfaces.setStatus('current')
mibBuilder.exportSymbols("MITEL-MIB", mitel=mitel, MitelIfType=MitelIfType, mitelIdCtiPlatforms=mitelIdCtiPlatforms, mitelIdApplicationPlatforms=mitelIdApplicationPlatforms, mitelIdInterfaces=mitelIdInterfaces, mitelPropProtocols=mitelPropProtocols, mitelIdTerminals=mitelIdTerminals, mitelIfTableEntry=mitelIfTableEntry, mitelIdentification=mitelIdentification, mitelIfTable=mitelIfTable, mitelPropHardware=mitelPropHardware, mitelExtensions=mitelExtensions, mitelExperimental=mitelExperimental, MitelNotifyTransportType=MitelNotifyTransportType, mitelIdMgmtPlatforms=mitelIdMgmtPlatforms, mitelConfAgents=mitelConfAgents, mitelIdCs2000Light=mitelIdCs2000Light, mitelIdCallServers=mitelIdCallServers, mitelIdCsMc2=mitelIdCsMc2, mitelPropApplications=mitelPropApplications, mitelPropReset=mitelPropReset, mitelExtInterfaces=mitelExtInterfaces, mitelPropCommon=mitelPropCommon, mitelConfCompliances=mitelConfCompliances, mitelPropTransmission=mitelPropTransmission, mitelProprietary=mitelProprietary, mitelGrpCommon=mitelGrpCommon, mitelConfGroups=mitelConfGroups, mitelGrpCs2000=mitelGrpCs2000, mitelGrpIpera3000=mitelGrpIpera3000, mitelPropUtilities=mitelPropUtilities, mitelComplMitel=mitelComplMitel, mitelIfTblType=mitelIfTblType, mitelIfNumber=mitelIfNumber, mitelGrpCmnInterfaces=mitelGrpCmnInterfaces, mitelIdCsIpera3000=mitelIdCsIpera3000, mitelPropNotifications=mitelPropNotifications, mitelAppCallServer=mitelAppCallServer, PYSNMP_MODULE_ID=mitel, mitelConformance=mitelConformance)
