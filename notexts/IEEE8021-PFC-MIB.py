#
# PySNMP MIB module IEEE8021-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-PFC-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:13:40 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
ifEntry, ifGeneralInformationGroup = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifGeneralInformationGroup")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
Bits, TimeTicks, Gauge32, NotificationType, iso, Counter64, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, Unsigned32, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Gauge32", "NotificationType", "iso", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021PFCMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 21))
ieee8021PFCMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2010-02-08 00:00',))
if mibBuilder.loadTexts: ieee8021PFCMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PFCMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PfcMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 1))
ieee8021PfcConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2))
ieee8021PfcIfTable = MibTable((1, 3, 111, 2, 802, 1, 1, 21, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfTable.setStatus('current')
ieee8021PfcIfEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1), )
ifEntry.registerAugmentions(("IEEE8021-PFC-MIB", "ieee8021PfcIfEntry"))
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setStatus('current')
ieee8021PfcLinkDelayAllowance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setStatus('current')
ieee8021PfcRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 2), Counter32()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcRequests.setStatus('current')
ieee8021PfcIndications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 3), Counter32()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcIndications.setStatus('current')
ieee8021PfcCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 1))
ieee8021PfcGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 2))
ieee8021PfcGlobalReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 21, 2, 2, 1)).setObjects(("IEEE8021-PFC-MIB", "ieee8021PfcLinkDelayAllowance"), ("IEEE8021-PFC-MIB", "ieee8021PfcRequests"), ("IEEE8021-PFC-MIB", "ieee8021PfcIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcGlobalReqdGroup = ieee8021PfcGlobalReqdGroup.setStatus('current')
ieee8021PfcCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 21, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("IEEE8021-PFC-MIB", "ieee8021PfcGlobalReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcCompliance = ieee8021PfcCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PFC-MIB", PYSNMP_MODULE_ID=ieee8021PFCMib, ieee8021PfcLinkDelayAllowance=ieee8021PfcLinkDelayAllowance, ieee8021PfcGroups=ieee8021PfcGroups, ieee8021PfcCompliances=ieee8021PfcCompliances, ieee8021PfcCompliance=ieee8021PfcCompliance, ieee8021PfcIfTable=ieee8021PfcIfTable, ieee8021PFCMib=ieee8021PFCMib, ieee8021PfcRequests=ieee8021PfcRequests, ieee8021PfcGlobalReqdGroup=ieee8021PfcGlobalReqdGroup, ieee8021PfcIndications=ieee8021PfcIndications, ieee8021PfcIfEntry=ieee8021PfcIfEntry, ieee8021PfcMIBObjects=ieee8021PfcMIBObjects, ieee8021PfcConformance=ieee8021PfcConformance)
