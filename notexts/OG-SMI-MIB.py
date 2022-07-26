#
# PySNMP MIB module OG-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SMI-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:24 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, IpAddress, ModuleIdentity, Counter32, iso, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, MibIdentifier, TimeTicks, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "iso", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "MibIdentifier", "TimeTicks", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
opengear = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049))
opengear.setRevisions(('2018-06-15 00:00', '2013-11-15 00:00', '2013-08-11 00:00', '2010-03-22 11:27', '2005-02-24 01:00',))
if mibBuilder.loadTexts: opengear.setLastUpdated('201806150000Z')
if mibBuilder.loadTexts: opengear.setOrganization('Opengear Inc.')
ogProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 1))
if mibBuilder.loadTexts: ogProducts.setStatus('current')
ogLegacyMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 2))
if mibBuilder.loadTexts: ogLegacyMgmt.setStatus('current')
ogExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 3))
if mibBuilder.loadTexts: ogExperimental.setStatus('current')
ogInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 4))
if mibBuilder.loadTexts: ogInternal.setStatus('current')
ogReserved1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 5))
if mibBuilder.loadTexts: ogReserved1.setStatus('current')
ogReserved2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 6))
if mibBuilder.loadTexts: ogReserved2.setStatus('current')
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 7))
if mibBuilder.loadTexts: otherEnterprises.setStatus('current')
ogAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 8))
if mibBuilder.loadTexts: ogAgentCapability.setStatus('current')
ogConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 9))
if mibBuilder.loadTexts: ogConfig.setStatus('current')
ogMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 10))
if mibBuilder.loadTexts: ogMgmt.setStatus('current')
ogModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 11))
if mibBuilder.loadTexts: ogModules.setStatus('current')
ogSpecific = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 18))
if mibBuilder.loadTexts: ogSpecific.setStatus('current')
mibBuilder.exportSymbols("OG-SMI-MIB", ogMgmt=ogMgmt, PYSNMP_MODULE_ID=opengear, ogAgentCapability=ogAgentCapability, ogSpecific=ogSpecific, otherEnterprises=otherEnterprises, ogReserved2=ogReserved2, ogLegacyMgmt=ogLegacyMgmt, opengear=opengear, ogProducts=ogProducts, ogInternal=ogInternal, ogModules=ogModules, ogReserved1=ogReserved1, ogExperimental=ogExperimental, ogConfig=ogConfig)
