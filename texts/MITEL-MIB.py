#
# PySNMP MIB module MITEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:05 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, iso, Bits, Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, IpAddress, Counter32, ModuleIdentity, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "iso", "Bits", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027))
mitel.setRevisions(('2014-02-11 12:00', '2011-07-14 00:00', '2006-01-01 00:00', '2005-04-12 21:34', '2004-02-23 00:00', '1999-02-23 00:00', '1996-04-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitel.setRevisionsDescriptions(('The top-level MITEL MIB module.', 'Restoring the mitelIdCallServers from previous revision', 'To be consistent with all other products this MIB was\n                           sanitized.', 'Small mods to naming convention to be consistent.', 'MITEL-MIB Version 3.0.0.2 - Draft', 'MIB Version 2.0', 'MIB Version 1.0',))
if mibBuilder.loadTexts: mitel.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitel.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitel.setContactInfo('Standards Group,\n                           Postal:    MITEL Networks Corporation\n                           350 Legget Drive, PO Box 13089\n                           Kanata, Ontario\n                           Canada  K2K 2W7\n                           Tel: +1 613 592 2122\n                           Fax: +1 613 592 4784\n                           URL: www.mitel.com')
if mibBuilder.loadTexts: mitel.setDescription('Replace E-Mail: std@mitel.com with URL: www.mitel.com.')
class MitelIfType(TextualConvention, Integer32):
    description = 'The MITEL-defined interface type.\n                          Additions to this list must be provided\n                          by the MITEL Standards Group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dnic", 1))

class MitelNotifyTransportType(TextualConvention, Integer32):
    description = 'The method of transporting a notification\n                          to an interested manager.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mitelNotifTransV1Trap", 1), ("mitelNotifTransV2Trap", 2), ("mitelNotifTransInform", 3))

mitelIdentification = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1))
if mibBuilder.loadTexts: mitelIdentification.setStatus('current')
if mibBuilder.loadTexts: mitelIdentification.setDescription('The identification subtree. Leaves in this subtree are\n                           used for the sysObjectID field in the MIB-II system tree or\n                           other similar OID fields.')
mitelExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 2))
if mibBuilder.loadTexts: mitelExperimental.setStatus('current')
if mibBuilder.loadTexts: mitelExperimental.setDescription('The experimental MIB development subtree. The branches \n                           in this subtree should follow the format of the mitelProprietary \n                           subtree.')
mitelExtensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 3))
if mibBuilder.loadTexts: mitelExtensions.setStatus('current')
if mibBuilder.loadTexts: mitelExtensions.setDescription('The standards extension subtree. Used for extensions to \n                           any of the standard subtrees under the MIB-II subtree.')
mitelProprietary = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4))
if mibBuilder.loadTexts: mitelProprietary.setStatus('current')
if mibBuilder.loadTexts: mitelProprietary.setDescription('The managed information subtree. Leaves in this subtree \n                           are generic devices or protocols that can be managed.')
mitelConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5))
if mibBuilder.loadTexts: mitelConformance.setStatus('current')
if mibBuilder.loadTexts: mitelConformance.setDescription('The conformance subtree. Leaves in this subtree \n                           identify compliance grouping and requirements.')
mitelIdMgmtPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 1))
if mibBuilder.loadTexts: mitelIdMgmtPlatforms.setStatus('current')
if mibBuilder.loadTexts: mitelIdMgmtPlatforms.setDescription('Products used to manage MITEL equipment.')
mitelIdCallServers = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2))
if mibBuilder.loadTexts: mitelIdCallServers.setStatus('current')
if mibBuilder.loadTexts: mitelIdCallServers.setDescription('Products providing call processing capabilities.')
mitelIdTerminals = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 3))
if mibBuilder.loadTexts: mitelIdTerminals.setStatus('current')
if mibBuilder.loadTexts: mitelIdTerminals.setDescription('Desktop products.')
mitelIdInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 4))
if mibBuilder.loadTexts: mitelIdInterfaces.setStatus('current')
if mibBuilder.loadTexts: mitelIdInterfaces.setDescription('Products providing the interface between a call \n                           processing entity and a network or terminal.')
mitelIdCtiPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 5))
if mibBuilder.loadTexts: mitelIdCtiPlatforms.setStatus('current')
if mibBuilder.loadTexts: mitelIdCtiPlatforms.setDescription('Products providing computer-telephony integration \n                           capabilities.')
mitelIdApplicationPlatforms = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6))
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setStatus('current')
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setDescription('Products providing application-based platforms that\n                           provide value-added capabilities.')
mitelIdCsMc2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 1))
if mibBuilder.loadTexts: mitelIdCsMc2.setStatus('current')
if mibBuilder.loadTexts: mitelIdCsMc2.setDescription('The MC-2 Call Server.')
mitelIdCs2000Light = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 2))
if mibBuilder.loadTexts: mitelIdCs2000Light.setStatus('current')
if mibBuilder.loadTexts: mitelIdCs2000Light.setDescription('The Mitel SX-2000 LIGHT Call Server.')
mitelIdCsIpera3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 2, 3))
if mibBuilder.loadTexts: mitelIdCsIpera3000.setStatus('current')
if mibBuilder.loadTexts: mitelIdCsIpera3000.setDescription('The MITEL Networks 3300 ICP Call Server.')
mitelExtInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 3, 2))
if mibBuilder.loadTexts: mitelExtInterfaces.setStatus('current')
if mibBuilder.loadTexts: mitelExtInterfaces.setDescription('Proprietary extensions to the MIB-II subtree.')
mitelIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 1027, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfNumber.setStatus('current')
if mibBuilder.loadTexts: mitelIfNumber.setDescription('The number of MITEL proprietary interfaces \n                         (regardless of their current state) present on \n                         this system.')
mitelIfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2), )
if mibBuilder.loadTexts: mitelIfTable.setStatus('current')
if mibBuilder.loadTexts: mitelIfTable.setDescription('A list of interface entries.  The number of entries\n                         is given by the value of mitelIfNumber. The table \n                         consists of one row for each MITEL-specific interface,\n                         and is indexed by the ifIndex value of the corresponding\n                         row in the MIB-II ifTable.')
mitelIfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mitelIfTableEntry.setStatus('current')
if mibBuilder.loadTexts: mitelIfTableEntry.setDescription('An entry containing management information applicable\n                         to a particular interface.')
mitelIfTblType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 3, 2, 2, 1, 1), MitelIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfTblType.setStatus('current')
if mibBuilder.loadTexts: mitelIfTblType.setDescription('The type of interface.  Additional values for \n                          mitelIfTblType are assigned by the Standards Group, \n                          through updating the syntax of the MitelIfType \n                          textual convention. This row is deleted automatically\n                          when the corresponding ifTable row is deleted.')
mitelPropApplications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1))
if mibBuilder.loadTexts: mitelPropApplications.setStatus('current')
if mibBuilder.loadTexts: mitelPropApplications.setDescription('Manageable applications.')
mitelPropTransmission = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 2))
if mibBuilder.loadTexts: mitelPropTransmission.setStatus('current')
if mibBuilder.loadTexts: mitelPropTransmission.setDescription('MITEL proprietary transmission media.')
mitelPropProtocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 3))
if mibBuilder.loadTexts: mitelPropProtocols.setStatus('current')
if mibBuilder.loadTexts: mitelPropProtocols.setDescription('Manageable proprietary protocols.')
mitelPropUtilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 4))
if mibBuilder.loadTexts: mitelPropUtilities.setStatus('current')
if mibBuilder.loadTexts: mitelPropUtilities.setDescription('Manageable utilities and middleware.')
mitelPropHardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 5))
if mibBuilder.loadTexts: mitelPropHardware.setStatus('current')
if mibBuilder.loadTexts: mitelPropHardware.setDescription('Management of proprietary hardware.')
mitelPropNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 6))
if mibBuilder.loadTexts: mitelPropNotifications.setStatus('current')
if mibBuilder.loadTexts: mitelPropNotifications.setDescription('Control and history of proprietary notifications.')
mitelPropReset = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 7))
if mibBuilder.loadTexts: mitelPropReset.setStatus('current')
if mibBuilder.loadTexts: mitelPropReset.setDescription('Access for remote reset of agent and platform.')
mitelPropCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 9))
if mibBuilder.loadTexts: mitelPropCommon.setStatus('current')
if mibBuilder.loadTexts: mitelPropCommon.setDescription('Manageable of common information that can span hardware,\n                           middleware, and utilities.')
mitelAppCallServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1, 1))
if mibBuilder.loadTexts: mitelAppCallServer.setStatus('current')
if mibBuilder.loadTexts: mitelAppCallServer.setDescription('Manageable Mitel Call Servers.')
mitelConfCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 1))
if mibBuilder.loadTexts: mitelConfCompliances.setStatus('current')
if mibBuilder.loadTexts: mitelConfCompliances.setDescription('The compliance subtree. Leaves in this subtree are\n                          used for defining the ways in which an agent can\n                          claim compliance with this or other MITEL MIBs.')
mitelConfGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2))
if mibBuilder.loadTexts: mitelConfGroups.setStatus('current')
if mibBuilder.loadTexts: mitelConfGroups.setDescription('The group subtree. Leaves in this subtree identify\n                          object groupings used in the compliance statements.')
mitelGrpCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1))
if mibBuilder.loadTexts: mitelGrpCommon.setStatus('current')
if mibBuilder.loadTexts: mitelGrpCommon.setDescription('The groups associated with the MITEL MIB.')
mitelGrpCs2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3))
if mibBuilder.loadTexts: mitelGrpCs2000.setStatus('current')
if mibBuilder.loadTexts: mitelGrpCs2000.setDescription('The groups associated with the MITEL SX2000 MIB.')
mitelGrpIpera3000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 4))
if mibBuilder.loadTexts: mitelGrpIpera3000.setStatus('current')
if mibBuilder.loadTexts: mitelGrpIpera3000.setDescription('The groups associated with the MITEL 3300 ICP MIB.')
mitelConfAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 3))
if mibBuilder.loadTexts: mitelConfAgents.setStatus('current')
if mibBuilder.loadTexts: mitelConfAgents.setDescription('The agent capabilities subtree. Leaves in this subtree\n                          are used for defining the capabilities of a particular\n                          agent implementation regarding the MIB compliance\n                          statements.')
mitelComplMitel = ModuleCompliance((1, 3, 6, 1, 4, 1, 1027, 5, 1, 1)).setObjects(("MITEL-MIB", "mitelGrpCmnInterfaces"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelComplMitel = mitelComplMitel.setStatus('current')
if mibBuilder.loadTexts: mitelComplMitel.setDescription('The compliance statement for SNMPv2 entities which\n                           implement the MITEL MIB.')
mitelGrpCmnInterfaces = ObjectGroup((1, 3, 6, 1, 4, 1, 1027, 5, 2, 1, 6)).setObjects(("MITEL-MIB", "mitelIfNumber"), ("MITEL-MIB", "mitelIfTblType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelGrpCmnInterfaces = mitelGrpCmnInterfaces.setStatus('current')
if mibBuilder.loadTexts: mitelGrpCmnInterfaces.setDescription('The objects in the MIB-II interfaces extension.')
mibBuilder.exportSymbols("MITEL-MIB", mitelGrpCommon=mitelGrpCommon, mitelConfAgents=mitelConfAgents, mitelPropProtocols=mitelPropProtocols, mitelIdCtiPlatforms=mitelIdCtiPlatforms, mitelIdInterfaces=mitelIdInterfaces, mitelPropApplications=mitelPropApplications, mitelExtensions=mitelExtensions, mitelConformance=mitelConformance, mitelPropCommon=mitelPropCommon, mitelExtInterfaces=mitelExtInterfaces, mitelIdCallServers=mitelIdCallServers, mitelPropHardware=mitelPropHardware, mitelAppCallServer=mitelAppCallServer, mitelGrpIpera3000=mitelGrpIpera3000, mitelPropReset=mitelPropReset, mitelIdCsMc2=mitelIdCsMc2, mitelIdCs2000Light=mitelIdCs2000Light, mitelExperimental=mitelExperimental, mitelIfTable=mitelIfTable, mitelConfCompliances=mitelConfCompliances, mitelGrpCmnInterfaces=mitelGrpCmnInterfaces, MitelIfType=MitelIfType, mitelIdApplicationPlatforms=mitelIdApplicationPlatforms, mitelConfGroups=mitelConfGroups, mitelIdCsIpera3000=mitelIdCsIpera3000, mitelIdMgmtPlatforms=mitelIdMgmtPlatforms, mitelComplMitel=mitelComplMitel, mitelPropUtilities=mitelPropUtilities, mitelPropTransmission=mitelPropTransmission, mitelGrpCs2000=mitelGrpCs2000, mitel=mitel, mitelIdentification=mitelIdentification, PYSNMP_MODULE_ID=mitel, mitelPropNotifications=mitelPropNotifications, mitelIdTerminals=mitelIdTerminals, mitelIfTableEntry=mitelIfTableEntry, MitelNotifyTransportType=MitelNotifyTransportType, mitelIfTblType=mitelIfTblType, mitelIfNumber=mitelIfNumber, mitelProprietary=mitelProprietary)
