#
# PySNMP MIB module APAMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAMI-MIB
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
apAMIModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 6))
apAMIModule.setRevisions(('2012-07-16 00:00', '2014-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apAMIModule.setRevisionsDescriptions(('initial version.', 'Updated Organization and Contact info.',))
if mibBuilder.loadTexts: apAMIModule.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apAMIModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apAMIModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apAMIModule.setDescription('The Acme Management Interface MIB for Oracle Communications Acme Packet SBCs')
apAMIMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1))
apAMISoapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1))
apAMISoapHttp = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttp.setStatus('current')
if mibBuilder.loadTexts: apAMISoapHttp.setDescription('Indicates the status of the soap http interface.')
apAMISoapHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttpPort.setStatus('current')
if mibBuilder.loadTexts: apAMISoapHttpPort.setDescription('the tcp port soap over HTTP is running on.')
apAMISoapHttps = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttps.setStatus('current')
if mibBuilder.loadTexts: apAMISoapHttps.setDescription('Indicates the status of the soap https interface.')
apAMISoapHttpsPort = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAMISoapHttpsPort.setStatus('current')
if mibBuilder.loadTexts: apAMISoapHttpsPort.setDescription('the tcp port soap over HTTPS is running on.')
apAMIModuleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2))
apAMIModuleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1))
apAMIMibObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1, 1)).setObjects(("APAMI-MIB", "apAMISoapHttp"), ("APAMI-MIB", "apAMISoapHttpPort"), ("APAMI-MIB", "apAMISoapHttps"), ("APAMI-MIB", "apAMISoapHttpsPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAMIMibObjectsGroup = apAMIMibObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apAMIMibObjectsGroup.setDescription('This automatically created object group contains\n                            all those objects that do not belong to any other\n                            OBJECT-GROUP')
mibBuilder.exportSymbols("APAMI-MIB", apAMISoapHttps=apAMISoapHttps, apAMIModule=apAMIModule, apAMIMibObjectsGroup=apAMIMibObjectsGroup, apAMIModuleConformance=apAMIModuleConformance, apAMISoapHttpsPort=apAMISoapHttpsPort, apAMIModuleGroups=apAMIModuleGroups, apAMISoapHttp=apAMISoapHttp, apAMISoapObjects=apAMISoapObjects, apAMIMIBObjects=apAMIMIBObjects, PYSNMP_MODULE_ID=apAMIModule, apAMISoapHttpPort=apAMISoapHttpPort)
