#
# PySNMP MIB module ALTEON-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alteonos/ALTEON-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:32 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, iso, Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, NotificationType, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "iso", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Counter64", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alteon = MibIdentifier((1, 3, 6, 1, 4, 1, 1872))
registration2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1))
private_mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2)).setLabel("private-mibs")
personalContentCache = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 3))
ics = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 3, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 1))
gs_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 2)).setLabel("gs-switch")
isd = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3))
switch_chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4)).setLabel("switch-chassis")
aws_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 5)).setLabel("aws-switch")
chassis_8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4, 1)).setLabel("chassis-8600")
wsm4Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 4, 1, 2))
platform = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 1))
sslOffload = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 2))
firewall = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 3))
contentDirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 2, 3, 4))
aceswitch110 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 1))
acedirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 2))
aceswitch180 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 3))
acedirector2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 4))
aceswitch180e = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 5))
acedirector3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 6))
cachedirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 7))
gs_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8)).setLabel("gs-switches")
aceswitch184 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 9))
acedirector4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 10))
isd_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11)).setLabel("isd-reg")
webswitch_module = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 12)).setLabel("webswitch-module")
aws_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13)).setLabel("aws-switches")
alteonLinkOptimizer = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 14))
wsm_BladeCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 15)).setLabel("wsm-BladeCenter")
alteonLinkOptimizer143 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 16))
alteonLinkOptimizer150 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 17))
ibm_BladeCenterL3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18)).setLabel("ibm-BladeCenterL3")
copperModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18, 1))
fiberModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 18, 2))
aws2000_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1)).setLabel("aws2000-switches")
aws3000_switches = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2)).setLabel("aws3000-switches")
aws2424 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 1))
aws2448 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 2))
aws2224 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 3))
aas2424s = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 4))
aas2208 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 5))
aas2216 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 6))
aws2424E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 7))
aas2424sE5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 8))
aas2208E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 9))
aas2216E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 1, 10))
aws3408 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 1))
aws3416 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 2))
aws3408E5 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 13, 2, 3))
chas_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1)).setLabel("chas-switch")
chas_switch_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1)).setLabel("chas-switch-reg")
alteon708 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 1, 1))
chas_switch_comp_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2)).setLabel("chas-switch-comp-reg")
alteonACPowerSupply7xx = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 1))
alteonDCPowerSupply7xx = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 2))
alteonFan708 = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 3))
alteonModuleMP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 5))
alteonModuleSF = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 6))
alteonModuleFE_UTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 7)).setLabel("alteonModuleFE-UTP")
alteonModuleGE_SX = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 8)).setLabel("alteonModuleGE-SX")
alteonModuleGE_UTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 8, 1, 2, 9)).setLabel("alteonModuleGE-UTP")
alteonContentDirector = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 1))
alteonSSLOffload = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 2))
alteonPersonalContentCache = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 3))
alteonFirewall = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 4))
alteonWSS = MibIdentifier((1, 3, 6, 1, 4, 1, 1872, 1, 11, 5))
mibBuilder.exportSymbols("ALTEON-ROOT-MIB", chas_switch=chas_switch, aws3408E5=aws3408E5, acedirector4=acedirector4, alteonACPowerSupply7xx=alteonACPowerSupply7xx, wsm_BladeCenter=wsm_BladeCenter, acedirector2=acedirector2, aws2000_switches=aws2000_switches, contentDirector=contentDirector, gs_switches=gs_switches, aceswitch180=aceswitch180, alteonFan708=alteonFan708, alteonFirewall=alteonFirewall, acedirector3=acedirector3, aas2216=aas2216, alteonPersonalContentCache=alteonPersonalContentCache, switch=switch, switch_chassis=switch_chassis, aws_switch=aws_switch, alteonLinkOptimizer=alteonLinkOptimizer, aws2424E5=aws2424E5, aas2424sE5=aas2424sE5, registration2=registration2, webswitch_module=webswitch_module, alteonWSS=alteonWSS, alteonModuleSF=alteonModuleSF, alteonDCPowerSupply7xx=alteonDCPowerSupply7xx, aws3000_switches=aws3000_switches, chassis_8600=chassis_8600, isd=isd, alteonContentDirector=alteonContentDirector, ics=ics, sslOffload=sslOffload, aws2448=aws2448, aceswitch184=aceswitch184, gs_switch=gs_switch, private_mibs=private_mibs, aws_switches=aws_switches, copperModule=copperModule, aas2216E5=aas2216E5, aws2424=aws2424, ibm_BladeCenterL3=ibm_BladeCenterL3, chas_switch_comp_reg=chas_switch_comp_reg, personalContentCache=personalContentCache, alteonLinkOptimizer143=alteonLinkOptimizer143, aceswitch110=aceswitch110, aws3408=aws3408, alteonModuleFE_UTP=alteonModuleFE_UTP, alteon708=alteon708, acedirector=acedirector, alteonModuleMP=alteonModuleMP, alteonModuleGE_SX=alteonModuleGE_SX, alteonLinkOptimizer150=alteonLinkOptimizer150, alteon=alteon, aas2208E5=aas2208E5, alteonModuleGE_UTP=alteonModuleGE_UTP, aas2208=aas2208, wsm4Traps=wsm4Traps, firewall=firewall, fiberModule=fiberModule, isd_reg=isd_reg, aws2224=aws2224, aas2424s=aas2424s, platform=platform, aws3416=aws3416, cachedirector=cachedirector, chas_switch_reg=chas_switch_reg, alteonSSLOffload=alteonSSLOffload, aceswitch180e=aceswitch180e)
