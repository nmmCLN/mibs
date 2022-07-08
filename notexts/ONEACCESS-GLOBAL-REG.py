#
# PySNMP MIB module ONEACCESS-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-GLOBAL-REG
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:27 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Gauge32, MibIdentifier, IpAddress, iso, Bits, NotificationType, Counter64, ModuleIdentity, Integer32, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "iso", "Bits", "NotificationType", "Counter64", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oneAccessMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 1))
oneAccessMIBModule.setRevisions(('2015-04-21 00:00', '2014-09-05 00:00', '2013-10-16 00:00', '2013-06-25 00:00', '2013-04-25 00:00', '2012-03-20 00:00', '2011-07-29 00:00', '2011-06-15 00:00', '2011-04-10 00:01', '2010-08-10 00:01', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oneAccessMIBModule.setLastUpdated('201504210000Z')
if mibBuilder.loadTexts: oneAccessMIBModule.setOrganization(' OneAccess ')
oneAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 13191))
oacRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1))
oacMIBModules = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 100))
oacOneOsDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1))
oacOne10 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1))
oacOne20 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 2))
oacOne30 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 3))
oacOne40 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 4))
oacOne50 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 5))
oacOne60 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 6))
oacOne20D = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 7))
oacOne80 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 8))
oacOne80XM = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 9))
oacOne100 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 10))
oacOne100D = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 11))
oacOne150 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 15))
oacOne180 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 18))
oacOne200 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 20))
oacOneCell25 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 25))
oacOne300 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 30))
oacOneCell35 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 35))
oacOne400 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 40))
oacOne70 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 70))
oacOne800 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 80))
oacPBXplug8 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 100))
oacPBXplug30 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 110))
oacPBXPLUG_1P_2B = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 111)).setLabel("oacPBXPLUG-1P-2B")
oacPBXPLUG_1P_2B_L = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 112)).setLabel("oacPBXPLUG-1P-2B-L")
oacPBXPLUG_4B = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 113)).setLabel("oacPBXPLUG-4B")
oacPBXPLUG_4B_L = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 114)).setLabel("oacPBXPLUG-4B-L")
oacPBXPLUG_4B_V2 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 115)).setLabel("oacPBXPLUG-4B-V2")
oacPBXPLUG_6B = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 116)).setLabel("oacPBXPLUG-6B")
oacPBXPLUG_6B_L = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 117)).setLabel("oacPBXPLUG-6B-L")
oac1440 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1440))
oacOne90 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 90))
oacLbb130 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 130))
oacLbb131 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 131))
oacLbb132 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 132))
oacLbb133 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 133))
oacLbb134 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 134))
oacLbb135 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 135))
oacLbb139 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 139))
oacLbb140 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 140))
oacLbb141 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 141))
oacLbb142 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 142))
oacLbb148 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 148))
oacLbb210 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 210))
oacLbb219 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 219))
oacLbb230 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 230))
oacLbb231 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 231))
oacLbb236 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 236))
oacLbb310 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 310))
oacLbb320 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 320))
oacLbb329 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 329))
oacLbb330 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 330))
oacOne410 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 410))
oacOne420 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 420))
oacOne425 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 425))
oacOne445 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 445))
oacOne540 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 540))
oacOne560 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 560))
oacOne700 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 700))
oacLbb4G = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1000))
oacOne1540 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1540))
oacOne1510 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1510))
oacOne1520 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1520))
oacOne1560 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 1, 1, 1560))
oacProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 2))
oacGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 3))
oacGenProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 3, 1))
oacGenManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 3, 10))
oacEmbeddedAgentMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 3, 10, 1))
oacCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 4))
oacRequirements = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 5))
oacExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10))
oacExpNewMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 1))
oacExpInternetDrafts = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 2))
oacExpInternalModules = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3))
oacExpIMIp = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1))
oacExpIMAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2))
oacExpIMSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 3))
oacExpIMManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4))
oacExpIMEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2))
oacExpIMPing = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3))
oacExpIMVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 5))
oacExpIMPstn = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6))
oacExpIMPstnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0))
oacExpIMIsdn = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7))
oacExpIMIsdnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 7, 0))
oacExpIMVoiceGlobalStat = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 5, 1))
oacExpIMAtmStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1))
oacExpIMAtmOamStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 2))
oacExpIMAtmAal5 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 3))
oacExpIMIpNat = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1))
oacExpIMIpNatStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1))
oacExpIMIpNatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 2))
oacExpIMIpAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2))
oacExpIMIpAclStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1))
oacExpIMIpVrrp = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5))
oacExpIMVrrpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1))
oacExpIMIPSec = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 4))
oacExpIMIPPerformanceCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 10))
oacExpIMDot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 8))
oacExpIMCellRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9))
oacExpIMEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 10))
oacExpIMZbFw = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9))
mibBuilder.exportSymbols("ONEACCESS-GLOBAL-REG", oacExpIMIpVrrp=oacExpIMIpVrrp, oacLbb231=oacLbb231, oacLbb148=oacLbb148, oacExpIMIPSec=oacExpIMIPSec, oacLbb320=oacLbb320, oacOne30=oacOne30, oacExpIMIsdnNotifications=oacExpIMIsdnNotifications, oacExperimental=oacExperimental, oacOne60=oacOne60, oacOne1540=oacOne1540, oacOne20D=oacOne20D, oacOne1510=oacOne1510, oacPBXPLUG_4B_L=oacPBXPLUG_4B_L, oacPBXPLUG_6B_L=oacPBXPLUG_6B_L, oacOne10=oacOne10, oacLbb135=oacLbb135, oacLbb142=oacLbb142, oacOne420=oacOne420, oacLbb210=oacLbb210, oacLbb4G=oacLbb4G, oacExpIMAtmOamStatistics=oacExpIMAtmOamStatistics, oacOneCell25=oacOneCell25, oacExpIMIPPerformanceCounters=oacExpIMIPPerformanceCounters, oacOne560=oacOne560, oacExpIMVoiceGlobalStat=oacExpIMVoiceGlobalStat, oacExpIMZbFw=oacExpIMZbFw, oacPBXPLUG_4B_V2=oacPBXPLUG_4B_V2, oacOne180=oacOne180, oacMIBModules=oacMIBModules, oacExpIMPstn=oacExpIMPstn, oacExpIMIpNatNotifications=oacExpIMIpNatNotifications, oacOne800=oacOne800, oacLbb134=oacLbb134, oacOneCell35=oacOneCell35, oacPBXplug30=oacPBXplug30, oacExpIMAtm=oacExpIMAtm, oacOne40=oacOne40, oacOne20=oacOne20, oacExpIMPing=oacExpIMPing, oacLbb132=oacLbb132, oacLbb140=oacLbb140, PYSNMP_MODULE_ID=oneAccessMIBModule, oacLbb139=oacLbb139, oacOne90=oacOne90, oacExpIMEvents=oacExpIMEvents, oacOne425=oacOne425, oacExpIMSystem=oacExpIMSystem, oneAccess=oneAccess, oacOne1520=oacOne1520, oacOne700=oacOne700, oacOne1560=oacOne1560, oacOne150=oacOne150, oneAccessMIBModule=oneAccessMIBModule, oacPBXplug8=oacPBXplug8, oacExpIMIpAclStatistics=oacExpIMIpAclStatistics, oacOneOsDevices=oacOneOsDevices, oacOne50=oacOne50, oacOne300=oacOne300, oacExpIMAtmAal5=oacExpIMAtmAal5, oacOne445=oacOne445, oacPBXPLUG_4B=oacPBXPLUG_4B, oacPBXPLUG_6B=oacPBXPLUG_6B, oacRequirements=oacRequirements, oacExpIMIpNat=oacExpIMIpNat, oacLbb310=oacLbb310, oacGenProtocols=oacGenProtocols, oacExpIMIsdn=oacExpIMIsdn, oacLbb329=oacLbb329, oacExpIMPstnNotifications=oacExpIMPstnNotifications, oacProductSpecific=oacProductSpecific, oacExpIMIpAcl=oacExpIMIpAcl, oacExpIMEthernet=oacExpIMEthernet, oacExpIMVoice=oacExpIMVoice, oacOne410=oacOne410, oacGenManagement=oacGenManagement, oacOne80=oacOne80, oacEmbeddedAgentMIB=oacEmbeddedAgentMIB, oacLbb130=oacLbb130, oacLbb133=oacLbb133, oacCapabilities=oacCapabilities, oacExpIMIp=oacExpIMIp, oacExpNewMIBs=oacExpNewMIBs, oacOne80XM=oacOne80XM, oac1440=oac1440, oacOne400=oacOne400, oacExpInternetDrafts=oacExpInternetDrafts, oacExpInternalModules=oacExpInternalModules, oacLbb330=oacLbb330, oacPBXPLUG_1P_2B=oacPBXPLUG_1P_2B, oacExpIMAtmStatistics=oacExpIMAtmStatistics, oacOne540=oacOne540, oacLbb236=oacLbb236, oacExpIMVrrpNotifications=oacExpIMVrrpNotifications, oacRegistration=oacRegistration, oacExpIMIpNatStatistics=oacExpIMIpNatStatistics, oacPBXPLUG_1P_2B_L=oacPBXPLUG_1P_2B_L, oacExpIMDot11=oacExpIMDot11, oacOne100D=oacOne100D, oacExpIMManagement=oacExpIMManagement, oacLbb131=oacLbb131, oacLbb230=oacLbb230, oacLbb141=oacLbb141, oacGeneric=oacGeneric, oacExpIMCellRadio=oacExpIMCellRadio, oacLbb219=oacLbb219, oacOne100=oacOne100, oacOne200=oacOne200, oacOne70=oacOne70)
