#
# PySNMP MIB module STORMSHIELD-PROPERTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-PROPERTY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:58 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, iso, Counter32, ModuleIdentity, Bits, ObjectIdentity, Integer32, MibIdentifier, Unsigned32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "iso", "Counter32", "ModuleIdentity", "Bits", "ObjectIdentity", "Integer32", "MibIdentifier", "Unsigned32", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsProductProperty = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 0))
snsProductProperty.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsProductProperty.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsProductProperty.setOrganization('Stormshield')
snsModel = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsModel.setStatus('current')
snsVersion = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsVersion.setStatus('current')
snsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSerialNumber.setStatus('current')
snsSystemName = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSystemName.setStatus('current')
snsSystemLanguage = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsSystemLanguage.setStatus('current')
snsNbEther = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbEther.setStatus('current')
snsNbVlan = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbVlan.setStatus('current')
snsNbDialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbDialup.setStatus('current')
snsNbPPTP = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbPPTP.setStatus('current')
snsNbSerial = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbSerial.setStatus('current')
snsNbLoopback = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsNbLoopback.setStatus('current')
snsWatchdog = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsWatchdog.setStatus('current')
snsLed = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsLed.setStatus('current')
snsClone = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsClone.setStatus('current')
snsHADialup = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 0, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsHADialup.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-PROPERTY-MIB", snsSystemLanguage=snsSystemLanguage, snsLed=snsLed, snsProductProperty=snsProductProperty, snsSystemName=snsSystemName, snsClone=snsClone, snsNbDialup=snsNbDialup, snsVersion=snsVersion, snsHADialup=snsHADialup, snsModel=snsModel, snsSerialNumber=snsSerialNumber, snsNbVlan=snsNbVlan, snsNbPPTP=snsNbPPTP, snsWatchdog=snsWatchdog, snsNbEther=snsNbEther, snsNbLoopback=snsNbLoopback, PYSNMP_MODULE_ID=snsProductProperty, snsNbSerial=snsNbSerial)
