#
# PySNMP MIB module WAYSTREAM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-SMI
# Produced by pysmi-1.1.8 at Thu Sep 29 13:20:20 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Gauge32, Counter64, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, enterprises, ObjectIdentity, Unsigned32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "Counter64", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "enterprises", "ObjectIdentity", "Unsigned32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
waystream = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303))
waystream.setRevisions(('2017-02-10 11:00', '2011-01-11 18:01', '2009-03-23 10:39', '2008-01-17 14:05', '2007-05-11 12:28',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: waystream.setRevisionsDescriptions(('Company name change:\n\t In October 2015 PacketFront Network Products was renamed Waystream.\n\t In this update all PacketFront were changed to Waystream and all\n\t pf* to ws*.', 'Updated company name', 'Updated telephone number in contact-info', 'Correct warnings in imports', 'Created from PACKETFRONT-MIB.mib',))
if mibBuilder.loadTexts: waystream.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: waystream.setOrganization('Waystream AB')
if mibBuilder.loadTexts: waystream.setContactInfo('Waystream AB\n         Customer Service\n\n         Mail : Farogatan 33\n                SE-164 51 Kista\n                Sweden\n\n         Tel  : +46 8 5626 9450\n\n         E-mail: info@waystream.com\n         Web   : http://www.waystream.com')
if mibBuilder.loadTexts: waystream.setDescription('The Waystream management information base SMI definitions')
wsProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1))
if mibBuilder.loadTexts: wsProduct.setStatus('current')
if mibBuilder.loadTexts: wsProduct.setDescription('The product group from which sysObjectID values are set.')
wsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2))
if mibBuilder.loadTexts: wsConfig.setStatus('current')
if mibBuilder.loadTexts: wsConfig.setDescription('The configuration subtree')
ipdConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2, 1))
if mibBuilder.loadTexts: ipdConfig.setStatus('current')
if mibBuilder.loadTexts: ipdConfig.setDescription('The configuration subtree')
wsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 3))
if mibBuilder.loadTexts: wsExperiment.setStatus('current')
if mibBuilder.loadTexts: wsExperiment.setDescription('The root object for experimental objects.\n\t\tExperimental objects are used during\n\t\tdevelopment before a permanent assignment\n\t\tto the waystream mib has been determined.\n \n\t\tObjects in this tree will come and go. No guarantees for \n\t\ttheir existance or accuracy is ever provided.')
wsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 4))
if mibBuilder.loadTexts: wsMgmt.setStatus('current')
if mibBuilder.loadTexts: wsMgmt.setDescription('The root object for all Waystream management objects')
wsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 5))
if mibBuilder.loadTexts: wsModules.setStatus('current')
if mibBuilder.loadTexts: wsModules.setDescription('wsModules provides a root object identifier from which the \n\t\tMODULE-IDENTITY values may be assigned')
pfSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 6))
if mibBuilder.loadTexts: pfSW.setStatus('current')
if mibBuilder.loadTexts: pfSW.setDescription('pfSW provides a root object identifier for all PacketFront \n\t\tSoftware Solutions objects')
mibBuilder.exportSymbols("WAYSTREAM-SMI", wsExperiment=wsExperiment, wsProduct=wsProduct, pfSW=pfSW, waystream=waystream, wsConfig=wsConfig, ipdConfig=ipdConfig, wsMgmt=wsMgmt, PYSNMP_MODULE_ID=waystream, wsModules=wsModules)
