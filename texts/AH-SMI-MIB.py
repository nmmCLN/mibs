#
# PySNMP MIB module AH-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aerohive/AH-SMI-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:07 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, ObjectIdentity, iso, Bits, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, enterprises, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "ObjectIdentity", "iso", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "enterprises", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
aerohive = ModuleIdentity((1, 3, 6, 1, 4, 1, 26928))
if mibBuilder.loadTexts: aerohive.setLastUpdated('201608310000Z')
if mibBuilder.loadTexts: aerohive.setOrganization('Aerohive Networks, Inc')
if mibBuilder.loadTexts: aerohive.setContactInfo('info@aerohive.com\n                        1011 McCarthy Boulevard\n                        \n                        Milpitas, CA 95035')
if mibBuilder.loadTexts: aerohive.setDescription('This is the MIB module for object type definitions\n\t    that are used throughout the Aerohive Networks enterprise MIBs.')
ahProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1))
ahAP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1))
ahAPCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1))
ahAPTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 1))
ahAPInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2))
ahAPMRP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3))
ahAPIDP = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 4))
ahAPHiveAP020_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 2)).setLabel("ahAPHiveAP020-ag")
ahAPHiveAP028_ag = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 3)).setLabel("ahAPHiveAP028-ag")
ahAPHiveAP320_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 4)).setLabel("ahAPHiveAP320-n")
ahAPHiveAP340_n = MibIdentifier((1, 3, 6, 1, 4, 1, 26928, 1, 1, 5)).setLabel("ahAPHiveAP340-n")
class AhString(TextualConvention, OctetString):
    description = 'A text string with 32 octets'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AhNodeID(MacAddress):
    description = 'Mgmt MAC address in hex decimal notation'
    status = 'current'

class AhInterfaceType(TextualConvention, Integer32):
    description = 'Interface type - (PHYSICAL, VIRTUAL)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ahPHYSICAL", 0), ("ahVIRTURAL", 1))

class AhInterfaceMode(TextualConvention, Integer32):
    description = 'Interface role types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ahNotUsed", 0), ("ahAccess", 1), ("ahBackhaul", 2), ("ahBridge", 3))

class AhMACProtocol(TextualConvention, Integer32):
    description = 'Radio Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ah11a", 0), ("ah11b", 1), ("ah11g", 2), ("ah11na", 3), ("ah11ng", 4))

mibBuilder.exportSymbols("AH-SMI-MIB", ahAPCommon=ahAPCommon, ahAP=ahAP, AhInterfaceMode=AhInterfaceMode, ahAPHiveAP020_ag=ahAPHiveAP020_ag, ahAPHiveAP028_ag=ahAPHiveAP028_ag, AhInterfaceType=AhInterfaceType, ahAPTrap=ahAPTrap, ahAPIDP=ahAPIDP, ahAPHiveAP320_n=ahAPHiveAP320_n, AhNodeID=AhNodeID, AhMACProtocol=AhMACProtocol, aerohive=aerohive, ahAPInterface=ahAPInterface, ahProduct=ahProduct, ahAPMRP=ahAPMRP, AhString=AhString, ahAPHiveAP340_n=ahAPHiveAP340_n, PYSNMP_MODULE_ID=aerohive)
