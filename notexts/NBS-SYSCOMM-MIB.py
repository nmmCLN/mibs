#
# PySNMP MIB module NBS-SYSCOMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-SYSCOMM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:09 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InetAddress, InetAddressPrefixLength = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, Gauge32, Unsigned32, Integer32, TimeTicks, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "Gauge32", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSyscommMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 214))
if mibBuilder.loadTexts: nbsSyscommMib.setLastUpdated('201306060000Z')
if mibBuilder.loadTexts: nbsSyscommMib.setOrganization('NBS')
nbsSyscommInetGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 3))
if mibBuilder.loadTexts: nbsSyscommInetGrp.setStatus('current')
nbsSyscommEventGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 100))
if mibBuilder.loadTexts: nbsSyscommEventGrp.setStatus('current')
nbsSyscommEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 214, 100, 0))
if mibBuilder.loadTexts: nbsSyscommEvents.setStatus('current')
nbsSyscommInetSlaacAddr = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddr.setStatus('current')
nbsSyscommInetSlaacAddrPrefix = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetSlaacAddrPrefix.setStatus('current')
nbsSyscommInetAddrAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommInetAddrAdmin.setStatus('current')
nbsSyscommInetAddrOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 11), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrOper.setStatus('current')
nbsSyscommInetAddrPrefixAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 22), InetAddressPrefixLength().clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixAdmin.setStatus('current')
nbsSyscommInetAddrPrefixOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 23), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrefixOper.setStatus('current')
nbsSyscommGateAddrAdmin = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 30), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyscommGateAddrAdmin.setStatus('current')
nbsSyscommGateAddrOper = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 3, 31), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommGateAddrOper.setStatus('current')
nbsSyscommInetAddrPrior = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 100, 311), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommInetAddrPrior.setStatus('current')
nbsSyscommGateAddrPrior = MibScalar((1, 3, 6, 1, 4, 1, 629, 214, 100, 331), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyscommGateAddrPrior.setStatus('current')
nbsSyscommInetCfgChanging = NotificationType((1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 30)).setObjects(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrAdmin"), ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrAdmin"))
if mibBuilder.loadTexts: nbsSyscommInetCfgChanging.setStatus('current')
nbsSyscommInetCfgChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 214, 100, 0, 31)).setObjects(("NBS-SYSCOMM-MIB", "nbsSyscommInetAddrPrior"), ("NBS-SYSCOMM-MIB", "nbsSyscommGateAddrPrior"))
if mibBuilder.loadTexts: nbsSyscommInetCfgChanged.setStatus('current')
mibBuilder.exportSymbols("NBS-SYSCOMM-MIB", nbsSyscommInetCfgChanging=nbsSyscommInetCfgChanging, PYSNMP_MODULE_ID=nbsSyscommMib, nbsSyscommEventGrp=nbsSyscommEventGrp, nbsSyscommInetSlaacAddr=nbsSyscommInetSlaacAddr, nbsSyscommInetSlaacAddrPrefix=nbsSyscommInetSlaacAddrPrefix, nbsSyscommInetAddrPrefixAdmin=nbsSyscommInetAddrPrefixAdmin, nbsSyscommMib=nbsSyscommMib, nbsSyscommEvents=nbsSyscommEvents, nbsSyscommInetAddrAdmin=nbsSyscommInetAddrAdmin, nbsSyscommInetAddrOper=nbsSyscommInetAddrOper, nbsSyscommInetGrp=nbsSyscommInetGrp, nbsSyscommGateAddrAdmin=nbsSyscommGateAddrAdmin, nbsSyscommGateAddrOper=nbsSyscommGateAddrOper, nbsSyscommInetAddrPrior=nbsSyscommInetAddrPrior, nbsSyscommGateAddrPrior=nbsSyscommGateAddrPrior, nbsSyscommInetAddrPrefixOper=nbsSyscommInetAddrPrefixOper, nbsSyscommInetCfgChanged=nbsSyscommInetCfgChanged)
