#
# PySNMP MIB module RS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/RS-COMMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:06 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, Counter64, ObjectIdentity, IpAddress, Unsigned32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, Integer32, NotificationType, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "Integer32", "NotificationType", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 2566))
rsRoot.setRevisions(('2006-05-17 08:40',))
if mibBuilder.loadTexts: rsRoot.setLastUpdated('200605170840Z')
if mibBuilder.loadTexts: rsRoot.setOrganization('Rohde&Schwarz GmbH & Co.KG')
rsCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 113))
if mibBuilder.loadTexts: rsCommon.setStatus('current')
rsProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127))
if mibBuilder.loadTexts: rsProducts.setStatus('current')
rsProdBroadcast = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1))
if mibBuilder.loadTexts: rsProdBroadcast.setStatus('current')
rsProdBroadcastMeasurement = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 1))
if mibBuilder.loadTexts: rsProdBroadcastMeasurement.setStatus('current')
rsProdBroadcastTransmitter = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2))
if mibBuilder.loadTexts: rsProdBroadcastTransmitter.setStatus('current')
rsRequirements = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 131))
if mibBuilder.loadTexts: rsRequirements.setStatus('current')
rsExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 137))
if mibBuilder.loadTexts: rsExperimental.setStatus('current')
rsCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 139))
if mibBuilder.loadTexts: rsCapabilities.setStatus('current')
rsRegistration = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149))
if mibBuilder.loadTexts: rsRegistration.setStatus('current')
rsRegModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 1))
if mibBuilder.loadTexts: rsRegModules.setStatus('current')
rsRegBroadcast = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2))
if mibBuilder.loadTexts: rsRegBroadcast.setStatus('current')
rsRegBroadcastMeasurement = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2, 1))
if mibBuilder.loadTexts: rsRegBroadcastMeasurement.setStatus('current')
rsRegBroadcastTransmitter = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2, 2))
if mibBuilder.loadTexts: rsRegBroadcastTransmitter.setStatus('current')
mibBuilder.exportSymbols("RS-COMMON-MIB", PYSNMP_MODULE_ID=rsRoot, rsCommon=rsCommon, rsProdBroadcast=rsProdBroadcast, rsRequirements=rsRequirements, rsRegBroadcast=rsRegBroadcast, rsExperimental=rsExperimental, rsRegistration=rsRegistration, rsProdBroadcastMeasurement=rsProdBroadcastMeasurement, rsCapabilities=rsCapabilities, rsRegBroadcastMeasurement=rsRegBroadcastMeasurement, rsRegBroadcastTransmitter=rsRegBroadcastTransmitter, rsRegModules=rsRegModules, rsProducts=rsProducts, rsProdBroadcastTransmitter=rsProdBroadcastTransmitter, rsRoot=rsRoot)
