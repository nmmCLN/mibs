#
# PySNMP MIB module WATCHGUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/WATCHGUARD-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 07:41:52 2022
# On host fv-az190-632 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, IpAddress, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "Bits", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
watchguard = MibIdentifier((1, 3, 6, 1, 4, 1, 3097))
wgProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1))
fbXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4))
fbX500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 1))
fbX550e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 2))
fbX700 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 3))
fbX750e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 4))
fbX750e_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 5)).setLabel("fbX750e-4")
fbX1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 6))
fbX1250e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 7))
fbX1250e_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 8)).setLabel("fbX1250e-4")
fbX2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 9))
fbX5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 10))
fbX5500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 11))
fbX6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 12))
fbX6500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 13))
fbX8000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 14))
fbX8500e = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 15))
fbX8500e_F = MibIdentifier((1, 3, 6, 1, 4, 1, 3097, 1, 4, 16)).setLabel("fbX8500e-F")
mibBuilder.exportSymbols("WATCHGUARD-MIB", fbX6500e=fbX6500e, fbX500=fbX500, watchguard=watchguard, fbX550e=fbX550e, fbXSeries=fbXSeries, fbX1000=fbX1000, fbX1250e=fbX1250e, fbX5000=fbX5000, fbX750e_4=fbX750e_4, fbX8500e=fbX8500e, fbX2500=fbX2500, fbX5500e=fbX5500e, fbX6000=fbX6000, fbX750e=fbX750e, fbX700=fbX700, fbX1250e_4=fbX1250e_4, fbX8000=fbX8000, wgProducts=wgProducts, fbX8500e_F=fbX8500e_F)
