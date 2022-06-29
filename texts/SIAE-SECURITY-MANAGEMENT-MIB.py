#
# PySNMP MIB module SIAE-SECURITY-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SECURITY-MANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:39 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, TimeTicks, iso, Counter64, Integer32, ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "iso", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "MibIdentifier", "Bits")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
securityManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 82))
securityManagement.setRevisions(('2014-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: securityManagement.setRevisionsDescriptions(('Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: securityManagement.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: securityManagement.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: securityManagement.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: securityManagement.setDescription('Security protocols management for SIAE equipments.\n            ')
securityManagementMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securityManagementMibVersion.setStatus('current')
if mibBuilder.loadTexts: securityManagementMibVersion.setDescription('Numerical version of this module.\n                 The string version of this MIB have the following format:\n                    XX.YY.ZZ\n                 so, for example, the value 1 should be interpreted as 00.00.01\n                 and the value 10001 should be interpreted as 01.00.01.')
servicesTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2), )
if mibBuilder.loadTexts: servicesTable.setStatus('current')
if mibBuilder.loadTexts: servicesTable.setDescription('A list of services entries. This table is useful \n             to show the manager the administrative and operative\n             status of all services on the equipment.')
serviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1), ).setIndexNames((0, "SIAE-SECURITY-MANAGEMENT-MIB", "serviceIndex"))
if mibBuilder.loadTexts: serviceEntry.setStatus('current')
if mibBuilder.loadTexts: serviceEntry.setDescription('An entry containing management information applicable \n             to a given service on the equipment.')
serviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceIndex.setStatus('current')
if mibBuilder.loadTexts: serviceIndex.setDescription('A unique value, greater than zero, for each service.\n             It is recommended that values are assigned contiguously \n             starting from 1.')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('current')
if mibBuilder.loadTexts: serviceName.setDescription('ASCII string to identify the service. \n            ')
serviceProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceProtocolVersion.setStatus('current')
if mibBuilder.loadTexts: serviceProtocolVersion.setDescription('An indication of the service protocol version \n             supported or enabled on the device. \n            ')
serviceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: serviceAdminStatus.setStatus('current')
if mibBuilder.loadTexts: serviceAdminStatus.setDescription('This object enables/ disables service on the \n              equipment. The value of this object depends on\n              effective protocol administrative status.')
serviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notAvailable", 0), ("running", 1), ("stopped", 2))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceOperStatus.setStatus('current')
if mibBuilder.loadTexts: serviceOperStatus.setDescription('This object shows service operative status on the\n               equipment.')
serviceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: serviceRowStatus.setStatus('current')
if mibBuilder.loadTexts: serviceRowStatus.setDescription('Status of this conceptual row in servicesTable.\n            ')
mibBuilder.exportSymbols("SIAE-SECURITY-MANAGEMENT-MIB", serviceProtocolVersion=serviceProtocolVersion, servicesTable=servicesTable, serviceOperStatus=serviceOperStatus, serviceEntry=serviceEntry, securityManagementMibVersion=securityManagementMibVersion, serviceRowStatus=serviceRowStatus, serviceName=serviceName, securityManagement=securityManagement, serviceIndex=serviceIndex, serviceAdminStatus=serviceAdminStatus, PYSNMP_MODULE_ID=securityManagement)
