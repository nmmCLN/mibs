#
# PySNMP MIB module ACMEPACKET-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-SMI
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:23 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, TimeTicks, NotificationType, Counter32, Unsigned32, Bits, enterprises, MibIdentifier, ModuleIdentity, iso, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Counter32", "Unsigned32", "Bits", "enterprises", "MibIdentifier", "ModuleIdentity", "iso", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acmepacket = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148))
acmepacket.setRevisions(('2012-02-02 18:00', '2004-02-26 18:00', '2001-09-05 00:00', '2014-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acmepacket.setRevisionsDescriptions(('Updated new contact info.', 'The Structure of Management Information for the\n\t\tAcme Packet enterprise. Add acmepacketModules.', 'Initial version of this MIB module.', 'Updated Organization and Contact info.',))
if mibBuilder.loadTexts: acmepacket.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: acmepacket.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: acmepacket.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: acmepacket.setDescription('Structure of Managed Information for Acme Packet Inc.')
acmepacketAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 2))
if mibBuilder.loadTexts: acmepacketAgentCapability.setStatus('current')
if mibBuilder.loadTexts: acmepacketAgentCapability.setDescription('acmepacketAgentCapability provides a root object identifier\n\t\tfrom which AGENT-CAPABILITIES values may be assigned.')
acmepacketMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 3))
if mibBuilder.loadTexts: acmepacketMgmt.setStatus('current')
if mibBuilder.loadTexts: acmepacketMgmt.setDescription('acmepacketMgmt is the main subtree for the management.')
acmepacketConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 4))
if mibBuilder.loadTexts: acmepacketConfig.setStatus('current')
if mibBuilder.loadTexts: acmepacketConfig.setDescription('acmepacketConfig is the subtree for configuration mibs. \n\t\tThis is reserved for future use.')
acmepacketExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 5))
if mibBuilder.loadTexts: acmepacketExperiment.setStatus('current')
if mibBuilder.loadTexts: acmepacketExperiment.setDescription('acmepacketExperiment provides a root object identifier\n\t\tfrom which experimental mibs may be temporarily\n\t\tbased. support for mibs in the acmepacketExperiment\n\t\tsubtree will be deleted when a permanent object\n\t\tidentifier assignment is made. This is reserved \n\t\tfor future use.')
acmepacketModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 6))
if mibBuilder.loadTexts: acmepacketModules.setStatus('current')
if mibBuilder.loadTexts: acmepacketModules.setDescription('acmepacketModules provides a root object identifier\n\t\tfrom which MODULE-IDENTITY values may be assigned.')
mibBuilder.exportSymbols("ACMEPACKET-SMI", acmepacketExperiment=acmepacketExperiment, acmepacketModules=acmepacketModules, acmepacketAgentCapability=acmepacketAgentCapability, acmepacketConfig=acmepacketConfig, PYSNMP_MODULE_ID=acmepacket, acmepacket=acmepacket, acmepacketMgmt=acmepacketMgmt)
