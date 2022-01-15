#
# PySNMP MIB module NMS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/NMS-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, ModuleIdentity, Unsigned32, NotificationType, MibIdentifier, iso, Integer32, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "ModuleIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "iso", "Integer32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nms = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320))
if mibBuilder.loadTexts: nms.setLastUpdated('20000628Z')
if mibBuilder.loadTexts: nms.setOrganization('')
if mibBuilder.loadTexts: nms.setContactInfo('')
if mibBuilder.loadTexts: nms.setDescription('Initial version of this MIB module.The Structure of\n\t\t Management Information for the NMS enterprise.')
nmsProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 1))
if mibBuilder.loadTexts: nmsProducts.setStatus('current')
if mibBuilder.loadTexts: nmsProducts.setDescription('NMS Products is the root OBJECT IDENTIFIER from\n\t\twhich sysObjectID values are assigned.')
nmslocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 2))
if mibBuilder.loadTexts: nmslocal.setStatus('current')
if mibBuilder.loadTexts: nmslocal.setDescription('Subtree beneath which pre-10.2 MIBS were built.')
nmstemporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 3))
if mibBuilder.loadTexts: nmstemporary.setStatus('current')
if mibBuilder.loadTexts: nmstemporary.setDescription('Subtree beneath which pre-10.2 experiments were\n\t\tplaced.')
nmsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 9))
if mibBuilder.loadTexts: nmsMgmt.setStatus('current')
if mibBuilder.loadTexts: nmsMgmt.setDescription('nmsMgmt is the main subtree for new mib development.')
nmsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 12))
if mibBuilder.loadTexts: nmsModules.setStatus('current')
if mibBuilder.loadTexts: nmsModules.setDescription('nmsModules provides a root object identifier\n\t\tfrom which MODULE-IDENTITY values may be assigned.')
nmsPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18))
if mibBuilder.loadTexts: nmsPolicyAuto.setStatus('current')
if mibBuilder.loadTexts: nmsPolicyAuto.setDescription('nmsPolicyAuto is the root of the NMS-assigned\n                OID subtree for OIDs which are automatically assigned\n                for use in Policy Management.')
nmsPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 18, 2))
if mibBuilder.loadTexts: nmsPibToMib.setStatus('current')
if mibBuilder.loadTexts: nmsPibToMib.setDescription("nmsPibToMib is the root of the NMS-assigned\n                OID subtree for MIBs which are algorithmically\n                generated/translated from NMS PIBs with OIDs\n                assigned under the nmsPIB subtree.\n                These generated MIBs allow management\n                entities (other the current Policy Server) to\n                read the downloaded policy.  By convention, for PIB\n                'nmsPIB.x', the generated MIB shall have the\n                name 'nmsPibToMib.x'.")
nmsWorkGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 20))
if mibBuilder.loadTexts: nmsWorkGroup.setStatus('current')
if mibBuilder.loadTexts: nmsWorkGroup.setDescription('nmsWorkGroup is the main subtree for new mib development categorized by module function.')
nmsEPONGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 101))
if mibBuilder.loadTexts: nmsEPONGroup.setStatus('current')
if mibBuilder.loadTexts: nmsEPONGroup.setDescription('nmsEPONGroup is the main subtree for new epon mib .')
nmsPTNGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 3320, 102))
if mibBuilder.loadTexts: nmsPTNGroup.setStatus('current')
if mibBuilder.loadTexts: nmsPTNGroup.setDescription('PTN .')
mibBuilder.exportSymbols("NMS-SMI", nmsMgmt=nmsMgmt, nmsPTNGroup=nmsPTNGroup, nmsProducts=nmsProducts, nms=nms, PYSNMP_MODULE_ID=nms, nmslocal=nmslocal, nmsModules=nmsModules, nmsPolicyAuto=nmsPolicyAuto, nmsWorkGroup=nmsWorkGroup, nmsEPONGroup=nmsEPONGroup, nmstemporary=nmstemporary, nmsPibToMib=nmsPibToMib)
