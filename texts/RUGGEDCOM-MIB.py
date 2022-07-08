#
# PySNMP MIB module RUGGEDCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ros/RUGGEDCOM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:27:52 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, Counter32, enterprises, Integer32, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "Counter32", "enterprises", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruggedcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004))
ruggedcom.setRevisions(('2015-04-02 09:00', '2012-06-01 17:00', '2010-05-27 10:30', '2010-03-12 10:30', '2008-12-17 13:00', '2006-09-09 09:00', '2003-02-18 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ruggedcom.setRevisionsDescriptions(('Added Added specific ros product branch ruggedcomMC.', 'Added Added specific rox2 products branch ruggedcomRX1XXXrox2X.', 'Updated ruggedcomProducts branches - added ruggedcomMX5000.', 'Updated ruggedcomProducts branches.', 'Removed inclusion of OBJECT-TYPE and Interger32.\n         Included OBJECT-IDENTITY.', 'Updated CONTACT-INFO.', 'The initial version of RuggedCom enterprise structure of management\n        information.',))
if mibBuilder.loadTexts: ruggedcom.setLastUpdated('201504020900Z')
if mibBuilder.loadTexts: ruggedcom.setOrganization('RuggedCom')
if mibBuilder.loadTexts: ruggedcom.setContactInfo('Postal: RuggedCom Inc.\n                300 Applewood Crescent\n                Concord, Ontario, \n                L4K 5C7 Canada\n        Tel:    1-905-856-5288\n        E-Mail: support@ruggedcom.com')
if mibBuilder.loadTexts: ruggedcom.setDescription('RuggedCom enterprise structure of management information.')
ruggedcomExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 1))
if mibBuilder.loadTexts: ruggedcomExperiment.setStatus('current')
if mibBuilder.loadTexts: ruggedcomExperiment.setDescription('The root object identifier from which experimental MIBs may\n        be temporarily based.  MIBs are typicaly based here if they fall\n        in one of two categories:\n        1) are IETF work-in-process MIBs which have not been assigned a \n        permanet object identifier by the IANA.\n        2) are RugedCom work-in-process which has not been assigne a \n        permanent object identifier, typically because the MIB is not \n        ready for deployment.')
ruggedcomProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 2))
if mibBuilder.loadTexts: ruggedcomProducts.setStatus('current')
if mibBuilder.loadTexts: ruggedcomProducts.setDescription('The root object identifier from which sysObjectID values are \n        assigned.')
ruggedcomRX1XXX = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 4))
ruggedcomRX1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 4, 1))
ruggedcomRX1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 4, 2))
ruggedcomRX5XXX = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 5))
ruggedcomRX5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 5, 1))
ruggedcomMX5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 5, 2))
ruggedmaxProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 6))
ruggedcomRX15XX = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8))
ruggedcomRX1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8, 1))
ruggedcomRX1501 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8, 2))
ruggedcomRX1510 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8, 11))
ruggedcomRX1511 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8, 12))
ruggedcomRX1512 = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 8, 13))
ruggedcomRX1XXXrox2X = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 9))
ruggedcomRX1000rox2X = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 9, 1))
ruggedcomRX1100rox2X = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 9, 2))
ruggedcomAirModule = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 10))
ruggedcomMC = MibIdentifier((1, 3, 6, 1, 4, 1, 15004, 2, 11))
ruggedcomOtherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 3))
if mibBuilder.loadTexts: ruggedcomOtherEnterprises.setStatus('current')
if mibBuilder.loadTexts: ruggedcomOtherEnterprises.setDescription('The root object identifier from which MIBs produced by other \n        companies may be placed.  MIBs produced by other enterprises \n        are typically implemented with the object identifiers as defined\n        in the MIB, but if the MIB is deemed to be uncontrolelled, we may \n        reroot the MIB at this subtree in order to have a controlled \n        version.')
ruggedcomMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4))
if mibBuilder.loadTexts: ruggedcomMgmt.setStatus('current')
if mibBuilder.loadTexts: ruggedcomMgmt.setDescription('The main subtree for new MIB development where specific RuggedCom\n        proprietary MIBs can be placed.')
ruggedcomTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 5))
if mibBuilder.loadTexts: ruggedcomTraps.setStatus('current')
if mibBuilder.loadTexts: ruggedcomTraps.setDescription('The root of the subtree where RuggedCom traps can be placed.')
ruggedcomAgentCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 6))
if mibBuilder.loadTexts: ruggedcomAgentCapabilities.setStatus('current')
if mibBuilder.loadTexts: ruggedcomAgentCapabilities.setDescription('The root object identifier from which AGENT-CAPABILITIES values\n        may be assigned.')
ruggedcomAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30))
if mibBuilder.loadTexts: ruggedcomAgentCapability.setStatus('current')
if mibBuilder.loadTexts: ruggedcomAgentCapability.setDescription('The root object identifier from which AGENT-CAPABILITIES for \n        individual MIBs are described.')
mibBuilder.exportSymbols("RUGGEDCOM-MIB", ruggedcomAgentCapabilities=ruggedcomAgentCapabilities, ruggedcomProducts=ruggedcomProducts, ruggedcomAgentCapability=ruggedcomAgentCapability, ruggedcomTraps=ruggedcomTraps, ruggedcomRX5000=ruggedcomRX5000, ruggedcomRX1000=ruggedcomRX1000, ruggedcomRX1501=ruggedcomRX1501, ruggedcomExperiment=ruggedcomExperiment, ruggedcomMgmt=ruggedcomMgmt, ruggedcomRX1511=ruggedcomRX1511, ruggedcomRX15XX=ruggedcomRX15XX, ruggedcomMX5000=ruggedcomMX5000, ruggedcomRX5XXX=ruggedcomRX5XXX, ruggedcomRX1510=ruggedcomRX1510, ruggedcomOtherEnterprises=ruggedcomOtherEnterprises, ruggedcomRX1100rox2X=ruggedcomRX1100rox2X, ruggedcomRX1500=ruggedcomRX1500, PYSNMP_MODULE_ID=ruggedcom, ruggedcomRX1XXXrox2X=ruggedcomRX1XXXrox2X, ruggedcomAirModule=ruggedcomAirModule, ruggedmaxProducts=ruggedmaxProducts, ruggedcomRX1000rox2X=ruggedcomRX1000rox2X, ruggedcomMC=ruggedcomMC, ruggedcom=ruggedcom, ruggedcomRX1512=ruggedcomRX1512, ruggedcomRX1100=ruggedcomRX1100, ruggedcomRX1XXX=ruggedcomRX1XXX)
