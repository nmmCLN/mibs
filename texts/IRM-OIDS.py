#
# PySNMP MIB module IRM-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/IRM-OIDS
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, IpAddress, Counter32, iso, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "IpAddress", "Counter32", "iso", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
layerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1))
repeater = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2))
bridge = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 4))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 5))
subsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6))
commonRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 1))
sysOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2))
repeaterRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 1))
repeaterRev2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 2))
subSysMMAC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1))
subSysDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2))
ups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 3))
dl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 4))
backplaneProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5))
nb30Rev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12))
sysOtherType = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 1))
sysChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2))
sysRepeaters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3))
sysBridges = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 4))
sysRouters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 5))
sysIntDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 6))
mibBuilder.exportSymbols("IRM-OIDS", layerMgmt=layerMgmt, commsDevice=commsDevice, router=router, repeater=repeater, nb30Rev1=nb30Rev1, sysRouters=sysRouters, product=product, backplaneProtocol=backplaneProtocol, ups=ups, subsystem=subsystem, sysBridges=sysBridges, sysRepeaters=sysRepeaters, bridge=bridge, dl=dl, subSysMMAC=subSysMMAC, sysOIDs=sysOIDs, common=common, commonRev1=commonRev1, repeaterRev1=repeaterRev1, subSysDevice=subSysDevice, repeaterRev2=repeaterRev2, sysOtherType=sysOtherType, sysChassis=sysChassis, sysIntDev=sysIntDev)
