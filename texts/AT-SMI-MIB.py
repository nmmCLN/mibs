#
# PySNMP MIB module AT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SMI-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:05 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, enterprises, Gauge32, iso, Integer32, Counter32, IpAddress, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "enterprises", "Gauge32", "iso", "Integer32", "Counter32", "IpAddress", "Bits", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alliedTelesis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207))
alliedTelesis.setRevisions(('2014-09-30 00:00', '2010-06-15 00:15', '2008-02-28 00:00', '2006-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alliedTelesis.setRevisionsDescriptions(('Merged object IDs from ATKK-WLAN-SMI-MIB for Wireless Products.', 'MIB revision history dates in descriptions updated.', 'Standardized the file head.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: alliedTelesis.setLastUpdated('201409300000Z')
if mibBuilder.loadTexts: alliedTelesis.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: alliedTelesis.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: alliedTelesis.setDescription('The Structure of Management Information for Allied Telesis enterprise.')
class DisplayStringUnsized(TextualConvention, OctetString):
    reference = 'DisplayString'
    description = 'Represents textual information taken from the NVT ASCII\n                character set. It is a variation of DisplayString which\n                is defined in RFC 2579.'
    status = 'current'
    displayHint = '255a'

products = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER. Beneath it there are subtree\n                bridgeRouter and routerSwitch, which are is defined in AT-PRODUCTS-MIB.')
wirelesslan = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 13))
if mibBuilder.loadTexts: wirelesslan.setStatus('current')
if mibBuilder.loadTexts: wirelesslan.setDescription('subtree beneath which wireless lan product MIB object ids are assigned.')
mibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8))
if mibBuilder.loadTexts: mibObject.setStatus('current')
if mibBuilder.loadTexts: mibObject.setDescription('mibObject is the root OBJECT IDENTIFIER from which brouterMib and\n                wirelessLanmMIB are built.')
brouterMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4))
if mibBuilder.loadTexts: brouterMib.setStatus('current')
if mibBuilder.loadTexts: brouterMib.setDescription('subtree beneath which atRouter object ids are assigned.')
wirelessLanmMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42))
if mibBuilder.loadTexts: wirelessLanmMIB.setStatus('current')
if mibBuilder.loadTexts: wirelessLanmMIB.setDescription('subtree beneath which object ids for wlanAccess and uwc are assigned.')
atUWC = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 8))
if mibBuilder.loadTexts: atUWC.setStatus('current')
if mibBuilder.loadTexts: atUWC.setDescription('subtree beneath which wlanSwitch object ids are assigned.')
atRouter = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4))
if mibBuilder.loadTexts: atRouter.setStatus('current')
if mibBuilder.loadTexts: atRouter.setDescription('subtree beneath which various groups of object id are assigned.')
objects = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1))
if mibBuilder.loadTexts: objects.setStatus('current')
if mibBuilder.loadTexts: objects.setDescription('subtree beneath which object ids for boards and chips are assigned.')
traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2))
if mibBuilder.loadTexts: traps.setStatus('current')
if mibBuilder.loadTexts: traps.setDescription('subtree beneath which un-sorted trap ids are assigned.')
sysinfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3))
if mibBuilder.loadTexts: sysinfo.setStatus('current')
if mibBuilder.loadTexts: sysinfo.setDescription('subtree beneath which system inforamtion ids are assigned.')
modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4))
if mibBuilder.loadTexts: modules.setStatus('current')
if mibBuilder.loadTexts: modules.setDescription('subtree beneath which software module ids are assigned.')
arInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5))
if mibBuilder.loadTexts: arInterfaces.setStatus('current')
if mibBuilder.loadTexts: arInterfaces.setDescription('subtree beneath which interface ids are assigned.')
protocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6))
if mibBuilder.loadTexts: protocols.setStatus('current')
if mibBuilder.loadTexts: protocols.setDescription('subtree beneath which protocol ids are assigned.')
atAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7))
if mibBuilder.loadTexts: atAgents.setStatus('current')
if mibBuilder.loadTexts: atAgents.setDescription('subtree beneath which variation from standards defined.')
mibBuilder.exportSymbols("AT-SMI-MIB", mibObject=mibObject, atUWC=atUWC, traps=traps, arInterfaces=arInterfaces, DisplayStringUnsized=DisplayStringUnsized, wirelessLanmMIB=wirelessLanmMIB, sysinfo=sysinfo, wirelesslan=wirelesslan, brouterMib=brouterMib, modules=modules, atRouter=atRouter, objects=objects, atAgents=atAgents, protocols=protocols, products=products, alliedTelesis=alliedTelesis, PYSNMP_MODULE_ID=alliedTelesis)
