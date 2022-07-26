#
# PySNMP MIB module RUGGEDCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ros/RUGGEDCOM-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:33:51 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Counter32, Bits, iso, Gauge32, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter32", "Bits", "iso", "Gauge32", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruggedcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004))
ruggedcom.setRevisions(('2015-04-02 09:00', '2012-06-01 17:00', '2010-05-27 10:30', '2010-03-12 10:30', '2008-12-17 13:00', '2006-09-09 09:00', '2003-02-18 14:00',))
if mibBuilder.loadTexts: ruggedcom.setLastUpdated('201504020900Z')
if mibBuilder.loadTexts: ruggedcom.setOrganization('RuggedCom')
ruggedcomExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 1))
if mibBuilder.loadTexts: ruggedcomExperiment.setStatus('current')
ruggedcomProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 2))
if mibBuilder.loadTexts: ruggedcomProducts.setStatus('current')
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
ruggedcomMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 4))
if mibBuilder.loadTexts: ruggedcomMgmt.setStatus('current')
ruggedcomTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 5))
if mibBuilder.loadTexts: ruggedcomTraps.setStatus('current')
ruggedcomAgentCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 6))
if mibBuilder.loadTexts: ruggedcomAgentCapabilities.setStatus('current')
ruggedcomAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30))
if mibBuilder.loadTexts: ruggedcomAgentCapability.setStatus('current')
mibBuilder.exportSymbols("RUGGEDCOM-MIB", ruggedcomTraps=ruggedcomTraps, ruggedcomRX1100rox2X=ruggedcomRX1100rox2X, ruggedcomRX1000rox2X=ruggedcomRX1000rox2X, ruggedcomRX15XX=ruggedcomRX15XX, ruggedcomRX1511=ruggedcomRX1511, ruggedcomRX5XXX=ruggedcomRX5XXX, ruggedcomAirModule=ruggedcomAirModule, ruggedmaxProducts=ruggedmaxProducts, ruggedcomProducts=ruggedcomProducts, ruggedcomAgentCapabilities=ruggedcomAgentCapabilities, ruggedcomMX5000=ruggedcomMX5000, ruggedcomRX5000=ruggedcomRX5000, ruggedcomRX1000=ruggedcomRX1000, ruggedcomRX1500=ruggedcomRX1500, ruggedcomRX1510=ruggedcomRX1510, ruggedcomMC=ruggedcomMC, ruggedcomRX1XXXrox2X=ruggedcomRX1XXXrox2X, ruggedcom=ruggedcom, ruggedcomMgmt=ruggedcomMgmt, ruggedcomRX1100=ruggedcomRX1100, PYSNMP_MODULE_ID=ruggedcom, ruggedcomExperiment=ruggedcomExperiment, ruggedcomRX1501=ruggedcomRX1501, ruggedcomAgentCapability=ruggedcomAgentCapability, ruggedcomRX1XXX=ruggedcomRX1XXX, ruggedcomRX1512=ruggedcomRX1512, ruggedcomOtherEnterprises=ruggedcomOtherEnterprises)
