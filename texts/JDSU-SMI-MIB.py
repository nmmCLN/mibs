#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:33:15 2022
# On host fv-az278-268 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, Unsigned32, ObjectIdentity, Integer32, Bits, Counter32, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ObjectIdentity", "Integer32", "Bits", "Counter32", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jdsuRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 35873))
jdsuRoot.setRevisions(('2010-06-08 09:53', '2014-01-22 08:51',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jdsuRoot.setRevisionsDescriptions(('Initial version.', 'Add jdsuOtu.',))
if mibBuilder.loadTexts: jdsuRoot.setLastUpdated('201006080953Z')
if mibBuilder.loadTexts: jdsuRoot.setOrganization('JDSU')
if mibBuilder.loadTexts: jdsuRoot.setContactInfo("For product's contacts please see specific product's MIBs\r\n\t\tJDS Uniphase Corporation\r\n\t\t430 N. McCarthy Blvd.\r\n\t\tMilpitas, CA\r\n\t\t95035\r\n\t\tUSA")
if mibBuilder.loadTexts: jdsuRoot.setDescription('Corporate SMI root MIB')
jdsuAccessNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 1))
jdsuCableNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 2))
jdsuDataIPTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 3))
jdsuDigitalVideoTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 4))
jdsuFiberFieldTestSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5))
jdsuRemoteFiberTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1))
jdsuOnmsi = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1, 1))
jdsuOtu = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1, 2))
jdsuLabManufacturingTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 6))
jdsuMetroNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 7))
jdsuNetworkEnterpriseTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 8))
jdsuServiceAssurance = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 9))
jdsuStorageProtocolTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 10))
jdsuWirelessTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 11))
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuRemoteFiberTest=jdsuRemoteFiberTest, PYSNMP_MODULE_ID=jdsuRoot, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuDataIPTest=jdsuDataIPTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems, jdsuOnmsi=jdsuOnmsi, jdsuOtu=jdsuOtu, jdsuRoot=jdsuRoot, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuServiceAssurance=jdsuServiceAssurance, jdsuWirelessTest=jdsuWirelessTest, jdsuCableNetworkTest=jdsuCableNetworkTest)
