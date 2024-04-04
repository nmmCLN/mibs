#
# PySNMP MIB module WAYSTREAM-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:24:02 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, iso, Integer32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, Counter32, Counter64, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "iso", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "Counter64", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wsModules, wsProduct = mibBuilder.importSymbols("WAYSTREAM-SMI", "wsModules", "wsProduct")
wsProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 2))
wsProductsMIB.setRevisions(('2017-02-10 11:00', '2015-04-08 14:52', '2012-09-24 14:35', '2012-02-02 15:30', '2011-12-05 11:00', '2011-06-10 13:56', '2011-01-12 13:10', '2010-05-17 14:10', '2009-04-14 12:29', '2009-03-23 10:53', '2007-05-14 12:38', '2006-01-25 13:30', '2004-10-20 14:34', '2003-11-04 00:01',))
if mibBuilder.loadTexts: wsProductsMIB.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: wsProductsMIB.setOrganization('Waystream AB')
asr = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 1))
if mibBuilder.loadTexts: asr.setStatus('current')
ipd = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 2))
if mibBuilder.loadTexts: ipd.setStatus('current')
legacy1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 3))
if mibBuilder.loadTexts: legacy1.setStatus('current')
ms = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 5))
if mibBuilder.loadTexts: ms.setStatus('current')
legacy2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 6))
if mibBuilder.loadTexts: legacy2.setStatus('current')
mpc = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 7))
if mibBuilder.loadTexts: mpc.setStatus('current')
asr4108C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 1))
asr4116C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 2))
asr4124C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 3))
asr4208FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 4))
asr4216FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 5))
asr4224FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 6))
asr4308FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 7))
asr4316FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 8))
asr4324FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 9))
asr4408SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 10))
asr4416SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 11))
asr4424SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 12))
asr4508SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 13))
asr4516SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 14))
asr4524SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 15))
asr4608SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 16))
asr4616SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 17))
asr4624SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 18))
asr3108VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 19))
asr3116VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 20))
asr3124VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 21))
asr3208VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 22))
asr3216VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 23))
asr3224VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 24))
asr3308VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 25))
asr3316VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 26))
asr3324VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 27))
asr4708SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 28))
asr4716SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 29))
asr4724SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 30))
asr4108Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 31))
asr4116Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 32))
asr4124Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 33))
asr4208FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 34))
asr4216FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 35))
asr4224FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 36))
asr4308FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 37))
asr4316FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 38))
asr4324FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 39))
asr4508SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 40))
asr4516SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 41))
asr4524SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 42))
asr4608SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 43))
asr4616SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 44))
asr4624SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 45))
asr4708SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 46))
asr4716SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 47))
asr4724SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 48))
asr10132co = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 49))
asr5124Cacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 50))
asr5124Cdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 51))
asr5224FMacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 52))
asr5224FMdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 53))
asr5624FSacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 54))
asr5624FSdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 55))
asr5724FLacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 56))
asr5724FLdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 57))
se1 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 58))
se2 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 59))
asr6026ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 60))
asr6026dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 61))
asr6126ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 62))
asr6126dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 63))
ipd1116C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 2, 1))
ms3028ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 3))
ms3028dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 4))
ms3128ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 5))
ms3128dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 6))
ms4026ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 64))
ms4026dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 65))
ms4126ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 66))
ms4126dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 67))
mpc480se4818 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 68))
mpc480se4818t = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 69))
mpc480re4818 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 70))
mpc480re4818t = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 71))
mpc480me4818 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 72))
mpc480me4818t = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 73))
reserved1 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 74))
reserved2 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 75))
reserved3 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 76))
reserved4 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 7, 77))
mibBuilder.exportSymbols("WAYSTREAM-PRODUCTS-MIB", asr3324VDSL=asr3324VDSL, asr4216FM=asr4216FM, legacy1=legacy1, asr4624SFS=asr4624SFS, asr5724FLdcco=asr5724FLdcco, asr4116C=asr4116C, asr3216VDSL=asr3216VDSL, mpc480me4818=mpc480me4818, asr4224FM=asr4224FM, asr4324FV=asr4324FV, asr3124VDSL=asr3124VDSL, asr4308FVco=asr4308FVco, asr6026dc=asr6026dc, asr4608SFSco=asr4608SFSco, asr5224FMdcco=asr5224FMdcco, asr=asr, mpc480me4818t=mpc480me4818t, PYSNMP_MODULE_ID=wsProductsMIB, se2=se2, asr4316FVco=asr4316FVco, asr4708SFL=asr4708SFL, asr4108C=asr4108C, asr4116Cco=asr4116Cco, reserved2=reserved2, ms4126ac=ms4126ac, asr5724FLacco=asr5724FLacco, asr4508SFMco=asr4508SFMco, ms3128dc=ms3128dc, asr4716SFL=asr4716SFL, asr4324FVco=asr4324FVco, asr6126ac=asr6126ac, asr5624FSacco=asr5624FSacco, asr5124Cdcco=asr5124Cdcco, reserved4=reserved4, asr4724SFL=asr4724SFL, asr4516SFMco=asr4516SFMco, asr4208FMco=asr4208FMco, ms4026ac=ms4026ac, ms3028dc=ms3028dc, mpc480re4818=mpc480re4818, mpc480re4818t=mpc480re4818t, mpc480se4818=mpc480se4818, wsProductsMIB=wsProductsMIB, asr4708SFLco=asr4708SFLco, asr4508SFM=asr4508SFM, asr4124C=asr4124C, asr4716SFLco=asr4716SFLco, asr4608SFS=asr4608SFS, ms3128ac=ms3128ac, ipd=ipd, asr5624FSdcco=asr5624FSdcco, ms=ms, asr4316FV=asr4316FV, asr4308FV=asr4308FV, asr4124Cco=asr4124Cco, asr6126dc=asr6126dc, asr3208VDSL=asr3208VDSL, asr4616SFSco=asr4616SFSco, legacy2=legacy2, asr3308VDSL=asr3308VDSL, mpc=mpc, asr3116VDSL=asr3116VDSL, asr5124Cacco=asr5124Cacco, reserved3=reserved3, asr6026ac=asr6026ac, ms3028ac=ms3028ac, asr4516SFM=asr4516SFM, asr4724SFLco=asr4724SFLco, asr4224FMco=asr4224FMco, ipd1116C=ipd1116C, asr4108Cco=asr4108Cco, reserved1=reserved1, asr4208FM=asr4208FM, asr4524SFM=asr4524SFM, asr3316VDSL=asr3316VDSL, asr4424SFV=asr4424SFV, se1=se1, asr4624SFSco=asr4624SFSco, asr10132co=asr10132co, asr3224VDSL=asr3224VDSL, asr4416SFV=asr4416SFV, asr3108VDSL=asr3108VDSL, mpc480se4818t=mpc480se4818t, asr4408SFV=asr4408SFV, ms4126dc=ms4126dc, asr4216FMco=asr4216FMco, asr4524SFMco=asr4524SFMco, ms4026dc=ms4026dc, asr4616SFS=asr4616SFS, asr5224FMacco=asr5224FMacco)
