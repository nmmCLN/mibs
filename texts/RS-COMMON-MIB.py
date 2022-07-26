#
# PySNMP MIB module RS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rs/RS-COMMON-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:33:52 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, Counter64, Gauge32, Unsigned32, IpAddress, iso, NotificationType, ObjectIdentity, ModuleIdentity, Bits, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "iso", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 2566))
rsRoot.setRevisions(('2006-05-17 08:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsRoot.setRevisionsDescriptions(('MODULE-IDENTITY added to RS-COMMON-MIB',))
if mibBuilder.loadTexts: rsRoot.setLastUpdated('200605170840Z')
if mibBuilder.loadTexts: rsRoot.setOrganization('Rohde&Schwarz GmbH & Co.KG')
if mibBuilder.loadTexts: rsRoot.setContactInfo('Rohde & Schwarz GmbH & Co. KG\n\t\t         Muehldorfstrasse 15\n\t\t         81671 Munich\n\t\t         Germany')
if mibBuilder.loadTexts: rsRoot.setDescription('The root OID of Rohde&Schwarz GmbH & Co.KG')
rsCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 113))
if mibBuilder.loadTexts: rsCommon.setStatus('current')
if mibBuilder.loadTexts: rsCommon.setDescription('Sub-tree for common object and event definitions.')
rsProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127))
if mibBuilder.loadTexts: rsProducts.setStatus('current')
if mibBuilder.loadTexts: rsProducts.setDescription('Sub-tree for products.')
rsProdBroadcast = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1))
if mibBuilder.loadTexts: rsProdBroadcast.setStatus('current')
if mibBuilder.loadTexts: rsProdBroadcast.setDescription('Sub-tree for broadcast products.')
rsProdBroadcastMeasurement = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 1))
if mibBuilder.loadTexts: rsProdBroadcastMeasurement.setStatus('current')
if mibBuilder.loadTexts: rsProdBroadcastMeasurement.setDescription('Sub-tree for broadcast measurement products.')
rsProdBroadcastTransmitter = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 127, 1, 2))
if mibBuilder.loadTexts: rsProdBroadcastTransmitter.setStatus('current')
if mibBuilder.loadTexts: rsProdBroadcastTransmitter.setDescription('Sub-tree for broadcast transmitter products.')
rsRequirements = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 131))
if mibBuilder.loadTexts: rsRequirements.setStatus('current')
if mibBuilder.loadTexts: rsRequirements.setDescription('Sub-tree for management application requirements.')
rsExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 137))
if mibBuilder.loadTexts: rsExperimental.setStatus('current')
if mibBuilder.loadTexts: rsExperimental.setDescription('Sub-tree for experimental definitions.')
rsCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 139))
if mibBuilder.loadTexts: rsCapabilities.setStatus('current')
if mibBuilder.loadTexts: rsCapabilities.setDescription('Sub-tree for agent capabilities.')
rsRegistration = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149))
if mibBuilder.loadTexts: rsRegistration.setStatus('current')
if mibBuilder.loadTexts: rsRegistration.setDescription('Sub-tree for registrations.')
rsRegModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 1))
if mibBuilder.loadTexts: rsRegModules.setStatus('current')
if mibBuilder.loadTexts: rsRegModules.setDescription('Sub-tree for modules registrations.')
rsRegBroadcast = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2))
if mibBuilder.loadTexts: rsRegBroadcast.setStatus('current')
if mibBuilder.loadTexts: rsRegBroadcast.setDescription('currently not used')
rsRegBroadcastMeasurement = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2, 1))
if mibBuilder.loadTexts: rsRegBroadcastMeasurement.setStatus('current')
if mibBuilder.loadTexts: rsRegBroadcastMeasurement.setDescription('currently not used')
rsRegBroadcastTransmitter = ObjectIdentity((1, 3, 6, 1, 4, 1, 2566, 149, 2, 2))
if mibBuilder.loadTexts: rsRegBroadcastTransmitter.setStatus('current')
if mibBuilder.loadTexts: rsRegBroadcastTransmitter.setDescription('currently not used')
mibBuilder.exportSymbols("RS-COMMON-MIB", rsCommon=rsCommon, rsProdBroadcast=rsProdBroadcast, rsRegistration=rsRegistration, rsProdBroadcastMeasurement=rsProdBroadcastMeasurement, rsCapabilities=rsCapabilities, PYSNMP_MODULE_ID=rsRoot, rsRoot=rsRoot, rsRegModules=rsRegModules, rsExperimental=rsExperimental, rsRegBroadcast=rsRegBroadcast, rsRequirements=rsRequirements, rsRegBroadcastMeasurement=rsRegBroadcastMeasurement, rsRegBroadcastTransmitter=rsRegBroadcastTransmitter, rsProdBroadcastTransmitter=rsProdBroadcastTransmitter, rsProducts=rsProducts)
