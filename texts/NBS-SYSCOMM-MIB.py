#
# PySNMP MIB module NBS-SYSCOMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SYSCOMM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:05 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, ObjectIdentity, NotificationType, ModuleIdentity, Counter32, Integer32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSyscommMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 214))
if mibBuilder.loadTexts: nbsSyscommMib.setLastUpdated('201306060000Z')
if mibBuilder.loadTexts: nbsSyscommMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsSyscommMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsSyscommMib.setDescription('Information Base for provisioning ip configuration of managed device.')
nbsSyscommInetGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 3))
if mibBuilder.loadTexts: nbsSyscommInetGrp.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetGrp.setDescription('TCP/IP configuration of system management card')
nbsSyscommEventGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 100))
if mibBuilder.loadTexts: nbsSyscommEventGrp.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommEventGrp.setDescription('Objects to be included in event notifications')
nbsSyscommEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 100, 0))
if mibBuilder.loadTexts: nbsSyscommEvents.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommEvents.setDescription('Events related to system communications')
nbsSyscommInetSlaacAddr = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddr.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddr.setDescription('The IPv6 link-local address assigned by the Stateless Address\n        Autoconfiguration process.')
nbsSyscommInetSlaacAddrPrefix = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddrPrefix.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddrPrefix.setDescription('The prefix length of nbsSyscommInetSlaacAddr.')
nbsSyscommInetAddrAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommInetAddrAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetAddrAdmin.setDescription('Persistent. User-desired IPv6 address.\n\n        For IPv4, use the object nbsCmmcSysIpAddr[Admin]')
nbsSyscommInetAddrOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 11), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrOper.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetAddrOper.setDescription('The user-specified Ipv6 address actually in effect.\n\n        For IPv4, please refer to the object nbsCmmcSysIpAddrOper.')
nbsSyscommInetAddrPrefixAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 22), InetAddressPrefixLength().clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixAdmin.setDescription('The prefix length of nbsSyscommInetAddrAdmin.')
nbsSyscommInetAddrPrefixOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 23), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixOper.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixOper.setDescription('The prefix length of nbsSyscommInetAddrOper.')
nbsSyscommGateAddrAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 30), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommGateAddrAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommGateAddrAdmin.setDescription('Persistent. Desired default IPv6 gateway.\n\n        For IPv4, use the object nbsCmmcSysDefaultGateway[Admin].')
nbsSyscommGateAddrOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 31), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommGateAddrOper.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommGateAddrOper.setDescription('The current IPv6 default gateway.\n\n        For IPv4, please refer to nbsCmmcSysDefaultGatewayOper.')
nbsSyscommInetAddrPrior = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 100, 311), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrior.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetAddrPrior.setDescription('The value nbsSyscommInetAddrOper had before the last modification')
nbsSyscommGateAddrPrior = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 100, 331), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommGateAddrPrior.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommGateAddrPrior.setDescription('The value nbsSyscommGateAddrOper had before the last modification')
nbsSyscommInetCfgChanging = NotificationType((1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 30)).setObjects(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrAdmin"), ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrAdmin"))
if mibBuilder.loadTexts: nbsSyscommInetCfgChanging.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetCfgChanging.setDescription("Sent when before the changes are actually applied.  This is a\n        warning to all SNMP Manager stations that the IP Address is\n        changing, and they will soon lose contact with this device.\n\n        This Notification's nbsCmmcSysTrapTblEntLevel is fatal(2).")
nbsSyscommInetCfgChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 31)).setObjects(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrPrior"), ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrPrior"))
if mibBuilder.loadTexts: nbsSyscommInetCfgChanged.setStatus('current')
if mibBuilder.loadTexts: nbsSyscommInetCfgChanged.setDescription("Sent after changes are complete and have been applied.\n\n        This Notification's nbsCmmcSysTrapTblEntLevel is fatal(2).")
mibBuilder.exportSymbols("NBS-SYSCOMM-MIB", PYSNMP_MODULE_ID=nbsSyscommMib, nbsSyscommMib=nbsSyscommMib, nbsSyscommEventGrp=nbsSyscommEventGrp, nbsSyscommEvents=nbsSyscommEvents, nbsSyscommInetSlaacAddrPrefix=nbsSyscommInetSlaacAddrPrefix, nbsSyscommInetAddrPrefixAdmin=nbsSyscommInetAddrPrefixAdmin, nbsSyscommGateAddrAdmin=nbsSyscommGateAddrAdmin, nbsSyscommGateAddrPrior=nbsSyscommGateAddrPrior, nbsSyscommInetCfgChanging=nbsSyscommInetCfgChanging, nbsSyscommInetCfgChanged=nbsSyscommInetCfgChanged, nbsSyscommInetAddrOper=nbsSyscommInetAddrOper, nbsSyscommInetGrp=nbsSyscommInetGrp, nbsSyscommInetAddrAdmin=nbsSyscommInetAddrAdmin, nbsSyscommInetSlaacAddr=nbsSyscommInetSlaacAddr, nbsSyscommInetAddrPrior=nbsSyscommInetAddrPrior, nbsSyscommGateAddrOper=nbsSyscommGateAddrOper, nbsSyscommInetAddrPrefixOper=nbsSyscommInetAddrPrefixOper)
