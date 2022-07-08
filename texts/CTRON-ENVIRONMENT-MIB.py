#
# PySNMP MIB module CTRON-ENVIRONMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENVIRONMENT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:35 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctenv, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctenv")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, ModuleIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1))
boardEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2))
psEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3))
bbuEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 4))
chEnvAmbientTemp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientTemp.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientTemp.setDescription('The ambient temperature of the room in which the chassis \n                 is located. If this sensor is broken or not supported, then\n                 this object will be set to zero. The value of this object\n                 is the actual temperature in degrees Fahrenheit * 10.')
chEnvAmbientStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientStatus.setDescription('This object reflects the status of the ambient temperature\n                 reading.')
chEnvHumidity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidity.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvHumidity.setDescription('The humidity value of the air flowing thru the chassis.\n                 The value of this object is the actual humidity * 10.')
chEnvHumidityStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("dry", 2), ("normal", 3), ("moist", 4), ("inoperative", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvHumidityStatus.setDescription('This object reflects the status of the ambient humidity\n                 reading.')
chEnvAmbientHot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientHot.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientHot.setDescription('The temperature value above which the ambient temperature\n                 is deemed to be hot.')
chEnvAmbientWarm = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientWarm.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientWarm.setDescription('The temperature value above which the ambient temperature\n                 is deemed to be warm, if it is below or equal the hot \n                 value.')
chEnvAmbientCool = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientCool.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientCool.setDescription('The temperature value below which the ambient temperature\n                 is deemed to be cool, if it is above or equal the cold\n                 value.')
chEnvAmbientCold = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientCold.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvAmbientCold.setDescription('The temperature value below which the ambient temperature\n                 is deemed to be cold.')
chEnvHumidityMoist = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityMoist.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvHumidityMoist.setDescription('The humidity value above which the chassis humidity\n                 is deemed to be moist.')
chEnvHumidityDry = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityDry.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvHumidityDry.setDescription('The humidity value below which the chassis humidity\n                 is deemed to be a static risk.')
chEnvNumFans = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvNumFans.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvNumFans.setDescription('Number of fans in a chassis.')
chEnvFanTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12), )
if mibBuilder.loadTexts: chEnvFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanTable.setDescription('A list of fans installed in this chassis.')
chEnvFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "chEnvFanID"))
if mibBuilder.loadTexts: chEnvFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanEntry.setDescription('A slot entry containing objects for a particular\n                 module.')
chEnvFanID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanID.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanID.setDescription('A unique value, in the range between 1 and and the \n                 value of chEnvNumFans.')
chEnvFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("testing", 3), ("slow", 4), ("inoperative", 5), ("off", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanStatus.setDescription('This object reflects the status of the chassis fan.')
chEnvFanAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoMode", 1), ("fullSpeed", 2), ("testingMode", 3))).clone('autoMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chEnvFanAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanAdmin.setDescription("This object is used to select the operational mode of the \n                 fan. If the value is set to 1 (auto) then fan speed is \n                 based on temperature. If the value is set to 3 (testing) \n                 then value will return to it's previous value prior to \n                 being set at 3.")
chEnvFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: chEnvFanSpeed.setDescription('The fan speed expressed as a percentage of the maximum \n                 fan speed.')
boardEnvSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1), )
if mibBuilder.loadTexts: boardEnvSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvSlotTable.setDescription('A list of networking modules installed in this chassis.')
boardEnvSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "boardEnvSlotID"))
if mibBuilder.loadTexts: boardEnvSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvSlotEntry.setDescription('A slot entry containing objects for a particular\n                 module.')
boardEnvSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvSlotID.setDescription('The slot number of a chassis slot in which this board is\n                 installed.  This object is similiar to chSlotID in the\n                 Chassis MIB.')
boardEnvTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTemp.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTemp.setDescription('The temperature of the networking board. If this sensor is \n                 broken or not supported, then this object will be set to \n                 zero. The temperature is in degrees Fahrenheit * 10.')
boardEnvTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempStatus.setDescription('This object reflects the status of the board temperature\n                 reading.')
boardEnvTempRelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("warm", 3), ("hot", 4), ("inoperative", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempRelStatus.setDescription('This object reflects the status of the board temperature\n                 reading relative to the ambient temperature.')
boardEnvShutdownAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardEnvShutdownAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvShutdownAdmin.setDescription('This object enables or disables the auto shutdown due\n                 to a temperature condition.')
boardEnvTempHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempHot.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempHot.setDescription('The temperature value above which the board temperature\n                 is deemed to be hot.')
boardEnvTempWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempWarm.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempWarm.setDescription('The temperature value above which the board temperature\n                 is deemed to be warm, if it is below or equal the hot \n                 value.')
boardEnvTempCool = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempCool.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempCool.setDescription('The temperature value below which the board temperature\n                 is deemed to be cool, if it is above or equal the cold\n                 value.')
boardEnvTempCold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempCold.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempCold.setDescription('The temperature value below which the board temperature\n                 is deemed to be cold.')
boardEnvTempRelHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelHot.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempRelHot.setDescription('The temperature value above ambient at which the board\n                 temperature is deemed to be hot relative to ambient.')
boardEnvTempRelWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelWarm.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempRelWarm.setDescription('The temperature value above ambient at which the board \n                 temperature is deemed to be warm relative to ambient, if\n                 it is below the relative hot value of boardEnvTempRelHot.')
boardEnvTempMaxFanRelHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempMaxFanRelHot.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempMaxFanRelHot.setDescription('The temperature value above ambient at which the board\n                 temperature is deemed to be hot relative to ambient, with\n                 all fans in the chassis running at there maximum speed.')
boardEnvTempMaxFanRelWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempMaxFanRelWarm.setStatus('mandatory')
if mibBuilder.loadTexts: boardEnvTempMaxFanRelWarm.setDescription('The temperature value above ambient at which the board \n                 temperature is deemed to be warm relative to ambient, if\n                 it is below the relative hot value of boardEnvTempMaxFanRelHot,\n                 with all fans in the chassis running at there maximum speed.')
psEnvSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1), )
if mibBuilder.loadTexts: psEnvSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvSlotTable.setDescription('A list of networking modules installed in this chassis.')
psEnvSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "psEnvSlotID"))
if mibBuilder.loadTexts: psEnvSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvSlotEntry.setDescription('A slot entry containing objects for a particular\n                 module.')
psEnvSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvSlotID.setDescription('The slot number of a chassis slot in which this power supply\n                 is installed.  An unique value, in the range between 1 and \n                 and the value of chNumSlots.  This object is similiar to\n                 chSlotID in the Chassis MIB.')
psEnvTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTemp.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTemp.setDescription('The temperature of the power supply. If this sensor is \n                 broken or not supported, then this object will be set to \n                 zero. The temperature is in degrees Fahrenheit * 10.')
psEnvTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTempStatus.setDescription('This object reflects the status of the power supply\n                 temperature reading.')
psEnvTempHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempHot.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTempHot.setDescription('The temperature value above which the power supply\n                 temperature is deemed to be hot.')
psEnvTempWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempWarm.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTempWarm.setDescription('The temperature value above which the power supply \n                 temperature is deemed to be warm, if it is below or\n                 equal the hot value.')
psEnvTempCool = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempCool.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTempCool.setDescription('The temperature value below which the power supply \n                 temperature is deemed to be cool, if it is above or \n                 equal the cold value.')
psEnvTempCold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempCold.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvTempCold.setDescription('The temperature value below which the power supply\n                 temperature is deemed to be cold.')
psEnvFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("testing", 3), ("slow", 4), ("inoperative", 5), ("off", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvFanStatus.setDescription('This object reflects the status of the chassis fan.')
psEnvFanAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoMode", 1), ("fullSpeed", 2), ("testingMode", 3))).clone('autoMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psEnvFanAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvFanAdmin.setDescription("This object is used to select the operational mode of the \n                 fan. If the value is set to 1 (auto) then fan speed is \n                 based on temperature. If the value is set to 3 (testing) \n                 then value will return to it's previous value prior to \n                 being set at 3.")
psEnvFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvFanSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: psEnvFanSpeed.setDescription('The fan speed expressed as a percentage of the maximum \n                 fan speed.')
mibBuilder.exportSymbols("CTRON-ENVIRONMENT-MIB", boardEnvTempRelWarm=boardEnvTempRelWarm, chEnvAmbientStatus=chEnvAmbientStatus, psEnvTempHot=psEnvTempHot, psEnvTempCold=psEnvTempCold, chEnv=chEnv, boardEnvTempWarm=boardEnvTempWarm, chEnvFanStatus=chEnvFanStatus, boardEnvSlotID=boardEnvSlotID, chEnvAmbientHot=chEnvAmbientHot, chEnvFanTable=chEnvFanTable, boardEnv=boardEnv, chEnvFanID=chEnvFanID, boardEnvTempCold=boardEnvTempCold, chEnvHumidityStatus=chEnvHumidityStatus, psEnvSlotEntry=psEnvSlotEntry, psEnvSlotID=psEnvSlotID, chEnvFanSpeed=chEnvFanSpeed, chEnvHumidity=chEnvHumidity, chEnvAmbientTemp=chEnvAmbientTemp, boardEnvTempHot=boardEnvTempHot, boardEnvTempMaxFanRelHot=boardEnvTempMaxFanRelHot, chEnvAmbientCold=chEnvAmbientCold, psEnvFanAdmin=psEnvFanAdmin, chEnvFanEntry=chEnvFanEntry, chEnvHumidityDry=chEnvHumidityDry, boardEnvTempStatus=boardEnvTempStatus, psEnvSlotTable=psEnvSlotTable, psEnvTempStatus=psEnvTempStatus, chEnvHumidityMoist=chEnvHumidityMoist, chEnvAmbientWarm=chEnvAmbientWarm, boardEnvTempCool=boardEnvTempCool, psEnvTemp=psEnvTemp, psEnvFanStatus=psEnvFanStatus, psEnv=psEnv, boardEnvSlotTable=boardEnvSlotTable, chEnvNumFans=chEnvNumFans, boardEnvSlotEntry=boardEnvSlotEntry, boardEnvTempMaxFanRelWarm=boardEnvTempMaxFanRelWarm, boardEnvTempRelHot=boardEnvTempRelHot, bbuEnv=bbuEnv, chEnvAmbientCool=chEnvAmbientCool, psEnvTempCool=psEnvTempCool, boardEnvTempRelStatus=boardEnvTempRelStatus, psEnvTempWarm=psEnvTempWarm, boardEnvTemp=boardEnvTemp, psEnvFanSpeed=psEnvFanSpeed, boardEnvShutdownAdmin=boardEnvShutdownAdmin, chEnvFanAdmin=chEnvFanAdmin)
