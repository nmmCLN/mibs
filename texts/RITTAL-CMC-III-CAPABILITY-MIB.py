#
# PySNMP MIB module RITTAL-CMC-III-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-CMC-III-CAPABILITY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:00 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
cmcIII, = mibBuilder.importSymbols("RITTAL-CMC-III-MIB", "cmcIII")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Unsigned32, iso, NotificationType, TimeTicks, Gauge32, ModuleIdentity, ObjectIdentity, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Unsigned32", "iso", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Counter64", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmcIIICapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606, 7, 8))
cmcIIICapability.setRevisions(('2015-10-27 00:00', '2014-10-06 00:00', '2013-03-30 00:00', '2012-08-30 00:00', '2011-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmcIIICapability.setRevisionsDescriptions(('Added cmcIIIPuCapsV104 and cmcIIIPduCapsV104.', 'Added variations of not supported functions of PDU.', 'Added cmcIIIPuCapsV103.', 'Added cmcIIIPduiCapsV102 and use new object group definitions.', 'The initial version (obsolete).',))
if mibBuilder.loadTexts: cmcIIICapability.setLastUpdated('201510270000Z')
if mibBuilder.loadTexts: cmcIIICapability.setOrganization('RITTAL GmbH & Co. KG')
if mibBuilder.loadTexts: cmcIIICapability.setContactInfo('www.rittal.de\n\n                            RITTAL GmbH & Co. KG\n                            Forschung & Entwicklung\n                            Auf dem Stuetzelberg\n                            D-35745 Herborn\n                            Germany, Europe\n\n                            +49(0)2772 5050\n                            info@rittal.de.')
if mibBuilder.loadTexts: cmcIIICapability.setDescription('Private agent capabilitiy MIB of cmcIII SNMP agent.')
cmcIIIPuCapsV102 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30102))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setProductRelease('V1.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setStatus('current')
if mibBuilder.loadTexts: cmcIIIPuCapsV102.setDescription('RITTAL GmbH & Co. KG : CMC III Processing Unit built-in capabilities.')
cmcIIIPuCapsV103 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30103))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setProductRelease('V1.03')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setStatus('current')
if mibBuilder.loadTexts: cmcIIIPuCapsV103.setDescription('RITTAL GmbH & Co. KG : CMC III Processing Unit built-in capabilities.')
cmcIIIPuCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setStatus('current')
if mibBuilder.loadTexts: cmcIIIPuCapsV104.setDescription('RITTAL GmbH & Co. KG : CMC III Power Distribution Unit built-in capabilities.')
cmcIIIPduCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 34104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setStatus('current')
if mibBuilder.loadTexts: cmcIIIPduCapsV104.setDescription('RITTAL GmbH & Co. KG : CMC III Power Distribution Unit built-in capabilities.')
mibBuilder.exportSymbols("RITTAL-CMC-III-CAPABILITY-MIB", cmcIIICapability=cmcIIICapability, cmcIIIPuCapsV102=cmcIIIPuCapsV102, cmcIIIPduCapsV104=cmcIIIPduCapsV104, cmcIIIPuCapsV104=cmcIIIPuCapsV104, cmcIIIPuCapsV103=cmcIIIPuCapsV103, PYSNMP_MODULE_ID=cmcIIICapability)
