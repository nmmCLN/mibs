#
# PySNMP MIB module WHISP-TCV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cambium/WHISP-TCV2-MIB
# Produced by pysmi-1.1.10 at Thu Apr  4 02:55:11 2024
# On host fv-az768-708 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter64, NotificationType, ObjectIdentity, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, iso, Bits, ModuleIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "NotificationType", "ObjectIdentity", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "iso", "Bits", "ModuleIdentity", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispModules, = mibBuilder.importSymbols("WHISP-GLOBAL-REG-MIB", "whispModules")
whispTextualConventionsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 3))
if mibBuilder.loadTexts: whispTextualConventionsModule.setLastUpdated('200304170000Z')
if mibBuilder.loadTexts: whispTextualConventionsModule.setOrganization('Motorola')
if mibBuilder.loadTexts: whispTextualConventionsModule.setContactInfo('Canopy Technical Support\n\t\temail: technical-support@canopywireless.com')
if mibBuilder.loadTexts: whispTextualConventionsModule.setDescription('This module contains textual conventions for the Canopy\n                product line.')
class WhispMACAddress(TextualConvention, OctetString):
    description = 'This a WHiSP MAC address or ESN type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class WhispLUID(TextualConvention, Integer32):
    description = 'The 12 LUID (Local Unit Identification) assigned to each Canopy\n                Subscriber Modem (SM).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class EventString(TextualConvention, OctetString):
    description = 'The string used to display event log.'
    status = 'current'
    displayHint = '2048a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("WHISP-TCV2-MIB", EventString=EventString, WhispMACAddress=WhispMACAddress, PYSNMP_MODULE_ID=whispTextualConventionsModule, whispTextualConventionsModule=whispTextualConventionsModule, WhispLUID=WhispLUID)
