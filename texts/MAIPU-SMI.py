#
# PySNMP MIB module MAIPU-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/maipu/MAIPU-SMI
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:26 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Bits, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter64, Counter32, Unsigned32, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
maipu = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651))
maipu.setRevisions(('1901-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: maipu.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: maipu.setLastUpdated('0101010000Z')
if mibBuilder.loadTexts: maipu.setOrganization('Maipu Data Communication, Inc.')
if mibBuilder.loadTexts: maipu.setContactInfo('E-mail: maipu2@mail.sc.cninfo.net')
if mibBuilder.loadTexts: maipu.setDescription('The Structure of Management Information for Maipu.')
mpProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 1))
if mibBuilder.loadTexts: mpProducts.setStatus('current')
if mibBuilder.loadTexts: mpProducts.setDescription('products is the root OBJECT IDENTIFIER from which sysObjectID\n\t\tvalues are assigned.  Actual values are defined in\n\t\tMAIPU-PRODUCTS-MIB.')
mpTrapObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 2))
if mibBuilder.loadTexts: mpTrapObject.setStatus('current')
if mibBuilder.loadTexts: mpTrapObject.setDescription('main subtree for maipu Traps.')
mpMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 3))
if mibBuilder.loadTexts: mpMgmt.setStatus('current')
if mibBuilder.loadTexts: mpMgmt.setDescription('mpMgmt is the main subtree for implemented MIB branch.\n\t\tNote that different type of maipu products may have the same\n\t\tprotocol implementation, so we put such content into here so\n\t\tthat every types could utilize corresponding module.')
mpExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 4))
if mibBuilder.loadTexts: mpExperiment.setStatus('current')
if mibBuilder.loadTexts: mpExperiment.setDescription('maipuExperiment provides a root object identifier from which\n\t\texperimental mibs may be temporarily based. MIBs are typicially\n\t\tbased here if they fall in one of two categories:\n\n\t\t1) IETF work-in-process mibs which have not been assigned a\n\t\t   permanent object identifier by the IANA.\n\t\t2) Maipu work-in-process which has not been assigned a\n\t\t   permanent object identifier by the maipu assigned number\n\t\t   authority, typicially because the mib is not ready for\n\t\t   deployment.\n\n\t\tNOTE:  support for mibs in the maipuExperiment subtree will be\n\t\terased when a permanent object identifier assignment is made.')
mpSecurity = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 5))
if mibBuilder.loadTexts: mpSecurity.setStatus('current')
if mibBuilder.loadTexts: mpSecurity.setDescription('mpSecurity is the main subtree for security product MIB branch.')
mpMgmt2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6))
if mibBuilder.loadTexts: mpMgmt2.setStatus('current')
if mibBuilder.loadTexts: mpMgmt2.setDescription('mpMgmt2 is the new subtree for implemented MIB branch.')
mpSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 1))
if mibBuilder.loadTexts: mpSystem.setStatus('current')
if mibBuilder.loadTexts: mpSystem.setDescription('mpSystem is the subtree  for system mib.')
mpRouterTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 2))
if mibBuilder.loadTexts: mpRouterTech.setStatus('current')
if mibBuilder.loadTexts: mpRouterTech.setDescription('mpLayer2 is the subtree for Layer3 MIB.')
mpSwitchTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 3))
if mibBuilder.loadTexts: mpSwitchTech.setStatus('current')
if mibBuilder.loadTexts: mpSwitchTech.setDescription('mpLayer3 is the subtree for Layer2 MIB.')
mpVoipTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 4))
if mibBuilder.loadTexts: mpVoipTech.setStatus('current')
if mibBuilder.loadTexts: mpVoipTech.setDescription('mpVoip is the subtree for maipu voip MIB.')
mpSecurityTech = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 5))
if mibBuilder.loadTexts: mpSecurityTech.setStatus('current')
if mibBuilder.loadTexts: mpSecurityTech.setDescription('mpSec  is the subtree for maipu security MIB')
mpApp = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 6))
if mibBuilder.loadTexts: mpApp.setStatus('current')
if mibBuilder.loadTexts: mpApp.setDescription('mpApp is the subtree for maipu application MIB.')
mpOtherSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 5651, 6, 7))
if mibBuilder.loadTexts: mpOtherSys.setStatus('current')
if mibBuilder.loadTexts: mpOtherSys.setDescription('mpOtherSys is the subtree for third part MIB.')
mibBuilder.exportSymbols("MAIPU-SMI", mpMgmt2=mpMgmt2, mpVoipTech=mpVoipTech, mpOtherSys=mpOtherSys, mpSecurity=mpSecurity, mpExperiment=mpExperiment, mpMgmt=mpMgmt, mpProducts=mpProducts, mpApp=mpApp, mpSecurityTech=mpSecurityTech, mpSystem=mpSystem, mpTrapObject=mpTrapObject, mpRouterTech=mpRouterTech, mpSwitchTech=mpSwitchTech, maipu=maipu, PYSNMP_MODULE_ID=maipu)
