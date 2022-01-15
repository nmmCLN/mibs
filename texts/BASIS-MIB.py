#
# PySNMP MIB module BASIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/BASIS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
stratacom, ciscoWan = mibBuilder.importSymbols("CISCOWAN-SMI", "stratacom", "ciscoWan")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, iso, Integer32, Bits, Counter32, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "Integer32", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 67))
basisMIB.setRevisions(('2003-04-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: basisMIB.setRevisionsDescriptions(('Initial version of this MIB Module.\n\n                     The content of this MIB was originally available\n                     in SMIv1 version. The MIB has been converted to\n                     SMIv2 version and descriptions of some of the objects\n                     have been modified.',))
if mibBuilder.loadTexts: basisMIB.setLastUpdated('200304040000Z')
if mibBuilder.loadTexts: basisMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: basisMIB.setContactInfo('Cisco Systems\n                     Customer Service\n\n                     Postal: 170 W Tasman Drive\n                     San Jose, CA  95134\n                     USA\n\n                     Tel: +1 800 553-NETS\n\n                     E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: basisMIB.setDescription("This MIB Contains OID subtrees used in\n                     some of the MIBs under 'stratacom' enterprise.\n                     ")
basis = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110))
par = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 130))
basisSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1))
cardGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2))
cardSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3))
basisLines = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4))
basisServices = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5))
axisDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6))
basisShelf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1, 1))
basisAsm = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1, 2))
axisRedundancy = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1, 3))
axisSvc = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1, 4))
atmLmiSignaling = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 4))
atmAddressRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 1, 4, 1))
dsx1 = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 3))
dsx3 = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 4))
x21 = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 5))
sonet = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 6))
dsx0Vism = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 7))
dsx1Line = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1))
dsx1Framing = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 2))
dsx1Plcp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 3))
dsx3Line = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 1))
dsx3Framing = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 2))
plcp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 4, 3))
cwsonetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 6, 1))
frameRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1))
frPort = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1))
frChan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2))
frPortCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1))
frPortCnfSig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2))
frPortCnfX21PortGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 3))
frPortServiceQueGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 4))
frPortCnfResPartGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 5))
frPortCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2))
frPortCntSig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2))
ausmPort = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1))
ausmPortCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1, 1))
ausmPortCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 1, 3))
ausmChan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 2))
circuitEmulation = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 3))
cesmChan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 3, 2))
sna = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4))
snaport = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1))
snaportCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 1))
snaportCnfSig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 1, 2))
snaportCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 2))
snaPortCntSig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 4, 1, 2, 2))
voice = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5))
vismPort = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2))
vismChanGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3))
vismChanCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1))
atmLines = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5))
bbInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6))
bbChan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7))
virtualInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 8))
rpmInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9))
rpmChan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10))
atmLineCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5, 1))
atmLineCntGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 5, 2))
bbIfCnf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 1))
bbIfCnfResPartGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 2))
bbIfStateGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 3))
bbIfCnt = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 6, 4))
bbChanCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 1))
bbChanStateGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 2))
bbChanCntGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 7, 3))
rpmPort = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1))
rpmChanGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1))
mibBuilder.exportSymbols("BASIS-MIB", basisSystem=basisSystem, axisDiagnostics=axisDiagnostics, atmAddressRegistration=atmAddressRegistration, dsx1Framing=dsx1Framing, dsx3Line=dsx3Line, snaportCnfSig=snaportCnfSig, frPortCnfX21PortGrp=frPortCnfX21PortGrp, snaPortCntSig=snaPortCntSig, bbIfCnfResPartGrp=bbIfCnfResPartGrp, axisRedundancy=axisRedundancy, ausmChan=ausmChan, dsx3=dsx3, frPort=frPort, ausmPortCnt=ausmPortCnt, snaportCnf=snaportCnf, snaportCnt=snaportCnt, vismChanGrp=vismChanGrp, bbIfStateGrp=bbIfStateGrp, rpmPort=rpmPort, frameRelay=frameRelay, basisMIB=basisMIB, basisServices=basisServices, frPortCnf=frPortCnf, rpmChan=rpmChan, basisLines=basisLines, sonet=sonet, basisAsm=basisAsm, ausmPort=ausmPort, virtualInterface=virtualInterface, bbIfCnf=bbIfCnf, bbChan=bbChan, bbChanStateGrp=bbChanStateGrp, cardSpecific=cardSpecific, sna=sna, atmLines=atmLines, par=par, frPortCnfResPartGrp=frPortCnfResPartGrp, frPortCntSig=frPortCntSig, dsx1Plcp=dsx1Plcp, cesmChan=cesmChan, atmLmiSignaling=atmLmiSignaling, snaport=snaport, voice=voice, x21=x21, cwsonetObjects=cwsonetObjects, bbIfCnt=bbIfCnt, axisSvc=axisSvc, atmLineCntGrp=atmLineCntGrp, dsx1=dsx1, frPortServiceQueGrp=frPortServiceQueGrp, dsx0Vism=dsx0Vism, atmLineCnfGrp=atmLineCnfGrp, rpmChanGrp=rpmChanGrp, basisShelf=basisShelf, cardGeneric=cardGeneric, vismChanCnfGrp=vismChanCnfGrp, basis=basis, dsx3Framing=dsx3Framing, PYSNMP_MODULE_ID=basisMIB, bbInterface=bbInterface, bbChanCnfGrp=bbChanCnfGrp, bbChanCntGrp=bbChanCntGrp, frChan=frChan, atm=atm, circuitEmulation=circuitEmulation, ausmPortCnf=ausmPortCnf, rpmInterface=rpmInterface, dsx1Line=dsx1Line, plcp=plcp, vismPort=vismPort, frPortCnfSig=frPortCnfSig, frPortCnt=frPortCnt)
