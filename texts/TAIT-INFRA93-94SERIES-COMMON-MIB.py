#
# PySNMP MIB module TAIT-INFRA93-94SERIES-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-COMMON-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 13:19:25 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, Bits, Gauge32, NotificationType, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "Gauge32", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
taitModules, = mibBuilder.importSymbols("TAIT-COMMON-MIB", "taitModules")
infra93_94MibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10)).setLabel("infra93-94MibModule")
infra93_94MibModule.setRevisions(('2014-06-17 11:00', '2014-01-26 00:00', '2014-01-14 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: infra93_94MibModule.setRevisionsDescriptions(('Define the module and product root OIDs for monitored Tait 93/94-series Base Stations', '1.04.00 - Remove unused import', '1.01.01 - Initial version prior to change log entries',))
if mibBuilder.loadTexts: infra93_94MibModule.setLastUpdated('201406171100Z')
if mibBuilder.loadTexts: infra93_94MibModule.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: infra93_94MibModule.setContactInfo('Tait Communications\n                     245 Wooldridge Road\n                     PO Box 1645\n                     Christchurch\n                     New Zealand\n\n             phone:  +64 3358 3399\n             email:  support@taitradio.com')
if mibBuilder.loadTexts: infra93_94MibModule.setDescription('Add system alarms for TDMA.')
mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", PYSNMP_MODULE_ID=infra93_94MibModule, infra93_94MibModule=infra93_94MibModule)
