#
# PySNMP MIB module ARISTA-VRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-VRF-MIB
# Produced by pysmi-1.1.8 at Fri Oct 13 13:56:09 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32, TimeTicks, ObjectIdentity, Unsigned32, Counter64, MibIdentifier, Counter32, NotificationType, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter64", "MibIdentifier", "Counter32", "NotificationType", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaVrfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 18))
aristaVrfMIB.setRevisions(('2015-01-11 00:00',))
if mibBuilder.loadTexts: aristaVrfMIB.setLastUpdated('201501110000Z')
if mibBuilder.loadTexts: aristaVrfMIB.setOrganization('Arista Networks, Inc.')
aristaVrfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1))
aristaVrfMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2))
class VrfName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '100t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 100)

class VrfRouteDistinguisher(TextualConvention, OctetString):
    reference = '[RFC4364]'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VrfState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

aristaVrfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1), )
if mibBuilder.loadTexts: aristaVrfTable.setStatus('current')
aristaVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1), ).setIndexNames((0, "ARISTA-VRF-MIB", "aristaVrfName"))
if mibBuilder.loadTexts: aristaVrfEntry.setStatus('current')
aristaVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 1), VrfName())
if mibBuilder.loadTexts: aristaVrfName.setStatus('current')
aristaVrfRoutingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("ipv4", 0), ("ipv6", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRoutingStatus.setStatus('current')
aristaVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 3), VrfRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfRouteDistinguisher.setStatus('current')
aristaVrfState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 4), VrfState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfState.setStatus('current')
aristaVrfIfTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2), )
if mibBuilder.loadTexts: aristaVrfIfTable.setStatus('current')
aristaVrfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaVrfIfEntry.setStatus('current')
aristaVrfIfMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1, 1), VrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaVrfIfMembership.setStatus('current')
aristaVrfMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1))
aristaVrfMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2))
aristaVrfMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfMibCompliance = aristaVrfMibCompliance.setStatus('current')
aristaVrfInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2, 1)).setObjects(("ARISTA-VRF-MIB", "aristaVrfRoutingStatus"), ("ARISTA-VRF-MIB", "aristaVrfRouteDistinguisher"), ("ARISTA-VRF-MIB", "aristaVrfState"), ("ARISTA-VRF-MIB", "aristaVrfIfMembership"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaVrfInformationGroup = aristaVrfInformationGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-VRF-MIB", aristaVrfRoutingStatus=aristaVrfRoutingStatus, aristaVrfInformationGroup=aristaVrfInformationGroup, aristaVrfIfEntry=aristaVrfIfEntry, PYSNMP_MODULE_ID=aristaVrfMIB, aristaVrfMibGroups=aristaVrfMibGroups, VrfName=VrfName, aristaVrfName=aristaVrfName, VrfState=VrfState, aristaVrfIfMembership=aristaVrfIfMembership, aristaVrfMibConformance=aristaVrfMibConformance, aristaVrfMIB=aristaVrfMIB, aristaVrfMibCompliances=aristaVrfMibCompliances, aristaVrfEntry=aristaVrfEntry, aristaVrfTable=aristaVrfTable, aristaVrfIfTable=aristaVrfIfTable, aristaVrfState=aristaVrfState, aristaVrfRouteDistinguisher=aristaVrfRouteDistinguisher, aristaVrfMibCompliance=aristaVrfMibCompliance, aristaVrfMibObjects=aristaVrfMibObjects, VrfRouteDistinguisher=VrfRouteDistinguisher)
