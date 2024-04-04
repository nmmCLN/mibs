#
# PySNMP MIB module SIAE-RET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-RET-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:18 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Bits, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Gauge32, Counter32, iso, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Bits", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Gauge32", "Counter32", "iso", "Unsigned32", "Counter64")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
remElement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 70))
remElement.setRevisions(('2014-06-23 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: remElement.setRevisionsDescriptions(('Fixed IMPORTS clause\n            ', 'Improved description of remoteElementMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: remElement.setLastUpdated('201406230000Z')
if mibBuilder.loadTexts: remElement.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: remElement.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: remElement.setDescription('Remote Element Table\n            ')
remoteElementMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteElementMibVersion.setStatus('current')
if mibBuilder.loadTexts: remoteElementMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
remoteElementTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2), )
if mibBuilder.loadTexts: remoteElementTable.setStatus('current')
if mibBuilder.loadTexts: remoteElementTable.setDescription('Table with ISO/OSI remote element that are reacheable from this NE.')
remoteElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1), ).setIndexNames((0, "SIAE-RET-MIB", "remoteElementIpAddress"))
if mibBuilder.loadTexts: remoteElementEntry.setStatus('current')
if mibBuilder.loadTexts: remoteElementEntry.setDescription('Remote element record.')
remoteElementIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteElementIpAddress.setStatus('current')
if mibBuilder.loadTexts: remoteElementIpAddress.setDescription('IP address of remote element.')
remoteElementGosipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: remoteElementGosipAddress.setStatus('current')
if mibBuilder.loadTexts: remoteElementGosipAddress.setDescription('Gosip address of remote element.')
remoteElementLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: remoteElementLabel.setStatus('current')
if mibBuilder.loadTexts: remoteElementLabel.setDescription('ASII string used for label the remote element.')
remoteElementType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("elemManager", 1), ("external", 2), ("remote", 3), ("snm", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: remoteElementType.setStatus('current')
if mibBuilder.loadTexts: remoteElementType.setDescription('Type of Remote Network Element:\n              * elemManager: element Manager.\n              * external: the NE is used as a gateway to connect the element.\n              * remote: the equipment connected to the other end of radio link.\n              * snm: equipment managed by SubNetwork Manager.')
remoteElementRadioBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remoteElementRadioBranchId.setStatus('current')
if mibBuilder.loadTexts: remoteElementRadioBranchId.setDescription('It reports the radio branch connecting the IP adress.\n             (Zero means IP address not directly connected).')
remoteElementRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 70, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: remoteElementRowStatus.setStatus('current')
if mibBuilder.loadTexts: remoteElementRowStatus.setDescription('Status of this row of remoteElementTable.\n            ')
mibBuilder.exportSymbols("SIAE-RET-MIB", remoteElementMibVersion=remoteElementMibVersion, remoteElementRadioBranchId=remoteElementRadioBranchId, remoteElementEntry=remoteElementEntry, remoteElementRowStatus=remoteElementRowStatus, remElement=remElement, PYSNMP_MODULE_ID=remElement, remoteElementIpAddress=remoteElementIpAddress, remoteElementTable=remoteElementTable, remoteElementLabel=remoteElementLabel, remoteElementType=remoteElementType, remoteElementGosipAddress=remoteElementGosipAddress)
