#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-REF-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:28 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Unsigned32, Counter32, ModuleIdentity, Integer32, iso, Bits, Counter64, NotificationType, Gauge32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Unsigned32", "Counter32", "ModuleIdentity", "Integer32", "iso", "Bits", "Counter64", "NotificationType", "Gauge32", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: broadcom.setRevisionsDescriptions(('Ubiquiti branding related changes.', 'Revisions made for new release.', 'Updated for release',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: broadcom.setContactInfo('')
if mibBuilder.loadTexts: broadcom.setDescription('')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight\n        ports, with the first octet specifying ports 1 through\n        8, the second octet specifying ports 9 through 16, etc.\n        Within each octet, the most significant bit represents\n        the lowest numbered port, and the least significant bit\n        represents the highest numbered port.  Thus, each port\n        of the bridge is represented by a single bit within the\n        value of this object.  If that bit has a value of '1'\n        then that port is included in the set of ports; the port\n        is not included if its bit has a value of '0'\n             \n        When setting this value, the system will ignore \n        configuration for ports not between the first and last \n        valid ports.  Configuration of any port numbers between \n        this range that are not valid ports return a failure \n        message, but will still apply configuration for valid \n        ports."
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", PYSNMP_MODULE_ID=broadcom, AgentPortMask=AgentPortMask, fastPath=fastPath, broadcomProducts=broadcomProducts, broadcom=broadcom)
