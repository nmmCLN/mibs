#
# PySNMP MIB module WAYSTREAM-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:29:39 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, iso, MibIdentifier, ModuleIdentity, Counter32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Gauge32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Gauge32", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wsProduct, wsModules = mibBuilder.importSymbols("WAYSTREAM-SMI", "wsProduct", "wsModules")
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
mibBuilder.exportSymbols("WAYSTREAM-PRODUCTS-MIB", asr4216FM=asr4216FM, mpc480me4818t=mpc480me4818t, mpc480re4818=mpc480re4818, asr3108VDSL=asr3108VDSL, asr4116C=asr4116C, asr4624SFSco=asr4624SFSco, mpc480se4818=mpc480se4818, asr4516SFM=asr4516SFM, asr4324FV=asr4324FV, asr4108C=asr4108C, ms3128dc=ms3128dc, asr4608SFS=asr4608SFS, ms4026ac=ms4026ac, asr5224FMdcco=asr5224FMdcco, se2=se2, asr4516SFMco=asr4516SFMco, asr4524SFMco=asr4524SFMco, mpc480me4818=mpc480me4818, asr4624SFS=asr4624SFS, asr4316FVco=asr4316FVco, asr4724SFLco=asr4724SFLco, asr4416SFV=asr4416SFV, asr4716SFLco=asr4716SFLco, reserved4=reserved4, asr=asr, asr4724SFL=asr4724SFL, ms=ms, asr4316FV=asr4316FV, se1=se1, asr4424SFV=asr4424SFV, asr4124C=asr4124C, asr3316VDSL=asr3316VDSL, asr3208VDSL=asr3208VDSL, asr4324FVco=asr4324FVco, asr5624FSacco=asr5624FSacco, asr4708SFL=asr4708SFL, ipd1116C=ipd1116C, reserved3=reserved3, asr4616SFS=asr4616SFS, asr4308FV=asr4308FV, asr3124VDSL=asr3124VDSL, asr5724FLacco=asr5724FLacco, asr3224VDSL=asr3224VDSL, asr10132co=asr10132co, asr5724FLdcco=asr5724FLdcco, asr4208FMco=asr4208FMco, asr4408SFV=asr4408SFV, asr5224FMacco=asr5224FMacco, asr4108Cco=asr4108Cco, asr4608SFSco=asr4608SFSco, asr3308VDSL=asr3308VDSL, asr4216FMco=asr4216FMco, asr6026ac=asr6026ac, ms3028dc=ms3028dc, asr4524SFM=asr4524SFM, mpc480re4818t=mpc480re4818t, asr6126ac=asr6126ac, PYSNMP_MODULE_ID=wsProductsMIB, asr4224FMco=asr4224FMco, asr4508SFM=asr4508SFM, legacy2=legacy2, asr4708SFLco=asr4708SFLco, asr4508SFMco=asr4508SFMco, ms4126dc=ms4126dc, asr4224FM=asr4224FM, asr6126dc=asr6126dc, asr5624FSdcco=asr5624FSdcco, legacy1=legacy1, asr3324VDSL=asr3324VDSL, ms4126ac=ms4126ac, asr5124Cacco=asr5124Cacco, wsProductsMIB=wsProductsMIB, asr4124Cco=asr4124Cco, ms4026dc=ms4026dc, ms3028ac=ms3028ac, asr6026dc=asr6026dc, asr4116Cco=asr4116Cco, mpc480se4818t=mpc480se4818t, asr3116VDSL=asr3116VDSL, reserved2=reserved2, mpc=mpc, asr4716SFL=asr4716SFL, ms3128ac=ms3128ac, asr3216VDSL=asr3216VDSL, asr4308FVco=asr4308FVco, reserved1=reserved1, ipd=ipd, asr5124Cdcco=asr5124Cdcco, asr4616SFSco=asr4616SFSco, asr4208FM=asr4208FM)
