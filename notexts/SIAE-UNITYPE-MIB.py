#
# PySNMP MIB module SIAE-UNITYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-UNITYPE-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:15:37 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, iso, ModuleIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, IpAddress, Unsigned32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "ModuleIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
unitTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 506))
unitTypeMib.setRevisions(('2016-10-14 00:00', '2016-07-19 00:00', '2016-04-05 00:00', '2015-03-04 00:00', '2014-12-01 00:00', '2014-03-19 00:00', '2014-02-07 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: unitTypeMib.setLastUpdated('201607190000Z')
if mibBuilder.loadTexts: unitTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
unitType = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3))
unitTypeUnequipped = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))
if mibBuilder.loadTexts: unitTypeUnequipped.setStatus('current')
unitTypeODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 5))
if mibBuilder.loadTexts: unitTypeODU.setStatus('current')
unitTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 200))
if mibBuilder.loadTexts: unitTypeALFO80HD.setStatus('current')
unitTypeALFO80HDelectrical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 201))
if mibBuilder.loadTexts: unitTypeALFO80HDelectrical.setStatus('current')
unitTypeALFO80HDelectricalOptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 202))
if mibBuilder.loadTexts: unitTypeALFO80HDelectricalOptical.setStatus('current')
unitTypeALFO80HDoptical = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 203))
if mibBuilder.loadTexts: unitTypeALFO80HDoptical.setStatus('current')
unitTypeAGS20ARI1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 210))
if mibBuilder.loadTexts: unitTypeAGS20ARI1.setStatus('current')
unitTypeAGS20ARI2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 211))
if mibBuilder.loadTexts: unitTypeAGS20ARI2.setStatus('current')
unitTypeAGS20ARI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 212))
if mibBuilder.loadTexts: unitTypeAGS20ARI4.setStatus('current')
unitTypeAGS20DRI4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 213))
if mibBuilder.loadTexts: unitTypeAGS20DRI4.setStatus('current')
unitTypeAGS20ARI1TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 214))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2.setStatus('current')
unitTypeAGS20ARI1TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 215))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3.setStatus('current')
unitTypeAGS20ARI2TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 216))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2.setStatus('current')
unitTypeAGS20ARI2TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 217))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3.setStatus('current')
unitTypeAGS20ARI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 218))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2.setStatus('current')
unitTypeAGS20ARI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 219))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3.setStatus('current')
unitTypeAGS20DRI4TDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 220))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM2.setStatus('current')
unitTypeAGS20DRI4TDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 221))
if mibBuilder.loadTexts: unitTypeAGS20DRI4TDM3.setStatus('current')
unitTypeAGS20CORE = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 222))
if mibBuilder.loadTexts: unitTypeAGS20CORE.setStatus('current')
unitTypeAGS20ARI1DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 223))
if mibBuilder.loadTexts: unitTypeAGS20ARI1DP.setStatus('current')
unitTypeAGS20ARI1TDM2DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 224))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2DP.setStatus('current')
unitTypeAGS20ARI1TDM3DP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 225))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM3DP.setStatus('current')
unitTypeALFOplus1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 229))
if mibBuilder.loadTexts: unitTypeALFOplus1.setStatus('current')
unitTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 230))
if mibBuilder.loadTexts: unitTypeALFOplus2.setStatus('current')
unitTypeAGS20ODU = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 231))
if mibBuilder.loadTexts: unitTypeAGS20ODU.setStatus('current')
unitTypeAGS20ARI1TDM2LC = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 240))
if mibBuilder.loadTexts: unitTypeAGS20ARI1TDM2LC.setStatus('current')
unitTypeAGS20ARI2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 250))
if mibBuilder.loadTexts: unitTypeAGS20ARI2XG.setStatus('current')
unitTypeAGS20ARI2TDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 251))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM2XG.setStatus('current')
unitTypeAGS20ARI2TDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 252))
if mibBuilder.loadTexts: unitTypeAGS20ARI2TDM3XG.setStatus('current')
unitTypeAGS20ARI4XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 253))
if mibBuilder.loadTexts: unitTypeAGS20ARI4XG.setStatus('current')
unitTypeAGS20ARI4TDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 254))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM2XG.setStatus('current')
unitTypeAGS20ARI4TDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 255))
if mibBuilder.loadTexts: unitTypeAGS20ARI4TDM3XG.setStatus('current')
unitTypeAGS20ARI2E = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 260))
if mibBuilder.loadTexts: unitTypeAGS20ARI2E.setStatus('current')
unitTypeAGS20ARI2ETDM2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 261))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2.setStatus('current')
unitTypeAGS20ARI2ETDM3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 262))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3.setStatus('current')
unitTypeAGS20ARI2EXG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 263))
if mibBuilder.loadTexts: unitTypeAGS20ARI2EXG.setStatus('current')
unitTypeAGS20ARI2ETDM2XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 264))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM2XG.setStatus('current')
unitTypeAGS20ARI2ETDM3XG = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 265))
if mibBuilder.loadTexts: unitTypeAGS20ARI2ETDM3XG.setStatus('current')
unitTypeALFO80HDx = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 280))
if mibBuilder.loadTexts: unitTypeALFO80HDx.setStatus('current')
mibBuilder.exportSymbols("SIAE-UNITYPE-MIB", unitTypeAGS20ARI4TDM3=unitTypeAGS20ARI4TDM3, unitTypeAGS20ARI4XG=unitTypeAGS20ARI4XG, unitTypeAGS20ARI1=unitTypeAGS20ARI1, unitTypeAGS20ARI1DP=unitTypeAGS20ARI1DP, unitTypeAGS20CORE=unitTypeAGS20CORE, unitTypeAGS20DRI4=unitTypeAGS20DRI4, unitTypeAGS20ARI4TDM2=unitTypeAGS20ARI4TDM2, unitTypeAGS20ARI2ETDM3=unitTypeAGS20ARI2ETDM3, unitTypeALFO80HDx=unitTypeALFO80HDx, unitTypeAGS20ARI2ETDM2=unitTypeAGS20ARI2ETDM2, unitTypeMib=unitTypeMib, unitTypeALFOplus2=unitTypeALFOplus2, unitTypeAGS20ARI4TDM2XG=unitTypeAGS20ARI4TDM2XG, unitTypeALFO80HDoptical=unitTypeALFO80HDoptical, unitTypeAGS20ARI2ETDM3XG=unitTypeAGS20ARI2ETDM3XG, unitTypeAGS20DRI4TDM3=unitTypeAGS20DRI4TDM3, unitTypeAGS20ARI4=unitTypeAGS20ARI4, unitTypeALFO80HDelectrical=unitTypeALFO80HDelectrical, unitTypeUnequipped=unitTypeUnequipped, unitTypeAGS20ARI2=unitTypeAGS20ARI2, unitTypeAGS20ARI1TDM2LC=unitTypeAGS20ARI1TDM2LC, unitTypeAGS20ARI2TDM2XG=unitTypeAGS20ARI2TDM2XG, unitTypeODU=unitTypeODU, unitTypeAGS20ARI1TDM3DP=unitTypeAGS20ARI1TDM3DP, unitTypeAGS20ARI4TDM3XG=unitTypeAGS20ARI4TDM3XG, unitTypeAGS20ODU=unitTypeAGS20ODU, unitTypeAGS20ARI2TDM2=unitTypeAGS20ARI2TDM2, PYSNMP_MODULE_ID=unitTypeMib, unitTypeAGS20ARI1TDM2DP=unitTypeAGS20ARI1TDM2DP, unitTypeALFOplus1=unitTypeALFOplus1, unitTypeAGS20ARI1TDM2=unitTypeAGS20ARI1TDM2, unitTypeAGS20ARI2EXG=unitTypeAGS20ARI2EXG, unitTypeAGS20ARI1TDM3=unitTypeAGS20ARI1TDM3, unitTypeALFO80HD=unitTypeALFO80HD, unitTypeAGS20DRI4TDM2=unitTypeAGS20DRI4TDM2, unitTypeAGS20ARI2TDM3XG=unitTypeAGS20ARI2TDM3XG, unitTypeAGS20ARI2TDM3=unitTypeAGS20ARI2TDM3, unitTypeAGS20ARI2XG=unitTypeAGS20ARI2XG, unitTypeAGS20ARI2ETDM2XG=unitTypeAGS20ARI2ETDM2XG, unitTypeAGS20ARI2E=unitTypeAGS20ARI2E, unitType=unitType, unitTypeALFO80HDelectricalOptical=unitTypeALFO80HDelectricalOptical)
