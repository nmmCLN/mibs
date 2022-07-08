#
# PySNMP MIB module HALON-SP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/halon/HALON-SP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:19:50 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ObjectIdentity, Counter64, ModuleIdentity, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Integer32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
halonSecuritySP = ModuleIdentity((1, 3, 6, 1, 4, 1, 33234, 1, 1))
halonSecuritySP.setRevisions(('2013-02-07 11:32',))
if mibBuilder.loadTexts: halonSecuritySP.setLastUpdated('201302061107Z')
if mibBuilder.loadTexts: halonSecuritySP.setOrganization('Halon Security')
halonSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 33234))
halonSecurityProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1))
halonSecuritySPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1))
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
configurationRevision = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationRevision.setStatus('current')
mailQueueLength = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mailQueueLength.setStatus('current')
quarantinedMessages = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quarantinedMessages.setStatus('current')
statTable = MibTable((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5), )
if mibBuilder.loadTexts: statTable.setStatus('current')
statEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1), ).setIndexNames((0, "HALON-SP-MIB", "statKey1Index"), (0, "HALON-SP-MIB", "statKey2Index"), (0, "HALON-SP-MIB", "statKey3Index"))
if mibBuilder.loadTexts: statEntry.setStatus('current')
statKey1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey1Index.setStatus('current')
statKey2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey2Index.setStatus('current')
statKey3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey3Index.setStatus('current')
statCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCount.setStatus('current')
statCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCreated.setStatus('current')
statUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statUpdated.setStatus('current')
mibBuilder.exportSymbols("HALON-SP-MIB", mailQueueLength=mailQueueLength, serialNumber=serialNumber, statCreated=statCreated, statUpdated=statUpdated, halonSecurityProducts=halonSecurityProducts, halonSecuritySP=halonSecuritySP, halonSecurity=halonSecurity, statTable=statTable, statKey1Index=statKey1Index, configurationRevision=configurationRevision, statCount=statCount, PYSNMP_MODULE_ID=halonSecuritySP, halonSecuritySPObjects=halonSecuritySPObjects, quarantinedMessages=quarantinedMessages, statKey3Index=statKey3Index, statKey2Index=statKey2Index, statEntry=statEntry)
