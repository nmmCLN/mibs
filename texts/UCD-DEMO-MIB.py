#
# PySNMP MIB module UCD-DEMO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/UCD-DEMO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:31 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, IpAddress, Counter64, Bits, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64", "Bits", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ucdavis, = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdavis")
ucdDemoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 14))
ucdDemoMIB.setRevisions(('1999-12-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ucdDemoMIB.setRevisionsDescriptions(('SMIv2 version converted from older MIB definitions.',))
if mibBuilder.loadTexts: ucdDemoMIB.setLastUpdated('9912090000Z')
if mibBuilder.loadTexts: ucdDemoMIB.setOrganization('University of California, Davis')
if mibBuilder.loadTexts: ucdDemoMIB.setContactInfo('This mib is no longer being maintained by the University of\n\t California and is now in life-support-mode and being\n\t maintained by the net-snmp project.  The best place to write\n\t for public questions about the net-snmp-coders mailing list\n\t at net-snmp-coders@lists.sourceforge.net.\n\n         postal:   Wes Hardaker\n                   P.O. Box 382\n                   Davis CA  95617\n\n         email:    net-snmp-coders@lists.sourceforge.net\n        ')
if mibBuilder.loadTexts: ucdDemoMIB.setDescription('The UCD-SNMP Demonstration MIB.')
ucdDemoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1))
ucdDemoPublic = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1))
ucdDemoResetKeys = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoResetKeys.setStatus('current')
if mibBuilder.loadTexts: ucdDemoResetKeys.setDescription("A set of value 1 to this object resets the\n\t demonstration user's auth and priv keys to the\n\t keys based on the P->Ku->Kul transformation of the\n\t value of the ucdDemoPasspharse object.\n\n\t Values other than 1 are ignored.")
ucdDemoPublicString = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ucdDemoPublicString.setStatus('current')
if mibBuilder.loadTexts: ucdDemoPublicString.setDescription('A publicly settable string that can be set for testing \n\t snmpsets.  This value has no real usage other than\n\t testing purposes.')
ucdDemoUserList = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoUserList.setStatus('current')
if mibBuilder.loadTexts: ucdDemoUserList.setDescription('The list of users affected by the ucdDemoResetKeys object.')
ucdDemoPassphrase = MibScalar((1, 3, 6, 1, 4, 1, 2021, 14, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ucdDemoPassphrase.setStatus('current')
if mibBuilder.loadTexts: ucdDemoPassphrase.setDescription('The demo passphrase that ucdDemoResetKeys changes each \n\t users localized key to based on the P->Ku->Kul transformation.')
mibBuilder.exportSymbols("UCD-DEMO-MIB", ucdDemoPublic=ucdDemoPublic, ucdDemoResetKeys=ucdDemoResetKeys, ucdDemoMIBObjects=ucdDemoMIBObjects, ucdDemoMIB=ucdDemoMIB, ucdDemoUserList=ucdDemoUserList, ucdDemoPublicString=ucdDemoPublicString, PYSNMP_MODULE_ID=ucdDemoMIB, ucdDemoPassphrase=ucdDemoPassphrase)
