#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 14:51:22 2023
# On host fv-az561-247 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, IpAddress, ModuleIdentity, iso, Bits, NotificationType, TimeTicks, MibIdentifier, ObjectIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "IpAddress", "ModuleIdentity", "iso", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Gauge32", "Integer32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInfoModule.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsInfoModule.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsInfoModule.setDescription('The MIB module describes general information\n            of RapidStream system.  Mainly, the information \n            obtained from this MIB is used by rsInfoSystemMIB,\n            rsClientMIB, rsSystemStatisticsMIB, rsIpsecTunnelMIB.')
rsInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 1))
if mibBuilder.loadTexts: rsInfoSystem.setStatus('current')
if mibBuilder.loadTexts: rsInfoSystem.setDescription('This is the base system information for all rs Client\n             branches.')
rsInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setStatus('current')
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setDescription("The host's notion of the local date and time of day.")
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoModule=rsInfoModule, PYSNMP_MODULE_ID=rsInfoModule, rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, rsInfoSystem=rsInfoSystem)
