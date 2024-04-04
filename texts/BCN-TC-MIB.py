#
# PySNMP MIB module BCN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-TC-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:25 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
bcnModules, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, iso, Gauge32, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "iso", "Gauge32", "MibIdentifier", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 3))
bcnTCMIB.setRevisions(('2010-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnTCMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnTCMIB.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnTCMIB.setOrganization('BlueCat Networks Inc.')
if mibBuilder.loadTexts: bcnTCMIB.setContactInfo('Adonis Technical Support\n        BlueCat Networks Inc.\n \t\t \n        Tel: +1 866 491 2228 (toll free)\n \t\t     +1 416 646 8400 (international) \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnTCMIB.setDescription('This module defines Textual Conventions used throughout BlueCat mibs.')
class BcnAlarmSeverity(TextualConvention, Integer32):
    description = 'Alarm severity. Valid values are:\n        1 Okay. The component that was experiencing a problem has recovered\n          or a normal, expected operation has taken place.\n        2 Other. The event does not require severity assessment or the \n          severity cannot be determined. \n        3 Informational: Informational event that requires no further action. \n        4 Minor: Minor event that does not require user intervention. \n        5 Warning: An event occurred that might affect services, but is part\n          of a system or user initiated process. It might indicate that a\n          service is transitioning states.\n        6 Major: Event that requires user intervention and assistance. \n        7 Critical: Problem that affects services and system operations, \n          and requires immediate assistance.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30, 40, 50, 60))
    namedValues = NamedValues(("ok", 1), ("other", 10), ("inform", 20), ("minor", 30), ("warning", 40), ("major", 50), ("critical", 60))

mibBuilder.exportSymbols("BCN-TC-MIB", bcnTCMIB=bcnTCMIB, PYSNMP_MODULE_ID=bcnTCMIB, BcnAlarmSeverity=BcnAlarmSeverity)
