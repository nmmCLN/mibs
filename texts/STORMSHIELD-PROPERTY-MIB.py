#
# PySNMP MIB module STORMSHIELD-PROPERTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-PROPERTY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:59 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, NotificationType, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "NotificationType", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsProductProperty = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 0))
snsProductProperty.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsProductProperty.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsProductProperty.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsProductProperty.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsProductProperty.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsProductProperty.setDescription('stormshield Product Property')
snsModel = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsModel.setStatus('current')
if mibBuilder.loadTexts: snsModel.setDescription('Stormshield Firewall model ')
snsVersion = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVersion.setStatus('current')
if mibBuilder.loadTexts: snsVersion.setDescription('Stormshield Firewall version')
snsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSerialNumber.setStatus('current')
if mibBuilder.loadTexts: snsSerialNumber.setDescription('Stormshield Firewall serial number')
snsSystemName = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSystemName.setStatus('current')
if mibBuilder.loadTexts: snsSystemName.setDescription('Stormshield Firewall system Name')
snsSystemLanguage = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSystemLanguage.setStatus('current')
if mibBuilder.loadTexts: snsSystemLanguage.setDescription('Firewall language')
snsNbEther = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbEther.setStatus('current')
if mibBuilder.loadTexts: snsNbEther.setDescription('Number of Ethernet interfaces')
snsNbVlan = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbVlan.setStatus('current')
if mibBuilder.loadTexts: snsNbVlan.setDescription('Number of VLAN interfaces')
snsNbDialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbDialup.setStatus('current')
if mibBuilder.loadTexts: snsNbDialup.setDescription('Number of Dialup')
snsNbPPTP = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbPPTP.setStatus('current')
if mibBuilder.loadTexts: snsNbPPTP.setDescription('Number of PPTP')
snsNbSerial = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbSerial.setStatus('current')
if mibBuilder.loadTexts: snsNbSerial.setDescription('Number of serial ports')
snsNbLoopback = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbLoopback.setStatus('current')
if mibBuilder.loadTexts: snsNbLoopback.setDescription('Number of loopback interfaces')
snsWatchdog = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsWatchdog.setStatus('current')
if mibBuilder.loadTexts: snsWatchdog.setDescription('Watchdog')
snsLed = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsLed.setStatus('current')
if mibBuilder.loadTexts: snsLed.setDescription('Firewall LED')
snsClone = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsClone.setStatus('current')
if mibBuilder.loadTexts: snsClone.setDescription("Firewall licence 'clone' token")
snsHADialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHADialup.setStatus('current')
if mibBuilder.loadTexts: snsHADialup.setDescription("Firewall licence 'HA-dialup' token")
mibBuilder.exportSymbols("STORMSHIELD-PROPERTY-MIB", snsClone=snsClone, snsWatchdog=snsWatchdog, snsLed=snsLed, snsProductProperty=snsProductProperty, snsSystemLanguage=snsSystemLanguage, snsNbPPTP=snsNbPPTP, snsVersion=snsVersion, PYSNMP_MODULE_ID=snsProductProperty, snsSerialNumber=snsSerialNumber, snsNbSerial=snsNbSerial, snsNbDialup=snsNbDialup, snsSystemName=snsSystemName, snsModel=snsModel, snsNbLoopback=snsNbLoopback, snsHADialup=snsHADialup, snsNbEther=snsNbEther, snsNbVlan=snsNbVlan)
