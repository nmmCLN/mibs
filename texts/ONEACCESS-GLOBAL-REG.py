#
# PySNMP MIB module ONEACCESS-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-GLOBAL-REG
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:28 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, Counter32, Bits, iso, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter32", "Bits", "iso", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oneAccessMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 1))
oneAccessMIBModule.setRevisions(('2015-04-21 00:00', '2014-09-05 00:00', '2013-10-16 00:00', '2013-06-25 00:00', '2013-04-25 00:00', '2012-03-20 00:00', '2011-07-29 00:00', '2011-06-15 00:00', '2011-04-10 00:01', '2010-08-10 00:01', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oneAccessMIBModule.setRevisionsDescriptions(('Add new device One445 see PR 74321', 'Add new devices oacLbb139, oacLbb148, oacLbb219, oacLbb329 see PR 73077', 'Update for 1440, Add new devices oacLbb133, oacLbb134, oacLbb140, oacLbb210, oacLbb310, oacLbb320, oacLbb330 , oacLbb4G ... see PR 65655', 'Add oacOneOsDevice for Lbbxxx  see PR 60762', 'Add oacOneOsDevice for one540,one1540,one1510,one1520  see PR 60762', 'Reserved the sub-tree 11 to new MIB oacExpIMIPVrfToIf  see PR 49262', 'fixed compilation issues', 'Contact updated', 'Add oacVlanConfig oacBridgeObjects oacIpServicesConfig ', 'Add oacOneOsDevice for 1440.', 'Initial version.',))
if mibBuilder.loadTexts: oneAccessMIBModule.setLastUpdated('201504210000Z')
if mibBuilder.loadTexts: oneAccessMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oneAccessMIBModule.setContactInfo('Pascal KESTELOOT\n            Postal: ONE ACCESS\n                    381 Avenue du General de Gaulle\n                    92140 Clamart, France\n\t\t    FRANCE\n\n            Tel: (+33) 01 41 87 70 00\n            Fax: (+33) 01 41 87 74 00\n\n            E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oneAccessMIBModule.setDescription('This MIB module describes the top-level ONEACCESS\n\t       \tarchitecture\n\t\tProducts sysObjectId are under oacRegistration\n\t\tModules registrations are under oacRegistration.oacMIBModules\n\t\tProduct Specicific MIBs are under oacProductSpecific\n\t\tGeneric MIBs common to several products are under\n\t\toacGeneric')
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
mibBuilder.exportSymbols("ONEACCESS-GLOBAL-REG", oacExpIMIPSec=oacExpIMIPSec, oacLbb142=oacLbb142, oacPBXPLUG_1P_2B=oacPBXPLUG_1P_2B, oacLbb135=oacLbb135, oacExpIMVrrpNotifications=oacExpIMVrrpNotifications, oacExpIMIpVrrp=oacExpIMIpVrrp, oacLbb131=oacLbb131, oacExpIMAtmOamStatistics=oacExpIMAtmOamStatistics, oacOne445=oacOne445, oacPBXPLUG_4B=oacPBXPLUG_4B, oacPBXPLUG_6B_L=oacPBXPLUG_6B_L, oacLbb134=oacLbb134, oacMIBModules=oacMIBModules, oacOne1540=oacOne1540, oacOne425=oacOne425, oacExpIMEvents=oacExpIMEvents, oacExpIMIpNat=oacExpIMIpNat, oacOneCell35=oacOneCell35, oacExpIMIsdn=oacExpIMIsdn, oacOne10=oacOne10, oacExpIMAtmAal5=oacExpIMAtmAal5, oacLbb236=oacLbb236, oneAccessMIBModule=oneAccessMIBModule, oacExpIMAtm=oacExpIMAtm, oacLbb329=oacLbb329, oacLbb133=oacLbb133, oacOne70=oacOne70, oacOne80=oacOne80, oacOne20=oacOne20, oacExpIMIpNatStatistics=oacExpIMIpNatStatistics, oacExpIMIsdnNotifications=oacExpIMIsdnNotifications, oacExpInternetDrafts=oacExpInternetDrafts, oacOne60=oacOne60, oacOne1560=oacOne1560, oacLbb210=oacLbb210, oacExpIMVoice=oacExpIMVoice, oacOneOsDevices=oacOneOsDevices, oacCapabilities=oacCapabilities, oacOne400=oacOne400, oacOne540=oacOne540, oneAccess=oneAccess, oacPBXPLUG_1P_2B_L=oacPBXPLUG_1P_2B_L, oacOne200=oacOne200, oacLbb320=oacLbb320, oacOne1510=oacOne1510, oacExpInternalModules=oacExpInternalModules, oacExpIMPstn=oacExpIMPstn, oacPBXPLUG_6B=oacPBXPLUG_6B, oacLbb230=oacLbb230, oacLbb148=oacLbb148, oacOne1520=oacOne1520, oacExpIMAtmStatistics=oacExpIMAtmStatistics, oacOne300=oacOne300, oacLbb139=oacLbb139, oacOne560=oacOne560, oacEmbeddedAgentMIB=oacEmbeddedAgentMIB, oacExpIMManagement=oacExpIMManagement, oacOneCell25=oacOneCell25, oacExpIMIpAclStatistics=oacExpIMIpAclStatistics, oacLbb330=oacLbb330, oacPBXPLUG_4B_V2=oacPBXPLUG_4B_V2, oacOne700=oacOne700, oacOne50=oacOne50, oacLbb310=oacLbb310, oacLbb140=oacLbb140, oacGenProtocols=oacGenProtocols, oacExpIMZbFw=oacExpIMZbFw, oacPBXplug8=oacPBXplug8, oacOne90=oacOne90, oacOne800=oacOne800, oacPBXplug30=oacPBXplug30, oacProductSpecific=oacProductSpecific, oacExpIMCellRadio=oacExpIMCellRadio, oacExpIMDot11=oacExpIMDot11, oacLbb4G=oacLbb4G, oac1440=oac1440, oacRegistration=oacRegistration, PYSNMP_MODULE_ID=oneAccessMIBModule, oacOne410=oacOne410, oacOne40=oacOne40, oacExpIMEthernet=oacExpIMEthernet, oacPBXPLUG_4B_L=oacPBXPLUG_4B_L, oacRequirements=oacRequirements, oacOne150=oacOne150, oacExpIMPstnNotifications=oacExpIMPstnNotifications, oacOne420=oacOne420, oacLbb219=oacLbb219, oacGeneric=oacGeneric, oacOne100=oacOne100, oacExpIMVoiceGlobalStat=oacExpIMVoiceGlobalStat, oacExpIMIPPerformanceCounters=oacExpIMIPPerformanceCounters, oacOne20D=oacOne20D, oacLbb231=oacLbb231, oacExpIMSystem=oacExpIMSystem, oacExpIMIp=oacExpIMIp, oacExperimental=oacExperimental, oacGenManagement=oacGenManagement, oacExpNewMIBs=oacExpNewMIBs, oacExpIMIpAcl=oacExpIMIpAcl, oacLbb132=oacLbb132, oacLbb141=oacLbb141, oacOne100D=oacOne100D, oacExpIMIpNatNotifications=oacExpIMIpNatNotifications, oacExpIMPing=oacExpIMPing, oacOne180=oacOne180, oacOne80XM=oacOne80XM, oacLbb130=oacLbb130, oacOne30=oacOne30)
